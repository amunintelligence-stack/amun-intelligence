# FalkorDB 6.0.x field-reported engine bugs + traversal-gate pattern (Oct 17–18, 2026)

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — retain 6.0.2 pin; re-verify issue closure before adopting FalkorDB; borrow the traversal-gate pattern.

## What changed
Community field reports from the Oct 2026 WeMakeDevs × FalkorDB Graph Hacks hackathon document several 6.0.x engine issues in production-adjacent use:
- `SSpaths` `pathCount` is a global top-k (full-looking results may be silently truncated)
- `OPTIONAL MATCH` after an aggregating `WITH` returns no rows
- Aggregating `SSpaths` output with a null property crashes the entire server from a read-only query
- `algo.WCC` and `algo.pageRank` fail when the projected label set holds exactly one node (filed as FalkorDB#3349)
- FalkorDB's own GraphRAG-SDK could not create fulltext indexes on 6.0.x (fix GraphRAG-SDK#345, superseded by fuller fix #348–#350)
- Two further engine findings went upstream as FalkorDB#3376 and #3377; one security-relevant finding was reported privately.
- Separately, a hackathon build ("Tether", Oct 18) demonstrated FalkorDB doing deep 4-hop traversal gates at 10ms p50 / 28.8ms p95 for agent tool-invocation security — a design reference for inline policy checks. (Secondary sources — community field reports, not official advisories.)

## Why it matters for ACI
FalkorDB 6.0.2 is our pinned future graph-upgrade candidate. These reports say: keep the 6.0.2 pin, re-verify #3349/#3376/#3377 and the GraphRAG-SDK index fix are resolved before any adoption, and wrap queries defensively (single-node projections, null-property aggregation). The sub-millisecond-class traversal-gate pattern is directly reusable for ACI's confidence-gated verdicts if enforcement ever moves into the graph.

## Sources
- "Our on-call agent isn't allowed to blame a deploy until FalkorDB returns a path (field notes, FalkorDB#3349/#3376/#3377)" — https://medium.com/@prashant101007/our-on-call-agent-isnt-allowed-to-blame-a-deploy-until-falkordb-returns-a-path-b32d8bcf2fb7 — ~2026-10-17
- "The Chain, Not the Grant: Building Runtime Dataflow Governance for AI Agents with FalkorDB (gate latency p50 10.0ms / p95 28.8ms)" — http://dev.to/sanskar_18c2d8e0e33ed827a/the-chain-not-the-grant-building-runtime-dataflow-governance-for-ai-agents-with-falkordb-41nb — 2026-10-18
