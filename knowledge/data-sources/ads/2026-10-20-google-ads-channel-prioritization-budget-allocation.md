# Google Ads channel prioritization + budget allocation (Oct 14, 2026)

## What changed
On October 14, 2026, Google announced two new optional campaign controls for Search, Shopping, Performance Max and Demand Gen: **channel prioritization** (mark Google Search, search partners and the Display Network as High or Low priority) and **budget allocation** (a percentage-of-daily-budget cap on channels marked Low). Rollout started October 15 and lands over the coming months. Google Ads Product Liaison Ginny Marvin confirmed (Oct 16) that both controls are **supported in the Google Ads API at launch**, are fully testable in experiments, are compatible with shared budgets, and that Performance Max advertisers can set Search partner allocation to 0%. Google also enabled **full placement reporting for the Search Partner Network**. Hard deadline: Search campaigns that still use the Display Network lose their current spend setup in **February 2027**.

## Why it matters for ACI
Ad-intelligence coverage of Google gains a new segmentation dimension: per-channel priority and budget-allocation percentages are now enumerable signals for competitive ad analysis. The full Search Partner Network placement reporting is a genuinely new data surface for tracking where rivals' ads appear. If ACI schemas model Google ads, they should accommodate channel-priority and allocation fields now; the February 2027 enforcement will shift advertiser behavior, so pre/post baselines should be annotated.

## Sources (with dates)
- Google Ads & Commerce Blog, Oct 14, 2026 (Tal Akabas announcement; via PPC Land: https://ppc.land/google-ads-lets-advertisers-limit-display-and-partner-spend-by-percentage/)
- Ginny Marvin Q&A (Ads Decoded newsletter + X), Oct 16, 2026: https://ppc.land/google-ads-lets-pmax-advertisers-set-search-partner-spend-to-0-marvin-says/
- Draper Gold summary, Oct 19, 2026: https://m.drapergold.com/blog/google-ads-now-lets-you-rank-channels-and-cap-spend-on-the-rest.html

## Action
watch
