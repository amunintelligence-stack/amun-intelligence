# الإطلاق التجاري لمحرك RuVector (متجه + رسم بياني Cypher في محرك Rust واحد)

**Date found:** 2026-10-20 (nightly dev researcher)
**Action:** WATCH — محرك مثير للاهتمام بنيويًا لكنه غير ناضج للاعتماد؛ راقب تقدمه وقيّم تكامله مع طبقتي RAG والرسم البياني لاحقًا.

## What changed
Cognitum One أطلقت في 20 أكتوبر 2026 النسخة التجارية من **RuVector™** (ترخيص + دعم للشركات) — محرك Rust مفتوح المصدر (github.com/ruvnet/ruvector، رخصتا Apache 2.0 وMIT) يجمع في محرك واحد: بحث متجهي HNSW مع تسريع SIMD (استعلامات دون مللي-ثانية)، **رسم بياني معرفي متوافق مع Cypher**، و«ذاكرة ذاتية التعلم» تسجل العلاقات وأي إجابات نجحت سابقًا.
- يعمل داخل PostgreSQL وفي المتصفح (WASM) وعلى الحافة — نفس المحرك في كل مكان.
- الأرقام من بيان الشركة (غير مُتحقق مستقلًا): +4,400 نجمة GitHub و580 fork و+500 ألف تحميل شهريًا عبر npm وcrates.io حتى 30 سبتمبر 2026.
- مصدر الخبر: بيان صحفي عبر ACCESS Newswire — أي تُعامل الأرقام والمزاعم التسويقية بحذر.

## Why it matters for ACI
- ACI اليوم تمشي نحو طبقتين منفصلتين: RAG (متجه) + Graph DB (networkx). RuVector يمثل اتجاهًا صناعيًا صاعدًا: **توحيد الطبقتين في مخزن واحد** — الوكيل يجد الشبيه ويتتبع العلاقات باستعلام واحد، بلا قاعدة ثانية.
- إن ثبتت أرقام الأداء، قد يصبح بديلًا خفيفًا للدمج RAG/Graph مستقبلًا — لكن الإطلاق التجاري حديث جدًا والنضج التشغيلي غير مثبت.

## Sources
- ACCESS Newswire via Morningstar: "Cognitum One Launches Commercial RuVector…" — https://www.morningstar.com/news/accesswire/1238912msn/cognitum-one-launches-commercial-ruvector-the-self-learning-database-giving-ai-agents-memory-that-persists-connects-and-improves — 2026-10-20
- RuVector crates (primary, Apache 2.0/MIT) — https://lib.rs/crates/ruvector-attention — repo: github.com/ruvnet/ruvector
