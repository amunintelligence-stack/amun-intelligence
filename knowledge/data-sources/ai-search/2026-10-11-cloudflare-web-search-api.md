# Cloudflare Web Search API (بيتا 2 أكتوبر 2026) — أرخص مسار بحث ويب مفتاحي + دخول Ceramic.ai

- التاريخ: 2026-10-11 | الفئة: data-sources/ai-search | الإجراء: **اعتماد (adopt)** — تقييم كـ backend رئيسي رخيص لمهام البحث

## What changed
- في 2 أكتوبر 2026 (Birthday Week) أطلقت Cloudflare **Web Search API** داخل AI Gateway في open beta: بحث ويب حي لتغذية الوكلاء، عبر REST أو Workers binding، مع حد أقصى 10 نتائج للطلب وشكل موحد (title/URL/description) — تبديل المزود = معامل واحد فقط.
- **3 مزودين عند الإطلاق** بأسعار القائمة دون هامش (تُخصم من AI Gateway credits أو Bring-Your-Own-Key):
  - **Ceramic.ai** (الافتراضي) — **$0.25 لكل 1,000 طلب** — دخول جديد: فهرس خاص 40+ مليار صفحة، أوصاف حتى 8,000 حرف، Zero Data Retention = نعم.
  - **Linkup** — $5/1k (وضع fast، نتائج خام بلا إجابة مولدة)، ZDR = نعم.
  - **Exa** — $7/1k (auto)، ZDR = لا عند الإطلاق.
- زوّاد Cloudflare أيضًا **"Server Tools" قادمة** ستجعل web search أداة أصلية يستدعيها الموديل بنفسه دون تعريف tool-calling يدويًا (لم تُطلق بعد).
- سياق الأسعار (مقارنة Digital Applied، قراءة 3 أكتوبر 2026 لكل 1,000 بحث): Ceramic $0.25 ← الأرخص بفارق؛ Parallel fast وPerplexity Fast $1؛ Brave $5؛ Exa $7؛ Tavily basic $8؛ OpenAI/Anthropic web search $10 (+توكنات)؛ Gemini grounding $14.

## Why it matters for ACI
- هذا أرخص مسار **مفتاحي** لبحث الويب وُجد حتى الآن ($0.25/1k = ربع سعر Perplexity Fast)، بسطح فوترة ولوغات موحد مع مكالمات الموديلات — مثالي لمهام ACI التي تجري مئات/آلاف الاستعلامات (مراقبة شركات، تتبع أخبار، جمع روابط للتحليل).
- Ceramic.ai نفسها دخيلة جديدة بفهرس خاص — بديل محتمل لـ Brave/Serper كمزود مستقل لاحقًا.
- BYOK يعني لو محمد عنده مفتاح Exa أو Linkup، تُدار من نفس الواجهة.

## Sources (links with dates)
- https://saascity.io/blog/cloudflare-web-search-api-ai-agents-2026 — ~2026-10-05 (تفاصيل الإطلاق: المزودون الثلاثة، الأسعار، BYOK، ZDR)
- https://www.digitalapplied.com/blog/web-search-apis-for-ai-agents-compared-2026 — 2026-10-02/03 (جدول مقارنة 15 مسار بحث للوكلاء)
- https://dev.to/ashraf_chowdury09/cloudflare-just-shipped-a-web-search-api-for-ai-agents-heres-what-the-hype-skips-1cg0 — ~2026-10-06 (مثال curl + Workers binding)
- https://blog.cloudflare.com/tag/ai-gateway/ — 2026-10-02 (إعلان Cloudflare الرسمي: Introducing Web Search API via AI Gateway)

## Action (adopt / watch / ignore — one concrete recommendation)
**اعتماد** — تقييم Web Search API (Ceramic tier) كـ backend البحث الافتراضي لمهام ACI التي تحتاج بحث ويب حي بكميات كبيرة؛ مقارنة جودة النتائج مع Brave (ألفا 2,000 مجانية/شهر) قبل الاعتماد النهائي.
