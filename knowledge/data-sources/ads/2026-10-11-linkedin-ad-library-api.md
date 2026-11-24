# LinkedIn Ad Library: واجهة REST رسمية موجودة لكنها مقيّدة بالمراجعة (فجوة في السجل)

- التاريخ: 2026-10-11 | الفئة: data-sources/ads | الإجراء: **اعتماد/تقييم (adopt — اطلب الوصول وقيّم)**

## What changed
ليست «خبرًا عاجلًا» بقدر ما هي اكتشاف موثق حديثًا (يوليو 2026) يملأ فجوة في سجلنا — كان الاعتقاد الشائع أن مكتبة LinkedIn بلا API: (1) يوجد منتج رسمي باسم **«Ad Library API»** في LinkedIn Developer Portal (منفصل عن منتج Advertising API) — تُنشئ تطبيق مطوّر، تطلب المنتج من تبويب Products، والطلب **يخضع لمراجعة LinkedIn** (ليست موافقة فورية). (2) نقطة النهاية: `GET https://api.linkedin.com/rest/adLibrary` كـ Rest.li finder مع `q=criteria` وفلاتر مثل `keyword` و`advertiser`؛ الترويسات المطلوبة: `Authorization: Bearer` و`X-RestLi-Protocol-Version: 2.0.0` وترويسة `Linkedin-Version` شهرية بصيغة YYYYMM (غيابها = خطأ). (3) التغطية: إعلانات معروضة بعد 1 يونيو 2023، عالميًا، وتُحفظ سنة واحدة بعد آخر ظهور؛ إعلانات الاتحاد الأوروبي تحمل نطاقات انطباعات ومعايير الاستهداف المفصح عنها؛ **لا يوجد إنفاق ولا CTR ولا تحويلات**؛ الصفحات محدودة بـ 25 إعلانًا. (4) تحذيرات عملية موثقة: صفحة توثيق LinkedIn الرسمية للمنتج تُرجع 404، وعميل Python الرسمي يُرجع 404 على نفس الطلب الذي ينجح كـ cURL خام — ابنِ الاستدعاءات يدويًا ولا تعتمد على الـ wrappers، واعتبر Developer Portal مصدر الحقيقة. (5) للمقارنة: واجهة الويب مجانية بلا تسجيل وتعرض هوية المعلن واسم الدافع والدولة وتواريخ التشغيل لكل إعلان.

## Why it matters for ACI
LinkedIn هي منصة إعلانات B2B الأولى — واستخبارات الشركات (ACI) معنية أساسًا بالكيانات التجارية، فمكتبة إعلاناتها مصدر منافسين مباشر لم نغطّه إطلاقًا في السجل. الـ API الرسمي يعطي بيانات منظمة (إبداعي، صيغة، تواريخ، استهداف الاتحاد الأوروبي) لبحث المنافسين آليًا. كلفة الدخول: تطبيق مطوّر + مراجعة (أيام)، بلا رسوم معلنة.

## Sources (links with dates)
- http://zenabm.com/blog/linkedin-ads-library-api — ~يوليو 2026 (توثيق المنتج + نقطة النهاية + مشكلة 404)
- https://affroom.com/blog/how-to-use-linkedin-ads-library/ — ~يونيو 2026 (تغطية واجهة الويب: بلا API عام، نافذة سنة واحدة، بيانات الاتحاد الأوروبي)
- https://github.com/southleft/linkedin-mcp/blob/HEAD/README.md — مارس 2026 (منتج «Ad Library API» في Developer Portal يتطلب مراجعة)
- https://github.com/zernio-dev/zernio-php/blob/HEAD/docs/Api/AdLibraryApi.md — محدّث أوائل أكتوبر 2026 (حدود الصفحات 25 + حقول التغطية)

## Action (adopt / watch / ignore — one concrete recommendation)
**adopt** — اطلب منتج «Ad Library API» لتطبيق ACI في LinkedIn Developer Portal الآن (المراجعة تستغرق أيامًا)، وقيّم الاستدعاء اليدوي لـ `GET /rest/adLibrary` كموصل استخبارات إعلانات B2B — مع ملاحظة أن بيانات الإنفاق/الأداء غير متاحة أصلًا في المصدر.
