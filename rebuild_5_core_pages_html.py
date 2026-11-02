"""
Rebuild HTML containers for school-info, alerts, archive, posting, users, audit in school.html
"""
import re, time

print("=" * 60)
print("Rebuilding HTML containers for 5 Core Interfaces...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Rebuild pg-school-info
school_info_html = """
<div class="page" id="pg-school-info">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-school"></i> واجهة معلومات المدرسة والسياسات السيادية (School Profile & Settings)</h2>
    </div>

    <!-- Stats & Status Bar -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المواقف التشغيلي للفرع</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">نشط ومعتمد (Active Branch)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>الرقم الترخيصي الوزاري</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">LIC-EDU-2026-9901</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>العملة الأساسية للنظام</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">ريال يمني (YER)</p></div>
        </div>
    </div>

    <!-- Branding & Identity + Form Panels -->
    <div style="display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:20px;">
        
        <!-- Main Details Form -->
        <div class="form-card" style="margin-bottom:0;">
            <h3 style="margin-top:0;color:#60a5fa;font-size:1rem;margin-bottom:14px;"><i class="fa-solid fa-file-contract"></i> مُصمم البيانات التعريفية والقانونية والاتصال</h3>
            <div class="form-grid">
                <div class="fg"><label>اسم المدرسة بالعربية <span class="req">*</span></label><input id="infoSchoolNameAr" value="مدرسة المجد النموذجية الأهلية" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>اسم المدرسة بالإنجليزية <span class="req">*</span></label><input id="infoSchoolNameEn" value="Al-Majd Model School" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>رقم الترخيص الوزاري <span class="req">*</span></label><input id="infoMinistryLicense" value="LIC-EDU-2026-9901" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>المراحل الدراسية المعتمدة <span class="req">*</span></label><input id="infoStages" value="الأساسية (1-9) + الثانوية (علمي/أدبي)" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>العنوان الجغرافي الدقيق <span class="req">*</span></label><input id="infoAddress" value="صنعاء - شارع حدة - أبعاد GPS" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>بيانات الاتصال الرسمية <span class="req">*</span></label><input id="infoPhone" value="770000000 | 01400000" oninput="validateNumbersOnly(this)"></div>
                <div class="fg"><label>البريد الإلكتروني المعتمد <span class="req">*</span></label><input id="infoEmail" value="info@almajd-school.edu.ye"></div>
                <div class="fg"><label>العملة الأساسية للنظام <span class="req">*</span></label><select id="infoCurrency"><option value="ريال يمني (YER)">ريال يمني (YER)</option><option value="دولار أمريكي (USD)">دولار أمريكي (USD)</option><option value="ريال سعودي (SAR)">ريال سعودي (SAR)</option></select></div>
                <div class="fg"><label>بداية ونهاية السنة المالية/الأكاديمية <span class="req">*</span></label><input id="infoFiscalYear" value="من 01 سبتمبر إلى 30 يونيو" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>حالة الفرع والترخيص <span class="req">*</span></label><select id="infoBranchStatus"><option value="نشط ومعتمد (Active Branch)">نشط ومعتمد (Active Branch)</option><option value="قيد التجديد">قيد التجديد</option></select></div>
            </div>
            <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px;">
                <button class="btn-save" onclick="saveSchoolInfo()"><i class="fa-solid fa-floppy-disk"></i> حفظ وإعادة تحميل بيانات المؤسسة</button>
            </div>
        </div>

        <!-- Branding & Authorized Signatures Panel -->
        <div style="display:flex;flex-direction:column;gap:14px;">
            <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:14px;text-align:center;">
                <h4 style="margin-top:0;color:#34d399;font-size:0.88rem;"><i class="fa-solid fa-image"></i> الشعار والختم الرسمي</h4>
                <div style="margin:10px 0;">
                    <img src="images/logo.png" alt="الشعار الرسمي" style="max-height:80px;object-fit:contain;background:#fff;padding:6px;border-radius:8px;" onerror="this.src='images/logo.png'">
                </div>
                <button class="btn-add" onclick="toast('📷 تم تحديث صورة الشعار والختم بنجاح')" style="width:100%;font-size:0.75rem;"><i class="fa-solid fa-upload"></i> رفع شعار جديد (Logo HD)</button>
            </div>

            <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:14px;">
                <h4 style="margin-top:0;color:#c084fc;font-size:0.88rem;"><i class="fa-solid fa-signature"></i> التوقيعات المعتمدة للشهادات والوثائق</h4>
                <div style="font-size:0.78rem;color:var(--text);margin-bottom:8px;">
                    <div>✍️ توقيع مدير المدرسة العام: <strong style="color:#60a5fa;">أ. خالد محمود العنسي</strong></div>
                    <div style="margin-top:4px;">✍️ توقيع مسؤول الكنترول والامتحانات: <strong style="color:#34d399;">د. عبدالملك الشامي</strong></div>
                </div>
                <button class="btn-add" onclick="toast('✍️ تم تحديث التوقيعات الرقمية للقيادة')" style="width:100%;font-size:0.75rem;background:linear-gradient(135deg,#8b5cf6,#7c3aed);"><i class="fa-solid fa-pen-nib"></i> تحديث التوقيعات الرقمية</button>
            </div>
        </div>

    </div>
</div>
"""

# 2. Rebuild pg-alerts
alerts_html = """
<div class="page" id="pg-alerts">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-bell"></i> واجهة التنبيهات التلقائية والمحفزات (Automated System Alerts)</h2>
    </div>
    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchAlerts" placeholder="ابحث باسم القاعدة، المحفز، أو القناة..." oninput="renderAlertsGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('alerts')"><i class="fa-solid fa-plus"></i> إضافة قاعدة تنبيه جديدة</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف التنبيهات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود القاعدة</th>
                    <th>اسم القاعدة / التنبيه</th>
                    <th>الحدث المحفز (Trigger)</th>
                    <th>قناة الإرسال</th>
                    <th>قالب الرسالة البرمجية</th>
                    <th>الجمهور المستهدف</th>
                    <th>حالة القاعدة</th>
                    <th>سجل حالة التسليم</th>
                    <th>زمن التنفيذ والتكرار</th>
                    <th>تكلفة بوابة الرسائل</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-alerts-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. Rebuild pg-archive
archive_html = """
<div class="page" id="pg-archive">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-box-archive"></i> واجهة الأرشيف والأرشفة الإلكترونية (Digital Archiving & OCR)</h2>
    </div>
    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchArchive" placeholder="ابحث بكود الوثيقة، العنوان، أو الهاشتاج..." oninput="renderArchiveGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('archive')"><div style="display:inline;"><i class="fa-solid fa-upload"></i> أرشفة وثيقة جديدة (OCR)</div></button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف الوثائق</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الوثيقة</th>
                    <th>عنوان الوثيقة الأصلي</th>
                    <th>التصنيف / المجلد</th>
                    <th>الرقم الإشاري الأصلي</th>
                    <th>نوع ومعاينة الملف</th>
                    <th>مستوى السرية</th>
                    <th>الكلمات المفتاحية (OCR Tags)</th>
                    <th>تاريخ الأرشفة والرفع</th>
                    <th>الموظف المؤرِشف</th>
                    <th>سياسة الحفظ والوضع</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-archive-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Rebuild pg-posting
posting_html = """
<div class="page" id="pg-posting">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-paper-plane"></i> واجهة إدارة الترحيلات والقيود المعلقة (Posting Management)</h2>
    </div>
    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchPosting" placeholder="ابحث بكود الدفعة، الموديول، أو السند..." oninput="renderPostingGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="executeBatchPosting()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check-double"></i> تنفيذ الترحيل الجماعي للمدفوعات</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف الترحيلات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود دفعة الترحيل</th>
                    <th>الموديول المصدر</th>
                    <th>رقم السند / القيد</th>
                    <th>تاريخ الحركة</th>
                    <th>إجمالي المدين والدائن</th>
                    <th>حالة التوازن والتدقيق</th>
                    <th>الحالة الحالية</th>
                    <th>القائم بالترحيل</th>
                    <th>تاريخ وختم الترحيل</th>
                    <th>الفترة المالية</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-posting-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Rebuild pg-users
users_html = """
<div class="page" id="pg-users">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-lock"></i> دليل المستخدمين وصلاحيات الوصول الشاملة (Users Directory)</h2>
    </div>
    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchUsers" placeholder="ابحث باسم المستخدم، الدور، أو البريد..." oninput="renderUsersGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('users')"><i class="fa-solid fa-user-plus"></i> إضافة مستخدم جديد وتحديد الصلاحيات</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة دليل المستخدمين</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>معرف المستخدم</th>
                    <th>اسم المستخدم</th>
                    <th>الاسم الكامل والوظيفي</th>
                    <th>نوع الحساب والدور</th>
                    <th>القسم التابع له</th>
                    <th>حالة الحساب</th>
                    <th>تاريخ الإنشاء والتفعيل</th>
                    <th>عدد الواجهات المصرح بها</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-users-grid"></tbody>
        </table>
    </div>
</div>
"""

# 6. Rebuild pg-audit
audit_html = """
<div class="page" id="pg-audit">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-shield-cat"></i> سجل العمليات والمحفوظات الأمنية المركزية (System Audit & Activity Log)</h2>
    </div>

    <!-- Security KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي الأنشطة المسجلة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.3rem;" id="auditTotalLogs">1,482 عملية</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>محاولات الدخول الناجحة</h3><p style="color:#34d399;font-weight:800;font-size:1.3rem;">99.4% ناضرة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>تأمين وقفل البيانات (WAL)</h3><p style="color:#fbbf24;font-weight:800;font-size:1.3rem;">نشط ومحمية 🛡️</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchAudit" placeholder="ابحث برقم السجل، اسم المستخدم، أو نوع الحركة..." oninput="renderAuditGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة سجل المحفوظات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود السجل (Log ID)</th>
                    <th>المستخدم والدور</th>
                    <th>التاريخ والتوقيت</th>
                    <th>الموديول التابع</th>
                    <th>نوع الحركة (CRUD)</th>
                    <th>السجل والكيان المستهدف</th>
                    <th>لقطة القيم السابقة (Old)</th>
                    <th>لقطة القيم الجديدة (New)</th>
                    <th>عنوان الـ IP والعميل</th>
                    <th>مستوى الخطورة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-audit-logs-grid"></tbody>
        </table>
    </div>
</div>
"""

pages_replacements = [
    ('pg-school-info', school_info_html),
    ('pg-alerts', alerts_html),
    ('pg-archive', archive_html),
    ('pg-posting', posting_html),
    ('pg-users', users_html),
    ('pg-audit', audit_html)
]

for pid, new_h in pages_replacements:
    pattern = rf'<div class="page" id="{pid}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    html = re.sub(pattern, new_h.strip() + '\n', html, flags=re.DOTALL)
    print(f"  ✓ Updated {pid} in school.html")

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
