# Tinuiti Bliss Point MCP Server — governed media-measurement data for AI agents

**Date:** 2026-10-16 (announced 2026-10-06)
**Source:** https://www.globenewswire.com/news-release/2026/10/06/3375727/0/en/tinuiti-unveils-bliss-point-mcp-server-pioneering-open-measurement-access-for-ai-agents.html (primary — press release)

## What changed
Tinuiti launched the **Bliss Point MCP Server** (6 Oct 2026), opening its proprietary measurement layer to AI agents. Powered by the Bliss Point Marketing Operating System (unifies audience, creative, media, measurement), it exposes clean, normalized cross-channel media performance and measurement intelligence through MCP-compatible agents (ChatGPT, Claude, Copilot, clients' own agents/BI), subject to client permissions and configuration. Positioning: an alternative to walled-garden platforms — one already-taxonomized view of performance for an agent to reason over, instead of reconciling fragmented platform reports.

## Why it matters for ACI
This is the template for how ACI's data-source connectors should evolve: a governed, normalized measurement layer exposed to agents, rather than raw per-platform API scraping. For ACI's ads-intel work, Bliss Point is a **paid/agency-gated** source (client permissions required) — not a keyless source — but it establishes the pattern: normalized cross-channel media data + governed access + MCP as the delivery mechanism. If a client ever grants ACI access to their Bliss Point data, the MCP interface means near-zero integration work.

## Action
**Watch.** Add to the ads-intel connector list as a gated/enterprise source (client permission required). Borrow the pattern: normalized + governed + MCP for ACI's own data-source layer.
