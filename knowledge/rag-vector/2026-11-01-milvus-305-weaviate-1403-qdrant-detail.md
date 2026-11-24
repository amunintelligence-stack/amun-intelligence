# Vector DB delta — Milvus 3.0.5, Weaviate 1.40.3, Qdrant 1.20 independent detail (late Oct 2026)

**Date noted:** 2026-11-01
**Category:** rag-vector — directly relevant: Qdrant 1.20.x is ACI's upgrade target; pgvector is the light fallback

## What changed
- **Milvus 3.0.5 (30 Oct 2026)** is now the current Milvus line (Lite / Standalone / Distributed), per the 1 Nov self-hosted RAG comparison. No breaking change flagged for ACI (Milvus is not adopted; it is a reference engine only).
- **Weaviate 1.40.3 (28 Oct 2026)** is the current Weaviate line. Recalls the 1.40.1 hardened minimum set 2026-10-18 (zlib CVE-2026-85091 + golang x/net CVE-2026-78663 fixes): 1.40.3 supersedes it as the floor for any future Weaviate pilot. Weaviate's GraphQL API deprecation (26 Oct) was already covered 2026-10-28.
- **Qdrant 1.20.0 (22 Oct 2026) — new independent detail:** a 29 Oct technical write-up of the release adds two numbers worth recording:
  - **Turbo16 kept recall@10 within 0.001 of float32** across 12 search-benchmark datasets — i.e. the 4-bit-class TurboQuant storage cut costs roughly half with negligible recall loss in that sweep (vendor-adjacent numbers, treat as signal, not a benchmark).
  - 1.20 adds a **`nested` parameter to every payload index type**, building a per-element index for array elements — directly relevant to ACI payloads that carry multi-valued fields (e.g. lists of entities/tags per chunk).
  - BM25 statistics are computed from the stored text itself and stay current as documents change (no separate sparse-vector pipeline needed for keyword ranking).
- No Qdrant 1.20.1 patch release was found in tonight's check — the "adopt after the 1.20.1 patch window" plan from 2026-10-22 still stands, and the window is still open.

## Why it matters for ACI
- Nothing changes the upgrade plan: Qdrant target stays **1.20.x after the 1.20.1 patch window**; pgvector stays the light fallback; the Postgres-only hybrid path (pg_textsearch BM25 + pg_vectorsearch) stays a comparison candidate.
- The Turbo16 recall figure strengthens the case for enabling TurboQuant at ingest time when the Qdrant upgrade lands, and the `nested` payload index is a concrete schema note for the migration checklist (multi-valued payload fields get per-element indexes instead of whole-array indexes).

## Action: WATCH
1. Keep Qdrant target at 1.20.x; re-check for 1.20.1 before any migration work.
2. Add to the Qdrant migration checklist: enable Turbo16 quantization; use `nested` payload indexes for multi-valued fields.
3. Raise any future Weaviate pilot floor from 1.40.1 to 1.40.3.

## Sources (checked 2026-11-01)
- Self-hosted RAG vector-DB comparison, refreshed 1 Nov 2026: https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/
- Qdrant 1.20 technical detail (29 Oct 2026 capture): https://dev.to/echakiri/qdrant-120-ranks-keyword-matches-inside-the-full-text-index-2i99
- Qdrant 1.20 release post: https://qdrant.tech/blog/qdrant-1.20.x/
- Prior ACI notes: 2026-10-22 (Qdrant 1.20.0 stable), 2026-10-25 (Qdrant vendor announcement), 2026-10-28 (pgvector surge / Weaviate GraphQL sunset)
