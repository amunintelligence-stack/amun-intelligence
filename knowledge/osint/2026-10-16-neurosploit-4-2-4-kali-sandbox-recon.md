# NeuroSploit v4.2.4 — Kali sandbox recon orchestration

**Date:** 2026-10-16 (release ~2026-10-04, per GitHub release page)
**Source:** https://github.com/JoasASantos/NeuroSploit/releases/tag/v4.2.4 (primary)

## What changed
NeuroSploit v4.2.4 adds full Kali sandbox orchestration for recon. With `--sandbox` (black-box mode) it:
- starts the container engine if installed but not running (colima / Docker Desktop / dockerd / podman machine),
- spins up a Kali container and provisions the recon toolbox on demand (subfinder, httpx, katana, gau, waybackurls, nuclei, naabu, dnsx, assetfinder, gf, qsreplace, anew — via `go install` + apt),
- runs a deterministic TOOL-RECON pass in Kali: subdomain enumeration (crt.sh + subfinder/amass), live-host filtering, URL harvest (gau/waybackurls/katana), targeted nuclei quick-wins, gf-flagged candidate URLs by vuln class,
- feeds all tool output into LLM recon/exploitation, which works ON TOP of tool output and confirms each finding with its own request,
- tears the container down at the end (keep with `NEUROSPLOIT_KEEP_SANDBOX=1`).

Carries forward everything from v4.2.3 (full recon arsenal, subdomain fan-out, multi-model preflight, reproducible-finding validation, broad OWASP/ASVS objective). 423 tests, 480 agents claimed.

## Why it matters for ACI
This is the closest public precedent to ACI's own "deterministic tools first, LLM on top" architecture: tool output is the evidence layer, the model only interprets and confirms. The sandbox-per-run pattern (provision → run → tear down) is exactly how ACI should isolate active recon if it ever runs active probes — it bounds blast radius and keeps the host clean. The deterministic TOOL-RECON pass (enumerate → filter live → harvest URLs → nuclei quick-wins → gf-flagged candidates) is a reusable pipeline shape for ACI mission templates.

## Action
**Watch.** Do not adopt the tool itself (it is an offensive exploitation orchestrator; ACI is defensive intel). Borrow two patterns: (1) sandbox-per-run provisioning/teardown for any future active recon, (2) the deterministic recon-pass ordering as a mission-template reference.
