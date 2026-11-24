# Reddit RSS shutdown 13 Nov 2026 + Data API request window closed 31 Oct

## What changed
- **Reddit RSS feeds stop being supported 13 Nov 2026** (10 days from tonight). Anyone tracking subreddits or brand mentions through RSS loses that channel on that date.
- **New requests for public Data API access no longer accepted after 31 Oct 2026** (window already closed). Full public Data API closure follows in March 2027 (tracked 23 Oct nightly).
- Context from the Q4 deadline calendar (3 Oct 2026): these two dates sit alongside Meta Marketing API v24 expiry (6 Oct, passed), Google Ads API v22 sunset (Oct, tentative), and Gemini Flash introductory-price end (31 Dec).

## Why it matters for ACI
- Any future Reddit listening eval for ACI must be built on a path that survives 13 Nov (RSS is dead) and March 2027 (public API closes) — i.e. a contracted/paid route or no Reddit route at all. Do not design a mission flow around Reddit RSS now; the 10-day fuse makes it a wasted build.
- For current missions: if any existing collection uses Reddit RSS (none documented in the registry — verify at next audit), it breaks 13 Nov.

## Sources
- https://www.digitalapplied.com/blog/q4-2026-platform-deadline-calendar-marketers (3 Oct 2026, dated deadlines incl. Reddit RSS 13 Nov + Data API 31 Oct)
- Prior nightly: 2026-10-21 (Reddit Data API new-request deadline 31 Oct + RSS end 13 Nov), 2026-10-23 (full public API shutdown Mar 2027)

## Action
- **Adopt (practice)**: no Reddit-RSS-based collection design from tonight onward; flag the 13 Nov date in any social-listening eval doc.
- **Watch**: Reddit's contracted/paid access terms for any future listening decision (March 2027 closure is the hard wall).
