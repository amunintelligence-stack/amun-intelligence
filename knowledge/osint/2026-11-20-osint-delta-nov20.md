# دلتا OSINT — KEV: 4 إضافات 18 نوفمبر (منها LiteLLM) + 4 إضافات 20 نوفمبر؛ nmap 7.993 حُسم أخيرًا؛ مرشحون جدد من تصنيف iThub (20 نوفمبر 2026)

## ⭐ 1. CISA KEV — 4 إضافات في 18 نوفمبر + 4 إضافات في 20 نوفمبر (إجمالي 1,786)

- **ما الذي تغيّر:** أضافت CISA إلى كتالوج الثغرات المستغَلة (KEV) **4 ثغرات في 18 نوفمبر** و**4 أخرى في 20 نوفمبر** (موعد الإصلاح الفيدرالي للأخيرة 23 نوفمبر 2026):
  - 18 نوفمبر: **CVE-2026-40217** — BerriAI LiteLLM (8.8، هروب sandbox في `/guardrails/test_custom_code`، استغلال نشط لـLLMjacking، الموعد 2 ديسمبر)؛ **CVE-2024-10441** — Synology DSM (9.8، يُستغل لنشر فدية C3RB3R)؛ **CVE-2026-90436** — Apache Axis 1.x (9.8، انعكاس غير آمن → تنفيذ كود، البرنامج منتهي الدعم)؛ **CVE-2026-90817** — REDCap (9.8، حقن كود عبر رابط استبيان عام).
  - 20 نوفمبر: **CVE-2026-129448** — Apache Roller؛ **CVE-2026-123890** — Broadcom VMware vCenter؛ **CVE-2025-42884** — SAP NetWeaver؛ **CVE-2026-76466** — Cisco Expressway.
- **لماذا يهم ACI:**‏ **LiteLLM هو الوحيد الذي يمس المكدّس مباشرة** (بروكسي 3a2l على Narmer) — لكن إضافته إلى KEV مغطاة منذ 18 نوفمبر وبانتظار تحقق الإصدار عند تشغيل Narmer التالي؛ الجديد الليلة هو **تأكيد الاستغلال النشط (LLMjacking)** لا ثغرة جديدة. الثغرات الأربع في 20 نوفمبر لا تمس المكدّس (لا VMware/SAP/Cisco/Roller عندنا) — مادة تغذية استخبارية فقط.
- **المصادر:** https://www.scworld.com/brief/cisa-adds-four-critical-vulnerabilities-to-known-exploited-catalog (20 نوفمبر 2026)؛ https://www.reconbee.com/cisa-warns-of-4-exploited-flaws-linked-to-ransomware-cryptomining-and-llmjacking-attacks/ (20 نوفمبر 2026)؛ https://www.pentestlab.wiki/cve (إضافات 20 نوفمبر)؛ https://www.immunitysec.com/vulnerabilities/kev/statistics/ (الإجمالي 1,786 حتى 20 نوفمبر — متزامن بفارق ساعات عن إضافات 20 نوفمبر)
- **الإجراء: watch** — لا تنبيه جديد في المحادثة (LiteLLM مغطى منذ 18 نوفمبر)؛ أضِف الثغرات الأربع الجديدة إلى تغذية KEV في قوالب الفرز.

## 2. nmap 7.993 — حُسم التعارض: nmap.org هو المصدر الصحيح، ووسوم GitHub متأخرة

- **ما الذي تغيّر:** قراءة مباشرة من **https://nmap.org/changelog.html** الليلة (فُحص 20 نوفمبر 2026): **Nmap 7.993 [2026-10-23]** على رأس السجل — يصلح تراجعًا منع معظم سكربتات فئة version من العمل، ويرفع Npcap إلى 1.90. وسوم GitHub ما زالت عند **v7.992** (لا وسم 7.993) — الوسوم متأخرة عن الإصدار الرسمي، وليس العكس.
- **لماذا يهم ACI:**‏ يغلق لغز 19 نوفمبر نهائيًا: **7.993 هو الأحدث**، والمصدر الموثوق هو nmap.org لا وسوم GitHub. التثبيت في السجل (7.993) مؤكد.
- **المصادر:** https://nmap.org/changelog.html (فُحص 20 نوفمبر 2026)؛ GitHub API (nmap/nmap tags، فُحص 20 نوفمبر 2026)
- **الإجراء: adopt** — عند نافذة تحديث الأدوات التالية: nmap 7.993 (الفحص نفسه ما زال عبر portscan.py).

## 3. Sherlock v0.16.2 مؤكد الأحدث عبر GitHub API — ادعاء ثانوي خاطئ عن v0.14.3

- **ما الذي تغيّر:** GitHub API الليلة: **sherlock-project/sherlock latest = v0.16.2** (كما في السجل). ملف CSG Cyber School يدّعي «v0.14.3 Released: 2026-11-01» — **خاطئ**: لا يوجد إصدار 0.14.3 في نوفمبر، والتاريخ يطابق آخر commit لا إصدارًا.
- **لماذا يهم ACI:**‏ تذكير منهجي: أدلة الأدوات الثانوية تخطئ في أرقام الإصدارات؛ **GitHub API هو المصدر الوحيد لأرقام الإصدارات** في هذه الدورة.
- **المصادر:** GitHub API (sherlock-project/sherlock releases/latest، فُحص 20 نوفمبر 2026)؛ https://csgcyberschool.org/tools/sherlock
- **الإجراء: ignore** — لا تغيير؛ لا تبنِ معلومة إصدار على CSG.

## 4. تصنيف iThub لأدوات OSINT مفتوحة المصدر (16 نوفمبر) — 5 مرشحين جدد ليسوا في السجل

- **ما الذي تغيّر:** دليل iThub «Best Open-Source OSINT Tools in 2026» (حدّث 16 نوفمبر 2026) يصنّف 11 أداة حسب المهمة، منها **5 ليست في سجل ACI**: **TgWitness** (التقاط محادثات Telegram كدليل قابل للتحقق)، **VoidAccess** (استخبارات تهديدات من الويب المظلم)، **World Monitor** (لوحة أخبار وإشارات حية، طرفية أيضًا)، **God's Eye View** (كرة أرضية حية: رحلات/سفن/أقمار/كاميرات)، **X-osint** (قائمة طرفية مجمّعة لعمليات بحث سريعة). الباقي مغطى: theHarvester (4.11.1، commits حتى 13 نوفمبر)، Sherlock، Web-Check، SpiderFoot، sn0int، Blackbird.
- **لماذا يهم ACI:**‏ **TgWitness** يملأ فجوة حقيقية: التقاط أدلة Telegram بسلسلة حفظ — خطوة «احفظ الدليل» في مهام ACI بلا أداة مخصصة اليوم. **VoidAccess** يملأ فجوة الويب المظلم (خارج نطاق ACI حاليًا لكنه مصدر تهديدات). World Monitor وGod's Eye View لوحات وعي ظرفي — أولوية منخفضة.
- **المصادر:** https://www.ithub.directory/blog/best-open-source-osint-tools (16 نوفمبر 2026)
- **الإجراء: watch** — أضِف TgWitness وVoidAccess إلى السجل بحالة eval؛ جرّب TgWitness على قناة تجريبية وقارن مخرجاته مع لقطات يدوية قبل أي اعتماد. World Monitor وGod's Eye View وX-osint: سجّل كمرجع فقط.

## بلا تغيير — تحقق الليلة (GitHub API)

- **theHarvester 4.11.1** (3 يونيو) ما زال الأحدث؛ commits على main حتى 13 نوفمبر؛ لا إصدار جديد.
- **Maigret v0.6.6** (18 سبتمبر) ما زال الأحدث.
- **subfinder v2.17.0** (8 أكتوبر)، **Amass v5.1.3** (25 أكتوبر)، **dnsrecon 1.6.3** (28 يونيو) — كلها ما زالت الأحدث (مغطاة أمس، لم تُعَد الليلة).
- **nuclei-templates v10.5.2** (12 نوفمبر) ما زال الأحدث (مغطى أمس).
