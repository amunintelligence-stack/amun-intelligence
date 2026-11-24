# Microsoft Agent Framework — Python 1.19.0 (سبتمبر 2026)
- التاريخ: 2026-10-10 | الفئة: multi-agent | الإجراء: **مراقبة**

## ما الذي تغيّر
- صدرت النسخة **python-1.19.0** بتاريخ 2026-09-18 (و .NET 1.22.0 في نفس اليوم).
- أبرز الإضافات:
  - بروتوكولات vector-store عامة (provider-agnostic) في `agent-framework-core`.
  - موصلات vector-store جديدة (alpha): MongoDB، Azure DocumentDB، وAzure Cosmos DB NoSQL.
  - تسجيل أسماء ثابتة لـ built-in orchestration workflows مع checkpoint types قابلة للاستعادة.
  - خيار استدعاء الدوال بشكل تسلسلي (sequential function calls).
  - CodeAct tool parameter schemas مع أوصاف قابلة للضبط.
  - عرض Aspire traces في DevUI.
- إطار العمل GA منذ أبريل 2026 وAutoGen أصبح رسميًا في وضع الصيانة (bug/security fixes فقط) — مايكروسوفت توجّه العمل الجديد نحو Agent Framework.

## لماذا يهم ACI
- موصلات vector-store الموحدة تسهل تبديل قاعدة المتجهات (Qdrant/Postgres) مستقبلًا، وcheckpointing للـ orchestration يهم أي مهام استخباراتية طويلة الأمد متعددة الوكلاء.
- تأكيد توجه AutoGen → maintenance mode يعني أي تصميم معماري جديد يُفضَّل أن يُبنى على Agent Framework أو LangGraph بدل AutoGen.

## المصادر
- https://github.com/microsoft/agent-framework/releases/tag/python-1.19.0 — 2026-09-18
- https://github.com/microsoft/agent-framework/blob/HEAD/python/CHANGELOG.md — تم الوصول 2026-10-10

## الإجراء المقترح
**مراقبة** — لا تبنِ عليه الآن، لكن اعتبره المرشح الرئيسي لأي migration مستقبلي خارج AutoGen.
