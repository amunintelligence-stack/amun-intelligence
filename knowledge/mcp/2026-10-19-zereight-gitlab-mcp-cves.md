# ثغرات zereight/gitlab-mcp الحرجة (CVE-2026-61559 وCVE-2026-61560): درس نمطي لمعايير ربط MCP في ACI

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** ADOPT (قاعدة، لا برنامج) — اكتب في معايير ربط MCP الخاصة بـ ACI: لا نقل شبكي بلا مصادقة، لا تشغيل كـ root مع أسرار في متغيرات البيئة، وقائمة سماح لأسماء المضيفين الصادرة؛ IGNORE السيرفر نفسه (غير مستخدم عندنا).

## What changed
- **CVE-2026-61560 (CVSS 9.8)** — منشورة 2026-09-15، حُدّثت سجلاتها 2026-10-15: حزمة `@zereight/mcp-gitlab` قبل 2.1.27؛ وضع نقل SSE (`SSE=true`) يكشف **كل أدوات MCP دون أي مصادقة**. أداة `upload_markdown` تقرأ ملفات محلية عشوائية عبر معامل `file_path` غير المُطهّر، فمهاجم شبكي غير مصدَّق يقرأ `/proc/self/environ` ويسرق `GITLAB_PERSONAL_ACCESS_TOKEN` = **استيلاء كامل على حساب GitLab**. الإعداد الافتراضي لـ Docker يربط المنفذ 3002 على `0.0.0.0` ويعمل كـ root. الإصلاح في 2.1.27.
- **CVE-2026-61559** (نفس النافذة، حُدّثت 2026-10-15): عند تفعيل `ENABLE_DYNAMIC_API_URL=true` يقرأ السيرفر ترويسة `X-GitLab-API-URL` من الطلب ويستخدمها كأساس لكل مكالمات GitLab الصادرة **مُرفَقًا بها الـ Private-Token** دون قائمة سماح — SSRF يسرّب التوكن لخادم المهاجم. الإصلاح: آلية `GITLAB_ALLOWED_HOSTS` في 2.1.27.
- سياق أوسع: الثغرتان ضمن موجة «48 ساعة قاسية» لسيرفرات MCP (منتصف سبتمبر): Bifrost gateway (CVE-2026-90898، 9.8)، mysql-mcp-server (CVE-2026-59971، 10.0)، IBM contextforge gateway (CVE-2026-53710، 10.0) — كلها نفس الجذر: **نقل شبكي بلا مصادقة**.

## Why it matters for ACI
- ACI **لا يشغّل هذا السيرفر** (غير موجود في الـ registry) — فلا حادثة عندنا. القيمة هنا **نمطية**: هذه بالضبط فئات الأخطاء التي يجب أن تمنعها معايير ربط MCP قبل أن نُوصّل أي سيرفر.
- ثلاث قواعد تستحق التدوين الآن (تُكمّل ملاحظات 10-17/10-18 عن SSRF وOAuth):
  1. سيرفر MCP محلي = stdio فقط؛ أي نقل شبكي (SSE/Streamable HTTP) يجب أن يكون خلف مصادقة — لا استثناء للوضع الافتراضي.
  2. لا تشغيل كـ root داخل حاوية تحمل أسرارًا في متغيرات البيئة؛ أي أداة قراءة ملفات = `/proc/self/environ` مكشوف.
  3. أي مكالمة صادرة مبنية على مدخل خارجي (ترويسة/معامل) تحتاج قائمة سماح صريحة لأسماء المضيفين — نفس مبدأ allow-list الخاص بـ 10-17 لكن للاتجاه الصادر.

## Sources
- "CVE-2026-61560: zereight/mcp-gitlab lets anyone read files and steal tokens" — https://stackflag.com/vulnerabilities/cve-2026-61560-gitlab-mcp — published 2026-09-15, updated 2026-10-15
- "CVE-2026-61559: zereight/mcp-gitlab can leak GitLab token via header" — https://stackflag.com/vulnerabilities/cve-2026-61559-gitlab-mcp — published 2026-09-15, updated 2026-10-15
- "MCP Servers Had a Rough 48 Hours: 4 Unauthenticated CVEs" — https://dev.to/kielltampubolon/mcp-servers-had-a-rough-48-hours-4-unauthenticated-cves-4oco — ~2026-10-04
