# Microsoft Agent Framework: إصدار Python 1.20.0 و.NET 1.24.0 (أكتوبر 2026)

- التاريخ: 2026-10-11 | الفئة: multi-agent | الإجراء: **مراقبة**

## ما الذي تغيّر
- **Python 1.20.0**: commit تحضير الإصدار في 2 أكتوبر 2026 (microsoft/agent-framework#8968) — تحديث الحزم، دعم Python 3.14/3.15 على Windows، وتحديث الحزم الداخلية.
- **.NET 1.23.x → 1.24.0** (7 أكتوبر 2026، عبر agent-framework-toolkit): دعم Decisions API من OpenAI (تجريبي)، طرق `AsAIAgent` لكل العملاء (OpenAI/Azure/Foundry/Anthropic/Bedrock/Google/Mistral)، ثوابت نماذج جديدة (GPT-6.1 Sol، Claude Sonnet 5.5)، وطبقة UltraFast.
- ملاحظة تصحيحية: مقال az365.ai (9 أكتوبر) يحتفي بـ «Declarative Workflows 1.0» (تنسيق YAML للتنسيق خارج الكود)، لكن الإصدار 1.0 الفعلي صدر في **أغسطس 2026** — المقال تعليق تحليلي جديد لا إصدارًا جديدًا.

## لماذا يهم ACI
الإطار هو خليفة AutoGen الرسمي (وضع الصيانة مؤكد) والمرشح الرئيسي لأي ترحيل مستقبلي لمعمارية ACI متعددة الوكلاء. فكرة «التنسيق كملف YAML مُصدَر» (Declarative Workflows) تناسب مهام الاستخبارات المتكررة: تعريف المهمة كأصل مُصدَر يُراجَع ويُنسَخ بدل كود مُجمَّع.

## المصادر
- https://github.com/microsoft/agent-framework/commit/6967986f8e4a753c1656743e49b4f955570d724c — تحضير 1.20.0، 2 أكتوبر 2026
- https://github.com/rwjdk/agent-framework-toolkit/blob/HEAD/CHANGELOG.md — 1.24.0، 7 أكتوبر 2026
- https://az365.ai/blog/microsoft-agent-framework-declarative-workflows/ — 9 أكتوبر 2026 (تحليل، لا إصدار)

## الإجراء المقترح
**مراقبة** — يبقى المرشح الأول لأي ترحيل خارج AutoGen؛ لا بناء عليه الآن.
