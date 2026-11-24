# Influencer-marketing MCP servers (2026) — creator data as agent tools

**Date:** 2026-10-16 (comparison published ~Sep 2026, verified current Oct 2026)
**Source:** https://influencers.club/blog/the-best-influencer-marketing-mcps-in-2026/ (secondary — vendor comparison; profile/tool counts are each vendor's own published claims as of Sep 2026)

## What changed
Creator-data platforms are now shipping MCP servers that let agents do discovery, audience analytics, and outreach directly:
- **Influencers.club**: 340M+ profiles, 47 platforms, 19 tools, audience data built on engagers rather than followers. Free server + credits, self-serve.
- **HypeAuditor**: 220M+ profiles, 3 platforms, 6 tools + 12 workflows, audience data. Free during beta, self-serve. Strength: fraud detection.
- **Upfluence**: 14M+ profiles, 3 platforms, 8 tools. Beta, on request (not self-serve). Strength: agent that sends outreach.
- **Favikon**: 10M+ profiles, 9 platforms, 43 tools. Requires a Favikon plan. Strength: B2B + LinkedIn creators.
- **Influship**: 14 tools, API credits, self-serve. Strength: campaign-fit scoring.
- **Kolsquare**: read-only, 5 platforms, audience data; clients with API access only. Strength: campaign reporting in chat.
- **CreatorDB**: 30M+ profiles, 3 platforms, credit plans, self-serve. Strength: brand + sponsor intelligence.
- **Hypefy**: 1M+ curated profiles, waitlist. Strength: brief-to-shortlist without subscription.
- Separately, **Meltwater** (30M creator profiles, fake-follower/engagement-authenticity checks, brand-safety vetting) is searchable by prompt via the **Meltwater MCP**, which also reaches Meltwater social-listening data — an agent can find creators already talking about a category and vet what others say about them.

## Why it matters for ACI
Social-intel missions (creator vetting, brand-safety, audience authenticity) currently rely on web/API connectors. MCP servers collapse that integration: HypeAuditor's fraud-detection workflows and Meltwater's listening-backed vetting are directly usable as agent tools. The vetting lesson from the comparison: audience data quality varies (followers vs. engagers), and no single score should decide approval — ACI should keep its multi-indicator rule (fit + content response + growth consistency + authenticity) and treat MCP-served scores as evidence, not verdicts. HypeAuditor's free-during-beta MCP is the cheapest evaluation path.

## Action
**Watch.** Evaluate HypeAuditor MCP (free beta) and Influencers.club MCP (free server + credits) as social-intel connectors when the next social-mission template is built. Do not auto-approve creators on any single MCP-served score.
