# دلتا الأطر متعددة الوكلاء — CrewAI 1.15.39 (توثيق فقط)؛ الباقي بلا تغيير (9 نوفمبر 2026)

## CrewAI 1.15.39 — صدر اليوم؛ تغيير توثيقي فقط

- **التاريخ:** 1.15.39 رُفع إلى PyPI في 2026-11-09 01:07 UTC؛ صفحة الإصدار قُرئت كاملة.
- **ما الذي تغيّر:** التغيير الوحيد هو توثيق خطأ `apps_not_connected` على نقطتي `/kickoff` و`/status`. لا ميزات ولا إصلاحات كود في هذا الإصدار.
- **لماذا يهم ACI:** لا أثر. يبقى 1.15.38 (8 نوفمبر) آخر إصدار ذي محتوى وظيفي: gpt-6-luna نموذجًا افتراضيًا + قراءة جداول عبر URL.
- **المصادر:** https://github.com/crewAIInc/crewAI/releases/tag/1.15.39 — https://pypi.org/pypi/crewai/json (تحقق 2026-11-09)
- **الإجراء: ignore.**

## LangGraph / Microsoft Agent Framework / AG2 — بلا تغيير

- **التاريخ:** تحققنا من PyPI في 9 نوفمبر 2026.
- **ما الذي تغيّر:** لا شيء: langgraph ما زال 1.2.20 (5 نوفمبر)، وlanggraph-sdk ما زال 0.4.14 (6 نوفمبر)، وحزمة `agent-framework` (MAF Python) ما زالت 1.25.0 (7 نوفمبر)، وAG2 ما زال 1.3.0 (4 نوفمبر).
- **المصادر:** https://pypi.org/pypi/langgraph/json — https://pypi.org/pypi/langgraph-sdk/json — https://pypi.org/pypi/agent-framework/json — https://pypi.org/pypi/ag2/json
- **الإجراء: ignore** (بلا جديد).

## تأكيد ثانوي — AutoGen مؤرشف؛ المقارنات المحدّثة في 9 نوفمبر تتفق

- **ما الذي تغيّر:** ثلاث مقارنات أطر محدّثة في 8–9 نوفمبر 2026 (what-will.ai، kanerika.com، aliteq.com) تتفق جميعًا على أن AutoGen مؤرشف وأن Microsoft توجّه المستخدمين الجدد إلى Microsoft Agent Framework، وأن AG2 هو الشوكة المجتمعية الحية الوحيدة — ما يطابق تحققنا المباشر من README في 8 نوفمبر. (ملاحظة: مصدر ثانوي واحد ما زال يكتب «وضع صيانة» — متأخر؛ نص README هو المعتمد.)
- **لماذا يهم ACI:** لا أثر تشغيلي (ACI لا يشغّل AutoGen)؛ لكن أي مرجع تصميمي يذكر AutoGen كخيار حي يجب تحديثه إلى «مؤرشف بلا دعم».
- **المصادر:** https://what-will.ai/blog/best-open-source-ai-agent-frameworks (9 نوفمبر 2026) — https://kanerika.com/blogs/ai-agent-frameworks/ (محدّث 8 نوفمبر 2026) — https://aliteq.com/best-ai-agent-frameworks (محدّث 3 نوفمبر 2026)
- **الإجراء: adopt** — حدّث كل مرجع لـ AutoGen في السجل والمستندات من «صيانة» إلى «مؤرشف بلا دعم» (استمرارًا لإجراء 8 نوفمبر).
