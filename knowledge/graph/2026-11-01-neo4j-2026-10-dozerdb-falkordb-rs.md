# Graph delta — Neo4j 2026.10.0, DozerDB matching release, falkordb-rs 0.11.0 (late Oct 2026)

**Date noted:** 2026-11-01
**Category:** graph — reference only: ACI graph stays networkx in-memory + Postgres snapshots

## What changed
- **Neo4j 2026.10.0 released 20 Oct 2026** (calendar line; Java 21 required), per the Neo4j community release thread. It follows 2026.09.0 (22 Sep). The 2026.09 behavioural notes already on record still apply as cautions for the calendar line: page cache reserves full configured memory at startup; Cypher 25 SEARCH accepts FULLTEXT INDEX; skip 2026.07.0 (UTF-8 trim regression) and 2026.08.0 (query failures).
- **DozerDB v2026.10.0.0 (28 Oct 2026)** — the free GPL plugin that adds enterprise-style features to Neo4j Community Edition — shipped a matching build for Neo4j CE 2026.10, plus v5.26.32.0 for the 5.26 LTS line. Every release file ships with a .sha256 checksum. DozerDB is independent of Neo4j, Inc.
- **falkordb-rs 0.11.0 (26 Oct 2026)** — already recorded in ACI's 28 Oct cycle (Rust client only, no engine change); repeated here for completeness: replica-aware read routing (opt-in, behind Redis Sentinel), batching, TLS, automatic retries, OpenTelemetry-aligned tracing/metrics. Engine pin stays **6.0.3**.
- A 21 Oct DEV analysis ("why I'd think twice before picking Neo4j for a GraphRAG stack") argues the mismatch is workload, not quality: Neo4j is built for stable, structured relationship data and analyst dashboards, while agentic GraphRAG needs single-digit-millisecond multi-hop + vector-fused lookups at high frequency; it shortlists ArcadeDB (multi-model + built-in MCP server), FalkorDB (latency), ArangoDB (multi-model), and Memgraph (C++ in-memory, Bolt-compatible). Vendor/analyst framing, not a benchmark — but it aligns with ACI's own stance of keeping the graph layer light (networkx) until a real scale trigger appears.

## Why it matters for ACI
- No engine change: networkx + Postgres snapshots remain the right weight for ACI's mission graphs. The Neo4j calendar line and DozerDB matter only if a future managed-Neo4j decision is revisited — in which case 2026.10 + DozerDB 2026.10.0.0 is the current pairing to evaluate, with the page-cache-at-startup behaviour as a sizing note.
- falkordb-rs 0.11.0 is worth noting for the FalkorDB candidate file: replica-aware reads + tracing close two operational gaps (read scaling, observability) that previously counted against it.
- The DEV piece reinforces the standing rule: if ACI ever needs graph + vector fused retrieval at agent speed, evaluate FalkorDB/ArcadeDB on ACI's own data rather than defaulting to Neo4j on familiarity.

## Action: WATCH
1. No adoption. Update the FalkorDB candidate note with falkordb-rs 0.11.0 (replica-aware reads, OTel tracing).
2. If Neo4j is ever revisited: evaluate 2026.10 (+ DozerDB 2026.10.0.0) with the page-cache sizing caveat.

## Sources (checked 2026-11-01)
- Neo4j 2026 release thread (2026.10.0, 20 Oct 2026): https://community.neo4j.com/t/neo4j-2026-releases/76512
- DozerDB current releases (28 Oct 2026): http://dozerdb.org/
- falkordb-rs releases (0.11.0, 26 Oct 2026): https://lib.rs/crates/falkordb
- Neo4j-vs-GraphRAG analysis (21 Oct 2026): https://dev.to/techanalysisinsights/why-id-think-twice-before-picking-neo4j-for-a-graphrag-stack-in-2026-1jb7
- Prior ACI notes: 2026-10-22-falkordb-6-0-oct-update.md, 2026-10-23 (FalkorDB 6.0.3 pin), 2026-10-12-neo4j-2026.09.md
