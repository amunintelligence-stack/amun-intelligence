# NVIDIA App MCP server — local agent control, ON BY DEFAULT (security watch)

**Date:** 2026-10-16 (NVIDIA App update 11.0.9.565, reported 2026-10-16)
**Source:** https://en.gamegpu.com/news/zhelezo/v-obnovlenie-nvidia-app-dobavili-lokalnyj-server-mcp-dlya-upravleniya-cherez-ii (secondary — hardware press; verify against NVIDIA's own release notes)

## What changed
NVIDIA App update 11.0.9.565 adds a **local HTTP server based on MCP** that connects the graphics ecosystem to external AI assistants/LLMs. Per the report, the feature is **activated by default immediately after installation**. Control lives in Settings → Features → "Communication with AI agents and applications".
The server exposes broad control: query system status, media-capture state, filter/overlay operation, game launches (IDs, windowed mode); commands include ShadowPlay recording control, instant replays, screenshots, RTX Dynamic Vibrance filter, frame counter, launching installed applications; driver/config access includes reading installed/available software versions and changelogs, applying automatic optimal settings profiles, resetting to defaults; on laptops, read/edit power profiles (Battery Boost, Whisper Mode).

## Why it matters for ACI
This is a textbook MCP attack-surface case study, directly relevant to ACI's MCP security posture: a **default-on** local MCP server with **system-control tools** (launch apps, record screen, change settings) and no apparent per-tool approval story in the report. It is the same threat shape as the MCP prompt-injection / confused-deputy issues tracked in this folder — only now shipped to millions of consumer desktops by a hardware vendor. ACI's own MCP posture should be the opposite: default-off, explicit per-tool allow-list, human approval for any state-changing tool.

## Action
**Watch / advisory.** Not our stack (no NVIDIA App in ACI). Record as a reference case for MCP threat modeling: default-on + broad tools + local HTTP = the pattern to never ship. If any ACI host runs NVIDIA App, disable the MCP feature in Settings.
