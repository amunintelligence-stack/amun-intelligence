# CISA KEV, week of 26 Oct – 1 Nov 2026: Ivanti chain + GitLab 10.0 RCE

**Date noted:** 2026-11-02
**Category:** osint — threat-intel feed (not ACI stack)

## What changed
- CISA added **10 CVEs to KEV in the week to 1 Nov 2026** (KNWOLF daily analysis, 1 Nov 2026).
- Headline chain: **Ivanti Connect Secure** — CVE-2026-111357 (missing authentication for a critical function, CVSS 8.8) + CVE-2026-118527 (predictable identifier generation, CVSS 4.3), added to KEV **30 Oct 2026**, chained with the earlier CVE-2026-104935 login bypass (KEV 13 Oct) for unauthenticated root-level code execution. Volexity attributes the activity to a previously undocumented actor **UTA0576**. Fixes: ICS **25.1.1.3 / 22.8R2.6** (29 Oct). Federal deadlines: **2 Nov 2026** (CVE-2026-111357, forensic triage required) and **13 Nov 2026** (CVE-2026-118527). Note: boxes patched 13 Oct are still exposed to the two new bugs — patching alone is not closure; CISA requires forensic triage.
- **GitLab CVE-2026-97229** (CVSS 10.0, unauthenticated RCE in the CI/CD pipeline engine), KEV with federal deadline **1 Nov 2026**. Alpine Linux's incident (20–21 Oct) is the cautionary case: a GitLab upgrade left the instance unprotected because the required Ruby patch was not bundled in its custom container image — a completed upgrade ≠ a closed vulnerability; log gaps forced a full rebuild.
- Rest of the week's KEV adds: Cisco Secure Firewall ASA/FTD (CVE-2026-76418), Broadcom VMware ESX (CVE-2026-41709, insufficient logging), Linux kernel (CVE-2026-46300), Adobe Commerce/Magento (CVE-2026-48356, unrestricted upload), Google Brotli (CVE-2026-111497), plus Drupal Commerce (CVE-2026-118539, missing authorization) flagged 1 Nov.

## Why it matters for ACI
- None of these products are in the ACI stack — this is intel-feed material, not a stack alert. Two patterns transfer directly to ACI mission design: (1) **chained-CVE reporting** — a mission that reports only the newest CVE misses the chain; KEV entries that reference each other must be reported as one chain with one remediation state; (2) **upgrade ≠ patched verification** — the Alpine case is the exact argument for ACI's verify-after-change rule (check the running artifact, not the deploy ticket).
- The Ivanti chain also reinforces the 23 Oct nightly's edge-device priority rule: internet-facing VPN/GitLab/firewall management interfaces go first in any exposure triage.

## Action: WATCH
- No stack change. Keep KEV as a standing mission input; when a mission touches VPN/GitLab/edge gear, report chains (not single CVEs) and require a running-version check, not a patch-ticket check.

## Sources (checked 2026-11-02)
- KNWOLF daily analysis, 1 Nov 2026: https://crime.knwolf.com/posts/2026-11-01-0600-daily-analysis/
- SecurityWeek via Qualactis, 2 Nov 2026: https://www.qualactis.com/cyber-news/i/9316703/ivanti-connect-secure-and-vpn-face-two-exploited-zero-days
- HOL triage, 2 Nov 2026 (fix versions + deadlines): https://hol.org/blog/cve-2026-111357-ivanti-connect-secure-root-escalation-cisa-kev
- Undercode News, KEV additions + UTA0576: https://undercodenews.com/cisa-adds-two-ivanti-connect-secure-vulnerabilities-to-kev-catalog-after-active-exploitation-warning-of-credential-theft-and-root-level-compromise-video/
- Pacific London, GitLab/Alpine case: https://www.pacific.london/insights/gitlab-cve-2026-97229-cicd-pipeline-rce-alpine-linux-container-patching-gap-cisa-kev-supply-chain-operational-resilience-uk-mid-market
