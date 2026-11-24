# n8n 3.0 (مجدول أكتوبر 2026) يُسقط تثبيتات npm/npx — Docker يصبح إلزاميًا؛ عُقد قديمة تُزال ⚠️ حرج تخطيطيًا

- التاريخ: 2026-10-08 | الفئة: soar | الإجراء: **اعتماد (تخطيط) — adopt**

## ما الذي تغيّر
n8n 3.0، المجدول للإصدار في أكتوبر 2026، يُوصف في توثيق n8n (عبر تقارير طرف ثالث) كإصدار رئيسي مركز على الأمن/التنظيف بتغييرين breaking: (1) n8n ذاتي الاستضافة سيتطلب نشرًا قائمًا على Docker — تثبيتات npm/npx لن تُدعم؛ (2) عُقد قديمة تُزال: Function/Function Item ← Code node، وCron/Interval ← Schedule Trigger، وItem Lists تنقسم إلى Split Out/Aggregate/Sort/Limit، وRead PDF ← Extract from File، وWorkflow Trigger ← n8n Trigger، وعُقد OpenAI وOpenAI Assistant القديمة ← عقدة OpenAI الحالية، وتقاعد AI Agent node v1. مسار الترحيل المتوقع Docker Compose. تحقق إضافي من الباحث الليلي: مصادر ثانوية مستقلة متعددة تستشهد بتوثيق n8n نفسه، وPR في مستودع n8n-docs يتضمن سطر "DEPRECATED: npm installs (will be removed in v3.0)". تحفظ: لم يُجلب docs.n8n.io مباشرة — يُوصى بالتأكيد هناك قبل الالتزام بالترحيل.

## لماذا يهم ACI
n8n الخاص بـ ACI منشور عبر npm (`~/workspace/n8n/start.sh`، حاليًا v2.42.4) — بالضبط مسار النشر الذي ينهيه 3.0. الترقية بعد 3.0 دون ترحيل Docker ستكسر خط تشغيل المهام ("ACI — Intelligence Mission Trigger"). أي سير عمل ما زال يستخدم عُقدًا متقاعدة (خاصة محفزات Cron أو عُقد Function) سينكسر أيضًا.

## المصادر
- https://medium.com/@bonfacealfonce/n8n-3-0-is-coming-heres-what-your-automations-need-before-you-upgrade-efce9897b6cb — 2026-10-03
- https://github.com/n8n-io/n8n-docs/pull/5111 — يتضمن "DEPRECATED: npm installs (will be removed in v3.0)"
- https://github.com/itspoma/n8n-challenges/blob/HEAD/content/blog/en/article-8e9e88be-5d7d-4cfa-944e-85c2ea5c5063.md — 2026-09-29 (يستشهد بتوثيق n8n: npm مهمل بدءًا من 3.0)

## الإجراء المقترح
**اعتماد (تخطيط)** — بدء تخطيط ترحيل Docker Compose الآن (نشر تجريبي + ترحيل البيانات/بيانات الاعتماد قبل لمس 3.0)؛ التثبيت على 2.x وتدقيق سير عمل المهام بحثًا عن العُقد المتقاعدة. صُنّف حرجًا على مستوى التخطيط لأنه يُهمل طريقة النشر التي تعتمد عليها أداة نعتمد عليها.
