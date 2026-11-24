# Queue-or-log is now two decisions, not a broker choice — Kafka 4.3.1 / RabbitMQ 4.3.6 / NATS 2.15.0 failure-mode comparison

**Date researched:** 2026-10-14
**Status:** Watch — design guidance for ACI's future event bus; no broker to adopt tonight.

## What changed
- A hands-on comparison (devops-daily, ~9–10 Oct 2026) ran the same four failure cases — replay after a bad deploy, one poison message, more consumers than partitions, event order after a retry — against six setups on Kafka 4.3.1, RabbitMQ 4.3.6, and NATS 2.15.0 (single nodes, behavior not throughput). Core result: "queue vs log" decomposes into **two independent decisions**: (1) **Storage** — does it keep messages after handling? (2) **Consumption** — per-message acks, or a single offset?
  - Kafka 4.2 (Feb 2026) made **share groups** production-ready: queue-style per-record ack/release/reject on a Kafka topic. Kafka 4.3: `share.version` finalized at level 1 on new clusters. RabbitMQ streams (since 3.9) are append-only logs; NATS JetStream lets each stream choose delete-on-ack vs keep-until-limit.
- **Surprises:**
  - **RabbitMQ 4.3 quorum-queue regression (documented behavior change):** since 4.3 the delivery limit is checked against `delivery-count`, which increments only on *failed* deliveries — `basic.nack(requeue=True)` no longer counts. A poison message with `x-delivery-limit=5` + DLQ was retried 6,064 times in 45 s and never dead-lettered; `basic.reject(requeue=True)` dead-lettered after 6 attempts. On 4.2.9 both calls dead-lettered after 6. (Cross-ref: ACI note `2026-10-12-rabbitmq-4-3-quorum-queue-retry-behavior.md` covered the retry behavior; this file adds the cross-broker comparison and the 4.2-vs-4.3 test table.)
  - **Kafka share-group batching:** six consumers on a 3-partition topic got work on only 3 members — `batch_optimized` acquire mode hands out whole producer batches and `max.poll.records` is only a soft cap. With one record per producer batch + `max.poll.records=1`, all 6 members split work evenly (1.3 s vs 6.0 s). Strict-cap mode `record_limit` (KIP-1206) exists but wasn't testable with the client used.
  - **Order:** offset readers kept per-key order 5/5 runs; per-message-ack setups lost order whenever a consumer held several messages at once — the share group lost it even with `max.poll.records=1`.
  - **Poison handling:** share group and both NATS setups gave up after 5 deliveries and handled the other 99; offset readers blocked behind the poison message (10/100 handled). Kafka's accepted **KIP-1191** adds a dead-letter topic for share groups — accepted, **not in 4.3**.
- **Replay rule:** replay followed storage, not consumption — share groups and NATS limits streams replayed all 1,000 messages; quorum queues and work-queue streams replayed 0. Share-group offset reset refuses while the group has active members.

## Why it matters for ACI
- ACI has no event bus yet (missions run as direct FastAPI/n8n calls); when one is added for fan-out recon/enrichment, this comparison is the selection framework. The ACI-relevant takeaways: (1) choose storage-that-keeps-messages + per-message ack (Kafka share group or NATS limits stream) so a buggy consumer's output can be replayed after a fix; (2) per-message ack trades away ordering — keep ordering-sensitive mission steps on offset readers or single-in-flight consumers; (3) if RabbitMQ is ever used, audit every consumer for `basic.nack(requeue=True)` — on 4.3+ it silently disables poison-message dead-lettering, and queue depth won't reveal the loop (only redelivery rate will).
- KIP-1191 (share-group DLQ) is the missing piece for a Kafka-based ACI bus; until it ships, dead-lettering on share groups is application code.

## Action
**WATCH:** no broker purchase/adoption. When ACI adds a queue: default to Kafka share groups or NATS JetStream limits streams (keep-messages + per-message ack) for fan-out work; keep a separate offset-based path for order-sensitive steps; set explicit poison-message budgets (max-deliver / delivery-count) and alert on redelivery rate, not just queue depth.

## Sources
- "Queue or Log? Kafka, RabbitMQ and NATS All Do Both Now" (devops-daily, ~9–10 Oct 2026): https://devops-daily.com/posts/queue-or-log-kafka-rabbitmq-nats
- Same article mirrored on DEV (9 Oct 2026): https://dev.to/devopsdaily/queue-or-log-kafka-rabbitmq-and-nats-all-do-both-now-1mmp
- NATS 2.15 AI-chat-backend write-up (7 Oct 2026, JetStream feature context): https://dev.to/thedonmon/beyond-kafka-and-redis-part-2-an-ai-chat-backend-on-nats-215-461c
- Prior ACI notes: `2026-10-13-kafka-kip-1191-share-group-dlq.md`, `2026-10-12-rabbitmq-4-3-quorum-queue-retry-behavior.md`, `2026-10-12-kafka-4-2-2-bugfix-4-4-0-rc4.md`
