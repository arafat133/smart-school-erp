"""
Rebuild HTML structure for system-settings, change-password, whatsapp-send, whatsapp-settings in school.html
and remove explicit actions th from tables
"""
import re, time

print("=" * 60)
print("Rebuilding HTML containers for 4 requested interfaces...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Rebuild pg-system-settings
system_settings_html = """
<div class="page" id="pg-system-settings">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-sliders"></i> واجهة إعدادات النظام والتكوين العام السيادي (Global System Settings)</h2>
    </div>

    <!-- Security & Status KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>مدة إغلاق الجلسة التلقائي</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;" id="setSessionTimeoutDisplay">15 دقيقة خمول</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>جدول النسخ الاحتياطي الآلي</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">يومياً 02:00 AM 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>حالة وضع الصيانة العامة</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">غير مفعل (System Live) 🟢</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchSystemSettings" placeholder="ابحث بكود الإعداد، الاسم، أو الموديول..." oninput="renderSystemSettingsGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('system_settings')"><i class="fa-solid fa-plus"></i> إضافة متغير / إعداد سيادي جديد</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف الإعدادات</button>
        </div>
    </div>

    <div style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);padding:8px 14px;border-radius:8px;margin-bottom:12px;font-size:0.8rem;color:#60a5fa;display:flex;align-items:center;gap:8px;">
        <i class="fa-solid fa-lightbulb"></i> <span>💡 <strong>تفاعل ذكي مبتكر:</strong> انقر مرتين (Double Click) على أي صف لتعديله، أو اضغط مطولاً (Long Press) على الصف لحذفه!</span>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الإعداد البرمجي (Setting Key)</th>
                    <th>اسم الإعداد (AR / EN)</th>
                    <th>التصنيف / الموديول</th>
                    <th>القيمة الحالية المعتمدة</th>
                    <th>نوع القيمة والتحكم</th>
                    <th>مهلة انتهاء الجلسة</th>
                    <th>جدول النسخ الاحتياطي (Cron)</th>
                    <th>حالة وضع الصيانة</th>
                    <th>القائم بآخر تعديل</th>
                    <th>تاريخ وتوقيت التعديل</th>
                </tr>
            </thead>
            <tbody id="tbl-system-settings-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Rebuild pg-change-password
change_password_html = """
<div class="page" id="pg-change-password">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-key"></i> واجهة تغيير كلمة المرور والسياسات الأمنية (Change Password)</h2>
    </div>

    <div style="max-width:550px;margin:0 auto;background:rgba(15,23,42,0.85);border:1px solid var(--border);border-radius:16px;padding:24px;">
        <h3 style="margin-top:0;color:#60a5fa;font-size:1.1rem;margin-bottom:16px;"><i class="fa-solid fa-shield-halved"></i> تحديث كلمة المرور للحساب الحالي</h3>
        
        <div class="fg" style="margin-bottom:14px;position:relative;">
            <label>كلمة المرور الحالية <span class="req">*</span></label>
            <input type="password" id="pwdCurrent" placeholder="أدخل كلمة المرور القديمة للحساب">
            <i class="fa-solid fa-eye" style="position:absolute;left:12px;top:38px;cursor:pointer;color:var(--muted);" onclick="togglePasswordVisibility('pwdCurrent')"></i>
        </div>

        <div class="fg" style="margin-bottom:14px;position:relative;">
            <label>كلمة المرور الجديدة <span class="req">*</span></label>
            <input type="password" id="pwdNew" placeholder="أدخل كلمة المرور الجديدة" oninput="checkPasswordStrength(this.value)">
            <i class="fa-solid fa-eye" style="position:absolute;left:12px;top:38px;cursor:pointer;color:var(--muted);" onclick="togglePasswordVisibility('pwdNew')"></i>
        </div>

        <!-- Real-Time Password Strength Meter Bar -->
        <div style="margin-bottom:14px;">
            <div style="display:flex;justify-content:space-between;font-size:0.78rem;margin-bottom:4px;">
                <span>مؤشر قوة كلمة المرور:</span>
                <strong id="pwdStrengthLabel" style="color:#ef4444;">ضعيفة جداً</strong>
            </div>
            <div style="background:rgba(255,255,255,0.1);height:6px;border-radius:3px;overflow:hidden;">
                <div id="pwdStrengthBar" style="background:#ef4444;width:15%;height:100%;transition:all 0.3s;"></div>
            </div>
        </div>

        <!-- Password Policy Rules Checklist -->
        <div style="background:rgba(15,23,42,0.6);border:1px solid var(--border);border-radius:10px;padding:10px;margin-bottom:14px;font-size:0.78rem;color:var(--muted);">
            <div style="font-weight:700;color:var(--text);margin-bottom:6px;">📋 قواعد وشروط تعقيد كلمة المرور (Password Policy):</div>
            <div id="ruleLength">❌ 8 حروف على الأقل</div>
            <div id="ruleNumber" style="margin-top:2px;">❌ تشتمل على أرقام (0-9)</div>
            <div id="ruleSpecial" style="margin-top:2px;">❌ تشتمل على رمز خاص (@#$%^&*)</div>
        </div>

        <div class="fg" style="margin-bottom:14px;position:relative;">
            <label>تأكيد كلمة المرور الجديدة <span class="req">*</span></label>
            <input type="password" id="pwdConfirm" placeholder="أعد كتابة كلمة المرور الجديدة لتطابقها">
            <i class="fa-solid fa-eye" style="position:absolute;left:12px;top:38px;cursor:pointer;color:var(--muted);" onclick="togglePasswordVisibility('pwdConfirm')"></i>
        </div>

        <!-- Session Invalidation Checkbox -->
        <div style="margin-bottom:16px;">
            <label style="display:flex;align-items:center;gap:8px;font-size:0.82rem;color:var(--text);cursor:pointer;">
                <input type="checkbox" id="chkLogoutAll" checked style="accent-color:#3b82f6;">
                <span>إلغاء وتسجيل الخروج التلقائي من جميع الأجهزة والجلسات الأخرى النشطة (Log Out All Devices)</span>
            </label>
        </div>

        <div style="font-size:0.75rem;color:var(--muted);margin-bottom:16px;">
            📅 آخر توقيت تم فيه تحديث كلمة المرور: <strong>2026-05-10 - 10:30 AM</strong>
        </div>

        <button class="btn-save" onclick="updateUserPassword()" style="width:100%;padding:10px;font-size:0.95rem;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-floppy-disk"></i> حفظ وتحديث كلمة المرور آمنياً</button>
    </div>
</div>
"""

# 3. Rebuild pg-sms-send as pg-whatsapp-send
whatsapp_send_html = """
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

# 4. Rebuild pg-sms-settings as pg-whatsapp-settings
whatsapp_settings_html = """
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

pages_replacements = [
    ('pg-system-settings', system_settings_html),
    ('pg-change-password', change_password_html),
    ('pg-sms-send', whatsapp_send_html),
    ('pg-sms-settings', whatsapp_settings_html)
]

for pid, new_h in pages_replacements:
    pattern = rf'<div class="page" id="{pid}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    html = re.sub(pattern, new_h.strip() + '\n', html, flags=re.DOTALL)
    print(f"  ✓ Updated {pid} in school.html")

# Remove <th>إجراءات</th> from all tables in school.html to prepare for Double-Click & Long-Press UX!
html = re.sub(r'<th>\s*إجراءات\s*</th>', '', html)

# Add double-click hint to all table-wrappers if not present
double_click_hint = '<div style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);padding:6px 12px;border-radius:8px;margin-bottom:8px;font-size:0.78rem;color:#60a5fa;display:flex;align-items:center;gap:6px;"><i class="fa-solid fa-lightbulb"></i> <span>💡 <strong>تفاعل ذكي مبتكر:</strong> انقر مرتين (Double Click) على أي صف لتعديله، أو اضغط مطولاً (Long Press) على الصف لحذفه!</span></div>'

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
