# Ruflo (Cognitum One, 13 Oct 2026) — open-source meta-harness: queen-led agent swarms + mission Mods

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — strong pattern reference (mission-driven orchestration, default-approval control plane, self-learning memory); no adoption — it's a coding-agent harness, not an OSINT mission platform.

## What changed
- **Ruflo**, an open-source (MIT) AI agent **meta-harness** from Cognitum One, announced its latest release 2026-10-13 via ACCESS Newswire. GitHub: `ruvnet/ruflo`; claims 74,000+ stars, 8,800 forks, 12.5M npm downloads in the last 12 months.
- What it is: turns one coding assistant (Claude Code, OpenAI Codex, or any MCP client) into a coordinated swarm of 100+ specialized agents (planner, coder, tester, reviewer, security, docs) with shared memory, model routing, and human approval controls.
- New capabilities in this release:
  - **Ruflo Mods**: "one mission, end to end" — a Mod turns a single mission statement into a complete agent workflow (research → build → test → validate → secure → benchmark → learn). Mission logic travels with the agent rather than living in an external doc.
  - **Control plane (Ruflo Console)**: missions, workflows, agent activity, logs, token usage, cost in one view. Admins grant read/write/manage/full control; **default posture is read access with approval**; a "Take back control" switch pauses the console tools at any time.
  - **Cross-machine federation**: independent Ruflo installs discover each other and delegate subtasks; remote agents start untrusted, prove identity via mTLS + Ed25519 challenge-response (no shared secrets); behavioral trust scoring upgrades/downgrades peers.
  - **PII data gating**: configurable 14-type detection pipeline scans outbound federation messages (emails, API keys, SSNs) before they leave the local machine; per-trust-level policies (block/redact/hash/pass); HIPAA/SOC 2/GDPR audit modes.
  - **SONA self-learning memory**: successful execution patterns captured as local embeddings (HNSW-indexed AgentDB), reused across tasks without retraining.
  - **314 native MCP tools** + 26 CLI commands + 35 plugins; **adaptive backpressure** on swarm messaging; **MetaHarness** readiness grader (1–100) with security scanning of tool configs.
- Honest caveats (from the dev.to deep-dive, 2026-10-14): swarm coordination overhead grows faster than swarm size; every agent burns tokens; "behavioral trust scoring" is under-specified — treat federated peers as adversarial in production; stars ≠ production guarantee.

## Why it matters for ACI
- **The premise is the finding**: "an agent is a model plus a harness" — most agent failures are harness failures (uncapped spend, no memory, no data gating, no audit). ACI's architecture already reflects this (orchestrator, mission log, approval gates), and Ruflo's public checklist is a useful external validation of that design philosophy.
- **Ruflo Mods are the mission-shape ACI wants**: one mission statement → full loop (research → act → verify → secure → learn). ACI mission templates should encode the whole loop once, not repeat review logic per workflow.
- **Default-approval posture** matches our standing rules (approval-gated irreversible actions); the "Take back control" pattern is a good model for a mission-level kill switch.
- **SONA's trajectory-memory idea** complements yesterday's Sakana MASS finding: capture successful mission trajectories as reusable patterns — but keep it external to the model, in the RAG store, not in a per-project DB.
- **Not a migration or integration**: Ruflo orchestrates coding agents on developer machines; ACI runs intel missions on our own stack. No adopt, no key needed, but keep the pattern notes. Federation + PII gating design is a reference for any future multi-site ACI deployment (run PII gating in block mode until every redaction decision is audited on real traffic).

## Sources
- "Cognitum One Releases Ruflo, AI Agent Orchestration for Claude Code and Codex, with Mission-Driven Mods and a Single Agent Control Plane" (ACCESS Newswire via Morningstar) — https://www.morningstar.com/news/accesswire/1236128msn/cognitum-one-releases-ruflo-ai-agent-orchestration-for-claude-code-and-codex-with-mission-driven-mods-and-a-single-agent-control-plane — 2026-10-13
- "Ruflo: The Open-Source Meta-Harness Running 100-Agent Coding Swarms" (dev.to deep-dive with limits) — https://dev.to/cortexflow_tech/ruflo-the-open-source-meta-harness-running-100-agent-coding-swarms-3609 — 2026-10-14
