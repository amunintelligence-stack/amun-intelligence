# Vector-DB snapshot, October 2026: versions, staleness signal, benchmark

## What changed
- October 2026 self-hosted RAG comparison (intelligibberish, updated ~Oct 18, 2026)
  pins current verified releases: Qdrant v1.19.2 (2026-10-05), Milvus v3.0.3
  (2026-10-14), Chroma 1.5.x line (`latest` tag shipping 1.5.10.dev324), Weaviate
  v1.40.1 (2026-10-13), pgvector v0.8.7, LanceDB v0.40.0 (2026-10-07).
- Staleness signal: Chroma has shipped no tagged release since May 5, 2026 despite
  daily commits (bestfreewebresources, Oct 2026). Weaviate's repo remains split-license
  (BSD-3-Clause outside `wl/`, Weaviate Enterprise License inside `wl/`).
- Benchmark (SearchBlox Index Server, Oct 2026, Graviton c8g.4xlarge, 20k x 384-dim,
  recall vs exact brute force): Qdrant 1.19 fastest raw ANN query (kNN k=10 p50
  2.83 ms, recall@10 1.00); Weaviate 10.07 ms / 0.99; Chroma 9.94 ms / 0.99 with
  ~35 ms filtered kNN — Chroma's documented post-filtering behavior at that
  selectivity. Index Server led ingest (4,221 docs/s vs Qdrant 3,436).
- Note for the Qdrant plan: this snapshot predates the Qdrant 1.20.0 stable release
  already recorded by the Oct 22 nightly (native BM25 + single-query hybrid) — 1.19.2
  here is the prior line, not a regression.

## Why it matters for ACI
- Confirms the standing plan with no change: Qdrant 1.20.x stays the upgrade target
  (after the 1.20.1 patch window); pgvector stays the light fallback. The benchmark
  reinforces that filtered queries are where engines diverge — ACI's hybrid stage
  must benchmark filtered kNN on its own corpus, not raw ANN latency.
- Chroma's 5-month release drought strengthens the existing "ignore for current stack"
  stance (it already carries a recorded CVE-2026-85664 reference). No new engine
  enters the plan from this snapshot.

## Sources
- intelligibberish, "Best vector databases for self-hosted RAG (October 2026)":
  https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/
- bestfreewebresources, "Best Vector Database for Local RAG in 2026", Oct 2026:
  https://www.bestfreewebresources.com/best-vector-database-local-rag-2026
- SearchBlox Index Server benchmarks, Oct 2026:
  https://index-server.searchblox.com/benchmarks.html

## Action
- WATCH (no plan change). When the Qdrant 1.20.x upgrade is attempted, include a
  filtered-kNN benchmark on ACI data in the acceptance check; keep Chroma out of
  the plan.
