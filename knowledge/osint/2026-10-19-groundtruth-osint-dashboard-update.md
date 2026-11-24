# GroundTruth OSINT dashboard rebuild — free global monitoring, no signup

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — keep as a free analyst-side situation-awareness source; do NOT build platform dependencies on it (single-developer project, no SLA).

## What changed
- The author's 2026-10-17 DEV post announces a rebuilt **GroundTruth OSINT dashboard** (groundtruthosint.com): free live global event monitoring with ~170 feeds, live 3D globe (150 tracked events, clickable markers with "so what" context), ranked reports with keyword+priority search and triage queue, shareable deep links, "new since last visit" highlighting, optional NASA FIRMS / USGS earthquake / severe-weather layers, and a free daily morning email brief (6:30 AM ET).
- Stack per the author: one Cloudflare Worker + D1, 15-minute server-side poll/cluster/priority cycle, snapshot-backed API (cold load 38s → ~1.5s). Cost claimed: ~$5/month + bandwidth, donation-funded; no accounts, no paywall, mobile-friendly. Roadmap: user-defined watch keywords, source-diversity scoring.

## Why it matters for ACI
- Corporate-intel missions benefit from cheap situational awareness (facility incidents, protests, disruptions near client sites) — a no-key event dashboard is a usable analyst bookmark alongside our keyed feeds. The same "Ground Truth" outfit runs a news-site-style OSINT publication (groundtruth.day) we've cited before, so the feed curation has some editorial history.
- Caveats for the registry: single-developer, donation-funded, no SLA — it belongs in analyst tooling, not in the automated mission pipeline. If the promised watch-keywords feature lands with a stable snapshot API, revisit as a structured event source.

## Sources
- "GroundTruth OSINT UI update: free live global monitoring — 170 feeds, 3D globe, daily brief, no signup" — https://dev.to/osintwatchapp/i-rebuilt-my-free-osint-dashboard-170-feeds-3d-globe-daily-email-brief-no-signup-kb5 — 2026-10-17
