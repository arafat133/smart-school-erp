"""
Fix unbalanced page divs for pg-sms-settings and pg-custom-reports in school.html, admin.html, parent.html
"""
import re, time

print("=" * 60)
print("Fixing page div balance for pg-sms-settings and pg-custom-reports...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix pg-sms-settings
clean_sms_settings = """
<div class="page" id="pg-sms-settings">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-brands fa-whatsapp" style="color:#25d366;"></i> واجهة إعدادات ورصيد واتساب (WhatsApp Gateway & Credits Settings)</h2>
    </div>

    <!-- Live Credits & Subscription Dashboard KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #25d366;">
            <div class="stat-info"><h3>رصيد الوحدات المتبقي</h3><p style="color:#34d399;font-weight:800;font-size:1.3rem;" id="waRemainingCredits">4,850 رسالة متاحة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>باقة الاشتراك النشطة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">الباقة المؤسسية (10k)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>تاريخ انتهاء الباقة</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">2026-12-31</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchWhatsappSettings" placeholder="ابحث باسم البوابة، الرقم، أو الحالة..." oninput="renderWhatsappSettingsGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('whatsapp_settings')" style="background:linear-gradient(135deg,#25d366,#128c7e);"><i class="fa-solid fa-plug"></i> إعداد رابط API جديد وشحن الأرصدة</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف إعدادات البوابة</button>
        </div>
    </div>

    <div style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);padding:8px 14px;border-radius:8px;margin-bottom:12px;font-size:0.8rem;color:#60a5fa;display:flex;align-items:center;gap:8px;">
        <i class="fa-solid fa-lightbulb"></i> <span>💡 <strong>تفاعل ذكي مبتكر:</strong> انقر مرتين (Double Click) على أي صف لتعديله، أو اضغط مطولاً (Long Press) على الصف لحذفه!</span>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اسم ورقم مزود الخدمة</th>
                    <th>حالة الربط التقني (API)</th>
                    <th>رصيد الوحدات المتبقي</th>
                    <th>باقة الاشتراك النشطة</th>
                    <th>تاريخ انتهاء الباقة</th>
                    <th>معدل استهلاك اليوم</th>
                    <th>سعر تكلفة الرسالة الواحدة</th>
                    <th>حد الانخفاض للتنبيه</th>
                    <th>معرف الـ Webhook وحالة التمكين</th>
                    <th>آخر عملية تحديث أو شحن</th>
                </tr>
            </thead>
            <tbody id="tbl-whatsapp-settings-grid"></tbody>
        </table>
    </div>
</div>
"""

pattern_sms_set = r'<div class="page" id="pg-sms-settings">.*?</div>\s*(?=<div class="page"|<!-- =====|\Z)'
html = re.sub(pattern_sms_set, clean_sms_settings.strip() + '\n', html, flags=re.DOTALL)

# Fix pg-custom-reports
pattern_custom_rep = r'<div class="page" id="pg-custom-reports">.*?</div>\s*(?=<div class="page"|<!-- =====|\Z)'
# Get existing pg-custom-reports and fix extra closing divs inside it
match_cr = re.search(pattern_custom_rep, html, re.DOTALL)
if match_cr:
    cr_content = match_cr.group(0)
    # Remove 2 extra </div> at the end of cr_content before the last </div>
    # Replace last </div></div></div> with </div>
    cr_fixed = re.sub(r'(?:</div>\s*){3,}\Z', '</div>\n', cr_content)
    html = html.replace(cr_content, cr_fixed)
    print("  ✓ Fixed pg-custom-reports closing divs")

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

print(f"Updated HTML files with timestamp v={ts}!")
