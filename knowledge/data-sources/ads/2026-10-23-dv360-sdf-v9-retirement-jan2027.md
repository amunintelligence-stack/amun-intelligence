# Google DV360: إيقاف Structured Data Files (SDF) v9 في 28 يناير 2027

## ماذا تغيّر؟

ضمن موجة إيقافات واجهات الإعلانات (أُعلن عنها ~أكتوبر 2026): تنسيق **Structured Data Files v9** في Google Display & Video 360 سيُتقاعد في **28 يناير 2027** — بفترة إشعار تقارب 7 أشهر. أي طلبات ما زالت تُسمّي التنسيق القديم ستتلقى خطأ `400` بعد ذلك التاريخ. هذا يأتي في سياق أوسع: Google Ads API v23 يغرب في فبراير 2027، وv24 في مايو 2027.

## لماذا يهم ACI؟

- ACI لا يربط DV360 حاليًا، لكن أي خطط مستقبلية لجمع بيانات إعلانات العرض (display creatives) عبر SDF يجب أن تستهدف v10+ من البداية — التصميم على v9 يعني كسرًا مضمونًا في يناير 2027.
- مثال حي على قاعدة عامة: Google/Meta يمنحان مهلة ~6–12 شهرًا للإيقافات، ثم يكسرون الصمت (requests تفشل بـ 400/404 دون تحذير لاحق) — سجّل هذا النمط في سياسات ACI للتعامل مع إصدارات الـ APIs.

## مصادر (مع التواريخ)

- PPC Land — Explaining sunset (API) (~2026-10-13): https://ppc.land/sunset-api/
- Google Ads Developer Blog — release/sunset schedule 2026–2027 (أكتوبر 2026): http://googleadsdeveloper.blogspot.com/
- Search Engine Land — Google Ads API moves to twice-monthly releases starting with v26 (2026-10-13): https://searchengineland.com/google-ads-api-moves-to-twice-monthly-releases-starting-with-v26-495545

## الإجراء المقترح: راقب

لا إجراء فوري (DV360 غير موصول). عند تصميم أي موصّل مستقبلي لبيانات الإعلانات المصوّرة، ثبّت أحدث إصدار SDF وتابع جدول الإيقافات الرسمي.

> الثقة: متوسطة (مصدر ثانوي؛ وثائق DV360 الرسمية لم تُفتح مباشرة)
