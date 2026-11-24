# TikTok Creative Center has NO public API — internal endpoint broke Oct 2026; Meta v24 expired

## What changed
- **No public TikTok Creative Center API exists.** The Creative Center (ads.tiktok.com/business/creativecenter) is a JS frontend calling TikTok's internal, signed `creative_radar_api` (per-session headers: anonymous-user-id, timestamp, user-sign; datacenter IPs refused — residential proxy required). That internal endpoint **broke for trending data in October 2026** — the month the "build on an undocumented endpoint" risk stopped being theoretical.
- **Official TikTok alternatives** (documented, keyed, contract-backed): Commercial Content API (Europe-only ad transparency data, 10 records/call, via TikTok for Developers), Research API (public content research), Marketing API (campaign management). None returns the Top Ads inspiration feed.
- **Meta Marketing API v24.0 expired 6 Oct 2026** (v25.0, Feb 2026, is the current line). Google Ads API moved to v25 (Adverity 2026.43, week of 19 Oct; lead contact details no longer include email; Keyword Planner Forecast columns removed). TikTok Ads dropped Reservation Ads service type + catalog dimensions from Dynamic Product Ads reports.
- **Ad-platform AI assistants** (Advertising Week NY, 5–6 Oct): TikTok Smart+ (Search Ads Campaign automation, Smart+ Creative Selection approval workflow, GMV Max) and Meta AI business assistant inside Ads Manager (Creative Studio insights, lifecycle recommendations). Advertiser approval still gates everything that goes live — a draft is not a publish.
- **Meta v26 enforcement** (27 Oct, tracked 2 Nov) + product-browsing default-on (28 Oct) + new business terms (30 Oct, Meta may crawl linked sites) remain the capture rules for ad snapshots: record country + date + attribution setting.

## Why it matters for ACI
- ACI's ads-intel sources list TikTok Creative Center as a keyless source. Correct classification: **not an API — an undocumented internal endpoint that broke in Oct 2026**. Any future TikTok ads collection must either accept the Europe-only Commercial Content API (contract, narrow) or budget for signed-session scraping with residential egress and a breakage contingency. Do not present Creative Center scrapes as a stable source in mission reports.
- Meta v24 expiry + Google Ads v25 migration are version-floor reminders for any future paid connector: pin the API version in the connector config and track expiry dates (Meta v21 Graph expiry is already on the early-2027 calendar).

## Sources
- https://adextract.co/blog/tiktok-creative-center-api (Nov 2026, no-API finding + Oct 2026 breakage)
- https://docs.adverity.com/reference/release-notes/version-2026-43.html (week of 19 Oct 2026, Google Ads v25 + TikTok removals)
- https://www.digitalapplied.com/blog/q4-2026-platform-deadline-calendar-marketers (3 Oct 2026, Meta v24 expiry 6 Oct)
- https://p2plabs.asia/blog/en/the-ad-platforms-will-draft-the-campaign/ (Oct 2026, Smart+/Meta assistant)

## Action
- **Adopt (practice)**: reclassify TikTok Creative Center in ACI source notes as "undocumented internal endpoint, broke Oct 2026 — unstable, not API-backed"; prefer Commercial Content API for any contracted TikTok ads work (Europe-only scope noted).
- **Watch**: Meta v25/v26 line for any future Meta connector; TikTok internal-endpoint recovery (unannounced, do not depend on it).
