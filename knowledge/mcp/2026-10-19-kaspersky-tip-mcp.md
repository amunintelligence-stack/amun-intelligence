# Kaspersky Threat Intelligence Portal يضيف دعم MCP

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — مرشّح للإضافة للـ registry تحت data-sources/ti؛ التقييم فقط عند الحاجة لمصدر TI تجاري عبر MCP (يحتاج ترخيص مدفوع).

## What changed
- أعلنت Kaspersky (بيان صحفي **2026-10-06**، تغطية 8–13 أكتوبر) عن مزايا ذكاء اصطناعي جديدة في **Threat Intelligence Portal**: تلخيص آلي للتقارير، بحث OSINT محسّن لمؤشرات الاختراق (IoCs)، و**دعم Model Context Protocol** يتيح لتطبيقات الذكاء الاصطناعي الخاصة أو الخارجية الاتصال مباشرة بالبوابة والاستعلام بمرونة بدل التكاملات الجامدة.
- البوابة مبنية على **25+ بيتابايت** من سياق التهديدات الخاص؛ المزايا الجديدة متاحة عبر ترخيص **Kaspersky Threat Lookup** الحالي (حصة طلبات قياسية، وسعة إضافية مدفوعة).

## Why it matters for ACI
- أول مورّد CTI تجاري كبير يكشف مخزون التهديدات عبر MCP — هذا **مسار إثراء threat-intel جاهز** لمهام ACI (IoC lookup، سياق الحملات/الجهات الفاعلة) دون كتابة موصّل مخصص، لو توفر الترخيص.
- لكنه **keyed/مدفوع** (Threat Lookup license)، بينما استراتيجية ACI الحالية تعتمد مصادر مفتوحة/مجانية (ScanMalware، Clearfront في الـ registry). القرار: بديل ممتاز مدفوع، لا أولوية اعتماد الآن.
- ملاحظة تقييم: التحقق من سياسة البيانات والاختصاص القضائي عند التعامل مع مورّد روسي الأصل قبل أي اعتماد مؤسسي.

## Sources
- "AI on the right side: Kaspersky accelerates Threat Intelligence workflows with new AI features" (press release) — https://www.kaspersky.co.za/about/press-releases/ai-on-the-right-side-kaspersky-accelerates-threat-intelligence-workflows-with-new-ai-features — 2026-10-06
- "Kaspersky Adds AI Tools to Threat Intelligence Portal" — https://aitimes.ph/kaspersky-adds-ai-tools-to-threat-intelligence-portal/ — 2026-10-08
- "Kaspersky Adds AI Features to Threat Intelligence Portal" — https://technologyarabia.com/archives/17578/kaspersky-ai-threat-intelligence-portal/ — 2026-10-13
