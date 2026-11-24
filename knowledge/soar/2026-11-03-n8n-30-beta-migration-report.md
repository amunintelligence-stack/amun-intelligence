# n8n 3.0 beta — Migration Report is the pre-upgrade gate (stable early Dec)

## What changed
- **n8n 3.0.0 beta** (27 Oct 2026; stable planned early December 2026; 1.x support ends 31 Dec 2026; 2.x keeps security + critical fixes for 12 months after stable). No headline features — it removes legacy parts and tightens security defaults. **One-way upgrade**: no path back to 2.x except from backup; no direct 1.x → 3.x path (go 1.x → 2.x first).
- **Removed nodes** (workflows using one do not activate on 3.0 — triggers silently stop): Function, Function Item, Item Lists, Cron, Interval, Read PDF, legacy OpenAI node, AI Agent node v1, Workflow Trigger, and others. Replacements: Code node, Schedule Trigger, Split Out/Aggregate/Sort/Limit, Extract from File, n8n Trigger, current OpenAI node.
- **Behavior changes**: queue mode — manual executions always run on workers; Code node task timeout 300 s → 60 s; binary data in-memory mode removed (filesystem/S3/Azure only); compression limits 2 GiB/5000 entries → 256 MiB/1000; unverified community packages default off; Gmail Trigger <v1.4 skips drafts + max 10 emails/poll by default; Slack Trigger needs a signing secret or stops receiving events; Chat Hub off by default (removed in 4.0).
- **Self-host rule**: 3.0 requires Docker-based deployment — npm/npx installs are no longer supported and no runnable n8n package is published to npm for 3.x.
- **Migration Report** (in 2.x since 2.39, Settings → Migration Report): lists affected nodes and required changes in your own instance; automatic migration covers node changes only — AI Transform → Code migration is manual, and published workflows keep running the old version until the new one is published. Independent agents experience still in Preview at 28 Oct; 3.0 does not turn n8n into a LangGraph equivalent for state-controlled agents.

## Why it matters for ACI
- ACI runs n8n **2.43.7 via npm** — squarely in the affected class: the 3.x move needs a Docker Compose migration, not an in-place upgrade. The 2.45.7 stable line remains the next in-branch upgrade candidate on «نفذ» (it carries the 28 Oct advisory fixes incl. GHSA-gx3v); 3.x stays staging-only.
- The ACI mission workflow («ACI — Intelligence Mission Trigger», aNGsxPVzrnepykqR) must be audited for removed nodes **before** any 3.x move — a workflow that fails to activate means missions silently stop firing. Run the Migration Report at the next maintenance window, on «نفذ» only.
- The Code-timeout cut (5→1 min) and worker-offload change affect any long-running mission steps if they ever move to n8n-side execution.

## Sources
- https://www.emergyaiops.com/blog/n8n-3-migration-report-before-upgrade (31 Oct 2026)
- https://websprint.dev/blog/n8n-3-migration-acceptance-evidence (Oct 2026, early-access vs stable distinction)
- https://muench.dev/en/post/2026-10-preparing-n8n-for-v3-migration-report-opencode-and-a-bit-of-manual-work (Oct 2026, variable table)
- https://antoniovfranco.com/articles/why-n8n-3-0-still-does-not-replace-langgraph/en/ (29 Oct 2026)

## Action
- **Watch**: 3.0 stable (early Dec) — do NOT touch beta; 2.45.7 stays the in-branch candidate.
- **Adopt (practice, on «نفذ»)**: run the in-instance Migration Report at the next maintenance window; audit the ACI mission workflow for removed nodes; plan Docker Compose staging before any 3.x decision. No upgrade tonight.
