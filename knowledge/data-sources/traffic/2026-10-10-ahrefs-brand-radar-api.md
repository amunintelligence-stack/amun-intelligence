# Ahrefs — أول Brand Radar API endpoint + AI-adjusted volume (سبتمبر 2026)
- التاريخ: 2026-10-10 | الفئة: data-sources/traffic | الإجراء: **اعتماد**

## ما الذي تغيّر
- **8 سبتمبر 2026**: أول Brand Radar API endpoint أصبح live — **AI responses** (نفس الأعمدة والفلاتر داخل التطبيق) للـ dashboards والـ pipelines والتقارير المخصصة.
- **10 سبتمبر**: Brand Radar يدعم Entities (تجميع تنويعات البراند في كيان واحد).
- **سبتمبر 2026**: تقارير AI visibility تستخدم الآن **AI adjusted volume** بدل Google search volume، مع معامل جديد `search_volume_type` في الـ API — الـ toggle للرجوع للحساب القديم يختفي بعد **30 سبتمبر 2026**.
- **2 سبتمبر**: Batch Analysis 2.0 أصبح الافتراضي (backlink metrics أغنى حتى 1,000 URL).
- Ahrefs Connect (من 19 أغسطس) أضاف OAuth integration layer على **API v3** مع extra API units للخطط المدفوعة.

## لماذا يهم ACI
- Brand Radar API يعطي ACI قياسًا مباشرًا لظهور الشركات/البراندات في إجابات الـ AI (ChatGPT, Gemini, Perplexity) — إشارة استخباراتية جديدة كليًا (share of voice في عصر الـ AI search).
- الـ `search_volume_type` الجديد يعني أي connector نبنيه يجب أن يحدد المعامل صراحة وإلا تغيّرت الأرقام بعد 30 سبتمبر.

## المصادر
- https://ahrefs.com/blog/new-features/ — changelog رسمي (8 و10 سبتمبر 2026)
- https://ahrefs.com/blog/new-features-july-august-2026/ — تفاصيل AI adjusted volume
- https://github.com/ahrefs/ahrefs-python/blob/HEAD/CHANGELOG.md — SDK البايثون

## الإجراء المقترح
**اعتماد** — عند تفعيل Ahrefs connector: استخدم API v3، حدّد `search_volume_type` صراحة، وقيّم Brand Radar "AI responses" endpoint كمصدر AI-visibility. المفتاح: API key مدفوع (units-based billing، حد أدنى 50 unit/request).
