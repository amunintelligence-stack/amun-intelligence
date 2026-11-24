# n8n 3.0 is coming: Docker-only self-hosting + legacy node retirements (Oct 2026)

## What changed
- n8n 3.0 is scheduled for October 2026 (Medium, Oct 3, 2026, summarizing n8n's own
  documentation): a security- and simplification-focused major release that will
  quietly break unmaintained workflows.
- Headline change: self-hosted n8n will REQUIRE Docker. The npm/npx install path
  ends at 3.0; Docker Compose is the expected path for local setups. ACI's n8n runs
  at 2.43.7 (npm-installed on this VM, per registry) — a 3.0 upgrade is therefore a
  deployment migration, not a version bump.
- Legacy nodes retiring in 3.0: Function / Function Item → Code node; Cron / Interval
  → Schedule Trigger; Item Lists → Split Out / Aggregate / Sort / Limit; Read PDF →
  Extract from File; Workflow Trigger → n8n Trigger; legacy OpenAI / OpenAI Assistant
  nodes → current OpenAI node; AI Agent node v1 → current version.
- Related, already in the Oct 23 nightly: 2.45.x (2.44.6 / 2.45.2 / 2.45.3) is the next
  upgrade candidate on نفذ with no new CVEs since the Oct 14 bulletin; 2.45.0's
  release notes (Releasebot, Oct 20, 2026) add agent/workflow tools, improved MCP
  permissions, migration notifications, and expanded node capabilities.
- Separate SOAR pattern note (Medium, Oct 15, 2026): a published SOC threat-
  enrichment pipeline built on n8n + Python + VirusTotal (token auth → internal-IP
  filtering → TI lookup → alerting) — a usable reference shape for ACI's
  incident-enrichment playbooks, with the caveat that its example hardcodes a
  token endpoint and credentials flow that ACI must never copy literally.

## Why it matters for ACI
- ACI's live mission workflow is «ACI — Intelligence Mission Trigger»
  (aNGsxPVzrnepykqR) on n8n 2.43.7. The 3.0 migration affects it in two ways: (1)
  the deployment itself must move to Docker before any 3.0 upgrade; (2) the workflow
  must be audited for retired nodes before upgrading. Neither is urgent — 2.43.7 is
  above the Oct 14 bulletin floor (2.43.5) — but the Docker migration needs a plan
  before 3.0 is adopted, and it needs Mohamed's نفذ like every other ACI change.
- Do NOT upgrade to 3.0 on this run: research only, and 3.0's exact release date is
  still "scheduled October 2026" in secondary coverage, not a confirmed release.

## Sources
- Medium (Bonface Alfonce), "n8n 3.0 Is Coming", Oct 3, 2026:
  https://medium.com/@bonfacealfonce/n8n-3-0-is-coming-heres-what-your-automations-need-before-you-upgrade-efce9897b6cb
- Releasebot, "n8n Release Notes — 2.45.0", Oct 20, 2026:
  https://releasebot.io/updates/n8n
- Medium (Mohamed Ehab), "Building an Automated SOC Threat Enrichment Pipeline with
  n8n, Python, and VirusTotal", Oct 15, 2026:
  https://medium.com/@mohddodo12/building-an-automated-soc-threat-enrichment-pipeline-with-n8n-python-and-virustotal-83556da0b909

## Action
- WATCH + PLAN (no upgrade). Next n8n step stays 2.45.x on نفذ. Before any 3.0 move:
  audit the ACI mission workflow for retired nodes, and plan the npm → Docker
  migration as its own نفذ item. Treat the SOC-enrichment pipeline shape as a
  playbook reference only.
