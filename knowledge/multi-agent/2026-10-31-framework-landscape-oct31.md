# Multi-agent framework landscape — 31 Oct 2026: stars vs shipping choices

**Date noted:** 2026-10-31
**Category:** multi-agent / orchestrator selection

## What changed
- **DeepSeek Harness** (open-sourced 13 Aug 2026, MIT, developer preview) now holds **~248,000 GitHub stars** (verified via GitHub API 12 Oct 2026) — more than LangChain (~148,000). It is pitched as a *harness* (model, tools, skills and UI all plugins), not a framework you write code inside. Stars measure buzz, not production use.
- **Microsoft's consolidation is complete**: AutoGen is in **maintenance mode** — no new features, community-managed — and the unified **Microsoft Agent Framework** (1.0 GA April 2026; 1.22 tracked 2026-10-22) is the recommended successor for new projects. The Oct 2026 framework census confirms the same.
- October-2026 shipping state (Geekflare refresh, 31 Oct 2026; framework census checked 8 Oct 2026):
  - **LangGraph** — MIT, ~44k stars, latest release Oct 2026; the pick for resilient, stateful, auditable agents. LangSmith Plus ~$195/10k traces (paid observability optional).
  - **CrewAI** — MIT, ~60k stars, 1.15.25 shipped 7 Oct 2026; role-based crews, fastest path to a working team; free tier 50 runs/month.
  - **Pydantic AI** — MIT, ~20k stars; typed Python, validated I/O.
  - **Mastra** — ~28.6k stars; TypeScript pick. **Google ADK** and **OpenAI Agents SDK** (still pre-1.0) also shipped October releases.
  - **AG2** (community fork of AutoGen 0.2) — Apache-2.0, ~5k stars, Oct 2026 release; the continuity path for existing AutoGen 0.2 systems.
  - Quiet: Hugging Face **smolagents** — no release since 29 May 2026.
- The fall-2026 pattern, consistent with ACI's own 2026-10-26 "single-agent-first" note: most teams ship on LangGraph, CrewAI, or the OpenAI Agents SDK; multi-agent is adopted where the workflow needs it, not by default.

## Why it matters for ACI
- ACI's architecture is already deterministic-pipeline-first (Python for computable agents, LLM only where interpretation is needed — per the trading-system design doc's lesson, which generalizes). This landscape confirms that choice: the frameworks that win in production are the ones with explicit state, retries, and auditability (LangGraph-style), not the most-starred harness.
- **Do not chase DeepSeek Harness**: a developer-preview harness with 248k stars is a hype signal, not a migration candidate. Evaluate only if it reaches a stable release with a persistence/audit story.
- If ACI ever needs a second orchestrator (e.g. a .NET/enterprise deployment), Microsoft Agent Framework is the supported path — not AutoGen, which is frozen.
- No change to ACI's current stack: ACI's backend is FastAPI + deterministic pipeline, not a hosted agent framework.

## Sources
- Fall-2026 landscape, 12 Oct 2026: https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html
- 19-framework census, checked 8 Oct 2026: https://aireviewrating.com/articles/best-open-source-ai-agent-frameworks
- Comparison refresh, data refreshed 31 Oct 2026: https://geekflare.com/open-source/ai-agent-frameworks/
- Decision framework (AutoGen maintenance mode, Agent Framework 1.0): https://dev.to/bitneka/single-agent-vs-multi-agent-a-decision-framework-for-enterprise-teams-b5b

## Action: IGNORE (DeepSeek Harness) / WATCH (others)
- Ignore DeepSeek Harness until a stable release with persistence/audit exists. Keep LangGraph as the reference orchestrator if ACI adds a stateful agent workflow; keep Microsoft Agent Framework noted as the AutoGen successor. No adoption, no install.
