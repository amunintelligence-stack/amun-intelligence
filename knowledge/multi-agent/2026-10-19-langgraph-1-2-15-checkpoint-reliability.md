# LangGraph 1.2.15 (12 Oct 2026) — latest 1.2.x, continuing the checkpoint/state reliability work

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — continue tracking the 1.2.x line; the reliability fixes in this patch train are the ones to port as patterns, not the version.

## What changed
- **langgraph 1.2.15** published to PyPI on 2026-10-12 (release files confirmed; registry last tracked 1.2.14 on the 11th). It closes the checkpoint-reliability patch train that started with 1.2.13 (checkpoint replay, update_state, DeltaChannel counters) and 1.2.14 (thread-stream run ending, delta-channel replay ordering, percent-encoded thread/assistant IDs in thread-stream requests).
- Per the upstream release PR trail (langchain-ai/langgraph #9165, merged for 1.2.14): "Keep an `update_state` on an older checkpoint out of its other branches" — replay-from-edit and forked `Command` writes no longer leak across branches; DeltaChannel counters are kept on every `update_state` path.
- The LangChain docs changelog for this cycle highlights the bigger durability features these patches harden: **DeltaChannel (beta)** (incremental deltas instead of re-serialized full state, with `snapshot_frequency=K` bounding read latency), **per-node timeouts** (`timeout=`, `run_timeout`, `idle_timeout` raising `NodeTimeoutError` with write-clearing + retry handoff), **node-level `error_handler`** returning `Command` for Saga/compensation patterns, and **graceful shutdown** (`RunControl.request_drain()` → resumable checkpoint).
- Note (independent reproduction, cairncommons.dev, issue #9218, checked 2026-10-07): on 1.2.13/1.2.14 a node `error_handler` that handles a failure still lets the exception reach the caller when the failing node shares a superstep with a sibling node. Fix status in 1.2.15 is unconfirmed — treat error-handler + sibling-node recovery as unreliable until verified.

## Why it matters for ACI
- ACI's orchestrator is hand-rolled, but the feature set LangGraph is converging on is the checklist for any durable mission runner: per-node timeouts with write-clearing, error handlers with compensation routing, checkpoint branches that don't leak state, and cooperative drain/resume. Our mission-run evaluator and retry logic should mirror these four primitives — timeout + compensation + isolated replay + drain.
- The issue #9218 reproduction is a concrete caution for anyone hand-rolling parallel-node recovery: exception semantics at superstep boundaries are where multi-node fault handling breaks. ACI's parallel pattern should enforce the same discipline — handler logic must run *before* the superstep closes, with a hard test on sibling-failure cases.
- No migration: the hand-rolled orchestrator stays. This line is pattern reference only.

## Sources
- "langgraph · PyPI — 1.2.15 release files" — https://pypi.org/project/langgraph/1.2.15/ — 2026-10-12
- "Changelog - Docs by LangChain (langgraph v1.2.0 entry)" — https://docs.langchain.com/oss/python/releases/changelog — 2026-10 (crawled ~2026-10-14)
- "LangGraph 1.2.13 and 1.2.14 re-raise a handled node error when a sibling node shares its superstep · Cairn Commons" — https://cairncommons.dev/post/4fd88a22-2db3-40ca-9be9-55ee4adec1e4 — 2026-10-07
- langgraph PR #9165 (update_state branch isolation) — https://github.com/langchain-ai/langgraph/pull/9165 — 2026-10-06
