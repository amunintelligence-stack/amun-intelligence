# Sublist3r: حالة «غير نشط» مؤكدة — لا إصدارات حديثة، وREADME ما زال يوصي بـ Python 2.7/3.4

## ما الذي تغيّر
- **مراجعة 27 أكتوبر 2026** (قائمة OSRepos): مستودع Sublist3r مصنّف «inactive» — لا commits منذ أكثر من سنة، ولا إصدارات حديثة، ولا معالجة ظاهرة للـissues والـpull requests في الفترة المقيسة. الـREADME ما زال يذكر دعم Python 2 وPython 3 ويوصي بـ Python 2.7 أو 3.4.
- هذا ليس إصدارًا جديدًا بل تأكيد حالة: الأداة متجمدة عمليًا، ومصادرها (محركات بحث + Netcraft وVirusTotal وThreatCrowd وDNSdumpster وReverseDNS) قديمة العهد ولم تُحدَّث لمقاومة تغيّرات واجهات 2026.

## لماذا يهم ACI
- Sublist3r ما زال مسجّلًا في سجل ACI كأداة recon نشطة. الاعتماد عليه في مهمة enumeration يعني نتائج جزئية بصمت: مصادر ميتة لا تُرجع خطأً واضحًا دائمًا، بل فراغًا يُقرأ خطأً على أنه «لا يوجد نطاقات فرعية».
- البديل داخل المكدّس أصلًا: subfinder (مصادر محدّثة، آخر مراجعة 26 أكتوبر حول حدود المصادر المفتاحية) وAmass، وكلاهما مغطى في ملفات سابقة.

## الإجراء: IGNORE (وخفض رتبة Sublist3r في السجل)
1. خفض حالة Sublist3r في `registry/tools.yaml` من active إلى watch/مهمل، مع ملاحظة «inactive منذ أكثر من سنة».
2. في أي مهمة enumeration جديدة: subfinder أولًا، ثم Amass للعمق؛ لا تُستخدم Sublist3r إلا كمصدر ثانوي مع ذكر حالته في التقرير.
3. لا حذف من السجل — التاريخ مهم للتدقيق.

## المصادر (تواريخ الفحص 30 أكتوبر 2026)
- OSRepos — Sublist3r (نُشر 27 أكتوبر 2026): https://osrepos.com/repo/aboul3la-sublist3r
- سياق الأدوات: قائمة OSINT أكتوبر 2026: https://hackersonlineclub.com/osint-framework-tools-list/
