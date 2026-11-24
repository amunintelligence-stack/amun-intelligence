# Consensus-OSINT: مجمّع OSINT ضخم بسيرفر MCP (19 مشروعًا، 7,900+ وحدة بحث)

**Date found:** 2026-10-19 (nightly dev researcher)
**Action:** WATCH — مرشّح عالي الأولوية للتقييم المعزول في أول نافذة تجربة سيرفرات MCP محلية؛ أولوية أعلى من سيرفرات الـ one-off غير المُصانة.

## What changed
- ظهر المستودع **OSINT-Experts-Society/Consensus-OSINT** بتاريخ **2026-10-08**، ودخل MCP Radar بتاريخ **2026-10-12** بزخم قوي (▲238 momentum، النجوم 49 ← 101 منذ 12 أكتوبر، 18 fork).
- أداة بحث موحّدة لأسماء المستخدمين والإيميلات وأرقام الهواتف: **7,900+ وحدة بحث** موحّدة من **19 مشروعًا مفتوح المصدر** — Sherlock (481)، Maigret (5,483)، WhatsMyName (716)، UserScanner (2,511 موقع/قاعدة)، Aliens Eye (840)، FindMe (412)، Nexfil (328)، GoSearch (306)، Vesper (299)، DetectDee (375) — مع **إزالة التكرار** (نسب تكرار موثقة: Maigret 40.8%، UserScanner 68.9%، Sherlock 98.5%).
- مميزات تهم العمل الاستخباري: **رسوم أدلة (evidence graphs)** ونتائج مُثراة، وتكامل MCP أصلي، و**مراجعة خبراء أسبوعية** (آخر مراجعة 2 أكتوبر 2026؛ آخر دفعة: 1,181 وحدة + 668 قاعدة موقع). الصفحة الرئيسية: osint.ngo.

## Why it matters for ACI
- الـ registry عندنا فيه بالفعل OpenOSINT وOSINT Toolbox MCP (nightly 10-13) — لكن Consensus-OSINT يحل **مشكلة الصيانة** التي وُثّقت في الـ nightly: أدوات مثل Sherlock توقفت تحديثاتها عمليًا (أبريل 2026)، بينما هذا المشروع له هدف مراجعة أسبوعي معلَن وفريق صيانة.
- لوكلاء ACI: سيرفر MCP **واحد** يغني عن تغليف Sherlock/Maigret/WhatsMyName كلٌّ على حدة لمهام البحث عن الكيانات (username/email/phone) — ومن غير API keys.
- التحفظ الأمني المعتاد: أي سيرفر MCP يشغّل عمليات محلية يجب تقييمه في عزلة أولًا (نفس قاعدة 10-13: فحص tool descriptions ضد tool-poisoning، تقييد الصلاحيات، احترام rate limits للمواقع المستهدفة).

## Sources
- "OSINT-Experts-Society/Consensus-OSINT — MCP Server | MCP Radar" — https://mcp.liqiwa.com/s/OSINT-Experts-Society--Consensus-OSINT.html — on radar since 2026-10-12 (accessed 2026-10-19)
- Homepage — https://osint.ngo (linked from radar page, 2026-10-19)
