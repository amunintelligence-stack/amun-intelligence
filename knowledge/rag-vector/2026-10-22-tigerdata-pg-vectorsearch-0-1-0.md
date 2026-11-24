# Tiger Data pg_vectorsearch 0.1.0 — فهرس PRISM للمتجهات داخل Postgres

**Date found:** 2026-10-22 (nightly dev researcher)

## What changed
أعلنت Tiger Data (Timescale سابقًا) في **13 أكتوبر 2026** عن **pg_vectorsearch 0.1.0** — إضافة Postgres مفتوحة المصدر (ترخيص PostgreSQL) تضيف طريقة فهرسة جديدة **PRISM** (Partitioned Routing Index for Similarity Matching):
- **يعمل فوق أعمدة pgvector الحالية**: الأنواع `vec32`/`vec16` متوافقة ثنائيًا مع `vector`/`halfvec` — يمكن بناء فهرس PRISM على جدول موجود **دون إعادة كتابة البيانات**، واستعلامات pgvector تعمل كما هي.
- التصميم: شجرة مراكز هرمية للتوجيه + تخزين مضغوط RaBitQ (~بت واحد لكل بُعد) + إعادة ترتيب بالمتجهات الكاملة من الـheap.
- الأرقام (من الشركة نفسها — غير مستقلة): بناء فهرس 100M متجه في ~1h40m على 128GiB، واستعلامات ~21ms عند recall 99%؛ بناء HNSW لم يُكمل على نفس الجهاز. تحليل مستقل (dev.to) خلص أن تفوق الاستعلام حقيقي وكبير، لكن مقارنة زمن البناء منحازة.
- **تحفظات موثقة في ملاحظات الإصدار**: الحذف يترك tombstones تُستعاد بـREINDEX؛ الـrecall قد ينجرف مع الإدخالات/التحديثات المتكررة (إعادة توازن يدوية)؛ حد أقصى صامت لعدد الصفوف في الـordered scan؛ وفجوة الاستعلامات المفلترة (WHERE) ما زالت قيد العمل.
- يتطلب **PostgreSQL 18+**، وما زال **alpha** (ترقيات ما قبل الإصدار قد تتطلب إسقاط الإضافة وإعادة بنائها).
- ملاحظة استراتيجية: Tiger Data تصف pg_vectorsearch كخليفة لـ**pgvectorscale** (إضافة DiskANN السابقة) — الأخيرة تتجه لوضع الصيانة.

## Why it matters for ACI
- ACI يعمل اليوم على TF-IDF V1 في Postgres مع مسار ترقية لـQdrant — pg_vectorsearch يعطي بديلًا "ابقَ في Postgres" للبحث المتجهي واسع النطاق دون خدمة جانبية، وبكلفة تجربة منخفضة (نفس الأعمدة).
- pg_textsearch (BM25 داخل Postgres، v1.1.0 production-ready على Tiger Cloud ومدمج في AlloyDB/Cloud SQL) + pg_vectorsearch = بحث هجين كامل داخل Postgres — منافس معماري جدي لثنائية Qdrant، يستحق المقارنة عند تصميم RAG V2.
- التحفظات (alpha + PG18 + tombstones + حد الـordered scan) تجعله غير صالح للإنتاج اليوم.

## Sources
- الإعلان (13 أكتوبر 2026) عبر digest بتاريخ 19 أكتوبر 2026: https://cortrix.ai/blog/semantic-tech-insights-2026-w42/
- تحليل مستقل (نُشر ~16 أكتوبر 2026): https://dev.to/alanwest/pgvectorsearch-vs-pgvector-hnsw-42-hours-vs-49-minutes-heres-the-catch-2id0
- تحليل الفجوات (نُشر ~14 أكتوبر 2026): https://dev.to/gabrielanhaia/pgvectorsearch-claims-6-ms-at-100m-vectors-filtered-queries-can-come-back-short-5cm2
- مدونة Tiger Data (pg_textsearch): https://www.tigerdata.com/blog/tag/pg_textsearch
- توثيق pg_textsearch: https://www.tigerdata.com/docs/learn/search/using-pg-textsearch
- خبر دمج pg_textsearch في AlloyDB/Cloud SQL (نُشر 21 سبتمبر 2026): https://aithority.com/machine-learning/google-cloud-brings-native-bm25-full-text-search-to-alloydb-and-cloud-sql-via-tiger-datas-pg_textsearch/

## Action
**watch** — لا اعتماد قبل نسخة beta مستقرة؛ عند نضجه: قيّم PRISM مقابل HNSW على بيانات مهام ACI الفعلية، وقارن مسار "Postgres فقط" (pg_textsearch + pg_vectorsearch) مع مسار Qdrant 1.20 في RAG V2. سجّل pgvectorscale كـmaintenance-mode في السجل.
