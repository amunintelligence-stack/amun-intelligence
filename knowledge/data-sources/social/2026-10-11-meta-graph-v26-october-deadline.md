# Meta Graph API: مهلة 27 أكتوبر 2026 لإزالة بروتوكولات قديمة + توسعة Creator Marketplace API (سبتمبر 2026)

- التاريخ: 2026-10-11 | الفئة: data-sources/social | الإجراء: **تبنٍّ جزئي (adopt) للمسار الجديد / مراقبة للمهلة**

## ما الذي تغيّر
1. **مهلة 27 أكتوبر 2026 (بعد 16 يومًا):** إصدار v26.0 (صدر 29 يوليو 2026) أزال خمس سلوكيات بروتوكول قديمة، وستُطبَّق على *كل* الإصدارات المدعومة بدءًا من 27 أكتوبر 2026: تجاهل معاملَي `pretty` و`debug`، تحويل طلبات `date_format` إلى خطأ، رفض `GET /?ids=...` الجذري، وإزالة سلوك `If-None-Match`/`ETag`/`304 Not Modified` بالكامل. في نفس التاريخ تُزال **Commerce Order Management API** (47 endpoint لأوامر Shops على فيسبوك/إنستغرام — بلا بديل) من كل الإصدارات. كما تم إهلاك حقول `reference_owner`/`sending_rights_holder` لصالح أنواع `RightsHolderOwner` المخصصة، وحقول صفحات قديمة (`current_location`, `genre`, `network`, `parking`, `start_info`) لصفحات New Pages Experience.
2. **توسعة Creator Marketplace API (سبتمبر 2026):** ضمن تحديث Creator Marketing Hub، أضافت Meta منشئي Facebook وInstagram إلى Creator Marketplace API، وحدّثت Messaging API، ووسّعت Content Discovery API بمحتوى عضوي عالي الأداء + بحث كلمات مفتاحية + رؤى أداء — أي بيانات صناع المحتوى والتعاون معهم أصبحت متاحة لأدوات الطرف الثالث عبر API رسمي، لا كشط فقط.
3. **انتهاء صلاحية v20.0 في 24 سبتمبر 2026** — لا تأثير مباشر علينا لكنه يحدد قاعدة الاستدعاء: أحدث إصدار هو v26.0.

## لماذا يهم ACI
لا نملك تكامل Graph API اليوم، لكن اتجاه Meta واضح: حقل "الوصول لبيانات صناع المحتوى عبر API رسمي" اتسع (Creator Marketplace + Content Discovery) — هذا مسار بيانات "نظيف" لاحقًا لو احتجنا اكتشاف/تدقيق مؤثرين لمهام الـ corporate intelligence، بدل الاعتماد على الكشط أو أدوات مدفوعة بالكامل. المهلة القريبة تُذكّر بأن أي كود Graph API مستقبلي يجب أن يلتزم بالبروتوكول الحديث (بدون `pretty`/`debug`/`date_format`/ETag).

## المصادر
- https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/ — 2026-07-29 (رسمي، Meta for Developers)
- https://developers.facebook.com/docs/graph-api/changelog/version26.0/ — رسمي (تغييرات v26.0)
- https://developers.facebook.com/docs/graph-api/changelog/versions/ — رسمي (جدول الإصدارات والانتهاءات)
- https://vafromeurope.com/2026/10/06/september-2026-social-media-digest/ — 2026-10-06 (ملخص سبتمبر، ثانوي — نقطة Creator Marketing Hub)

## الإجراء المقترح
**تبنٍّ/مراقبة** — تُضاف مدخلة Meta (Graph API / Creator Marketplace API) للـ registry كـ stub. أي تكامل مستقبلي يستهدف v26.0+ مباشرة ويلتزم بالبروتوكول الحديث؛ بيانات صناع المحتوى تُجرَّب أولًا عبر Creator Marketplace API الرسمي قبل الذهاب لحلول مدفوعة (HypeAuditor/Modash).
