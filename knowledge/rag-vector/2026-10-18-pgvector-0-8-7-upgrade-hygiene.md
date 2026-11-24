# pgvector 0.8.7 upgrade hygiene — backend recycling required

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** ADOPT — write backend-recycle + git-tag verification into the ACI pgvector runbook when pgvector is installed; adopt least-privilege app role now in principle.

## What changed
A deep-dive analysis of CVE-2026-103484 (published 2026-10-08, already on our watch) adds three actionable deltas the Oct 9 coverage missed:
1. The fix lives in the `vector` shared library, so installing the package is NOT enough — every backend that loaded the old library keeps running vulnerable code until it exits. Remediation requires recycling backends (`pg_terminate_backend()` on old backend_start, PgBouncer RECONNECT, or a restart if vector is in shared_preload_libraries). `pg_extension.extversion` is not proof of patch.
2. pgvector publishes git tags, not GitHub Releases — Releases-page alerting saw nothing.
3. This is the third memory-safety CVE in pgvector's index-build code in 2026 (CVE-2026-3172 in 0.8.2/Feb, CVE-2026-18022 in 0.8.6/Jul), all in rarely-exercised build code — plus the privilege angle: app roles that own tables (and MAINTAIN/pg_maintain reindex rights since PG17) can all trigger it.

## Why it matters for ACI
pgvector is the natural vector index for the RAG Postgres tier on the upgrade path. When pgvector lands, ACI needs this exact procedure: install package + recycle backends + verify via git tag (not extension version), and harden with a migration role owning the schema while the app role gets only CRUD. The "third CVE in index-build code this year" pattern says keep pgvector patches in the monthly security pass.

## Sources
- "The Vector That Lied About Its Dimensions" — https://thebuild.com/blog/the-vector-that-lied-about-its-dimensions/ — 2026-10-08
- "PostgreSQL: pgvector 0.8.7 Released" — https://www.postgresql.org/about/news/pgvector-087-released-3392/ — 2026-10-05
