# اختراق سلسلة إمداد LiteLLM — إصدار خبيث `1.107.0` (21 أكتوبر 2026) ⚠️ حرج

## ماذا حدث؟
في **21 أكتوبر 2026** نشر مهاجمون إصدارًا خبيثًا من حزمة `litellm` (وكيل بايثون الشهير لمزودي LLM، ~23 مليون تنزيل أسبوعيًا): الإصدار **1.107.0** على PyPI وفي صور Docker الرسمية، وبقي متاحًا نحو **ساعتين** قبل إزالته.

الحمولة الخبيثة:
- **سارق بيانات اعتماد (infostealer)** يعمل عند بدء تشغيل بايثون — يستهدف: بيانات AWS/GCP/Azure السحابية، Kubernetes، Docker، Git، مفاتيح SSH/GPG/TLS، كلمات مرور وملفات تعريف الارتباط في المتصفحات، متغيرات البيئة، وصفوف جدولي `LiteLLM_CredentialsTable` و`LiteLLM_ProxyModelTable` عندما يكون `DATABASE_URL` مضبوطًا.
- **حصان طروادة للوصول عن بُعد (RAT)** بمرحلة ثانية.
- آثار الإصابة: ملفات `cook.pth` و`cook.py` و`sitecustomize.py` غير المتوقعة في جذر site-packages، وعلامة `/tmp/.pc_once_72129118c59f5636c0bb`، واتصالات صادرة نحو `litellm[.]dev`.

طريقة الاختراق (وفق تحقيق LiteLLM نفسه): المهاجمون استخدموا **رموز GitHub CLI OAuth مسروقة من حسابات 3 مهندسين** لتشغيل سير عمل الإصدار الخاص ضد fork خبيث اسمه `Berri-AI/litellm` (يختلف عن `BerriAI/litellm` الشرعي بشرطة واحدة)، ثم حذفوا أدلة التشغيل. الحزم نُشرت عبر قنوات الإصدار الطبيعية وبـ"build provenance" تبدو شرعية. هذه **ثاني** مرة تُخترق فيها LiteLLM في 2026 (الأولى: الإصداران 1.82.7/1.82.8 في مارس 2026، ونُسبت لمجموعة TeamPCP — لا صلة مؤكدة بين الحادثتين).

## لماذا يهم ACI؟
**العلاقة مباشرة جدًا:** محمد يشغّل **وكيل 3a2l المبني على LiteLLM** (Scheduled Task على جهازه `127.0.0.1:4000`، ~647 موديلًا) — أي نسخة `litellm` مسمومة هناك تعني سرقة مفاتيح الـAPI الحرة (Gemini/Groq/…) وبيانات اعتماد الجهاز. إضافةً لذلك، أي بيئة تطوير/CI حدّثت `litellm` يوم 21 أكتوبر معرّضة.

سياق أوسع: حملة **GhostAction** المتصاعدة لسرقة الأسرار عبر GitHub Actions (موجتا حقن آلي في **8 أكتوبر 2026**؛ GitGuardian: 772 مستودعًا متأثرًا بين 31 أغسطس و30 سبتمبر؛ وحزمة PyPI خبيثة `claudecord 0.3.2` تنقل أسرار النشر إلى `http://193.32.204[.]199`) — نفس نمط استهداف بيانات الاعتماد في أدوات المطورين.

## مصادر (مع التواريخ)
- Datadog Security Labs — "LiteLLM supply chain compromise: What you need to know" (21 أكتوبر 2026): https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
- Kodem Security — IOCs + runbook للاستجابة (21 أكتوبر 2026): https://www.kodemsecurity.com/resources/litellm-supply-chain-attack-litellm-1-107-0-affected-versions-iocs-and-first-hour-response-runbook
- The Hacker News — "LiteLLM Compromised in Supply Chain Attack" (21 أكتوبر 2026): https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
- undercodenews — تصعيد GhostAction وموجتا 8 أكتوبر (20 أكتوبر 2026): https://undercodenews.com/ghostaction-supply-chain-attack-escalates-as-hackers-hijack-github-accounts-to-steal-ai-cloud-and-ci-cd-secrets-video/

## الإجراء المقترح: ⚠️ تحقق عاجل (حرج)
1. على جهاز محمد (3a2l proxy): التأكد أن نسخة `litellm` المثبتة **ليست** `1.107.0`، وأن لا وجود لملفات `cook.pth`/`cook.py`/`sitecustomize.py` غريبة، والرجوع للإصدار `1.106.2` المثبت بالـhash إن لزم.
2. تدوير أي مفاتيح API/بيانات اعتماد كانت موجودة على أي جهاز حدّث `litellm` في 21 أكتوبر.
3. تثبيت (pin) نسخ `litellm` في أي متطلبات مستقبلية، وتفعيل تنبيه على أي إصدار جديد قبل التحديث التلقائي.

> الثقة: عالية — مصادر أمنية متعددة مستقلة + بيان LiteLLM الرسمي.
