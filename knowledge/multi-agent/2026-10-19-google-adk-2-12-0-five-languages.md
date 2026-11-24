# Google ADK 2.12.0 (13 Oct 2026) + "One ADK, five languages": MCP + A2A as the interop fabric

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — the ADK + MCP + A2A interop story validates our protocol choices; re-evaluate only if ACI ever needs JVM/on-device agents.

## What changed
- **google-adk 2.12.0** released 2026-10-13 (pepy/PyPI; registry last tracked 2.11.0). Downloads running ~10.1M/month on PyPI.
- Same day, Google published **"One Agent Development Kit, five languages"** (cloud.google.com blog, 2026-10-13): ADK now ships natively in **Python, Go, TypeScript, Java, and Kotlin**. The explicit pitch: *"every version of ADK speaks MCP and A2A, each component of your system can use the language that fits it best."* Interoperability is via the two open protocols, not a shared runtime.
- Kotlin flavor details (build-time safety angle): KSP compiler plugin reads `@Tool`/`@Param` annotations at build time and emits tool schemas into bytecode — unsupported types fail the Gradle build, not the agent run; zero runtime reflection so it survives Android R8 shrinking. On-device: integrates LiteRT-LM for tool calling and ML Kit (Gemini Nano), Room/AppSearch for local state, Android AppFunctions for OS-level actions — all without network.
- Java flavor: Maven Dev UI plugin plus first-party bridges for Spring AI and LangChain4j.
- Companion ecosystem datapoint (secondary, altatools comparison, ~Oct 2026): ADK 2.x ships SequentialAgent / ParallelAgent / LoopAgent workflow agents, `adk optimize` (GEPA instruction optimizer for root instructions), OpenTelemetry-first observability, and native A2A support via Agent Cards.

## Why it matters for ACI
- Google's five-language ADK converging on **MCP + A2A as the universal interop layer** is strong vendor validation of ACI's own protocol strategy: our agents expose tools via MCP, and agent-to-agent delegation should ride A2A Agent Cards — exactly the two protocols the whole ADK family now assumes. This is the direction of travel; ACI is already aligned.
- The Kotlin KSP build-time tool-schema compilation is a pattern worth noting for our evaluator-optimizer ambitions: schema errors caught at build/registration time rather than at tool-call time. Our tools.yaml registry + typed tool wrappers are the Python-side equivalent; the lesson is to lint tool schemas in CI, not at mission runtime.
- The `adk optimize` GEPA-based instruction optimizer is a concrete implementation of the Sakana-MASS-style "optimizer matters more than evaluator" result from yesterday's finding — watch for its methodology write-up as an evaluator-optimizer reference.
- No adoption: ACI stays Python + provider-neutral. Only revisit if an ACI component ever needs to run on JVM or on-device (not on the roadmap).

## Sources
- "google-adk · 126.4M downloads on PyPI — latest version 2.12.0, released Oct 13, 2026" — https://pepy.tech/projects/google-adk?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=1.17.0%2C1.16.0%2C1.15.1 — 2026-10-13
- "One Agent Development Kit, five languages" — https://cloud.google.com/blog/topics/developers-practitioners/one-agent-development-kit-five-languages — 2026-10-13
- "Google ADK Vs LangGraph: Which To Use In 2026?" — https://altaitools.com/google-adk-vs-langgraph/ — 2026-10 (secondary; treated as background, not primary)
