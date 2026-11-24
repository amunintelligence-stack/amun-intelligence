# Ten MCP SDK OAuth advisories (Sep 28–Oct 5) + official "rug pull" guidance in the docs

**Date found:** 2026-10-22 (advisories published 2026-09-28 → 2026-10-05; docs guide added October 2026)
**Category:** mcp / spec-security posture

## What changed
- The **official MCP SDKs published ten security advisories between Sep 28 and Oct 5, 2026** — six for the Python SDK, four for the TypeScript SDK — most of them OAuth flaws where credentials or tokens were trusted with the wrong party, plus a session-to-principal binding flaw on SSE and Streamable HTTP transports.
- Headline flaw (Cycode finding): a malicious MCP server answers the client's discovery request with **404**, which pushed the **MCP Python SDK's OAuth client into a legacy fallback that skipped issuer validation** — the client then sent client secrets, authorization codes and PKCE verifiers to attacker endpoints. **Fixed in Python SDK 1.30.0 / 2.2.0** (releases were already on PyPI Sep 7 — a silent patch window where non-upgraders ran known-vulnerable code).
- TypeScript safe line per advisory: **1.31.0** (one widely-shared roundup says 1.32.0 — go at least 1.31.0, preferably higher). Python needs **1.30.0 / 2.2.0+**, and for session-to-principal binding on SSE/Streamable HTTP the write-up says go to **1.27.2+** on the relevant branch.
- **Important caveat:** the most important fixes are **opt-in** — e.g. Python audience validation requires setting `validate_token_resource=True` plus `resource_server_url`; upgrading without the setting leaves the gap open.
- Separately, MCP's **local server security guide (added October 2026)** now documents the **rug-pull** pattern explicitly: "Definitions are not fixed at install time either: a server can quietly change them after you approved it (a rug pull), so a one-time consent dialog and package pinning do not cover this surface." The official advice: prefer clients that **pin tool definitions**.

## Why it matters for ACI
Two direct touchpoints: (1) **n8n 2.45 upgraded its MCP TypeScript SDK to v2** (see soar/2026-10-22-n8n-2.45-mcp-upgrade.md) — on our current 2.43.7 the bundled TS SDK is older; (2) any ACI MCP servers built on FastMCP/Python SDK pre-1.30.0 carry the OAuth-fallback credential-leak. The rug-pull guidance is operational policy for ACI missions: pin and review MCP server versions, re-approve on upgrades, never treat a clean scanner result as approval (two malicious MCP servers passed five scanners clean this month, per adversa.ai).

## Sources (with dates)
- autocoder.dev, "MCP Security: 10 SDK Advisories in 8 Days" (2026-10-12): https://autocoder.dev/blog/mcp-sdk-security-advisories-2026
- dev.to/fabwaseem, "MCP Security in 2026: The OAuth SDK CVEs, Tested" (Oct 2026): http://dev.to/fabwaseem/mcp-security-in-2026-the-oauth-sdk-cves-tested-and-how-to-lock-down-your-server-3lln
- Adversa AI October 2026 digest (2026-10-08): https://adversa.ai/blog/top-mcp-security-resources-october-2026/
- Glasp, "MCP Tool Poisoning & Rug Pulls: 2026 Security Guide" (Oct 2026): https://glasp.co/articles/mcp-security-tool-poisoning-supply-chain

## Action: ADOPT (as policy + backlog)
1. Inventory: record the MCP SDK versions of every ACI MCP server (Python SDK ≥ 1.30.0 / 2.2.0; TS ≥ 1.31.0) and upgrade anything below.
2. Enable the opt-in protections the advisories require (`validate_token_resource=True` + `resource_server_url` on FastMCP Python servers).
3. Add to the ACI runbook: pin MCP server versions, re-approve tool lists on upgrade (anti-rug-pull), move secrets out of MCP config files, re-authorize inside each tool.
