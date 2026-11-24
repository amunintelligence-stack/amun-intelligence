# Microsoft Agent Framework (AutoGen's successor) at Python 1.22.0 — AutoGen effectively frozen

**Date found:** 2026-10-22 (1.22.0 released 2026-10-15; 1.21.0 on 2026-10-08)
**Category:** multi-agent / orchestrator frameworks

## What changed
- Microsoft **finished its consolidation**: Semantic Kernel + AutoGen were folded into the single **Microsoft Agent Framework** (Python + .NET, MIT). AutoGen has taken **no feature commit since April 2026** — the 61k-star project is effectively frozen, and the framework conversation moved to Agent Framework.
- The Python package is on a **~weekly cadence**: 1.0.0 (April 2) → **1.21.0 (Oct 8)** → **1.22.0 (Oct 15)**, with Python 3.15 support; NuGet `Microsoft.Agents.AI` at 1.25.0. Stable at 1.0: single agents with first-party connectors (Foundry, Azure OpenAI, OpenAI, Anthropic, Bedrock, Gemini, Ollama), middleware, memory/context providers, graph workflows with checkpointing, and sequential/concurrent/handoff/group-chat/Magentic-One orchestrations.
- Security-relevant change in **1.21.0** (Oct 8): fixes a side effect of an earlier security fix — the 1.19 label-tracking middleware made security labels restrict-only, removing the only channel a tool had to provide **explanatory context about its own hidden output** (a hidden failed compile and a hidden clean compile looked identical to the model, and integrators had resorted to declaring whole tools "trusted"). The fix lets a tool declare `standing_guidance` — fixed sentences attached as trusted content by the middleware itself, never passing through the tool body, so attacker-controlled tool inputs can't alter it. Also: provider-owned session state is now isolated per delegated agent-tool call (fail-closed), and Purview integration can evaluate policy on the full buffered text of a streamed response.
- Context: nothing newer than Oct 20 for the covered incumbents — LangGraph 1.2.16 and OpenAI Agents SDK 0.24.0 (both Oct 20, covered last night) remain the latest sighted; CrewAI 1.15.27 (Oct 9), Agno 3.1.2 (Oct 8), Pydantic AI 2.55.0 (Oct 9), Google ADK 2.11.0 (Oct 2).

## Why it matters for ACI
ACI's 5-pattern architecture currently uses plain Python for the deterministic agents and reserves an LLM "mind" via 3a2l. If we ever formalize the LLM-agent layer, the framework shortlist should be: LangGraph (default for stateful/durable orchestration), CrewAI (role crews), OpenAI Agents SDK (lightweight), Pydantic AI (typed) — and **Microsoft Agent Framework as the Microsoft-stack pick instead of AutoGen**. AutoGen should not be chosen for anything new. The `standing_guidance` pattern is worth stealing conceptually for our own prompt-injection posture: fixed declaration-time guidance that tool bodies can't rewrite.

## Sources (with dates)
- GitHub release python-1.21.0 (2026-10-08): https://github.com/microsoft/agent-framework/releases/tag/python-1.21.0
- developersdigest.tech, "Microsoft Agent Framework in October 2026: What Changed Since 1.0" (Oct 2026): https://www.developersdigest.tech/blog/microsoft-agent-framework-whats-new-2026
- tech-insider.org, "Microsoft Agent Framework Setup: 13 Steps [2026]" (2026-09-28): https://tech-insider.org/microsoft-agent-framework-setup-2026/
- aicassindra.com Framework Watch on 1.21 standing_guidance (2026-10-11): https://www.aicassindra.com/research/2026/10/11/framework-watch-pydantic-ai-2-55-microsoft-agent-framework-1-21-standing-guidance.html
- dreaming.press, "AI Agent Frameworks: What Actually Changed This Fall (October 2026)" (Oct 2026): https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html

## Action: WATCH
Record Microsoft Agent Framework (not AutoGen) as the Microsoft-ecosystem option in ACI's framework notes. No migration or install — ACI's current Python-deterministic design is unaffected. Revisit if the LLM-mind (3a2l) phase needs a framework.
