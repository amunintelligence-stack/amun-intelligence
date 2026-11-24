# نماذج القرارات: Perplexity تخفض سعر Decision API إلى النصف + Microsoft Decision-1 (تحديث 13 أكتوبر)

## ماذا تغيّر
- **Perplexity خفّضت سعر Decision API إلى النصف**: من $0.04 إلى **$0.02 لكل مليون توكن إدخال** (أُعلن ~8 أكتوبر 2026). النموذج مفتوح الأوزان pplx-decider-v1.1-27b ما زال متاحًا للاستضافة الذاتية.
- **Microsoft دخلت سباق نماذج القرارات** بنموذج **Decision-1**: بحسب تغطية ثانوية (worthview، 12 أكتوبر) الجودة منافسة لـ GPT-6 Sol بسرعة أعلى ~14 مرة وتكلفة أقل ~200 مرة — أرقام البائع نفسه، لم تُنشر مقارنة مستقلة بعد.
- بقية المشهد كما في ملف 12 أكتوبر: OpenAI Decisions API (public beta، POST /v1/decisions، يعمل فقط على gpt-6-luna، $0.10 لكل مليون توكن إدخال والإخراج مجاني، ~10 أضعاف سرعة Responses API بحسب OpenAI، مع دعم Zero Data Retention وHIPAA للعملاء المؤهلين وإقامة بيانات US/EU)، وCloudflare Clef مفتوح الأوزان عبر AI Gateway.

## لماذا يهم ACI
- اتجاه السوق واضح: **القرارات المُهيكلة أصبحت سلعة رخيصة ومنفصلة عن التوليد النصي** — وهذا بالضبط ما تحتاجه طبقة التوجيه (routing) وبوابات التقييم (evaluator-optimizer) في وكلاء ACI المتعددين، وبوابة R0/M2 في خط إشارات التداول.
- تخفيض Perplexity إلى $0.02/M يجعل تجربة قرارات حقيقية شبه مجانية (مليون تصنيف قصير بعشرات الدولارات)، والنموذج مفتوح الأوزان يعني بديلًا ذاتي الاستضافة بلا مفاتيح مدفوعة لاحقًا.
- Microsoft Decision-1 مرشح يُراقب: إن ثبتت أرقامه، قد يكون أرخص بوابة قرارات على الإطلاق — لكن ننتظر توثيقًا رسميًا وأسعارًا معلنة.

## المصادر
- تخفيض السعر (ثانوي، نشرة 13 أكتوبر 2026): https://www.anothercodingblog.com/p/another-daily-ai-newsletter-october-13f — «Perplexity topped Hugging Face's Decision Index and halved its Decision API price to 2 cents per million input tokens».
- Microsoft Decision-1 (ثانوي، 12 أكتوبر): https://www.worthview.com/decision-models-explained-jev-vs-microsoft-decision-1-vs-openai-decisions-api/ — أرقام البائع، تحتاج تأكيدًا مستقلًا.
- تفاصيل OpenAI Decisions API (ثانوي، 7 أكتوبر): https://aiweekly.co/alerts/openai-launches-decisions-api-public-beta-on-gpt-6-luna

## الإجراء
**watch** — يُبنى على ملف 12 أكتوبر. عند أول حاجة لتوجيه LLM رخيص في ACI/التداول: قارن pplx-decider (ذاتي الاستضافة، $0.02/M عبر API) مع OpenAI Decisions ($0.10/M) وDecision-1 عند توفره رسميًا. لا اعتماد إنتاجي الآن.
