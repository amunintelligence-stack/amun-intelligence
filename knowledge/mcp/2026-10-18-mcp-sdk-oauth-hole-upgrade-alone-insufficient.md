# MCP SDK OAuth credential leak — upgrading alone does NOT close it

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** ADOPT — add the three-step rule (upgrade + expectedIssuer everywhere + clear-and-rotate pre-patch tokens) to ACI's MCP wiring standards now, before any MCP OAuth client is wired.

## What changed
An independent lab repro (published ~2026-10-17/18) re-tested the October MCP SDK OAuth flaw (TypeScript CVE-2026-104850; Python GHSA-qx49-fqc8-xw99, Cycode advisory 2026-09-28) where a malicious/compromised MCP server names its own authorization server and the client sends it OAuth secrets (refresh token, client secret, signed assertions, PKCE verifier). On Python SDK 1.30.1 all four lab client setups still leaked. On patched versions (1.31.0, 1.32.1) the leak stopped ONLY when the client was built with `expectedIssuer` set; providers created without it still sent secrets to the attacker's issuer — and credentials/tokens stored before the upgrade (which carry no issuer field) still leak until cleared and rotated. The real fix is three steps: (1) upgrade SDK, (2) pass `expectedIssuer` on every provider, (3) wipe pre-patch token caches and rotate anything that may have gone out. Cycode demonstrated taking stolen material to the genuine provider, receiving a valid access token, and inheriting all client permissions (confused-deputy).

## Why it matters for ACI
ACI has "MCP wiring planned" (backend functions in app.py are the first exposure candidates) plus the MCP prompt pack and the n8n-mcp server flagged in the registry. Any OAuth-authenticated MCP client ACI builds or adopts must implement the three-step fix; the documented 10-14-nightly SEP-2352 auth-binding note does not by itself guarantee operators will set expectedIssuer or rotate caches — this is the operational rule to write into ACI's MCP standards. (Secondary sources — lab repro + advisory coverage, not a vendor advisory.)

## Sources
- "Upgrading Your MCP SDK Won't Close the OAuth Hole on Its Own" — https://medium.com/@waseemaofficial/upgrading-your-mcp-sdk-wont-close-the-oauth-hole-on-its-own-df6637b93c38 — 2026-10-17/18
- "Your MCP Server Shouldn't Decide Where Your Credentials Go (CVE-2026-104850 detail)" — https://medium.com/@dvsteja/your-mcp-server-shouldnt-decide-where-your-credentials-go-b6a436e1dbfe — 2026-10-16
- "MCP Python SDK flaw exposes OAuth credentials to servers (GHSA-qx49-fqc8-xw99)" — https://www.techceodaily.com/cybersecurity/mcp-python-sdk-oauth-credential-flaw — 2026-10-02
