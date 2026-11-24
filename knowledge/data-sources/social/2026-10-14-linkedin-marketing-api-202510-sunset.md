# LinkedIn Marketing API — version 202510 sunset 15 Oct 2026, Company Intelligence API, geo migration

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **Version sunset:** LinkedIn Marketing API version **202510** is sunset on **15 Oct 2026** (tomorrow). Monthly versions in `YYYYMM` format are supported for at least a year; a request with a retired version returns HTTP 426 `NONEXISTENT_VERSION`, and omitting the `Linkedin-Version` header returns 400 `VERSION_MISSING`. Earlier versions 202508 (17 Aug 2026) and 202509 (15 Sep 2026) already sunset.
- **Company Intelligence API (documented Sep 2026):** a company (target-account)-level API returning engagement score, paid impressions, paid clicks, leads, paid qualified leads, conversions, paid video views, cost per paid qualified lead (CPQL), organic impressions and organic engagements, plus firmographics (company size, industry, HQ country/region). Positioned for attribution tooling.
- **Legacy Geo removal:** from 31 Aug 2026 LinkedIn stopped supporting Legacy Geo for ads targeting; campaigns created with legacy geo return 400 `INVALID_VALUE_FOR_FIELD`. All targeting must use Bing-geo.
- **Profile location field removal:** the top-level `location` field is being removed from `/v2/me` and `/v2/people` responses (empty/null); migrate to the `geoLocation` field with the `geo~` projection.
- **Access reality check (Oct 2026):** the only permissions open to every developer are sign-in (`profile`, `email`) and posting on the member's behalf. People search, profile lookup by anything other than a known Person ID, and most other data require an approved partner program (e.g. SNAP). No self-serve endpoint lets an ordinary developer search people by title/company.

## Why it matters for ACI

- Any ACI LinkedIn integration pinned to `202510` breaks tomorrow (15 Oct). Pin the `Linkedin-Version` header to a live version (e.g. `202606` or later) in one constant, and add a calendar reminder for its sunset.
- Company Intelligence API is the closest thing to a legitimate company-level LinkedIn intel feed — engagement + firmographics per target account. It needs an approved ads-account context, so it fits ACI's "own-account" data path, not open collection.
- The access reality check confirms ACI must not promise LinkedIn people-search via the official API. For people discovery, the legitimate routes are partner programs, or clearly-labelled third-party data vendors (with their own ToS/legal review) — never credentialled scraping.
- Geo migration: any stored LinkedIn geo targeting or location fields in ACI missions must move to Bing-geo / `geoLocation`, or queries will start 400ing.

## Sources

- Microsoft Learn, "Recent Marketing API Changes — LinkedIn" (accessed Oct 2026; lists 202510 sunset 15 Oct 2026) — https://learn.microsoft.com/vi-vn/linkedin/marketing/integrations/recent-changes
- Microsoft Learn, "Company Intelligence API" (Sep 2026 versioned docs) — https://learn.microsoft.com/en-us/linkedin/marketing/account-intel/account-intel-api?view=li-lms-2026-09
- DEV Community, "Is the LinkedIn API free? Pricing and posting access in 2026" (13 Oct 2026) — https://dev.to/frandeveloper/is-the-linkedin-api-free-pricing-and-posting-access-in-2026-4im9
- DEV Community, "How to Scrape LinkedIn Profiles Without Logging In (Python, 2026 Guide)" (13 Oct 2026, documents official-API limits) — http://dev.to/azzamahmed/how-to-scrape-linkedin-profiles-without-logging-in-python-2026-guide-llp

## Action

**Adopt** — bump `Linkedin-Version` off `202510` before 15 Oct 2026; migrate geo fields to Bing-geo / `geoLocation`. **Watch** — Company Intelligence API for an approved-account pilot. **Ignore** — LinkedIn people-search via official API (not available self-serve).
