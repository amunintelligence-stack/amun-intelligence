# Radware MCP Server Protection — first purpose-built MCP firewall (announced 2026-10-14)

**Date:** 2026-10-14
**Category:** mcp / security

## What changed
Radware announced MCP Server Protection on 2026-10-14 (press release, 06:00 ET):
a purpose-built product to secure MCP servers, joining its Agentic AI
Protection and LLM Firewall. Claimed capabilities:
- MCP attack-surface visibility: deployed MCP servers, exposed tools and
  resources, agent activity, usage patterns, communication flows.
- MCP-aware attack protection: protocol abuse, authentication attacks, tool and
  resource enumeration, unauthorised MCP interactions, AI-driven tool flooding,
  and denial-of-service.
- Governance: evaluate MCP exposure, flag weaknesses, enforce organisational
  policy as deployments scale.
- Agent activity monitoring: agent identities, tool-invocation patterns,
  behavioural anomalies, resource-consumption trends.
- Deployment: cloud service (Radware Cloud Application Protection Service) or
  cloud-augmented on-prem (Alteon / DefensePro); supports public cloud, private
  cloud, Kubernetes, and hardware data centres.

Context cited in the announcement: per Stacklok's State of MCP in Software
2026 survey, nearly half of software companies surveyed run MCP in production
(19% broad production) — i.e. the MCP attack surface is now mainstream, and
traditional web/DDoS controls were not built to parse MCP traffic.

## Why it matters for ACI
ACI's architecture already treats MCP as a bridge channel (the B↔Hermes
MCP prompt pack). Every MCP server ACI consumes or exposes is a new attack
surface: tool enumeration leaks capabilities, a malicious/flooded server can
poison agent context, and unauthenticated stdio/HTTP servers are a recurring
CVE theme this month (see the x64dbg-mcp-server finding tonight). Radware's
launch is a market signal that MCP-specific filtering — not generic WAF rules —
is becoming the expected control plane. For ACI's own deployments, the
relevant ideas are directly reusable even without buying the product:
inventory every MCP server, allow-list tools, rate-limit tool calls, and log
agent→tool invocations.

## Sources
- Radware press release (primary), 2026-10-14:
  https://www.radware.com/newsevents/pressreleases/2026/radware-introduces-mcp-server-protection/

## Action
**Watch** — No purchase, no integration. Adopt the *pattern* in ACI hardening:
maintain an MCP server inventory with exposed tools, put an allow-list +
rate-limit in front of any MCP server ACI exposes, and log tool invocations
per agent. Re-evaluate commercial MCP firewalls when ACI exposes MCP to
external clients.
