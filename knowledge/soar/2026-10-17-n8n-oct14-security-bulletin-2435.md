# n8n October 14 security bulletin — 8 vulnerabilities, 5 High; our 2.42.4 is below the patched floor

**Date of finding:** 2026-10-17
**Window covered:** last ~30 days

## What changed

- **n8n published a security bulletin on 14 Oct 2026 covering eight vulnerabilities, five classified High.** Patched floors: **1.x → 1.123.85+**, **2.x stable → 2.43.5+**, **2.x beta → 2.44.1+**. Cloud instances were patched automatically; self-hosted operators must update themselves. No confirmed active exploitation reported as of the bulletin date.
- **The five High items (per the bulletin summary):**
  - **Stored XSS (CVSS 8.4):** malicious HTML returned through webhook responses could execute JavaScript inside another user's authenticated session.
  - **Cross-project data access (CVSS 7.2):** a specially crafted workflow ID could let a restricted user read or modify Data Tables belonging to a different project.
  - **Prototype pollution (High):** a workflow-history vulnerability could cause denial of service.
  - **File-operation DoS (High):** crafted glob patterns in the Read/Write Files node could block the application's event loop.
  - **Credential exposure:** certain node execution errors could reveal sensitive credential data to users with access to execution logs.
  - Three further vulnerabilities in the bulletin were not detailed in the summary source (medium/low — exact IDs/CVEs not yet confirmed from a primary source).
- **Latest stable as of 16 Oct 2026: n8n@2.43.7.** The 2.43.x line is now the maturing stable line (2.43.4 went stable 12–13 Oct).
- **Context — Censys (reported 15 Oct):** ~114,000 n8n instances are internet-exposed; ~76% of exposed instances ran versions with known critical vulnerabilities. The October security updates alone are reported to have patched 14 advisories in total across batches.
- **Important contrast with the 5–6 Oct batch:** the earlier CVE-2026-86076 / CVE-2026-44790 batch was verified NOT to affect our 2.42.4 (fixed in 1.123.76 / 2.37.7 / 2.38.2 or later). **This 14 Oct batch is different: its 2.x stable patched floor is 2.43.5, which is ABOVE our 2.42.4.** Treat 2.42.4 as unpatched for this batch until each advisory's affected range is verified against the primary GHSA entries.

## Why it matters for ACI

- **Our n8n runs 2.42.4** (the ACI "Intelligence Mission Trigger" workflow, id aNGsxPVzrnepykqR). It is now below the patched floor for a bulletin that includes stored XSS, cross-project data access, and credential exposure via execution logs — the last one is directly relevant because ACI workflows touch API keys and credentials.
- **Mitigating factor:** our instance is not internet-exposed (localhost-only), which removes the easiest exploitation path. The stored-XSS and cross-project items mainly bite multi-user / exposed deployments, but the credential-exposure-via-logs and glob-DoS items do not require internet exposure.
- **Upgrade path is now clearer:** 2.43.7 stable exists, but any upgrade still needs the standing «نفذ» approval, a pre-upgrade backup, and the deprecated-node audit (2.42.6+/2.43.3+ block create/update of workflows containing deprecated nodes). The n8n 3.0 Docker-only migration plan (see 2026-10-14 file) is a separate, bigger step — do not conflate the two: patch to 2.43.x first, migrate to 3.0/Docker second.
- **Post-upgrade hygiene (from the bulletin coverage):** review execution logs for anomalies, rotate secrets used by n8n, and verify no unexpected users/credentials were added.

## Sources

- Medium / BizStack, "n8n self-hosted: 5 high-severity flaws patched, update now" (15 Oct 2026) — https://medium.com/cagris-biz-stack/n8n-self-hosted-5-high-severity-flaws-patched-update-now-982502f5ee21
- DEV Community, "Censys Counted 114,000 Exposed n8n Instances: Your Self-Hosted Hardening Checklist" (15 Oct 2026) — https://dev.to/cortexflow_tech/censys-counted-114000-exposed-n8n-instances-your-self-hosted-hardening-checklist-ck5
- selfhost.directory, n8n project page (latest n8n@2.43.7, 16 Oct 2026) — https://selfhost.directory/project/n8n
- **Verification gap:** individual GHSA/CVE IDs and per-advisory affected-version ranges for the 14 Oct batch were not yet confirmed from n8n's primary advisory index at write time — verify before declaring any single advisory applicable/inapplicable.

## Action

**CRITICAL — adopt (upgrade), pending «نفذ»:** upgrade the ACI n8n instance from 2.42.4 to 2.43.7 (or newer patched stable) at the earliest approved window: backup DB + file storage first, audit the mission workflow for deprecated nodes, upgrade, verify credential store + workflow execution, rotate n8n-held secrets, review execution logs. Do NOT jump straight to n8n 3.0 (npm installs end; Docker-only) without the separate Docker migration plan.
