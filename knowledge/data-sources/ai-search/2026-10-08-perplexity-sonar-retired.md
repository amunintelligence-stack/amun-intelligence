# Perplexity أوقفت Sonar API في 2026-09-27 — التحول إلى Agent API؛ طبقة Fast Search رخيصة جديدة

- التاريخ: 2026-10-08 | الفئة: data-sources/ai-search | الإجراء: **اعتماد (adopt)**

## ما الذي تغيّر
أعلنت Perplexity في مدونتها (13 أغسطس 2026) تقاعد طبقات Sonar في 27 سبتمبر 2026، وAgent API (GA منذ فبراير 2026، المسار `/v1/agent`) هو السطح الرئيسي. استدعاءات sonar عبر chat-completions توقفت بعد الموعد. التحويل الموصى به: sonar→fast وsonar-pro→low وsonar-reasoning-pro→medium وsonar-deep-research→high — وليس مجرد تبديل اسم موديل: مسار الـ endpoint وهيكل الطلب وتحليل الرد والفوترة كلها تتغير (رسوم لكل أداة: web_search بـ $2.50/1k وfetch_url بـ $0.50/1k). Search API منتج منفصل غير متأثر. أطلقت Perplexity أيضًا Fast Search في 2026-09-24 بسعر $1/1k طلب (مقابل $5/1k للقياسي)، وخادم Perplexity MCP البعيد (https://api.perplexity.ai/mcp) حصل على تسجيل دخول OAuth في سبتمبر 2026.

## لماذا يهم ACI
أي موصل ai-search أو برومبت وكيل في ACI مربوط بسلاسل موديلات `sonar*` معطّل بصمت منذ 27 سبتمبر. التكاملات الجديدة يجب أن تستهدف Agent API؛ طبقة Fast Search وMCP+OAuth مساران أرخص/أحدث.

## المصادر
- https://dev.to/kashif_manzer/two-ai-apis-die-this-weekend-perplexity-sonar-sep-27-and-appsmith-ai-sep-30-599h — 2026-09-25
- https://ecorpit.com/perplexity-sonar-retirement-september-27-agent-api-migration-2026/ — 2026-08-21

## الإجراء المقترح
**اعتماد** — تدقيق تكامل Perplexity في ACI بحثًا عن سلاسل `sonar*` والترحيل إلى Agent API قبل دورة المهام التالية؛ شبه حرج لو كانت السلاسل ما زالت مستخدمة.
