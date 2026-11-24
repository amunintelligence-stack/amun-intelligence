# OpenAI تطلق MCP Events — قدرة دفع حدثية على MCP 2.0 (مواصفة 2026-07-28)

- التاريخ: 2026-10-08 | الفئة: mcp | الإجراء: **مراقبة (watch)**

## ما الذي تغيّر
قدّمت OpenAI "MCP Events": تعلن الخوادم قدرة `events` عبر `server/discover`، وتنفّذ `events/list` و`events/subscribe` و`events/unsubscribe`، وتدفع webhooks موقعة (Standard Webhooks HMAC، سقف حمولة 256 KiB، إعادة محاولة بتراجع أسي، إعادة تشغيل بالـ cursor) إلى URL رد — مثل `comment.created` على مستند أو `message.created` على قناة Slack لتدفع ChatGPT للتصرف. يتطلب MCP 2.0 (إصدار البروتوكول `2026-07-28`، ما زال أحدث مواصفة أساسية مستقرة حتى أواخر سبتمبر 2026 حسب خارطة TS SDK). التوفر حاليًا محدود بدردشات ChatGPT Work (وضع Cloud على الويب/سطح المكتب) وdots؛ والـ polling/streaming وعناصر التحكم `gap`/`terminated` في المسودة غير مدعومة بعد.

## لماذا يهم ACI
يوحّد هذا بالضبط مشكلة الدفع-مقابل-السحب التي تواجهها طبقة حافلة الأحداث وSOAR/n8n في ACI: التحفيز الحدثي للمهام (ملفات جديدة، إشارات علامة جديدة، إصابات CVE جديدة) يصبح نمط بروتوكول من الدرجة الأولى بدل الـ cron polling. راقب دعم Python MCP SDK لامتداد الأحداث.

## المصادر
- https://developers.openai.com/plugins/build/mcp-events — وثائق أكتوبر 2026 (جُلبت 2026-10-08)
- https://ai-engineering-trend.medium.com/mcp-events-openai-adds-new-event-driven-capabilities-to-the-model-context-protocol-c7aab747bc1c — أكتوبر 2026

## الإجراء المقترح
**مراقبة** — امتداد في مرحلة المسودة بدعم مضيف ضيق؛ تتبّع التنفيذ على جانب SDK قبل اعتماده في حافلة أحداث ACI.
