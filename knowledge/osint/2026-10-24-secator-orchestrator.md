# secator — security-tool workflow orchestrator (Oct 2026 coverage)

## What changed
- secator, an open-source orchestrator for offensive-security toolchains, is getting fresh
  October 2026 coverage (OffSec blog, Oct 2026). It wraps a broad toolset behind one
  workflow engine with Celery-backed horizontal scaling for large scopes.
- Wrapped tools relevant to ACI recon: nmap, naabu, fping, arpscan, mapcidr, getasn
  (network); httpx, ffuf, feroxbuster, dirsearch, dalfox, arjun, x8, katana, gospider,
  cariddi (web); subfinder, dnsx, gau, xurlfind3r (passive recon); maigret (username
  dossiers), h8mail (email lookups), jswhois/whois; nuclei, trivy, grype, searchsploit,
  wpscan/wpprobe, gitleaks, trufflehog, testssl, sshaudit — plus msfconsole under an
  `exploit/attack` category.
- Each tool carries a category tag (`url/fuzz`, `dns/recon`, `user/recon/username`, …),
  which the engine uses to chain outputs of one class into inputs of another — the same
  shape as ACI's mission → agent-roster mapping.

## Why it matters for ACI
- ACI already owns the individual tools (subfinder, httpx, nuclei, ffuf, trufflehog,
  maigret-class username work). secator is not a new capability, it is a chaining pattern:
  category-tagged tool outputs feeding the next stage, with Celery scaling for /16-size
  scopes. That pattern is directly borrowable for ACI mission pipelines.
- Caution, recorded from the same coverage: msfconsole integration means secator can
  chain straight into exploitation — ACI must keep its recon-only scope discipline and
  never adopt the exploit category. Also note the rate-limit warning carried by the
  October bug-bounty roundup: nuclei/httpx/katana default to 150 req/s and ffuf is
  uncapped by default — any orchestrated run must set explicit rate caps per target
  scope, or it risks bans and out-of-scope traffic.

## Sources
- OffSec blog, "secator for orchestrating security tool workflows", Oct 2026:
  https://www.offsecblog.com/2026/10/secator-for-orchestrating-security-tool.html
- XHack, "Best Bug Bounty Tools for 2026" (subfinder v2.17.0, Oct 8 2026; rate defaults),
  Oct 2026: https://xhack.io/blog/bug-bounty-tools-2026

## Action
- WATCH. Borrow the category-tag chaining idea for ACI mission design; do not install
  secator and do not adopt its exploit category. Add explicit per-tool rate caps to any
  future orchestrated recon run (see rate-default warning above).
