# Reddit public Data API — new-access requests close 31 Oct 2026; RSS shutdown 13 Nov

**Date noted:** 2026-10-31 (deadline day)
**Category:** data-sources / social — Reddit access

## What changed
- Per Reddit's published Q4 calendar, **31 Oct 2026 is the last day new requests for public Data API access are accepted**. Teams planning a Reddit listening/research integration after today cannot start a new public-access request through that route.
- Next date on the same calendar: **13 Nov 2026 — RSS feeds stop being supported**. Anyone tracking subreddits or brand mentions through RSS loses that channel on that date.
- This is the arrival of deadlines announced earlier and already tracked: `2026-10-21-reddit-data-api-oct31-deadline.md`, `2026-10-23-reddit-public-api-rss-full-shutdown.md`, `2026-10-29-reddit-api-rss-closure-full-timeline.md`.
- Honest status note: this file records the **deadline falling today per Reddit's published calendar**, not an independently verified confirmation that the request form closed — the form's live state was not re-checked tonight. Treat "closed" as calendar-expected, and verify before citing it to a third party.

## Why it matters for ACI
- Reddit is a key social-listening source for corporate-intel missions (brand mentions, executive discussion, breach chatter). Any future Reddit connector must now be planned around **existing approved access or an alternative route** (e.g. enterprise/commercial data arrangements) — the free public on-ramp is gone as of today.
- RSS-based subreddit tracking, if ever used as a cheap collection fallback, has a **13-day remaining life** — do not build anything new on it; anything already RSS-based needs a migration plan before 13 Nov.
- No ACI impact today: ACI has no Reddit connector and no RSS-based collection in production.

## Sources
- Q4 2026 deadline calendar (Reddit rows, sourced from Reddit Help Center, read 3 Oct 2026): https://www.digitalapplied.com/blog/q4-2026-platform-deadline-calendar-marketers
- Prior ACI notes: `2026-10-21-reddit-data-api-oct31-deadline.md`, `2026-10-29-reddit-api-rss-closure-full-timeline.md`

## Action: WATCH
- If a Reddit source is ever scoped for ACI, start from "public Data API onboarding closed 31 Oct 2026" and price the commercial route first. Kill any RSS-based collection idea before 13 Nov 2026.
