# MCP TypeScript SDK 2.3.0 — auth binding (SEP-2352), same-origin redirects, pagination

**Date:** 2026-10-14 (SDK packages published 2026-10-02; downstream upgrade merged 2026-10-04)
**Category:** mcp / spec & SDKs

## What changed
The MCP TypeScript SDK v2 line advanced to 2.3.0 (split packages
`@modelcontextprotocol/client` / `core` / `server` 2.0.0 → 2.3.0; `node`
2.0.0 → 2.1.1; the v1 `sdk` proxy/legacy line 1.30.0 → 1.32.0), per the
Apify `mcpc` upgrade record (2026-10-04). Notable behaviours from the
changelogs reviewed in that upgrade:
- **Auth binding (SEP-2352):** client-credentials and id-jag logins now record
  the authorisation server they were validated against and bind the SDK
  provider to it. SDK 2.2.0 printed a deprecation notice without that binding,
  which broke `--json` stderr output for `login --grant client-credentials`.
  Older unbound profiles keep working.
- **Same-origin redirect policy:** redirect errors now explain the SDK's new
  same-origin policy and keep the target URL the SDK names.
- **Pagination:** the SDK now walks every page of a list call itself; the cap
  rises from 64 to the caller's own 1000 pages (in mcpc's case).
- Migration risks flagged in the same review: a 4 MiB request-body limit now
  enforced by the v1 proxy server, and `saveTokens()` failures after refresh
  now surfacing instead of being swallowed.

This is distinct from the v1-line SDK 1.31.0 covered in a previous night's
finding (2026-10-11): the v2 line implements the stateless 2026-07-28 spec,
while the 1.x line receives only critical/security fixes.

## Why it matters for ACI
ACI consumes MCP servers and may expose its own. The SEP-2352 binding closes a
real confused-authorisation-server hole (a token validated against one IdP
being replayed against another), and the same-origin redirect rule blocks a
classic OAuth redirect leak. Any ACI code still on the v1 SDK should plan the
v2 migration: the stateless spec removes the `initialize` handshake and
`Mcp-Session-Id`, which changes session handling, and the 4 MiB body limit
matters for large evidence payloads returned through MCP.

## Sources
- Apify mcpc upgrade to MCP TypeScript SDK 2.3.0, PR #438, 2026-10-04
  (changelog review + migration risks):
  https://github.com/apify/mcpc/commit/7ac28052acb673bda5d07ba04affa6ac9802d141
- MCP spec 2026-07-28 migration notes (background):
  https://github.com/fblissjr/fb-claude-skills/blob/HEAD/docs/internals/mcp_spec_2026_07_28.md

## Action
**Watch / plan** — Do not bump production MCP clients to SDK v2 mid-mission.
In a dev branch, trial the v2 SDK against ACI's MCP servers, verify the
auth-binding behaviour, the same-origin redirect handling, and the 4 MiB body
limit against real evidence payloads. Schedule the v1→v2 migration before the
1.x line stops receiving fixes.
