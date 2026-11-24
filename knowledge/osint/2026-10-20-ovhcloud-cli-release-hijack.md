# OVHcloud CLI — GitHub release binaries hijacked (Oct 19, 2026)

## What changed
On 2026-10-19, an attacker using the hijacked GitHub account of a legitimate OVHcloud contributor (HassenBF) replaced the prebuilt binaries on five already-published releases of the OVHcloud CLI — v0.11.0, v0.12.0, v0.13.0, v0.14.0 and v0.15.0 — via the GitHub Releases API. Source code and tags were untouched; only the release assets (and the published `checksums.txt`) were swapped with a secrets-stealing build. The malicious files were live for ~94 minutes (12:47–14:21 UTC). A customer caught it by pinning SHA-256 hashes in CI; OVHcloud deleted the swapped files, and published a clean, immutable, attested v0.16.0 the same evening. OpenSourceMalware links the incident to the GlassWorm campaign and notes the contributor account had been compromised for ~7 months.

## Why it matters for ACI
ACI installs ~20 recon/OSINT tools as prebuilt binaries from GitHub Releases. This incident is the exact failure mode of that install path: the source repo was clean, CI/CD was unaffected, and the published checksums were attacker-controlled — only a pre-pinned hash caught it. It validates (and hardens) our tooling policy.

## Sources (with dates)
- WindowsForum report, published 2026-10-20: https://windowsforum.com/news/ovhcloud-cli-github-release-hijack-rotate-secrets-and-upgrade-to-v0-16-0.449215/
- tsecurity.de release tracking, 2026-10-19/20 (GlassWorm/ForceMemo linkage noted in the OpenSourceMalware report it cites)
- CEO Octave Klaba's public update (2026-10-19): versions v0.11.0–v0.15.0 affected, v0.16.0 clean with release attestation

## Action
watch
