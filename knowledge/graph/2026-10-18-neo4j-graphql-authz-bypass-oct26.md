# @neo4j/graphql authorization bypasses — CVE-2026-92682 (CVSS 8.6), fixed in 7.6.4 (12 Oct 2026)

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — threat-pattern reference for any future declarative/API exposure of the ACI graph; not in current stack.

## What changed
Two authorization defects in the @neo4j/graphql library were disclosed and fixed in 7.6.4 on 12 October 2026:
- CVE-2026-92682 (CVSS 8.6 HIGH): in versions ≥7.0.0 <7.6.4, the `none` quantifier in @authorization filters on relationships/connections was not negated when translated to Cypher — it behaved like `some`, so a rule denying related records returned exactly the records it meant to exclude, on reads AND mutations.
- Sibling flaw (versions ≤7.6.3): @authentication directives applied at schema or Query/Mutation-type level were silently ignored for top-level @cypher fields; only directives placed directly on the individual field were enforced, so unauthenticated callers could run arbitrary Cypher with service-account privileges.

## Why it matters for ACI
ACI has no GraphQL layer, so no direct exposure. This is the cleanest recent real-world example of the "authorization logic lost in schema→query translation" pattern — the exact failure class ACI must avoid if it ever exposes its networkx/Postgres graph via GraphQL or another declarative API. Record alongside the existing policy-to-query-translation design lessons.

## Sources
- "CVE-2026-92682: @neo4j/graphql Incorrect Authorization (CVSS 8.6)" — https://www.strix.ai/cve/CVE-2026-92682 — published 2026-10-12, page updated ~2026-10-16
- "This Week's Vulnerabilities (incl. both @neo4j/graphql flaws)" — https://neterix.com/vulnerabilities/cve_week.html — week of 2026-10-12
- "When Authorization Is Translated Wrong, the API Becomes the Weak Point" — https://netcrook.com/written_article?slug=neo4j-graphql-authorization-bugs-expose-api-risk&lang=en — 2026-10-18
