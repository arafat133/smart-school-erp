"""
Python script to update/re-architect SMS & Comprehensive Reports modules in school.html:
- pg-sms-send (إرسال الرسائل النصية SMS)
- pg-sms-templates (قوالب الرسائل الجاهزة)
- pg-sms-settings (إعدادات ورصيد الرسائل)
- pg-monthly-report (تقارير الأعمال الشهرية)
- pg-semester-report (تقرير أعمال الفصل الدراسي)
- pg-class-details (كشف تفصيلي للصفوف)
- pg-top-students (كشف أوائل المدرسة والتفوق)
- pg-success-rate-subject (نسب النجاح بالمواد والشعب)
- pg-custom-reports (تقارير مخصصة)
- pg-control-reports (تقارير الكنترول الشاملة)
"""
import re, time

print("=" * 60)
print("Updating SMS & Comprehensive Reports Modules in school.html...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page content for: {page_id}")
    else:
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added page content for: {page_id}")
    return html_text

# 1. SMS Dispatcher (pg-sms-send)
sms_send_html = """
<div class="page" id="pg-sms-send">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-paper-plane"></i> إرسال الرسائل النصية SMS والإشعارات الفورية</h2>
    </div>

    <!-- Balance Alert Banner -->
    <div style="display:flex;justify-content:space-between;align-items:center;background:rgba(59,130,246,0.15);border:1px solid #3b82f6;color:#60a5fa;padding:10px 14px;border-radius:8px;margin-bottom:14px;font-weight:700;">
        <span><i class="fa-solid fa-coins"></i> رصيد البوابة المتاح: <strong>12,450 رسالة</strong> | الموفر: Yemen Mobile API</span>
        <button class="btn-add" onclick="goTo('pg-sms-settings')" style="padding:4px 10px;font-size:0.8rem;background:#3b82f6;"><i class="fa-solid fa-gear"></i> إعدادات البوابة</button>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('sms-send')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-paper-plane"></i> صياغة وإرسال دفعة رسائل جديدة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود المعاملة</th>
                    <th>الفئة المستهدفة</th>
                    <th>نوع التنبيه</th>
                    <th>قالب الرسالة المعتمد</th>
                    <th>نص الرسالة الفعلي</th>
                    <th>عدد الحروف والأجزاء</th>
                    <th>إجمالي المستلمين</th>
                    <th>موعد وتوقيت الإرسال</th>
                    <th>بوابة الإرسال</th>
                    <th>حالة التسليم والتقرير</th>
                    <th>تكلفة الدفعة ورصيد الحساب</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-sms-send-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. SMS Templates (pg-sms-templates)
sms_templates_html = """
<div class="page" id="pg-sms-templates">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-code"></i> دليل قوالب الرسائل الجاهزة والمتغيرات الذكية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('sms-templates')"><i class="fa-solid fa-plus"></i> إنشاء قالب رسالة جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود القالب</th>
                    <th>عنوان / اسم القالب</th>
                    <th>التصنيف والنظام التابع</th>
                    <th>قناة الإرسال</th>
                    <th>مُحدث الحدث التلقائي</th>
                    <th>نص القالب بالمتغيرات</th>
                    <th>المتغيرات المستدعاة</th>
                    <th>لغة القالب والترميز</th>
                    <th>طول النص والأجزاء</th>
                    <th>حالة القالب والاعتماد</th>
                    <th>معاينة وتجربة</th>
                </tr>
            </thead>
            <tbody id="tbl-sms-templates-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. SMS Settings & Balance (pg-sms-settings)
sms_settings_html = """
<div class="page" id="pg-sms-settings">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-sliders"></i> إعدادات ورصيد بوابات الإرسال الـ SMS والـ WhatsApp</h2>
    </div>

    <!-- Balance KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>الرصيد المتاح حالياً</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">12,450 رسالة ($150.00)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المستهلك هذا الشهر</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">2,550 رسالة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>معرّف الراسل (Sender ID)</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">AL-AMAL SCH (نشط)</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('sms-settings')"><i class="fa-solid fa-plus"></i> إضافة / ربط بوابة إرسال جديدة</button>
        <button class="btn-add" onclick="toast('تم تحديث فحص اتصال البوابات أونلاين')" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-rotate"></i> فحص الاتصال بالمزودين</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اسم مزود الخدمة</th>
                    <th>معرّف الراسل (Sender ID)</th>
                    <th>مفتاح الربط (API Key)</th>
                    <th>الرصيد المتاح</th>
                    <th>حد التنبيه بالانخفاض</th>
                    <th>تكلفة الشريحة</th>
                    <th>فترة السماح بالإرسال</th>
                    <th>السقف اليومي</th>
                    <th>حالة الاتصال</th>
                    <th>تاريخ آخر تغذية</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-sms-settings-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Monthly Business Report (pg-monthly-report)
monthly_report_html = """
<div class="page" id="pg-monthly-report">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-week"></i> تقارير الأعمال الإدارية والتشغيلية الشهرية</h2>
    </div>

    <!-- Monthly KPI Executive Dashboard -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي الإيرادات الشهرية</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">45,000 $ (تحصيل 88%)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>إجمالي المصروفات التشغيلية</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">12,300 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>نسبة انضباط الطلاب العامة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">94.5%</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="mrMonthSelect" onchange="renderMonthlyReportGrid()" style="width:160px;"><option value="أغسطس 2026">أغسطس 2026</option><option value="يوليو 2026">يوليو 2026</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-file-pdf"></i> تصدير التقرير التنفيذي الشهري PDF</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود التقرير</th>
                    <th>الشهر والسنة المالية</th>
                    <th>القطاع / القسم</th>
                    <th>نسبة انضباط الطلاب</th>
                    <th>نسبة انضباط المعلمين</th>
                    <th>إجمالي التحصيل المالي</th>
                    <th>المصروفات والتوريدات</th>
                    <th>مؤشرات حركة المخزون</th>
                    <th>كفاءة المواصلات</th>
                    <th>التوصيات والخطوات القادمة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-monthly-report-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Semester Report (pg-semester-report)
semester_report_html = """
<div class="page" id="pg-semester-report">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-contract"></i> تقرير أعمال الفصل الدراسي الشامل والتراكمي</h2>
    </div>

    <div class="toolbar">
        <select id="semTermSelect" onchange="renderSemesterReportGrid()" style="width:200px;"><option value="الفصل الدراسي الأول 2025/2026">الفصل الدراسي الأول 2025/2026</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-print"></i> طباعة التقرير الاستراتيجي الفصلي</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود التقرير الفصلي</th>
                    <th>الفصل والعام الدراسي</th>
                    <th>نسبة النجاح العامة</th>
                    <th>متوسط المعدل الأكاديمي</th>
                    <th>نسبة الانضباط والتسرب</th>
                    <th>إجمالي التحصيل المالي الفصلي</th>
                    <th>إجمالي المتبقي والديون</th>
                    <th>تقييم كفاءة الكادر</th>
                    <th>استهلاك المخزون</th>
                    <th>اعتماد التقرير القيادي</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-semester-report-grid"></tbody>
        </table>
    </div>
</div>
"""

# 6. Detailed Class Manifest (pg-class-details)
class_details_html = """
<div class="page" id="pg-class-details">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-table-list"></i> كشف تفصيلي للصفوف والطلاب والسجل الموحد</h2>
    </div>

    <div class="toolbar">
        <select id="cdGradeSelect" onchange="renderClassDetailsGrid()" style="width:200px;"><option value="الثالث الثانوي - شعبة (أ)">الثالث الثانوي - شعبة (أ)</option><option value="الثاني الثانوي - شعبة (ب)">الثاني الثانوي - شعبة (ب)</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشف تفصيلي الشعبة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>الرقم الأكاديمي</th>
                    <th>اسم الطالب الرباعي</th>
                    <th>الصف والشعبة</th>
                    <th>حالة القيد</th>
                    <th>مربّي / رائد الصف</th>
                    <th>نسبة الانضباط والغياب</th>
                    <th>المعدل الأكاديمي (GPA)</th>
                    <th>الموقف المالي للرسوم</th>
                    <th>بيانات ولي الأمر</th>
                    <th>اشتراك المواصلات</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-class-details-grid"></tbody>
        </table>
    </div>
</div>
"""

# 7. Top Students & Honors (pg-top-students)
top_students_html = """
<div class="page" id="pg-top-students">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-award"></i> كشف أوائل المدرسة واللوحة الشرفية للتفوق</h2>
    </div>

    <div class="toolbar">
        <select id="tsScopeSelect" onchange="renderTopStudentsGrid()" style="width:200px;"><option value="أوائل المدرسة">أوائل المدرسة العامة</option><option value="أوائل الصفوف">أوائل الصفوف الدراسية</option></select>
        <button class="btn-add" onclick="generateBulkHonorCertificates()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-certificate"></i> إصدار شهادات التقدير وإرسال التهاني</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المركز والترتيب</th>
                    <th>الرقم الأكاديمي</th>
                    <th>اسم الطالب الكامل</th>
                    <th>الصف والشعبة</th>
                    <th>المجموع الكلي والنسبة</th>
                    <th>المعدل التراكمي (GPA)</th>
                    <th>درجة السلوك والمواظبة</th>
                    <th>معيار كسر التعادل</th>
                    <th>حالة التكريم والشهادة</th>
                    <th>إشعار ولي الأمر</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-top-students-grid"></tbody>
        </table>
    </div>
</div>
"""

# 8. Success Rate by Subject & Section (pg-success-rate-subject)
success_rate_subject_html = """
<div class="page" id="pg-success-rate-subject">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-chart-column"></i> نسب النجاح والتحليل الأكاديمي بالمواد والشعب</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة تقرير نسب النجاح بالمواد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود المادة والشعبة</th>
                    <th>اسم المادة</th>
                    <th>الصف والشعبة</th>
                    <th>المعلم المدرس</th>
                    <th>عدد الطلاب المتقدمين</th>
                    <th>الناجحين والراسبين</th>
                    <th>نسبة النجاح العامة</th>
                    <th>متوسط درجات المادة</th>
                    <th>أعلى وأدنى درجة</th>
                    <th>مؤشر التنبيه والتقييم</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-success-rate-subject-grid"></tbody>
        </table>
    </div>
</div>
"""

# 9. Custom Dynamic Report Builder (pg-custom-reports)
custom_reports_html = """
<div class="page" id="pg-custom-reports">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-invoice"></i> مُصمم ومُنشئ التقارير المخصصة والاستعلامات</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('custom-reports')"><i class="fa-solid fa-wand-magic-sparkles"></i> تصميم استعلام / تقرير مخصص جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود التقرير المخصص</th>
                    <th>عنوان التقرير</th>
                    <th>مصدر البيانات الأساسي</th>
                    <th>الحقول المختارة</th>
                    <th>الشروط المطبقة</th>
                    <th>التجميع والفرز</th>
                    <th>الدوال الحسابية</th>
                    <th>نمط العرض المرئي</th>
                    <th>جدولة التصدير الآلي</th>
                    <th>صلاحية المشاركة</th>
                    <th>تشغيل واستعراض</th>
                </tr>
            </thead>
            <tbody id="tbl-custom-reports-grid"></tbody>
        </table>
    </div>
</div>
"""

# 10. Comprehensive Control Reports (pg-control-reports)
control_reports_html = """
<div class="page" id="pg-control-reports">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-shield"></i> تقارير الكنترول والمشيت الموحد الرسمي</h2>
    </div>

    <div class="toolbar">
        <select id="crReportTypeSelect" onchange="renderControlReportsGrid()" style="width:220px;"><option value="المشيت الرسمي الموحد">المشيت الرسمي الموحد (Master Sheet)</option><option value="كشف المكملين">كشف المكملين (الدور الثاني)</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-print"></i> طباعة المشيت المعتمد رسمياً</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود تقرير الكنترول</th>
                    <th>العام والفصل الدراسي</th>
                    <th>المرحلة والصف</th>
                    <th>نوع تقرير الكنترول</th>
                    <th>إجمالي الطلاب المقيدين</th>
                    <th>نسبة اكتمال الرصد</th>
                    <th>حالة الأرقام السرية</th>
                    <th>إحصائية الموقف الأكاديمي</th>
                    <th>حالة اعتماد الكنترول</th>
                    <th>ختم وتوثيق الشهادة</th>
                    <th>معاينة وطباعة</th>
                </tr>
            </thead>
            <tbody id="tbl-control-reports-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-sms-send', sms_send_html)
html = replace_or_add_page(html, 'pg-sms-templates', sms_templates_html)
html = replace_or_add_page(html, 'pg-sms-settings', sms_settings_html)
html = replace_or_add_page(html, 'pg-monthly-report', monthly_report_html)
html = replace_or_add_page(html, 'pg-semester-report', semester_report_html)
html = replace_or_add_page(html, 'pg-class-details', class_details_html)
html = replace_or_add_page(html, 'pg-top-students', top_students_html)
html = replace_or_add_page(html, 'pg-success-rate-subject', success_rate_subject_html)
html = replace_or_add_page(html, 'pg-custom-reports', custom_reports_html)
html = replace_or_add_page(html, 'pg-control-reports', control_reports_html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

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

print("SMS & Comprehensive Reports HTML update completed successfully!")
