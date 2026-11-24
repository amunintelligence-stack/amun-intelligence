# Exa 3.0: الفحص المستقل لا يعيد إنتاج ادعاء «الأول على كل المعايير» (2026-10-25)

## ماذا تغيّر؟
- بعد ملاحظة 22 أكتوبر عن Exa 3.0 (إعلان الشركة: الأول على 8 معايير، Lite بـ$4/1000 طلب)، ظهر **فحص مستقل** يخفف الادعاء:
  - **Artificial Analysis Search Index** (بيانات 19 أكتوبر 2026، 27 منتجًا من 14 مزودًا، نموذج إجابة GPT-5.6 Luna medium): **Exa Search (auto, dynamic highlights) = 80 نقطة، وPerplexity Search (medium) = 80 نقطة أيضًا** — تعادل في المتوسط الكلي، لا صدارة منفردة.
  - التفصيل: Exa يتقدم في DeepSearchQA (86 مقابل 81) وPerplexity يتقدم في BrowseComp (87 مقابل 83).
  - Exa Lite = 79 نقطة بتكلفة بحث $31.20/1000 مهمة مقابل $53.17 لأعلى إعداد Exa.
  - منافسون أرخص بفارق كبير: **Octen Search (highlights) = 77 نقطة بـ$9.07/1000 مهمة** (والأسرع: 14.9 ثانية/مهمة)، و**DeepSeek Search (summary) = 69 نقطة بـ$8.47** بحثًا (لكن تكلفة نموذجها أعلى: $23.24/1000 مهمة).
- ملاحظة منهجية: معايير Exa الخاصة (ATLAS منشور 8 أكتوبر من Exa نفسها، وCompany/People FindAll بمقاييسها الخاصة) لم تُعاد إنتاجها مستقلًا؛ الأرقام المنشورة من الشركة أُجريت بأدواتها ولم تُنشر مخرجات خام قابلة لإعادة الإنتاج (وفق Daily AI Brief، 19 أكتوبر).

## لماذا يهم ACI؟
- هذا **تصحيح مهم لملاحظة 22 أكتوبر**: لا ننقل ادعاء الشركة كحقيقة. Exa 3.0 ما زال مرشح بحث ذكاء اصطناعي قويًا (خاصة استخراج الكيانات: شركات/أشخاص)، لكن صدارة المعايير **لم تُثبت مستقلًا**، والتعادل مع Perplexity في المؤشر المستقل يعني أن قرار التبديل لا يُبنى على المعايير وحدها.
- للقرار الاقتصادي: Octen وDeepSeek يقدمان نقاطًا أقل بتكلفة بحث أقل بكثير — أي أن الاختبار الحقيقي لدينا يجب أن يقيس **التكلفة لكل مهمة منتهية + جودة الإجابة على استعلاماتنا** (كيانات شركات/أشخاص عربية ودولية)، لا نقاط المعايير العامة.
- يبقى الوضع: Exa في السجل كـ«watch» (يحتاج مفتاحًا) — لا ترقية إلى مرشح أول قبل اختبارنا الخاص.

## مصادر (مع التواريخ)
- AI Socratic — Exa 3.0 tops the Artificial Analysis Search Index, but DeepSeek and Octen undercut it on price (أكتوبر 2026، بيانات 19 أكتوبر): https://aisocratic.org/news/exa-30-tops-the-artificial-analysis-search-index-but-deepseek-and-octen-undercut-it-on-price-t1y0of
- Daily AI Brief — Exa Labs Releases Exa 3.0 Search Engine for AI Agents (19 أكتوبر 2026): https://dailyaibrief.com/news/exa-labs-releases-exa-3-0-search-engine-for-ai-agents-m1WXEyz8
- MarkTechPost — Exa 3.0 Search API Tops Perplexity, Brave and Parallel on 8 Benchmarks (20 أكتوبر 2026، ينقل معايير الشركة): https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/

## الإجراء المقترح: راقب (لا تغيير في الترتيب)
- يبقى Exa «watch». قبل أي اعتماد: اختبار مقارن على استعلامات ACI الحقيقية (Lite مقابل Auto مقابل Perplexity مقابل Octen) بقياس الجودة والتكلفة لكل مهمة منتهية.

> الثقة: عالية للمؤشر المستقل (Artificial Analysis، منهجية منشورة)؛ متوسطة لتفسير فروق التكلفة (تعريفات «مهمة» تختلف بين المزودين).
