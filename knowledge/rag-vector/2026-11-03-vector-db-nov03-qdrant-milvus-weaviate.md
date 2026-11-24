# Vector-DB November snapshot — Qdrant 1.20.0, Milvus 3.0.5, Weaviate 1.40.3, pg_pinecone

## What changed
- **Qdrant v1.20.0** (22 Oct 2026, confirmed in two independent Oct/Nov comparisons): native BM25 full-text ranking, single-query dense+keyword hybrid, ACORN filtering, code-identifier normalization. Still the upgrade target (1.19.2 → 1.20.x) after the 1.20.1 patch window — note: no 1.20.1 found in tonight's sources; 1.20.0 remains the latest cited.
- **Milvus v3.0.5** (30 Oct 2026): latest 3.x patch; heaviest indexer in the 2 Nov Geekflare bench (2.6 GB per 100k embeddings) — VM-budget warning stands.
- **Weaviate v1.40.3** (28 Oct 2026): follows 1.40.1 (zlib CVE-2026-85091 + x/net CVE-2026-78663 fixes). GraphQL API deprecated 26 Oct, off Cloud 1 May 2027 — not our stack, but a deprecation-planning reference.
- **Pinecone pg_pinecone** (reported 27 Oct 2026): open-source Postgres extension bringing Pinecone's engine to pgvector columns — a Postgres-native hybrid path to compare against the Qdrant plan, not a replacement.
- **Benchmark refresh** (Geekflare, 2 Nov 2026; 100k ada-002 embeddings, 1k queries): Qdrant + Weaviate 99.3% recall@10 at defaults, Weaviate fastest (4.9 ms median); pgvector 95.4% → 98.4% with `hnsw.ef_search` 40 → 100 (<2 ms cost). Chroma still 1.5.9 (May 2026) — no release since.
- pgvector 0.8.7 stands; Oct-1 buffer-overflow patch hygiene (backend recycle) already in the runbook.

## Why it matters for ACI
- No change to the plan: Qdrant 1.20.x after the 1.20.1 patch window; pgvector as light fallback with `ef_search=100` tuning rule (recorded 2 Nov). Milvus stays out on VM budget. pg_pinecone is worth one eval note for the Postgres-only hybrid path (Tiger Data pg_vectorsearch/pg_textsearch comparison from 22 Oct).
- Weaviate's GraphQL sunset is a cautionary pattern for ACI's own API surface: deprecate with a dated off-ramp, not a silent removal.

## Sources
- https://geekflare.com/open-source/vector-database/ (refreshed 2 Nov 2026, benchmark + versions)
- https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/ (Oct 2026, Qdrant 1.20.0 / Milvus 3.0.5 / Weaviate 1.40.3 table)
- https://tech-insider.org/ca/vector-database-comparison-pinecone-qdrant-weaviate-milvus-pgvector-2026/ (28 Oct 2026, pg_pinecone + GraphQL sunset)

## Action
- **Watch**: Qdrant 1.20.1 (patch window gate for the upgrade); pg_pinecone eval note for the Postgres-only hybrid comparison.
- **Adopt (practice)**: pgvector fallback tuning `hnsw.ef_search=100` already recorded — keep.
