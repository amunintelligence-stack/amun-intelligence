# SEP-2640 "Skills over MCP" reaches Final — canonical skill-serving convention

## What changed
The MCP **SEP-2640: Skills Extension** (Skills over MCP Working Group, created 2026-04-23) now carries **Final** status; the spec page was last updated ~2026-10-18. It standardizes serving Agent Skills over MCP using the existing Resources primitive: skills live under `skill://` URIs, servers implement `skills/list` and `skills/get` (with SHA-256 content digests), and optional `resources/directory/read` gives scoped file navigation. Notably: **approval is per skill** (activating a nested skill needs fresh consent), names are not unique (disambiguate by path), and a skill never shadows same-named skills from other origins — anti-shadow-server rules baked into the spec. FastMCP 4.1.2 (2026-10-20) ships the extension foundation plus experimental discovery, so this is now implementable, not a draft.

## Why it matters for ACI
ACI's analyst personas, pivot playbooks and investigation procedures are currently design docs and prompts; SEP-2640 gives a standard, verifiable way to package and serve them to any MCP-compatible agent — with integrity digests that fit ACI's confidence/evidence discipline. It also provides the shape for evaluating third-party skills safely (per-skill consent gates).

## Sources (with dates)
- modelcontextprotocol.io SEP-2640 spec page, status Final, page updated ~2026-10-18 — https://modelcontextprotocol.io/seps/2640-skills-extension
- FastMCP changelog v4.1.2, 2026-10-20 — https://gofastmcp.com/changelog

## Action
watch
