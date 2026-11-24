# دلتا الرسم البياني — Neo4j Relate مفتوح المصدر Apache 2.0؛ نجوم FalkorDB تتضاعف؛ لا إصدارات جديدة (21 نوفمبر 2026)

## 1. Neo4j Relate — التفاصيل المؤكدة بعد الإطلاق (12 نوفمبر 2026)

- **ما الذي تغيّر:** قاعدة رسم بياني في الذاكرة مبنية بـRust للوكلاء والأنظمة الوكيلة؛ openCypher ‏100%‏ وGQL ‏+97%‏؛ واجهتا Bolt وHTTP Query API v2 كبديل مباشر (drop-in) لبرامج Neo4j التشغيلية؛ مفتوحة المصدر Apache 2.0؛ متاحة الآن. هاكاثون Relate (فُتح 11 نوفمبر، شهر كامل) ما زال جاريًا.
- **لماذا يهم ACI:** مرشح مستقبلي لطبقة الذاكرة/الرسم للوكلاء (خفيف، يبدأه الوكيل نفسه) — لكن الرسم في ACI ما زال networkx؛ لا تغيير في الخطة، والنمط (ذاكرة وكيل خفيفة + استدلال متعدد القفزات + GraphRAG) قابل للاستعارة.
- **المصادر:** https://www.blocksandfiles.com/ai-ml/2026/11/13/neo4js-rusty-in-memory-ai-agent-graph-database/5309746 (13 نوفمبر 2026)
- **الإجراء: watch.**

## 2. لا إصدارات جديدة: Neo4j 2026.10.2 (2 نوفمبر) وFalkorDB 6.0.4 وMemgraph 3.14.0 ما زالت الأحدث

- **ما الذي تغيّر:** تحقق الليلة من endoflife.date وFirmwarely: لا إصدار أحدث لأي من الثلاثة.
- **المصادر:** https://endoflife.date/neo4j ؛ https://www.firmwarely.com/devices/neo4j/ ؛ https://www.peterindia.net/GraphDBs.html
- **الإجراء: ignore.**

## 3. FalkorDB: النجوم تتضاعف تقريبًا في 90 يومًا (5,570 ← 10,508)

- **ما الذي تغيّر:** من 17 أغسطس إلى 17 نوفمبر 2026 عبر GitHub REST API؛ إشارة زخم مجتمع قوية لمرشح الرسم.
- **لماذا يهم ACI:** يعزز الثقة في التثبيت 6.0.4 كمرشح رسم؛ لا تغيير في الخطة.
- **المصادر:** https://www.xerj.org/compare/best-graph-database-for-graphrag-2026 (17 نوفمبر 2026)
- **الإجراء: watch.**

## 4. فحص التراخيص: «مفتوح المصدر» ليست كلها OSI

- **ما الذي تغيّر:** تحديث ArcadeDB ‏12 نوفمبر: FalkorDB ‏SSPL v1‏، Memgraph ‏BSL 1.1‏، ArangoDB ‏BSL — ليست تراخيص OSI؛ الوحيدة المعتمدة OSI بين المقارَنين: ArcadeDB ‏(Apache 2.0)‏ وHugeGraph ‏(Apache 2.0)‏ وKuzu/LadybugDB ‏(MIT)‏. ArcadeDB ‏26.11.1‏ (نوفمبر 2026) ما زال الأحدث؛ LadybugDB يُصدر بنشاط الآن.
- **لماذا يهم ACI:** عند أي قرار اعتماد لمحرك رسم، الترخيص قيدٌ مستقل عن الأداء — FalkorDB ‏(SSPL)‏ مقبول كمرشح داخلي لكنه ليس «مفتوح المصدر» بالمعنى القانوني الدقيق.
- **المصادر:** https://arcadedb.com/blog/neo4j-alternatives-in-2026-a-fair-look-at-the-open-source-options/ (حدّث 12 نوفمبر 2026)
- **الإجراء: watch** — أضف ملاحظة الترخيص إلى سجل FalkorDB/Memgraph.
