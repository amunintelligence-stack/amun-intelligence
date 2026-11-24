# WordPress MCP Adapter 0.7.0 — canonical plugin lands on WordPress.org

**Date:** 2026-10-14 (release: 2026-10-02; announcement: 2026-10-07)
**Category:** mcp / data-sources (CMS as an MCP source)

## What changed
WordPress published version 0.7.0 of its official MCP Adapter plugin to the
WordPress.org plugin directory — the first version distributed there. It was
previously available only via GitHub/Composer, yet already had 40,000+
active installs. The adapter turns abilities registered through the WordPress
Abilities API (WordPress 6.9+) into MCP tools, resources, and prompts, so AI
clients (Claude, Cursor, VS Code, etc.) can discover and call them.

Key 0.7.0 details:
- Supports the new stateless `2026-07-28` MCP spec; older clients requesting
  `2025-06-18` / `2024-11-05` are still served through the `2025-11-25` schema.
- Direct callable tools can request elicitation input under `2026-07-28`
  (`McpInputRequired`).
- The default server exposes three meta-tools
  (`discover-abilities`, `get-ability-info`, `execute-ability`) instead of one
  tool per ability, keeping the `tools/list` response small no matter how many
  abilities are registered.
- Plugins should now declare `Requires Plugins: mcp-adapter` instead of
  bundling their own copy (bundled copies still work but log a deprecation).
- Security default to note: the transport permission callback defaults to
  "any logged-in user" (`read` capability), and each ability still runs its own
  `permission_callback`. One independent review flagged that a Subscriber-level
  account can reach the server by default unless the site raises the callback.

## Why it matters for ACI
AMUN missions routinely need to assess a target organisation's public web
footprint — and a huge share of corporate sites run WordPress. A canonical,
dependency-declarable MCP adapter means: (a) WordPress sites become
machine-readable MCP sources with a stable contract instead of ad-hoc scraping;
(b) an ACI recon agent could, with proper authorisation, enumerate a target's
exposed abilities (content, products, forms) through the discovery meta-tools
rather than crawling blindly; (c) the same adapter is a template for how ACI
itself could expose its own findings/tools over MCP (meta-tools + discovery
pattern keeps tool catalogues small).

## Sources
- WordPress Core AI team announcement, 2026-10-07:
  https://make.wordpress.org/ai/2026/10/07/the-mcp-adapter-plugin-is-now-available-on-wordpress-org/
- InstaWP review of v0.7.0 (security default, install notes), Oct 2026:
  https://instawp.com/wordpress-mcp-adapter-review/
- Elementor overview of MCP options for WordPress, Oct 2026:
  https://elementor.com/blog/mcp-for-wordpress-what-each-option-is-and-what-to-install/

## Action
**Watch** — Do not add WordPress MCP Adapter as an ACI data source yet
(pre-1.0, experimental, and the default permission callback is permissive).
Track it toward v1.0; when a client engagement involves a WordPress target
with authorisation, pilot a read-only discovery pass against a staging copy
with the permission callback raised and abilities allow-listed. Revisit the
meta-tools/discovery pattern when designing ACI's own MCP exposure.
