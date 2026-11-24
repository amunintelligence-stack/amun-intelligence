# RabbitMQ 4.4.0 — feature release: native delayed messages on quorum queues, Erlang 28/29, OIDC hardening

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — no adoption (ACI has no message bus yet). If a bus is ever chosen, 4.4.0's quorum-queue delayed messaging removes the need for the delayed-message-exchange plugin; note the OIDC breaking change for any future SSO wiring.

## What changed
- **RabbitMQ 4.4.0** is the current latest feature release (tag v4.4.0 on branch v4.4.x; Oct-9 nightly had 4.3.6 maintenance, Oct-12 covered 4.3 quorum retry behavior). Headline changes from the official release notes:
  - **Quorum queues now support delayed messages natively**: a message with `x-opt-delivery-time` (future epoch ms) is routed/enqueued immediately but delivered only when due — kills the classic TTL+DLX retry-loop pattern and, combined with 4.3's delayed retry, makes the Mnesia-based delayed-message-exchange plugin obsolete for new designs.
  - **Erlang 28/29 fully supported** for new clusters and rolling upgrades (recommendation: upgrade RabbitMQ to 4.3.7+ first if changing Erlang simultaneously).
  - **Breaking**: OpenID Connect discovery responses are now strictly validated (HTTPS endpoints, issuer must match discovery URL) — non-compliant IdPs (e.g. Cloud Foundry UAA) fail unless `auth_oauth2.discovery.verify_issuer`/`verify_https_endpoints` are disabled before upgrade.
  - Security bits: PBKDF2-HMAC-SHA256 password hashing option, password salts now from a CPRNG, encrypted values for `definitions.https.url`, web MQTT/STOMP strict-origin validation and HSTS config.
  - Operational: AMQP listeners can bind Unix domain sockets, `stream.max_connections`, classic queue shared-store v2 on-disk format (`.sqs` — **no downgrade** once present), delivery-limit policy now applies to existing quorum queues.

## Why it matters for ACI
- The 2026-10-14 queue-vs-log comparison shortlisted Kafka/RabbitMQ/NATS for a future ACI event bus. 4.4.0 strengthens the RabbitMQ option: native delayed messaging + quorum-queue reliability covers the scheduled-retry pattern a mission orchestrator needs without plugins; the v2 classic-queue format caveat (no downgrade) must be recorded in any future runbook.
- Not urgent: ACI currently has no broker; this is design-input only.

## Sources
- "Release RabbitMQ 4.4.0" (official release notes) — https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.4.0 — 2026-10-19 (checked; tag is current latest)
