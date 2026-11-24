---
title: AMUN Corporate Intelligence
emoji: 🦅
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# AMUN Corporate Intelligence (ACI)

Corporate intelligence & OSINT multi-agent platform.

- **Live console:** open `/console` in the running Space
- **API:** `POST /api/v1/run` with `{"mission":"corporate","target":"example.com"}`
- **Health:** `GET /healthz`

Storage: PostgreSQL when available, otherwise a local SQLite file (missions, memory, RAG, graph).
