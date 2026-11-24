# Pydantic AI v2.56.0 — Skills layering, PGTaskDurability, ZaiProvider base_url (2026-10-13)

**Date:** 2026-10-14 (release: 2026-10-13)
**Category:** multi-agent / frameworks

## What changed
Pydantic AI v2.56.0 was published 2026-10-13 (Deploy Log entry, sourced from
Pydantic's release). Headline items:
- **Skills layering** — skills can now be layered/composed, i.e. reusable
  capability bundles (instructions + tools + context) stacked on an agent
  instead of hand-wired per agent.
- **ZaiProvider `base_url`** — configurable base URL for the Z.ai provider.
- **PGTaskDurability** — Postgres-backed task durability for durable execution.
- **Render Workflows integration** — run agents on Render's workflow platform.

Context from the two prior releases (covered in earlier nights only up to
2.55.0 on 2026-10-12): v2.55.0 (2026-10-09) added a unified cross-provider
prompt-caching setting, a `Conversation` object carrying state between runs,
Postgres-backed step/media stores, and required Python ≥3.11. v2.56.0 builds
directly on that durability + state story.

## Why it matters for ACI
Three items map straight onto ACI's architecture: (1) **Skills layering** is
the same idea as ACI's analyst personas / tool registry — a skill bundle per
specialisation (recon, graph, RAG) that composes instead of duplicating
prompts; worth copying as a design pattern even though ACI's orchestration is
Python-deterministic, not Pydantic AI. (2) **PGTaskDurability** validates
ACI's own choice of Postgres-backed durable mission state — long-running
missions survive restarts. (3) **ZaiProvider base_url** matters because
Z.ai is one of Mohamed's free-provider pool members in the 3a2l proxy:
configurable base URLs make it easier to route a provider through a local
proxy without forking the SDK.

## Sources
- Pydantic AI v2.56.0 release log (secondary, sourced from Pydantic),
  2026-10-13:
  https://deployedbyai.com/log/2d253c416b9e/pydantic-ai-v2-56-0/
- Pydantic AI v2.55.0 release log (context), 2026-10-09:
  https://deployedbyai.com/log/cafacb37c265/pydantic-ai-v2-55-0/
- Note: verify details against the official GitHub release page before
  pinning a version; the Deploy Log entries are secondary summaries.

## Action
**Watch** — Do not adopt Pydantic AI into ACI's core (ACI's deterministic
Python pipeline stays). Borrow the Skills-layering pattern for ACI's
persona/tool bundles, and note the Z.ai `base_url` support for any future
direct (non-proxy) Z.ai integration. Re-check the official v2.56.0 release
notes on GitHub before acting on the feature list.
