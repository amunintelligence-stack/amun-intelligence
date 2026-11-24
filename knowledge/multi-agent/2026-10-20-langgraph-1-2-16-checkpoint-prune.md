# LangGraph 1.2.16 + checkpoint-postgres 3.2.0 (checkpoint pruning lands)

## What changed
LangGraph's Python release train shipped together (visible on the official GitHub releases page, checked 2026-10-20): `langgraph` 1.2.16, `langgraph-sdk-py` 0.4.8, `langgraph-cli` 0.4.37, and — most notably — `checkpoint-postgres` 3.2.0, which adds a `prune` method to `PostgresSaver` and `AsyncPostgresSaver`. The 1.2.16 fixes are all resume-reliability edge cases: letting other tasks finish when a resume value is invalid, applying a resumed `Command`'s update exactly once, stopping a subgraph from rerunning finished tasks on resume, and saving a resumed exit run's pending writes once. sdk-py 0.4.8 surfaces thread-stream errors instead of silently retrying a rejected stream.

## Why it matters for ACI
ACI's multi-agent design relies on checkpointed, resumable runs. These fixes remove a class of duplicate-execution and lost-write bugs that produce phantom evidence or double side-effects in long missions. The new `prune` API is the real prize: the OSS Postgres checkpointer previously had no native TTL (LangGraph issue #1138 has tracked ~100 checkpoint rows per traversal since 2025), forcing a cron-based cleanup. Pruning can now be built into ACI's session-management layer directly.

## Sources (with dates)
- github.com/langchain-ai/langgraph — releases page, verified live 2026-10-20 (1.2.16, sdk-py 0.4.8, checkpoint-postgres 3.2.0, cli 0.4.37)
- dev.to/the_movie_9b1357e8c99cfaa — "AI Agent Frameworks in 2026: CrewAI vs LangGraph vs AutoGen, Tested" (2026-10-19): version check confirms LangGraph 1.2.16
- dev.to/avenotech — "AI Agent Frameworks Compared: LangGraph vs CrewAI vs AutoGen" (2026-10-13): documents the missing checkpointer TTL (issue #1138)

## Action
watch
