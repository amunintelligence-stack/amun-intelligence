# مستودع AWS-Serverless-SOAR — playbooks جاهزة (نشط سبتمبر 2026)

- التاريخ: 2026-10-09 | الفئة: soar | الإجراء: **مراقبة (watch)** — مرجع تصميمي

## ما الذي تغيّر
مستودع `thtcsec/AWS-Serverless-SOAR` (نشط قبل ~11 يومًا): SOAR serverless على AWS — GuardDuty/CloudTrail ← EventBridge ← Lambda IncidentPipeline مع playbooks مسيّجة بالسياسات (احتواء EC2، تسريب S3، اختراق IAM، عزل EKS pods، سلسلة توريد CI/CD)، موافقة Slack، وTerraform lab. أيضًا أداة PhishGuard SOAR (استخراج IoCs + إثراء VirusTotal/URLScan + تقارير MITRE ATT&CK) — تعليمية لكن بنيتها قابلة للاستلهام.

## لماذا يهم ACI
بنية playbooks جاهزة كمرجع تصميمي: خط أنابيب الحوادث المسيّج بالسياسات + بوابات الموافقة البشرية يصلح كنموذج لمهام الاستجابة في ACI. لكنه AWS-only ولسنا على AWS.

## المصادر
- https://github.com/thtcsec/AWS-Serverless-SOAR
- https://github.com/meghana13-beep/-phishguard-soar-automated-phishing-response-playbook
- https://github.com/hossam77i/security-agent-architecture/blob/HEAD/skills/csoc-operations-playbook-automation/SKILL.md — تحديث v3.0 بتعزيزات AI لعمليات SOC

## الإجراء المقترح
**مراقبة** — استلهم بنية الـplaybooks؛ تجاهل كاعتماد مباشر (AWS-only).
