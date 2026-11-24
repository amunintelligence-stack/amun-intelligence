# AMUN — Cloudflare Pages (بديل Netlify)

المجلد ده نسخة موقع أمون مهيأة لـ Cloudflare Pages — نفس ملفات Netlify
بس دالة الـ DoH متحوّلة لصيغة Pages Functions، والمسار بقى `/doh`
بدل `/.netlify/functions/doh` (اتعدّل في console.html).

## النشر (بعد الدخول لحساب Cloudflare بتاع أمون)
1. من لوحة Cloudflare: Workers & Pages ← Create ← Pages ← Connect to Git
   واختار ريبو أمون، وخلي Build output directory هو المجلد ده
   (أو ارفع المجلد ده نفسه كمشروع Pages).
2. الـ Function بتتكتشف لوحدها من مجلد `functions/` — مفيش إعداد زيادة.
3. جرّب: `https://<project>.pages.dev/doh?name=example.com&type=A`
   وبعدين افتح `/console` وجرّب فحص نطاق.

ملحوظة: ملف `_redirects` بيخلي `/console` يفتح `console.html`.
