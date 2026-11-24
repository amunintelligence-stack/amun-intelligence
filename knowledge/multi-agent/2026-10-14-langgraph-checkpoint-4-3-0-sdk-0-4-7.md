# LangGraph checkpoint packages 4.3.0 / 3.1.x + SDK 0.4.7 — replay & delta fixes (2026-10-12)

**Date:** 2026-10-14 (releases: 2026-10-12)
**Category:** multi-agent / orchestration — durable execution

## What changed
LangChain shipped a coordinated set of LangGraph persistence releases on
2026-10-12 (after the core `langgraph` 1.2.13/1.2.14 covered on 2026-10-11):
- **langgraph-checkpoint 4.3.0** — fixes for delta history, namespace
  validation, and serialised data.
- **langgraph-checkpoint-postgres 3.1.3** — fixes for empty `checkpoint_id`
  handling plus a delta-walk performance improvement.
- **langgraph-checkpoint-sqlite 3.1.2** — fixes for empty `checkpoint_id`
  handling and namespace label validation.
- **langgraph-sdk 0.4.7** — fixes for thread-stream run ending and delta
  channel replay ordering.

The through-line: checkpoint replay and delta-channel ordering — the machinery
that lets a long-running graph pause, resume, and replay exactly — got
correctness and performance fixes across all three checkpointer backends at
once.

## Why it matters for ACI
ACI's mission runner is its own deterministic Python pipeline, not LangGraph —
but it has the same durability requirements (pause/resume, replay, audit
trail), and its checkpointing is Postgres-first with SQLite fallback, exactly
the two backends patched here. Two transferable lessons: (1) empty-checkpoint-ID
and namespace-validation edge cases are where durable systems corrupt state
silently — ACI's checkpoint code should have explicit tests for empty/None
checkpoint IDs and for namespace/label validation; (2) delta-walk performance
is the same hot path ACI hits when replaying long missions — worth profiling
once missions grow. If ACI ever adopts LangGraph for a subgraph, these are the
minimum versions to pin.

## Sources
- langgraph-checkpoint 4.3.0 release log, 2026-10-12:
  https://deployedbyai.com/log/214f97237676/langgraph-checkpoint-4-3-0/
- langgraph-sdk 0.4.7 release log, 2026-10-12:
  https://deployedbyai.com/log/29d6ba15e771/langgraph-sdk-0-4-7/
- langgraph-checkpoint-postgres 3.1.3 release log, 2026-10-12:
  https://deployedbyai.com/log/d3a7a58b816a/langgraph-checkpoint-postgres-3-1-3/
- langgraph-checkpoint-sqlite 3.1.2 release log, 2026-10-12:
  https://deployedbyai.com/log/d4b3710de20d/langgraph-checkpoint-sqlite-3-1-2/
- Note: entries are secondary summaries sourced from LangChain; verify against
  the LangGraph GitHub releases before pinning.

## Action
**Watch** — No LangGraph adoption. Add explicit ACI tests for empty/None
checkpoint IDs and namespace validation in the mission checkpoint path, and
profile delta replay on a long mission. If LangGraph is adopted later, pin at
least these versions.
