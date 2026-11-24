# Google SERP-collection breakage — rank trackers returned partial results; Ranktracker restored Top 100 on 1 Oct

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **From ~17 Sep 2026**, Google changed how search results are delivered to automated systems. Rank-tracking providers began retrieving incomplete SERPs: in tests, some tools returned only **1–3 listings** from page one, result counts varied between repeated requests, crawls stopped after one or two pages, and keywords were incorrectly reported as lost because deeper results could not be retrieved.
- **Ranktracker** investigated across **20+ competing platforms**, then restored full Google Top 100 tracking (desktop + mobile) on **1 Oct 2026**, and published its technical investigation "Is Your Rank Tracker Actually Tracking Accurately?" on 7 Oct 2026 (announced 8 Oct 2026).
- **Provider divergence confirmed by practitioners (Sep–Oct 2026):** for the same sites, Ahrefs picked up drops/recoveries promptly, Semrush picked them up late, and Sistrix missed them entirely in the reported cases. Multiple SEOs reported trackers "not fully working" as of 9–12 Oct 2026.
- **MozCast handoff:** Dr. Pete Meyers (Moz) noted on 9 Oct 2026 that he has "documented and handed off MozCast as best as I'm able" and that "Google certainly doesn't make it easy to maintain" — a signal that even Google-volatility monitors are under maintenance strain.

## Why it matters for ACI

- ACI's SEO data sources (Semrush, Ahrefs, Moz, SERP APIs) all sit downstream of this breakage. Any ranking/visibility figure collected 17 Sep – mid-Oct 2026 from an affected provider may reflect collection failure, not real movement. ACI must treat that window as low-confidence unless the provider confirms its collection was intact.
- The incident proves the value of ACI's multi-provider design: no single rank source is trustworthy during a SERP-delivery change. ACI briefs should carry a per-provider collection-health note during such windows.
- Ranktracker's 20-platform test methodology (re-request the same SERP, compare result counts, check deep positions) is a cheap self-test ACI can run against its own SERP providers before trusting a mission's ranking data.
- MozCast's maintenance strain is a watch item: if volatility monitors degrade, ACI loses an independent "is Google turbulent today" signal and must rely on cross-provider disagreement as its turbulence proxy.

## Sources

- EINPresswire / Ranktracker, "Ranktracker Restores Google Top 100 Rankings as SEO Platforms Face Widespread Disruptions" (8 Oct 2026) — https://www.einnews.com/pr_news/948157260/ranktracker-restores-google-top-100-rankings-as-seo-platforms-face-widespread-disruptions
- Search Engine Roundtable, "Third-Party Google Rank Tracking Not Fully Working Now" (12 Oct 2026) — https://www.seroundtable.com/third-party-google-rank-tracking-broken-42272.html
- Ranktracker technical investigation (7 Oct 2026), linked from the EIN release — https://www.ranktracker.com/blog/is-your-rank-tracker-accurate/

## Action

**Adopt** — SERP self-test (repeat-request + deep-position check) before trusting ranking data; low-confidence flag for 17 Sep – mid-Oct 2026 ranking series. **Watch** — MozCast continuity and whether other providers confirm full restoration.
