# Langflow MCP stdio RCE (CVE-2026-105740) + OS command injection — 1,400+ exploit attempts; first fix was incomplete

**Date found:** 2026-10-22 (THN coverage 2026-10-15; honeypot telemetry Sep 19 → Oct 11)
**Category:** soar / agent-builder supply chain

## What changed
- **GHSA-w794-rj3p-xv45** — OS command injection via **MCP stdio configuration** in Langflow. **Fixed in 1.10.3**; the earlier fix in **1.9.0 was incomplete**. On a default pip install with auto-login, the instance is effectively unauthenticated.
- **CVE-2026-105740** — **authenticated RCE via the MCP stdio transport** (GHSA-7w94-79vh-5mr2).
- Previdian sensor telemetry: **1,512 exploit attempts from 27 IPs in 15 countries** (first seen Sep 19, peaking ~Oct 11); The Hacker News reported 1,423 in its Oct 15 article. Single-sensor data — scans, not confirmed victim counts. Not in CISA KEV as of the write-up.
- Pattern context: the same October digest notes the **rug-pull** mechanics — MCP clients cache tool definitions at connect and reload them on reconnect/update **without re-approval**; the `postmark-mcp` 1.0.16 incident added one line that **BCC'd every email** after thirteen clean versions.

## Why it matters for ACI
ACI does not run Langflow, but the lesson is architectural, not product-specific: **any setting that names a command, module path, or URL to load is code execution** — and the MCP stdio transport is exactly that. ACI's tool registry and any future "add an integration" UI must treat MCP server configs as privileged input: gated, reviewed, pinned, version-checked. The incomplete-1.9.0-fix detail is a process lesson: track the *actual fixed version* (1.10.3), not the first patch announcement. Low-code AI builders (Langflow, and in our case n8n's MCP nodes) are prime targets because they hold many credentials and are stood up fast outside change control — n8n's Oct 14 advisory batch already showed the same credential-exfiltration-via-agent-tools class on our own stack.

## Sources (with dates)
- aicyberbrief.com, "Langflow MCP flaw draws 1,400+ exploit attempts — and the first fix, 1.9.0, was incomplete" (Oct 2026): https://aicyberbrief.com/article/langflow-mcp-flaw-draws-1-400-exploit-attempts-and-the-first-fix-1-9-0-was-incomplete
- THN coverage referenced within (2026-10-15)
- Glasp, "MCP Tool Poisoning & Rug Pulls: 2026 Security Guide" (Oct 2026): https://glasp.co/articles/mcp-security-tool-poisoning-supply-chain

## Action: WATCH
No Langflow in ACI — no install/patch needed. Adopt the process lessons into the ACI registry runbook: (1) record fixed versions, not announcement dates; (2) treat MCP server config fields as code-exec surfaces in review; (3) keep n8n patched per the soar/2026-10-22-n8n-2.45-mcp-stack.md calculus.
