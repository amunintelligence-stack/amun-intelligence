# n8n 3.0 — npm installs end, legacy nodes retire, stricter defaults (scheduled Oct 2026)

**Date researched:** 2026-10-14
**Status:** ⚠️ ACTION REQUIRED BEFORE ANY UPGRADE. Scheduled for October 2026 per n8n's own docs as reported 3 Oct 2026. This is the night's most important finding for ACI.

## What changed
n8n 3.0 (scheduled October 2026) is a breaking major release, summarized from n8n's documentation (Medium, 3 Oct 2026; corroborated by an independent analysis of docs.n8n.io and a migration walkthrough):
- **Docker or nothing:** npm/npx self-hosted installs end at 3.0. Self-hosted n8n will require a Docker-based deployment; Docker Compose is the recommended path. n8n's docs mark the npm install page deprecated from 3.0 and describe npm/local setup as unsafe for production (local dev/testing only).
- **Legacy nodes retire:** Function / Function Item → Code node; Cron / Interval → Schedule Trigger; Item Lists → Split Out / Aggregate / Sort / Limit; Read PDF → Extract from File; Workflow Trigger → n8n Trigger; legacy OpenAI / OpenAI Assistant nodes → current OpenAI node. **AI Agent node v1 is also removed** — agents built on the older modes must be updated.
- **Small defaults, big consequences:** task-runner timeout drops from 5 min → 1 min (a 90-second Code node will now fail); unverified community packages are switched **off** by default (community nodes won't load until explicitly allowed); binary-data folder renamed from `binaryData` to `storage` (matters for volume mounts).
- **Stricter security:** wider default SSRF block list; significantly lower limits on unzipping large archives — workflows calling unusual internal addresses or handling large compressed files need explicit allowances.
- **Chat Hub:** switched off by default in 3.0, planned removal in 4.0 (can be kept enabled for the 3.x line as a bridge).
- **Safety net:** n8n built a Migration Report into Settings listing affected nodes/changes per instance — run it before anything else.

## Why it matters for ACI
- ACI's automation layer runs on self-hosted n8n (currently 2.42.x line, with a standing 2.42.6→2.43.x upgrade thread). If the ACI instance is npm-installed, **upgrading to 3.0 in place is not possible** — it needs a Docker Compose migration first, with the encryption key, credentials, database, and execution history carried over (the migration guides warn of two silent data-loss paths: skipping the last v2 run against the volume, and the empty-workflow trap).
- The 1-minute task-runner timeout directly threatens long-running ACI workflows (large-file Code nodes, bulk recon fan-out). The SSRF block-list widening can break workflows that call internal/loopback services (ACI backend on 127.0.0.1) unless allowances are set. Community nodes going off-by-default can silently unload custom nodes.
- The AI Agent v1 removal interacts with the n8n Agents launch (see `2026-10-14-n8n-assistant-agents.md`): agent-based mission workflows need re-validation on the current agent node.

## Action
**ADOPT (plan now, do NOT upgrade yet):**
1. Confirm how ACI's n8n is installed (npm vs Docker). If npm: plan a Docker Compose migration (backup + export key workflows first; run the last v2 release once against the migrated volume).
2. Open the Migration Report in Settings and list every flagged legacy node.
3. Replace old nodes one workflow at a time, testing as you go; audit timeouts (>60 s Code nodes), community-node allowances, and `binaryData`→`storage` volume paths; set explicit SSRF allowances for 127.0.0.1/internal ACI endpoints.
4. Pin the n8n version until the migration is verified — do not float to `latest` across the 3.0 boundary.

## Sources
- "n8n 3.0 Is Coming…" (Medium, 3 Oct 2026, summarizing n8n's own docs): https://medium.com/@bonfacealfonce/n8n-3-0-is-coming-heres-what-your-automations-need-before-you-upgrade-efce9897b6cb
- Independent analysis of docs.n8n.io install-method statuses (npm deprecated from 3.0; Docker Compose recommended), 8 Oct 2026: https://github.com/itspoma/n8n-challenges/blob/HEAD/content/blog/en/article-8e9e88be-5d7d-4cfa-944e-85c2ea5c5063.md
- Migration walkthrough, "n8n 3.0 Kills NPM Install" (YouTube, Sep 2026): https://www.youtube.com/watch?v=_174SKJnVVY
- Prior ACI notes: `2026-10-13-n8n-2.43.4-stable-cve-verdict.md`, `2026-10-08-n8n-30-docker-only-npm-dropped.md`
