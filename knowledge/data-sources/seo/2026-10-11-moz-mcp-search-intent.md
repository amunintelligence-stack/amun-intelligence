# Moz: Data MCP server (beta, ~Sept 2026) + search intent becomes default billed keyword-metric (2026-10-01)
- Date: 2026-10-11 | Category: data-sources/seo | Action: **WATCH**

## What changed
- **Moz Data MCP server in beta (~Sept 2026):** Moz now exposes Domain Authority, keyword metrics, and ranking data through an MCP server connectable from Claude, ChatGPT, Claude Code via OAuth. Beta caveats reported by a third-party reviewer: no published tool reference, only the account owner can connect (seated users excluded), usage rows burn through quotas quickly, and Moz Data / Moz Local are separate connections/subscriptions.
- **Search intent billing change (2026-10-01):** search intent became a default — and billed — part of Moz keyword metrics instead of opt-in. Any per-row cost estimates for Moz keyword data must now account for intent being included.

## Why it matters for ACI
- Moz is already a stubbed ACI seo connector. An MCP endpoint is a secondary integration path (agent-native access to DA/keyword data without REST plumbing), but the beta's missing tool reference and owner-only connection limit its production value.
- The search-intent billing change affects cost modeling for any future Moz API usage: keyword-metric calls got effectively more expensive as of 2026-10-01.

## Sources (links with dates)
- https://growthmethod.com/moz-data-mcp-server/ — ~2026-09-16 (third-party review; no official Moz announcement found — treat as reported, not confirmed by Moz)
- No primary Moz source found for the MCP server or the intent-billing change at research time (2026-10-11).

## Action (adopt / watch / ignore — one concrete recommendation)
**Watch** — Do not integrate the beta MCP server; when Moz publishes an official tool reference, re-evaluate it as the agent-native path for DA/keyword data in the ACI seo connector.
