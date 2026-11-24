# Meta creative audience pairing — per-creative age/gender audiences (19 Oct 2026)

**Date noted:** 2026-10-31
**Category:** data-sources / ads — Meta Marketing API

## What changed
- Meta announced **"Choose an audience for each ad creative"** on its developer blog on **19 Oct 2026** (post by Graham Mahon and Mohamed Khalil). Marketing API partners could see and test it from that day; the toggle appeared in Ads Manager a day later (20 Oct, reported by Jon Loomer).
- What it is: within one ad set, **each image/video creative gets its own age range and gender**, instead of demographics living only at ad-set level. In API terms the feature is **creative audience pairing**; each creative's audience is called a **persona**.
- Example from Meta: a financial-services advertiser pairs retirement-planning videos with ages 50–65 while showing savings-account videos to all ages.
- Constraints (from Meta's API reference, as reported): the ad set must allow minimum age 18–25, maximum age 65, and all genders; it **cannot be combined with Advantage+ audience**. Ads Manager text notes an ad "may also reach others likely to respond" beyond the selected audience — pairing is a direction, not a hard fence.
- The post lists the affected ad set, ad, and ad creative endpoints but names no specific objectives, placements, or markets. Loomer observed it on by default in Sales campaigns (once you further limit reach) and off by default for other objectives, with no objective-based restrictions found.
- Context: this lands after the 27 Oct 2026 removals (Messenger Stories placement, poll ads, Delivery Estimate fields) tracked in `2026-10-29-meta-marketing-api-v26-oct27-removals.md` and `2026-10-30-meta-marketing-api-oct27-deadlines.md`. Any future Meta reporting connector must target **v25/v26** and drop the removed fields.

## Why it matters for ACI
- For ad-intelligence missions, creative-level audience pairing is a **new observable dimension**: the same ad set can now carry different demographic targeting per creative. A future Meta Ad Library / Marketing API connector should record **per-creative personas** (age band + gender) alongside the creative, not just ad-set-level demographics — otherwise two creatives in one ad set will look identically targeted when they are not.
- It also changes interpretation: a creative reaching outside its paired audience is by design ("may also reach others likely to respond"), so audience-vs-reach mismatches are no longer automatically an anomaly.
- No immediate build: ACI has no Meta connector yet (the keyed-connector list is still future work). This is a schema note for when one is built.

## Sources
- Announcement summary with API-reference constraints: https://gradezilla.org/meta-audience-for-each-ad-creative/ (reporting Meta's 19 Oct 2026 developer post and Jon Loomer's 20 Oct observations)
- October change calendar (v24 expiry 6 Oct, 27 Oct removals): https://mockingbird.digital/blog/meta-ads-changes-october-2026

## Action: WATCH
- Record per-creative persona fields in the future Meta connector schema. No connector exists yet, so no code change. Re-check the persona field names against Meta's API reference at build time — the announcement post does not name the exact field set for every endpoint.
