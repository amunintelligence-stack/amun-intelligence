# LangGraph4j 1.9.6 — Action Catalogs: تنظيم سلوك الرسم بـ @NodeAction و@EdgeCondition (أكتوبر 2026)

## ماذا تغيّر؟

ابتداءً من LangGraph4j 1.9.6 (مكتبة LangGraph لجافا، مغطّاة عندنا حتى 1.9.0):
- تعليقان جديدان في `langgraph4j-core` بحزمة `org.bsc.langgraph4j.annotation`:
  - `@NodeAction` — طريقة جافا عادية تصبح فعل عقدة (node action) ينتج تحديثات لحالة الرسم.
  - `@EdgeCondition` — طريقة تصبح قرار توجيه (routing)، مع تحديثات حالة اختيارية.
- تُجمَّع في **Action Catalog**: كلاس يطبق واجهة `ActionCatalog`؛ `ActionCatalogRepository.of(catalog)` يكتشف الطرق المعلّمة (بما فيها الموروثة) ويكيّفها أفعالًا قابلة للتنفيذ.
- الفصل المعماري: **الكتالوج يملك السلوك، وتعريف `StateGraph` يملك الروابط** — تسجيل الكتالوج لا ينشئ workflow تلقائيًا؛ ما زلنا نختار الأفعال التي تصبح عقدًا ونقطة البداية وخريطة التوجيه.
- التعليقان يدعمان سمتين اختياريتين، منها اسم صريح مستقر للفعل (مفيد عند إعادة تسمية الطرق) مع أسماء فريدة داخل كل خريطة بحث.

## لماذا يهم ACI؟

- **قيمة تصميمية أكثر من كونها خبر إصدار**: نمط "فصل السلوك عن الروابط" هو بالضبط ما نحتاجه لو أعدنا كتابة طبقة التنسيق (orchestration) في ACI مستقبلًا — مكتبة أدوات/أفعال قابلة للاكتشاف تُركَّب عليها الرسوم دون أن يتداخل كود التنفيذ مع منطق التوجيه.
- LangGraph4j خيارنا الجاد لو احتجنا تنسيق وكلاء بلغة JVM يومًا ما؛ الـ annotations تقلل الـ boilerplate في تعريف العقد.
- لا تأثير مباشر على الـ backend الحالي (Python/FastAPI) — راقب فقط.

## مصادر (مع التواريخ)

- Medium (Bartolomeo Sorrentino) — LangGraph4j Annotations: Organize Graph Behavior with Action Catalogs (أكتوبر 2026، منشور قبل يوم من 23 أكتوبر): https://medium.com/@bsorrentino/langgraph4j-annotations-organize-graph-behavior-with-action-catalogs-88a2e2d2acbb
- Toolbit AI — LangGraph vs. CrewAI: Which Multi-Agent Framework? (أكتوبر 2026 — سياق: LangGraph v1.2 أضاف per-node timeouts، node-level error handlers بنمط Saga، graceful shutdown، وDeltaChannel beta): https://www.toolbit.ai/blog/langgraph-vs-crewai-choosing-the-right-python

## الإجراء المقترح: راقب — لا تغيير فوري؛ اعتمد نمط "كتالوج الأفعال" كمبدأ تصميمي مرجعي عند تطوير طبقة التنسيق في ACI، وقيّم LangGraph4j 1.9.6+ عند أي تجربة JVM مستقبلية.

> الثقة: متوسطة (مصدر مجتمعي يتبع التوثيق الرسمي؛ رقم الإصدار 1.9.6 من المقال نفسه)
