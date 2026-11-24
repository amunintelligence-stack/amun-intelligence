# OpenAI Agents SDK 0.24.0: MCP annotations on converted tools

## What changed
OpenAI released `openai-agents` (Python) v0.24.0 on 2026-10-15, per the official GitHub release notes. Two changes: (1) MCP annotations are now exposed on tools converted from MCP servers, and (2) run-wide tool exception formatting is supported. The SDK is still pre-1.0 despite ~14.7M monthly PyPI downloads (March 2026 figure) and ~30k GitHub stars.

## Why it matters for ACI
MCP annotations on converted tools let ACI's orchestrator read the richer metadata MCP servers ship (e.g. title, behavior hints) instead of bare schemas — directly relevant to the tool-registry layer, where annotation fidelity decides whether the agent picks the right recon tool. Run-wide tool exception formatting gives ACI cleaner, uniform error traces from tool failures across a mission, which feeds both the RAG-evidence log and the evaluator. Caveat stands: pre-1.0 means pinning versions, not floating.

## Sources (with dates)
- github.com/openai/openai-agents-python — release v0.24.0 (2026-10-15)
- geekflare.com — "Best Open Source AI Agent Frameworks in 2026" (updated 2026-10-19): independently confirms v0.24.0 as latest, notes default OpenAI-side tracing and no built-in crash recovery

## Action
watch
