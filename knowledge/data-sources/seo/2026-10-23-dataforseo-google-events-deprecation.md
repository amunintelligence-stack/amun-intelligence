# DataForSEO: إيقاف Google Events SERP API (2026-09-15) وحقول جديدة لمنتجات AI Mode (أكتوبر 2026)

## ماذا تغيّر؟

نشرت DataForSEO في أكتوبر 2026 سلسلة تحديثات على SERP API (المصدر الأساسي: dataforseo.com/updates):

1. **إيقاف Google Events SERP API:** اعتبارًا من **15 سبتمبر 2026** أصبح Google Events deprecated كنوع محرك بحث مستقل — لأن Google أزالت Events كتبويب بحث منفصل. أي استعلامات للـ Events API ستتوقف عن الإرجاع.
2. **حقول جديدة لتوصيات التسوق في Google AI Mode SERP API:** حقلان جديدان يوفران وصفًا نصيًا للمنتجات ومحتوى Markdown، بجانب الأسعار والتقييمات.
3. **Popular Products وHotel Packs:** حقولا تجميع (grouping fields) جديدان في Google Organic SERP API لتحليل e-commerce والفنادق بدقة أعلى.
4. **مصفوفة checks جديدة للنتائج العضوية:** `checks` array يدرج خصائص النتيجة العضوية (صور/فيديو/إشارات أمان...) بشكل قابل للتوسع بدل حقول متفرقة.
5. **تغيير عمق Local Finder:** Google Places تعيد الآن حتى 10 نتائج لكل صفحة على سطح المكتب (نزولًا من 20) — عدّل أي منطق pagination يفترض 20.

## لماذا يهم ACI؟

- DataForSEO من مزوّدي SERP المرشّحين لجمع بيانات SEO/التجارة في ACI (keyed، pay-as-you-go). أي كود يقرأ Google Events API **مكسور الآن** — إصلاح عاجل إذا كان لدينا اعتماد.
- حقول AI Mode/Popular Products تفتح قدرة جديدة: مراقبة ظهور المنتجات/العلامات التجارية داخل Google AI Mode وAI Overviews — مباشرة ذات صلة بذكاء المنافسة (corporate intel)، لا مجرد SEO.
- تغيير بنية `checks` يعني تحديث parsers قبل أن تتعطل المعالجة الصامتة.

## مصادر (مع التواريخ)

- DataForSEO — SERP API updates category, primary changelog (أكتوبر 2026): https://dataforseo.com/updates/category/serp-api
- DataForSEO — Deprecation of Google Events SERP API (سبتمبر 2026، ساري من 2026-09-15): مذكور في نفس صفحة التحديثات أعلاه
- Built For SEO — Changelog surfacing DataForSEO AI Overview presence/ads detection (2026-10): https://docs.builtforseo.com/changelog

## الإجراء المقترح: تبنَّ

أزل أي استعلامات Google Events SERP API من خطوط ACI، وحدّث parsers للاستفادة من حقول `checks` وحقول التسوق في AI Mode، وعدّل pagination في Local Finder إلى 10. قيّم حقول AI Mode كقناة رصد لظهور الكيانات التجارية في إجابات Google.

> الثقة: عالية
