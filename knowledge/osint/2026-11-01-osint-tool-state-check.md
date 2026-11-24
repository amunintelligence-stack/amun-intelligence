# OSINT tool-state check — no new releases for the ACI recon stack; subfinder keyless run independently confirmed

**Date noted:** 2026-11-01
**Category:** osint — verification round: theHarvester, sherlock, maigret, subfinder, amass, nuclei

## What changed
- **No new release** was found tonight for any ACI-stack OSINT tool beyond the versions already on record:
  - subfinder **2.17.0** (8 Oct 2026) still latest — confirmed by two independent Oct write-ups (21 Oct, 23 Oct).
  - maigret **0.6.6** (18 Sep 2026) still latest; project still committing in October; site DB holds 5,897 entries (top-500 Majestic Million checked by default).
  - sherlock **0.16.2** (10 Sep 2026) still latest per registry; maigret-vs-sherlock comparison (31 Oct) confirms the functional split: sherlock checks presence, maigret follows profile links onward over a much larger DB.
  - amass **5.1.2** (25 Oct 2026) still latest per ACI's own 31 Oct note — third-party round-ups still showing 5.1.1 are stale relative to ACI's notes.
  - nuclei **3.11.1** still latest per the 23 Oct ASM tutorial pin check; subfinder 2.17.0 + nuclei 3.11.1 pinned there.
- **Correction to the line above:** the 31 Oct ACI note (2026-10-31-amass-5-1-2.md) already records amass 5.1.2 — tonight's sweep found no newer amass tag, so **5.1.2 stands as latest**; no registry change needed.
- **Independent keyless-run data point for subfinder 2.17.0** (darknet.org.uk test, 21 Oct 2026): with no API keys, a run returned **17 subdomains in 14 seconds, of which only 1 resolved in DNS**. This corroborates ACI's 26 Oct dev-branch count (37/58 sources need keys; keyless runs cover ~20/58 sources, report coverage as partial): keyless subfinder output is a candidate list, not a verified footprint — every candidate needs DNS resolution before it enters a mission report.

## Why it matters for ACI
- The recon stack is stable: no upgrade window is triggered tonight. The durable lesson is the keyless-coverage rule — missions must label subfinder keyless output as partial and resolve candidates before reporting.
- The amass note is a process reminder: third-party round-ups lag ACI's own notes by days; ACI's dated notes are the fresher source for these tools.

## Action: IGNORE (no upgrade); WATCH (coverage rule stands)
- No tool changes. Keep reporting keyless subfinder runs as partial coverage with DNS-resolution verification.

## Sources (checked 2026-11-01)
- Subfinder 2.17.0 independent test (21 Oct 2026): https://www.darknet.org.uk/2026/10/subfinder-passive-subdomain-enumeration-tool/
- Maigret 0.6.6 profile (31 Oct 2026): https://www.darknet.org.uk/2026/10/maigret-osint-username-search-tool/
- ASM tutorial pin check (23 Oct 2026): https://tech-insider.org/attack-surface-management-subfinder-httpx-naabu-2026/
- Prior ACI notes: 2026-10-31-amass-5-1-2.md, 2026-10-26 (subfinder dev-branch source count), 2026-10-29-username-tools-state-nuclei-go-note.md
