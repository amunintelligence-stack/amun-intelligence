# AutoGen في وضع الصيانة — Microsoft توصي بـ Agent Framework للمشاريع الجديدة
## ماذا تغيّر
- مستودع microsoft/autogen يعلن رسميًا أنه في وضع الصيانة (maintenance mode): لا مزايا جديدة، صيانة مجتمعية فقط — وMicrosoft توصي بـ Microsoft Agent Framework للمشاريع الجديدة (GA أبريل 2026).
- آخر إصدار لـ autogen-agentchat كان 0.7.5 في سبتمبر 2025؛ بينما Agent Framework يصدر أسبوعيًا (وصل 1.21.0 في أكتوبر 2026).
- بدائل مجتمعية نشطة: AG2 (fork مجتمعي، v1.1.1 في سبتمبر 2026) يواصل التطوير خارج Microsoft.
## لماذا يهم ACI
- تأكيد استراتيجي: أي مرجع أو مثال في وثائق التصميم لدينا يستند إلى AutoGen يجب أن يُعامَل كمرجع تاريخي؛ المعيار الجديد للمقارنات هو Agent Framework وLangGraph وADK.
- لا اعتماد مباشر على AutoGen في مكدس ACI — لا إجراء هجرة مطلوب.
## المصادر
- dev.to — Single Agent vs Multi-Agent decision framework (2026-10-11، يقتبس README الرسمي): http://dev.to/bitneka/single-agent-vs-multi-agent-a-decision-framework-for-enterprise-teams-b5b
- مقارنة أطر الوكلاء (بيانات GitHub API، 2026-10-02): https://github.com/floatingcatty/flower/blob/HEAD/context/notes/prior-art-survey/multi_agent_graph_frameworks.md
## الإجراء
**ignore** — لا تأثير على المكدس؛ حدّث المراجع في وثائق التصميم من AutoGen إلى Agent Framework عند المراجعة القادمة.
