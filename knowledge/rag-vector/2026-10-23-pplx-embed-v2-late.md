# Perplexity pplx-embed-v2-late — نموذجا تضمين late-interaction متعددا الوسائط (0.6B و 9B) بمساحة تضمين مشتركة (8 أكتوبر 2026)

## ماذا تغيّر؟
أصدرت Perplexity زوجًا من نماذج التضمين مفتوحة الأوزان برخصة MIT على Hugging Face في 7–8 أكتوبر 2026، ونُشر تقرير تقني على arXiv في 21 أكتوبر 2026:
- **pplx-embed-v2-late-0.6B** (حوالي 594M معامل: 240M للنص + 340M للصور) — مصمم للأجهزة الطرفية/الاستعلامات السريعة.
- **pplx-embed-v2-late-9B** — للفهرسة عالية الجودة.
- كلاهما **late-interaction retrievers (بنمط ColBERT)** مبنيان على Qwen3.5 بانتباه ثنائي الاتجاه، يُنتج كلٌّ منهما **متجهًا واحدًا 128 بُعدًا لكل توكن** ويُقيَّم بـ MaxSim — أي لا يُشفَّر النص إلى متجه كثيف واحد.
- دُرّبا معًا بـ **تقطير تمثيلي (LEAF-style representation distillation)** من معلّم داخلي 18B على مستوى التوكن، فنتجت **مساحة تضمين واحدة مشتركة**: يمكنك فهرسة المجموعة بالنموذج 9B ثم تقديم الاستعلامات الحية بالنموذج 0.6B دون إعادة فهرسة (index with 9B, query with 0.6B).
- التدريب: 186 مليون زوج استعلام–مستند عبر **46 لغة**؛ المدخلات: نصوص، صور، وصفحات مستندات بصرية (PDFs، شرائح، تقارير ممسوحة) تُعالَج مباشرة **دون OCR**.
- أرقام معلنة (من Perplexity نفسها): 9B سجّل **92.4% على MADQA**، و65.2% على ViDoRe v3 لاسترجاع الصور، ومتوسط nDCG@10 يصل إلى 81.3% على مهام استرجاع نصية متخصصة، و74.8% Recall@1000 على Q2D-Web. ملاحظة مهمة: Gemini Embedding 2 تفوّق عليهما على MIRACL-Vision — ليس تفوقًا شاملًا.
- الوصول عبر API «قادم»؛ الإصدار الحالي موجّه للاستضافة الذاتية (يتطلب sentence-transformers ≥ 6.0.0 و transformers ≥ 5.4.0).

## لماذا يهم ACI؟
- RAG الحالي عندنا TF-IDF V1 في Postgres، ومرشّحنا الأساسي الكثيف هو EmbeddingGemma 2 (وQwen3-Embedding منافسًا) — هذا **مرشّح جديد ثالث** من عائلة late-interaction، وهي العائلة نفسها التي أظهرت دراستنا الداخلية (19 أكتوبر) أنها تتفوق على الكثيفة في استرجاع الوثائق الدقيقة.
- أهميته العملية: **الاسترجاع من المستندات المرئية** (PDFs عربية، تقارير ممسوحة، شرائح) دون خط OCR — وهذا مسار يتقاطع مباشرة مع اهتمامنا بنماذج Falcon العربية للـ OCR/ASR؛ قد يغني عن OCR في مسار الاستيراد كليًا.
- 46 لغة تدريب تعني احتمال تغطية عربية أفضل من نماذج الإنجليزية الخالصة — لكن **لا توجد نتائج عربية منشورة بعد**، والمعايير المستقلة غير متوفرة حتى الآن.
- عائق تقني: التخزين متعدد المتجهات (multi-vector) غير مدعوم في pgvector؛ يتطلب Qdrant (يدعم multivectors/ColBERT) — وهو أصلًا هدف ترقيتنا (1.20.x) — ومساحة التخزين أكبر بكثير من الكثيفة أحادية المتجه.

## مصادر (مع التواريخ)
- Perplexity AI — Multimodal embeddings beyond a single vector (8 Oct 2026): https://www.perplexity.ai/hub/blog/multimodal-embeddings-beyond-a-single-vector
- marktechpost — Perplexity AI Releases pplx-embed-v2-late: A 0.6B Edge Model and a 9B Model Scoring 92.4% on MADQA (7 Oct 2026): https://www.marktechpost.com/2026/10/07/perplexity-ai-releases-pplx-embed-v2-late-a-0-6b-edge-model-and-a-9b-model-scoring-92-4-on-madqa/
- aiweekly — Perplexity Open-Sources pplx-embed-v2-late, 92.4% on MADQA (9 Oct 2026): https://aiweekly.co/alerts/perplexity-open-sources-pplx-embed-v2-late-924-on-madqa
- arXiv (تقرير تقني، 21 Oct 2026، عبر oossa): https://oossa.com/en/new-multilingual-multimodal-models-pplx-embed-v2-late-released

## الإجراء المقترح: راقب — أضِفه كمرشّح ثالث إلى خطة المقارنة العربية القادمة (EmbeddingGemma 2 مقابل Qwen3-Embedding)، مع اختبار فرعي خاص بالوثائق العربية المرئية (PDFs ممسوحة) حيث يتفوق نمط late-interaction؛ لا تعتمد عليه قبل صدور معايير مستقلة وعربية.
> الثقة: عالية (مصادر أولية: مدونة Perplexity + بطاقات النماذج على Hugging Face)
