# GraphRAG engine choice, Oct 2026: Neo4j questioned, ArcadeDB/FalkorDB/Memgraph pitched

## What changed
- dev.to analysis (Oct 21, 2026), "Why I'd Think Twice Before Picking Neo4j for a
  GraphRAG Stack in 2026": argues Neo4j is built for stable, structured relationship
  data while GraphRAG workloads are ephemeral, high-velocity hybrid lookups — a
  mismatch. Five engines pitched instead:
  - ArcadeDB: Apache 2.0, multi-model (graph + document + vector), Cypher/SQL/
    Gremlin, built-in MCP server so an agent queries it directly.
  - FalkorDB: in-memory, Redis + GraphBLAS, vendor-claimed 10x–100x faster multi-hop
    traversals than Neo4j; FalkorDB's own benchmark page claims P99 83 ms vs Neo4j
    41,157 ms on its dataset (vendor numbers, unverified independently).
  - TigerGraph: distributed-first, billions of edges, GSQL inline algorithms, hybrid
    graph-vector queries in one pass.
  - ArangoDB: one engine, four models, ~8x faster than Neo4j on multi-model workloads
    per the piece (vendor-adjacent claim).
  - Memgraph: C++ in-memory, Bolt-compatible with Neo4j (near drop-in), Kafka
    streaming, MCP server.
- FalkorDB Rust client falkordb-rs 0.10.5 released Oct 19, 2026 (lib.rs): sync +
  async tokio clients, typed results, parameter binding, batching/pipelining, async
  streaming, retry policy, OpenTelemetry-aligned tracing, replica routing via Redis
  Sentinel, embedded server for tests.
- Independent field report (dev.to, Oct 18, 2026): a team loaded FalkorDB's own
  GitHub graph into FalkorDB behind FastAPI + MCP, read-only via GRAPH.RO_QUERY,
  with measured local latencies (experts_for 88 ms, decision_trail 14 ms,
  triage_candidates 75 ms) on 20,961 nodes / 80,642 edges — a realistic, small-scale
  data point, not a vendor benchmark.

## Why it matters for ACI
- ACI's graph layer is networkx in-memory + persisted JSON; FalkorDB 6.0.3 is already
  the pinned candidate if the graph outgrows networkx. This coverage does not change
  that pin, but it adds two useful items: (1) ArcadeDB's built-in MCP server is a
  second data point (after Memgraph's MCP) for "graph engines ship MCP natively" —
  relevant when ACI eventually exposes its own graph over MCP; (2) the RO_QUERY
  read-only pattern from the field report is directly copyable for any future
  graph-MCP exposure.
- Treat the 496x/10x–100x traversal claims as vendor marketing until reproduced on
  ACI-shaped data; the field report's tens-of-ms latencies on a ~21k-node graph are
  the credible anchor.

## Sources
- dev.to, Oct 21, 2026:
  https://dev.to/techanalysisinsights/why-id-think-twice-before-picking-neo4j-for-a-graphrag-stack-in-2026-1jb7
- lib.rs falkordb crate (0.10.5, Oct 19, 2026): https://lib.rs/crates/falkordb
- dev.to field report, Oct 18, 2026:
  http://dev.to/zephyr2e1/we-loaded-falkordbs-github-into-falkordb-now-it-explains-itself-5f13
- FalkorDB benchmark page (vendor): https://www.falkordb.com/

## Action
- WATCH. No pin change (FalkorDB 6.0.3 stays the candidate). Borrow the
  GRAPH.RO_QUERY read-only pattern for any future ACI graph-MCP design; add
  ArcadeDB to the engine-selection reference list, not to the plan.
