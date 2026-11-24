# ثغرات RCE جديدة في Langflow بسبب MCP stdio (CVE-2026-105740 / CVE-2026-105697) — وعنقود ثغرات mcp-atlassian

## ماذا تغيّر
- في **5 أكتوبر 2026** نشرت GitHub's CNA سجلّين CVE ضد **Langflow** (منصة بناء الوكلاء، تابعة لـ IBM عبر DataStax)، الاتنين بنفس الدرجة **CVSS 9.9** ونفس الـ vector (`AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`) ونفس النوع **CWE-78** (command injection):
  - **CVE-2026-105740** — النطاق المتأثر `< 1.9.0`، والإصلاح في `1.9.0`.
  - **CVE-2026-105697** — النطاق المتأثر `>= 1.1.2, < 1.10.3` (و`langflow-base >= 0.1.2, < 0.10.3` و`lfx < 1.10.3`) — يعني الإصلاح الكامل في **1.10.3** بس.
- الثغرة: أي مستخدم مُصادَق عليه في Langflow يقدر يحقق **RCE** على السيرفر بإضافة MCP server بترانسبورت **stdio** — الأمر المدخَل من المستخدم بيتبنَّى كـ string وبيتم تمريره للشل. التايم لاين بيوضح إن الإصلاح على مرحلتين: `v1.9.0` أضاف allowlist للكوماندات وتدقيق للأرجومنتات في REST model، و`v1.10.3` طبق السياسة الأمنية على طبقة التنفيذ **وشال غلاف `bash -c` خالص** (مصدر القصة: ملف `MCPStdioClient._connect_to_server` في `src/lfx/src/lfx/base/mcp/util.py`).
- وفي نفس النافذة، في **22 سبتمبر 2026** اتنشرت استشارات أمنية ضد **mcp-atlassian** (سيرفر MCP شائع لـ Jira/Confluence)، أبرزها:
  - GHSA-wrhw-j3f9-8vc6: الـ token verifier بتاع الـ HTTP transport بيقبل **أي string غير فارغ** كتوكن (CVSS **10.0**، `PR:N`)، ومعاه fallback للمشغّل لما مفيش OAuth proxy → أي حد واصل للـ HTTP endpoint بيشغّل كل أدوات أتلاسيان بصلاحيات المشغّل. الإصلاح في `0.22.0` (اتشحن 10 يوليو — الاستشارة اتأخرت 74 يوم).
  - CVE-2026-77248 / CVE-2026-77262: **path traversal** في `upload_attachment`/`confluence_upload_attachment` — المسار المُزوَّد من المُستدعِي بيتقرأ من الـ filesystem من غير workspace confinement (CWE-22)، والناتج بيترفع لـ Confluence/Jira → file read بأي مسار (`/etc/passwd`, `~/.ssh/id_rsa`).
  - CVE-2026-77251: تجاوز `JIRA_PROJECTS_FILTER` / `CONFLUENCE_SPACES_FILTER` — عميل محدود الصلاحيات يقدر يقرأ issues وboards وصفحات خارج الـ allowlist.
- مصدر تحليلي مشترك: Forkast (6 أكتوبر 2026) بيقول إن **خمس سيرفرات MCP فيدرالية أمريكية لسه غير مُرقَّعة** ضد ثغرة "على مستوى الـ spec" كشف عنها ClawSecure الأسبوع ده — تأكيد إن مشكلة MCP الأمنية بقى عندها بُعد تنظيمي (مفيش FedRAMP baseline لـ MCP، وNIST AI Agent Standards Initiative لسه شغالة).

## لماذا يهم ACI
- ACI **مش** بيشغّل Langflow ولا mcp-atlassian — الثغرات دي **مش** بتلمس ستاك بتاعنا، فمفيش إجراء طارئ.
- لكنها **design rules** حاسمة لـ MCP wiring المخطط في ACI:
  1. **Stdio transports هي أكبر خطر**: أي تول بيبني shell command من string مركّب (زي `bash -c`) لازم يتبدل بـ argument array + allowlist — اللست دي هتكون مرجع لما نكتب سيرفراتنا بـ FastMCP.
  2. **auth fallback قاتل**: الـ middleware اللي "لو مفيش توكن، استخدم بيانات المشغّل" هو نفس نمط `operator-credentials fallback` — أي سيرفر MCP في ACI لازم يرفض الـ anonymous requests صراحةً، مش يخدمهم بصلاحيات مرتفعة.
  3. **path confinement**: أي تول بيتعامل مع ملفات (upload/download) لازم يقيد المسار للـ workspace بعد canonicalization — مش `abspath` لوحدها.
  4. **bind loopback-only** + لا أسرار hard-coded في الكونفيج — قواعد مسجّلة بالفعل، الثغرات دي بتدعمها.

## المصادر
- severitydaily.com: تحليل سجلي Langflow CVE (2026-10-06 تقريبًا): https://severitydaily.com/langflow-cve-2026-105697-105740-mcp-stdio-bash-c-1-9-0-vs-1-10-3/
- severitydaily.com: تحليل ثغرة mcp-atlassian الـ 10.0 (سبتمبر 2026): https://severitydaily.com/mcp-atlassian-cve-2026-77244-token-verifier-any-non-empty-string-74-days/
- sentinelone.com — vulnerability database: CVE-2026-77248 / CVE-2026-77262 / CVE-2026-77251 / CVE-2026-55071 (MCP-for-Stata RCE، 21 سبتمبر 2026): https://www.sentinelone.com/vulnerability-database/cve-2026-77248/
- forkast.news (2026-10-06): Five Unpatched MCP Servers in Government: https://forkast.news/federal-mcp-security-exposure-five-unpatched-mcp-servers-in-government/
- NVD: CVE-2026-105697 / CVE-2026-105740 منشورة 5 أكتوبر 2026؛ CVE-2026-77248/77251/77262 منشورة 22 سبتمبر 2026.
- تواريخ الاستشارات الأصلية: GHSA-7w94-79vh-5mr2 (10 سبتمبر 2026، Langflow)؛ GHSA-w794-rj3p-xv45 (28 سبتمبر 2026، Langflow)؛ GHSA-wrhw-j3f9-8vc6 (22 سبتمبر 2026، mcp-atlassian).

## الإجراء
**watch** — مش في ستاك بتاعنا (لا عاجل ولا critical)، لكن أضف الـ 4 قواعد التصميمية أعلاه لـ security checklist بتاع الـ MCP wiring في ACI، وارجع للملف ده عند تقييم أي stdio-based MCP server جديد.
