# Hashnode launches remote MCP server with tokenless delegated-identity + DCR

## What changed
On 2026-10-20, **Hashnode** launched an official remote MCP server: a login-and-approve remote server that requires **no token or secret** from the user. The record (apis.io) notes delegated identity, protected resource metadata, and dynamic client registration (DCR) are the moving parts — a user signs in, approves, and the server works without any credential ever entering an agent transcript ("a way in that never puts a secret in a transcript"). It ships a draft-first workflow (dry run expressed in the product) and built-in reviewer roles as human-in-the-loop, rather than bolted-on approvals.

## Why it matters for ACI
Not an intel tool itself (publishing), but it is a concrete reference implementation of the post-September-28 spec auth model: delegated identity + DCR + dynamic auth, zero stored secrets on the client side. If ACI ever exposes its tools as a remote MCP service (missions from Mohamed's phone or Hermes desktop), this is the trust model to copy. The draft-first + human-in-the-loop-by-design pattern also maps directly to ACI's approval-gated write actions.

## Sources (with dates)
- apis.io record, published 2026-10-20 — https://apis.io/2026/10/20/hashnode-ships-an-mcp-server-with-no-token-to-handle/

## Action
watch
