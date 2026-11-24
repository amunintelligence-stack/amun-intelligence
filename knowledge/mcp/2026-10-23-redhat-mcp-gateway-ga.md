# Red Hat MCP Gateway — وصول GA ودعم متزامن لأربع نسخ من بروتوكول MCP (16 أكتوبر 2026)

## ماذا تغيّر؟
- أعلنت Red Hat في 16 أكتوبر 2026 أن **MCP Gateway على Red Hat OpenShift أصبح متاحًا عامًا (Generally Available)** — بوابة على مستوى Envoy لفدرلة MCP servers وتوجيهها.
- البوابة تدعم **أربع نسخ بروتوكول على endpoint واحد مع التفاوض لكل عميل**: `2025-03-26` و`2025-06-18` و`2025-11-25` و`2026-07-28` (الـ stateless الجديدة). المسار `/mcp` يتفاوض تلقائيًا، ومسار `/mcp/stateful` المخصص يجبر النسخ القديمة.
- التسجيل يتم عبر CRD جديد `MCPServerRegistration` (مثل `apiVersion: mcp.kuadrant.io/v1`) مع category وhint لأغراض الاكتشاف.
- بالتوازي: OpenShift AI 3.4 يضيف **MCP catalog / lifecycle operator** (Technology Preview) — متجر حوكمي لاكتشاف ونشر وترقية خوادم MCP داخل الكلاستر، مع خطط لـ supply-chain controls وtrust tiers وauditability كاملة لمكالمات الأدوات.

## لماذا يهم ACI؟
- ACI لا يشغّل MCP في الإنتاج اليوم، لكن اتجاهنا المعلن هو استيعاب MCP servers لمصادر OSINT وربط n8n بها. بوابة مؤسسية بهذه المواصفات هي **النموذج الذي يجب أن ننسخه عندما نتبنى MCP**: نقطة عبور واحدة تفاوض نسخ البروتوكول، وسياسات موحدة، وسجل تدقيق لكل مكالمة أداة — بدل أن يتصل كل عميل بكل خادم مباشرة.
- نقطة تشغيلية مهمة: التفاوض الصامت للأسفل (silent fallback) قد يعطّل ميزات أمان تعتمد عليها خوادم أحدث (مثل typed output validation) — نفس التحذير الذي ورد في تقرير telegra.ph (22 أكتوبر): سجّل `protocolVersion` الفعلية التي يرد بها الخادم لا المطلوبة.
- نحن لسنا على OpenShift، لكن الفكرة قابلة للتنفيذ خفيفًا (gateway صغير يوحّد الوصول ويفرض allowlist) قبل التفكير في أي حل مؤسسي.

## مصادر (مع التواريخ)
- redhat.com — "Model Context Protocol gateway for Red Hat OpenShift is now generally available" (16 أكتوبر 2026): https://www.redhat.com/en/blog/model-context-protocol-gateway-red-hat-openshift-now-generally-available
- telegra.ph — "Three MCP protocol versions are live at once. Here is how to see which one a server really speaks" (22 أكتوبر 2026): https://telegra.ph/Three-MCP-protocol-versions-are-live-at-once-Here-is-how-to-see-which-one-a-server-really-speaks-10-22
- redhat.com — "The MCP catalog is here: Discover, deploy, and connect on Red Hat OpenShift AI" (updated 8 سبتمبر 2026): https://www.redhat.com/en/blog/mcp-catalog-here-discover-deploy-and-connect-red-hat-openshift-ai

## الإجراء المقترح: راقب
لا تبنِّ الآن (نحن لسنا على OpenShift ولا نشغّل MCP إنتاجيًا)، لكن اعتمد مبدأه التصميمي: عندما نتبنى MCP في ACI، الوصول يكون عبر بوابة واحدة مسجّلة ومدققة بدل اتصالات مباشرة متفرقة، مع تسجيل نسخة البروتوكول الفعلية لكل خادم.

> الثقة: عالية
