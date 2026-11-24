#!/bin/bash
# ACI backend starter (uses venv). Ensures PostgreSQL is up first.
# NOTE: apt-installed packages are ephemeral on this VM (system area was wiped
# 2026-10-08). If postgres is missing we start DEGRADED but say so loudly.
LOGDIR=/home/hatch/workspace/aci/logs
mkdir -p "$LOGDIR"
if command -v pg_ctlcluster >/dev/null 2>&1; then
  pg_ctlcluster 16 main status >/dev/null 2>&1 || pg_ctlcluster 16 main start >>"$LOGDIR/postgres-start.log" 2>&1
else
  echo "$(date -Iseconds) WARN: pg_ctlcluster not found — PostgreSQL not installed; starting backend WITHOUT database (degraded, db:false)" >>"$LOGDIR/backend-warnings.log"
fi
cd /home/hatch/workspace/aci
# Detach with nohup (like n8n's start.sh) so the backend survives the end of
# the watchdog's exec session: a foreground `exec uvicorn` dies minutes after
# every watchdog restart when the scheduler tears the session's process tree down.
# Logs go to uvicorn.log so crashes leave evidence (this log stayed empty before).
nohup ./venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000 --workers 1 --log-level info >>"$LOGDIR/uvicorn.log" 2>&1 &
echo "$(date -Iseconds) INFO: uvicorn detached as PID $! (log: $LOGDIR/uvicorn.log)" >>"$LOGDIR/uvicorn.log"
