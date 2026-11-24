# Perplexity Agent API (Oct 2026) — Fast Search presets, native file input, image_search tool

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **Fast Search becomes the default for most Agent API presets (Oct 2026 changelog):** the `low`, `medium`, and `high` presets for Agent API `web_search` now use `search_type: "fast"` (the `fast` preset already did). Reported effect: web-search invocation cost falls from **$2.50 to $1.00 per 1,000 calls**, with ~**800 ms** less latency. `xhigh` remains on standard web search; developers can explicitly set `search_type: "web"` to keep the standard retrieval path.
- **Native file input (Oct 2026):** Agent API added native **PDF, DOC, DOCX, TXT, and RTF** input — documents can be sent directly instead of being pre-extracted.
- **New `image_search` tool (Oct 2026):** returns image and source-page URLs, giving agents a visual-evidence path alongside text search.
- **Context:** this follows the 1 Oct 2026 Decisions API launch (`pplx-decider-v1-27b`, covered 2026-10-12) — Perplexity is shipping a full agent stack (decide → search → act) in one month.

## Why it matters for ACI

- Cheaper + faster default search directly lowers ACI's cost per AI-search probe: missions that fan out many web searches should default to `low`/`medium`/`high` presets and reserve `xhigh` (standard search) for high-stakes verification passes where source coverage matters more than cost.
- The Fast Search switch is a **quality caveat, not a free lunch**: Perplexity's changelog does not establish identical sources or quality across modes. ACI should A/B its own probe set (same questions, fast vs standard) once and record which preset its retrieval-quality gates accept.
- Native file input removes a whole extraction step from ACI's document-intel path (PDF reports, DOCX filings, RTF dumps can go straight to the Agent API). Keep ACI's own extractor as fallback for scanned/image PDFs, but stop pre-extracting clean text files.
- `image_search` gives ACI a legitimate route to visual evidence (logos, screenshots, product images with source pages) without scraping image search pages.

## Sources

- Perplexity API Changelog (October 2026), as reported by NetContentSEO, "Perplexity Switches Low, Medium and High Agent API Presets to Fast Search" (12 Oct 2026) — https://netcontentseo.com/article/perplexity-switches-low-medium-and-high-agent-api-presets-to-fast-search-1385
- ScriptByAI, "Perplexity AI Timeline: Products, Models & APIs" (updated 7 Oct 2026; Oct 2026 Agent API entry) — https://www.scriptbyai.com/perplexity-ai-timeline/
- Note: primary source is docs.perplexity.ai changelog; figures above are as reported by secondary coverage — verify pricing/latency against the official changelog before budgeting.

## Action

**Adopt** — default ACI Perplexity probes to `medium`/`high` (Fast Search); keep `xhigh`/`search_type: "web"` for verification passes; send clean documents natively. **Watch** — run one fast-vs-standard quality A/B on ACI's own probe set.
