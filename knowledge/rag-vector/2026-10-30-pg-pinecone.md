# pg_pinecone (27 أكتوبر 2026): بحث متجهي داخل Postgres على أعمدة pgvector — مع تقاعد GraphQL في Weaviate

## ما الذي تغيّر
- **27 أكتوبر 2026:** أطلقت Pinecone الامتداد مفتوح المصدر **pg_pinecone** (Apache 2.0) لبحث المتجهات داخل Postgres على أعمدة pgvector الحالية، دون تغيير الجداول أو استعلامات SQL (`ORDER BY embedding <=> $1 LIMIT 10`).
  - ثلاثة محركات لكل جدول: `native` (الافتراضي — يبني ويبحث داخل Postgres، بلا حساب Pinecone أو مفاتيح أو اتصالات شبكية)، و`pgvector` (يبحث في فهرس HNSW/IVFFlat الحالي)، و`remote` (يرسل البحث إلى فهرس Pinecone مُدار عندما يتجاوز الجدول خادمًا واحدًا). التبديل بينها بمكالمة `pinecone.set_engine()` واحدة والاستعلامات لا تتغير.
  - الفكرة الجوهرية: تطبيق الفلتر **أثناء** البحث لا بعده، فيظل الاستعلام الضيّق (مستأجر واحد/مستخدم واحد) يُرجع مجموعة كاملة بدل أن يخسر نتائج بسبب تقليم فهرس الرسم البياني.
  - أرقام Pinecone الخاصة (غير مستقلة): على مليون متجه wiki_dpr بـ768 بُعدًا، الفهرس الأصلي 136 MB مقابل 2.0 GB لـHNSW على halfvec و4.1 GB على متجهات كاملة — مع ملاحظة أن اختبارات الفلترة أُجريت على PostgreSQL 18 في جلسة منفصلة.
- **في نفس الأسبوع:** Weaviate أهملت واجهة GraphQL في **26 أكتوبر 2026**، مع إيقافها على Weaviate Cloud في **1 مايو 2027**؛ وpgvector 0.8.7 (1 أكتوبر) أصلح تجاوز مخزن مؤقت، وQdrant 1.20 أضاف BM25 هجينًا.

## لماذا يهم ACI
- ACI اليوم على TF-IDF في Postgres (RAG V1) مع خطة ترقية إلى Qdrant 1.20.x. pg_pinecone يفتح مسارًا ثالثًا: البقاء في Postgres مع بحث متجهي مُصفّى أفضل من HNSW وحده، دون خادم جديد — وهو ما يناسب أحجام ACI الحالية. لكنه إصدار أول (first release)، وPinecone نفسها تطلب ملاحظات المجتمع، وأرقامه من مختبرها فقط.
- إهمال GraphQL في Weaviate لا يؤثر على ACI (Weaviate خارج المكدّس)، لكنه تذكير: أي اعتماد مستقبلي على واجهة «مريحة» يحتاج خطة خروج قبل أن تُعلن الشركة تقاعدها.

## الإجراء: WATCH (تجربة معزولة، لا اعتماد)
1. لا تغيير على خطة Qdrant 1.20.x؛ pg_pinecone مرشح تجربة فقط.
2. عند توفر نافذة: ثبّته على نسخة Postgres غير إنتاجية، وقارنه بـHNSW الحالي على عيّنة عربية من بيانات ACI، مع التركيز على الاستعلامات المُصفّاة (per-mission/per-tenant) لا على المتوسطات غير المُصفّاة.
3. أعد فحصه بعد إصدارين مستقرين أو بعد ظهور تقييم مستقل للأرقام.

## المصادر (تواريخ الفحص 30 أكتوبر 2026)
- إعلان Pinecone (27 أكتوبر 2026): https://www.pinecone.io/blog/introducing-pg-pinecone/
- سجل إصدارات Pinecone 2026: https://docs.pinecone.io/release-notes/2026
- تغطية Unite.AI (27 أكتوبر 2026): https://www.unite.ai/pinecone-releases-pg-pinecone-an-open-source-postgres-search-extension/
- مقارنة أكتوبر 2026 (28 أكتوبر 2026، تشمل تقاعد GraphQL): https://tech-insider.org/ca/vector-database-comparison-pinecone-qdrant-weaviate-milvus-pgvector-2026/
