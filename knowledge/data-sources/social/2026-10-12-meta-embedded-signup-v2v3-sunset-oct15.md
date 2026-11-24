# Meta: إيقاف التسجيل المدمج (embedded signup) v2 وv3 في 15 أكتوبر 2026
## ماذا تغيّر
- في **15 أكتوبر 2026** (بعد 3 أيام) توقف Meta نهائيًا عن دعم embedded signup **v2 وv3**؛ الترقية إلى **v4** إلزامية.
- أنواع الميزات التالية تتوقف عن العمل: `only_waba_sharing` و`marketing_messages_lite` و`coex` — أي تدفقات onboarding لـ WhatsApp Business API المبنية عليها ستنكسر.
- السياق الأوسع: ضمن سلسلة تشديدات Meta على المطورين في أكتوبر 2026 — في **27 أكتوبر 2026** تُطبَّق قيود Graph API v26 (إزالة سلوكيات البروتوكول القديمة: `pretty` و`debug` و`date_format` و`GET /?ids=` وETag/304) على **كل الإصدارات المدعومة** وليس v26 فقط، وإزالة حقول تقدير التسليم الإعلاني الثلاثة من كل إصدارات Marketing API.
## لماذا يهم ACI
- ACI لا يستخدم embedded signup حاليًا، لكن أي تكامل مستقبلي مع WhatsApp Business (قناة استخبارات أو إشعارات) يجب أن يُبنى على v4 من اليوم الأول.
- موعد 27 أكتوبر: تدقيق سريع لأي استدعاءات Graph API نستخدمها (أدوات السوشيال) للتأكد من عدم الاعتماد على السلوكيات القديمة المزالة.
## المصادر
- ppc.land (إعلان الترحيل، مايو 2026): https://ppc.land/metas-embedded-signup-v4-is-here-but-the-october-15-clock-is-ticking/
- إعلان Graph API v26.0 — Meta Developers (29 يوليو 2026): https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/
## الإجراء
**watch** — لا تأثير مباشر على الـ stack الحالي؛ التزم بـ v4 في أي تكامل WhatsApp مستقبلي، ودقق استدعاءات Graph API قبل 27 أكتوبر.
