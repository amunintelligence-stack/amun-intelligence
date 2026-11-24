# Splunk: إصلاح 24 ثغرة في 21 أكتوبر — 4 حرجة تشمل SOAR 8.7.0 (2026-10-23)

## ماذا تغيّر؟
نشرت Splunk في **2026-10-21** ثلاثة نشرات أمنية تغطي **24 ثغرة** في Splunk Enterprise وSplunk SOAR، بينها **أربع ثغرات حرجة** (CVSS من 9.3 إلى 9.9):
- **CVE-2026-76531** (9.9، CWE-552) — Splunk SOAR: ملفات/مجلدات مكشوفة لأطراف خارجية (Exposed Dangerous File).
- **CVE-2026-76407** (9.3، CWE-284) — Splunk SOAR: خلل في التحكم بالوصول.
- **CVE-2026-76299** (9.9، CWE-284) — Splunk Enterprise: تحكم وصول غير سليم.
- **CVE-2026-76302** (9.9، CWE-707) — Splunk Enterprise: تحييد غير سليم للمدخلات.
- الثغرات الثماني في SOAR **مصلّحة في الإصدار 8.7.0** (الذي غطّيناه في 2026-10-10) — النشرة الأمنية هي الإعلان الرسمي المتأخر عن الإصلاحات.
- باقي الثغرات: تحقق ضعيف من مسارات URL، معالجة مدخلات غير آمنة، ضوابط موارد ضعيفة، وحرمان من الخدمة.

## لماذا يهم ACI؟
ACI لا يشغّل Splunk SOAR — **لا تأثير تشغيلي مباشر** علينا. لكن كمرجع SOAR: الخبر يؤكد نمط «الإصدار يحمل الإصلاحات قبل النشرة الرسمية» عند Splunk، ويعطينا مقياس مقارنة لنضج إدارة الثغرات عند اختيار منصة SOAR مرجعية لاحقًا (Splunk SOAR مقابل Shuffle/Tines).

## مصادر (مع التواريخ)
- Cryptika — Splunk Fixes 24 Security Flaws, Including Four Critical Vulnerabilities in Enterprise and SOAR (نُشر ~2026-10-22، يغطي نشرات 2026-10-21): https://www.cryptika.com/splunk-fixes-24-security-flaws-including-four-critical-vulnerabilities-in-enterprise-and-soar/

## الإجراء المقترح: تجاهل (غير مؤثر)
ليست في stack لدينا. تُحفظ كمرجع تاريخي فقط لسياسات disclosure في عالم SOAR.

> الثقة: متوسطة (مصدر ثانوي واحد؛ النشرات الرسمية من Splunk لم تُفتح مباشرة)
