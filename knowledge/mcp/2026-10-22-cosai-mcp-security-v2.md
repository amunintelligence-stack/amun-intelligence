# CoSAI MCP Security v2.0 — auditable assurance levels for MCP deployments

**Date found:** 2026-10-22 (released October 2026)
**Category:** mcp / defense framework

## What changed
The Coalition for Secure AI (**CoSAI**) released **MCP Security v2.0** (Adversa AI was among the workstream leads). It turns the 12 MCP threat categories from v1 into an **auditable model with four security assurance levels and eight security dimensions**, spanning from a local sandbox up to regulated multi-tenant platforms. New in v2.0: guidance for the protocol's move **away from stateful sessions** (the sessionless direction FastMCP 4 targets), the **Tasks framework**, a **post-quantum migration path**, and **centralized gateway enforcement**.

## Why it matters for ACI
ACI's architecture is MCP-centric: FastMCP servers expose recon/OSINT tools, n8n speaks MCP, missions chain agent→tool calls. Up to now our MCP posture was implicit. v2.0 gives us a ready-made, audit-friendly framework to (a) classify each ACI MCP server by assurance level, (b) justify controls to anyone we on-board, and (c) track the sessionless-protocol migration that is already happening under us (FastMCP 4 sessionless + n8n 2.45's MCP 2026-07-28 discovery handshake). This is a reference document, not a dependency.

## Sources (with dates)
- CoSAI MCP Security v2.0 announcement context, via Adversa AI October 2026 digest (2026-10-08): https://adversa.ai/blog/top-mcp-security-resources-october-2026/ — https://www.coalitionforsecureai.org (v2.0 release page)

## Action: WATCH
Download the v2.0 model and map ACI's current MCP surface (FastMCP servers, n8n instance server, any third-party MCP servers) onto the four assurance levels; pick a target level per server and record it in the registry. Revisit after the next nightly flags sessionless-protocol migration requirements.
