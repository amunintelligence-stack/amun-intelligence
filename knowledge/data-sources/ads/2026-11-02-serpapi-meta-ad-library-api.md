# SerpApi launches Meta Ad Library API (week of 26 Oct – 1 Nov 2026)

**Date noted:** 2026-11-02
**Category:** data-sources / ads — paid fallback route (ACI's baseline stays keyless)

## What changed
- SerpApi's weekly changelog (26 Oct – 1 Nov 2026) adds a **Meta Ad Library API**: scrape ads across Facebook, Instagram, Messenger, WhatsApp, Threads, and Audience Network. Search by keyword, advertiser page, or both; filter by country, ad category, active status, media type, platform, language, and date range; sort like the Ad Library itself.
- Per ad it returns: Library ID, run dates, platforms, advertiser page, text, images, videos, carousel cards, call to action, plus spend / impressions / estimated audience size / payer **on political and social-issue ads** (i.e., the fields Meta only publishes for political ads — consistent with ACI's existing capture rules).
- Same changelog also adds a Google Books API and a Google Translate API (up to 5,000 chars, 249 languages) — noted, not intel-relevant.

## Why it matters for ACI
- ACI's ads baseline is keyless (Meta Ad Library web UI + the keyless facebook-ad-library-mcp-cli eval). SerpApi's API is the first **structured, paid fallback** that covers the same surface with filters ACI would otherwise hand-build (country + date-range + media-type filtering in one call). It does not change what Meta publishes — political-ad spend stays the only spend data — so it is a collection-convenience upgrade, not a data-coverage upgrade.
- Cost note: SerpApi is already in the registry as a paid watch candidate (AI Overview reference parsing). No pricing for the Ad Library API was in the changelog; price before any eval.

## Action: WATCH
- No purchase, no key. If the keyless Ad Library path ever breaks or rate-limits a mission, SerpApi's Ad Library API is the first paid fallback to price — reuse the existing SerpApi registry entry (append the Ad Library note there).

## Sources (checked 2026-11-02)
- SerpApi changelog, week of 26 Oct – 1 Nov 2026: https://serpapi.com/blog/serpapi-weekly-changelog-october-26-november-1-2026/
- Prior ACI notes: 2026-10-09 (facebook-ad-library-mcp-cli eval), Meta Ad Library registry entry (27 Oct cliff notes)
