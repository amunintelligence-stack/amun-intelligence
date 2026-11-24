# TII تطلق Falcon-ASR وFalcon-OCR-Arabic وFalcon-Emirati (2026-10-06)

## ماذا تغيّر
- أعلن معهد الابتكار التكنولوجي (TII، أبوظبي) في 6 أكتوبر 2026 عن ثلاثة نماذج عربية جديدة:
  - **Falcon-Emirati**: نموذج لغوي 7B مخصّص للهجة الإماراتية (مفردات وتعبيرات وثقافة)، حقّق 84.83% على معيار Alyah المحلي — متفوقًا حسب TII على كل النماذج العربية والمفتوحة المُقيّمة.
  - **Falcon-ASR**: تعرّف كلام مضغوط 1.6B يحوّل العربية الفصحى والإماراتية والإنجليزية والفرنسية والإسبانية والبرتغالية المنطوقة إلى نص.
  - **Falcon-OCR-Arabic**: نموذج خفيف لاستخراج النص العربي والمحتوى المهيكل من الصور والمستندات.
- ملاحظة: TII لم يعلن بعد ما إذا كانت أوزان Falcon-Emirati ستُنشر للمطورين أم ستُتاح عبر منصة Falcon Chat فقط.

## لماذا يهم ACI
- خط أنابيب الاستيعاب العربي في ACI: Falcon-OCR-Arabic = استخراج النصوص من الصور والمستندات العربية قبل التضمين والفهرسة؛ Falcon-ASR = تفريغ التسجيلات الصوتية العربية إلى نص قابل للبحث — كلاهما يغذّي RAG العربي مباشرة ويوسّع تغطية المهام beyond النصوص المكتوبة.
- Falcon-Emirati قد يحسّن مستقبلًا فهم اللهجات الخليجية في التحقيقات التي تتعامل مع محتوى إماراتي/خليجي.

## المصادر
- TII (2026-10-06): https://www.tii.ae/insights/tii-launches-falcon-emirati-alongside-new-arabic-ai-models-speech-and-visual-text
- GEC Newswire (2026-10-06): https://gecnewswire.com/tiis-new-7-billion-parameter-model-scored-84-83-on-an-emirati-dialect-test-heres-why-that-matters/

## الإجراء
**watch** — تقييم Falcon-ASR وFalcon-OCR-Arabic لخط الاستيعاب فور توفر الأوزان أو واجهة الوصول.
