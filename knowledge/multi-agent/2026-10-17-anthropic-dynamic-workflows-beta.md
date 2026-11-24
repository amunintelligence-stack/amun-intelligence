# Anthropic dynamic workflows (beta) — agent-written programs orchestrating up to 1,000 agents

**Date of finding:** 2026-10-17
**Window covered:** last ~30 days

## What changed

- **Anthropic put dynamic workflows for Claude Managed Agents into public beta on 9 Oct 2026** (behind the `managed-agents-2026-04-01` beta header). Anthropic's one-line definition: "A workflow is a program that runs many agents in phases and combines their results."
- **How it differs from subagent delegation:** previously, Claude delegated to subagents conversationally (one level deep, ≤25 child threads). With dynamic workflows, **the agent itself writes a program** that orchestrates agents — passing results between them in code — while the main thread keeps talking to the user. The server runs the program in the background as a workflow run.
- **Scale limits (per Anthropic docs):** up to **1,000 agents over a run's lifetime**, up to **64 working concurrently**, **24-hour default lifetime**, up to **10 runs open per session** by default.
- **Anthropic's own benchmark:** with 70 bugs planted in a 116k-line codebase, a single agent found 14 / 15 / 27 across three runs; a dynamic workflow found **66 in each of its three runs**.
- **Cost model:** a run has no price of its own — its agents' tokens bill at each model's rates, plus Managed Agents **session runtime at $0.08 per session-hour**; a session budget can cap spend.
- **Control model — read carefully:** the agent decides when to start a run from the user message or system prompt; there is **no approval step for launching a run**, and **permission policies apply to the tools a run's agents call, not to starting the run**. Once a run starts, the agent cannot send follow-up messages to its threads. Runs are followed via `workflow_run.*` events on the session stream. Enable with `multiagent: {"type": "multiagent_20261001", "workflows": {"type": "enabled"}}`; with that type, workflows + subagents are enabled by default.
- **Same release-notes batch (14 Oct 2026):** Claude Developer Platform launched **beta OpenTelemetry export** for tracing Messages API requests and Managed Agent sessions (SDK emits spans in Python, TypeScript, C#, Go, Java, PHP, Ruby; API spans via an OpenTelemetry destination in Claude Console), and **scheduled deployments for Claude Managed Agents on Claude Platform on AWS**.

## Why it matters for ACI

- **This is the strongest vendor validation yet of ACI's own pattern:** deterministic orchestration programs + phased specialist agents + result merging — exactly what ACI's orchestrator module implements (chaining / routing / parallelization / evaluator-optimizer). Anthropic's 66-vs-27 bug-hunt gap is a useful citation for "phased multi-agent beats single agent on broad-sweep evidence work" — the shape of a corporate-intel mission (sweep many sources, verify, merge).
- **Cost/governance warning to copy:** a run that can self-launch 1,000 agents with no launch approval is a runaway-spend and blast-radius risk. ACI's standing rules (approval-gated irreversible actions, per-mission budgets, confidence-gated verdicts) are the correct counter-pattern. If ACI ever consumes Managed Agents, **disable workflows by default** and gate run-launch behind the same approval as any other bulk action; never rely on tool-level permission policies to bound fleet size.
- **Observability pattern to borrow:** OpenTelemetry export for agent sessions (spans across API + agent runs) is the shape ACI's mission tracing should aim for — one trace per mission spanning dispatch, tool calls, and verdict. ACI's mission_log is the seed; OTel-style spans are the target.
- **Not a migration:** ACI's orchestrator stays hand-rolled and provider-neutral. Managed Agents is a hosted, Claude-only, token-billed harness — useful as an external benchmark and a fallback execution path, not as ACI's core.

## Sources

- Anthropic Claude Developer Platform release notes, 9 Oct 2026 (dynamic workflows beta) and 14 Oct 2026 (OpenTelemetry export beta, scheduled deployments on AWS) — via Releasebot mirror: https://releasebot.io/updates/anthropic/claude-developer-platform
- CellCog, "Claude Dynamic Workflows: 1,000 Agents per Run" (Oct 2026) — https://cellcog.ai/blog/claude-dynamic-workflows/
- FourWeekMBA, "Claude Managed Agents Adds Workflows of Up to 1,000 Agents" (12 Oct 2026) — https://fourweekmba.com/ai-claude-managed-agents-adds-workflows-of-up-to-1000-agents/
- Mixed News, "Claude now writes its own programs to run up to 1,000 agents, and starts them itself" (Oct 2026) — https://mixed-news.com/en/claude-managed-agents-dynamic-workflows-1000-agents-permission-policies/

## Action

**Watch (adopt the patterns):** (1) keep ACI's orchestrator provider-neutral — no Managed Agents dependency; (2) borrow the phased-sweep + merge pattern and the 66-vs-27 citation for ACI's multi-agent justification; (3) adopt the governance counter-pattern — fleet-launch behind approval + per-mission budget caps; (4) target OTel-style mission tracing as the observability upgrade. **Ignore** — using Managed Agents dynamic workflows as ACI's execution engine (hosted, Claude-only, self-launching fleets).
