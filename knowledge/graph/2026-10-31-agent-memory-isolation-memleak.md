# MemLeak — cross-user leakage in multi-tenant agent memory (NeurIPS 2026 PALM workshop)

**Date noted:** 2026-10-31
**Category:** graph / memory / agent safety — applies to ACI Memory + RAG + Graph layers

## What changed
- **MemLeak** (Mudgal et al., Workday AI Research; NeurIPS 2026 Workshop PALM) formalizes *cross-user admissibility failure*: in a multi-tenant deployment where agents share one vector store, an ordinary cosine-similarity query can retrieve **another user's memories** — no exploit, no adversarial intent required.
- Measured results (sparse TF-IDF and production-faithful MiniLM-L6-v2 retrieval, six experiments + ablations):
  - **Incidental leakage 70–100%** under pooled same-team retrieval.
  - Adversarially crafted memories reach **90–100% top-k placement**, with score lifts of +0.416 to +0.511 under dense retrieval.
  - End-to-end response contamination **5.00/5** under a production retrieval path, **4.67/5** with Claude Sonnet 4.5 — contaminated answers often scored as helpful or *more* helpful than clean ones (validated against human judgment).
  - Of three architectural mitigations tested, **only hard post-retrieval ownership gating** consistently restored the clean baseline (1.00/5) across two generation models, at ~**1.4 ms per query** overhead.
  - Strict user partitioning (the ACL baseline) drives passive leakage to **0%** — confirmed in their own experiments.
- Adjacent confirmations the same month:
  - **Spring AI CVE-2026-41712**: a shared default conversation ID could expose one user's chat memory to another (same failure class, framework-level).
  - A second MemLeak paper (Wang & Zhang, Georgia Tech; arXiv 2606.29788) shows the deletion side: after "forgetting" a fact, retained correlated text enables **18.3% recovery** and retained images **12.0%** (47% of image leaks not text-recoverable); content-aware semantic deletion cuts the image residual to 2.0% but does not eliminate it.
  - Vendor data point (treat as vendor-reported, not independent): FalkorDB reports per-user graphs with 81,500 graphs in one production cluster, and 0.3–0.5 ms per-user memory deletion vs 150–190 ms on Neo4j in their benchmark.

## Why it matters for ACI
- ACI's Memory API + RAG + graph evidence store will hold **multi-target, multi-mission** material. The MemLeak result maps directly: if mission memories ever share one pooled index with only a metadata filter (or a filter applied after top-k), cross-mission leakage is the *default* outcome, not an edge case — and the leaked context will look helpful, so reviewers won't catch it.
- Design rule this study justifies: **scope inside the query + hard post-retrieval ownership gate**, never filter-after-top-k; and for strict separation, **one namespace/graph per mission (or per client)**, not one pooled index with a `mission_id` tag.
- Deletion matters too: a "delete this mission's memory" operation must purge embeddings, graph edges, and derived facts — text-only deletion leaves recoverable residue (12–18% in the study).
- This is a design constraint for future work, not a vulnerability in today's ACI (single-operator, local deployment). No incident, no patch needed now.

## Sources
- Primary: MemLeak, NeurIPS 2026 Workshop PALM — https://arxiv.org/html/2610.04195
- Deletion-side study: https://arxiv.org/pdf/2606.29788 (Wang & Zhang)
- Practitioner synthesis of the same controls: https://www.aicassindra.com/blogs/llm_security/agent_memory_security.html (6 Oct 2026)
- Vendor benchmark cited as vendor-reported: https://www.falkordb.com/blog/agent-memory-for-long-running-agents/

## Action: ADOPT (as a design rule)
- Write into ACI's memory/RAG architecture notes: per-mission namespace + ownership gating after retrieval + content-aware deletion checklist. Apply when the multi-mission memory store is built; do not retrofit under time pressure. No code change tonight (research only).
