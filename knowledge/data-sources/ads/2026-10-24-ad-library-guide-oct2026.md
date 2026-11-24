# Ad-library landscape, Oct 2026: retention gaps + Meta US political blackout window

## What changed
- AdLibraryGuide comparison (data as of Oct 8, 2026, from each platform's own docs):
  - Meta Ad Library: Facebook/Instagram/Messenger/Audience Network/Threads,
    keyword search; ordinary ads kept after they stop ONLY if shown in EU/UK (1 year);
    spend shown for political ads only, as a range.
  - Google Ads Transparency Center: advertiser/website search only (no keyword);
    1-year retention; election-ad spend only, as a range; ads are static screenshots
    with no landing-page click-through.
  - LinkedIn Ad Library: keyword search, 1-year retention, ads since June 1, 2023,
    no spend.
  - TikTok Commercial Content Library: EEA/UK/Switzerland/Türkiye only, 1-year
    retention; TikTok bans political ads, so no spend data. Creative Center Top Ads
    is a separate curated, global selection.
  - Microsoft Ad Library, Pinterest Ads Repository, X Ads Repository, Snap Political
    & Advocacy Ads Library: all EU/EEA-scoped, ~12-month retention, no commercial
    spend.
- Why the EU sees more: the EU Digital Services Act drives the extra fields — Meta
  adds reach/targeting, Google adds impressions/targeting categories, LinkedIn adds
  impressions/targeting parameters for EU-served ads. The same advertiser's US-only
  ads show creative + advertiser + date and little else.
- Same-day country variance measured Oct 8, 2026: one Nike Page showed ~35 active ads
  from the US view vs ~82 from the France view — country selection changes results
  materially, so ACI ad-intel captures must always record the country filter used.
- Meta US political ads: PPC Land (Oct 2026) reports Meta will block new US political
  ads Oct 27 – Nov 3, 2026. During that window, the library's low-impression labels
  help show whether a late ad started before the cut-off — a time-sensitive
  collection note for any US political-ad monitoring.

## Why it matters for ACI
- ACI's ads connectors already treat the official libraries as keyless baselines and
  paid tools (GetHookd, BigSpy) as the gap-fillers for inactive/historical creative.
  This comparison sharpens the gap list: no official library publishes commercial
  spend; non-EU/UK ordinary Meta ads vanish entirely once they stop; Google gives no
  keyword search and no landing-page link.
- Operational rules to add to ACI ad-intel missions: (1) always record country +
  date of capture (results are country-dependent); (2) capture EU/UK views when
  retention matters (they persist 1 year); (3) for US political-ad timelines, collect
  before/during the Oct 27 – Nov 3 blackout window — after it, late starters are
  harder to evidence.

## Sources
- AdLibraryGuide (data Oct 8, 2026): https://adlibraryguide.com/
- PPC Land, "Explaining Ads Library" (Meta US political blackout Oct 27 – Nov 3, 2026):
  https://ppc.land/ads-library/
- TopGrowthMarketing, "TikTok Ads Library: How to Search & Use It (2026 Guide)":
  https://topgrowthmarketing.com/tiktok-ads-library/page/3/?et_blog

## Action
- WATCH + ADOPT the capture rules (record country + date; prefer EU/UK views for
  retention; collect US political ads around the Oct 27 – Nov 3 window). No new
  connector; paid gap-fillers stay as-is.
