# n8n version state, 2 Nov 2026: no new stable; 3.0 stable still planned early Dec

**Date noted:** 2026-11-02
**Category:** soar — ACI runs n8n 2.43.7 (npm install); research only, no changes made

## What changed
- **No new stable release since ACI's 1 Nov note.** Stable line remains **2.45.7**; pre-release line remains **2.46.3** (GitHub labels: 2.45.7 "Latest", 2.46.3 "Pre-release", per the 30 Oct tag check). A self-host directory snapshot updated 2 Nov lists an experimental `2.45.7-exp` tag — treat tag-suffix builds as experimental, not as a new stable.
- **n8n 3.0 plan unchanged:** 3.0.0 beta released 27 Oct 2026 (official blog); stable planned **early December 2026**; Docker-only (npm/npx installs no longer supported); one-way upgrade; 2.x security fixes for 12 months after 3.0 stable. Workflows containing removed nodes fail to activate under 3.0 — the Migration Report (Settings > Migration Report, available on 2.39+) is the pre-upgrade gate.
- **No new n8n advisory surfaced in tonight's sweep** beyond the 28–29 Oct advisories already recorded (GHSA-gx3v expression-isolation escape affects ACI's 2.43.7, fixed 2.45.5+; upgrade candidate remains 2.45.5+ on نفذ only).
- Context from a 29 Oct analysis: n8n 3.0 does not turn the execution engine into a LangGraph equivalent — agents needing complex state control/recovery still favor LangGraph. This supports ACI's split: n8n for mission triggers/automation, deterministic Python for the intel pipeline itself.

## Why it matters for ACI
- ACI's 2.43.7 (npm) is affected by the 3.0 Docker-only rule at migration time, not today: any future upgrade path must include a Docker migration, not a version bump. The 2.45.5+ upgrade candidate (for GHSA-gx3v) stays on نفذ only, and risk stays bounded (localhost-only, single trusted editor).
- Do not chase the `2.45.7-exp` tag or the 2.46.3 pre-release for production.

## Action: WATCH
- No change tonight. At the next maintenance window on نفذ: run the Migration Report, then decide 2.45.5+ (2.x line) vs the December 3.0 stable with its Docker migration.

## Sources (checked 2026-11-02)
- n8n 3.0 official blog, 27 Oct 2026: https://blog.n8n.io/introducing-n8n-v3/
- n8n 3.0 migration analysis (breaking changes, removed nodes): https://websprint.dev/blog/n8n-3-migration-acceptance-evidence
- Tag state, 30 Oct 2026: https://kira-ai.de/blog/n8n-2-46-3-is-pre-release-while-2-45-7-is-latest-stable/
- n8n 3.0 vs LangGraph analysis, 29 Oct 2026: https://antoniovfranco.com/articles/why-n8n-3-0-still-does-not-replace-langgraph/en/
- Prior ACI notes: 2026-11-01-n8n-2-45-7-stable-2-46-3-prerelease.md, 2026-10-30-n8n-3-0-beta-oct27.md, 2026-10-29-n8n-oct28-advisories-gx3v-affects-2437.md
