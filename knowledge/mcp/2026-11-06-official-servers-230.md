# خوادم MCP الرسمية v2.3.0 — ضوابط تشغيل دقيقة (4 نوفمبر 2026)

## v2.3.0 (4 نوفمبر 2026) — filesystem للقراءة فقط، fetch بقائمة مضيفين مسموحين
- **ما الذي تغيّر:** وُسمت خوادم MCP الرسمية **v2.3.0** في 4 نوفمبر 2026 (تحققنا من GitHub Releases API). الضوابط الجديدة كلها اختيارية (opt-in) ولا تغيّر السلوك السابق عند حذفها:
  - **filesystem** (`@modelcontextprotocol/server-filesystem` 2.2.0): علامة `--read-only` جديدة — الخادم يرفض الكتابة بالكامل.
  - **fetch** (`mcp-server-fetch` 2026.11.4): إدخالات `--allowed-hosts` قابلة للتكرار (قائمة سماح للمضيفين) + مهلة طلب HTTP قابلة للتكوين.
  - **git** (`mcp-server-git` 2026.11.4): أداة `git_merge` جديدة — دمج على الفرع الحالي، fast-forward فقط افتراضيًا.
  - نُشرت أيضًا: server-everything 2.2.1، server-memory 2.1.0، server-sequential-thinking 2.1.1، mcp-server-time 2026.11.4.
  - تحذير إصدارات: الوسم v2.3.0 لا يعني أن كل حزمة تحمل 2.3.0 — تحقق من إصدار الحزمة المثبَّتة فعلًا.
- **لماذا يهم ACI:** هذه بالضبط ضوابط التقوية التي يحتاجها أي تعريض MCP في ACI: filesystem للقراءة فقط + fetch بقائمة مضيفين هما نمطا التصميم الواجب نسخهما حرفيًا لأي خادم MCP يقرأ أدلة الأدلة أو يجلب URLs. `git_merge` fast-forward فقط نموذج لعمليات كتابة آمنة.
- **المصادر:** https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0 — https://forkast.news/understanding-the-v2-3-0-mcp-server-release-and-its-granular-controls/ (2026-11-05)
- **الإجراء: adopt** — سجّل `--read-only` + `--allowed-hosts` كمتطلبات تصميم إلزامية في أي خادم MCP مستقبلي لـ ACI؛ لا تعتمد v2.3.0 نفسها إلا عند الحاجة.

## خوادم MCP من المورّدين لفرق التسويق — مرجع مصادر بيانات (2 نوفمبر 2026)
- **ما الذي تغيّر:** مراجعة موثّقة (21 صفحة مورّد، قُرئت 5 نوفمبر) لـ 13 خادم MCP **يصونها المورّد نفسه**: Google Analytics (9 أدوات للقراءة فقط)، Google Ads (نقطة نهاية مستضافة في تجربة بقائمة سماح)، Meta ads (بيتا مفتوحة منذ 29 أبريل 2026)، HubSpot (GA)، Salesforce (GA)، Shopify Dev MCP، Semrush (جديد)، Ahrefs (خطط مدفوعة من Lite). ثلاثة GA، واحد بيتا مفتوحة، اثنان للقراءة فقط بالتصميم. لا خادم Google Search Console من Google نفسها — مشاريع مجتمع فقط.
- **لماذا يهم ACI:** هذه خريطة طريق جاهزة لمصادر بيانات الإعلانات/الحركة في ACI عبر MCP بدل تجريف غير مستقر — Meta ads وSemrush وAhrefs وGoogle Analytics كلها مصادر تتبَّعها ACI أصلًا في data-sources.
- **المصادر:** https://www.digitalapplied.com/blog/official-mcp-servers-for-marketing-teams (2026-11-02)
- **الإجراء: watch** — عند تقييم أي مصدر إعلانات عبر MCP، ابدأ بخادم المورّد الرسمي لا بخادم مجتمع.

## Craft CMS 5.12 — MCP في النواة (3 نوفمبر 2026)؛ إشارة منظومة فقط
- **ما الذي تغيّر:** Craft CMS 5.12 (3 نوفمبر) يشحن MCP في النواة بثلاثة خوادم (HTTP موثّق بـ OAuth + 2FA + شاشة موافقة؛ HTTP عام للمحتوى المعتمد فقط؛ stdio محلي) و68 أداة. Strapi 5.49 جعل خادم MCP المدمج GA على كل الخطط.
- **لماذا يهم ACI:** إشارة انتشار: MCP في نواة أنظمة إدارة المحتوى يعني أن مصادر محتوى الويب المستهدفة في المهام ستكشف واجهات MCP رسمية أكثر فأكثر.
- **المصادر:** https://dev.to/aimeos/best-mcp-cms-2026-11-cms-with-model-context-protocol-compared-1lfj
- **الإجراء: ignore**
