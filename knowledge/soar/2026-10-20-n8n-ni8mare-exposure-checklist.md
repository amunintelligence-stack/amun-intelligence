# Ni8mare Retrospective + Exposure Hardening Coverage (Oct 17–18, 2026)

## What changed
No new n8n CVE landed Oct 19–20; the Oct-14 advisory batch remains the latest. What is new is in-window awareness coverage consolidating the exposure data: Censys 2026 State of the Internet (released Oct 14) — **~114,000 exposed n8n hosts**, the most exposed AI product measured, with **76% of version-detectable instances vulnerable** to at least one recent critical; Shadowserver scan data via TechRadar (Sept) — **~60,000 internet-connected instances still vulnerable**. A dev.to series (published Oct 17–18) revisits **Ni8mare (CVE-2026-21858, CVSS 10.0)**: unauthenticated webhook RCE that reads arbitrary server files and escalates to full takeover — reported to n8n Nov 2025, **patched in 1.121.0**, i.e. it predates the entire 2.x line. No official workaround exists for Ni8mare; mitigation is patch or remove internet exposure. 68% of exposed HTTP(S) services ran on non-standard ports — port-shifting does not hide from scanners.

## Why it matters for ACI
Ni8mare predates 2.x, so our 2.43.7 is not affected — confirmed safe, no action. The coverage's real value is as a hardening reference: it validates our existing posture (n8n localhost-only on :5678, no public tunnel, local-only watchdogs) and documents why that posture is the cheap fix — "make n8n boring to the internet". The Shadowserver ~60k stat is a warning that the vuln window stays open long after fixes ship, which argues for keeping our nightly version-floor checks. Keep this file as the reference the next hardening audit cites.

## Sources (with dates)
- https://dev.to/cortexflow_tech/ni8mare-the-cvss-100-n8n-flaw-that-turns-a-webhook-into-a-full-server-takeover-5fkf — published ~2026-10-17, accessed 2026-10-20
- https://dev.to/cortexflow_tech/censys-counted-114000-exposed-n8n-instances-your-self-hosted-hardening-checklist-ck5 — published ~2026-10-15, accessed 2026-10-20
- https://www.morningstar.com/news/pr-newswire/20261014de71227/censys-2026-state-of-the-internet-report-finds-exposed-ai-infrastructure-grew-63-in-nine-months — Censys 2026 State of the Internet, released 2026-10-14

## Action
watch
