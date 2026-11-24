# MCP reference servers 2.0.0 — modern (2026-07-28) era, Node 24 floor

## What changed
- **MCP reference servers v2.0.0** (19 Oct 2026, eight days after 1.0): every reference server now speaks the **modern-era spec (2026-07-28)** — stateless, no `initialize` handshake, no session state — while still answering legacy-era (2025-11-25 and earlier) clients from the same process. Era is chosen from the client's first message (`server/discover` or 2026-07-28 per-request metadata = modern; `initialize` = legacy).
- **Breaking client-visible changes**: TypeScript servers move to `@modelcontextprotocol/server` v2 packages and **require Node 24+** (declared 20, docs/CI disagreed — audit raised the floor just before publish). Python servers (fetch, git, time — 2026.10.19 on PyPI) require `mcp` >=2.3 <3 and advertise prompts/resources capabilities. The `everything` test server drops experimental task tools for 2025-era clients (they return for 2026-07-28 clients via the tasks extension); a 2026-07-28 client sending `ping` gets method-not-found (removed in that revision).
- **Tool-surface drift audit** (3–7 Oct 2026): 140 unannounced changes across 66 consecutive official-server release pairs; 218 silent contract changes across most-installed npm servers. Defense practice: pin version **and** SHA-256-hash tool descriptions + input schemas against a committed lockfile (mcp-lock / rugsnare pattern); exit non-zero on drift.
- **Ecosystem note**: Red Hat MCP Gateway GA 16 Oct (negotiates 2025-03-26 / 2025-06-18 / 2025-11-25 / 2026-07-28 per client on one endpoint); Azure MCP Server 3.0 (12 Oct, clearer tool contracts). Three protocol versions live at once — the useful question for any server is which revision it actually negotiates, not which it claims.

## Why it matters for ACI
- Directly relevant to the n8n 2.45.x MCP stack (TS SDK v2, 2026-07-28 discovery handshake) and to any future ACI MCP exposure: negotiated-version logging (adopted 26 Oct) is now confirmed as the operational rule — log the `protocolVersion` the server returns, not the one requested.
- Node 24 floor matters for any Node-based MCP tooling in the pipeline; Python `mcp` >=2.3 floor matters for Python servers. Neither changes tonight's stack (no MCP servers deployed in ACI), but both set version floors for the next eval.
- The silent-drift audit strengthens the standing rule: MCP servers are mutable dependencies — pin + hash before any agent with permissions touches one.

## Sources
- https://agentriot.com/news/ai-infrastructure/mcp-reference-servers-2-0-2026-07-28-spec-node-24 (Oct 2026, 2.0.0 detail)
- https://agentry.news/tools/mcp-servers-hit-20-legacy-clients-still-work (29 Oct 2026)
- https://vibecoding.app/blog/mcp-servers-change-under-you (Oct 2026, drift audit + pin/hash practice)
- https://telegra.ph/Three-MCP-protocol-versions-are-live-at-once-Here-is-how-to-see-which-one-a-server-really-speaks-10-22 (22 Oct 2026, negotiated-version rule)

## Action
- **Adopt (practice)**: pin + hash tool surface for any MCP server before agent use; log negotiated protocol version per server (already adopted — now with a second source confirming it).
- **Watch**: Node 24 / `mcp` 2.3 floors for future MCP evals; Red Hat gateway negotiation pattern if ACI ever fronts multiple servers.
