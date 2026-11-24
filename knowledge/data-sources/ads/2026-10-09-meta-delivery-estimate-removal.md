# Meta تزيل 3 حقول من Delivery Estimate API في 27 أكتوبر 2026 — على كل النسخ

- التاريخ: 2026-10-09 | الفئة: data-sources/ads | الإجراء: **مراقبة (watch)**

## ما الذي تغيّر
في 27 أكتوبر 2026 تختفي حقول `daily_outcomes_curve` و`budget_guardrail` و`estimate_dau` من استجابة `GET /{ad-account-id}/delivery_estimate` على **كل** نسخ Marketing API المدعومة بما فيها غير المُنسخة — تثبيت النسخة لن يحمي. أُعلن في يوليو مع v26.0 وطُبق على نسخة v26.0 في 29 يوليو. (تغيير أقدم هذا العام: إزالة نوافذ الـ view-through attribution لـ 7 و28 يومًا من Ads Insights API — بقيت نافذة يوم واحد فقط.)

## لماذا يهم ACI
أي موصل إعلانات نبنيه يجب ألا يعتمد على هذه الحقول؛ وتغيّر قياس الإسناد يؤثر على تفسير بيانات أداء المعلنين.

## المصادر
- http://dev.to/driftsignal/on-october-27-metas-ad-api-stops-returning-three-delivery-estimate-fields-pinning-your-version-4d62 — ~1 أكتوبر 2026
- https://www.businesswire.com/news/home/20260610201735/en/Drive-Social-Media-Offers-an-Update-to-Clients-Regarding-the-2026-Meta-Ads-Attribution-Window-Changes — يونيو 2026

## الإجراء المقترح
**مراقبة**.
