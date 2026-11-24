# Reddit: نهاية طلبات Data API العامة في 31 أكتوبر + إيقاف RSS في 13 نوفمبر

**Date found:** 2026-10-21 (nightly dev researcher)

## What changed
بحسب تقويم مواعيد Q4 2026 (مقروءًا مقابل Reddit Help Center في 3 أكتوبر 2026):
- **31 أكتوبر 2026**: توقف قبول **الطلبات الجديدة** للوصول العام إلى Reddit Data API.
- **13 نوفمبر 2026**: توقف دعم **خلاصات RSS**.
- الاستخدام التجاري مُسعَّر (~0.24 دولار لكل 1,000 استدعاء)؛ غير التجاري 100 طلب/دقيقة عبر OAuth بموافقة.

## Why it matters for ACI
Reddit مصدر استماع اجتماعي عالي القيمة (منتديات، مناقشات تسريبات، مشاعر). لا تكامل Reddit لدينا حاليًا — فلا طوارئ — لكن أي حاجة مستقبلية لبيانات Reddit تتطلب تقديم طلب الوصول **قبل 31 أكتوبر** (10 أيام). وبعد 13 نوفمبر يموت تتبع subreddits عبر RSS نهائيًا — أي مراقبة مستقبلية يجب أن تمر عبر الـ API.

## Sources (with dates)
- Digital Applied Q4 2026 deadline calendar (مقروء 2026-10-03): https://www.digitalapplied.com/blog/q4-2026-platform-deadline-calendar-marketers
- Blotato — Social Media APIs in 2026 (أكتوبر 2026): https://www.blotato.com/blog/social-media-api

## Action
watch
