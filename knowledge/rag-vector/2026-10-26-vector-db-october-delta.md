# Vector DBs: دلتا أكتوبر — Milvus 3.0.3 وWeaviate 1.40.1 وLanceDB 0.40.0 (2026-10-26)

> دلتا فوق لقطة 24 أكتوبر وملاحظة Qdrant 1.20 (25 أكتوبر) — لا تعيد ما فيهما. خطة Qdrant 1.20.x ما زالت قائمة بلا تغيير.

## ماذا تغيّر؟
- **Milvus v3.0.3 (14 أكتوبر 2026):** أوسع تشكيلة فهارس في اللقطة — HNSW وIVF وFLAT وSCANN وDiskANN وCAGRA (GPU). نشر Lite مدمج وStandalone وDistributed.
- **Weaviate v1.40.1 (13 أكتوبر 2026):** فهارس HNSW وFlat وDynamic وHFresh (الأخير يدعم cosine وl2-squared فقط). تنبيه ترخيص متكرر: الشفرة خارج `wl/` تحت BSD-3-Clause، وما داخل `wl/` تحت ترخيص Weaviate Enterprise — اقرأ ملف LICENSE قبل أي إعادة توزيع للثنائي.
- **LanceDB v0.40.0 (7 أكتوبر 2026):** مدمج (يعمل داخل العملية) مع فهارس IVF-PQ وHNSW وبناء فهارس GPU؛ خيار سحابي serverless.
- **تحذير مقارن (Tiger Data):** في اختبارهم الخاص، بنى Qdrant فهرسه أسرع من pgvectorscale — مهم إن كان معدل تعديل البيانات مرتفعًا جدًا، وهو وصف ينطبق على مخازن ذاكرة الوكلاء.

## لماذا يهم ACI؟
- لا شيء هنا يغيّر خطة RAG الحالية (Postgres + pgvector أولًا، وQdrant 1.20.x هدف الترقية). القيمة في نقطتين:
  1. إن نضج حجم بيانات ACI إلى ملايين المتجهات مع تعديلات متكررة، يصبح Qdrant (وليس pgvectorscale) هو البديل المُفضَّل — وهذا يعزز خطة الترقية القائمة بدل أن ينافسها.
  2. LanceDB المدمج مرشح خفيف لاحقًا لأي مكوّن ACI يعمل بلا خادم (أداة محلية)، لكنه ليس بديلًا عن مخزن المهمات المركزي.

## مصادر (مع التواريخ)
- Intelligibberish — Best vector databases for self-hosted RAG (أكتوبر 2026؛ إصدارات موثّقة بتواريخها): https://intelligibberish.com/articles/best-vector-databases-for-self-hosted-rag/
- Geekflare — Best Open Source Vector Databases in 2026 (تحديث أكتوبر 2026): https://geekflare.com/open-source/vector-database/
- Jahanzaib.ai — Vector Database Comparison 2026 (تحذير Tiger Data حول سرعة بناء الفهرس): https://www.jahanzaib.ai/blog/vector-database-ai-agents-pinecone-weaviate-chroma-qdrant

## الإجراء المقترح: راقب
- لا تغيير في الخطة. عند مراجعة RAG القادمة: أعد قياس سرعة بناء الفهرس تحت تعديلات متكررة على عينة ACI قبل تثبيت Qdrant 1.20.x نهائيًا.

> الثقة: متوسطة (مقارنات ثانوية متفقة على أرقام الإصدارات؛ أرقام Tiger Data من مصدرها نفسه، لم تُعَد اختبارها).
