# X started retiring OAuth 1.0a (2026-09-21); pay-per-use pricing remains the cost backdrop

- التاريخ: 2026-10-11 | الفئة: data-sources/social | الإجراء: **مراقبة (watch)**

## ما الذي تغيّر
بدأ X رسميًا ترحيل OAuth 1.0a في 21 سبتمبر 2026 دون تاريخ إيقاف نهائي معلن: تغيير الـ changelog بعنوان "Migrate OAuth 1.0a user tokens to OAuth 2.0 with token exchange" — أي تطبيق يحمل access token + secret قديم يستدعي `POST /2/oauth2/token` بمنحة `urn:ietf:params:oauth:grant-type:token-exchange` ويحصل على OAuth 2.0 access + refresh token بنفس الـ scopes، دون أن يُعاد تسجيل المستخدم للدخول. الـ token الجديد يتضمن دائمًا `offline.access` (نشر خلفي/مجدول). نفس التحديث أضاف دعم OAuth 2.0 لـ Account Activity API v2 مع scopes أضيق (مثل `follow.read`) بدل الوصول الشامل القديم.

ملاحظات مهمة من نفس النافذة:
- ثغرة/خلل معلن 2026-10-01 على منتدى المطورين: إعادة تشغيل الـ exchange لثاني مرة لنفس المستخدم تمسح اشتراكات الـ webhooks الخاصة به (private-event subscriptions) في Account Activity API — حتى تلك المُنشأة بالـ token الأصلي.
- سياق التسعير القائم منذ فبراير 2026: pay-per-use — إنشاء بوست نصي $0.015، بوست برابط $0.20، قراءة بوست طرف ثالث ~$0.005 لكل مورد، قراءة بيانات الحساب نفسه ~$0.001 (بعد تعديل 20 أبريل 2026)؛ طبقة الـ $200 Basic أُجبرت على pay-per-use في 1 يونيو 2026.

## لماذا يهم ACI
أي تكامل مستقبلي مع X (رصد حسابات/محتوى، إرسال تقارير، webhooks) يجب أن يُبنى على OAuth 2.0 من البداية + ميزانية pay-per-use محسوبة: قراءة محتوى طرف ثالث مكلف نسبيًا ($0.005/مورد) ويُحرق الميزانية بسرعة عند التوسع. نموذج الـ webhook/webhooks للـ Account Activity API يحمل مخاطرة عملياتية الآن (خلل المسح عند إعادة الـ exchange) — لو احتجنا webhooks لاحقًا، يُطبَّق الـ exchange مرة واحدة فقط لكل مستخدم.

## المصادر
- https://futuretweets.com/x-api-breaking-changes-oauth-1-0a-retirement-2026/ — أوائل أكتوبر 2026 (يغطي أحداث 14 سبتمبر – 1 أكتوبر 2026)
- https://docs.x.com (وثائق التسعير الرسمية المشار إليها أعلاه — تحقق مباشرة قبل أي بناء)

## الإجراء المقترح
**مراقبة** — لا نملك أي تكامل مع X اليوم. عند أول تكامل: OAuth 2.0 فقط، single-exchange policy، وحساب تكلفة قراءات الطرف الثالث (pay-per-use) في موازنة المهمة. تُضاف مدخلة X API للـ registry كـ stub بالملاحظات أدناه.
