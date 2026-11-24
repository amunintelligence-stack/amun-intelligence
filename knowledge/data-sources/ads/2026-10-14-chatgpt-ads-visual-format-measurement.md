# ChatGPT Ads — visual format test, measurement stack, and rapid geographic rollout

**Date of finding:** 2026-10-14
**Window covered:** last ~30 days

## What changed

- **Visual ad format (announced ~7 Oct 2026):** OpenAI is testing a visual ad format appearing next to image-generation outputs in ChatGPT — US-only, select advertisers, **later in October 2026**. Ads are clearly labelled, kept separate from the generated image, and OpenAI says advertising does not influence ChatGPT's answers.
- **Measurement infrastructure (same announcement):** third-party measurement via geo-experiment vendors **Haus, Measured, WorkMagic**; **10 attribution partners**; **3 data integrations**; pixel-based measurement; **Conversions API** support; brand-safety pilots with **DoubleVerify** and **Integral Ad Science** (without access to real conversations); and an **Ads Manager beta** with campaign creation, reporting, conversion measurement, and CPC bidding.
- **Rollout pace:** text ads began testing 9 Feb 2026; self-serve Ads Manager opened in May; by Oct 2026 ads show in **60+ countries** (still beta). **31 new European markets** launched 17 Sep 2026 via agency/tech partners only (initial phase, expected to last several weeks) — first clients included Bouygues Telecom, Cultura, TotalEnergies, Carrefour (France) and Repsol, Fotocasa, Santalucia (Spain). **India:** OpenAI began showing ads to logged-in adults on Free/Go plans end-Aug 2026; on **5 Oct 2026** Razorpay Engage began setting up/managing ChatGPT Ads for nine Indian brands (Tanishq, Fastrack, Traya, Tata Neu, Rivaah by Tanishq, Shaadi.com, Axis Max Life, Palmonas, NMIMS), with self-serve budgets reportedly from ₹725/day.
- **Audience limits:** ads reach eligible logged-in adults on **Free and Go** plans only; Plus, Pro, Business, Enterprise, and Education plans remain ad-free.
- **Caveat (14 Oct 2026):** reporting notes ChatGPT Ads removed **UTM links** (per Search Engine Roundtable podcast "It's New 10/14") — attribution via UTMs is currently unreliable; use the Conversions API / pixel path instead.

## Why it matters for ACI

- ChatGPT Ads is a **new ad-transparency surface ACI does not yet cover**. There is no public ad library equivalent announced; the only visibility today is: (a) what advertisers self-report, (b) partner/agency announcements naming early advertisers, (c) in-product observation by Free/Go users. ACI should start a watchlist of known ChatGPT advertisers (from partner announcements like Cosmo5/Razorpay) as the seed of a future ChatGPT-ads dataset.
- The measurement stack (geo experiments + Conversions API + DV/IAS) tells ACI what evidence will exist: aggregate impressions/clicks to advertisers, no access to conversations. ACI must not claim access to "who saw which ad in which chat" — that data does not leave OpenAI.
- For brand-intel missions, "is this brand advertising inside ChatGPT" is now a legitimate question with a checkable (if partial) answer — partner announcements + Ads Manager eligibility + observed sponsored units. Add it to the ads-surface checklist alongside Meta / Google / TikTok.
- The UTM removal is a practical trap: any ACI pipeline attributing ChatGPT-driven traffic via UTMs will undercount. Prefer Conversions API / pixel / geo-experiment evidence.

## Sources

- DEV Community, "OpenAI Adds Visual ChatGPT Ads and Third-Party Measurement Tools for Advertisers" (7 Oct 2026) — https://dev.to/alifar/openai-adds-visual-chatgpt-ads-and-third-party-measurement-tools-for-advertisers-1chj
- ExplainX, "ChatGPT Visual Ads in Image Generation: What Changes" (5 Oct 2026) — https://explainx.ai/blog/chatgpt-visual-ads-image-generation-test-october-2026
- ABNewswire, "Cosmo5 joins OpenAI's agency partner network to support the launch of ChatGPT Ads in Europe" (17 Sep 2026; listed 14 Oct 2026) — https://www.abnewswire.com/pressreleases/cosmo5-joins-openais-agency-partner-network-to-support-the-launch-of-chatgpt-ads-in-europe_836290.html
- MediaNama, "Razorpay to set up and manage ChatGPT ads for Indian brands" (6 Oct 2026) — https://www.medianama.com/2026/10/223-razorpay-chatgpt-ads-india/
- Search Engine Roundtable podcast, "It's New 10/14" (14 Oct 2026; ChatGPT Ads UTM note) — https://creators.spotify.com/pod/profile/rustybrick/episodes/Big-Google-Search-Update--Google-Ads-Bug--New-Link-Best-Practices--More-On-Bing-AI-Search-e1v4831

## Action

**Watch** — start a ChatGPT-advertiser watchlist seeded from partner announcements; add "ChatGPT Ads presence" to the ads-surface checklist. **Ignore** (for now) — any third-party "ChatGPT Ad Library" claiming full coverage; no public library exists.
