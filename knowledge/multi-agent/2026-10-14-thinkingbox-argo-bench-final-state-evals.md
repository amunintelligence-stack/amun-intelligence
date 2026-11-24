# ThinkingBox + Argo-Bench — agents graded on final state, not on what they said (Oct 2026)

**Date:** 2026-10-14 (ThinkingBox October coverage; Argo-Bench released 2026-10-01)
**Category:** multi-agent / evaluator-optimizer & reliability research

## What changed
Two October 2026 benchmarks push agent evaluation from "did the answer look
right" to "did the world end up right":
- **ThinkingBox** (Microsoft + Hugging Face; October coverage of the
  repeated-run results): grades agents on the final state of a backend
  database, not on their trajectory or text. Across 121,680 trials, 79,853
  attempts failed — and 67.24% of those failures ended *without any final tool
  error*. Headline: the best models (Claude Opus 5.5 / Opus 5) pass all 20
  attempts on only 241 of 507 tasks (47.53% pass^20), versus ~66.5% pass@1.
  The authors' thesis: "a trajectory is a claim; database state is the
  evidence." The gap between pass@1 and pass^20 is the **discovery–reliability
  gap**: a model can *find* a winning path yet fail to *repeat* it.
- **Argo-Bench** (TextQL Labs, released 2026-10-01): 210 enterprise operations
  / analytics tasks inside a simulated food-delivery data warehouse (81M
  orders, 235 tables, 7.5B rows), grading the real-world consequence of the
  agent's action. Best of 14 frontier/open models (Claude Opus 5.5) cleared the
  95-point "solved" bar on only 34.8% of tasks. Harness, grader, and dataset
  are public (GitHub + Hugging Face).

## Why it matters for ACI
ACI missions end in evidence, entities, and database state — exactly what
these benchmarks grade. Two direct applications: (1) **Evaluator design:**
ACI's evaluator-optimizer loop should score the *final stored evidence/graph
state* (did the mission write correct, sourced, deduplicated findings?), not
the agent's prose or tool-call trace. Silent failures — no tool error, wrong
outcome — were two-thirds of ThinkingBox failures, and they are the failure
mode ACI's evaluator must be built to catch. (2) **Reliability reporting:**
report ACI agent quality as pass^k (solved on *all* k runs), not pass@1 —
a single successful demo run proves discovery, not reliability. This is the
same honesty standard ACI already applies to its trading backtests.

## Sources
- ThinkingBox October reliability coverage (secondary), Oct 2026:
  https://explainx.ai/blog/microsoft-thinkingbox-agent-benchmark-database-state-reliability-2026
- ThinkingBox pass@1 vs pass^20 analysis (secondary):
  https://neuportal.ai/blog/ai-agent-reliability-thinkingbox-benchmark
- Argo-Bench release coverage, Oct 2026:
  https://shattered.io/argo-bench-ai-agent-benchmark-34-8-percent-2026/
- Note: these are secondary summaries; confirm figures against the primary
  papers/repos (ThinkingBox arXiv:2608.19741; TextQL Argo-Bench repo) before
  quoting numbers externally.

## Action
**Adopt the pattern** — Change ACI's mission evaluator to grade final
stored state (evidence rows / graph entities) plus a pass^k reliability
report over repeated runs, and add a "silent failure" check: missions that
ended with no error but wrote nothing verifiable must fail the gate. Pilot
the final-state grading on one mission type before rolling it out.
