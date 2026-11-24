# Meta Graph/Marketing API v26: 27 Oct 2026 enforcement + attribution change

**Date noted:** 2026-11-02
**Category:** data-sources / social — capture-rule update (no ACI connector change)

## What changed
- **27 Oct 2026 enforcement (all API versions, not just v26.0):** Meta removed the Commerce Order Management API (47 endpoints, no replacement); dropped legacy protocol features (pretty, debug, date_format, ?ids= root requests, ETag caching); removed three Delivery Estimate fields; dropped the Messenger Stories placement; poll ads can no longer be created; Web+App campaigns refuse web-only creatives. (Overads tracker, updated 2 Nov 2026, sourced from Meta's v26.0 changelog; ACI's 11 Oct note covered the deadline, this is the enforcement detail.)
- **Attribution change (same window):** the default click-through conversion now counts **link clicks only** — not the broader clicks (photo expand, profile tap, reaction-then-buy) that previously fed the number — plus a new **1-day engage-through window**. Dashboards and Ads Manager can now disagree on the same campaigns while both are "right" under their own settings.
- Google Ads API v26 (14 Oct 2026) sunset planned November 2027 — noted for the ads-side timeline; no ACI Google Ads connector exists yet.

## Why it matters for ACI
- Any future Meta reporting connector, and any ad snapshot taken from 27 Oct onward, must be read under the new rules: (1) **record capture date + API version + attribution setting** on every snapshot — pre-27-Oct numbers are not comparable to post-27-Oct numbers without re-baselining; (2) Delivery Estimate fields and Commerce Order Management endpoints are gone on every version — pinning an old version does not restore them; (3) the link-clicks-only change means click-through series break at 27 Oct — flag the break in any trend chart, do not smooth over it.
- This extends ACI's existing ad-intel capture rules (country + date on every snapshot; US political blackout 27 Oct – 3 Nov) with an attribution-setting field.

## Action: WATCH
- No connector change (none exists). Add "attribution setting + API version" to the ad-snapshot capture checklist at the next mission-template touch.

## Sources (checked 2026-11-02)
- Overads API pricing/policy tracker, updated 2 Nov 2026: https://overads.io/blog/social-platform-pricing-and-policy-changes
- Attribution explainer (Vertex Agency, 2 Nov 2026): https://vertexagencyin.medium.com/your-meta-ads-didnt-get-worse-your-attribution-changed-d636302f578e
- Prior ACI notes: 2026-10-11-meta-graph-v26-october-deadline.md, 2026-10-24 ad-intel capture rules
