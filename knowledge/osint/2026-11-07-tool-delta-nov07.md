# دلتا أدوات OSINT — بلا إصدارات جديدة (7 نوفمبر 2026)

## تحقق مباشر من GitHub Releases API — لا جديد
- **ما الذي تغيّر:** لا شيء. تحققنا مباشرة من GitHub Releases API في 7 نوفمبر 2026:
  - **nuclei-templates v10.5.1** (23 أكتوبر 2026) ما زال الأحدث — بلا إصدار أحدث.
  - **theHarvester 4.11.1** (3 يونيو 2026) ما زال الأحدث — بلا إصدار أحدث.
  - **sherlock v0.16.2** (8 سبتمبر 2026) ما زال الأحدث — بلا إصدار أحدث.
- **لماذا يهم ACI:** أدوات الاستطلاع الأساسية مستقرة؛ لا ترقية ولا تغيير قوالب مطلوب الليلة. nuclei-templates 10.5.1 يبقى خط الأساس (قوالب KEV لـ WordPress وPHP2Shell وIvanti).
- **المصادر:** https://api.github.com/repos/projectdiscovery/nuclei-templates/releases — https://api.github.com/repos/laramies/theHarvester/releases — https://api.github.com/repos/sherlock-project/sherlock/releases (فُحصت 2026-11-07)
- **الإجراء: ignore** (لا جديد).

## ملاحظة منهجية — حد GitHub API
- استُنفد حد الطلبات غير المصرّح بها (60/ساعة) أثناء الفحص؛ فشل استعلام FalkorDB اللاحق لهذا السبب لا لغياب إصدار. في الدورات القادمة: وزّع استعلامات GitHub API على دفعات أو استخدم `git ls-remote --tags` (بلا حد) للتحقق من الوسوم.
