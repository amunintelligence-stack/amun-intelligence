# MCP reference servers v1.0.0 — fetch server blocks private/loopback/metadata addresses by default

**Date of finding:** 2026-10-17
**Window covered:** last ~30 days

## What changed

- **The Model Context Protocol project published its reference servers at v1.0.0 on 11 Oct 2026** — four TypeScript reference servers at 1.0.0 and three Python servers at 2026.10.10.
- **Fetch server (breaking behavior change):** it now **refuses private, loopback, and metadata addresses by default**. A previously reachable localhost/internal service (e.g. `http://127.0.0.1:8000`, cloud metadata `169.254.169.254`) is now blocked unless explicitly allowed. This is an SSRF guardrail: a prompt-injected agent can no longer trivially pivot the fetch tool at internal services or cloud metadata endpoints.
- **Filesystem server:** it now **waits for initial client directory roots before accepting tool calls**, plus fixes for root revocation and refresh ordering. Tools called before roots are established are rejected rather than silently operating on a default.
- **Scope warning from the project itself:** these are explicitly described as **educational reference implementations** — the 1.0.0 label does not establish production readiness. Do not treat them as hardened production servers.
- **Related hardening signal (same week):** Radware's MCP Server Protection (announced 14 Oct, already in registry) and the NVIDIA App default-on MCP case (16 Oct) confirm the ecosystem is moving from "connect everything" to "default-deny + allow-list".

## Why it matters for ACI

- **Direct collision with ACI's architecture:** ACI's backend lives at `http://127.0.0.1:8000` and n8n at `http://localhost:5678`. Any ACI flow that routes an MCP fetch tool at those loopback endpoints will now hit the default block after upgrading to reference-server v1.0.0. If ACI ever adopts the reference fetch server (e.g. for web evidence fetching), internal-URL workflows must be allow-listed explicitly — and that allow-list is itself a security decision (allow-list only the exact ACI endpoints, never `*` / `127.0.0.1` broadly).
- **Adopt the pattern, not just the server:** the default-deny posture (block private/loopback/metadata unless explicitly allowed) is exactly the SSRF rule ACI's own tool executor should enforce for any agent-invoked HTTP fetch — agents must never be able to fetch `169.254.169.254`, localhost admin endpoints, or RFC-1918 targets unless the mission explicitly requires a named internal endpoint.
- **Filesystem-server lesson:** "wait for roots before accepting calls" maps to ACI's evidence handling — no file tool should operate before its allowed directory set is fixed and canonicalized (already a registry design rule; this release validates it).
- **No ACI stack breakage today:** ACI does not run the MCP reference servers in production (MCP wiring is still planned), so this is a design input, not an incident.

## Sources

- Medium / The Provenance AI Report, "AI Daily Digest: MCP Servers Tighten Access as Voice Tools Expand — October 12, 2026" (12 Oct 2026) — https://medium.com/@provenance_report/ai-daily-digest-mcp-servers-tighten-access-as-voice-tools-expand-october-12-2026-b455a6e58eac (citing MCP servers v1.0.0 release, 11 Oct 2026, and reference-server README)

## Action

**Adopt (pattern) / Watch (servers):** bake default-deny SSRF rules (block private/loopback/link-local/metadata) into ACI's agent HTTP-fetch path and any future MCP fetch server, with a narrow explicit allow-list for named ACI endpoints. Do not deploy the reference servers as production components — they are educational implementations. Before any upgrade of an MCP fetch server in ACI, regression-test all internal-URL workflows.
