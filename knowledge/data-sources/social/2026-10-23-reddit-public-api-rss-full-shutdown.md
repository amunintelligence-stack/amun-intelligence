# ⚠️ Reddit يغلق الوصول العام لـ Data API نهائيًا في مارس 2027 ويوقف RSS في 13 نوفمبر (2026-09-30)

## ماذا تغيّر؟

أعلن Reddit في 30 سبتمبر 2026 (عبر منشوري r/modnews وr/redditdev، وغطّته TechCrunch في اليوم نفسه) إغلاقًا مرحليًا كاملًا لواجهتي القراءة المجانية:

- **31 أكتوبر 2026:** التوقف عن قبول طلبات وصول جديدة للـ Data API العامة (مذكور في تقرير أكتوبر — هذا التحديث يضيف بقية الجدول الزمني).
- **10 نوفمبر 2026:** تحديث عن تقدم الترحيل وتذكير بالمواعيد.
- **13 نوفمبر 2026:** إيقاف دعم RSS feeds نهائيًا على مستوى الموقع — Reddit: «لا يوجد بديل» لمن يستخدم RSS خارج المجتمعات التي يشرف عليها.
- **30 نوفمبر 2026:** إغلاق التسجيل في برنامج الترحيل ($1M fund — ألف دولار لكل تطبيق مؤهل يُرحّل بنجاح).
- **12 يناير 2027:** بدء قطع الوصول عن التطبيقات والمستخدمين غير المسجّلين.
- **23 فبراير 2027:** تذكير أخير بالمواعيد.
- **مارس 2027:** إغلاق كامل لما تبقى من الوصول العام للـ Data API — استثناءات فقط للشركاء بعقود مكتوبة (مثل Google وOpenAI).
- **Old Reddit:** يُحصر في المشرفين والمستخدمين النشطين فيه خلال آخر 6 أشهر (تسجيل الدخول إلزامي أصلًا).
- بديل Reddit الرسمي هو Devvit (منصة المطوّرين الخاصة به) — وتعمل فقط بـ TypeScript؛ Python «ليس على خارطة الطريق حاليًا» حسب تقارير صحفية. أكثر من 14,000 تطبيق وبوت سجّلوا للترحيل حتى 30 سبتمبر.

## لماذا يهم ACI؟

- **مصدر رصد اجتماعي يموت:** أي قدرة في ACI تقرأ Reddit (مراقبة العلامات التجارية، رصد الإشاعات/التسريبات، تحليل المشاعر) ستفقد قناتين مجانيتين/بدون مفتاح: RSS (نوفمبر) ثم الـ Data API (مارس 2027). البقاء يتطلب اتفاقية تجارية أو الترحيل إلى Devvit بـ TypeScript.
- التكلفة والتعقيد يتحولان من keyless إلى keyed/commercial — قرار معماري يجب اتخاذه الآن وليس في مارس.
- «Reddit for Researchers» عبر Google BigQuery Analytics Hub يبقى متاحًا للمشاريع الأكاديمية المعتمدة — خيار بحثي وليس تشغيليًا.

## مصادر (مع التواريخ)

- PPC Land — Reddit to halt public Data API access in March 2027 as 14,000 apps register (2026-09-30): https://ppc.land/reddit-to-halt-public-data-api-access-in-march-2027-as-14-000-apps-register/
- MediaNama — Reddit to shut RSS feeds, close public API as bots scrape its data (2026-10-01): https://www.medianama.com/2026/10/223-reddit-rss-feeds-public-api-bots/
- Shelly Palmer — Reddit Tightens Access to its Data (2026-10-01): https://shellypalmer.com/2026/10/reddit-tightens-access-to-its-data/
- Startup Fortune — Reddit is cutting off free API and RSS access while keeping Google and OpenAI paying (2026-10-05): https://startupfortune.com/reddit-is-cutting-off-free-api-and-rss-access-while-keeping-google-and-openai-paying/
- Digital Applied — Reddit Ends RSS and Its Public API: Deadlines for AI Tools (2026-10-01): https://www.digitalapplied.com/blog/reddit-api-rss-shutdown-ai-tools-deadlines

## الإجراء المقترح: تبنَّ

أوقف أي اعتماد تشغيلي على RSS لـ Reddit فورًا (يموت 13 نوفمبر)، وسجّل أي تطبيق Reddit لدينا قبل 12 يناير 2027، وافتح قرارًا صريحًا: اتفاقية تجارية مع Reddit أم التخلي عن Reddit كمصدر مستمر في المissions أم الترحيل إلى Devvit (TypeScript). لا تُبنِ خطط جمع جديدة على الـ Data API المجانية بعد مارس 2027.

> الثقة: عالية
