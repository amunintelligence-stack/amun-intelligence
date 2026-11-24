# MCP reference servers 1.0.0 — fetch server now blocks private/loopback/metadata IPs by default

**Date found:** 2026-10-22 (released 2026-10-11)
**Category:** mcp / behavior change in reference implementations

## What changed
The Model Context Protocol project published its reference implementations at **1.0.0**: four TypeScript servers and three Python servers (2026.10.10). Two behavior changes matter:
- The **fetch server now refuses private, loopback, and metadata (cloud IMDS) addresses by default** — a previously reachable `localhost` service or internal API is now blocked unless explicitly allowed.
- The **filesystem server waits for initial client directory roots** before accepting tool calls, with fixes for root revocation and refresh ordering.
- The project stresses these are **educational reference implementations** — 1.0.0 does not mean production-ready.

## Why it matters for ACI
ACI agents routinely fetch internal endpoints (the FastAPI backend at 127.0.0.1:8000, n8n at 127.0.0.1:5678, local tooling). If any ACI workflow or third-party MCP server we adopt is built on (or mirrors) these reference servers, the new default blocks loopback/internal fetch and will break workflows that worked before. More importantly, the pattern is the **right default to copy**: our own FastMCP servers that do outbound fetching should adopt a private-IP deny-by-default policy, and SSRF against cloud metadata endpoints should be on our deny list (cf. the Grafana MCP CVE-2026-19516 SSRF via `X-Grafana-URL` found the same month).

## Sources (with dates)
- "AI Daily Digest: MCP Servers Tighten Access as Voice Tools Expand — October 12, 2026" (2026-10-12): https://medium.com/@provenance_report/ai-daily-digest-mcp-servers-tighten-access-as-voice-tools-expand-october-12-2026-b455a6e58eac — cites "MCP servers v1.0.0 release, October 11, 2026 (UTC)"

## Action: ADOPT (as config practice)
1. Do not build ACI servers on the reference fetch/filesystem implementations, or pin + review their new defaults first.
2. Copy the practice into ACI FastMCP servers: deny private/loopback/metadata IPs by default on any outbound-fetch tool; allowlist what missions need.
