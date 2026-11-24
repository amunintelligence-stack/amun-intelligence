# Nmap 7.992 (2026-10-15) — security-hardening release

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — pin 7.992+ as minimum whenever nmap is re-provisioned; keep the NotCVE-2026-0011 packet.lua watch open.

## What changed
Nmap 7.992 shipped 2026-10-15, dominated by security fixes reported by SentinelOne's Karan Bamal: NSE flaws including a hardcoded DH exponent in afp.lua decryptable from traffic, unverified redirects in anyconnect.lua/upnp.lua, unbounded memory in rpc.lua/drda.lua/eigrp.lua/msrpctypes.lua/db2-das-info/dns-zone-transfer, CPU infinite loops in rdp.lua/tn3270.lua/ospf.lua, and a coroutine loop in tftp.lua; plus Horizon3.ai's Zach Hanley findings — two use-after-frees in the massdns parallel DNS resolver, and the NSE default Lua PRNG seed leaking the process ASLR base. NSE now ships execution time and memory limits (threads killed after 5s without yielding; allocations over 400MB throw), plus a new libfuzzer framework for internal functions. Also 8 new DICOM audit scripts (620 total) and Npcap 1.89. The changelog shows no fix yet for the NotCVE-2026-0011 (packet.lua) item on our registry watch list.

## Why it matters for ACI
Our nmap registry entry is status "missing" (apt binary wiped 2026-10-08, replaced by wipe-proof portscan.py), so nothing live needs patching. But this confirms the "hostile scan target attacks the scanner" threat pattern in an official security release — directly relevant to an intel stack that scans untrusted hosts. When nmap is ever re-provisioned, 7.992 is the minimum acceptable version, and the new 5s/400MB NSE guardrails are the right default shape for any NSE invocation ACI wraps. Note: Debian sid was still on 7.991+dfsg-1 (2026-10-04), so 7.992 needs a source install.

## Sources
- Nmap Change Log — http://nmap.org/changelog.html — 2026-10-15
- "How to Use Nmap for Network Scanning: 12 Steps [2026]" — https://tech-insider.org/how-to-use-nmap-network-scanning-2026/ — 2026-10-17
