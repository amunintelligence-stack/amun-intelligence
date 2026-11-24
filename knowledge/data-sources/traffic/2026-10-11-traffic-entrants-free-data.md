# لاعبون جدد وتغيّرات الوصول المجاني + تنبيه: إيقاف Google Custom Search JSON API في 2027-01-01

- التاريخ: 2026-10-11 | الفئة: data-sources/traffic | الإجراء: **مراقبة (watch)**

## ما الذي تغيّر
- **30 سبتمبر 2026**: منصة **SEOApp** أطلقت **SERP Sensor** مع تتبع أصلي (native) لـ Google AI Overviews داخل صفحات النتائج — تتبع يومي للكلمات والعبارات الكاملة وتنبيهات التقلب، **مشمول في الاشتراكات القياسية** (ليس إضافة مدفوعة). (أداة rank/SERP أكثر منها traffic estimator، لكنها لاعب جديد في قياس الرؤية.)
- **أكتوبر 2026**: إطلاق **Flowsery** — منصة تحليلات ويب privacy-first (بدون كوكيز، متوافقة GDPR/CCPA) مع **REST API ودعم MCP**، وطبقة مجانية 5,000 event/شهر بدون بطاقة. ملاحظة صريحة: هذه تحليلات **لمواقعك أنت** (تحتاج تثبيت سكريبت)، ليست بيانات ترافيك للمنافسين — قيمتها لـ ACI كنمط تصميم (MCP-native analytics) لا كمصدر بيانات.
- **21 سبتمبر 2026**: SpeedyIndex فتحت استطلاعًا لعملائها حول منتجات SERP data الجديدة التي سيبنونها — والسبب: **Google تُوقف Custom Search JSON API نهائيًا في 1 يناير 2027** (مغلق أمام العملاء الجدد منذ 2025، والبديل الرسمي Vertex AI Search مدفوع وبشكل مختلف). البدائل المتداولة: Brave Search API وserper.dev وExa/Tavily، ومشاريع توافقية مثل cse-compat.
- **ما لم يتغير**: لم نجد في نافذة الـ 30 يومًا أي طبقة مجانية جديدة لبيانات ترافيك المنافسين (Similarweb/Ahrefs/Semrush ما زالت مدفوعة بالكامل للـ API)، ولا تغييرات جديدة في Semrush Traffic Analytics خلال سبتمبر–أكتوبر 2026 (قنوات AI Traffic وGoogle AI Mode أُطلقت في نوفمبر 2025 — خارج النافذة).

## لماذا يهم ACI
- إيقاف Google CSE JSON API في 2027-01-01 يؤثر على أي pipeline في ACI يعتمد على `customsearch/v1` لبيانات SERP/البحث — البدء المبكر في الترحيل (Brave/serper/Exa/Tavily) أرخص من الترحيل تحت الضغط.
- SEOApp تُظهر أن تتبع AI Overviews أصبح ميزة قياسية لا premium — توقّع مماثل من كل مزودي الترافيك.

## المصادر
- https://markets.financialcontent.com/bpas/article/newsfile-2026-9-30-seo-app-launches-serp-sensor-to-monitor-ai-overviews — 30 سبتمبر 2026
- https://news.harbingertimes.com/story/643294/flowsery-launches-as-the-best-google-analytics-alternative-for-privacyfirst-teams-in-2026.html — أكتوبر 2026
- https://markets.financialcontent.com/stocks/article/accwirecq-2026-9-21-speedyindex-asks-customers-which-serp-data-to-build-as-google-custom-search-api-nears-shutdown — 21 سبتمبر 2026
- https://developers.google.com/custom-search/v1/overview — توثيق Google الرسمي (الإيقاف 2027-01-01، مغلق للجدد)
- https://github.com/langroid/langroid/releases/tag/0.67.6 — ~سبتمبر 2026 (إيقاف GoogleSearchTool لنفس السبب)

## الإجراء المقترح
**مراقبة** — وخطوة عملية واحدة: راجع أي اعتماد حالي أو مخطط على Google Custom Search JSON API داخل ACI (backend أو سكريبتات) وحدد بديله (Brave/serper/Exa/Tavily) قبل نهاية 2026.
