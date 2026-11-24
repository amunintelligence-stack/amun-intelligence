# ACI Architecture — the 5 patterns, and where each one lives

> Rule: every new capability in this system must map to at least one pattern below.
> If it doesn't fit, the design is wrong — not the pattern list.

## 01 — Prompt Chaining
**Where:** `app.py :: run_mission()` — the mission pipeline is a chain:
`extract_domain → dns_lookup → whois_lookup → subdomains_lookup → risk_analysis → report_build`.
Each step's output feeds the next; each step is independently testable and replaceable.
**n8n mirror:** Webhook → Validate → Dispatch → Report (the trigger workflow).

## 02 — Routing
**Where:** mission → agent roster + collector set.
- n8n `✅ تحقق وبناء المهمة` node: `MISSIONS` table routes each mission type
  (corporate / due_diligence / competitive / market / risk / cyber) to its agent roster.
- Backend `MISSION_LABELS` + per-mission collector selection (domain missions get
  DNS/whois/subdomain collectors; other targets get the generic path).
**Rule:** routing decisions are data (tables), never hard-coded branches.

## 03 — Parallelization
**Where:** `app.py :: collect_all()` — DNS, whois, and subdomain lookups run
concurrently via `ThreadPoolExecutor` (they are independent I/O).
**Rule:** anything I/O-bound and independent runs in parallel; the chain only
sequences what has true data dependencies.

## 04 — Orchestrator-Workers
**Where:** the backend *is* the orchestrator; collectors are workers.
- Orchestrator owns: mission lifecycle (running → completed/failed), budgets
  (max 45 min / token budget documented per mission), persistence, and final synthesis.
- Workers own: one collection task each, with timeouts, returning evidence items.
- n8n is the outer orchestrator (trigger + delivery); the backend is the inner
  orchestrator (collection + synthesis). Neither reaches into the other's internals.
**Multi-agent upgrade path:** workers become subagents following
`workflow_0_mex6_v2.json` (message protocol, loop guards, arbitration).

## 05 — Evaluator-Optimizer
**Where:** `app.py :: evaluate_and_optimize()`.
- **Evaluate:** after collection, confidence is scored (0.65 base + 0.05/evidence,
  capped 0.90) and risks are extracted as structured signals.
- **Optimize:** if confidence < 0.75, the optimizer widens collection
  (adds extra subdomain depth + retries failed collectors once) and re-scores.
  Max 1 optimization pass — bounded, never infinite.
- The final report always carries the confidence score and the evidence list,
  so a human (or downstream agent) can audit the evaluation.

## Cross-cutting
- **Memory:** every mission, fact, and evaluation is persisted (Postgres) and
  recallable — the system learns across missions, not just within one.
- **RAG:** reports and ingested documents are retrievable by semantic similarity
  to ground future missions.
- **Graph:** entities (domains, orgs, people, IPs) and relations persist as a
  graph for entity-resolution queries ("what connects X to Y?").
- **Observability:** healthz + mission log + watchdog cron = the system watches itself.
- **Registry:** `registry/tools.yaml` is the single catalog — add there first,
  wire code second.

## What "highest result" means here
Not more tools — **tighter loops**: route correctly → collect in parallel →
evaluate honestly → optimize once → persist everything → recall next time.
