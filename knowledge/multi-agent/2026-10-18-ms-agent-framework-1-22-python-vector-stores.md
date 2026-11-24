# Microsoft Agent Framework Python 1.22.0 + experimental native Python vector stores (Oct 2026)

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — experimental APIs + alpha/beta DB packages; pattern-only reference for ACI memory layer until stabilized.

## What changed
Microsoft Agent Framework (our designated AutoGen-migration candidate) moved to Python 1.22.0 in October 2026 (registry last covered 1.21.0), with Python 3.15 support aligning Python and .NET release lines. More significant: in an Oct 15, 2026 announcement, Microsoft added *experimental* native Python vector-store support for RAG and agent memory — carrying Semantic Kernel's vector-store design forward with two new architectural pieces: `VectorCollectionContextProvider` (vector search exposed as safe callable tools for agents) and `VectorStoreHistoryProvider` (manages long-running conversation history to prevent context-window blowout). Microsoft explicitly flags the APIs as experimental and the DB integration packages as alpha/beta.

## Why it matters for ACI
Two direct pattern references for our stack: `VectorCollectionContextProvider` models exactly what we need when our TF-IDF/Qdrant RAG becomes agent-callable memory (typed, callable vector search instead of ad-hoc wrappers), and `VectorStoreHistoryProvider` is a shape to copy for mission-history retention as mission graphs grow. Keep MAF on the migration watchlist; nothing to adopt while experimental — design patterns transfer, experimental packages don't belong in our stack yet.

## Sources
- "Microsoft Agent Framework Setup: 13 Steps [2026]" — https://tech-insider.org/microsoft-agent-framework-setup-2026/ — 2026-10
- "Microsoft Agent Framework Adds Experimental Python Vector Stores for RAG and Agent Memory" — https://windowsforum.com/news/microsoft-agent-framework-adds-experimental-python-vector-stores-for-rag-and-agent-memory.448460/ — 2026-10-15
