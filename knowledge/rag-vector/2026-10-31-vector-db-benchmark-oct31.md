# Vector DB benchmark refresh — 31 Oct 2026 (Geekflare, 100k embeddings)

**Date noted:** 2026-10-31
**Category:** rag-vector / store selection

## What changed
- Geekflare refreshed its open-source vector DB comparison on **31 Oct 2026**: 100,000 OpenAI `text-embedding-ada-002` embeddings (1,536 dims, cosine) loaded into Qdrant, Milvus, Weaviate, Chroma and pgvector on one cloud server, 1,000 held-out top-10 searches each.
- Results:
  - **Qdrant and Weaviate: 99.3% recall** of the true top 10 with default settings — joint best.
  - **Weaviate fastest**: median **4.9 ms** per search.
  - **pgvector**: raising `hnsw.ef_search` from 40 to 100 lifted recall to **98.4%** for under 2 ms extra per search — i.e. pgvector is within ~1 point of the dedicated engines once tuned, at zero extra infrastructure.
  - All five returned the same top five as an exact search for the sample query.
- Corroborating October snapshots (same week): Qdrant v1.19.2 (5 Oct) → v1.20.0 with BM25 hybrid search; Weaviate v1.40.1 (13 Oct); pgvector v0.8.7 (1 Oct); Milvus v3.0.3 (14 Oct); LanceDB v0.40.0 (7 Oct). Chroma's `latest` tag sits on the 1.5.x line (May 2026 release line) — the stalest of the five.
- Caveat from the parallel tech-insider comparison (28 Oct): **no neutral apples-to-apples benchmark of all five engines exists** in the October material — vendor numbers are signals, not a leaderboard. Geekflare's run is at least a single-harness, same-data test, which is better than vendor claims but still one harness.

## Why it matters for ACI
- ACI's RAG store is Postgres/TF-IDF v1 today, with the Qdrant 1.20.x plan already on record (2026-10-25) and pg_pinecone noted as an isolated-pilot-only option (2026-10-30). This benchmark **does not overturn that plan**: Qdrant stays the self-hosted pick for filtered, hybrid search at scale.
- It does strengthen the pgvector fallback case: for a modest corpus, tuned pgvector (ef_search 100) is within ~1 recall point of Qdrant, with vectors, filters and joins in the one Postgres ACI already operates. If Qdrant adoption stalls, pgvector + Postgres full-text is a credible interim, not a downgrade.
- Weaviate's speed lead comes with the GraphQL API retirement already tracked (26 Oct deprecation) — do not let a median-latency win pull a GraphQL dependency into the stack.

## Sources
- Benchmark refresh, data refreshed 31 Oct 2026: https://geekflare.com/open-source/vector-database/
- Self-hosted comparison, versions verified Oct 2026: https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/
- Five-engine comparison, 28 Oct 2026: https://tech-insider.org/ca/vector-database-comparison-pinecone-qdrant-weaviate-milvus-pgvector-2026/

## Action: WATCH
- No change: Qdrant 1.20.x remains the planned vector upgrade; pgvector (ef_search 100) is now the documented fallback with a measured ~98.4% recall figure. Re-check only if ACI's corpus passes ~5M vectors or needs sparse/multi-vector search at scale.
