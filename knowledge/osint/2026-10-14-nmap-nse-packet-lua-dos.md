# Nmap NSE packet.lua DoS — hostile scan target can OOM the scanner (NotCVE-2026-0011)

**Date researched:** 2026-10-14
**Status:** Watch — fix exists in dev tree; no released version verified to carry it (as of the 19 Aug 2026 advisory).

## What changed
- A public advisory (NotCVE-2026-0011, Full Disclosure, 19 Aug 2026) documents an infinite-loop / unbounded-allocation bug in Nmap's NSE packet-dissection library `nselib/packet.lua`, function `Packet:parse_options()`. A scanned host can reply with a packet carrying a zero-length TCP header option; the parser accepted a length byte of 0, never advanced its cursor, and allocated a new table on every loop pass — growing memory until the Nmap process died. CVSS 3.1: 6.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H). CWE-835 / CWE-400 / CWE-770. Discovered by Maxim Suhanov; tracked upstream as nmap/nmap issue #3368 / PR #3373.
- Affected: Nmap 7.99 and earlier. Fix: upstream commit `7ef4ee0` ("Stop parsing on a zero-length packet option", 11 Jun 2026) adds a `l == 0 → break` guard before any allocation.
- Nmap 7.991 shipped 5–6 Aug 2026 (latest in the release archive). **Caution:** the fix commit (11 Jun) predates the 7.991 release (5 Aug), but the 19 Aug advisory still states no released version carrying the fix had been verified. Treat 7.991 as *possibly* fixed but **unverified** until the shipped `packet.lua` is checked. A secondary aggregator (DailyCVE, 13 Aug 2026) also maps this to "CVE-2026-72712" — that CVE ID does **not** appear in the primary advisory; treat the mapping as unconfirmed.
- Exploitation requires running an NSE script that captures/parses raw packets against an attacker-controlled host. No RCE, no persistence; the effect ends with the process, but the attacker can repeat it on every scan, making the host effectively unscannable by affected scripts.

## Why it matters for ACI
- ACI's own scanner is a Python port scanner, not the nmap binary — so this is **not** a live vulnerability in the ACI backend. But nmap is in the ACI tool registry as the reference scanner alternative, and the failure mode generalizes: **any scanner that parses hostile responses can be DoS'd by a malicious target**. ACI missions routinely scan untrusted, potentially hostile infrastructure, so scanner-process hardening is directly in scope. The "attacker only needs to be scanned" inversion (scan target attacks the scanner) is the exact threat model for ACI recon runs.

## Action
**WATCH** (do not adopt a new nmap build on this alone):
1. Before any nmap use, verify the installed build's `nselib/packet.lua` contains the zero-length guard (or that the installed version is newer than the advisory's verified-fix state).
2. Regardless of version: run scans under a memory limit (e.g. systemd `MemoryMax` / container limits), isolate scanning from the main backend process, and treat scanner crashes on specific targets as a signal, not noise.
3. Apply the same discipline to ACI's Python scanner: bound all parser loops over untrusted bytes, cap allocation per response, and enforce per-scan memory/time limits.

## Sources
- NotCVE-2026-0011 advisory, Full Disclosure mailing list, 19 Aug 2026: https://seclists.org/fulldisclosure/2026/Aug/112
- Nmap release archive (7.991 files dated 5–6 Aug 2026): https://nmap.org/dist/?M=D
- Upstream fix commit 7ef4ee0 (11 Jun 2026), referenced in the advisory: https://github.com/nmap/nmap/commit/7ef4ee030a0023fe22616387a000032e1a678b6a
- Secondary CVE-ID mapping (unconfirmed), DailyCVE, 13 Aug 2026: https://dailycve.com/nmap-denial-of-service-cve-2026-72712-critical-dc-oct2026-3112/
