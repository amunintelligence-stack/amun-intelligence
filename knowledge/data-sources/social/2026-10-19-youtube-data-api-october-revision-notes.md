# YouTube Data API revision notes, Oct 2026 (comments imageUrl property, madeForKids clarification)

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — no action needed for existing social-intel usage; note the new comment-image field for future sentiment/evidence pipelines (available to all users November 2026).

## What changed
- Google's YouTube Data API (v3) revision history, official docs:
  - **15 Oct 2026:** `videos.list` documentation clarified — `status.selfDeclaredMadeForKids` and `status.madeForKids` are only updated when explicitly specified in the request and are **not overridden if omitted**.
  - **30 Sep 2026:** new `snippet.imageUrl` property on the `comments` resource — URL for an image or animated GIF attached to a comment. Available to all users in November 2026.
  - **14 Sep 2026:** `thumbnails.set` / `playlistImages.insert` max upload size raised from 2MB to 50MB.
  - **11 Sep 2026:** `fhd` (1080p), `qhd` (1440p), `uhd` (4K) thumbnail sizes now documented for some videos.
  - **1 Sep 2026:** `videos.getRating` accepts the narrower `youtube.readonly` OAuth scope.
- Context (stable, not new): since June 2026 the default quota is split into buckets — 100 `search.list` calls/day, 100 `videos.insert` calls/day, and 10,000 units/day for all other methods; quota extensions still require a compliance audit.

## Why it matters for ACI
- `comments.imageUrl` (Nov 2026) adds a new evidence primitive for social-intel: comments with attached images/GIFs become machine-collectable via the official API — relevant to reputation missions that track image-based complaints or memes.
- The madeForKids clarification is a correctness note only; the quota-bucket model is now the baseline assumption for any YouTube API budget in mission design (100 free searches/day/project).

## Sources
- "Revision History | YouTube Data API | Google for Developers" — https://developers.google.cn/youtube/data/revision_history?hl=en — 2026-10-15 (changelog, crawled 2026-10-17)
- "How a YouTube API Quota Extension Works" — https://adaptlypost.com/blog/youtube-api-quota-extension — 2026-09-27
