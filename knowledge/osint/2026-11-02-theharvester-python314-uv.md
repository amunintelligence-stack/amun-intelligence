# theHarvester toolchain delta: Python 3.14 + uv now required

**Date noted:** 2026-11-02
**Category:** osint — tool state (no new release found tonight)

## What changed
- No new theHarvester / sherlock / holehe / dnsrecon release surfaced in tonight's sweep beyond ACI's 31 Oct – 1 Nov state notes (theHarvester v4.11.1 in ACI's venv; sherlock 0.16.2; maigret 0.6.6).
- Toolchain note from the upstream README (read 2 Nov 2026): **theHarvester now requires Python 3.14 and uv** (`.python-version` lets uv select the version automatically; install path is `uv run theHarvester -d example.com -b crtsh,certspotter`). This is a deployment constraint, not a feature: the ACI venv (older Python) cannot track upstream master without a Python upgrade.
- Context: theHarvester 4.9.0 (Dec 2025) added Hudson Rock infostealer-data integration; the 5.0.0 dev line (REST API, HarvestView, scheduler) remains in progress per the registry.

## Why it matters for ACI
- ACI's theHarvester stays pinned at v4.11.1 in its venv until a deliberate tool-update window. Any future pull from upstream master must budget a Python 3.14 + uv migration for that tool's venv — do not let a routine `git pull` break the working install.

## Action: WATCH
- No change tonight. At the next tool-update window: verify the venv Python version before pulling theHarvester, and record the uv migration as a prerequisite if tracking master.

## Sources (checked 2026-11-02)
- theHarvester README (Python 3.14 + uv requirement): https://github.com/laramies/theHarvester
- Prior ACI notes: 2026-11-01-osint-tool-state-check.md, 2026-10-30-sublist3r-inactive-status.md
