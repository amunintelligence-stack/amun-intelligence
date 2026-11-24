# OpenAI Agents SDK (TypeScript) 0.20.0
## ماذا تغيّر
- وصل `@openai/agents` إلى 0.20.0 في 2026-10-08 (وتيرة إصدار أسبوعية؛ آخر ما غطيناه كان 0.4.0).
- أبرز ما تراكم في آخر ~30 يومًا (من ملاحظات الإصدارات الرسمية): تفاوض MCP v2 مع دعم خوادم v1 القديمة (0.15.0)، أدوات اختبار حتمية (`ScriptedModel` و`scriptedSandboxSession` — اختبار الوكلاء دون نماذج حية)، إعدادات sandbox أكثر أمانًا (اعتمادات التحميل داخل الحاوية تفشل مغلقة افتراضيًا)، دعم Programmatic Tool Calling، وتعطيل تسجيل البيانات الحساسة افتراضيًا (0.14.0).
- النموذج الافتراضي الجديد للوكلاء دون نموذج محدد أصبح `gpt-5.6-luna` بجهد استدلال `none`.
## لماذا يهم ACI
- دعم MCP v2 الأصلي يعني أن أي عميل TS نبنيه مستقبلًا يتفاوض بروتوكول 2026-07-28 تلقائيًا — متوافق مع خوادم MCP التي سنبنيها.
- فلسفة «الأمان الافتراضي» (تعطيل التسجيل الحساس، الفشل المغلق للاعتمادات) تستحق الاقتباس في إعدادات وكلائنا.
## المصادر
- GitHub releases — openai/openai-agents-js v0.15.0 (2026-08): https://github.com/openai/openai-agents-js/releases/tag/v0.15.0
- GitHub releases — openai/openai-agents-js v0.16.0: https://github.com/openai/openai-agents-js/releases/tag/v0.16.0
- GitHub releases — openai/openai-agents-js v0.17.0: https://github.com/openai/openai-agents-js/releases/tag/v0.17.0
## الإجراء
**watch** — راقب استقرار 0.20.x؛ اقتبس أنماط الأمان الافتراضي في وكلائنا.
