# Cloudflare Web Search API for AI agents (Oct 2, 2026)

## What changed
During Birthday Week on October 2, 2026, Cloudflare launched a **Web Search API inside AI Gateway**, currently in open beta. It is a router, not an index: three providers at launch — **Ceramic.ai** (default, own 40B-page index, $0.25/1k), **Linkup** ($5/1k, structured results with citations), **Exa** ($7/1k, semantic search tuned for RAG) — all returning one uniform result shape (title, URL, description), so switching providers is a single parameter. Requests flow through AI Gateway: one auth, one billing surface, gateway logs; billed at each provider's list price with **no Cloudflare markup** (AI Gateway credits, or bring-your-own provider key). All three providers support **Zero Data Retention** for Cloudflare requests. Limits at launch: max 10 results per request; a native server tool a model can call on its own is marked "coming soon".

## Why it matters for ACI
This is a cheap, key-aggregated web-search grounding layer purpose-built for AI agents — directly usable for ACI's mission research loops. Ceramic at $0.25/1k makes large-scale agent search runs affordable (10–30x cheaper than model-native search tools at $10–14/1k); Exa gives semantic/RAG-tuned retrieval; Linkup gives citation-structured results. It replaces juggling three search API keys with one parameter switch, and the ZDR posture suits intel work. Evaluate as the standard search tool for the ACI multi-agent platform; the 10-result cap and beta status mean keep the existing fallbacks until it matures.

## Sources (with dates)
- Cloudflare changelog, Oct 2, 2026: https://developers.cloudflare.com/changelog/product/web-search/
- Digital Applied price comparison, Oct 2, 2026: https://www.digitalapplied.com/blog/web-search-apis-for-ai-agents-compared-2026
- DEV Community analysis, Oct 2026: https://dev.to/ashraf_chowdury09/cloudflare-just-shipped-a-web-search-api-for-ai-agents-heres-what-the-hype-skips-1cg0

## Action
watch
