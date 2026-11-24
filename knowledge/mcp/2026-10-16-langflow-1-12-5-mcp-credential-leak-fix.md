# Langflow 1.12.5 — MCP management responses no longer expose server credentials

**Date:** 2026-10-16 (release 2026-10-06)
**Source:** https://blog.elest.io/elestio-catalog-updates-125-new-releases-this-week-october-4-10-2026/ (secondary — Elestio catalog roundup; verify against Langflow release notes)

## What changed
Langflow 1.12.5 (6 Oct 2026) includes three security-relevant fixes:
- built-in code execution is now limited to administrators,
- chat attachments stay in authorized storage,
- **MCP management responses no longer show server credentials**.

Same roundup notes sibling fixes: ToolJet 3.20.242 LTS enforces `ENABLE_SIGNUP` on the signup endpoint, Qdrant 1.19.2 accepts only read-write keys on internal gRPC, Mage AI 0.9.80 closes a shell injection when adding Git hosts.

## Why it matters for ACI
Langflow is not in the ACI stack, but the MCP credential-leak bug class is: any MCP management/monitoring surface that echoes server credentials (tokens, keys) into API responses hands them to whoever can call that endpoint — including an agent or a log pipeline. ACI must apply the same rule to its own surfaces: never return credentials, tokens, or keys in any API response, log line, or error payload. The code-execution-to-admins-only fix is also a good default for any flow builder ACI ever embeds.

## Action
**Watch.** No stack change. Add "never echo credentials in API responses/logs" to the ACI security checklist (it is already implied by the MCP threat notes; this is the concrete precedent).
