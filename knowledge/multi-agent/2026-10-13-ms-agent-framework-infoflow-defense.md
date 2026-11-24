# Microsoft Agent Framework: دفاع Information-Flow Control ضد prompt injection في الـ core

## ماذا تغيّر
- صفحة الـ **upgrade / significant-changes بتاعة Microsoft Agent Framework (بايثون 2026)** سجّلت تغيير جديد في `agent-framework-core`: **آلية Information-Flow Control** للمساعدة في الدفاع ضد هجمات **prompt injection** (الـ PR المرجعي: microsoft/agent-framework رقم 5331). الفكرة: تتبّع تدفّق المعلومات بين البيانات "الغير موثوقة" (مخرجات التولز، محتوى خارجي) والتعليمات، بدل الاعتماد على الفلترة النصية بس.
- في نفس حزمة التغييرات المهمة:
  - **إنفاذ `approval_mode`** على الـ function tools في وكلاء Claude وGitHub Copilot (اتساق مع باقي التطبيقات) — يعني أي تول حساس بيمر على بوابة موافقة بشرية بشكل إجباري مش اختياري.
  - دعم **`allowed_tools`** في اختيار الأدوات (tool choice) لوكلاء OpenAI وGemini — تقييد صريح لمجموعة الأدوات اللي الموديل مسموح له يندهها في run معيّن.
  - (سياق الإصدارات: بايثون 1.19.0 في 18 سبتمبر، و1.20.0→1.21.0 اتسجّلت في دورة 12 أكتوبر — التغييرات دي جزء من خط التطوير النشط.)
- توازيًا، مقال dev.to «Python for Agentic AI: LangGraph vs CrewAI vs MAF» (آخر سبتمبر) بيؤكد إن مايكروسوفت وحّدت AutoGen + Semantic Kernel تحت MAF (GA في 3 أبريل 2026) وإن prompt flow هيتقاعد في أبريل 2027 بمسار هجرة رسمي لـ Agent Framework — يعني MAF بقى المرجع المؤسسي للـ orchestration عند مايكروسوفت.

## لماذا يهم ACI
- ACI مش بيستخدم Microsoft Agent Framework (الـ orchestrator بتاعنا Python خاص بأنماط chaining/routing/parallel/evaluator-optimizer) — فالإجراء مش "نقل للفريمورك".
- القيمة في **استعارة النمط**: الـ evaluator-optimizer loop بتاعنا بياخد مخرجات تولز خارجية (whois, DNS, صفحات ويب) وبيحكم عليها — دي بالظبط سطح هجوم prompt injection. الـ information-flow control (تمييز بيانات غير موثوقة عن تعليمات، وتتبّع التلوّث عبر المراحل) هو التطبيق العملي لمبدأ "evidence-judged verdicts" اللي اتسجّل في دورة 11 أكتوبر.
- `allowed_tools` per-run و`approval_mode` الإجباري هما النسخة المؤسسية من قاعدتين عندنا: أقل صلاحيات لكل وكيل، ولا إجراء خارجي irreversible من غير موافقة بشر (CSOC playbook principles، 11 أكتوبر).

## المصادر
- microsoftdocs/semantic-kernel-docs — agent-framework/support/upgrade/python-2026-significant-changes.md (محدّثة ~2 أكتوبر 2026): https://github.com/microsoftdocs/semantic-kernel-docs/blob/HEAD/agent-framework/support/upgrade/python-2026-significant-changes.md
- microsoft/agent-framework — release dotnet-1.22.0 (18 سبتمبر 2026، سياق الإصدارات): https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.22.0
- dev.to — «Python for Agentic AI: LangGraph vs CrewAI vs MAF» (سبتمبر 2026): https://dev.to/shaam_ai/python-for-agentic-ai-langgraph-vs-crewai-vs-maf-4od0

## الإجراء
**watch** — لا تبنّي للفريمورك، لكن عند بناء مرحلة evaluator-optimizer في ACI: صمّم الـ verdict pipeline على مبدأ تتبّع مصدر البيانات (taint tracking خفيف: مخرجات التولز = غير موثوقة، لا تُعامل كتعليمات)، وقيّد أدوات كل وكيل لكل run. أضف النمط ده لـ ARCHITECTURE.md مع مبادئ 11 أكتوبر.
