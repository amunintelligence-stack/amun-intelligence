# osintkit 0.7.0 و Quasar 1.2.1 — أدوات OSINT جديدة (تقييم فقط)

## osintkit 0.7.0 (صدر 2026-11-02)
- **ما الذي تغيّر:** CLI بايثون يأخذ هدفًا واحدًا (بريد/اسم مستخدم/نطاق/شركة) وينتج تقريرًا دفاعيًا ملوّنًا موجزًا بواسطة LLM من ~24 مصدرًا مجانيًا بلا تسجيل دخول: crt.sh، DNS العام (SPF/DMARC/DKIM)، WHOIS، نطاقات فرعية سلبية، بحث GitHub، HIBP (بمفتاح)، XposedOrNot، LeakCheck، Gravatar، أرشيفات paste، grep.app، Hacker News، Stack Exchange، حضور اسم المستخدم. `GITHUB_TOKEN` اختياري يرفع حد GitHub من 60 إلى 5000 طلب/ساعة.
- **لماذا يهم ACI:** يتداخل مع سلسلتنا الحالية (theHarvester + sherlock + dnsrecon + crt.sh) لكن كمولّد تقرير بأمر واحد قد يسرّع «المسح الأول» على هدف — وصيغة تقرير الشركة/النطاق تطابق حالة استخدام ACI الاستخباراتية للشركات أكثر من أدوات الـ bug-bounty. ملاحظة حذر: اسم المؤلف في رابط المستودع يبدو اسمًا مؤقتًا (sjdsjadjajdjsa) — تعامل مع المصدر بحذر.
- **المصادر:** https://pypi.org/project/osintkit/0.7.0/ — https://github.com/sjdsjadjajdjsa/osintkit
- **الإجراء: watch** — جرّب على نطاق معروف وقارن عمق المخرجات بسلسلتنا قبل أي التزام.

## Quasar 1.2.1 (المستودع أُنشئ 2026-10-27؛ مقال 3 نوفمبر)
- **ما الذي تغيّر:** إطار Python (نواة stdlib فقط) ينسّق 12 أداة موجودة — subfinder، sublist3r، BBOT، amass، assetfinder، findomain، knockpy، theHarvester، PureDNS، dnsrecon، dnsenum، httpx — يزيل التكرار ويتحقق ويكتب `Final_Subdomains.txt` + `Alive_Subdomains.txt`. متعدد المنصات مع سكربتات إعداد ومحولات لكل أداة واختبارات. توثيق صادق: التوفر ≠ نجاح المسح الحيّ، بلا تصعيد امتيازات صامت.
- **لماذا يهم ACI:** قريب مفاهيميًا مما تفعله خطتنا الاستطلاعية أصلًا (subfinder → amass → httpx) — نسخة جاهزة من هذا الغراء. لكن: نجمة واحدة، 4 commits، بلا وسوم إصدار، مؤلف واحد، عمره ~9 أيام. مبكر جدًا للاعتماد عليه.
- **المصادر:** https://github.com/Th3BlackHol3/Quasar — https://execure.medium.com/quasar-a-cross-platform-subdomain-enumeration-framework-for-modern-cybersecurity-red-team-1b434ed02cd8 (2026-11-03)
- **الإجراء: watch** — سجّله؛ أعد التقييم بعد شهر (نجوم/commits/إصدارات) قبل أي تجربة.

## user-scanner 1.5.2.2 (12 أكتوبر 2026) — للعلم فقط
- 2,720+ متجه مسح (210+ موقع بريد، 2,510+ منصة اسم مستخدم)، إثراء ملفات، مسح متقاطع. نفس مساحة Helix؛ تمييز Helix (التحقق الحيّ) أكثر إثارة. **الإجراء: ignore** — راقب Helix بدلًا منه.
- المصدر: https://pypi.org/project/user-scanner/1.5.2.2/
