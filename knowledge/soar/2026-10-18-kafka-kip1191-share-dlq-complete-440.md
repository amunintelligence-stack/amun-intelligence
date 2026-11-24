# Kafka KIP-1191 (share-group DLQ) now listed complete for 4.4.0 — still unreleased

**Date found:** 2026-10-18 (nightly dev researcher)
**Action:** WATCH — update the event_bus registry note (KIP-1191 complete-for-4.4.0, GA pending). Shapes future bus selection; no action on the current synchronous-dispatch architecture.

## What changed
Early-October 2026 write-ups on Kafka share-group semantics (KIP-932) confirm the DLQ story has moved: KIP-1191 (share-group dead-letter topics) is now listed as complete for Kafka **4.4.0**, which is not released yet (only RCs; 4.4.0 RC4 confirmed inflight). In 4.3, share groups still redeliver poison messages ~5x (share.delivery.count.limit) then archive with no DLQ copy. Client-side caveat reconfirmed: franz-go has full KIP-932 support since v1.21.0, but confluent-kafka's ShareConsumer remains marked Preview/not-for-production — so Python consumers of Kafka queues are explicitly not production-ready yet.

## Why it matters for ACI
ACI's planned event bus (postgres-backed queue short-term, NATS JetStream 2.15 candidate) is documented in the registry; this refines the design notes: Kafka share groups won't solve the poison-message/DLQ problem out of the box until 4.4.0 GA, and our Python backend couldn't use share consumers in production anyway. Reinforces keeping the poison-handling-coded-in-design rule regardless of bus.

## Sources
- "Kafka Just Learned to Be a Queue. Postgres Has Been One All Along." — https://dev.to/firfircelik/kafka-just-learned-to-be-a-queue-postgres-has-been-one-all-along-2i9g — 2026-10-05
- "Queue or Log? Kafka, RabbitMQ and NATS All Do Both Now" — https://devops-daily.com/posts/queue-or-log-kafka-rabbitmq-nats — 2026-10-09
