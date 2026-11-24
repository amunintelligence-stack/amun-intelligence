# RuVector commercially launched by Cognitum One (2026-10-20)

## What changed
Cognitum One commercially launched **RuVector** on 2026-10-20 (open-source Rust engine, previously open project): vector search (HNSW with SIMD, sub-ms queries), a **Cypher-compatible knowledge graph**, and self-learning agent memory in one engine. Runs on a server, **inside PostgreSQL**, in the browser, and at the edge. Claims 500,000+ downloads/month across npm and crates.io and 4,400+ GitHub stars. Roles are distinct: Ruflo coordinates agents, ruOS provides governed compute, RuVector is the memory.

## Why it matters for ACI
ACI currently splits memory across TF-IDF/SQLite RAG, networkx graphs and Postgres persistence. RuVector's pitch — similarity search + graph traversal + memory with "which answers worked before" feedback, in one engine that runs inside Postgres — is exactly the consolidation candidate for ACI's memory tier, and the Postgres-embeddable story fits ACI's 3-tier persistence design. Download volume suggests real adoption, but commercial claims are vendor-issued and unverified.

## Sources (with dates)
- Morningstar / ACCESS Newswire release, 2026-10-20: https://www.morningstar.com/news/accesswire/1238912msn/cognitum-one-launches-commercial-ruvector-the-self-learning-database-giving-ai-agents-memory-that-persists-connects-and-improves
- cognitum.one/ruvector product page.

## Action
watch
