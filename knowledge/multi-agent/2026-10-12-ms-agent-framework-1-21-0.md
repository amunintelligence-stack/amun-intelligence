# Microsoft Agent Framework 1.21.0 (Python)
## ماذا تغيّر
- صدر `agent-framework` 1.21.0 على PyPI في 2026-10-08 (إصدار GitHub: python-1.21.0).
- الجديد: إرشادات دائمة لنتائج الأدوات (tool-result standing guidance)، كشف وسائط توسيع المتغيرات المعاد كتابتها، وتقييم سياسات Purview بكامل المخزن المؤقت للاستجابات المتدفقة؛ حزمة OpenAI تضيف خيار أقصى جهد استدلال (maximum reasoning-effort)؛ موصل مخزن متجهات أصلي لـ Oracle (ألفا)؛ وأمثلة لترشيح استجابات الدردشة الجماعية.
- السياق: الإطار هو توصية Microsoft الرسمية للمشاريع الجديدة بعد دخول AutoGen وضع الصيانة.
## لماذا يهم ACI
- إطار مرشح جدي لأي إعادة هيكلة مستقبلية لطبقة الوكلاء في ACI: دعم أصلي لـ MCP (تحسينات موثوقية MCP سابقة)، تكامل A2A، وحوكمة Purview — كلها تلائم متطلبات منصة استخباراتية.
- معمارية ACI الحالية مبنية على FastAPI مباشرة بأنماط الوكلاء الخمسة؛ لا حاجة للهجرة الآن.
## المصادر
- GitHub releases — microsoft/agent-framework (2026-10-08): https://github.com/microsoft/agent-framework/releases/tag/python-1.21.0
- PyPI — agent-framework 1.21.0 (2026-10-08): https://pypi.org/project/agent-framework/1.21.0/
## الإجراء
**watch** — قيّمه كبديل إطار الوكلاء عند أي إعادة تصميم كبرى؛ لا تغيير حاليًا.
