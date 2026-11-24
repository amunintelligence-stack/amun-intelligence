# Microsoft Agent Framework MCP: C# SDK 2.2.0, stateless HTTP by default

**Date noted:** 2026-11-02
**Category:** mcp — protocol/SDK state (pattern reference, not ACI stack)

## What changed
- Independent guide checked **2 Nov 2026**: Microsoft Agent Framework (.NET) uses the official C# SDK (`ModelContextProtocol` **2.2.0**, with `ModelContextProtocol.AspNetCore` for HTTP servers). Key facts:
  - Since the **2026-07-28 protocol revision**, the HTTP transport is **stateless by default** (`HttpServerTransportOptions.SessionMode = Stateless`) — servers scale behind a load balancer with no sticky sessions.
  - Framework add-on `Microsoft.Agents.AI.Mcp` (alpha, shipped with `Microsoft.Agents.AI` 1.26.0) adds **long-running MCP tasks** and **MCP-delivered skills**.
  - Provider packages add hosted MCP (the model provider calls the MCP server for you).
  - Clients on protocol `2026-07-28` must send `Mcp-Method` and `Mcp-Name` headers on every POST; clients on `2025-11-25` negotiate down automatically (per the Azure MCP 3.0 guide, same week).
- This is the .NET-side confirmation of the stateless-era rules ACI already tracks from the reference-servers notes (ping removed in 2026-07-28, log negotiated protocolVersion per server).

## Why it matters for ACI
- ACI has no .NET, but the stateless-default is a design rule for any future ACI MCP server: **design for stateless from day one** (no server-side session affinity), and treat long-running tasks + skills-over-MCP as the two extensions to watch, not to implement early. The `Mcp-Method`/`Mcp-Name` header requirement is a concrete interop check for any client ACI builds against a 2026-07-28 server.

## Action: WATCH
- No change. Add the stateless-default + header requirement to the ACI MCP design checklist at the next MCP-doc touch.

## Sources (checked 2026-11-02)
- Microsoft Agent Framework (.NET) MCP guide (checked 2 Nov 2026): https://codehalwell.github.io/AgentGuides/microsoft-agent-framework-guide/dotnet/microsoft_agent_framework_dotnet_mcp/
- Azure MCP Server 3.0 guide (protocol negotiation detail): https://ashishkasaudhan.medium.com/azure-mcp-server-3-0-goes-stable-a-practical-guide-for-devops-platform-engineers-0b83bd64ef0c
- Prior ACI notes: 2026-10-24-reference-servers-2-0-2026-07-28.md, 2026-10-26-mcp-version-negotiation.md
