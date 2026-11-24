# دلتا إطارات الوكلاء في 4 نوفمبر 2026 — LangGraph 1.2.19 وCrewAI 1.15.35 وMAF 1.24/1.26 ووقت تشغيل إنتاجي

## ما الجديد

- **LangGraph:** آخر إصدار مستقر هو `1.2.19` (نُشر 30 أكتوبر 2026، وفق PyPI وGitHub Releases) — إصلاح يمنع `trace_policy` من إعادة كتابة حمولات العقد المتدفقة، مع `checkpoint-sqlite 3.1.3`. حزمة `langgraph-sdk` المنفصلة وصلت إلى `0.4.12` في 3 نوفمبر 2026. لا يوجد إصدار `2.0` رسمي حتى 4 نوفمبر 2026.
- **CrewAI:** الإصدار `1.15.35` مؤكد في 4 نوفمبر 2026 (بعد `1.15.33` في 29 أكتوبر و`1.15.30` في 24 أكتوبر الذي نقل `AgentExecutor` إلى `crewai.agents.agent_executor` وأزال `CrewAgentExecutor`). خط `1.15` ما زال يتطور أسبوعيًا دون تغيير معماري معلن.
- **Microsoft Agent Framework (MAF):** بايثون وصل إلى `1.24.0` في 30 أكتوبر 2026 (ترحيل فهرس سياق Redis، خط أساس Python 3.11، وافتراضات صريحة لموافقة MCP)، وحزم .NET الأساسية عند `1.26.0` (مؤكدة في 4 نوفمبر 2026) مع حزمة `Microsoft.Agents.AI.Mcp` في مرحلة alpha لمهام MCP طويلة ومهارات MCP — مع ملاحظة تقنية: الـ alpha يثبّت `ModelContextProtocol` على `2.2.0` بالضبط، ومع `2.3.0` يظهر تحذير NU1608.
- **وقت تشغيل إنتاجي لـ MAF (أُبرز في Build 2026):** انتقل الإطار من SDK فقط إلى منصة تشغيل مدعومة — Agent Harness ووكلاء Foundry المستضافون متاحون عموميًا (GA)، مع موصلات لـ GitHub Copilot وClaude Agent SDK وأنماط تنسيق متعدد الوكلاء مستقرة.
- **تحذير عملي من مقال Towards AI (نُشر 4 نوفمبر 2026):** أدلة "LangGraph 2.0" المنتشرة غير صحيحة — PyPI يقول `1.2.19` ولا يوجد `2.0`، ودالة `create_react_agent` المقترحة في تلك الأدلة مهملة (deprecated). خلاصة المقال: الإطار مستقر، لكن المعلومات المحيطة به غير موثوقة، ويجب التثبيت من فهرس الحزم والوثائق الرسمية فقط.

## لماذا يهم ACI

- هذا يمدّد حالة 3 نوفمبر دون أن يغيّرها: LangGraph ما زال الخيار الافتراضي للعمل طويل العمر القابل للتدقيق، وCrewAI للفرق القائمة على الأدوار، وMAF لخيار Microsoft — ولا يوجد سبب الليلة لتبنّي أي إطار في ACI، لأن معمارية ACI الخمسية مصممة أصلًا لتكون مستقلة عن الإطار (Python للوكلاء القابلة للحساب، وLLM حيث يلزم التفسير فقط).
- نقطتان عمليتان تستحقان التثبيت: (1) افتراضات موافقة MCP الصريحة في MAF 1.24 تعزز اتجاه "الموافقة قبل أداة MCP" الذي نطبقه أصلًا؛ (2) تحذير "لا يوجد 2.0" قاعدة مراجعة: أي كود أو دليل يصل ACI مدّعيًا إصدارًا غير موجود يُرفض حتى يُتحقق من PyPI أو GitHub Releases.
- وقت تشغيل MAF الإنتاجي (Harness + استضافة Foundry) مهم فقط إذا قرر ACI يومًا ما العمل على مكدّس Microsoft — وهو ليس المكدّس الحالي.

## المصادر

- https://pypi.org/project/langgraph/ (سجل إصدارات langgraph — 1.2.19، 30 أكتوبر 2026)
- https://pub.towardsai.net/langgraph-in-november-2026-what-changed-what-competes-with-it-and-what-to-watch-out-for-250601568487 (Towards AI، نُشر 4 نوفمبر 2026)
- https://codehalwell.github.io/AgentGuides/crewai-guide/ (دليل CrewAI — v1.15.35، فُحص 4 نوفمبر 2026)
- https://www.developersdigest.tech/blog/microsoft-agent-framework-whats-new-2026 (آخر تحديث 2 نوفمبر 2026 — Python 1.24.0 في 30 أكتوبر)
- https://codehalwell.github.io/AgentGuides/microsoft-agent-framework-guide/dotnet/microsoft_agent_framework_dotnet_mcp/ (MAF .NET — Microsoft.Agents.AI 1.26.0، فُحص 4 نوفمبر 2026)
- https://techgig.com/news/ai/microsoft-agent-framework-now-offers-production-runtime-for-ai-agents/132847132 (وقت تشغيل MAF الإنتاجي، Build 2026)

## الإجراء

- **مراقبة**: لا تبنّي لأي إطار الليلة؛ تُثبَّت قاعدة "التحقق من PyPI/GitHub Releases قبل قبول أي رقم إصدار أو دالة في كود الوكلاء" كقاعدة مراجعة دائمة، ويُتابَع MAF كخيار Microsoft فقط.
