# n8n 2.44.4 (2026-10-19) — beta line now above the Oct-14 bulletin patch floor

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — no change to our instance; stay on the 2.43.x stable line. Revisit only if the 2.44 line is promoted to stable.

## What changed
- **n8n 2.44.4** shipped **2026-10-19** as a pre-release (beta line). Fixes: connection reuse in the log-streaming webhook destination (#41281), expression spans turned off by default (#41309). Prior betas this week: 2.44.3 (2026-10-16, Observer detail lines), 2.44.2 (2026-10-15, per-webhook-request XML parser).
- Key point: the Oct-14 security bulletin set the 2.x **beta** patched floor at **2.44.1+**. 2.44.4 is the first beta clearly above that floor — the earlier 2.44.0 finding (below-floor, 2026-10-18 nightly) no longer describes the beta line's head.
- Stable line unchanged: **2.43.7 (2026-10-16)** remains the latest stable — exactly what we run.

## Why it matters for ACI
- Our instance was upgraded to **2.43.7** on 2026-10-18, which is ≥ the 2.43.5 stable bulletin floor — no new advisory this cycle affects us, no action needed.
- The 2.44 line keeps accumulating execution/access-policy fixes (osrepos Oct 9–15 roundup flags 2.44's agent-tool access policies and workflow reliability as the most interesting new bits), but it is still pre-release. Per the standing rule, the beta line is not tracked until promotion.

## Sources
- n8n releases (2.44.4, 2.44.3, 2.44.2, 2.43.7, 2.43.6, 2.43.5) — https://github.com/n8n-io/n8n/releases — 2026-10-19
- "Open Source AI Weekly: Five Developments to Watch, October 9–15" (n8n 2.44 caveat: 2.43.6 stable vs 2.44.2 pre-release) — https://osrepos.com/blog/open-source-ai-weekly-five-developments-to-watch-october-9-15 — 2026-10-17
