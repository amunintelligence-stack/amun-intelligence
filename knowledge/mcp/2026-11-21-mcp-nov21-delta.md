# دلتا MCP — FastMCP 4.2.4 يغلق ثغرة OAuth (GHSA-78c8-3jhx-5mg7)؛ ارفع التثبيت؛ Skills over MCP تستقر (21 نوفمبر 2026)

## 1. FastMCP 4.2.4 «Burn After Reading» (20 نوفمبر 2026) — إصلاح أمني

- **ما الذي تغيّر:** يصلح سباقًا يمكّن طلبَي رمز متزامنين من استرداد رمز تفويض OAuth proxy أو رمز تحديث مرتين (GHSA-78c8-3jhx-5mg7)، ويمنع رمز وصول proxy مُلغى من التحقق مجددًا بعد التحديث.
- **لماذا يهم ACI:** التثبيت في السجل كان ‎>=4.1.8‏ مع 4.2.0 «تقييم مرحلي» — الآن 4.2.4 هو الحد الأدنى؛ أي خادم MCP مستقبلي في ACI يجب أن يُبنى على ‎>=4.2.4‏.
- **المصادر:** https://gofastmcp.com/docs/updates (صفحة التحديثات الرسمية)
- **الإجراء: adopt** — ارفع التثبيت إلى ‎>=4.2.4‏.

## 2. سلسلة 4.2.0–4.2.3: Skills over MCP + Python 3.11+

- **ما الذي تغيّر:** ‏4.2.0 «Mad Skills» (13 نوفمبر):‏ Skill كائن عادي يخدمه الخادم (SkillCatalogProvider / SkillsDirectoryProvider)، مع تحقق العميل من الحجم والبصمة؛ Python ‏≥3.11‏ (3.10 خارج)؛ واجهة skills في 4.1 مهملة وتُزال في 4.3؛ تبعيات Annotated. ‏4.2.1‏ (17 نوفمبر) تصحيح أمني/صحة؛ ‏4.2.2‏ (18 نوفمبر) اكتشاف skills لعملاء الأدوات فقط؛ ‏4.2.3‏ (20 نوفمبر) تتبع parent_task_spans + إصلاحات مخطط الإخراج. ‏VS Code 1.146‏ يقرأ skills من خادم MCP مباشرة (معاينة، خلف `chat.agentHost.mcpSkills.enabled`).
- **لماذا يهم ACI:** شكل التغليف المرشح لشخصيات/مسرحيات المحلل في ACI ‏(SEP-2640)‏ — الخادم مصدر واحد للحقيقة للمهارة بدل نسخة لكل وكيل؛ التقييم في dev قبل أي اعتماد.
- **المصادر:** https://www.prefect.io/blog/fastmcp-4-2-skills-over-mcp (13 نوفمبر 2026)؛ https://modelcontextprotocol.info/blog/fastmcp-4-2-skills-over-mcp/ ؛ https://gofastmcp.com/docs/updates
- **الإجراء: watch** — تقييم مرحلي في dev على 4.2.4؛ لا تثبيت إنتاجي قبل اختبار skills.

## 3. MCP Python SDK الرسمي 2.3.0 (2 أكتوبر) ما زال الأحدث

- **ما الذي تغيّر:** تحقق 20 نوفمبر: لا إصدار أحدث.
- **المصادر:** https://fastero.com/blog/python-mcp-server (20 نوفمبر 2026)
- **الإجراء: ignore.**
