# دلتا الأطر متعددة الوكلاء — بلا تغيير؛ تصحيح رقم إصدار MAF في المقارنات (10 نوفمبر 2026)

## LangGraph / CrewAI / Microsoft Agent Framework / AG2 / AutoGen — بلا تغيير

- **ما الذي تغيّر:** لا شيء. تحققنا من PyPI في 10 نوفمبر 2026:
  - **langgraph 1.2.20** (5 نوفمبر) ما زال الأحدث.
  - **crewai 1.15.39** (9 نوفمبر) ما زال الأحدث — تغيير توثيقي فقط كما سُجّل أمس.
  - **agent-framework (MAF Python) 1.25.0** (7 نوفمبر) ما زال الأحدث.
  - **autogen-agentchat 0.7.5** (30 سبتمبر 2025) بلا تغيير — مؤرشف/صيانة فقط.
- **لماذا يهم ACI:** لا أثر؛ خط الأساس من دورة 9 نوفمبر ما زال قائمًا.
- **المصادر:** https://pypi.org/pypi/langgraph/json — https://pypi.org/pypi/crewai/json — https://pypi.org/pypi/agent-framework/json — https://pypi.org/pypi/autogen-agentchat/json (تحقق 2026-11-10)
- **الإجراء: ignore** (بلا جديد).

## تصحيح منهجي — مقارنات نوفمبر تذكر MAF «1.26»؛ PyPI يقول 1.25.0

- **ما الذي تغيّر:** مقارنات أطر محدّثة في 3–9 نوفمبر 2026 (aibuzz.blog، forasoft.com) تذكر Microsoft Agent Framework بإصدار **1.26** (أكتوبر 2026). تحققنا المباشر من PyPI الليلة يقول إن أحدث إصدار منشور هو **1.25.0** (7 نوفمبر 2026) — لا 1.26 على PyPI. الأرجح أن «1.26» رقم داخلي أو خطأ نسخ في المقارنات الثانوية؛ **PyPI هو المعتمد** حتى يظهر وسم 1.26 على GitHub.
- **لماذا يهم ACI:** لا أثر تشغيلي (ACI لا يشغّل MAF)؛ لكن أي مرجع تصميمي يذكر 1.26 يُصحَّح إلى 1.25.0.
- **المصادر:** PyPI (تحقق 2026-11-10) — https://aibuzz.blog/ai-agent-frameworks-explained/ (3 نوفمبر 2026) — https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/langgraph-vs-crewai-vs-autogen-agent-frameworks (أكتوبر 2026)
- **الإجراء: ignore** — تصحيح توثيقي فقط.
