# memory-graph: knowledge-graph memory MCP server (SQLite / Neo4j / Memgraph)

**Date noted:** 2026-11-02
**Category:** graph + mcp crossover — new tool

## What changed
- **memory-graph** (gregorydickson/memory-graph, surfaced on Hacker News ~30 Oct – 1 Nov 2026): an MCP server that stores entities, observations, and relationships in a knowledge graph, positioned as a queryable alternative to the official `@modelcontextprotocol/server-memory` (JSONL).
  - Three backends: **SQLite (default)** — single file, zero config, ~50 MB with embeddings; **Neo4j** (scale); **Memgraph** (speed).
  - **30 MCP tools**, **409 tests passing (90%+ coverage)**, 8 architecture decision records.
  - Relationship types include SOLVES / CAUSES / RELATES_TO, so agents can query chains ("what blocks what") rather than similarity-ranked text.
  - Install: `pip install memorygraphMCP`.
- Context: a Towards AI piece published **2 Nov 2026** makes the same case for agent memory — vector search returns what *sounds like* the question, a graph returns the *chain of facts* that answers it — with a Neo4j/Memgraph/Zep walkthrough. The pattern is converging across independent sources this week.

## Why it matters for ACI
- ACI's graph layer is networkx in-memory + Postgres snapshots. memory-graph is not a replacement (ACI's graph is mission-scoped evidence, not agent memory), but two things transfer: (1) the **SQLite-default, zero-config** shape is a credible pattern for per-mission graph persistence if networkx snapshots ever need querying without Postgres; (2) its **30-tool surface + ADRs + 90% test coverage** is a quality bar to hold any future ACI graph MCP server to — and its relationship vocabulary (SOLVES/CAUSES/RELATES_TO) maps cleanly onto ACI's evidence chains (finding → caused-by → entity).
- Added to the registry as a watch/eval candidate under MCP servers.

## Action: WATCH
- No adoption. Eval isolated first if ACI ever exposes its graph over MCP: compare its SQLite backend against ACI's Postgres snapshots on a real mission graph, and borrow the read-only discipline from the Memgraph MCP pattern (Oct 23 nightly) for any write surface.

## Sources (checked 2026-11-02)
- Hacker News thread: https://news.ycombinator.com/item?id=46091577
- Repository (from thread): https://github.com/gregorydickson/memory-graph
- Towards AI, 2 Nov 2026: https://pub.towardsai.net/day-38-100-knowledge-graph-memory-for-ai-agents-neo4j-memgraph-and-zep-a72dbc5cf558
- Neo4j lifecycle cross-check: https://endoflife.date/neo4j (2026.10.1 released 20 Oct 2026; 2026.09 support ended 20 Oct — 2026.10 line confirmed current)
