# n8n maintenance wave — 2.45.7 now latest stable, 2.46.3 pre-release (30 Oct 2026)

**Date noted:** 2026-11-01
**Category:** soar / n8n — directly relevant: ACI runs n8n 2.43.7

## What changed
- On **30 Oct 2026** n8n's GitHub tags moved one step on both trains (per the 31 Oct tag check):
  - **2.45.7 — now marked "Latest" (stable)** on its release page, superseding 2.45.6.
  - **2.46.3 — marked "Pre-release"**, superseding 2.46.2 on the beta/next line.
- No new GHSA references surfaced with these two tags in the sources checked: they are follow-up fixes on top of the **28 Oct advisory baseline** (patched by 3.0.1 / 2.46.1 / 2.45.5, covered 2026-10-29 — GHSA-gx3v still unpatched on our 2.43.7; GHSA-9p7v already covered by 2.43.3+).
- Context: 2.46.0's notes (27 Oct) include **Kafka node v2 as the default for new nodes** and **Monday.com node V2 with full V1 parity as default** — relevant only if ACI ever adds those nodes; the mission-trigger workflow uses neither.
- 3.0 stable is still expected **early December 2026** (beta since 27 Oct); 3.x remains Docker-only, one-way, staging-only for ACI.

## Why it matters for ACI
- **Upgrade candidate re-pointed again: 2.45.6 → 2.45.7.** Same advisory baseline, plus the follow-up fixes. If/when Mohamed approves the upgrade from 2.43.7, the candidate is 2.45.7 (re-verify its notes at that time), not 2.45.5/2.45.6.
- 2.46.3 stays preview: do not promote. 3.x stays staging-only.
- No action on the running instance tonight: research only, and ACI's standing rule requires Mohamed's explicit go-ahead before any upgrade.

## Action: WATCH (re-point candidate)
1. At the next approved maintenance window: upgrade 2.43.7 → 2.45.7 in-branch (backup first, Migration Report, audit deprecated nodes), closing GHSA-gx3v.
2. Do not touch 2.46.x or 3.x in production before the December stable + Docker staging plan.

## Sources (checked 2026-11-01)
- Tag status check, 30 Oct 2026: https://kira-ai.de/blog/n8n-2-46-3-is-pre-release-while-2-45-7-is-latest-stable/
- n8n 3.0 beta announcement (27 Oct 2026): https://blog.n8n.io/introducing-n8n-v3/
- 28 Oct advisories summary: https://kira-ai.de/blog/n8n-publishes-high-severity-advisories-with-3-0-1-2-46-1-2-45-5/
- Prior ACI notes: 2026-10-29-n8n-oct28-advisories-gx3v-affects-2437.md, 2026-10-31-n8n-2-45-6-2-46-2-oct29.md
