# مقارنة مستقلة: Qwen3-Embedding يتفوق على EmbeddingGemma 2 في النص — وEmbeddingGemma 2 يفوز في المستندات البصرية

**Date found:** 2026-10-22 (nightly dev researcher)

## What changed
مقارنة منشورة (~16 أكتوبر 2026، من Regolo — مزوّد API، أي أرقام طرف ثالث بتحفظ) تضع الأرقام الرسمية من بطاقات النماذج جنبًا إلى جنب، وتكشف ما حذفته بطاقة EmbeddingGemma 2 من مقارنات خارجية:
- **MTEB Multilingual v2** (متوسط المهام): Qwen3-Embedding-8B **70.58**، Qwen3-Embedding-0.6B **64.33**، مقابل EmbeddingGemma 2 **61.36** (وv1: 61.15).
- **MTEB Code v1** (nDCG@10): Qwen3-Embedding-8B **80.68** > EmbeddingGemma 2 **78.68** > Qwen3-Embedding-0.6B 75.41.
- **MMEB v2 VisDoc** (مستندات بصرية، nDCG@5): EmbeddingGemma 2 **67.84** — لا منافس (Qwen3 لا يدعمها).
- نافذة السياق: Qwen3-Embedding **32,768** توكن مقابل 8,192 لـEmbeddingGemma 2 — فارق 4x يهم المستندات الطويلة.
- **جديد**: OpenBMB أصدر **Trident-Qwen3VL-2B** (12 أكتوبر 2026) — نموذج تضمين متعدد الوسائط 2B للاسترجاع مختلط الوسائط على Hugging Face.

## Why it matters for ACI
- EmbeddingGemma 2 هو المرشح الأساسي لـRAG الكثيف، لكن ACI يعمل على نصوص **عربية/متعددة اللغات** ومستندات — وهنا يتفوق Qwen3-Embedding-0.6B (أخف: 595M مقابل 270M للنص فقط في Gemma، لكن نافذة 32k وأداء multilingual أعلى).
- القرار الصحيح: **لا تثبيت نهائي قبل اختبار الثلاثة على عيّنة عربية فعلية من بيانات المهام** (أخبار عربية، أسماء كيانات، سجلات شركات). الأرقام الرسمية ليست بديلًا عن corpus خاص.
- Trident-Qwen3VL-2B: مرشح watch للمستندات البصرية/الصور لاحقًا (تقارير مصورة، لقطات).

## Sources
- المقارنة (~16 أكتوبر 2026 — مصدر بائع، تحفظ واجب): https://regolo.ai/embeddinggemma-2-vs-qwen3-embedding-benchmarks/
- سجل إصدار Trident-Qwen3VL-2B (12 أكتوبر 2026): https://deployedbyai.com/log/80b022b2b828/trident-qwen3vl-2b/
- سياق سابق: 2026-10-10-embeddinggemma-2.md (المرشح الأساسي)

## Action
**watch** — أضف Qwen3-Embedding-0.6B وQwen3-Embedding-8B وTrident-Qwen3VL-2B كمرشحين في السجل؛ عند بدء RAG الكثيف: benchmark ثلاثي (EmbeddingGemma 2 / Qwen3-0.6B / Qwen3-8B) على عيّنة عربية من بيانات ACI قبل التثبيت. تحقق من الترخيص (يُفترض Apache 2.0 لعائلة Qwen3 — أكّد من بطاقة النموذج).
