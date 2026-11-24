# Subfinder 2.17.0 + Blackbird username recon — 2026-11-03 nightly

## What changed
- **subfinder 2.17.0** (ProjectDiscovery, released 8 Oct 2026): two new passive sources — **crtname** and **subdomaincenter** — plus `-match-regex` / `-filter-regex` options and concurrent enumeration of several domains. Independent re-check (darknet.org.uk, 13 Oct run, no API keys): 17 subdomains in 14 s, only `www` resolving — a reminder that passive lists are candidates, not assets.
- **Maintenance reality check** (same source, Oct 2026): Sublist3r last commit July 2020, assetfinder April 2020 — both effectively unmaintained. OWASP Amass v5.1.1 (Apr 2026) remains the heavyweight alternative; subfinder has shipped three releases since August.
- **Blackbird** (7.3k stars, cited 5 Oct 2026): username-or-email search across 600+ platforms with an AI-generated PDF profile summary. New arrival for the username-intel shelf alongside Sherlock/Maigret.

## Why it matters for ACI
- Subfinder is already ACI's primary passive enumerator (wipe-proof binary, 2.17.0 noted 22 Oct). The new keyless sources widen keyless coverage — the 26 Oct count (37/58 sources need keys, ~20 keyless usable) should be re-measured with crtname/subdomaincenter added.
- Sublist3r's inactive status was already downgraded 30 Oct; this confirms it — keep it secondary-only, never the sole subdomain source in a mission report.
- Blackbird is a candidate eval for username missions: email-input support is the differentiator vs Sherlock (username-only). PDF summary is a reporting convenience, not evidence — verify hits before citing.

## Sources
- https://www.darknet.org.uk/2026/10/subfinder-passive-subdomain-enumeration-tool/ (Oct 2026, 2.17.0 detail + maintenance comparison)
- https://tau-home.com/en/post/five-open-source-osint-tools-for-digital-footprint-self-audit/ (5 Oct 2026, Blackbird/SpiderFoot/theHarvester roundup)
- https://osrepos.com/repo/aboul3la-sublist3r (snapshot 3 Nov 2026: inactive, no commits >1 yr)

## Action
- **Watch**: re-measure subfinder keyless-source coverage at the next tool-update window; eval Blackbird (username + email input) against Sherlock/Maigret on a known handle before any mission use.
- **Adopt (practice)**: mission reports must note subdomain-source coverage (keyless vs keyed) and never present a passive list as verified assets.
