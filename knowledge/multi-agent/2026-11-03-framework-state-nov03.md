# Multi-agent framework state, 3 Nov 2026 — LangGraph/CrewAI ship weekly, AutoGen frozen, harness hype

## What changed
- **Fall-2026 snapshot** (dreaming.press, 12 Oct 2026; LinkedIn field guide, 20 Oct 2026; dev.to decision framework, Oct 2026 — three independent sources agree): LangGraph **1.2.14** (6 Oct, near-weekly cadence) remains the production default for stateful, debuggable, multi-step work; CrewAI **1.15.27** (9 Oct) the role-based crew pick; Google ADK, Agno, Pydantic AI all shipped within days of each other mid-October.
- **Microsoft consolidation complete**: AutoGen frozen (no feature commits since April; maintenance mode, community-managed) → unified **Microsoft Agent Framework** (Python + .NET, 1.0 GA April 2026, LTS commitment; Go SDK in public preview). AutoGen README now redirects newcomers to MAF. AG2 continues as a community fork led by the original creators.
- **DeepSeek Harness** (open-sourced 13 Aug 2026, MIT, developer preview): ~248k stars by 12 Oct — more than LangChain (~148k) — but stars measure buzz, not production use; LangGraph/CrewAI/OpenAI Agents SDK remain what teams ship. Treat Harness as hype signal, not a framework decision.
- **Protocols over frameworks**: MCP (tool/data access) + A2A (agent-to-agent discovery/messaging) are the 2026 interoperability layer — a CrewAI agent and a LangGraph agent can share MCP servers and coordinate via A2A. Single-agent-first remains the right default (26 Oct nightly): multi-agent only when the task structure genuinely needs it.
- No new LangGraph/CrewAI version numbers surfaced tonight beyond the mid-October snapshot (1.2.14 / 1.15.27, with 1.2.15–16 / 1.15.28 noted 27–29 Oct) — no delta worth a version bump tonight.

## Why it matters for ACI
- ACI's 5-pattern architecture is framework-agnostic by design (Python for computable agents, LLM only where interpretation is needed). The framework news confirms that choice: the durable layer is the protocol (MCP/A2A) and the state/checkpoint discipline (LangGraph-style), not any single framework's API.
- If ACI ever adopts a framework for a mission agent, the decision tree from the dev.to framework stands: long-lived/auditable → graph-based; role-shaped delegation → hierarchical CrewAI; Microsoft stack → MAF, never new AutoGen.

## Sources
- https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html (12 Oct 2026)
- https://www.linkedin.com/pulse/ai-agentic-framework-landscape-2026-what-survived-ahamed-uwsyc (20 Oct 2026)
- https://dev.to/bitneka/single-agent-vs-multi-agent-a-decision-framework-for-enterprise-teams-b5b (Oct 2026)

## Action
- **Watch**: DeepSeek Harness only as a hype indicator; MAF Go SDK preview for completeness.
- **Ignore** for ACI: no framework adoption tonight — architecture stays framework-agnostic, protocols-first.
