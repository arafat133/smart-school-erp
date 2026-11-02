"""
Fix unclosed pg-sms-send page container and remove leaking SMS table headers in school.html, admin.html, parent.html
"""
import re, time

print("=" * 60)
print("Fixing leaking pg-sms-send container & removing stray table headers...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace pg-sms-send cleanly with exact balanced div count
clean_whatsapp_send_page = """
<div class="page" id="pg-sms-send">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-brands fa-whatsapp" style="color:#25d366;"></i> واجهة إرسال رسائل وتنبيهات الواتساب التفاعلية (WhatsApp Business Messaging)</h2>
    </div>

    <!-- WhatsApp Session Status KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #25d366;">
            <div class="stat-info"><h3>حالة اتصال حساب الواتساب</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">متصل بنجاح (Meta API) 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>النافذة الزمنية للجلسة الحرة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">نشطة (متبقي 14 ساعة)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>إجمالي الرسائل المرسلة اليوم</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">320 رسالة تفاعلية</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchWhatsappSend" placeholder="ابحث بكود الرسالة، الرقم، أو القالب..." oninput="renderWhatsappSendGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('whatsapp_send')" style="background:linear-gradient(135deg,#25d366,#128c7e);"><i class="fa-brands fa-whatsapp"></i> إرسال رسالة واتساب جديدة ومرفقات PDF</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف سجل الرسائل</button>
        </div>
    </div>

    <div style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);padding:8px 14px;border-radius:8px;margin-bottom:12px;font-size:0.8rem;color:#60a5fa;display:flex;align-items:center;gap:8px;">
        <i class="fa-solid fa-lightbulb"></i> <span>💡 <strong>تفاعل ذكي مبتكر:</strong> انقر مرتين (Double Click) على أي صف لتعديله، أو اضغط مطولاً (Long Press) على الصف لحذفه!</span>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الرسالة</th>
                    <th>الرقم المستهدف (WhatsApp)</th>
                    <th>اسم ونوع القالب (Template)</th>
                    <th>المرفقات والوسائط (Media PDF)</th>
                    <th>أزرار التفاعل السريع</th>
                    <th>حالة التسليم والقراءة (Read Status)</th>
                    <th>النافذة الزمنية للجلسة (24h)</th>
                    <th>تكلفة واستهلاك البوابة</th>
                    <th>توقيت الإرسال والقراءة</th>
                </tr>
            </thead>
            <tbody id="tbl-whatsapp-send-grid"></tbody>
        </table>
    </div>
</div>
"""

pattern = r'<div class="page" id="pg-sms-send">.*?</div>\s*(?=<div class="page" id="pg-sms-templates"|<!-- =====|\Z)'
html = re.sub(pattern, clean_whatsapp_send_page.strip() + '\n', html, flags=re.DOTALL)

# Update cache timestamps
ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print(f"Updated HTML files cleanly with timestamp v={ts}!")
