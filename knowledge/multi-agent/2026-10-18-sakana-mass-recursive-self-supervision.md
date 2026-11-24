# Sakana AI's MASS — multi-agent workflows as training signal for recursive self-improvement

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** ADOPT (pattern-level) — add data contracts to inter-agent stages + champion-comparison eval in the evaluator-optimizer design.

## What changed
Sakana AI + UC Berkeley submitted "Recursive Self-Improvement through Multi-Agent Self-Supervision" (arXiv 2610.12176) on 8 Oct 2026. A single base model (Qwen3.6-27B) alternates between evolutionary workflow optimization (solver/optimizer/evaluator roles; workflows as written plans with roles, instructions, and explicit data contracts like `no_future_leakage: bool`, plus hop order) and LoRA fine-tuning on self-ranked trajectories (champion workflow run 18× per task, Bradley-Terry scoring, top 16 kept). Two cycles lifted win rates 53.9% → 69.9% and 1.2–1.6× performance per output token on four open-ended research benchmarks (honest misses: 0.96× Terminal-Bench 2.0, 0.94× SWE-bench Verified). Key ablations: role generalization improved evaluator agreement with external judges 73% → 93%, and upgrading the *optimizer* mattered far more than upgrading the *evaluator* to GPT-5.5. The authors name homogeneous self-evaluation's shared blind spots as recursive self-improvement's "Achilles' heel" and mitigate with external judges.

## Why it matters for ACI
Directly actionable for our evaluator-optimizer pattern (pattern 5 in ARCHITECTURE.md). Three borrowable mechanics:
1. Explicit data contracts between pipeline stages (required artifacts + checks) instead of free-text handoffs — matches our evidence-ledger discipline.
2. Champion-vs-candidate workflow comparison: run the current mission workflow against a revised one and score head-to-head on labelled cases, mirroring our existing "budget-matched single-agent baseline" rule.
3. The optimizer-bottleneck result: if we ever add an LLM reranker or reflection step, invest in the *revision* model, not a bigger grader — and keep the evaluator a *different* model than the generator to dodge the shared-blind-spot failure mode.

## Sources
- "Recursive Self-Improvement through Multi-Agent Self-Supervision (arXiv:2610.12176)" — https://arxiv.org/abs/2610.12176 — 2026-10-08
- "Sakana AI's MASS Turns Multi-Agent Teams Into Training Data for Recursive Self-Improvement" — https://getaibook.com/news/sakana-mass-recursive-self-improvement-multi-agent-self-supervision/ — 2026-10-12
