# بحث ذكاء اصطناعي — Perplexity Decider v1.3 (Locate)؛ Multiagent اليوم؛ Gemini Decisions API؛ Gemini 4 Hydrogen في بحث Google (17 نوفمبر 2026)

## ⭐ 1. Perplexity Decider v1.3 — استخراج نص حرفي (Locate) وأوزان مفتوحة (12 نوفمبر 2026)

- **ما الذي تغيّر:** أصدرت Perplexity في **12 نوفمبر 2026** نموذجي **Decider v1.3** و**Decider Flash v1.3** مع ميزة **Locate** الجديدة: تعيد النص المطابق حرفيًا مع مواضع بداية ونهاية الأحرف — لمهام التعرف على الكيانات المسماة (NER) وكشف المعلومات الشخصية (PII) والأسئلة الاستخراجية؛ وبلا مطابقة تعيد قائمة فارغة. الأوزان **قابلة للتنزيل برخصة Apache-2.0**: Decider v1.3 على عمود Qwen3.8-27B (~49 GiB BF16) وFlash على Qwen3.5-4B (~8.5 GiB). الدقة المعلنة: **91.6% متوسط عبر 63 مهمة تصنيف**، بزيادة 6.54 نقطة مئوية عن مصنّفات الإنتاج. المخرجات الأخرى رقمية: احتمالات لأسئلة نعم/لا أو خيارات مخصصة أو درجات مرتبة بدل نثر مولّد. متاحان عبر OpenRouter وDecisions API. **التسعير:** $0.02 لكل مليون رمز إدخال (Decider) و$0.01 (Flash)، بلا رسوم رموز إخراج. تنبيه منهجي: في Flash، `fast=True` يعطّل Locate؛ وLocate نص فقط وبحد 128 سؤال Locate لكل طلب.
- **لماذا يهم ACI:**‏ هذا أقوى مرشح عملي حتى الآن لثلاث مهام ACI: **تصنيف الأدلة** (نعم/لا/درجة بدل نثر)، **كشف PII** في المستندات المجمّعة قبل التخزين، و**استخراج نص حرفي موثّق بالمواضع** للاقتباس في التقارير. Flash صغير بما يكفي للتشغيل المحلي (8.5 GiB) — يلائم قاعدة ACI «البيانات الحساسة لا تغادر».
- **المصادر:** https://www.unite.ai/perplexity-releases-decider-v1-3-models-with-text-span-extraction/ (12 نوفمبر 2026)؛ https://www.ai-primer.com/engineer/stories/perplexity-decider-v13-release؛ https://www.artiverse.ca/perplexitys-new-decider-models-turn-text-into-clear-decisions/
- **الإجراء: watch** — قيّم Decider Flash محليًا لتصنيف الأدلة وكشف PII في مهمة تجريبية؛ ثبّت النموذج والسعر صراحةً في أي استدعاء Decisions API (لا تعتمد على افتراضات).

## 2. Perplexity Multiagent — تنسيق حتى 16 وكيلًا (17 نوفمبر 2026، Max فقط)

- **ما الذي تغيّر:** أطلقت Perplexity اليوم **17 نوفمبر 2026** وضع **Multiagent** في Computer: قائد Claude Fable 5.2 يوزع العمل على حتى 16 وكيلًا داعمًا عبر Claude Opus 5.5 وGPT 6.1 Sol وGemini 4 Carbon، مع تحقق متقاطع قبل رد واحد. **متاح لمشتركي Max فقط ($200/شهر)، على الويب.** التفاصيل الكاملة للنمط في ملف `multi-agent/2026-11-17-framework-delta-nov17.md`.
- **لماذا يهم ACI:**‏ مرجع نمطي (تحقق متقاطع متعدد النماذج) لا منتج يُعتمد؛ لا API للتنسيق.
- **المصادر:** https://www.unite.ai/perplexity-launches-multiagent-to-coordinate-frontier-ai-models/ (17 نوفمبر 2026)
- **الإجراء: watch** — مرجع نمطي فقط.

## 3. نماذج القرار تتكاثر — Gemini Decisions API من DeepMind؛ وGemini 4 Hydrogen في بحث Google لكل المستخدمين (12 نوفمبر)

- **ما الذي تغيّر:** أطلقت **Google DeepMind Gemini Decisions API** (أُعلن يوم أربعاء — 11 نوفمبر حسب السياق): نموذج **Gemini Decision 1** يجيب حتى **1,000 سؤال عن نفس المادة في تمريرة واحدة**. وفي السياق: OpenAI عمّمت Decisions API في 22 أكتوبر؛ Amazon أصدرت Strands Decider 2B في أكتوبر (Qwen3.5-based، يعمل على CPU/GPU). وبالتوازي: **Gemini 4 Hydrogen وصل إلى بحث Google لكل المستخدمين في 12 نوفمبر 2026** — أي أن نموذجًا جديدًا يجيب الآن عن استعلامات بحث حقيقية، فيؤثر على ما يراه أي جامع يعتمد على نتائج Google.
- **لماذا يهم ACI:**‏ سباق نماذج القرار (Perplexity/OpenAI/Google/Amazon) يعني أن «القرارات الاحتمالية» أصبحت سلعة API رخيصة — بوابة E1 في ACI يمكن أن تستدعي نموذج قرار بدل حكم نموذج توليدي. وHydrogen في بحث Google يعني أن نتائج بحث Google نفسها تتغير (نموذج جديد يلخّص) — أي مقارنة تاريخية لنتائج بحث يجب أن تسجّل تاريخ 12 نوفمبر كنقطة انقطاع.
- **المصادر:** https://www.artiverse.ca/perplexitys-new-decider-models-turn-text-into-clear-decisions/ (Gemini Decisions API)؛ https://www.hubstudio.ai/resources/insights/ai-news-google-core-update-november-2026 (Gemini 4 Hydrogen في بحث Google، 12 نوفمبر)
- **الإجراء: watch** — سجّل 12 نوفمبر كنقطة انقطاع في سجلات بحث Google؛ قارن عروض نماذج القرار الأربعة قبل أي اعتماد.

## بلا تغيير — تحقق الليلة

- **Perplexity Agent API**: دعم Gemini 4 Hydrogen (14 نوفمبر) وافتراضي 128K رمز إخراج (12 نوفمبر) مغطيان في ملف الأمس؛ بلا إضافات الليلة.
- **Perplexity Decisions API**: التأسيس الأرضي الحي (4 نوفمبر — الدقة 56.4% ← 97.3% في التحقق من الحقائق) مغطى سابقًا؛ بلا جديد.
- **Genspark / You.com / Exa / Tavily / Brave**: بلا إعلانات جديدة الليلة.
- **Perplexity Computer**: Teammates أُطلقت 5 نوفمبر (Max)؛ بلا جديد الليلة.
