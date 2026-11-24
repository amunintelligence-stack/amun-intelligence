# Pydantic AI security fix v2.53.0 — GHSA-6fqq-452j-qhrp, streaming concurrency-limiter DoS (HIGH)

**Date:** 2026-10-14 (advisory + fix: 2026-10-01/02)
**Category:** multi-agent / security — NOT CRITICAL to ACI's own stack

## What changed
Pydantic AI v2.53.0 (2026-10-01) fixed a HIGH security issue (CVSS 3.1: 7.5,
availability impact) in `ConcurrencyLimitedModel`, advisory
GHSA-6fqq-452j-qhrp. A streamed request through `ConcurrencyLimitedModel` or
`limit_model_concurrency` could keep its concurrency slot when the slot was
released on a different task than the one that acquired it — after an early
exit (consumer stopped iterating, raised, or was cancelled), and also after
fully consuming `stream_text()` with its default debouncing. Repeated streams
could then exhaust every slot, blocking all requests sharing the limiter.
Agent-level `max_concurrency` and non-streaming requests were not affected;
v1 was not affected. The fix also changed limiter-sharing semantics: a model
wrapper now raises `UserError` when it shares a limiter with the requesting
agent or an enclosing wrapper, `acquire()` takes a slot on every call, and a
custom `AbstractConcurrencyLimiter` must allow `release()` from another task.
v2.53.0 is the first fixed version; v2.54.0 (2026-10-03) and later include it.

## Why it matters for ACI
ACI does not run Pydantic AI, so this is **not** a direct exposure. It matters
as a design warning for ACI's own concurrency controls: any limiter/semaphore
around LLM calls or tool execution must release on *every* exit path —
cancellation, early return, exception — and must be safe when acquire/release
happen on different tasks. ACI's mission runner and any future streaming
endpoint should be audited against exactly this failure shape (a slow slot
leak that looks like "the system just got slower" until it wedges).

## Sources
- Pydantic AI v2.53.0 release notes (primary), 2026-10-01:
  https://github.com/pydantic/pydantic-ai/releases/tag/v2.53.0
- Upgrade checklist / advisory summary, Oct 2026:
  https://rohitai.com/blog/pydantic-ai-streaming-concurrency-limiter-security-upgrade

## Action
**Watch / audit own code** — No dependency to bump (Pydantic AI is not in
ACI's stack). Audit ACI's own concurrency limiters (LLM-call semaphore,
tool-execution pool) for the same leak: release in `finally`, tolerate
cross-task release, and add a metric/alert for limiter saturation so a leak
shows up before it wedges missions.
