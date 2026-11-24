# Meta Marketing API — 27 Oct 2026 cliff: poll ads deprecated, delivery-estimate fields gone for ALL versions, Commerce Order Management removed

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **27 Oct 2026 is a hard cliff, not a version migration.** Several Graph API v26.0 / Marketing API v26.0 changes (announced 29 Jul 2026) apply to **all remaining API versions, including unversioned calls**, on 27 Oct 2026. Pinning an older version does NOT defer them.
- **Delivery-estimate fields removed:** `daily_outcomes_curve`, `budget_guardrail`, and `estimate_dau` disappear from `GET /{ad-account-id}/delivery_estimate` and `GET /{adset-id}/delivery_estimate`. The call still returns 200 with a valid object — the fields are simply gone, with **no replacement API**. Code that reads them silently gets nulls.
- **Poll ad creation deprecated:** `poll_spec` and the `poll` type under `interactive_components_spec` are unavailable when creating/updating ads and creatives. Updates that do not change the creative can continue.
- **Commerce Order Management API removed:** all 47 endpoints (order details, items, payments, refunds, shipments, returns, cancellations, tax settings) are removed for all versions on 27 Oct 2026. The underlying Facebook/Instagram Shops checkout was sunset; no replacement API exists.
- **Shop Ads defaulting (v26.0+):** eligible ad creatives automatically default to `destination_spec.destination_type = WEBSITE_AND_SHOP` when the advertiser has a shop; opt out explicitly with `WEBSITE_AND_SHOP_OPT_OUT`.
- **Access-tier changes:** "Ads Management Standard Access" renamed to "Marketing API Access Tier" ("Standard Access" → "Limited access", "Advanced Access" → "Full access"); auto-approval threshold lowered from 1,500 to 500 Marketing API calls in 15 days; error-rate calculation now a rolling 500-request window (< 15%); screen-recording requirement removed for tier-upgrade submissions.

## Why it matters for ACI

- This is the most actionable ads-intel deadline this month: **13 days out**. Any ACI code, connector, or mission template touching Meta delivery estimates, poll ads, or commerce orders must be patched before 27 Oct — and the delivery-estimate failure mode is silent (200 + nulls), so ACI needs an explicit field-presence check, not just status-code handling.
- For ad-intel missions, the Ad Library itself is unaffected, but forecasting ("what would this campaign deliver") loses its only official estimation surface. ACI should stop promising reach/budget forecasts derived from these fields and note the removal in affected briefs.
- The tier changes lower the bar to Full access (500 calls) — good news if ACI needs a higher Marketing API tier; the rolling error window means sloppy retry loops now count against tier standing.
- Shop Ads defaulting changes what "destination" means in creative analysis: creatives that previously went to a website may now resolve to website+shop. ACI ad-creative parsing should record `destination_type` explicitly.

## Sources

- Meta for Developers, "Graph API and Marketing API v26.0 Changelog" (released 29 Jul 2026; 27 Oct 2026 all-versions enforcement) — https://developers.facebook.com/docs/graph-api/changelog/version26.0/?locale=en_US
- Meta for Developers, "Marketing API changelog" (updated 21 May 2026; tier rename, 500-call threshold) — https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog
- DEV Community, "On October 27, Meta's Ad API Stops Returning Three Delivery Estimate Fields. Pinning Your Version Won't Save You." (1 Oct 2026) — http://dev.to/driftsignal/on-october-27-metas-ad-api-stops-returning-three-delivery-estimate-fields-pinning-your-version-4d62
- Meta for Developers blog, "Introducing Graph API v26.0 and Marketing API v26.0" (29 Jul 2026) — https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/

## Action

**Adopt** — before 27 Oct 2026: remove reads of the three delivery-estimate fields (add field-presence alerts), strip poll fields from creative specs, drop Commerce Order Management calls, record `destination_type` on creatives. Consider applying for Full access under the new 500-call threshold.
