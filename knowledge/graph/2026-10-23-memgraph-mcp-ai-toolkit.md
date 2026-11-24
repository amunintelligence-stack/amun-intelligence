# Memgraph — خادم MCP بوضع قراءة صارم + حزمة AI للـ GraphRAG (أكتوبر 2026)

## ماذا تغيّر؟
تحديثان متزامنان في منظومة Memgraph (أكتوبر 2026، حسب مدوناتهم الرسمية):
1. **خادم MCP مُصلَّب:** وضع قراءة فقط صارم يمنع `CREATE/MERGE/DELETE/SET/DROP/REMOVE` مع خطأ منظم (`Set MCP_READ_ONLY=false` للكتابة)؛ دعم Streamable HTTP وSTDIO؛ تثبيت عبر `uv`؛ مصادقة وأسماء قواعد غير افتراضية؛ بناء Docker من monorepo الخاص بـ ai-toolkit.
2. **AI Toolkit — SQL2Graph وUnstructured2Graph:** خطوط أنابيب لتحويل SQL والملفات غير المنظمة (PDF/DOCX/TXT) إلى رسم معرفي في Memgraph، مع تكامل **LightRAG** لاستخلاص الكيانات عبر LLM. المعلن القادم: **MCP Client داخل Memgraph Lab** (وكلاء يتفاعلون مع خوادم MCP متعددة لحظيًا).
3. **Memgraph 3.14.0:** صفحة التنزيل الرسمية تعرض حزم v3.14.0 (x86_64/aarch64، deb/rpm، نسخ FIPS) — إصدار رئيسي جديد بعد 3.13.x التي غطيناها، دون سجل تغييرات منشور وجدته بعد.

## لماذا يهم ACI؟
- **نمط أمني للتبني المباشر:** وضع القراءة الصارم في خادم MCP هو بالضبط ما نحتاجه عندما نعرض أي رسم بياني لوكلاء LLM — اعتمده كمتطلب في أي واجهة MCP نضيفها لرسم الأدلة.
- Unstructured2Graph + LightRAG منافس/بديل محتمل لخط بناء الرسم المعرفي لدينا (اليوم: استخلاصنا الخاص + networkx). راقبه قبل أي قرار بناء-مقابل-شراء.
- Memgraph نفسه ليس في خطتنا (FalkorDB هو المرشح)، لكن 3.14.0 يستحق ملاحظة في السجل كبديل.

## مصادر (مع التواريخ)
- Memgraph Blog — Pushing MCP Forward: What's New in the Memgraph MCP Server (أكتوبر 2026): https://memgraph.com/blog/pushing-mcp-forward
- Memgraph Blog — Welcome SQL2Graph + Unstructured2Graph (أكتوبر 2026): https://memgraph.com/blog/introducing-ai-toolkit-for-graphrag-sql2graph-unstructured2graph
- Memgraph — Direct download links (تعرض v3.14.0، زُحفت 23 أكتوبر 2026): https://memgraph.com/docs/getting-started/install-memgraph/direct-download-links

## الإجراء المقترح: راقب — اعتمد نمط "وضع القراءة الصارم" تصميميًا لأي MCP فوق الرسم البياني. لا تغيير في خطة المحرك (FalkorDB 6.0.3 يبقى المرشح).

> الثقة: عالية (محتوى المدونات) / متوسطة (تاريخ الإصدار الدقيق ووجود سجل تغييرات 3.14.0)
