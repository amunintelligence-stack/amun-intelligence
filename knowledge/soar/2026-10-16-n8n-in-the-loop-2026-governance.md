# n8n In The Loop 2026 (Berlin, 13–14 Oct) — production agents = governance + human oversight

**Date:** 2026-10-16 (event 2026-10-13/14, Berlin; agenda reported 2026-10-07/09)
**Sources:** https://dev.to/alifar/n8n-in-the-loop-2026-will-examine-what-makes-ai-agents-ready-for-production-2pmp (secondary); https://dev.to/alifar/n8n-in-the-loop-2026-will-put-its-vision-and-next-product-chapter-on-the-agenda-36p0 (secondary)

## What changed
n8n's In The Loop 2026 ran 13–14 Oct 2026 in Berlin (Partner Day 13 Oct, Ecosystem Day 14 Oct). The program's stated focus: what makes AI agents ready for production — building with n8n, operating at scale, **governance, safety, guardrails, and human oversight** for AI-enabled automation. Speakers listed include people from Webflow, TELUS, Albertsons, and Bosch. The published agenda did **not** announce a specific new product release; a separate item notes n8n's interest in connected, agentic automation with human oversight, with no confirmed end-to-end design-automation product. The recurring theme: apply deterministic rules + human review to probabilistic AI; review steps control ambiguous or high-impact workflow outcomes.

## Why it matters for ACI
ACI's mission pipeline runs through n8n (mission trigger workflow) plus the backend orchestrator. The event's framing validates ACI's existing design choices — confidence-gated verdicts, evidence-judged outputs, and approval gating before any irreversible external action — and signals where n8n's own roadmap is heading: guardrails (cf. 2.43.0 publish guardrails, tracked 2026-10-15) rather than new agent capabilities. If n8n ships governance features (approval UX, audit trails) from this direction, ACI's SOAR playbooks should consume them instead of building parallel gates.

## Action
**Watch.** Keep approval-gating + evidence-judged verdicts as ACI's SOAR defaults; track n8n's post-event governance releases for reusable guardrails. No workflow changes.
