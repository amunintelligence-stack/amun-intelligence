# Perplexity Agent API presets (low/medium/high) switch to Fast Search, Oct 13 2026

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — in any ACI/Perplexity Agent API integration, explicitly pin `search_type: "web"` for low/medium/high presets now; adopt Fast Search defaults only after re-validating recall on intel queries.

## What changed
- Per the October 2026 Perplexity API changelog (reported ~13 Oct): the Agent API's `web_search` tool for the **low, medium, and high presets now defaults to `search_type: "fast"`** (matching the existing `fast` preset); only **xhigh** keeps standard web search.
- Cost per web-search invocation drops from **$2.50 to $1.00 per 1,000 calls** (60% reduction on the search-tool line), and Perplexity claims ~800ms less latency.
- Silent behavior change: any integration that uses a preset without explicitly setting `search_type` now takes a different retrieval path even though its own code didn't change. Developers can restore the old path with `search_type: "web"`.
- Same October window: Agent API added native PDF/DOC/DOCX/TXT/RTF file input plus an `image_search` tool (returns image + source-page URLs); pplx-decider v1.1 (Oct 6, open weights Apache 2.0, $0.02/M input on hosted API) and v1.2 on Vercel AI Gateway (Oct 17) extend the Decisions family.

## Why it matters for ACI
- **ACI's Perplexity direct-probing pattern is directly affected:** Fast Search is cheaper and faster but its recall/quality trade-off on deep intel queries is unmeasured — treat preset defaults as a moving target and pin `search_type` explicitly in any mission pipeline.
- The new native document input + `image_search` tool widens Perplexity as a one-call evidence source: upload a leaked document or suspect image and get cited answers with source pages — useful for document-authenticity and image-provenance checks.
- Decision models (pplx-decider, OpenAI Decisions API) are new typed-answer primitives (predicate/choice/score with probabilities) relevant to evidence triage (e.g., "does this review report a defect?" → probability), but the hosted Decisions API had an Oct 13 bug report (near-uniform probabilities), so treat as experimental, not production.

## Sources
- "Perplexity Switches Low, Medium and High Agent API Presets to Fast Search" — https://netcontentseo.com/article/perplexity-switches-low-medium-and-high-agent-api-presets-to-fast-search-1385 — 2026-10-13
- "Perplexity's Decider V1.2 models now available on AI Gateway" — https://techbytes.app/posts/perplexitys-decider-v12-models-now-available-on-ai-gateway/ — 2026-10-17
- "Decisions API returns near-uniform probabilities for every question, including the quickstart example" — https://community.perplexity.ai/t/decisions-api-returns-near-uniform-probabilities-for-every-question-including-the-quickstart-example/6348 — 2026-10-13
- "Changelog - Perplexity" (docs) — https://docs.perplexity.ai/docs/resources/changelog — 2026-10-17
