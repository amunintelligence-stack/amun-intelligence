# اتجاه السوق نحو Postgres + إيقاف GraphQL في Weaviate — تحديث 28 أكتوبر 2026

**التاريخ:** 2026-10-28 | **الفئة:** rag-vector | **الحالة:** اتجاهات سوق + إيقاف منتج، ليست إصدارات جديدة في ACI

## ما الذي تغيّر
- **PyPI، 1–25 أكتوبر 2026 مقابل مايو 2026 (pypistats.org، فحص 26 أكتوبر):** حصة تنزيلات pgvector ارتفعت **+74%**، وrank-bm25 +55%، وbm25s +30% — مقابل تراجع عملاء Qdrant −39%، وPinecone −36%، وChroma −36%، وFAISS −22%. في أول 25 يومًا من أكتوبر تفوّق pgvector وحده (30.9 مليون) على Qdrant+Chroma+Pinecone مجتمعة (21.4 مليون). القراءة: السوق يميل إلى "المتجه عمود آخر في Postgres" بدل قاعدة متجهات مستقلة جديدة — وهذا يدعم بقاء pgvector كبديل خفيف في ACI، ولا يلغي خطة Qdrant 1.20.x للإنتاج الهجين.
- **Weaviate:** GraphQL **مهمل منذ 26 أكتوبر**، ويُطفأ على Weaviate Cloud في **1 مايو 2027** (مقارنة tech-insider، 27–28 أكتوبر). Weaviate ليست في مكدس ACI، لكنها إشارة: أي اعتماد مستقبلي على GraphQL فوق مخزن المتجهات مخاطرة هجرة.
- **Qdrant 1.20.1:** لم يُعثر على إصدار 1.20.1 حتى فحص الليلة — خطة الترقية تبقى: **انتظار نافذة 1.20.1** كما قررت ليلة 22 أكتوبر. إعلان BusinessWire في 22 أكتوبر يؤكد BM25 على النص المخزّن + تطبيع معرّفات الكود (اسم يجد getUserName/get_user_name).
- **تقرير ثانوي غير مؤكّد:** مقارنة tech-insider تذكر إغلاق Chroma Cloud ضمن "مخاطر هجرة قسرية" هذا الشهر — لم يُتحقق من مصدر أولي الليلة، فيُعامل كإشاعة/تقرير حتى التأكد، ولا يؤثر على ACI (Chroma ليست في المكدس).

## لماذا يهم ACI
- يعزز قرار التصميم الحالي: TF-IDF الحالي → Qdrant 1.20.x للإنتاج، وpgvector كبديل خفيف — بدل إضافة قاعدة ثالثة.
- درس التكلفة من ليلة 27 أكتوبر ما زال قائمًا: S3 Vectors بـ 0.06$/GB-شهر لا ينافس إلا فوق 100M+ متجه؛ أحجام ACI أصغر بكثير، فلا مبرر لتغيير المخزن لأسباب تكلفة.

## الإجراء: WATCH
- لا تغيير على خطة Qdrant 1.20.x. إعادة فحص 1.20.1 في دورة الغد.
- عند أي تجربة مستقبلية مع Weaviate: حظر الاعتماد على GraphQL، والعمل عبر REST/gRPC فقط.

## المصادر
- https://tensorust.com/articles/context-engineering-rag-not-dead-pypi/ (فحص 26 أكتوبر 2026)
- https://tech-insider.org/ca/vector-database-comparison-pinecone-qdrant-weaviate-milvus-pgvector-2026/ (تحديث 27–28 أكتوبر 2026)
- https://www.businesswire.com/news/home/20261022243967/en/Qdrant-1.20-Simplifies-Hybrid-Search-by-Ranking-Keywords-Directly-on-Stored-Text (22 أكتوبر 2026)
