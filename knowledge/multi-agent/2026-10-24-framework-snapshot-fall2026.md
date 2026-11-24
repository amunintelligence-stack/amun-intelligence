# Multi-agent framework snapshot, fall 2026 + orchestration cost benchmark

## What changed
- Fall-2026 framework roundup (dreaming.press, mid-Oct 2026): LangGraph 1.2.14
  (Oct 6, near-weekly cadence) remains the production default for stateful,
  graph-based orchestration; CrewAI 1.15.27 (Oct 9) for role-based crews; Agno 3.1.2
  (Oct 8) repositioned as a "platform"; Pydantic AI 2.55.0 (Oct 9) for type-safe I/O;
  Google ADK 2.11.0 (Oct 2); OpenAI Agents SDK 0.23.1 (Oct 2, still pre-1.0).
- Microsoft consolidation confirmed: AutoGen (~61k stars) has taken no feature commit
  since April 2026; development moved to the unified Microsoft Agent Framework
  (Python 1.21.0, Oct 8). Starting fresh on the Microsoft stack means starting there,
  not on AutoGen. LlamaIndex repositioned toward document processing / data + RAG
  agents rather than general orchestration.
- Cost benchmark (Kulkarni & Kulkarni, arXiv:2603.22651, March 2026, cited Oct 2026):
  on SEC filings, reflexive self-correcting loops reached the highest field-level F1
  (0.943) at 2.3x a sequential baseline; hierarchical supervisor-worker reached F1
  0.921 at 1.4x cost — the best cost-accuracy point; a hybrid recovered 89% of the
  reflexive gains at 1.15x baseline. Mapping: CrewAI hierarchical = supervisor-worker
  row; LangGraph cyclic graphs = reflexive loop; AutoGen group chat = a third, less
  disciplined shape.
- Corroborating guidance (toolbit.ai, updated Oct 21, 2026; dev.to, Oct 20, 2026):
  teams that start on CrewAI and later hit audit-trail / exactly-once / recoverable-
  failure requirements usually move the core workflow to LangGraph, not the reverse.

## Why it matters for ACI
- ACI's orchestration is deliberately deterministic (Python pipeline, n8n validate
  node, mission → agent roster mapping) rather than framework-driven. This snapshot
  validates that choice: the field is converging on "LangGraph when behavior must be
  auditable and recoverable" — which is ACI's requirement — and the cost data says
  the reflexive loop's accuracy premium costs 2.3x, while hierarchical supervision
  gets nearly the same accuracy at 1.4x.
- Practical consequence for ACI mission design: default to hierarchical
  supervisor-worker shape; reserve reflexive self-correction loops for fields where
  a wrong value is expensive (entity identity, verdicts), not for every field.

## Sources
- dreaming.press, "AI Agent Frameworks: What Actually Changed This Fall (October 2026)":
  https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html
- toolbit.ai, "LangGraph vs. CrewAI", updated Oct 21, 2026:
  https://www.toolbit.ai/blog/langgraph-vs-crewai-choosing-the-right-python
- dev.to, "AI Agent Frameworks Compared: LangGraph vs CrewAI vs AutoGen", Oct 2026:
  https://dev.to/avenotech/ai-agent-frameworks-compared-langgraph-vs-crewai-vs-autogen-2l2o

## Action
- WATCH (design guidance, no framework adoption). Record the pattern rule in ACI
  mission design: hierarchical by default, reflexive loops only for high-cost fields.
  Do not start any new work on AutoGen; if a Microsoft-stack piece is ever needed,
  it starts on Microsoft Agent Framework.
