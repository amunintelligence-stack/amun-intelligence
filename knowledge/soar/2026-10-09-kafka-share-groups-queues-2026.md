# Kafka 4.x — مجموعات المشاركة (share groups) تجلب دلالات الطوابير إلى Kafka

- التاريخ: 2026-10-09 | الفئة: soar | الإجراء: **مراقبة (watch)**

## ما الذي تغيّر
منذ Kafka 4.2 (مارس 2026؛ التغطية التحليلية جديدة في أكتوبر 2026): share groups عبر KIP-932 تسمح لعدة مستهلكين بالقراءة من نفس الـpartition مع إقرار لكل سجل (accept/release/reject)، كاسرةً قاعدة "عدد الـpartitions يحد التوازي". KIP-1222 أضاف تجديد الإقرار للأعمال الطويلة ومقاييس التأخر. تحليل أكتوبر 2026 يؤكد: Kafka أصبح يقدم queue semantics حقيقية لمعالجة المهام.

## لماذا يهم ACI
لو احتجنا event bus لأوركسترا المهام، Kafka 4.x لم يعد محصورًا في نموذج الـlog — أصبح بديلًا شرعيًا لـRabbitMQ في سيناريوهات work queues. معلومة معمارية للمستقبل.

## المصادر
- https://devrimozcay.medium.com/kafka-vs-rabbitmq-in-2026-kafka-now-has-queues-here-is-what-changed-and-what-did-not-281e81a20b29 — أكتوبر 2026
- https://www.systemdesign.academy/compare/kafka-vs-rabbitmq

## الإجراء المقترح
**مراقبة** — مرجع معماري عند الحاجة لاحقًا.
