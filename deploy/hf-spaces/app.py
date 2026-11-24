"""
ACI — AMUN Corporate Intelligence backend.
Serves the frontend, runs OSINT collection missions, stores results in
PostgreSQL when available, else in a SQLite file under ~/workspace/aci/data/
(which survives VM replacements), else in memory.
No external API keys required: DNS, whois, crt.sh (certificate transparency).
"""
import json
import re
import socket
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------- DB ---
# Durable storage: PostgreSQL when available, else SQLite file in the
# workspace (survives VM replacements), else in-memory dicts (lost on restart).
import os as _os
import sqlite3 as _sqlite3

DB_DSN = "dbname=aci user=aci password=aci_local host=127.0.0.1"
SQLITE_PATH = _os.environ.get("ACI_DB_PATH", str(BASE_DIR / "data" / "aci.db"))
_db_ok = False
_db_kind = "memory"  # postgres | sqlite | memory
_mem_store = {}

_PG_SCHEMA = """
CREATE TABLE IF NOT EXISTS missions(
    id SERIAL PRIMARY KEY,
    mission_id TEXT UNIQUE NOT NULL,
    mission TEXT NOT NULL,
    target TEXT NOT NULL,
    status TEXT NOT NULL,
    result JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE IF NOT EXISTS memories(
    id SERIAL PRIMARY KEY,
    fact TEXT NOT NULL,
    domain TEXT DEFAULT 'general',
    created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE IF NOT EXISTS documents(
    id SERIAL PRIMARY KEY,
    source TEXT DEFAULT '',
    chunk TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE IF NOT EXISTS graph_nodes(
    name TEXT PRIMARY KEY,
    ntype TEXT DEFAULT 'entity',
    props JSONB DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS graph_edges(
    src TEXT NOT NULL,
    dst TEXT NOT NULL,
    rel TEXT DEFAULT 'related',
    PRIMARY KEY (src, dst, rel)
);
"""

_SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS missions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mission_id TEXT UNIQUE NOT NULL,
    mission TEXT NOT NULL,
    target TEXT NOT NULL,
    status TEXT NOT NULL,
    result TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS memories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT NOT NULL,
    domain TEXT DEFAULT 'general',
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS documents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT DEFAULT '',
    chunk TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS graph_nodes(
    name TEXT PRIMARY KEY,
    ntype TEXT DEFAULT 'entity',
    props TEXT DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS graph_edges(
    src TEXT NOT NULL,
    dst TEXT NOT NULL,
    rel TEXT DEFAULT 'related',
    PRIMARY KEY (src, dst, rel)
);
"""

def _pg_connect():
    import psycopg2
    return psycopg2.connect(DB_DSN)

def _sqlite_connect():
    _os.makedirs(_os.path.dirname(SQLITE_PATH), exist_ok=True)
    c = _sqlite3.connect(SQLITE_PATH, timeout=30)
    c.execute("PRAGMA journal_mode=WAL")
    return c

def db():
    """Connect: PostgreSQL first, SQLite file fallback. Sets _db_kind."""
    global _db_kind
    try:
        c = _pg_connect()
        _db_kind = "postgres"
        return c
    except Exception:
        pass
    c = _sqlite_connect()
    _db_kind = "sqlite"
    return c

def _ph(query):
    """Translate %s placeholders to ? for SQLite."""
    return query.replace("%s", "?") if _db_kind == "sqlite" else query

def _init_schema(c):
    cur = c.cursor()
    schema = _SQLITE_SCHEMA if _db_kind == "sqlite" else _PG_SCHEMA
    for stmt in schema.strip().split(";"):
        if stmt.strip():
            cur.execute(stmt)
    c.commit()

def db_init():
    global _db_ok, _db_kind
    try:
        c = db()
        _init_schema(c)
        c.close()
        _db_ok = True
        print(f"DB ready (kind={_db_kind})")
    except Exception as e:
        print("DB unavailable, using memory store:", e)
        _db_ok = False
        _db_kind = "memory"

def _as_iso(v):
    return v if isinstance(v, str) else v.isoformat()

def _as_json(v):
    if v is None or isinstance(v, dict):
        return v
    try:
        return json.loads(v)
    except Exception:
        return v

_mem_memories = []
_mem_docs = []
_mem_gnodes = {}
_mem_gedges = []

def db_save(mission_id, mission, target, status, result):
    rec = {"mission_id": mission_id, "mission": mission, "target": target,
           "status": status, "result": result,
           "created_at": datetime.now(timezone.utc).isoformat()}
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute(_ph(
                """INSERT INTO missions(mission_id, mission, target, status, result)
                   VALUES(%s,%s,%s,%s,%s)
                   ON CONFLICT (mission_id) DO UPDATE
                   SET status=EXCLUDED.status, result=EXCLUDED.result"""),
                (mission_id, mission, target, status, json.dumps(result)))
            c.commit(); c.close(); return rec
        except Exception as e:
            print("DB save failed:", e)
    _mem_store[mission_id] = rec
    return rec

def db_list(limit=20):
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute(_ph("SELECT mission_id, mission, target, status, created_at FROM missions ORDER BY id DESC LIMIT %s"), (limit,))
            rows = [{"mission_id": r[0], "mission": r[1], "target": r[2], "status": r[3],
                     "created_at": _as_iso(r[4])} for r in cur.fetchall()]
            c.close(); return rows
        except Exception as e:
            print("DB list failed:", e)
    return list(reversed(list(_mem_store.values())))[-limit:]

def db_get(mission_id):
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute(_ph("SELECT mission_id, mission, target, status, result, created_at FROM missions WHERE mission_id=%s"), (mission_id,))
            r = cur.fetchone(); c.close()
            if r:
                return {"mission_id": r[0], "mission": r[1], "target": r[2], "status": r[3],
                        "result": _as_json(r[4]), "created_at": _as_iso(r[5])}
        except Exception as e:
            print("DB get failed:", e)
    return _mem_store.get(mission_id)

# ------------------------------------------------------------- OSINT ---
# NOTE: local DNS in this sandbox is intercepted by the egress proxy
# (everything resolves to a proxy IP), so all collection goes through
# HTTPS APIs: DNS-over-HTTPS (Cloudflare/Google) + hackertarget free tier.

DOH_URLS = [
    "https://cloudflare-dns.com/dns-query",
    "https://dns.google/resolve",
]
HT = "https://api.hackertarget.com"

def extract_domain(target):
    t = target.strip().lower()
    t = re.sub(r"^https?://", "", t)
    t = t.split("/")[0].split(":")[0]
    t = t.split("?")[0]
    return t if re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", t) else None

def doh_lookup(domain, rtype):
    for base in DOH_URLS:
        try:
            r = requests.get(base, params={"name": domain, "type": rtype},
                             headers={"accept": "application/dns-json"}, timeout=12)
            data = r.json()
            if data.get("Status") == 0:
                return [a["data"].strip('"') for a in data.get("Answer", []) if a.get("type") in (1, 2, 5, 15, 16, 28)]
        except Exception:
            continue
    return []

def dns_lookup(domain):
    return {
        "A": doh_lookup(domain, "A"),
        "MX": doh_lookup(domain, "MX"),
        "NS": doh_lookup(domain, "NS"),
        "TXT": doh_lookup(domain, "TXT"),
    }

def ht_get(path, q):
    try:
        r = requests.get(f"{HT}{path}", params={"q": q}, timeout=15)
        txt = r.text.strip()
        if r.status_code == 200 and txt and "error" not in txt.lower()[:60]:
            return txt
    except Exception:
        pass
    return ""

def whois_lookup(domain):
    txt = ht_get("/whois/", domain)
    if not txt:
        return {"error": "whois unavailable"}
    out = {}
    for line in txt.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip().lower()
            if k in ("registrar", "creation date", "registry expiry date", "registrant organization", "registrant country"):
                out[k] = v.strip()
    out["raw_lines"] = len(txt.splitlines())
    return out

def subdomains_lookup(domain, limit=60):
    txt = ht_get("/hostsearch/", domain)
    subs = []
    for line in txt.splitlines():
        parts = line.split(",")
        if parts:
            subs.append(parts[0].strip().lower())
    seen = []
    for s in subs:
        if s and s not in seen:
            seen.append(s)
    return seen[:limit]

MISSION_LABELS = {
    "corporate": "استخبارات الشركات",
    "due_diligence": "الفحص النافي للجهالة",
    "competitive": "استخبارات المنافسين",
    "market": "استخبارات الأسواق",
    "risk": "استخبارات المخاطر",
    "cyber": "الاستخبارات السيبرانية",
}

def _collect_parallel(domain):
    """Pattern 03 — Parallelization: independent I/O collectors run concurrently."""
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as ex:
        f_dns = ex.submit(dns_lookup, domain)
        f_whois = ex.submit(whois_lookup, domain)
        f_subs = ex.submit(subdomains_lookup, domain)
        return f_dns.result(), f_whois.result(), f_subs.result()

def _score_confidence(evidence):
    return round(min(0.9, 0.65 + 0.05 * len([e for e in evidence if e])), 2)

def run_mission(mission, target, context):
    """Pattern 01 — Prompt Chaining: extract → collect → analyze → synthesize.
       Pattern 05 — Evaluator-Optimizer: score, then one bounded optimization pass."""
    t0 = time.time()
    evidence = []
    domain = extract_domain(target)
    optimized = False

    def collect(d):
        dns, w, subs = _collect_parallel(d)
        ev = [f"النطاق المستخرج من الهدف: {d}",
              f"سجلات DNS — A: {len(dns['A'])}, MX: {len(dns['MX'])}, NS: {len(dns['NS'])}, TXT: {len(dns['TXT'])}"]
        if w.get("registrar"):
            ev.append(f"المسجل: {w['registrar']} | الإنشاء: {w.get('creation date')} | الانتهاء: {w.get('registry expiry date')}")
        ev.append(f"نطاقات فرعية مرصودة: {len(subs)}")
        return dns, w, subs, ev

    if domain:
        dns, w, subs, ev = collect(domain)
        evidence.extend(ev)
        # apex fallback: subdomains often publish almost nothing; the zone apex
        # holds NS/SOA and usually MX/TXT. Check it automatically when sparse.
        apex_info = None
        parts = domain.split(".")
        if len(parts) > 2:
            apex = ".".join(parts[-2:])
            try:
                apex_dns = dns_lookup(apex)
                if any(apex_dns.values()):
                    apex_info = {"domain": apex, "dns": apex_dns}
                    evidence.append(
                        f"فحص الدومين الأساسي {apex} تلقائياً — "
                        f"NS: {len(apex_dns['NS'])}, MX: {len(apex_dns['MX'])}, TXT: {len(apex_dns['TXT'])}"
                    )
            except Exception:
                pass
    else:
        dns, w, subs, apex_info = {}, {}, [], None
        evidence.append("الهدف ليس نطاقاً قابلاً للحل — تم تخطي جمع DNS المباشر (استخدم اسم النطاق الرسمي للدقة الكاملة).")

    # ---- Pattern 05: evaluate, then optimize once if weak ----
    confidence = _score_confidence(evidence)
    if domain and confidence < 0.75:
        # optimization pass: deepen subdomain search + retry collectors once
        try:
            subs2 = subdomains_lookup(domain, limit=120)
            if len(subs2) > len(subs):
                subs = subs2
                evidence.append(f"تحسين: تعميق البحث كشف {len(subs)} نطاقاً فرعياً")
            optimized = True
        except Exception:
            pass
        confidence = _score_confidence(evidence)

    # ---- risk signals ----
    risks = []
    if domain:
        try:
            cd = str(w.get("creation date") or "")
            m = re.search(r"(\d{4})", cd)
            if m and int(m.group(1)) >= datetime.now().year - 1:
                risks.append("النطاق حديث التسجيل (أقل من سنة) — يتطلب حذراً إضافياً في التعامل.")
        except Exception:
            pass
        if not dns.get("MX"):
            risks.append("لا توجد سجلات بريد (MX) — قد يشير لنطاق غير تشغيلي أو بنية غير مكتملة.")
        if len(subs) > 40:
            risks.append(f"بنية تحتية واسعة ({len(subs)} نطاقاً فرعياً) — سطح هجوم رقمي كبير يستحق المراجعة.")
    if not risks:
        risks.append("لا توجد مؤشرات خطر حرجة من الفحص الآلي — يُنصح بمراجعة بشرية قبل القرار النهائي.")

    opportunities = [
        "استكمال الفحص بمصادر OSINT إضافية (سجلات الشركات، الأخبار، التواصل الاجتماعي).",
        "بناء خط أساس للمراقبة المستمرة (تغيرات DNS/الشهادات كمؤشر مبكر).",
    ]
    options = [
        "اعتماد النتائج كمؤشر أولي والمضي قدماً مع ضوابط.",
        "طلب فحص معمّق (Due Diligence كامل) قبل أي التزام.",
        "تأجيل القرار لحين استكمال مصادر إضافية.",
    ]

    elapsed = round(time.time() - t0, 1)

    # persist entities to the graph (Pattern: Graph DB)
    try:
        if domain:
            graph_add([{"name": domain, "ntype": "domain"},
                       {"name": target, "ntype": "target"}],
                      [{"src": target, "dst": domain, "rel": "resolves_to"}])
            for s in subs[:20]:
                graph_add([{"name": s, "ntype": "subdomain"}],
                          [{"src": domain, "dst": s, "rel": "has_subdomain"}])
    except Exception:
        pass

    return {
        "mission_label": MISSION_LABELS.get(mission, mission),
        "target": target,
        "domain": domain,
        "situation": f"فحص استخباراتي ({MISSION_LABELS.get(mission, mission)}) للهدف «{target}» اكتمل في {elapsed} ثانية عبر {len(evidence)} مصدر دليل.",
        "evidence": evidence,
        "details": {"dns": dns, "whois": w, "subdomains": subs[:60], "apex": apex_info},
        "risk": risks,
        "opportunity": opportunities,
        "options": options,
        "confidence": confidence,
        "optimized": optimized,
        "elapsed_s": elapsed,
    }

# ------------------------------------------------- Memory / RAG / Graph ---
def _tfidf_search(corpus, query, top_k=5):
    """V1 semantic search: TF-IDF + cosine. Upgrade path: pgvector/Qdrant."""
    if not corpus or not query.strip():
        return []
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    texts = [c[0] for c in corpus]
    try:
        vec = TfidfVectorizer().fit_transform(texts + [query])
        sims = cosine_similarity(vec[-1], vec[:-1])[0]
        ranked = sorted(zip(corpus, sims), key=lambda x: x[1], reverse=True)
        return [{"text": c[0], "meta": c[1], "score": round(float(s), 3)}
                for c, s in ranked[:top_k] if s > 0]
    except Exception:
        return []

# --- Memory ---
def memory_add(fact, domain="general"):
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute(_ph("INSERT INTO memories(fact, domain) VALUES(%s,%s)"), (fact, domain))
            c.commit(); c.close(); return True
        except Exception as e:
            print("memory_add failed:", e)
    _mem_memories.append({"fact": fact, "domain": domain})
    return True

def memory_recall(query, domain=None, top_k=5):
    corpus = []
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            if domain:
                cur.execute(_ph("SELECT fact, domain FROM memories WHERE domain=%s ORDER BY id DESC LIMIT 500"), (domain,))
            else:
                cur.execute("SELECT fact, domain FROM memories ORDER BY id DESC LIMIT 500")
            corpus = [(r[0], {"domain": r[1]}) for r in cur.fetchall()]
            c.close()
        except Exception as e:
            print("memory_recall failed:", e)
    if not corpus:
        items = _mem_memories if not domain else [m for m in _mem_memories if m["domain"] == domain]
        corpus = [(m["fact"], {"domain": m["domain"]}) for m in items[-500:]]
    return _tfidf_search(corpus, query, top_k)

# --- RAG ---
def rag_ingest(source, chunks):
    if isinstance(chunks, str):
        chunks = [chunks]
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            for ch in chunks:
                if ch.strip():
                    cur.execute(_ph("INSERT INTO documents(source, chunk) VALUES(%s,%s)"), (source, ch.strip()))
            c.commit(); c.close(); return len(chunks)
        except Exception as e:
            print("rag_ingest failed:", e)
    for ch in chunks:
        if ch.strip():
            _mem_docs.append({"source": source, "chunk": ch.strip()})
    return len(chunks)

def rag_query(query, top_k=5):
    corpus = []
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute("SELECT chunk, source FROM documents ORDER BY id DESC LIMIT 1000")
            corpus = [(r[0], {"source": r[1]}) for r in cur.fetchall()]
            c.close()
        except Exception as e:
            print("rag_query failed:", e)
    if not corpus:
        corpus = [(d["chunk"], {"source": d["source"]}) for d in _mem_docs[-1000:]]
    return _tfidf_search(corpus, query, top_k)

# --- Graph ---
def graph_add(nodes, edges):
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            for n in nodes:
                cur.execute(_ph(
                    """INSERT INTO graph_nodes(name, ntype, props) VALUES(%s,%s,%s)
                       ON CONFLICT (name) DO UPDATE SET props=EXCLUDED.props"""),
                    (n["name"], n.get("ntype", "entity"), json.dumps(n.get("props", {}))))
            for e in edges:
                cur.execute(_ph(
                    """INSERT INTO graph_edges(src, dst, rel) VALUES(%s,%s,%s) ON CONFLICT DO NOTHING"""),
                    (e["src"], e["dst"], e.get("rel", "related")))
            c.commit(); c.close(); return True
        except Exception as e:
            print("graph_add failed:", e)
    for n in nodes:
        _mem_gnodes[n["name"]] = n
    _mem_gedges.extend(edges)
    return True

def _graph_snapshot():
    import networkx as nx
    g = nx.DiGraph()
    if _db_ok:
        try:
            c = db(); cur = c.cursor()
            cur.execute("SELECT name, ntype FROM graph_nodes")
            for name, ntype in cur.fetchall():
                g.add_node(name, ntype=ntype)
            cur.execute("SELECT src, dst, rel FROM graph_edges")
            for s, d, r in cur.fetchall():
                g.add_edge(s, d, rel=r)
            c.close(); return g
        except Exception as e:
            print("graph snapshot failed:", e)
    for name, n in _mem_gnodes.items():
        g.add_node(name, ntype=n.get("ntype"))
    for e in _mem_gedges:
        g.add_edge(e["src"], e["dst"], rel=e.get("rel"))
    return g

def graph_neighbors(node, depth=1):
    import networkx as nx
    g = _graph_snapshot()
    if node not in g:
        return []
    seen, frontier, out = {node}, [node], []
    for _ in range(depth):
        nxt = []
        for n in frontier:
            for nb in list(g.successors(n)) + list(g.predecessors(n)):
                if nb not in seen:
                    seen.add(nb); nxt.append(nb)
                    out.append({"node": nb, "ntype": g.nodes[nb].get("ntype")})
        frontier = nxt
    return out

def graph_path(src, dst):
    import networkx as nx
    g = _graph_snapshot()
    try:
        return nx.shortest_path(g.to_undirected(), src, dst)
    except Exception:
        return []

# ---------------------------------------------------------------- API ---
class MissionIn(BaseModel):
    mission: str = "corporate"
    target: str = ""
    context: dict = {}
    mission_id: str | None = None

app = FastAPI(title="ACI — AMUN Corporate Intelligence")

@app.on_event("startup")
def _startup():
    db_init()

@app.get("/healthz")
def healthz():
    return {"ok": True, "db": _db_ok, "db_kind": _db_kind, "time": datetime.now(timezone.utc).isoformat()}

@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse(str(BASE_DIR / "static" / "index.html"))

@app.get("/console", response_class=HTMLResponse)
def console():
    return FileResponse(str(BASE_DIR / "console.html"))

@app.post("/api/v1/run")
def api_run(m: MissionIn):
    if not m.target.strip():
        raise HTTPException(400, "target مطلوب")
    mission_id = m.mission_id or f"aci_{int(time.time()*1000)}"
    db_save(mission_id, m.mission, m.target, "running", None)
    try:
        result = run_mission(m.mission, m.target, m.context)
        rec = db_save(mission_id, m.mission, m.target, "completed", result)
        return JSONResponse({"mission_id": mission_id, "status": "completed", **result})
    except Exception as e:
        db_save(mission_id, m.mission, m.target, "failed", {"error": str(e)[:500]})
        raise HTTPException(500, str(e)[:500])

# n8n compatibility: the trigger workflow posts {mission...} wrapped as {mission:{...}}
@app.post("/api/v1/missions/run")
def api_run_wrapped(body: dict):
    inner = body.get("mission", body)
    return api_run(MissionIn(**{k: inner.get(k) for k in ("mission", "target", "context", "mission_id") if k in inner}))

@app.get("/api/v1/missions")
def api_list(limit: int = 20):
    return {"missions": db_list(limit)}

@app.get("/api/v1/missions/{mission_id}")
def api_get(mission_id: str):
    rec = db_get(mission_id)
    if not rec:
        raise HTTPException(404, "mission not found")
    return rec

# ------------------------------------------------- Memory / RAG / Graph API ---
class MemoryIn(BaseModel):
    fact: str
    domain: str = "general"

@app.post("/api/v1/memory")
def api_memory_add(m: MemoryIn):
    if not m.fact.strip():
        raise HTTPException(400, "fact مطلوب")
    memory_add(m.fact.strip(), m.domain)
    return {"ok": True}

@app.get("/api/v1/memory/recall")
def api_memory_recall(q: str, domain: str | None = None, top_k: int = 5):
    return {"results": memory_recall(q, domain, top_k)}

class RagIn(BaseModel):
    source: str = ""
    chunks: list[str] = []

@app.post("/api/v1/rag/ingest")
def api_rag_ingest(r: RagIn):
    n = rag_ingest(r.source, r.chunks)
    return {"ok": True, "ingested": n}

@app.post("/api/v1/rag/query")
def api_rag_query(body: dict):
    return {"results": rag_query(body.get("q", ""), int(body.get("top_k", 5)))}

class GraphIn(BaseModel):
    nodes: list[dict] = []
    edges: list[dict] = []

@app.post("/api/v1/graph/add")
def api_graph_add(g: GraphIn):
    graph_add(g.nodes, g.edges)
    return {"ok": True}

@app.get("/api/v1/graph/neighbors")
def api_graph_neighbors(node: str, depth: int = 1):
    return {"neighbors": graph_neighbors(node, depth)}

@app.get("/api/v1/graph/path")
def api_graph_path(src: str, dst: str):
    return {"path": graph_path(src, dst)}
