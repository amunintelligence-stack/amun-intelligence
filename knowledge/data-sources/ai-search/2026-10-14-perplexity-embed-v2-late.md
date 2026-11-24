# Perplexity pplx-embed-v2-late — token-level late-interaction embeddings for text, images, rendered pages

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **Released 7 Oct 2026:** Perplexity released **`pplx-embed-v2-late`** in **0.6B and 9B** sizes for text and image retrieval. It uses **token-level (late-interaction) vectors** — a 128-dim vector per token — to search text, natural images, and **rendered document pages**. Both sizes share an embedding space, so the smaller model can query a document index built with the larger model. Both models are available on **Hugging Face**.
- **Opposite bet, same week:** on **6 Oct 2026** Google released **EmbeddingGemma 2** (740M params), a single-vector model whose vector can be truncated down to 128 dims — optimised for small indexes and on-device retrieval. Perplexity's model trades a much larger index for finer-grained matching that single vectors miss.
- **Pricing context (checked 2 Oct 2026):** Perplexity (Fast) search listed at $1.00/1,000 requests in the Cloudflare-adjacent price tracker; Exa at $7.00/1,000 (contents billed separately); Tavily basic at $8.00/1,000; Brave at $5.00/1,000 — relevant when choosing which retrieval stack backs ACI probes.

## Why it matters for ACI

- Late-interaction embeddings are a genuine retrieval-quality upgrade for ACI's RAG store: token-level matching finds answers buried in long filings, contracts, and reports where single-vector retrieval returns the wrong chunk. The 0.6B model querying a 9B-built index is a practical cost split (index once with 9B, serve with 0.6B).
- Rendered-document-page search is the standout: ACI evidence includes scanned PDFs, screenshots, and page renders — a model that retrieves over rendered pages (not just extracted text) closes the gap where text extraction fails.
- The shared-space design maps to ACI's tiered pipeline: heavy indexing offline, cheap querying at mission time. Evaluate 0.6B-vs-9B recall on ACI's own corpus before committing; index size grows roughly with token count, so storage/cost must be modelled.
- **Scope note:** this is filed under ai-search because it is a retrieval/search model release, but it overlaps the rag-vector category — the rag-vector researcher should treat this as a candidate embedding upgrade, not a duplicate topic.

## Sources

- ScriptByAI, "Perplexity AI Timeline: Products, Models & APIs" (7 Oct 2026 entry: pplx-embed-v2-late 0.6B/9B, Hugging Face) — https://www.scriptbyai.com/perplexity-ai-timeline/
- Towards AI, "Google Shrank Its Embeddings to Fit a Phone. A Day Later, Perplexity Gave Every Token Its Own." (12 Oct 2026; EmbeddingGemma 2 vs pplx-embed-v2-late, storage math) — https://pub.towardsai.net/google-shrank-its-embeddings-to-fit-a-phone-a-day-later-perplexity-gave-every-token-its-own-f7c2b55bf85f?gi=373a85e9bd8f
- SaaSCity, "Cloudflare Web Search API in AI Gateway: $0.25 per 1,000" (5 Oct 2026; 2 Oct 2026 price tracker) — https://saascity.io/blog/cloudflare-web-search-api-ai-agents-2026

## Action

**Watch** — benchmark pplx-embed-v2-late (0.6B querying a 9B index) against ACI's current embedding on ACI's own corpus; model index-size cost before adopting. **Ignore** — for now, replacing the whole RAG embedding stack on vendor benchmarks alone.
