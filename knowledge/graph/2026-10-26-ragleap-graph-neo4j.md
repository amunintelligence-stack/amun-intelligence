# ragleap-graph 0.9.0: رسم بياني للكيانات فوق Neo4j لاسترجاع RAG (2026-10-26)

## ماذا تغيّر؟
- مكتبة جديدة موثّقة: **ragleap-graph 0.9.0** تضيف استخراج الكيانات ورسوم التواجد المشترك (co-occurrence) والاسترجاع القائم على الرسم البياني فوق Neo4j، ومصممة لأنظمة RAG مثل ragleap-rag.
- الواجهة دنيا: `pip install ragleap-graph`، ثم `GraphIndex.upsert_document(document_id, title, chunks)` للتخزين، و`find_documents_by_entities([...])` للبحث بالكيان، و`search_related_entities([...], max_depth=2)` للكيانات المرتبطة حتى عمق 2.
- يتطلب مثيل Neo4j عاملًا (مثال README: `bolt://localhost:7687`) وكلمة مرور.

## لماذا يهم ACI؟
- طبقة الرسم البياني لدينا حاليًا networkx + Postgres (مع FalkorDB كمرشح). ragleap-graph لا ينافسها مباشرة — قيمته كنمط مرجعي: **الاسترجاع بالكيان أولًا ثم بالمستند**، بدل البحث المتجهي فقط. إن أردنا لاحقًا ربط مستندات المهمات بالكيانات (شركات/أشخاص)، فهذا هو الشكل الأبسط للواجهة المطلوبة.
- نقطة حذر: الاعتماد على Neo4j كامل يضيف خادمًا ثقيلًا (JVM) مقابل مكاسب الاسترجاع بالكيان — وزنه مقابل FalkorDB الخفيف/المدمج ما زال لصالح FalkorDB في سياق ACI.

## مصادر (مع التواريخ)
- RagLeap Blog — How to add a knowledge graph to a RAG system with ragleap-graph and Neo4j (دليل يتبع README لإصدار 0.9.0؛ آخر تحديث قبل ~3 أيام من 26 أكتوبر 2026): https://ragleap.com/blog/how-to-add-a-knowledge-graph-to-rag-with-neo4j/

## الإجراء المقترح: راقب
- لا تثبيت. عند تصميم استرجاع الكيانات في ACI: استعر واجهة `find_documents_by_entities` / `search_related_entities` كمواصفة، ونفّذها فوق مخزننا الحالي قبل إضافة Neo4j.

> الثقة: متوسطة (مدونة منتج تصف README الخاص بها؛ لم تُختبر المكتبة هنا).
