# GraphRAG عصبي-رمزي موجه بأنطولوجيا (أكتوبر 2026) — إجابات مؤصلة قابلة للتدقيق

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — مرجع معماري لنمط "الأنطولوجيا أولًا" عند تصميم طبقة المعرفة في ACI؛ لا اعتماد قبل أن يصل GraphRAG إلى مرحلة التصميم الفعلي.

## What changed
ورقة Benfenati وRinaldi في مجلة Neural Computing and Applications (المجلد 38، العدد 19، المقال 797، نُشرت 10 أكتوبر 2026، DOI: 10.1007/s00521-026-12495-0): "Ontology-guided neuro-symbolic GraphRAG for grounded query answering" — استرجاع معزز بالتوليد عصبي-رمزي موجه بأنطولوجيا للإجابة عن استعلامات فوق رسوم معرفية متغايرة، مع التركيز على: التأصيل (grounding) في الرسم، والتدقيقية (auditable) عبر النسب (provenance)، وقابلية التفسير، واسترجاع دلالي فوق تكامل البيانات — مع حالة استخدام في تحليل الثغرات السيبرانية.

## Why it matters for ACI
- أقوى ما يميز ACI كمطلوب هو سلسلة الأدلة القابلة للتدقيق خلف كل حكم (confidence-gated verdicts): النمط "الأنطولوجيا أولًا + تأصيل كل إجابة في الرسم" هو بالضبط ما تحتاجه مهام الاستخبارات — إجابة بلا مصدر مرفوضة في عملنا.
- حالة الاستخدام السيبرانية (تحليل الثغرات) قريبة مباشرة من مجال ACI، مما يجعل الورقة مرجع تصميم أقرب من أوراق GraphRAG العامة.
- النقطة العملية: أي بناء GraphRAG مستقبلي في ACI يجب أن يبدأ بمخطط أنطولوجي للمجال (كيانات/علاقات المهام) لا باستخراج حر للعلاقات ثم التنظيم لاحقًا.

## Sources
- "Ontology-guided neuro-symbolic GraphRAG delivers grounded, auditable answers" (ملخص ثانوي مع المرجع) — https://scienmag.com/ontology-guided-neuro-symbolic-graphrag-delivers-grounded-auditable-answers/ — 2026-10-10
- DOI الرسمي — https://doi.org/10.1007/s00521-026-12495-0 — 2026-10-10
