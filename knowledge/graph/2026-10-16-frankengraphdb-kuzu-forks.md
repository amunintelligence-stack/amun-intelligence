# FrankenGraphDB + the post-Kùzu graph landscape

**Date:** 2026-10-16 (repo activity ~2026-10-11)
**Source:** https://github.com/dicklesworthstone/frankengraphdb (primary — repo README/spec)

## What changed
- **frankengraphdb** is a new blank-slate property-graph database in Rust: unified MVCC / time-travel / branches / replication over a fountain-coded commit stream, WCO + factorized execution, incremental everything, deterministic auditable results. Three postures: embedded library (`fgdb`), server (`fgdbd`), CLI (`fgdb`), speaking **GQL (ISO/IEC 39075:2024)** with an openCypher on-ramp. Status: spec-stage — the repo currently describes the system it builds; treat as early-stage, not shippable.
- The README states the context: **Kùzu was acquired by Apple (agreed Oct 2025, disclosed Feb 2026 via Apple's EU DMA filing)** and the upstream repo was archived read-only; community forks (e.g. LadybugDB, already tracked) carry the architecture forward.

## Why it matters for ACI
ACI's graph layer is networkx + Postgres snapshots today, with FalkorDB/LadybugDB/AGE as upgrade candidates. Two takeaways: (1) the Kùzu archival confirms the fork-first reality — any Kùzu-derived dependency must be pinned to a maintained fork (LadybugDB), never upstream; (2) frankengraphdb's design goals — time-travel, branches, deterministic auditable results — map directly onto ACI's evidence needs (a mission graph that can be rewound to the state behind a verdict is an audit win). GQL as the query language is also worth noting: if ACI ever adds a real graph engine, GQL (ISO standard) is a safer long-term bet than a vendor dialect.

## Action
**Watch.** No adoption — spec-stage. Add Kùzu-archived to the engine-selection notes so nobody proposes upstream Kùzu again.
