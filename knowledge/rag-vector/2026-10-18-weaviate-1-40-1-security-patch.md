# Weaviate 1.40.1 (2026-10-13) — security patch

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — Weaviate not deployed today; note ≥1.40.1 as the hardened minimum for any future pilot.

## What changed
Weaviate shipped patch release v1.40.1 on 2026-10-13 — pure fixes, no breaking changes or features. Two fixes are explicitly security: "Fix zlib to a version unaffected by CVE-2026-85091" (#13482) and "Update golang.org/x/net to fix CVE-2026-78663 etc" (#13509). Also: HNSW entrypoint bootstrap-exhaustion detection, multi-vector write guard, backup/memtable shutdown reliability fixes, and schema updates no longer loading shards an unload released. A 1.39.11 backport was cut in the same window; docs.weaviate.io's Docker quickstart now pins weaviate:1.40.1.

## Why it matters for ACI
Weaviate is one of the vector-DB candidates in our RAG upgrade path alongside Qdrant 1.19.x. Any future ACI pilot of Weaviate must deploy ≥1.40.1, not 1.40.0, since 1.40.0 ships a vulnerable zlib/x-net. It also confirms the 1.40 line (namespaces + MuVeRA from the Oct 16 file) is being actively hardened with patch releases — good hygiene signal for a candidate we keep watching.

## Sources
- weaviate/weaviate v1.40.1 on GitHub — https://newreleases.io/project/github/weaviate/weaviate/release/v1.40.1 — 2026-10-13
- Quickstart: Locally hosted with Docker (pins weaviate:1.40.1) — https://docs.weaviate.io/weaviate/quickstart/local — accessed 2026-10-18
