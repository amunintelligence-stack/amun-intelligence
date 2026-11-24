# you.com — n8n node أصبح 7 عمليات وإزالة livecrawl (سبتمبر 2026)
- التاريخ: 2026-10-10 | الفئة: data-sources/ai-search | الإجراء: **مراقبة**

## ما الذي تغيّر
- n8n node الخاص بـ you.com وصل **7 operations** (تحديث سبتمبر 2026، الصفحة حُدّثت قبل ~18 يومًا).
- **تغيير كاسر**: Web Search لم يعد يقبل `livecrawl` أو `livecrawl_formats` — البديل هو **Extraction collection** (وضع `highlights` أو `full_page` مع `extraction_formats`: markdown/html).
- معامل جديد `max_age` يحدد عتبة قِدم المحتوى المخزَّن قبل إعادة الجلب.
- عملية Research تدعم background mode (تُرجع task id فورًا + polling عبر Get Research Task).

## لماذا يهم ACI
- you.com هو مرشح أساسي لمصدر ai-search في ACI (بحث ويب مُحسَّن للـ LLMs مع citations). أي connector مباشر للـ API يجب أن يعكس البنية الجديدة: Web Search + Contents + Extraction + Research + Answer، بدون `livecrawl`.
- إن استُخدم n8n لاحقًا كطبقة أوركستراشن، الـ node المحدَّث يبسط دمج you.com.

## المصادر
- https://you.com/resources/n8n-you-com-node-7-operations — سبتمبر 2026 (تم الوصول 2026-10-10)

## الإجراء المقترح
**مراقبة** — عند بناء you.com connector: اعتمد بنية operations الجديدة وتجنَّ `livecrawl`. المفتاح المطلوب: you.com API key (مدفوع).
