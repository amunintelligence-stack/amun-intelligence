# Meta Marketing API v27.0 (4 نوفمبر 2026) — إعلانات WhatsApp Status وإيقافات

## v27.0 صدر 4 نوفمبر 2026؛ v24.0 ينتهي 10 نوفمبر (بعد 4 أيام)
- **ما الذي تغيّر:** **Marketing API v27.0** صدر **4 نوفمبر 2026** (صفحة الإصدار حُدّثت 5 نوفمبر؛ «Available until TBD»). أبرز إضافة: **إعلانات WhatsApp Status متاحة عبر Marketing API**. وv24.0 «Available until **November 10, 2026**» — أي بعد 4 أيام من هذه الدورة. للسياق: v25.0 حتى 23 فبراير 2027؛ v26.0 حتى TBD.
- **التغييرات الستة في v27.0** (تحققنا منها عبر المتصفح من سجل التغيير الرسمي):
  1. **Catalog:** إيقاف **Catalog Batch API** (POST /{catalog-id}/batch) — استخدم Catalog Items Batch API بدلًا منها (v27.0+).
  2. **Ad Sets / Reach & Frequency:** إيقاف `meta_moment_maker_spec` في v27.0+ (سيُطبَّق على كل الإصدارات عند انتهاء v26.0، التاريخ TBD). البديل: معامل `product_type` في reachfrequencypredictions لطلب Ads Burst (ADS_BURST) أو Ads Super Burst (ADS_SUPER_BURST).
  3. **Ad Sets:** «Reach more people across other mobile devices» **مفعّل افتراضيًا** في v27.0+ (سيُطبَّق على كل الإصدارات بعد ~90 يومًا، التاريخ TBD) — لمجموعات Sales المؤهلة دون إعداد جهاز صريح؛ عيّن device إلى 0 للاحتفاظ بالاستهداف المحدد. مجموعات الإعلانات الحالية بلا تغيير.
  4. **Custom Audiences:** حقول `country` و`location_spec` في `lookalike_spec` لم تعد مقبولة في v27.0+ (تُرفَض فورًا)؛ الإصدارات الأخرى تقبلها حتى نهاية نافذة 90 يومًا ثم تُرفَض على كل الإصدارات.
  5. **Ad Creative:** **Product showcase قد يُفعَّل تلقائيًا** عند إنشاء إعلانات بلا إعدادات product_extensions عندما تطابق مجموعة منتجات بثقة عالية (مثل collections تطابق رابط collections)؛ للإلغاء عيّن `product_extensions.enroll_status` إلى OPT_OUT. معاينة عبر `product_extensions/catalog_suggestions_preview`.
  6. **Lead Ads:** خيارات التحقق من الهاتف برمز OTP في نموذج العميل المحتمل: `phone_otp_verification_type` بقيم NOT_ENABLED / OTP_REQUIRED / OTP_OPTIONAL (الأخيرة لحسابات مؤهلة فقط).
- **لماذا يهم ACI:** أي مهمة تستطلع إعلانات Meta عبر API يجب أن تستهدف v26.0 أو v27.0 — **v24.0 يموت 10 نوفمبر**. ملاحظتان تحليليتان: (أ) التفعيل التلقائي لـ Product showcase يعني أن لقطات الإعلانات المرصودة قد تعرض منتجات لم يخترها المعلن صراحة — سجّل ذلك كتحيز قياس عند تحليل المواد الإبداعية؛ (ب) إعلانات WhatsApp Status مصدر إعلاني جديد كليًا للمراقبة.
- **المصادر:** https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog/version27.0 — https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog/version24.0 (فُحصا عبر المتصفح 2026-11-06)
- **الإجراء: adopt** — ثبّت v26.0 كحد أدنى لأي استدعاء Marketing API في مهام ACI؛ راقب إعلانات WhatsApp Status كمصدر جديد.
