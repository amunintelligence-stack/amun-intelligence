# Pydantic AI 2.57.0 (15 Oct 2026) — Harness ApprovalReviewer: model pre-approves low-risk tool calls

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — copy the two-tier approval pattern (model triages low-risk calls, human only sees high-risk) into ACI's approval gating; adopt nothing until a mission run needs it.

## What changed
- Pydantic AI **v2.57.0** released 2026-10-15 (GitHub; registry last tracked 2.56.0 on the 14th). Headline for us:
- **Harness `ApprovalReviewer`**: "let a model approve low-risk tool calls before a person sees them" (#10143). A model acts as a first-line reviewer that green-lights low-risk calls so the human approval queue only contains calls that actually warrant human attention.
- **Skills compatibility notes**: 2.57.0 honours `disable-model-invocation` and `user-invocable` in Skills and skips stray skill library paths (#10378) — the permission semantics for skill/plugin tools are being hardened.
- **MetaProvider for Meta Muse models** with `meta:` using the Responses API (#10156); **price requests at their reported service tier** (#10244) — cost telemetry per tier, not blended averages.
- **MCP Apps integration**: forward MCP Apps tool results to AG-UI and Vercel AI frontends; new `MCPToolset.read_resource_contents` (#10179) and `MCPToolset.call_tool_for_app` (#10190).
- Reliability fixes worth noting: token-based compaction retaining too little history (#9784 — context compaction bug), FallbackModel concurrency-slot release after streamed cleanup (#10225), `available_tool_names`/`active_capability_ids` surviving Temporal/Render task copies (#10280).

## Why it matters for ACI
- The `ApprovalReviewer` is the cleanest two-tier HITL pattern seen this week: a cheap model pre-classifies tool calls by risk, humans only approve the tail. ACI's orchestrator already gates irreversible actions behind approval — this pattern lets us scale approvals down to the per-tool-call level (e.g. agent-initiated WHOIS/DNS queries auto-approved, outbound notifications/email escalated). Pattern is framework-agnostic; implement in our own approval layer when approval fatigue becomes a bottleneck, not by adopting Pydantic AI.
- The MCP Apps forwarding (`call_tool_for_app`) is a preview of where tool-calling is heading: tool results rendered by frontends, not just models. If ACI's console ever needs to render tool output (e.g. a whois record as a structured card), this is the shape.
- The compaction bug (#9784, "token-based compaction retaining too little recent history") is a caution for our own mission-history truncation: keep recency floors, don't let compaction strip recent evidence.

## Sources
- "Release v2.57.0 (2026-10-15) · pydantic/pydantic-ai" — https://github.com/pydantic/pydantic-ai/releases/tag/v2.57.0 — 2026-10-15
- SourceForge PydanticAI activity mirror (release listing) — https://sourceforge.net/mirror/pydanticai/activity/ — 2026-10-15
