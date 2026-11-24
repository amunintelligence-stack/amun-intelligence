# Google Ads API v26 — Search Lift measurement + twice-monthly release cadence

**Date of finding:** 2026-10-17
**Window covered:** last ~30 days

## What changed

- **Google released v26 of the Google Ads API on 15 Oct 2026** (announced on the Google Ads Developer Blog; client libraries and code examples published the same day). Headline features:
  - **Search Lift measurements:** new read-only `SearchLiftKeywordBundle` resource + `segments.search_lift_keyword_bundle` / `segments.search_property` segmentation + **15 new Search Lift metrics** (including `relative_search_lift`, `normalized_incremental_searches`, `search_lift_impressions`) alongside `Campaign.lift_measurement_config`. Search Lift measures how much ads increase search activity vs. the no-ads counterfactual — now pullable programmatically instead of checked manually in the UI.
  - **Local Services Performance Max campaign creation:** lead, coupon, and message conversion support — but the campaign type must be locked in at launch.
  - **Streamlined EU political advertising declarations:** `Campaign.contains_eu_political_advertising` now optional for campaigns / Demand Gen ad groups that positively target only non-EU locations with no proximity/location-group criteria; new `require_eu_political_advertising_declaration` field on `GeoTargetConstant`, `CampaignCriterion`, `AdGroupCriterion`.
  - **Vertical-agnostic travel bid modifiers:** hotel-specific `AdGroupBidModifier` criteria renamed to apply across travel verticals (`user_set_dates`, `advance_booking_window`, `length_of_booking` with min/max days, `start_day_of_week`, `start_date_range`).
  - **Unified enhanced conversions configuration**, Shopping and Demand Gen enhancements, SMS messaging, hotel center accounts, EU political items, conversion features.
- **Release cadence change (the structural news):** Google is moving the Ads API to **approximately twice-monthly releases starting with v26** (up from monthly since 2025). Still **four major versions per year**; extra releases are minor, non-breaking. Major versions keep ~1 year of support; minor releases sunset with their parent major. Tentative schedule: v26 (Oct 2026) → v26.1, v27 (Jan 2027), v28 (Apr 2027), v29 (Jul 2027), v30 (Oct 2027).
- **Sunset schedule:** v23 → Feb 2027; v24 → May 2027; v25 → Aug 2027.
- **Same-week ads context (16 Oct):** Meta introduced new brand advertising formats across Facebook and Instagram; Google launched Universal Cart in Search and Gemini (US, powered by the Universal Commerce Protocol) — both expand the ad-transparency surfaces ACI watches, but neither changed an API ACI consumes.

## Why it matters for ACI

- **Search Lift is a new evidence type for ACI's ads/transparency work:** when a mission asks "did this brand's ads move the market?", Search Lift gives a programmatic, advertiser-side incrementality signal (incremental searches, relative lift) — complementary to the Ad Library / Ads Transparency surfaces ACI already tracks. It is advertiser-authenticated data, so ACI can only use it for clients who grant API access — it is not a public scraping surface.
- **Cadence change = maintenance load:** twice-monthly releases mean ACI's Google Ads connector (currently stubbed — needs a developer token + client credentials) must pin a major version and treat minor releases as routine, not events. The v23/v24/v25 sunset dates go on the connector's calendar the day it is built.
- **EU political declarations matter for compliance missions:** the new `require_eu_political_advertising_declaration` check is a clean, checkable signal for "is this campaign declaring EU political advertising?" — directly useful for DSA / political-ads transparency checks in the ads connector.
- **No immediate action:** the Google Ads connector in ACI is still a stub (see tools.yaml — needs user dev token). v26 changes nothing about that; it changes what the connector should request when it is built.

## Sources

- Google Ads Developer Blog (via PostGoo mirror), "Announcing v26 of the Google Ads API" (14–15 Oct 2026) — https://postgoo.com/posts/6ad1f1148e3aa3dadc6d3509?type=article
- Search Engine Land, "Google Ads API moves to twice-monthly releases starting with v26" (Oct 2026) — https://searchengineland.com/google-ads-api-moves-to-twice-monthly-releases-starting-with-v26-495545
- Search Engine Roundtable, "Google Ads API Version 26 Now Out" (15 Oct 2026) — https://www.seroundtable.com/google-ads-api-version-26-42307.html
- Search Engine Roundtable, "Daily Search Forum Recap: October 16, 2026" (16 Oct 2026) — https://www.seroundtable.com/recap-10-16-2026-42318.html (Meta brand formats, Universal Cart)

## Action

**Watch:** when the Google Ads connector is built, target v26 (Search Lift + EU political-declaration check as first-class fields), pin the major version, and calendar the v23/v24/v25 sunsets. **Ignore** — chasing every twice-monthly minor release; track majors only.
