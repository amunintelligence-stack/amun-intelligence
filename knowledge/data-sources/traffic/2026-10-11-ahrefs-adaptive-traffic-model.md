# Ahrefs يحوّل نموذج تقدير الترافيك الافتراضي في الـ API إلى "Adaptive" (ضبط تلقائي لوزن AI Overviews)

- التاريخ: 2026-10-11 | الفئة: data-sources/traffic | الإجراء: **اعتماد (adopt)**

## ما الذي تغيّر
- **4 سبتمبر 2026**: Ahrefs غيّر الـ default mode لترافيك الـ Site Explorer API من **static** إلى **adaptive**. أي استدعاء API بدون تحديد المعامل يحسب الترافيك بالمعادلة الجديدة تلقائيًا. للرجوع للمعادلة القديمة يجب تمرير `traffic_mode=static` صراحة.
- النموذج الجديد **Adaptive organic traffic model** (أُطلق opt-in في 4 أغسطس 2026) يوزّع أوزان CTR منفصلة على **15 نوعًا من عناصر SERP** — من بينها صراحةً **AI Overviews** — بدل معامل تعديل عام واحد. النتيجة: نفس الترتيب (ranking) ممكن يعطي تقدير ترافيك مختلف تمامًا حسب البيئة المحيطة بالنتيجة في صفحة البحث.
- Ahrefs يقول إن النموذج يُعاد معايرته **شهريًا** باستخدام بيانات Web Analytics الحقيقية، فتأثير عناصر SERP يتطور مع تغيّر سلوك النقر الفعلي.
- معامل `traffic_mode` (قيمه `adaptive` | `static`) متاح على endpoints: Metrics، Metrics by country، Metrics history، Organic competitors، Organic keywords، Pages by traffic، Top pages.

## لماذا يهم ACI
- أي connector نبنيه لـ Ahrefs ويقرأ ترافيك (site-explorer) **ستتغير أرقامه صامتًا** بعد 4 سبتمبر إن لم نحدد `traffic_mode` صراحة — نفس الدرس من `search_volume_type` في ملف 2026-10-10. التوثيق يجب أن يثبّت القيمة المستخدمة في كل استدعاء.
- الـ adaptive model أقرب للحقيقة في عصر AI Overviews (الترتيب ≠ فرصة الترافيك)، وهذا يقوّي دقة أي تقدير ترافيك للمنافسين داخل ACI.

## المصادر
- https://netcontentseo.com/article/ahrefs-finally-adjusts-traffic-estimates-for-ai-overviews-instead-of-treating-every-serp-feature-equally-1083 — 30 سبتمبر 2026
- https://ahrefs.com/blog/new-features/ — الـ changelog الرسمي (تحديث 29 سبتمبر 2026 أبرز النموذج مجددًا)

## الإجراء المقترح
**اعتماد** — في تصميم Ahrefs connector: مرّر `traffic_mode=adaptive` صراحة (لا تعتمد على الـ default)، وسجّل القيمة في metadata كل snapshot ترافيك حتى لا تُقارن أرقام محسوبة بمعادلتين مختلفتين.
