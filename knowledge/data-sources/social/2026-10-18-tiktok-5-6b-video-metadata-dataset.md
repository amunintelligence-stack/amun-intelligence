# 5.6B TikTok video metadata dataset posted to Hugging Face (datasocial / "hashfunction"), Oct 2026

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — eval the dataset offline for schema coverage only; never ingest into ACI pipelines given ToS provenance.

## What changed
A developer going by "hashfunction" published metadata for ~5.6 billion public TikTok videos to Hugging Face under the datasocial account (reported ~6 Oct 2026). The dataset spans July 2014–Oct 2026, ships as 460 GB of monthly Parquet files (free, ungated), and per-row carries caption, hashtags, sound ID, on-screen text, TikTok Shop product and seller IDs, engagement counts (views/likes/comments/shares/saves/downloads), plus TikTok's own labels for AI-generated flag and off-For-You-page status. Hugging Face counter shows ~1,181 downloads. The developer's write-up says the data came from TikTok's private mobile API with no login; TikTok's US ToS (sec 3.4) bars automated extraction without written approval, so the dataset's provenance is legally contested.

## Why it matters for ACI
This is the largest free, keyless TikTok corpus ACI could ever touch — creator vetting, TikTok Shop seller intel, and virality-pattern analysis would be natural fits for the social-intel connector stubs. But it must not enter production pipelines: provenance violates TikTok ToS, per-row quality is archive-dependent (AI flag empty for older videos), and commercial use is routed to a paid product (datasocial.ai, scraper source $1,699). Candidate only for isolated offline research, with ToS-compliant alternatives (Research API eligibility, TikAPI/EnsembleData) preferred for anything mission-grade.

## Sources
- "Someone Scraped 5.6 Billion TikTok Videos and Put the Data on Hugging Face for Free" — https://decrypt.co/380229/someone-scraped-5-billion-tiktok-videos-posted-data-hugging-face — 2026-10-06
- "The TikTok Ad Library API: A Developer's Honest Guide to the DSA Commercial Content Library" — https://dev.to/odeeb/the-tiktok-ad-library-api-a-developers-honest-guide-to-the-dsa-commercial-content-library-5446 — 2026-09-29
