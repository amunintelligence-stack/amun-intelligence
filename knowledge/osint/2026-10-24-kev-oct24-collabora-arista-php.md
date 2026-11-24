# Oct 24 2026: CISA KEV additions + PHP unpatched RCE warning (not our stack)

## What changed
- CISA added two actively exploited flaws to the KEV catalog on Friday Oct 24, 2026
  (The Hacker News, Oct 24, 2026):
  - CVE-2026-110447 (CVSS 9.2) — OS command injection in Collabora Online Built-in
    CODE Server (richdocumentscode) inside Nextcloud, RCE via `proxy.php` when the
    local CODE document server is not running. Fixed in 26.4.303 (Sep 2026).
  - Arista VeloCloud Orchestrator (VCO) flaw (second KEV entry; details in the THN
    piece) — also under active exploitation.
- Separately, PHP warned Oct 24, 2026 of an UNPATCHED RCE path (CVE-2026-115560):
  session-upload serializer confusion. Mitigation until a routine fix lands: disable
  session upload progress (`session.upload_progress.enabled=Off`) and restart PHP
  workers. This is distinct from PHP2Shell; the PHP2Shell emergency releases
  (PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35, Oct 21) still stand.
- Same-day CVE batch (Oct 24, 2026, via TheHackerWire/NVD intake): CVE-2026-116014
  (open62541 integer overflow, 8.1, fixed 1.5.7), CVE-2026-116019 (Grav allowlist
  bypass, 8.8, fixed 2.2.13), CVE-2026-116009 (Camaleon CMS path traversal, 8.8,
  fixed 2.9.3), CVE-2026-116011 (Crow JSON recursion DoS, 7.5, fixed 1.3.4),
  CVE-2026-112866 (WPFactory Product Filter SQLi, 9.3). None confirmed exploited.

## Why it matters for ACI
- None of these products are in the ACI stack (Python/FastAPI backend, n8n, Postgres/
  SQLite, networkx). No action on ACI itself.
- Kept as threat-pattern reference: (1) KEV additions keep arriving on Fridays — the
  nightly KEV check stays worth doing; (2) the PHP case is a second "unpatched, use a
  config mitigation" story in one week after PHP2Shell — a reminder that "patched
  branch" is not the same as "no open exposure" when a vendor issues interim guidance.

## Sources
- The Hacker News, Oct 24, 2026:
  http://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html
- Spartech Software, "PHP CVE-2026-115560: Unpatched RCE Risk Emerges", Oct 24, 2026:
  https://www.spartechsoftware.com/cybersecurity-news/php-cve-2026-115560-unpatched-rce/
- TheHackerWire CVE intake, Oct 24, 2026 (116014 / 116019 / 116009 / 116011 / 112866).

## Action
- IGNORE for ACI stack (no Collabora, Arista VCO, PHP, open62541, Grav, Camaleon,
  Crow, or WPFactory in use). Keep the Friday KEV check in the nightly routine.
