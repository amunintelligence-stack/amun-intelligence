# Meta switches product browsing ON by default for existing ads, 28 Oct 2026

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — flag in any Ad Library-based ad-intel pipeline: from 28 Oct, a tap on an ad may open a Meta-hosted product page, not the brand's site, so "destination URL" evidence must be read against the new default.

## What changed
- Advertisers received notice (~14 Oct 2026, reported by PPC Land 15 Oct and MediaPost 16 Oct): **from 28 October 2026 Meta adds product browsing to existing Facebook/Instagram ads unless the advertiser opts out** (toggle lives in Advantage+ Creative / Destination controls).
- Meta claims an August experiment (6–21 Aug, ~117,700 advertisers, ecommerce/CPG/retail) averaged **+3% conversions** with >99% reported confidence; conversion event and comparison method were not defined.
- The notice does not specify which placements/formats/objectives are covered, whether newly created ads inherit the default, or the opt-out scope (account vs portfolio).
- Related, same week: Meta announced updated Commercial + Self-Serve Ad Terms effective **30 Oct 2026** — advertisers become legally responsible for AI-generated content in their ads (even when Meta's own tools create it), and Meta gains broad rights to crawl advertiser websites and use the content for AI model training.

## Why it matters for ACI
- **Ad-destination evidence changes meaning:** taps now land on a Meta-controlled product layer instead of the brand website, so click-through/destination analysis of Meta ads must note the product-browsing setting as a confounder.
- **Completeness caveat joins the 8-Oct ByteDance-ban caveat:** combined with the TikTok-destination ad ban in 7 markets (incl. Egypt), Meta Ad Library interpretation now needs at least two standing policy-artifact warnings.
- The Oct-30 terms change also means brands whose sites get crawled by Meta for AI training may appear more prominently in Meta's own ad/storefront surfaces — a small reputational-footprint signal.

## Sources
- "Meta will turn on product browsing in existing ads on October 28" — https://ppc.land/meta-will-turn-on-product-browsing-in-existing-ads-on-october-28/ — 2026-10-15
- "Social Ad Clicks Are Becoming Platform-Owned Storefronts" — https://missionmedia.asia/social-ad-storefronts/ — 2026-10-18
- "Meta's New Ad Terms Take Effect October 30: What Ecommerce Brands Must Know Before the Deadline" — https://commonthreadco.com/blogs/coachs-corner/metas-new-ad-terms-take-effect-october-30-what-ecommerce-brands-must-know-before-the-deadline — 2026-10-09
