# Tines: تحديثات أكتوبر 2026 — إصدار 44.0.0 ذاتي الاستضافة + موصلات بحث ويب جديدة + هجرة سجل OCI (2026-10-23)

## ماذا تغيّر؟
- **Self-hosted Release 44.0.0** (أكتوبر 2026): يزيل نهائيًا كود هجرة الـrecords القديمة — إلزامية التحقق من اكتمال الهجرة قبل الترقية (عدم رؤية شارات "migration in progress" شرط).
- **50 تحديثًا في Tines 3B** (أكتوبر): أبرزها — GPT-6.1 Sol كخيار نموذج للموفر الافتراضي، Chat مع voice mode، دعم مستندات Word عبر Chat، API لـbillable usage عبر `/billable_usage`.
- **موصلات جديدة** (Connector updates): **Linkup، Nimble، Octen، You.com** كموصلات بحث ويب — ذات صلة مباشرة بـai-search في ACI؛ وMiniMax وInception وLiquid AI كموصلات/مزودي ذكاء.
- **هجرة سجل الحاويات**: من 15 يناير 2027 الصور الجديدة تُنشر فقط على `oci.tines.com`؛ الوصول إلى `registry.tines.com` وDocker Hub ينتهي **1 مارس 2027**.
- إعلان توظيف 100 وظيفة (Boston) وتثبيت التقييم $1.1B (جولة Series C من فبراير 2025 — ليس تمويلًا جديدًا).

## لماذا يهم ACI؟
Tines منافس مرجعي لـn8n في عالم SOAR؛ ACI لا يستخدمه. القيمة هنا:
1. **موصلات البحث Linkup/Nimble/Octen/You.com** — مرشحات data-source جديدة لطبقة ai-search لدينا (تقييم مستقل لكل API لاحقًا).
2. **نمط هجرة سجل الحاويات** — درس تشغيلي: نحن نخطط لـDocker لـ3a2l/Hermes مستقبلًا؛ توثيق نمط OCI migration مفيد.
3. **Release 44.0.0 كدرس «كيفية عدم كسر الترقيات الذاتية الاستضافة»** — قائمة تحقق ما قبل الترقية (migration banners) نمط يمكن تبنيه في إجراءات ترقية n8n لدينا.

## مصادر (مع التواريخ)
- Tines — Tines 3B product updates | Tines — October 2026 (مصدر رسمي أولي): https://www.tines.com/3b/product-updates/
- Tines Docs — Release notes: self-hosted 44.0.0 (مصدر رسمي أولي): https://www.tines.com/stories/docs/self-hosted/release-notes/
- tech-insider.org — Tines to Add 100 Jobs; $1.1B Valuation Holds From 2025 (2026-10-22): https://tech-insider.org/ie/tines-100-jobs-1-1-billion-valuation-2026/

## الإجراء المقترح: راقب
موصلات البحث الجديدة تُقيَّم كـdata sources مستقلة لاحقًا؛ لا تغيير على stack الحالي.

> الثقة: عالية
