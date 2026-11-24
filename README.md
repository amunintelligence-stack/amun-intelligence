# AMUN Corporate Intelligence (ACI) — Backend

**AMUN Corporate Intelligence** — OSINT / corporate-intelligence platform backend. Serves the frontend, runs OSINT collection missions, and stores results.

Founded by **[Mohamed Nagy](https://github.com/SeniorMohamed)** — Founder, Designer & Principal Developer.

## What it does

- FastAPI backend (`app.py`) + web console (`/console`)
- OSINT collection missions: DNS, whois, crt.sh (certificate transparency) — no external API keys required
- Endpoints: `POST /api/v1/run`, missions, memory, RAG, graph (`/api/v1/...`)
- Results stored in PostgreSQL when available, else a SQLite file, else in memory

## Run it

```sh
pip install -r requirements.txt
uvicorn app:app --port 8000
```

Or deploy with Docker / Render (`Dockerfile`, `render.yaml`).

## Live

- Frontend: https://amun-intelligence.netlify.app/
