# Multi-agent framework check — Nov 1 refresh confirms the Oct 31 landscape, adds cost/install data

**Date noted:** 2026-11-01
**Category:** multi-agent — reference only: ACI's pipeline is deterministic Python; LLM only where interpretation is needed

## What changed
- Geekflare's open-source agent-framework comparison was **refreshed 1 Nov 2026** (same 7-framework build test as before: LangGraph, CrewAI, Pydantic AI, OpenAI Agents SDK, Mastra, Microsoft Agent Framework, Google ADK). Headline deltas vs the 31 Oct ACI landscape note:
  - **Install weight:** Microsoft Agent Framework (~78s, ~400 MB) and CrewAI (~57s, ~400 MB) were the heaviest installs in the test.
  - **Cost per answer:** CrewAI cost roughly **2x Mastra** per answer in the same research-agent build.
  - Rankings unchanged: LangGraph for resilient stateful agents, CrewAI for role-based teams — consistent with ACI's 31 Oct note.
- Independent confirmation of the AutoGen end-state: AutoGen is in **maintenance mode (no new features, community-managed)** and Microsoft's recommended successor for new projects is **Microsoft Agent Framework** (1.0 GA April 2026). Two separate Oct sources agree; ACI's own 31 Oct landscape note already recorded this, so tonight is confirmation, not news.
- No new LangGraph / CrewAI / ADK version release was found in tonight's sweep beyond the versions recorded 2026-10-30 (framework-versions-oct19-verified).

## Why it matters for ACI
- Reinforces, rather than changes, ACI's architecture decision: the deterministic Python pipeline with LLM-at-the-edges avoids exactly the cost/weight profile CrewAI shows in this test (2x per-answer cost vs Mastra) and the state-management overhead LangGraph exists to solve. If ACI ever adds a second orchestration layer, the shortlist stays LangGraph (stateful, debuggable) vs Pydantic AI (typed) — not CrewAI, and not AutoGen (frozen).
- The install-weight numbers are a deployment note for any future agent-runtime packaging: ~400 MB installs argue for keeping the ACI runtime lean and vendored, not framework-heavy.

## Action: WATCH
- No framework change. Keep the 31 Oct landscape note as the canonical reference; this file is the Nov 1 confirmation + cost data.

## Sources (checked 2026-11-01)
- Geekflare framework comparison, refreshed 1 Nov 2026: https://geekflare.com/open-source/ai-agent-frameworks/
- AutoGen maintenance-mode confirmation (Oct 2026): https://dev.to/bitneka/single-agent-vs-multi-agent-a-decision-framework-for-enterprise-teams-b5b
- Prior ACI notes: 2026-10-31-framework-landscape-oct31.md, 2026-10-30-framework-versions-oct19-verified.md
