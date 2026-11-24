# Framework landscape delta, 2 Nov 2026: AutoGen frozen (3rd confirmation) + MAF 1.26.0

**Date noted:** 2026-11-02
**Category:** multi-agent — reference only: ACI's pipeline is deterministic Python; LLM only where interpretation is needed

## What changed
- **AutoGen maintenance mode — third independent confirmation this cycle.** Three comparisons updated 30 Oct – 2 Nov 2026 (Spheron, Concision, UMA Technology) all state the same end-state: AutoGen receives bug fixes/security patches only, is community-managed, and Microsoft's README directs new users to **Microsoft Agent Framework**. Concision (30 Oct) sharpens it to "archived" in Microsoft's guidance. ACI's 31 Oct landscape note + 1 Nov refresh already recorded this; tonight is confirmation, not news — no new AutoGen release exists to track.
- **Microsoft Agent Framework .NET 1.26.0** (checked 2 Nov 2026) with `Microsoft.Agents.AI.Mcp` alpha (long-running MCP tasks, MCP-delivered skills) — see tonight's MCP note for the SDK 2.2.0 stateless-default detail.
- **CrewAI 0.80+**: dynamic agent instantiation (3 agent templates × N instances instead of 10 specialist agents) and 2B agent executions / 150+ enterprise customers claimed for the trailing 12 months (vendor claim, unverified). CrewAI AMP free tier: 50 executions/month.
- Evaluator-relevant stat: a **2026 study of 6,259 deployed agents measured a 56.6% task success rate** — cited as the reason recovery design matters more than framework choice.

## Why it matters for ACI
- Reinforces the standing decision: hand-rolled deterministic orchestrator stays; the shortlist for any future second layer remains LangGraph (stateful, debuggable) vs Pydantic AI (typed) — not CrewAI, not AutoGen (frozen).
- The 56.6% figure is a useful calibration for ACI mission-confidence reporting: a pipeline that claims high confidence without a recovery/retry story is the exception, not the norm. It supports ACI's existing confidence-cascade + evidence-judged verdicts design.

## Action: WATCH
- No framework change. Keep the 31 Oct landscape note canonical; this file is the 2 Nov confirmation + version numbers.

## Sources (checked 2026-11-02)
- Spheron comparison (AutoGen maintenance mode, 56.6% study): https://www.spheron.network/blog/langgraph-vs-crewai-vs-autogen-2026/
- Concision comparison, updated 30 Oct 2026: https://concision.ai/blog/comparing-multi-agent-ai-frameworks-crewai-langgraph-autogpt-autogen
- UMA Technology guide: http://umatechnology.org/langgraph-vs-crewai-vs-autogen-in-2026-which-should-you-choose/
- MAF .NET MCP guide (1.26.0, checked 2 Nov 2026): https://codehalwell.github.io/AgentGuides/microsoft-agent-framework-guide/dotnet/microsoft_agent_framework_dotnet_mcp/
- Prior ACI notes: 2026-11-01-framework-refresh-nov01.md, 2026-10-31-framework-landscape-oct31.md
