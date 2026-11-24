# YouTube Data API — videoTrainability, batchGetStats, quota buckets, Brand Account auth incident

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **New `videoTrainability` method (Oct 2026):** the YouTube Data API discovery document now includes a method reporting whether a video's owner allows third parties to train AI models on it — returning `all`, `none`, or a list of permitted parties. It exposes the opt-in setting YouTube introduced in Dec 2024 letting creators authorise named AI companies.
- **New `batchGetStats` method:** retrieve statistics on several videos in one call, instead of one `videos.list` per video.
- **Quota buckets (in force since 1 Jun 2026, confirmed in Oct 2026 write-ups):** default projects get 100 `search.list` calls/day (Search Queries bucket), 100 `videos.insert` calls/day (Video Uploads bucket), and 10,000 units/day combined for all other endpoints. Upload cost dropped from ~1,600 units to ~100 in Dec 2025. Every request — including invalid ones — costs at least 1 unit.
- **Brand Account auth incident (8–12 Oct 2026):** a YouTube-side change broke authorisation of YouTube Brand Accounts; channel connections showed as disconnected and reconnects only helped temporarily. YouTube reverted the change; the incident was marked resolved 12 Oct 2026, 06:47 UTC, with a one-time reconnect advised for still-disconnected channels.

## Why it matters for ACI

- `videoTrainability` is a machine-readable consent signal for training use — ACI must check it before treating any YouTube video's content as training/indexing material, and can record it as provenance metadata on YouTube evidence. Honouring it is a differentiator, not just compliance.
- `batchGetStats` cuts quota spend on bulk channel/video profiling — the exact pattern ACI uses when sizing a target's YouTube footprint. Route all multi-video stats through it.
- The quota buckets change capacity planning: search is now the binding constraint (100/day default), not the general pool. Any ACI mission doing broad YouTube search needs a quota-increase request or a paginated, budgeted search plan; note each extra results page costs the full method price again.
- The Brand Account incident is a reminder that YouTube-side auth changes can silently invalidate stored channel connections. ACI connectors should surface a "reconnect required" state rather than failing missions quietly.

## Sources

- PPC Land, "Explaining YouTube Data API" (updated ~12 Oct 2026) — https://ppc.land/youtube-data-api/
- Outstand, "YouTube API Pricing 2026: Quota, Upload Limits, Real Costs" (updated ~15 Sep 2026) — https://www.outstand.so/blog/youtube-api-pricing-quota
- Pingoru / Swat.io incident timeline, "YouTube channels repeatedly disconnecting" (8–12 Oct 2026) — https://pingoru.io/providers/swatio/incidents/12188325

## Action

**Adopt** — use `batchGetStats` for bulk stats; record `videoTrainability` on YouTube evidence; add Brand-Account reconnect detection to the YouTube connector. **Watch** — quota-increase approval path for `search.list`.
