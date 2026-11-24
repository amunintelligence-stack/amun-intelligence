# KEV 30 Oct 2026 — Ivanti Connect Secure chain completed (CVE-2026-111357, CVE-2026-118527)

**Date noted:** 2026-10-31 (CISA additions dated 2026-10-30)
**Category:** osint / threat intel — exploited-vulnerability watch

## What changed
- CISA added **two Ivanti Connect Secure flaws** to the Known Exploited Vulnerabilities (KEV) catalog on **30 Oct 2026**, citing evidence of active exploitation:
  - **CVE-2026-111357** — missing authentication for a critical function; a local authenticated attacker can escalate privileges (reportedly via the `dsinvoked` broker trusting DSCache configuration data, toward root). Federal due date: **2 Nov 2026**.
  - **CVE-2026-118527** — predictable numbers/identifiers; a remote authenticated attacker can upload attacker-controlled content to a known disk location. Federal due date: **13 Nov 2026**.
- The two flaws **complete a three-bug chain** with **CVE-2026-104935** (authentication bypass, unauthenticated remote command execution). Volexity observed threat actor **UTA0576** using the chain in early October against a fully patched Connect Secure appliance.
- Ivanti published fixes for the remaining two flaws on **29 Oct 2026**. Recommended fixed branches per the Canadian Centre for Cyber Security: **25.1.1.3, 25.1.3.1, or 22.8R2.6** (branch-dependent).
- Context: this closes the October edge-device wave — CISA added a dozen exploited edge products in October 2026 (Fortinet, Citrix NetScaler, Cisco, Ivanti, PAN-OS, BeyondTrust, Arista, Ahsay, SiteGuard…). The only open federal deadline after 31 Oct is Cisco ASA/FTD CVE-2026-76418, due **1 Nov 2026**.
- Prior-night cross-reference: the 29 Oct KEV additions (GitLab CVE-2026-97229, Cisco CVE-2026-76418) are covered in `2026-10-30-kev-oct29-gitlab-cisco.md`.

## Why it matters for ACI
- Edge-device chains are a first-class collection target for ACI missions: a single-vendor chain (auth bypass + privesc + file write) is exactly the pattern our recon/enrichment pipeline should flag when profiling a target's exposed VPN/firewall estate.
- Ivanti Connect Secure is a common corporate perimeter box; a mission target running it on a pre-fix branch is a high-priority finding, and the UTA0576 activity window (early Oct, against patched appliances) means "patched" alone is not a clean verdict — look for the chain, not one CVE.
- No ACI stack impact: ACI does not run Ivanti, and nothing here changes our own patching (unlike the n8n advisories tracked separately).

## Sources
- CISA KEV catalog additions, 30 Oct 2026, via: https://www.abijita.com/cisa-adds-ivanti-connect-secure-flaws-kev/ (31 Oct 2026) and https://runbooklabhq.com/news/cisa-kev-cisco-asa-gitlab-ivanti-php/ (31 Oct 2026, catalog version 2026.10.30)
- October edge-device recap: https://datawater.com/edge-device-zero-days-october-2026/ (31 Oct 2026)
- KEV record summaries: https://cyber.hendryadrian.com/article/12497/cisa-adds-two-actively-exploited-ivanti-connect-secure-vulnerabilities-to-kev-catalog (30–31 Oct 2026)

## Action: WATCH
- Add the Ivanti triple (CVE-2026-104935 + CVE-2026-111357 + CVE-2026-118527) to the mission enrichment checklist as a chained-finding rule: flag any Connect Secure instance below 25.1.1.3 / 25.1.3.1 / 22.8R2.6 as "chain-exploitable", not just "one CVE present".
- No change to ACI's own infrastructure. Not a critical alert for our stack (no Ivanti in it).
