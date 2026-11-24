# Google September 2026 spam update — traffic volatility makes modelled estimates unreliable in-window

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **Google's September 2026 spam update** began rolling out globally on **24 Sep 2026** and completed **8 Oct 2026**, across all languages (per Google's Search Status Dashboard). Google published no detailed list of targeted spam techniques; established spam policies apply (link spam, keyword stuffing, scaled content abuse, cloaking, misleading redirects). AI-generated content is not automatically spam — the test is whether content provides genuine value or exists mainly to manipulate rankings.
- **Real traffic damage documented:** one site owner-confirmed case showed a site "hammered" on **29 Sep** during the update — a near-total drop picked up by Ahrefs promptly, by Semrush late, and not at all by Sistrix at the time of reporting (7 Oct 2026). A second case showed a near-100% drop followed by full recovery around the **4 Sep** unconfirmed update, with the same tool divergence (Ahrefs caught the recovery, Semrush lagged, Sistrix missed it).
- **Compounding factor:** from ~17 Sep 2026 Google also changed how search results are delivered to automated systems (see the companion SEO note on SERP-collection breakage), so third-party visibility series and modelled traffic estimates in this window mix real ranking change with collection failure.

## Why it matters for ACI

- Any ACI traffic estimate, visibility trend, or "site dropped X%" claim dated mid-Sep to mid-Oct 2026 is suspect until cross-checked across at least two providers. A single-provider series in this window can show a phantom drop (collection failure) or miss a real one (slow pickup).
- The Ahrefs-vs-Semrush-vs-Sistrix divergence is itself evidence: when providers disagree in-window, ACI should report the disagreement and lower confidence rather than picking the most dramatic number.
- For target profiling, a spam-update casualty is signal, not noise: a site that lost most traffic on 29 Sep and did not recover is a materially different entity (possible link-spam / scaled-content operator) than one with a stable series. ACI should annotate Sep–Oct 2026 traffic series with the update window.
- Missions that compare "before/after" traffic around this window need a wider baseline (pre-Sep) and an explicit caveat in the brief.

## Sources

- Theta Solutions, "Google October 2026 Spam Update: SEO Guide" (13 Oct 2026, cites Google Search Status Dashboard: 24 Sep – 8 Oct 2026) — https://thetasolutions.pk/blog/google-october-2026-spam-update/
- Search Engine Roundtable, "Third-Party Google Rank Tracking Not Fully Working Now" (12 Oct 2026; Glenn Gabe / Lily Ray posts 7–8 Oct 2026) — https://www.seroundtable.com/third-party-google-rank-tracking-broken-42272.html

## Action

**Adopt** — cross-provider verification + confidence downgrade for any traffic/visibility claim dated 17 Sep – 14 Oct 2026; annotate the spam-update window on traffic charts. **Watch** — whether providers converge once collection stabilises.
