# نماذج NVIDIA Nemotron 3.5 للاسترجاع (Embed-1B / Embed-8B / Rerank-8B / Parse)

**Date found:** 2026-10-20 (nightly dev researcher)
**Action:** WATCH — تتبع Nemotron-3.5-Rerank-8B وEmbed-1B كمرشحَين للمرحلة الهجينة؛ لا اعتماد قبل قياسهما على بيانات ACI (نفس قاعدة ملف 14 أكتوبر: أي مرتب/مُضمّن يُقاس ولا يُفترض).

## What changed
NVIDIA نشرت في 20 أكتوبر 2026 مجموعة **Nemotron 3.5 Retriever** على Hugging Face (النماذج محدّثة قبل يوم): `Nemotron-3.5-Embed-1B` و`Nemotron-3.5-Embed-8B` و`Nemotron-3.5-Rerank-8B` و`Nemotron-3.5-Parse` — نماذج مفتوحة «جاهزة للإنتاج» للاسترجاع متعدد الوسائط وتحويل المستندات وإعادة الترتيب وRAG.
- Embed-8B: 8.38B معامل، متجهات 4096 بُعدًا، سياق 32,768 توكنًا، مبني على Ministral 3 8B Instruct، يقبل نصًا أو صور مستندات أو مزيجًا (جداول، مخططات، إنفوجرافيك)، والاسترجاع النصي مُقيَّم على 34 لغة والمصور على 18 لغة.
- أمثلة استخدام لـ Transformers وSentence Transformers وvLLM؛ الرخصة **OpenMDW 1.1** (تحتاج مراجعة توافق للاستخدام التجاري قبل أي اعتماد).

## Why it matters for ACI
- خريطة طريق ACI: هجين على Qdrant ثم مرتب — الآن لدينا مرشحان جددان مفتوحان للقياس: Rerank-8B (ثقيل؛ قد يكون بديلًا عن voyage-rerank-3 عند الوثائق التقنية) وEmbed-1B (خفيف) للتجربة المحلية بدل النماذج المغلقة.
- الميزة الجوهرية: استرجاع **بصري للمستندات** مباشرة من صور الصفحات — يتجاوز خطوة الـ OCR/الاستخراج، ومفيد لوثائق PDF المصورة التي تظهر في مهام الاستخبارات.
- الحذر: 4096 بُعدًا ضعف ما نستخدمه حاليًا — أثره على حجم الفهرس والذاكرة يُقاس لا يُفترض.

## Sources
- "NVIDIA Releases Nemotron 3.5 Retriever Models" — https://dailyaibrief.com/news/nvidia-releases-nemotron-3-5-retriever-models-curSnNOq — 2026-10-20
- NVIDIA Nemotron 3.5 Retriever collection (primary) — https://huggingface.co/collections/nvidia/nemotron-35-retriever — updated 2026-10-19
