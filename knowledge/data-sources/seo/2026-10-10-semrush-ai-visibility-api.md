# Semrush — ظهور AI Visibility API ("Serenity") في البرية (سبتمبر 2026)
- التاريخ: 2026-10-10 | الفئة: data-sources/seo | الإجراء: **مراقبة**

## ما الذي تغيّر
- **9 سبتمبر 2026**: changelog مشروع Adobe spacecat-api-service (v1.800.0) سجّل دعم "sermush serenity api access for S2S consumers" — أول دليل عام على وجود **Semrush Serenity API** (واجهة AI-search visibility) متاحة للاستهلاك server-to-server.
- بالتوازي: Semrush AI Visibility Toolkit (2026) يقيس الظهور في ChatGPT/Gemini/Perplexity/Copilot عبر GraphQL API (حسب مقارنات سبتمبر 2026: ~5k calls/day rate limit، add-on مدفوع).
- ملاحظة access model: Semrush API يتطلب Business tier + purchased units (10 req/s على Trends) — لا وصول مجاني حقيقي.

## لماذا يهم ACI
- مكافئ Semrush لـ Ahrefs Brand Radar: قياس share-of-voice في إجابات الـ AI — إشارة استخباراتية متماثلة. وجود API رسمي (Serenity) يعني إمكانية connector نظيف بدل scraping.
- لكن الـ access model مكلف (Business tier) مقارنة بـ Ahrefs — الاختيار بينهما قرار تكلفة.

## المصادر
- https://github.com/adobe/spacecat-api-service/blob/HEAD/CHANGELOG.md — v1.800.0 (2026-09-09)
- https://salpseo.ai/blog/ahrefs-brand-radar-vs-semrush-ai-visibility-toolkit-2026-3595 — سبتمبر 2026
- https://www.devx.com/uncategorized/best-seo-api-production/ — 2026-09-04 (access models)

## الإجراء المقترح
**مراقبة** — لا اعتماد حتى تتضح وثائق Serenity API الرسمية وشروط الوصول؛ قارن تكلفته مع Ahrefs Brand Radar عند تفعيل أي منهما.
