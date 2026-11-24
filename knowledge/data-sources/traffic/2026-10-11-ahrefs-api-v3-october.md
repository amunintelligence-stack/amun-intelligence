# Ahrefs API v3 — إضافات أكتوبر 2026 (Rank Tracker competitor metrics + Site Audit Page Explorer)

- التاريخ: 2026-10-11 | الفئة: data-sources/traffic | الإجراء: **اعتماد (adopt)**

## ما الذي تغيّر
من الـ changelog الرسمي لـ Ahrefs خلال أواخر سبتمبر وأكتوبر 2026:
- **10 أكتوبر**: endpoint جديد في API v3 لـ **Rank Tracker competitor metrics** — يكشف Share of Voice وtraffic وposition stats للمنافسين المتتبَّعين برمجيًا (فلاتر على مستوى الكلمة المفتاحية قادمة قريبًا).
- **3 أكتوبر**: endpoint جديد **Site Audit Page Explorer** — الوصول لحقول الـ crawl ومقارنة الـ snapshots وربطه مع Issues endpoint.
- **30 سبتمبر**: فلتر **spam** أصبح مدعومًا عبر كل backlink endpoints في الـ API (استبعاد الروابط منخفضة الجودة في الـ dashboards والـ pipelines).
- **29 سبتمبر**: تقرير Top Pages في Site Explorer حصل على **shared filter presets** وعمود **UR** (URL Rating) — في الواجهة وعبر الـ API.
- **19 سبتمبر**: مخطط branded vs non-branded traffic في Site Explorer يقسّم الآن النقرات ذات العلامة إلى "Your brand" مقابل "Other brands".
- ملاحظة: بنود Brand Radar في نفس الفترة (Brand Performance chart، شراء الـ indexes منفردة) **مستثناة عمدًا** — مغطاة في ملف 2026-10-10-ahrefs-brand-radar-api.md.

## لماذا يهم ACI
- Rank Tracker competitor metrics endpoint يعطي ACI مصدرًا برمجيًا مباشرًا لمقارنة الترافيك والـ Share of Voice بين الشركات المستهدفة — يكمّل تقديرات Site Explorer للترافيك العضوي.
- فلتر الـ spam وعمود UR يحسّنان جودة أي تحليل backlink-to-traffic نبنيه.

## المصادر
- https://ahrefs.com/blog/new-features/ — الـ changelog الرسمي (بنود 19 سبتمبر – 10 أكتوبر 2026)
- https://github.com/0xenzyme/awesome-seo-articles/blob/HEAD/ahrefs-blog/product-blog/new-features.md — أرشيف مرآة للـ changelog الرسمي (فُحص 2026-10-11؛ نسخة الموقع الرسمي هي المرجع)

## الإجراء المقترح
**اعتماد** — أضف Rank Tracker competitor metrics endpoint إلى مخطط Ahrefs connector في tools.yaml (Share of Voice + traffic + positions للمنافسين)، وثبّت استخدام فلتر الـ spam افتراضيًا في أي استعلام backlink.
