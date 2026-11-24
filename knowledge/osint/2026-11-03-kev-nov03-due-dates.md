# KEV 3 Nov 2026 — due dates pass, LXD CVSS 10.0, Next.js security release

## What changed
- CISA KEV catalog at version **2026.10.30, 1,766 entries** (no new additions 31 Oct–1 Nov). Due dates now passing: Cisco ASA/FTD **CVE-2026-76418** and GitLab **CVE-2026-97229** (CVSS 10.0, unauthenticated RCE via CI/CD regex compiler) due 1 Nov; Ivanti Connect Secure **CVE-2026-111357** due 2 Nov, **CVE-2026-118527** due 13 Nov. Ivanti Integrity Checker caveat stands: Volexity notes the chain alters code in memory only and restores config data, so the checker may miss in-memory exploitation — forensic triage flag applies.
- **CVE-2026-112816** (Canonical LXD/MicroCloud, CVSS 10.0, published 30 Oct): pose as a trusted client on the LXD network API without the client's private key. Fixed LXD 6.10.1 / 5.21.9 / 5.0.11 / 4.0.15, MicroCloud 3.4.1 / 2.1.5. Not known exploited.
- **Next.js security release scheduled 3 Nov 2026** (per 2 Nov engineering roundup) — details pending at check time.
- KEV velocity: 10 additions 26–30 Oct (PHP, Adobe Commerce, Brotli, Linux kernel CVE-2026-46300, VMware ESX, GitLab, Cisco, Ivanti); 80% of KEV entries since 10 Jun carry ≤3-day federal deadlines (vs 3% in 2025).

## Why it matters for ACI
- None of these are ACI-stack CVEs (Python backend, n8n, Postgres) — intel-feed material, not an ACI emergency. The Ivanti/GitLab chain was already covered 1–2 Nov; tonight's delta is the due-date rollover + LXD + Next.js.
- The ≤3-day deadline trend matters for mission triage guidance: when ACI reports a KEV item to a client, the remediation window is now days, not weeks — reports should state the due date explicitly.
- Alpine Linux rebuilt its GitLab server after confirmed targeting 20–21 Oct — a concrete exploitation datapoint for the GitLab item, not just catalog presence.

## Sources
- https://www.immunitysec.com/vulnerabilities/kev/ (KEV mirror, read 3 Nov 2026)
- https://runbooklabhq.com/news/cisa-kev-cisco-asa-gitlab-ivanti-php/ (updated 3 Nov 2026, Ivanti checker caveat)
- https://carthageelectronics.com/november-1-2026-cve-threat-brief/ (1 Nov 2026, LXD CVE-2026-112816)
- https://www.highcircl.com/en/blog/engineering-news-week-2026-11-02 (2 Nov 2026, Next.js 3 Nov release note)

## Action
- **Watch**: Next.js 3 Nov security release details at next cycle (not our stack; note only if it affects a JS tool in the pipeline). Keep KEV due dates in mission triage templates.
- **Ignore** for ACI stack: LXD, Ivanti, GitLab, Cisco items — no deployment of those here.
