# سيرفرات MCP جديدة للـ OSINT: osint-mcp-server 0.2.0 و OSINT Toolbox MCP

## ماذا تغيّر
- **osint-mcp-server 0.2.0** (الحزمة على PyPI، مُرفوعة **26 سبتمبر 2026**؛ المستودع: robyroro/osint-mcp، رخصة MIT): سيرفر MCP خفيف مبني على الـ SDK الرسمي، بيدي أدوات `domain_whois` (عبر RDAP، ملاحظة: بعض الـ ccTLDs زي `.ro` و`.de` معندهاش RDAP عام) — الـ README بيوثّق إن الـ HTTP calls معمولها mock في التستات، وفيه تعليمات تجربة بـ MCP inspector. ملاحظة المؤلف الصريحة: للاستخدام على أهدافك أنت أو bug bounty ضمن النطاق — مش للاستهداف الشخصي.
- **OSINT Toolbox MCP** (renkagod/osint-toolbox-mcp، PyPI `osint-toolbox-mcp 1.0.1`): بيجمع **12 أداة OSINT** تحت سيرفر واحد — Sherlock وMaigret وBlackbird (usernames)، Holehe وGHunt (emails)، theHarvester وSpiderFoot وsubfinder وdnsrecon وdnstwist (domains)، PhoneInfoga (phones)، ExifTool (metadata) — بالإضافة لـ WHOIS وDNS وcrt.sh وWayback lookups المدمجة (17 تول MCP إجمالًا). **من غير API keys خالص**؛ بيتثبت بـ `uvx` (بيستخدم الأدوات المثبتة عندك) أو بـ Docker image فيها كل الأدوات (ماعدا Blackbird). اتضاف مؤخرًا للقائمة المُنسَّقة soxoj/awesome-osint-mcp-servers (الـ README اتحدّث 10 أيام فاتت).
- (تنقيح: Voidly censorship MCP ظهر في نفس القوائم لكن تبين إنه من ~5 شهور مش جديد، اتستبعد.)

## لماذا يهم ACI
- الـ ACI registry فيه بالفعل ScanMalware وClearfront وContrastAPI وn8n-mcp وOpenOSINT كمرشحين للـ MCP — الاتنين دول **خفيفين ومن غير keys**، ومناسبين جدًا لفكرة إن وكلاء ACI يندهوا أدوات OSINT جاهزة من غير ما نكتب تول لكل CLI.
- **OSINT Toolbox MCP** تحديدًا بيغلّف نفس الأدوات اللي عندنا في الـ venv (sherlock, maigret, theHarvester, subfinder, dnsrecon...) — بدل ما ACI يعمل wrapper لكل واحدة، سيرفر واحد يقدمهم كـ MCP tools جاهزة للـ agents.
- تحفظ أمني: أي سيرفر MCP بيشتغل local processes (خاصةً Docker/uvx بينده CLIs) **لازم يتقيّم في عزلة الأول** — ده نفس التوصية اللي اتسجلت لـ OpenOSINT وn8n-mcp (فحص tool descriptions ضد tool-poisoning، وتقييد الصلاحيات).

## المصادر
- PyPI — osint-mcp-server (ريليز 0.2.0، 26 سبتمبر 2026): https://pypi.org/project/osint-mcp-server/
- PyPI — osint-toolbox-mcp (1.0.1): https://pypi.org/project/osint-toolbox-mcp/1.0.1/
- soxoj/awesome-osint-mcp-servers — README (محدّث ~10 أيام، فيه الإدخالات بالتفاصيل): https://github.com/soxoj/awesome-osint-mcp-servers/blob/HEAD/README.md
- مستودع robyroro/osint-mcp (مذكور في وثائق PyPI).

## الإجراء
**watch** — مرشحان للتقييم (eval) في بيئة معزولة عند أول نافذة لتجربة سيرفرات MCP محلية. OSINT Toolbox MCP (renkagod) أولوية أعلى لأنه بيغطّي أدواتنا الحالية كلها من غير keys. لا تثبيت ولا تغيير في الخدمات دلوقتي — بس التقييم المعزول لاحقًا.
