# Arize AI: shipped a memory file, not a temporal KG (2026-10-19)

## What changed
Arize AI published a detailed postmortem on building long-term memory for Alyx (published 2026-10-19). They prototyped with **Zep's Graphiti** temporal knowledge graph, then shipped the opposite: one always-loaded, 8,000-character structured text file per user/space (User Profile, Goals, Projects, Assets, Conventions, Corrections), updated by background summarization jobs. Key numbers: a Graphiti `add_episode` for 5 entities/6 facts costs ~10 LLM calls without custom types, >20 with them, on every turn; their shipped file scored 16/18 on memory-dependent evals at ~2,000 tokens/read. They also evaluated memory's harm direction (questions memory could make worse) — and ChatGPT/Claude landed on the same always-loaded-profile shape.

## Why it matters for ACI
ACI is eyeing temporal KG for agent memory. This is honest, measured evidence on Graphiti's operational cost and a concrete cheaper pattern that production AI tools converged on. Adopt two things: (1) the two-directional eval (memory-needed vs memory-could-hurt) for ACI's memory tier; (2) the "structured profile always in context + retrieval for the long tail" hybrid before defaulting to a full temporal graph.

## Sources (with dates)
- Arize AI blog, published 2026-10-19, updated 2026-10-19: https://arize.com/blog/alyx-agent-long-term-memory-architecture/
- Referenced: Graphiti main branch (Sept 2026), Mem0 arXiv:2504.19413, Letta filesystem-memory eval (Aug 2025).

## Action
adopt
