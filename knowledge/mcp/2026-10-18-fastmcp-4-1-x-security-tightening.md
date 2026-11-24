# FastMCP v4.1.0 (Oct 8) + v4.1.1 (Oct 17) — security-tightening releases

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** ADOPT — update the tools.yaml FastMCP pin from ≥4.0.11 to ≥4.1.1 for any ACI MCP server work.

## What changed
FastMCP 4.1.0 shipped 2026-10-08 (PrefectHQ/fastmcp): a security-hardening release — OpenAPI path parameters now reject `.`/`..` segments (path-traversal guard), skill files must resolve inside their configured directories (symlink-escape guard), regex tool search is time/length-bounded, HTTP sessions expire on the SDK's 30-min idle default, MultiAuth qualifies client IDs by source, CLI OAuth tokens are encrypted at rest, and gitleaks secret scanning was added to prek. v4.1.1 (2026-10-17) is a pure security patch: regex tool search rejects patterns over 1,000 characters and stops after ~1 second (ReDoS guard), and SkillsDirectoryProvider re-discovers symlinked skill folders. All 4.x users are urged to upgrade.

## Why it matters for ACI
The registry currently pins FastMCP ≥4.0.11 (10-10 nightly). FastMCP is ACI's candidate framework for any MCP server we build (OSINT/intel servers per the registry's "MCP wiring planned" note). The 4.1.x changes are exactly the classes of bugs that matter to an intel stack handling hostile inputs: ReDoS on tool search, traversal on OpenAPI proxies, skill-file escapes. FastMCP 4 targets the stateless 2026-07-28 spec while serving older clients — the right side of the spec line for us.

## Sources
- FastMCP Changelog — v4.1.0 "Fourth and One" / v4.1.1 "Regex Marks the Spot" — https://gofastmcp.com/changelog — 2026-10-08 / 2026-10-17
- FastMCP Updates — v4.1.1 release announcement — https://gofastmcp.com/updates — 2026-10-17
- "FastMCP v4.1.0 | The Deploy Log" — https://deployedbyai.com/log/44c900d01ff3/fastmcp-v4-1-0/ — 2026-10-08
