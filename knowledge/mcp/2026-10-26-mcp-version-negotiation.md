# MCP: التفاوض على إصدار البروتوكول أصبح ممارسة إلزامية + خوادم جديدة (2026-10-26)

## ماذا تغيّر؟
- **ثلاثة إصدارات بروتوكول حيّة معًا:** المواصفة أضافت مراجعة 2026-07-28 (بلا حالة/stateless)، وبوابة Red Hat MCP (GA في 16 أكتوبر 2026) تدعم أربع مراجعات على نقطة نهاية واحدة — 2025-03-26 و2025-06-18 و2025-11-25 و2026-07-28 — وتتفاوض لكل عميل. **Azure MCP Server 3.0 صدر 12 أكتوبر** بعقود أدوات أوضح.
- **فحص عملي موثّق (22 أكتوبر 2026):** طلب `initialize` بإصدار 2026-07-28 إلى خادم عام للقراءة فقط أجاب بإصدار 2025-06-18 — وهذا تفاوض صحيح، لا فشل: على العميل أن يتراجع (fallback) أو يوجَّه عبر بوابة تجسر الإصدارات.
- **خوادم جديدة هذا الأسبوع:** Halon MCP (26 أكتوبر 2026، ضمن Halon Engage/Protect 26.3) — استعلامات بلغة طبيعية على بنية البريد الإلكتروني ومراقبة التسليم وإساءة الاستخدام؛ Qlik MCP Server (26 أكتوبر 2026) متاح عبر Claude Directory — وصول محكوم إلى البيانات والأنساب ومقاييس الأعمال وسير عمل التحليلات.

## لماذا يهم ACI؟
- قاعدة جديدة تُضاف إلى معيار ربط MCP لدينا (FastMCP ≥4.1.2 + issuer صريح + مسح ذاكرة الرموز): **سجّل إصدار البروتوكول الذي يُعيده الخادم، لا الذي طلبته**، وتحقق من استقرار `tools/list` بين الاستدعاءات (قدرة `listChanged`). أي خادم لا يتفاوض صراحةً يُعامل كخطر توافق.
- Halon وQlik نفسيهما ليسا في نطاق ACI مباشرةً، لكنهما يؤكدان الاتجاه: كل بائع بنية تحتية ينشر خادم MCP خاصًا به — سطح هجومنا المستقبلي سيكون "أي خادم نربطه"، لا "هل نستخدم MCP".

## مصادر (مع التواريخ)
- Telegraph — Three MCP protocol versions are live at once (فحص 22 أكتوبر 2026): https://telegra.ph/Three-MCP-protocol-versions-are-live-at-once-Here-is-how-to-see-which-one-a-server-really-speaks-10-22
- EIN Presswire — Halon Connects AI Agents to Email Infrastructure (26 أكتوبر 2026): https://www.einpresswire.com/article/952286556/halon-connects-ai-agents-to-email-infrastructure-for-faster-investigation-and-insight
- Enterprise AI World — Qlik MCP Server Now Delivers Governed Business Context (26 أكتوبر 2026): https://www.enterpriseaiworld.com/Articles/News/News/Qlik-MCP-Server-Now-Delivers-Governed-Business-Context-and-Analytics-Workflows-to-Claude%c2%a0-177193.aspx

## الإجراء المقترح: اعتمد كقاعدة
- أضف إلى قائمة فحص ربط أي خادم MCP جديد: تسجيل `protocolVersion` المُعاد + اختبار `tools/list` مرتين + توجيه عبر بوابة عند اختلاف الإصدارات. لا تغيير في الخوادم المربوطة حاليًا.

> الثقة: عالية للفحص والمصادر الرسمية (بيانات صحفية)؛ متوسطة لادعاء "ثلاثة إصدارات حيّة" كتعميم (مصدره مدونة فردية لكنه متسق مع GA لبوابة Red Hat الموثّقة في جولة 23 أكتوبر).
