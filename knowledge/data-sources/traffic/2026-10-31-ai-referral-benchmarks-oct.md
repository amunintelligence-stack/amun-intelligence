# AI referral traffic benchmarks — October 2026: under 0.5% of visits, but growing fast

**Date noted:** 2026-10-31
**Category:** data-sources / traffic — measurement baseline for ACI traffic analysis

## What changed
- Converging October-2026 measurements of AI-assistant referral traffic (all panels agree on direction, differ on size — they measure different things):
  - **Ahrefs Web Analytics benchmark (Sep 2026, 100k+ sites): AI referrals = 0.43% of all visits** (~4 in 1,000).
  - **SE Ranking (early 2026): 0.32%**, up from 0.02% in 2024 (~16x).
  - **Similarweb (Jun 2025–May 2026): 770.7M AI referral visits/month worldwide**, more than double the year before; every tracked industry grew ≥115% YoY (Beauty +312.5% but from a small base).
  - **Kevin Indig / Growth Memo analysis of Similarweb estimates (10,000 US + 10,000 French domains, Sep 2023–Aug 2026, published 26 Oct 2026):** AI referrals = **2.85% of organic-search traffic in the US** (2.44% France), roughly **0.5% of total visits**. US organic-search visits fell **13.2%** (19.9B → 17.3B) and France **24.4%** over Aug 2024–Aug 2026, while paid search rose 21% / 17.3%. Indig stresses the data **cannot establish whether AI or paid search caused the organic losses**.
  - **ChatGPT's share of AI referral traffic: 74.78%** (SE Ranking 2026) to 87.4% (Conductor 2025 enterprise sample); Similarweb notes ChatGPT's share of AI-chatbot web traffic fell ~76% → ~53% over a year as Gemini rose to ~27–28%.
- Measurement caveat carried forward: a ChatGPT bug stripped the tracking tag from many links from ~**8 Oct 2026** (fix began 15 Oct; OpenAI has not commented publicly), so October AI-referral figures are **undercounted** toward Direct — already tracked in `2026-10-27-ai-referral-traffic-chatgpt-tag-bug.md`. Any October reading must carry that asterisk.
- Related: Chartbeat's 2026 Publisher Playbook (via Reuters Institute) found Google Search referrals to news/media sites down **40.2%** Jul 2025–Jul 2026; Ahrefs measured a **58% lower CTR** for top-ranking pages when an AI Overview appears (vs 34.5% in Apr 2025).

## Why it matters for ACI
- Traffic analysis is a core ACI data-source category (Similarweb/Ahrefs). The baseline to use in mission reporting: **AI referrals are real but still <0.5% of total visits; organic search is down double-digits over two years, and attribution is noisy**. Quoting a single vendor's AI-referral share without the panel and the tag-bug asterisk would mislead a client.
- For competitor/company traffic narratives: AI-referral growth (2x YoY) is a trend line, not yet a dominant channel — but the October tag bug means Q4 AI-referral readings will look artificially soft; note the bug window in any Oct–Nov traffic comparison.
- Cross-reference: `2026-10-25-semrush-similarweb-accuracy-787-sites.md` (panel accuracy limits) and `2026-10-30-google-q3-ai-mode-query-growth.md` (Google's AI Mode growth) remain the companion notes.

## Sources
- Benchmark synthesis, updated 22 Oct 2026, 15 sources: https://enleaf.com/ai-referral-traffic-statistics/
- Indig/Similarweb 10k-domain study, published 26 Oct 2026: https://anythingengineoptimization.com/item/2026-10-26-similarweb-data-organic-search-visits-fall-13-in-us-ai-referrals-stay/
- Publisher/CTR context: https://for.you.com/posts/google-ai-overviews-cut-publisher-search-traffic-40-in-a-20ce4622

## Action: WATCH
- Adopt the <0.5% baseline + tag-bug asterisk as the standard framing for AI-referral claims in ACI traffic reporting. No tooling change; no new vendor needed.
