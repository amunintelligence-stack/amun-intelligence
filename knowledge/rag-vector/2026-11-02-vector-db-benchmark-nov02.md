# Vector-DB benchmark refresh, 2 Nov 2026: recall defaults + pgvector tuning

**Date noted:** 2026-11-02
**Category:** rag-vector — benchmark evidence (no version change)

## What changed
- Geekflare's open-source vector-DB comparison was **refreshed 2 Nov 2026** with a fixed benchmark: 100,000 OpenAI ada-002 embeddings (1,536-dim, cosine), 1,000 held-out top-10 searches per engine, same cloud server.
  - **Qdrant and Weaviate: 99.3% recall** of the true top 10 at default settings; Weaviate fastest at **4.9 ms median**.
  - **pgvector: 95.4% at defaults → 98.4%** by raising `hnsw.ef_search` from 40 to 100, for under 2 ms extra latency.
  - **Milvus: 94.8% at defaults**, and the heaviest indexer: **2.6 GB peak** for 100k vectors vs 755 MB (Chroma) and under 1 GB (Qdrant, pgvector).
- Independent cross-check (Intelligibberish, updated ~1 Nov 2026) confirms the current versions ACI already tracks: Qdrant **1.20.0** (22 Oct), Milvus **3.0.5** (30 Oct), Weaviate **1.40.3** (28 Oct), Chroma **1.5.9** (May 2026 — no release since), pgvector **0.8.7**. No new vector-DB release tonight.

## Why it matters for ACI
- ACI's RAG is TF-IDF V1 today with Qdrant 1.20.x as the pinned upgrade target — this benchmark supports that plan (best default recall, sub-1 GB indexing) and adds a concrete tuning rule for the fallback: **if pgvector is ever used, `hnsw.ef_search = 100` is not optional** — defaults leave ~4 points of recall on the table.
- The Milvus memory number is a deployment warning for any future Milvus pilot on the ACI VM: 2.6 GB for 100k vectors scales badly against the VM's memory budget.

## Action: WATCH
- No plan change. Record the pgvector `ef_search` rule in the Qdrant-upgrade runbook as the fallback tuning, and keep Qdrant 1.20.x as the upgrade target (after the 1.20.1 patch window, per prior nights).

## Sources (checked 2026-11-02)
- Geekflare benchmark, refreshed 2 Nov 2026: https://geekflare.com/open-source/vector-database/
- Intelligibberish self-hosted comparison, updated ~1 Nov 2026: https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/
- Prior ACI notes: 2026-11-01-milvus-305-weaviate-1403-qdrant-detail.md, 2026-10-22-qdrant-1-20-stable-bm25-hybrid.md
