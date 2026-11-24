# mcp-audit-tap: 100-line MCP traffic logger (Oct 20, 2026)

## What changed
- Developer Mike Webber released mcp-audit-tap on Oct 20, 2026 (ClawdBytes, Oct 20,
  2026): a ~100-line Python utility that sits as a man-in-the-middle between an MCP
  client and a stdio MCP server and logs every JSON-RPC `tools/call` request and
  result, so operators can see what data actually leaves the machine.
- Motivation: a Hacker News thread about a free WhatsApp MCP server debated privacy
  and account bans without evidence; READMEs claim minimal access while code may
  allow more. Audit-tap replaces trust with a traffic record — especially valuable
  for stdio servers, whose traffic is otherwise opaque.
- Fits the month's pattern: MCP tool-surface drift (silent contract changes counted
  Oct 3–7), the "pin tool definitions" guidance, and the CrowdStrike read-only audit
  pattern recorded Oct 22–23.

## Why it matters for ACI
- ACI's standing MCP rule is "eval servers isolated first" (Consensus-OSINT, GraphIQ,
  Memgraph read-only patterns). mcp-audit-tap is the cheap enforcement tool for that
  rule: run any candidate MCP server behind the tap during eval and keep the
  request/result log as the eval evidence. No key, no install into ACI itself — it
  is an eval harness, not a dependency.
- Also applicable later to ACI's own MCP servers: tap ACI's server during testing to
  prove it sends only what its tool contracts claim.

## Sources
- ClawdBytes, "MCP Audit Tap Reveals What Third-Party Servers Actually Send",
  Oct 20, 2026:
  https://www.clawdbytes.com/article/2026-10-20-mcp-audit-tap-see-what-a-third-party-server-actually-sends

## Action
- ADOPT as eval practice (not as a dependency): any future MCP server eval for ACI
  runs behind mcp-audit-tap (or an equivalent tap) with the traffic log filed with
  the eval. No code change to ACI today.
