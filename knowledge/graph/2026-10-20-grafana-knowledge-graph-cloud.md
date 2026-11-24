# Grafana Cloud: Knowledge Graph in every stack (2026-10-20)

## What changed
Grafana Labs announced at ObservabilityCON 2026 (announced 2026-10-20) that every Grafana Cloud stack now includes a **Knowledge Graph** connecting infrastructure and application dependencies to user experience and incident response. The stated purpose: give people and AI agents one connected view, linking technical symptoms (a failing database) to the service, team and customer affected, so agents can investigate problems with shared context instead of raw telemetry.

## Why it matters for ACI
This is a mainstream "knowledge graph as agent context" move from a non-graph vendor, confirming the direction ACI is already on. Two direct takeaways: (1) the pattern of linking entity → infrastructure/service → responsible party → affected stakeholder is directly reusable in ACI's corporate-intelligence entity graph (company → asset → person → incident); (2) it reinforces ACI's Graph DB choice over ad-hoc join tables for mission evidence correlation — multi-hop "what does this failure touch" queries are precisely where graphs beat SQL.

## Sources (with dates)
- Press release coverage, 2026-10-20: https://lifestyle.duovoltart.com/story/927477/grafana-labs-extends-knowledge-graph-from-infrastructure-to-the-user-giving-people-and-agents-one-connected-view-at-observabilitycon-2026/
- Grafana Labs 2026 State of Observability Report (released same week).

## Action
watch
