# CrewAI 1.15.28 (14 Oct 2026) — `crewai eval` reports where a stopped model broke

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — borrow the eval-loop shape (failure-point localization + stop reasons + per-run cost/time) for our mission_log evaluation; do not migrate frameworks.

## What changed
CrewAI shipped 1.15.28 on 14 Oct 2026 (registry last covered 1.15.27 on the 12th). The headline feature: the new `crewai eval` command now reports *where a stopped model broke* — pinpointing the failure point of a halted model run — plus LiteLLM catalog use for context windows. This extends an eval tooling streak: 1.15.24 added `crewai eval` markdown briefs for agent runs, `--models` model/role swapping, and exit-code-1-unless-gate-passed; 1.15.27 added eval stop-reasons and per-run cost/time tracking. The trajectory is clear: every traced run is graded, failure points are localized, and gates block deployment.

## Why it matters for ACI
This is the exact eval-loop shape our registry already adopted as discipline (confidence cascade + evidence-judged verdicts + final-state grading + pass^k from Argo-Bench). CrewAI's "report where it broke + stop reason + cost/time per run" is a checklist we can copy into our own mission-run evaluation: mission_log already stores status/result/confidence; the missing pieces are per-stage failure localization and per-run cost/time. No migration — our hand-rolled orchestrator stays per the registry decision.

## Sources
- "Changelog - CrewAI (official docs)" — https://docs.crewai.com/v1.15.28/en/changelog — 2026-10-14
- "CrewAI 1.15.28 | The Deploy Log" — https://deployedbyai.com/log/31ec3ee26d09/crewai-1-15-28/ — 2026-10-14
