# Google: Custom Search JSON API retires 2027-01-01; google.com/goto anti-scraping redirects roll out (~Oct 2026)
- Date: 2026-10-11 | Category: data-sources/seo | Action: **ADOPT** (migrate any Google-API-based SERP sourcing to a third-party SERP API before 2027-01-01)

## What changed
- **Custom Search JSON API sunset confirmed for 2027-01-01.** Google's docs state the API is already closed to new customers (new keys return 403; existing customers keep access until 2027-01-01). Until then: 100 free queries/day, $5 per 1,000 above that, 10,000 queries/day cap. Programmable Search Engine also restricted: engines created since 2026-01-20 must use "Sites to search" (max 50 domains); existing whole-web engines keep their setting only until the sunset.
- **Migration rush is visible in the wild (Sept–Oct 2026):** SpeedyIndex (link-indexing service) ran a customer survey (2026-09-21) to decide which Google SERP data products to build next, citing the sunset — candidates include AI Overview citations, index-drop alerts, bulk site: counts.
- **google.com/goto redirect rollout (~Oct 2026):** per Nozzle's reporting (~Oct 9, 2026), Google is rolling out redirects through google.com/goto with tokens that cannot be decoded client-side, forcing scrapers to follow every redirect to resolve destination URLs. Context given: the ongoing Google vs SerpApi lawsuit and large-scale AI-company scraping.
- Corroborating shifts: `num=100` parameter was removed (Sept 2025), so deep rank tracking now costs 5–10x more requests.

## Why it matters for ACI
- The ACI seo connector notes list third-party SERP providers; any future plan to use Google's own official API must be discarded — **there is no free/official JSON SERP path after 2027-01-01** (only site-restricted Vertex AI Search / Agent Search, which do not search the open web).
- The goto-redirect change raises the cost floor of DIY SERP scraping: any scraping-based rank-tracking or AI Overview citation work must now follow redirects at production scale (bandwidth + rate-limit risk). This strengthens the case for paying for a structured SERP API (e.g., DataForSEO Live SERP, ~$2.00 per 1,000 queries) rather than maintaining scraping infrastructure.

## Sources (links with dates)
- http://dev.to/rbatista19/what-should-i-migrate-to-now-that-googles-custom-search-json-api-is-retiring-3hgk — 2026-10-07 (migration guide; cites Google docs on the 2027-01-01 deadline)
- https://github.com/wnrj9204/serp-scraping-api/blob/HEAD/README.md — updated 2026-09-22 (documents num=100 removal, Custom Search sunset)
- http://finance.minyanville.com/minyanville/article/accwirecq-2026-9-21-speedyindex-asks-customers-which-serp-data-to-build-as-google-custom-search-api-nears-shutdown — 2026-09-21
- https://bizscoreai.com/blog/google-search-google-com-goto-tracking-parameters/ — ~2026-10-09 (Nozzle goto-redirect rollout report)

## Action (adopt / watch / ignore — one concrete recommendation)
**Adopt** — Record DataForSEO Live Google SERP as the primary planned SERP source for the ACI seo connector (pay-as-you-go, $0.002/10 results), and rule out Google Custom Search JSON API for any new work; if any ACI pipeline currently uses Custom Search, schedule migration before 2027-01-01.
