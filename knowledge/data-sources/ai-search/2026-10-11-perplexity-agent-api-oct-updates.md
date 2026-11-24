# Perplexity أكتوبر 2026: أسماء presets جديدة + تقاعد GPT-5.x في 24 أكتوبر + Decisions API مفتوحة الأوزان

- التاريخ: 2026-10-11 | الفئة: data-sources/ai-search | الإجراء: **اعتماد (adopt)** — شبه حرج قبل 24 أكتوبر

## What changed
- **إعادة تسمية الـ presets** في Agent API: fast-search→`fast`، pro-search→`low`، deep-research→`medium`، advanced-deep-research→`high`، ultra→`xhigh`، إضافة `wide-research` جديدة. أي كود يستدعي الأسماء القديمة معرّض للكسر.
- **تقاعد 7 موديلات GPT-5.x على منصة Perplexity في 24 أكتوبر 2026**: `openai/gpt-5.4`، `gpt-5.4-mini`، `gpt-5.4-nano`، `gpt-5.2`، `gpt-5.1`، `gpt-5`، `gpt-5-mini` — أي fallback chain يذكرها سيتوقف بعد التاريخ. (النبأ من وثائق Perplexity عبر مصدر ثانوي — يُتحقق من docs.perplexity.ai قبل أي تغيير.)
- **Decisions API** (أُطلقت 1 أكتوبر 2026): موديل مفتوح الأوزان `pplx-decider-v1-27b` (Apache 2.0 على Hugging Face، مُشتق من Qwen3.8-27B) — يُجيب بصيغ مكتوبة (نعم/لا، اختيار متعدد، score مرتب) بـ $0.04 لكل مليون توكن إدخال ومخرجات مجانية؛ نسخة v1.1 على OpenRouter بـ $0.02/M (7 أكتوبر). مفيد للتصنيف/التوجيه في الوكلاء، وليس بحثًا.
- **كتالوج سبتمبر 2026**: أُضيفت GPT-6 Sol وLuna وClaude Opus 5.5 وGrok 4.7 وGemini 3.8 Flash؛ موديلات الطرف الثالث تُفوتر بسعر المزود بدون هامش + رسوم استدعاء أدوات (web_search $2.50/1k، fetch_url $0.50/1k).
- `POST /v1/agent` هو المسار الرئيسي مع alias `POST /v1/responses` لتوافق OpenAI SDK؛ الرد بصيغة Open Responses (مصفوفة `output` مكتوبة بدل `choices`).

## Why it matters for ACI
- أي connector أو برومبت يسمّي presets قديمة (`pro-search`، `deep-research`...) أو موديلات `gpt-5*` سيكسر في 24 أكتوبر — والخطر يمتد لإعداد 3a2l (LiteLLM proxy على جهاز محمد) لو كانت سلاسل الـ fallback تذكر GPT-5.x عبر Perplexity.
- الأسماء الجديدة للـ presets هي المعيار الذي يُبنى عليه أي connector جديد؛ Decisions API الرخيصة مرشحة لخطوة تصنيف/توجيه في مهام ACI (فلترة نتائج، توجيه مهمة) دون تشغيل موديل محادثة كامل.

## Sources (links with dates)
- https://github.com/linda-mhmd/ai-solutions-wiki/blob/HEAD/content/tools/perplexity.md — محدّث ~2026-10-04 (ملخص لوثائق Perplexity: الأسماء الجديدة + تقاعد GPT-5.x في 24-10-2026)
- https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel — 2026-10-01 (Decisions API + pplx-decider-v1-27b)
- https://openrouter.ai/perplexity/pplx-decider-v1.1-27b — 2026-10-07 (سعر $0.02/M input، نافذة 262k توكن)

## Action (adopt / watch / ignore — one concrete recommendation)
**اعتماد** — تدقيق فوري لكل سلاسل الموديلات المرتبطة بـ Perplexity (وfallback chains في 3a2l) بحثًا عن `gpt-5*` والـ presets القديمة، والترحيل للأسماء الجديدة قبل 24 أكتوبر 2026؛ التحقق من التفاصيل على docs.perplexity.ai قبل التنفيذ.
