# PerplexityBot crawler docs update — 29 Oct 2026: UA strings, IP ranges, WAF rules

**Date noted:** 2026-10-31
**Category:** data-sources / ai-search — crawler identification & collection hygiene

## What changed
- Perplexity updated its **crawler documentation** (change spotted ~29 Oct 2026 via page watcher; exact edit date approximate):
  - **User-agent strings shortened**: PerplexityBot's example UA is now `Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)` — the AppleWebKit/KHTML tokens were dropped. Same shortening for Perplexity-User. Version number noted as subject to change.
  - **IP-range files moved**: published ranges now listed at `perplexity.ai/perplexitybot.json` and `perplexity.ai/perplexity-user.json` (previously under perplexity.com).
  - **WAF guidance rewritten**: Cloudflare example now says match each bot's UA **against that bot's own IP ranges**, using a Skip action placed above any custom block/challenge rules; Cloudflare Bot Fight Mode cannot be skipped by custom rules and may still challenge Perplexity's bots. AWS WAF steps now pair an IP-set match with a UA match per bot.
  - Standing behavior reaffirmed: **Perplexity-User (the bot that visits a page when a person's question prompts it) generally ignores robots.txt**.
- Adjacent Perplexity October items (context, not the headline): Agent API `low`/`medium`/`high` presets switched to Fast Search (13 Oct changelog; $2.50 → $1.00 per 1,000 web-search invocations, ~800 ms less latency; `xhigh` stays on standard search); pplx-embed-v2-late released 7 Oct (0.6B edge + 9B models, MIT, Hugging Face; hosted API endpoint still planned, not live); Wiley journals/books searchable on all plans from 5 Oct.
- Prior ACI note: `2026-10-23-deepseek-search-fetch-api-launch.md` / `2026-10-29-deepseek-search-fetch-api.md` cover the competing search-fetch API; Perplexity's own embedding models were noted 2026-10-23 (`pplx-embed-v2-late`).

## Why it matters for ACI
- **Detection side**: if ACI missions identify AI-crawler traffic on a target (or audit a client's exposure to AI search), the UA + IP-range pair is now the correct fingerprint — UA alone is officially insufficient per Perplexity's own docs. Log-analysis playbooks should match UA *and* published IP range.
- **Collection side**: Perplexity-User ignoring robots.txt is a standing fact to keep in mind when assessing how a target's content reaches AI answers — robots.txt is not a barrier for that bot, and it is not a lever ACI can pull for a client either.
- **Cost side (if ACI ever uses Perplexity's Agent API)**: Fast Search defaults cut web-search invocation cost 60% for low/medium/high presets — but the changelog does not claim identical result quality, so a quality check is required before relying on it for mission-grade retrieval.

## Sources
- Doc-change report, posted 29 Oct 2026: https://anythingengineoptimization.com/item/2026-10-29-perplexity-updates-perplexitybot-and-perplexity-user-crawler/
- Agent API preset change, 13 Oct 2026 changelog: https://netcontentseo.com/article/perplexity-switches-low-medium-and-high-agent-api-presets-to-fast-search-1385
- Embedding models, 7 Oct 2026: https://www.artiverse.ca/perplexitys-new-embedding-models-target-faster-multimodal-search/

## Action: WATCH
- Update any ACI log-analysis / crawler-identification checklist to the UA+IP-range rule for PerplexityBot/Perplexity-User. No connector build, no crawl of Perplexity itself — this is identification hygiene for mission analysis.
