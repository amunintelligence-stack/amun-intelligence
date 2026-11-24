# AI-search APIs — Perplexity Agent API pinned effort versions (22–29 Oct) + ultra-preview; Exa 3.0 pricing steady

**Date noted:** 2026-11-01
**Category:** data-sources / ai-search — relevant: Perplexity/Exa are ACI's AI-search data-source candidates

## What changed
- **Perplexity's official changelog** (read 1 Nov 2026) pins new Agent API effort versions, each dated, with earlier versions staying available as pinned versions:
  - `fast@2026-10-16.0` — falls back to openai/gpt-5.6-luna when gpt-6-luna is unavailable.
  - `low@2026-10-24.0` — max output tokens 32,768 → 128,000; web_search max_tokens and max_tokens_per_page 2,000 → 4,000; fetch_url extraction via gpt-6-luna.
  - `medium@2026-10-22.1` — web_search token caps 2,000 → 4,000; fetch_url extraction via gpt-6-luna.
  - `high@2026-10-28.0` — model switches to gpt-6.1-terra (from gpt-6-sol); max steps 15 → 40 (max 40 tool calls); web_search caps 2,000 → 4,000.
  - `xhigh@2026-10-29.0` — stays on claude-opus-5-5 with gpt-6.1-sol fallback; max steps 100 → 300; context compaction from 150,000 tokens; no system prompt sent (frozen config no longer sends `instructions`).
  - **New: `ultra-preview`** — effort level for broad research/coverage-first gathering; runs can take a long time.
- This follows the 13 Oct change already on record (low/medium/high presets defaulting to Fast Search: $1 vs $2.50 per 1,000 web_search invocations, ~800ms less latency; xhigh stays on standard search). The late-Oct versions raise token/step budgets substantially — a coverage-vs-cost trade that missions should pin explicitly rather than float on "latest".
- **Exa 3.0** (18 Oct, covered 22/25/27 Oct): pricing confirmed steady in the 20 Oct follow-ups — Auto $7 / Lite $4 per 1,000 requests; Dynamic Highlights GA (vendor claim: 95% fewer tokens than full page text); self-reported benchmark leads (BrowseComp 91.8%, ATLAS 42.0%) remain vendor-run, not independent.

## Why it matters for ACI
- If ACI missions ever call Perplexity's Agent API, **pin the effort version** (e.g. `high@2026-10-28.0`) — unpinned calls silently inherit budget/model changes like the 15→40 step jump, which changes cost and latency profiles mid-mission. The 4,000-token web_search caps also change how much retrieved text lands in context per call.
- `ultra-preview` is the coverage-first option for deep company dossiers, but "runs can take a long time" makes it unsuitable for time-boxed mission steps — watch only.
- Exa Lite at $4/1k remains the cheapest independent-index search tier on record; no change to the Exa-vs-Perplexity comparison from 27 Oct.

## Action: WATCH
1. No integration change. Record the pinning rule: any future Perplexity Agent API use pins an effort version, never "latest".
2. Keep Exa 3.0 Lite as the cost floor in the ai-search comparison.

## Sources (checked 2026-11-01)
- Perplexity API changelog (official, primary): https://docs.perplexity.ai/docs/resources/changelog
- Perplexity Fast Search preset change (13 Oct 2026): https://netcontentseo.com/article/perplexity-switches-low-medium-and-high-agent-api-presets-to-fast-search-1385
- Exa 3.0 follow-ups (20 Oct 2026): https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/ and https://dailyaibrief.com/news/exa-labs-releases-exa-3-0-search-engine-for-ai-agents-m1WXEyz8
- Prior ACI notes: 2026-10-27-exa-3-0-lite.md, 2026-10-22-exa-3.0-perplexity-api.md, 2026-10-31-perplexitybot-docs-oct29.md
