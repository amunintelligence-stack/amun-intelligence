# Google Ads API — إلغاء developer tokens نهائيًا (9 سبتمبر 2026)
- التاريخ: 2026-10-10 | الفئة: data-sources/ads | الإجراء: **اعتماد**

## ما الذي تغيّر
- **9 سبتمبر 2026**: Google ألغت **developer tokens** من Google Ads API نهائيًا — الـ access أصبح مرتبطًا بـ **Google Cloud project** بمستويات: Test / Explorer / Basic / Standard.
- هيدر `developer-token` أصبح اختياريًا ويُتجاهَل؛ سيُرفَض في major version قادمة غير مسماة.
- لم يعد MCC account مطلوبًا للحصول على API access؛ التقديم من Google Cloud Console (صفحة Google Ads API).
- الـ quota أصبح per Cloud project بدل per token؛ Basic Access approval أصبح آليًا (مراجعة خلال دقائق)؛ كل طلبات Basic المعلقة أُغلقت ويجب إعادة التقديم.
- **23 سبتمبر 2026**: Google Ads API **v25.2** أضاف peer rankings للـ agency reporting (مقارنة الإنفاق والنشاط مع الأقران).

## لماذا يهم ACI
- أي connector لـ Google Ads في ACI يجب أن يُبنى على النموذج الجديد: **Google Cloud project + OAuth (adwords scope)** — لا developer token. هذا يبسط الـ onboarding (لا حاجة لـ MCC).
- ملاحظة: Ads Transparency Center ما زال **بلا API رسمي** — الـ scraping عبر RPC الداخلي فقط، ويبقى خارج الـ ToS. v25.2 peer rankings مفيدة لتحليل المنافسين عبر API الرسمي.

## المصادر
- https://ppc.land/google-drops-developer-tokens-from-ads-api-access-decisions/ — 2026-09-10
- https://github.com/helpcode-ai/anythingmcp/blob/HEAD/content/guides/en/google-ads-api-without-developer-token.mdx — 2026-09-27
- https://www.techwyse.com/news/platform-updates/google-ads-api-v25-2-competitive-rankings-agency-reporting — 2026-09-23

## الإجراء المقترح
**اعتماد** — وثّق نموذج الـ auth الجديد في registry: Google Cloud project (Basic/Standard access) + OAuth، بدون developer token. المفتاح المطلوب: Google Cloud project مع Google Ads API مفعّلة.
