# خوادم MCP رسمية للإعلانات: TikTok for Business وX + شبكة إعلانات TikTok الأمريكية (أكتوبر 2026)

- التاريخ: 2026-10-11 | الفئة: data-sources/ads | الإجراء: **مراقبة (watch)**

## What changed
(1) في Advertising Week New York (أوائل أكتوبر 2026) أعلنت TikTok أن خادم «TikTok for Business MCP» أصبح موصلًا على عدة منصات وسجلات AI: Claude وKimi وManus وPerplexity وReplit وSnowflake وTencent WorkBuddy وسجل IAB Tech Lab للوكلاء. الخادم (`business-api.tiktok.com/open_mcp/tt-ads-mcp-flat`) ظهر أول مرة في TikTok World في 13 مايو 2026، وTikTok تقول إن عدد المعلنين المستخدمين له في تفعيل/إدارة الحملات ارتفع أكثر من 200% بين يوليو وسبتمبر 2026 (بيانات داخلية بلا رقم أساس معلن). في يوليو كان هناك «Agentic Hub» فوقه مع مهارات جاهزة (تقارير، اكتشاف جمهور، تحسين ميزانية) من شركاء مثل HubSpot وWix — إعلان أكتوبر لم يذكره. (2) X تشغّل خادم MCP رسميًا مستضافًا على `api.x.com/mcp` يغطي الإعلانات وسطح الـ API (موثق في مقال dev.to، ~سبتمبر 2026). (3) السياق العام: Amazon فتحت واجهات إعلاناتها للوكلاء عبر MCP في فبراير 2026، وMeta أصدرت موصلات إعلانية لـ Claude/ChatGPT (~نهاية أبريل) ثم فتحت ads MCP لأي تطبيق في يوليو — أي أن MCP أصبح البروتوكول المعياري لربط الوكلاء بمنصات الإعلانات. (4) في نفس الحزمة: TikTok فتحت «TikTok Ad Network» (TTAN، الاسم السابق Pangle) لمعلني الولايات المتحدة — شبكة ~400 ألف تطبيق خارج تجربة TikTok الأساسية، مدمجة في Ads Manager. ملاحظة هيكلية مهمة من تغطية PPC Land (يناير 2026): الشبكة تقع **خارج** مشروع TikTok الأمريكي المشترك (ByteDance تحتفظ بـ 19.9%)، أي أن بياناتها خارج كيان الولايات المتحدة.

## Why it matters for ACI
تحذير مهم قبل أي حماس: هذه الخوادم تكشف **حساب المعلن الخاص** (إدارة حملاته وتقاريره) وليست مكتبات شفافية للمنافسين — لا تحل محل Ad Library في استخبارات المنافسين. قيمتها لـ ACI في اتجاهين: (أ) طبقة إدارة برمجية لحساباتنا الإعلانية الخاصة مستقبلًا، (ب) إشارة معمارية: أي تكامل «وكيل ↔ إعلانات» نبنيه يجب أن يتكلم MCP أولًا لأنه أصبح المعيار. معلومة TTAN/الهيكل الأمريكي مفيدة عند تفسير مصدر بيانات إعلانات TikTok (داخل/خارج الكيان الأمريكي).

## Sources (links with dates)
- https://ppc.land/tiktok-opens-ad-network-of-nearly-400-000-apps-to-us-advertisers/ — 6 أكتوبر 2026
- https://www.thekeyword.co/news/tiktok-agentic-hub-ai-skills — يوليو 2026 (Agentic Hub والمهارات)
- https://dev.to/rupa_tiwari_dd308948d710f/mcp-agent-use-cases-8-ai-agents-you-can-build-by-role-4c91 — ~15 سبتمبر 2026 (خادم X الرسمي api.x.com/mcp)
- https://www.geekmetaverse.com/tiktok-unveils-ai-shopping-assistant-and-ad-tools-at-advertising-week/ — ~7 أكتوبر 2026 (حزمة الإعلانات الكاملة)

## Action (adopt / watch / ignore — one concrete recommendation)
**watch** — سجّل نقاط النهاية في السجل (TikTok for Business MCP وX MCP) كخيارات مستقبلية لإدارة حساباتنا الإعلانية الخاصة عبر الوكلاء، مع ملاحظة صريحة أنها **لا** توفر بيانات إعلانات المنافسين — لا تبنِ عليها أي جمع استخباري تنافسي.
