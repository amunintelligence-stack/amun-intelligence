# Weaviate 1.40.0 — Namespaces + drop vector index GA, MUVERA, RQ-4 quantization

**Date:** 2026-10-16 (release 2026-10-07)
**Source:** https://blog.elest.io/elestio-catalog-updates-125-new-releases-this-week-october-4-10-2026/ (secondary — Elestio catalog roundup; verify against Weaviate release notes before any decision)

## What changed
- Weaviate 1.40.0 (7 Oct 2026): **Namespaces** and **drop vector index** are now generally available. Namespaces require a license.
- Adds **MUVERA** (multi-vector retrieval via fixed dimensional encodings) for HFresh and **RQ-4 quantization**.
- Patch builds 1.39.9–1.39.11 and 1.38.19–1.38.20 also shipped; **1.39.11 pins zlib for CVE-2026-85091**.

## Why it matters for ACI
Namespaces = native multi-tenancy (per-case / per-client collections without separate clusters) — the same tenancy problem ACI will hit if missions ever isolate per client. MUVERA is a multi-vector retrieval technique relevant to the hybrid-search work tracked in RAG notes: it compresses many per-token vectors into one fixed-size encoding, a cheaper alternative to full ColBERT-style late interaction. The zlib pin is a reminder to audit transitive C dependencies in any vector-store container we run. None of this changes the current stack (TF-IDF V1 → Qdrant target), but it keeps Weaviate as a credible alternative if the Qdrant plan ever stalls.

## Action
**Watch.** Record Namespaces + MUVERA as reference points for the next vector-store evaluation. No change to the Qdrant upgrade plan.
