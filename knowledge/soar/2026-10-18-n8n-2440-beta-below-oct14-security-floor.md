# n8n 2.44.0 (13 Oct 2026) — beta line, BELOW the Oct-14 security bulletin patch floor

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — stay on 2.43.x stable line; do not track 2.44 beta until it is promoted to stable and its post-bulletin patch status is confirmed.

## What changed
n8n shipped 2.44.0 on 13 Oct 2026 (one day before the Oct-14 security bulletin), with workflow reliability, access-policy enforcement, and queue-handling improvements plus Assistant/editor polish. The Oct-14 bulletin patch floors are: 1.x → 1.123.85+, 2.x stable → 2.43.5+, 2.x beta → 2.44.1+. This confirms 2.44.x is the **beta** line (stable remains 2.43.x; 2.43.7 released 16 Oct is current stable) — and 2.44.0 itself predates the bulletin fix, so it is below the patched floor for its own line. Censys data cited in coverage notes ~114k exposed n8n instances, ~77k on versions tied to recent critical disclosures.

## Why it matters for ACI
Our instance was upgraded to 2.43.7 today (18 Oct), which is ≥ the 2.43.5 bulletin floor and the latest stable — exactly where it should be. 2.44.0 must not be read as "newer = safer": it is unpatched for the Oct-14 batch and beta-only, so tracking the beta line is rejected on security grounds. Continue monitoring the stable line only.

## Sources
- "n8n Release Notes - October 2026 Latest Updates (2.44.0, Oct 13)" — https://releasebot.io/updates/n8n — 2026-10-13
- "n8n self-hosted: 5 high-severity flaws patched, update now" — https://medium.com/cagris-biz-stack/n8n-self-hosted-5-high-severity-flaws-patched-update-now-982502f5ee21 — 2026-10-15
- "Censys Counted 114,000 Exposed n8n Instances: Your Self-Hosted Hardening Checklist" — https://dev.to/cortexflow_tech/censys-counted-114000-exposed-n8n-instances-your-self-hosted-hardening-checklist-ck5 — 2026-10-18
