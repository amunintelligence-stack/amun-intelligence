# تقارب أطر الوكلاء خريف 2026: الجميع يتحرك نحو «رسم + حالة» — واختلافات البقاء والملاجئ

## ما الذي تغيّر
- **التقارب المعماري (تحليلات منتصف أكتوبر 2026):** LangGraph وCrewAI وGoogle ADK وMicrosoft Agent Framework كلها تتحرك نحو الشكل نفسه: رسم (graph) بحالة صريحة. LangChain 1.x يجعل `create_agent` يعيد رسم LangGraph مجمّعًا؛ ADK 2.0 أعاد البناء حول runtime رسم بياني (Python GA مايو 2026، TypeScript أغسطس 2026)؛ CrewAI رقّت Flows الحوارية إلى stable في 1.15.18 (أغسطس 2026) مع checkpointing تلقائي وإعادة تشغيل مهام من CLI.
- **جدول مقارنة عملي (قراءات 14–17 أكتوبر 2026، عينات صغيرة يدوية):**
  - النجاة من الانهيار: LangGraph +، CrewAI +، ADK +، Strands ~ (لقطات حالة لا المهمة الجارية)، MAF + عبر workflows، OpenAI Agents SDK ~ (عبر Temporal وشركاء)، Claude Agent SDK ~ (محادثة فقط).
  - ملجأ (sandbox) مدمج: ADK +، Strands + (Docker/SSH)، الباقي ~ إضافات أو opt-in. **الملجأ opt-in في كل المنتجات — لا يوجد افتراضي آمن.**
  - التتبع في مراقبتك الخاصة: ADK + (OpenTelemetry)، الباقي ~ (LangSmith/CrewAI Cloud أولًا مع إمكانية التحويل).
- **أرقام الإصدارات (منتصف أكتوبر، تأكيد لملفات سابقة):** LangGraph 1.2.14 (6 أكتوبر) ثم 1.2.15/1.2.16؛ CrewAI 1.15.27 (9 أكتوبر) ثم 1.15.28؛ ADK 2.11.0 (2 أكتوبر) ثم 2.12.0؛ Pydantic AI 2.55.0 (9 أكتوبر)؛ OpenAI Agents SDK 0.23.1 (2 أكتوبر، ما زال pre-1.0)؛ MAF Python 1.21.0 (8 أكتوبر)؛ Agno 3.1.2 (8 أكتوبر، من مكتبة إلى «منصة»)؛ AutoGen بلا feature commits منذ أبريل (مجمّد — بديله MAF).
- **فجوة الحتمية تتقلص لكنها لا تختفي:** Flows في CrewAI حتمية حيث تُعلن ذلك، لكن الـcrews الهرمية (مدير LLM يفكك المهمة) احتمالية بالبناء — إذا أخطأ المدير في التفكيك، يتغير مسار التشغيل كله. LangGraph يبقى متفوقًا في تشخيص الفشل على مستوى العقدة مع لقطة حالة للاستئناف.

## لماذا يهم ACI
- ACI يعمل بنمط mission → roster في n8n وليس بإطار وكلاء خارجي؛ قيمة هذا الملف هي قاعدة قرار مستقبلية: إذا انتقلت ACI إلى إطار وكلاء برمجي، فالمعيار هو: حالة قابلة للاستئناف على مستوى العقدة (LangGraph)، أو حتمية Flows (CrewAI)، أو OpenTelemetry الأصلي (ADK) — مع ملجأ إجباري غير opt-in في كل الحالات.
- تحذير ADK العملي (من بحث 7 أكتوبر): جلسات الذاكرة تختفي عند إعادة التشغيل، والفروع المتوازية التي تكتب نفس المفتاح تتعارض، والتأكيد على الأدوات ما زال تجريبيًا — كلها فخاخ تنطبق على أي تصميم mission-state في ACI.

## الإجراء: WATCH
- لا تغيير في بنية ACI. عند تقييم أي إطار مستقبلي: اشترط checkpointing على مستوى العقدة + sandbox غير اختياري + تتبع OpenTelemetry.

## المصادر (فحص 29 أكتوبر 2026)
- https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html
- https://geekflare.com/open-source/ai-agent-frameworks/
- https://toolbit.ai/blog/langgraph-vs-crewai-choosing-the-right-python
- https://hexcursion.com/blog/google-adk-explained
