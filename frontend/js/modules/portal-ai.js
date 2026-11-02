/**
 * ============================================================================
 * MODULE: PORTAL-AI.JS - Parent Portal & Dedicated AI Student Assistant
 * ============================================================================
 */
function sendAiQuery(customMsg) {
    const input = document.getElementById('aiChatInput');
    const chatBody = document.getElementById('aiChatBody');
    const msg = customMsg || (input ? input.value.trim() : '');
    if (!msg || !chatBody) return;

    // Student Context Banner
    const contextHeader = `
        <div style="background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.35);padding:8px 12px;border-radius:8px;margin-bottom:8px;font-size:0.8rem;color:#60a5fa;display:flex;align-items:center;gap:6px;">
            <i class="fa-solid fa-graduation-cap"></i>
            <span>👤 <strong>تقرير واستعلام خاص بالطالب:</strong> أحمد علي محمد باعباد | الصف الثالث الثانوي (علمي)</span>
        </div>
    `;

    // Append user query
    chatBody.innerHTML += `
        <div class="ai-msg user-msg" style="margin-bottom:12px;text-align:right;">
            <div style="background:#3b82f6;color:#fff;padding:10px 14px;border-radius:12px 12px 0 12px;display:inline-block;max-width:85%;font-size:0.9rem;">
                ${msg}
            </div>
        </div>
    `;

    if (input) input.value = '';
    chatBody.scrollTop = chatBody.scrollHeight;

    // Generate intelligent AI response based on query
    setTimeout(() => {
        let reply = 'أهلاً بك يا ولي أمر الطالب أحمد. أنا مساعدك الذكي الخاص بمدارس المتفوقين الأهلية.';
        const q = msg.toLowerCase();

        if (q.includes('غياب') || q.includes('حضور')) {
            reply = `${contextHeader}📊 <strong>سجل الحضور والغياب:</strong><br>• نسبة الحضور الإجمالية: <strong>96.5%</strong> 🟢<br>• إجمالي أيام الغياب: <strong>يومان فقط (بعذر مقبول)</strong>.<br>• آخر تسجيل حضور: اليوم الساعة 07:45 ص.`;
        } else if (q.includes('درجات') || q.includes('نتيجة') || q.includes('اختبار')) {
            reply = `${contextHeader}📝 <strong>الدرجات والنتائج الأكاديمية:</strong><br>• المعدل العام التراكمي: <strong>98.4% (ممتاز مرتفع) 🏆</strong><br>• الرياضيات المتقدمة: 99/100<br>• الفيزياء النووية: 98/100<br>• الكيمياء العضوية: 97/100<br>• اللغة الإنجليزية: 100/100.`;
        } else if (q.includes('رسوم') || q.includes('قسط') || q.includes('مالي') || q.includes('سند')) {
            reply = `${contextHeader}💳 <strong>الحالة المالية والرسوم:</strong><br>• إجمالي الرسوم المقررة: 450,000 YER<br>• المسدد بسندات رسمية: 300,000 YER 🟢<br>• المتبقي: 150,000 YER (تاريخ الاستحقاق: 2026-10-01).`;
        } else if (q.includes('واجب') || q.includes('مهام')) {
            reply = `${contextHeader}📚 <strong>الواجبات والمهام المدرسية:</strong><br>• واجب الرياضيات: حل تمارين ص 45 (موعد التسليم: غداً).<br>• تقرير الفيزياء: تجربة انكسار الضوء (تم التسليم بنجاح 🟢).`;
        }

        chatBody.innerHTML += `
            <div class="ai-msg bot-msg" style="margin-bottom:12px;text-align:left;">
                <div style="background:#1e293b;border:1px solid #334155;color:#f8fafc;padding:12px 16px;border-radius:12px 12px 12px 0;display:inline-block;max-width:90%;font-size:0.9rem;line-height:1.6;text-align:right;">
                    ${reply}
                </div>
            </div>
        `;
        chatBody.scrollTop = chatBody.scrollHeight;
    }, 450);
}
window.sendAiQuery = sendAiQuery;

function renderParentPortal() {
    // Renders custom parent dashboard
}
window.renderParentPortal = renderParentPortal;
