# Meta Marketing/Graph API — غروب v24.0 وكسر v26.0 يطبَّق على كل النسخ 27 أكتوبر
- التاريخ: 2026-10-10 | الفئة: data-sources/ads | الإجراء: **مراقبة**

## ما الذي تغيّر
- **6 أكتوبر 2026**: غروب Marketing API **v24.0** — الاستدعاءات القديمة تُنفَّذ بصمت كـ v25.0 بدل أن تفشل.
- **27 أكتوبر 2026**: تغييرات v26.0 الكاسرة تُطبَّق على **كل النسخ المدعومة** (الـ pin لا يحمي):
  - إزالة `daily_outcomes_curve` و`budget_guardrail` و`estimate_dau` من Delivery Estimate endpoints (لا بديل).
  - تغييرات `messenger_positions` / story — القيم المكتوبة قد تُسقَط بصمت.
- تغييرات access tiers: "Ads Management Standard Access" → "Marketing API Access Tier" (Limited/Full)، وخفض عتبة الـ auto-approval إلى 500 call في 15 يومًا.

## لماذا يهم ACI
- موصل Meta Ad Library في ACI يستخدم Graph API — أي قراءة لـ delivery estimates أو حقول إعلانية يجب أن تُراجَع قبل 27 أكتوبر، والحل الوحيد الموثوق هو التحقق من الـ responses الحية لا الـ fixtures.
- الـ auto-approval المخفَّض (500 calls/15 days) يسهّل الحصول على API access لمشاريع جديدة.

## المصادر
- https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/ — 2026-07-29
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog — تم الوصول 2026-10-10
- https://dev.to/driftsignal/on-october-27-metas-ad-api-stops-returning-three-delivery-estimate-fields-pinning-your-version-4d62 — 2026-10-01

## الإجراء المقترح
**مراقبة** — راجع أي كود يقرأ delivery estimates قبل 27 أكتوبر 2026؛ خلاف ذلك لا إجراء.
