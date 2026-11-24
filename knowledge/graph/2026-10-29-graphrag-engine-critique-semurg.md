# نقد GraphRAG 2026: Neo4j ليس الخيار الأسرع لأحمال الذاكرة المؤقتة — وSemurg يدّعي أرقامًا غير متحقق منها

## ما الذي تغيّر
- **نقد معماري (dev.to، أكتوبر 2026):** حجة أن Neo4j — المصمم لبيانات علاقات مستقرة ومنظمة — غير مناسب لأحمال GraphRAG التي تتسم باستعلامات هجينة مؤقتة عالية السرعة. البدائل المقترحة: ArcadeDB (Apache 2.0، متعدد النماذج، Cypher+SQL+Gremlin، خادم MCP مدمج)، FalkorDB (داخل الذاكرة، Redis + GraphBLAS، ادعاء 10–100x أسرع في الاجتياز متعدد القفزات من Neo4j)، TigerGraph (موزّع، GSQL)، ArangoDB (4 نماذج في محرك واحد، ~8x أسرع من Neo4j في أحمال متعددة النماذج حسب الادعاء)، Memgraph (C++ داخل الذاكرة، متوافق مع Bolt).
- **Semurg (مدونة 27 أكتوبر 2026):** محرك موحّد جديد يدّعي على رسم Orkut الاجتماعي: استعلام 4 قفزات في 2.94ms مقابل Neo4j 285.7ms وArangoDB 347ms وFalkorDB 207ms؛ وبحث متجه في 14.3ms مقابل Milvus 19.0ms وpgvector 59.3ms. **الأرقام من مدونة البائع نفسه، بلا تحقق مستقل — تُعامل كادعاءات لا كحقائق.**
- **FalkorDB:** عرض تجريبي «عقل شركة» مبني من GitHub خاص بها (Graph Hacks، أكتوبر 2026) — مثال تطبيقي على GraphRAG + MCP، لا منتج جديد.

## لماذا يهم ACI
- رسم ACI الحالي networkx داخل الذاكرة + لقطات JSON في Postgres، والمرشح المعتمد هو FalkorDB 6.0.3. النقد يعزز اتجاه FalkorDB (داخل الذاكرة، اجتياز سريع) مقابل Neo4j الثقيل، ويدعم نمط «المحرك الموحّد» (متجه + رسم) كاتجاه مراقبة — لكن Semurg حديث جدًا وغير متحقق منه، فلا يدخل أي خطة.
- نمط ArcadeDB (خادم MCP مدمج) يستحق النسخ كممارسة عند بناء أي واجهة MCP فوق رسم ACI مستقبلًا.

## الإجراء: WATCH
- لا تغيير: الرسم يبقى networkx، والمرشح FalkorDB 6.0.3. Semurg مراقبة فقط حتى يظهر تقييم مستقل.

## المصادر (فحص 29 أكتوبر 2026)
- https://dev.to/techanalysisinsights/why-id-think-twice-before-picking-neo4j-for-a-graphrag-stack-in-2026-1jb7
- https://one.semurg.io/blog/semurg-against-the-databases-you-run
- https://dev.to/chethan_vasthaw/we-built-falkordb-a-company-brain-from-its-own-github-it-knew-things-they-may-not-47h8
