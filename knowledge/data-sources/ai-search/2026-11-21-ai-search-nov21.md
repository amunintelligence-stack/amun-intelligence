# بحث ذكاء اصطناعي — معيار نوفمبر 2026 لثمانية APIs: Parallel وPerplexity وExa متقاربة؛ Perplexity الأسرع؛ Exa MCP بلا مفتاح (21 نوفمبر 2026)

## 1. معيار مستقل: 8 APIs على 3 مجموعات أسئلة (نوفمبر 2026)

- **ما الذي تغيّر:** ‏SimpleQA‏ (1,000 حقيقة قصيرة): ‏Parallel 97.8%، Perplexity Search API 97.5%، Exa 97.3%‏. ‏FreshQA‏ (358 حدثًا حديثًا): ‏Perplexity 84.1%، Exa 82.7%، Parallel 82.1%‏. ‏FRAMES‏ (824 متعدد القفزات): ‏Parallel 65.7%، Exa 63.8%، Perplexity 62.9%‏. زمن الوسيط: ‏Perplexity 0.34 ثانية، Exa 0.74 ثانية، Parallel 2.99 ثانية‏. نفس نموذج القارئ لكل API وGemini كمقيّم؛ استبعدت Perplexity نطاقَي huggingface.co وkaggle.com (نسخ من مجموعات المعيار).
- **لماذا يهم ACI:** ادعاء Exa «الأول» من البائع غير مؤكد مستقلًا — الثلاثة متقاربة في الدقة؛ السرعة تميّز Perplexity؛ الاختيار يبقى على قياس ACI الفعلي (جودة + تكلفة لكل مهمة منتهية) كما هو مسجل.
- **المصادر:** https://devplace.net/news/383a4581c3f9-what-are-the-best-web-search-apis-for-ai-agents-in-2026-8-apis-tested-with-mcp-servers-and-pricing (فُحص 17–18 نوفمبر 2026)
- **الإجراء: watch** — استخدم المعيار كمرجع؛ القرار يبقى على قياس ACI.

## 2. لقطة الأسعار (فُحص 10–18 نوفمبر 2026)

- **ما الذي تغيّر:** ‏Perplexity Search API:‏ ‏$5/1,000‏ طلب، ‏Fast $1/1,000‏؛ بلا شريحة مجانية معلنة؛ ‏MCP‏ رسمي يتطلب مفتاحًا. ‏Exa:‏ ‏Lite $4/1,000، Auto $7، Deep $12، Contents $1/1,000‏ صفحة؛ رصيد مجاني $10/شهر بلا بطاقة؛ ‏MCP‏ مستضاف بلا مفتاح عند حد مجاني. ‏Tavily:‏ أساسي $5–8/1,000، متقدم $10–16؛ 1,000 رصيد مجاني شهريًا. ‏Parallel:‏ ‏$1/1,000‏ في الوضعين السريع والتوربو.
- **المصادر:** https://websearchapi.space/blog/tavily-vs-perplexity ؛ https://79337.genesis.estage.com/compare/exa-vs-perplexity-api (فُحص 10 نوفمبر 2026)؛ https://www.stork.ai/blog/best-web-search-apis-for-ai-applications-2026
- **الإجراء: watch** — حدّث أسعار Exa/Perplexity في السجل؛ أرخص مسار تقييم بلا بطاقة هو Exa ‏($10 مجاني)‏ ثم Perplexity Fast ‏($1/1,000)‏.
