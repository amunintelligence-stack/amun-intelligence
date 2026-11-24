# لقطة أطر الوكلاء في 19 أكتوبر: LangGraph 1.2.16 وCrewAI 1.15.28 وAutoGen مجمّد

## ما تغيّر
- مقارنة موثّقة من فهرس الحزم بتاريخ 19 أكتوبر 2026: LangGraph 1.2.16، CrewAI 1.15.28، AutoGen 0.14.1 (مع ملاحظة أن حزمة pyautogen القديمة أصبحت وكيلًا يثبّت autogen-agentchat الجديد).
- الصورة الأوسع (منتصف أكتوبر): LangGraph 1.2.14 في 6 أكتوبر بإيقاع شبه أسبوعي، CrewAI 1.15.27 في 9 أكتوبر، Agno 3.1.2 في 8 أكتوبر (تحوّل من مكتبة إلى «منصة»)، Pydantic AI 2.55.0 في 9 أكتوبر، Google ADK 2.11.0 في 2 أكتوبر، OpenAI Agents SDK 0.23.1 في 2 أكتوبر (ما زال قبل 1.0 رغم التبني الواسع).
- النقطة الحاسمة المتكررة: Microsoft جمّدت AutoGen (لا التزامات ميزات جديدة منذ أبريل 2026؛ آخر إصدار Microsoft هو 0.7.5 من 30 سبتمبر 2025، صيانة أمنية فقط)، وانتقل التطوير إلى Microsoft Agent Framework (Python 1.21.0 في 8 أكتوبر، GA أبريل 2026). أي مشروع جديد على مكدس Microsoft يبدأ من Agent Framework، لا من AutoGen.
- إطار القرار المتفق عليه في مصدرين مستقلين: ابدأ بوكيل واحد. يبقى الوكيل الواحد كافيًا عندما يكون العمل خطيًا، أو تتسع نافذة السياق للمشكلة كلها، أو يكون طرف واحد مسؤولًا عن المخرج، أو يكون الفريق حديثًا على الوكلاء. الوكلاء المتعددون يدفعون ثمن التنسيق وحالة النظام وعبء التقييم — وهم يستحقون الثمن فقط عندما تضيف تقسيم العمل قدرة حقيقية.

## لماذا يهم ACI؟
- هذا تأكيد خارجي لقاعدة 26 أكتوبر (ابدأ بوكيل واحد): ACI نفسه بُني على خط أنابيب حتمي مع وكلاء متخصصين عند الحاجة، لا على «فريق دردشة» حر. لا نعيد فتح هذا النقاش.
- إن احتاج ACI يومًا إطارًا للتنسيق: LangGraph هو الخيار للتدفق الحتمي القابل للتدقيق (حالة، فروع، إعادة محاولة، إيقاف واستئناف) — وهذا يطابق متطلبات مهمة استخباراتية قابلة للمراجعة. CrewAI أسرع للنماذج الأولية القائمة على الأدوار، لكنه «يقاومك عندما تحتاج ترتيبًا مفروضًا» — وهو بالضبط ما تحتاجه مهمة ACI.
- AutoGen خارج خيارات ACI الجديدة نهائيًا: مجمّد من Microsoft، وأي كود قديم عليه يحتاج خطة ترحيل إلى Agent Framework، لا تحديثًا.

## مصادر (مع التواريخ)
- Dev.to — AI Agent Frameworks in 2026: CrewAI vs LangGraph vs AutoGen, Tested (إصدارات موثّقة 19 أكتوبر 2026): https://dev.to/the_movie_9b1357e8c99cfaa/ai-agent-frameworks-in-2026-crewai-vs-langgraph-vs-autogen-tested-1geh
- Dreaming.press — AI Agent Frameworks: What Actually Changed This Fall (منتصف أكتوبر 2026): https://dreaming.press/posts/ai-agent-frameworks-whats-changed-fall-2026.html
- IntelligentTools — What Happened to Microsoft AutoGen? (فحوصات حزم 5 أكتوبر 2026): https://intelligenttools.co/blog/what-happened-to-autogen
- Dev.to — Single Agent vs Multi-Agent: A Decision Framework for Enterprise Teams (توثيق أكتوبر 2026): https://dev.to/bitneka/single-agent-vs-multi-agent-a-decision-framework-for-enterprise-teams-b5b

## الإجراء المقترح: اعتمد كقاعدة اختيار
- قاعدة ثابتة: وكيل واحد أولًا؛ LangGraph هو إطار التنسيق المرجعي إن لزم تنسيق متعدد الوكلاء في ACI؛ CrewAI للنماذج الأولية فقط؛ AutoGen ممنوع في أي عمل جديد.
- لا تُجرِ أي ترحيل إطار الآن — ACI يعمل، وهذه لقطة مرجعية لقرارات مستقبلية، لا مبرر لإعادة كتابة.

> الثقة: عالية على الإصدارات (من فهرس PyPI)؛ متوسطة على التوصيات (آراء خبراء متفقة في مصدرين).
