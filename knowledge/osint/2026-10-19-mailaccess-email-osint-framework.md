# MailAccess — new MIT email-OSINT framework (holehe-replacement candidate)

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — evaluate `pip install mailaccess` in an isolated venv on the next tool-eval window; compare account-discovery coverage against our broken holehe before any registry change.

## What changed
- **MailAccess** (`KatrielMoses/MailAccess`, MIT) is a self-hostable email-OSINT framework that surfaced on Show HN / OSINT resource roundups the week of 2026-10-07. PyPI is already at **0.18.7** (crawled 2026-10-15), so it is iterating fast.
- Per the current PyPI docs (v0.18.7): **76 modules over a 5,300+ platform corpus**; investigations probe a bounded, evidence-first wave (~700 highest-signal platforms by default) rather than the whole corpus. Most modules are keyless; HIBP/SerpAPI/Shodan etc. are optional.
- Notable internals: a **native Maigret engine** (2,500+ platform coverage, no Maigret runtime dependency), Sherlock/Nexfil/Blackbird/WhatsMyName coverage, and an `account_discovery` module explicitly described as **"Holehe 120+ platforms"** — i.e. it embeds holehe's coverage as an opt-in module.
- Identity graph (cross-platform correlation by usernames/avatars/breach data), Name Consensus Engine with confidence bands, deep breach mode (top-100 severest breached sites), Wayback + GitHub-commit author search, Credential Risk Score 0–100, exports to **JSON/CSV/PDF/Markdown/STIX 2.1/Maltego XML**, REST API + WebSocket + CLI (`mailaccess investigate`, `mailaccess serve`, `mailaccess harvest-emails`), Docker Compose self-hosting, Maltego local transform server.

## Why it matters for ACI
- Our `holehe` registry entry is **broken** (venv crashes with `httpx.InvalidURL`; upstream stagnant since 2024-09). MailAccess is the clearest drop-in path to recover email→account-existence coverage — it embeds the holehe module set, so its probe quality can be compared module-for-module.
- The identity-graph / name-consensus output is the email-identity equivalent of what our graph tier wants for entity resolution — evaluated outputs could seed graph entities instead of raw lists.
- Fast-moving project (0.4.x → 0.18.7 within weeks): eval a pinned version and re-check the platform corpus before trusting hit quality. YAML platform system + platform-health self-demotion are promising anti-noise features worth the eval.

## Sources
- "mailaccess 0.18.7" — https://pypi.org/project/mailaccess/0.18.7/ — 2026-10-15 (crawl)
- "mailaccess 0.10.2" (module/integration docs) — https://pypi.org/project/mailaccess/0.10.2/ — 2026-10-11 (crawl)
- MailAccess integrations doc (GitHub main) — https://github.com/KatrielMoses/MailAccess/blob/main/docs/integrations.md — 2026-10-16 (crawl)
- "Open-Source Intelligence (OSINT) Resources" (Show HN: MailAccess listed 2026-10-07) — https://appsec.fyi/osint.html — 2026-10-17
