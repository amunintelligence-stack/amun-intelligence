# Phind متوقفة منذ يناير 2026 — لم تصدر API رسميًا أبدًا

- التاريخ: 2026-10-11 | الفئة: data-sources/ai-search | الإجراء: **تجاهل (ignore)**

## What changed
لا جديد — تصحيح سجل: Phind (محرك إجابات للمطورين، YC S22) **أُغلقت في 16 يناير 2026** (استرداد متناسب لمشتركي Pro، تصدير سجل المحادثات حتى 30 يناير، ثم مسح الخوادم).
- لم تُصدر Phind **أبدًا API رسميًا** للمطورين: لا base URL موثق ولا مصادقة ولا OpenAPI — مشاريع "Phind API" على GitHub/RapidAPI هي أغلفة غير رسمية معكوسة من الموقع الداخلي.
- الأثر الوحيد الباقي: أوزان موديلات Phind المفتوحة على Hugging Face.
- تحذير: صفحات مقارنة قديمة (مثال aitoolranked المحدّثة ~6 سبتمبر 2026) ما زالت تعرض Phind كأنها حية — لا يُعتمد عليها.

## Why it matters for ACI
- Phind **خارج خارطة مصادر ai-search نهائيًا**: لا API رسمي كان ولا سيكون؛ أي خطة connector لها تُلغى.
- درس إجرائي: صفحات المقارنات الثانوية قد تعرض أدوات ميتة كأنها حية — المصدر الرسمي أو سجل الإغلاق هو المرجع.

## Sources (links with dates)
- https://github.com/api-evangelist/phind — محدّث ~2026-08-04 (سجل تاريخي: الإغلاق 16-01-2026، لم توجد API رسمية)
- https://aitoolranked.com/blog/perplexity-vs-youcom-vs-phind-ai-search-engines-comparison-2026 — محدّث ~2026-09-06 (مثال على محتوى قديم يعرضها حية — **لا يُعتمد**)

## Action (adopt / watch / ignore — one concrete recommendation)
**تجاهل** — شطب Phind من أي خارطة مصادر مستقبلية؛ لا تغيير في السجل (ليست موجودة فيه أصلًا).
