# OpenAI Agents SDK (TypeScript) — 0.4.0 و Guardrails 0.3.0 (كسر التوافق)
- التاريخ: 2026-10-10 | الفئة: multi-agent | الإجراء: **مراقبة**

## ما الذي تغيّر
- **@openai/agents-core 0.4.0** (نهاية سبتمبر 2026): **إسقاط دعم Zod v3** — يتطلب الآن Zod v4 لأدوات الـ schema والمخرجات المهيكلة (breaking change).
- تحديث افتراضيات gpt-5.1/gpt-5.2 و reasoning effort types.
- إضافات عملية: per-run tracing API key، tool input/output guardrails في TS SDK، compaction mode افتراضي "auto"، معالجة لطيفة لـ invalid JSON في tool call arguments (#723)، إنهاء آمن لـ streamable HTTP MCP sessions.
- **@openai/guardrails 0.3.0** (سبتمبر 2026): breaking — يتطلب Node 22.13+/24 (إسقاط 18/20)، Zod 4، OpenAI 7، Agents SDK 0.17.

## لماذا يهم ACI
- backend الـ ACI بايثون ولا يستخدم هذه الـ SDKs، لكن الـ pattern مهم: الـ ecosystem كله يتحرك نحو Zod v4 + guardrails مدمجة في الـ SDK — أي integration مستقبلي مع أدوات JS (public tool page, n8n nodes) يجب أن يستهدف هذه النسخ.
- الـ `agents-openai` Python SDK على PyPI وصل 0.22.3 (17 سبتمبر 2026) — البايثون أقل تقلبًا من TS line حاليًا.

## المصادر
- https://github.com/openai/openai-agents-js/blob/HEAD/packages/agents-core/CHANGELOG.md — تم الوصول 2026-10-10
- https://github.com/openai/openai-guardrails-js/commit/09ebad8d4d2115894b41e11b62ebd71c041c9f87 — سبتمبر 2026
- https://pypi.org/project/openai-agents/0.22.3/ — 2026-09-17

## الإجراء المقترح
**مراقبة** — لا اعتماد مباشر؛ لكن عند أي عمل JS جديد اعتمد Zod v4 من البداية ولا تقم بـ pin قديم.
