# n8n Assistant (9 Sep 2026) + n8n Agents (25 Sep 2026) — agent layer beside workflows

**Date researched:** 2026-10-14
**Status:** Watch — evaluate for mission triage once self-hosted/Docker availability is confirmed.

## What changed
- **n8n Assistant** (launched 9 Sep 2026, supersedes the AI Workflow Builder beta): plain-language requests → editable workflow on the canvas. It plans the workflow, adds nodes, asks for credentials when required, executes, and iterates on fixes. The generated workflow remains the single source of truth — visible, editable, with execution history and logs. Runs behind a preview flag; on n8n Cloud by default; self-hosted Docker support from a specified version; Enterprise support planned. Usage billed in AI credits, separate from prior AI Workflow Builder usage.
- **n8n Agents** (introduced 25 Sep 2026): configurable AI agents for tasks that don't fit a fixed sequence. An agent has its own model, instructions, triggers/channels, tools, memory, sessions, and approvals. Channels: Slack, Telegram, schedule, or as a step inside another workflow. Agents can call workflows as tools; workflows can invoke agents. Available on n8n Cloud's latest stable, with community self-hosting and Enterprise preview options. Cost: AI credits + execution usage.
- The two are positioned as complementary, not competing: deterministic steps stay in workflows; interpretation, follow-up, and routing decisions go to agents. The official n8n Agents announcement (blog.n8n.io) describes agents as configurable units (task + model + tools + workflows).

## Why it matters for ACI
- ACI missions are exactly the hybrid pattern n8n now supports natively: deterministic recon/enrichment pipelines (workflows) + judgment calls (triage, follow-up questions, routing). Today ACI implements the judgment layer with its own orchestrator/evaluator agents; n8n Agents could host or prototype that layer with approvals, memory, and Telegram channels built in — the Telegram channel is directly relevant since ACI-adjacent bots already live there.
- **Cost/governance caveat:** agents consume AI credits + executions, and quality depends on instructions/model/tools. An unbounded agent on a mission pipeline is a spend and correctness risk. The approvals feature is the control that makes this usable for ACI (human gate before destructive/containment actions).
- Interacts with n8n 3.0 (see `2026-10-14-n8n-3-0-breaking-changes.md`): AI Agent node v1 is removed in 3.0, so any agent work should target the current agent/Agents constructs, not v1.

## Action
**WATCH:** no build yet. On the next n8n upgrade cycle, verify self-hosted Docker availability + credit pricing for Assistant/Agents, then pilot ONE bounded use case (e.g. intake-and-routing triage with an approval gate) before considering mission use. Do not hand an agent broad tool access on day one.

## Sources
- "n8n Assistant and Agents Expand AI Automation…" (DEV, 13 Oct 2026, summarizing official announcements): https://dev.to/alifar/n8n-assistant-and-agents-expand-ai-automation-from-workflow-design-to-ongoing-tasks-ml6
- n8n official Agents announcement (blog.n8n.io, linked from the above)
- Assistant-supersedes-Builder note (n8n blog, Sep 2026, via n8n-challenges analysis, 8 Oct 2026): https://github.com/itspoma/n8n-challenges/blob/HEAD/content/blog/en/article-d4333b57-cc1f-4406-85a5-65c95551e365.md
