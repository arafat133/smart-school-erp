"""
Python script to update/re-architect HR & Staff pages in school.html:
- pg-guarantors (دليل الضمناء والكفلاء)
- pg-teacher-subjects (إسناد المواد للمدرسين)
- pg-emp-attendance (حضور وانضباط الموظفين)
- pg-emp-notices (إشعارات وتنبيهات الموظفين)
- pg-emp-contracts (عقود الموظفين والوظائف)
- pg-emp-advances (سلفيات وقروض الموظفين)
- pg-leave-management (إدارة إجازات الموظفين - RE-ADDED to HR section)
- pg-performance-eval (تقييم الأداء والكفاءة)
- pg-payroll (مسير ومعالجة الرواتب)
"""
import re, time

print("=" * 60)
print("Updating school.html HR & Staff Modules...")
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

# 1. Guarantors Page (pg-guarantors)
guarantors_html = """
<div class="page" id="pg-guarantors">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-handshake"></i> دليل الضمناء والكفلاء والالتزامات الماليـة</h2>
    </div>

    <!-- Filters & Search -->
    <div class="toolbar">
        <div class="search-box" style="flex:1;max-width:300px;"><i class="fa-solid fa-magnifying-glass"></i><input id="searchGuarantors" placeholder="بحث بالكفيل أو المكفول..." oninput="renderGuarantorsList()"></div>
        <select id="filterGuaranteeType" onchange="renderGuarantorsList()" style="width:160px;">
            <option value="all">جميع أنواع الضمانات</option>
            <option value="ضمانة تجارية">ضمانة تجارية</option>
            <option value="كفالة حضورية غرمية">كفالة حضورية غرمية</option>
            <option value="سند لأمر">سند لأمر</option>
            <option value="عقد رهن">عقد رهن</option>
        </select>
        <select id="filterGuaranteeStatus" onchange="renderGuarantorsList()" style="width:150px;">
            <option value="all"> جميع الحالات</option>
            <option value="سارية وموثقة">سارية وموثقة</option>
            <option value="تحت المراجعة">تحت المراجعة</option>
            <option value="منتهية">منتهية</option>
        </select>
        <button class="btn-add" onclick="openForm('guarantors')"><i class="fa-solid fa-plus"></i> إضافة كفيل / ضامن جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الكفيل</th>
                    <th>اسم الكفيل الكامل</th>
                    <th>نوع الضمانة</th>
                    <th>رقم الهوية / CR</th>
                    <th>جهة العمل / المنشأة</th>
                    <th>بيانات التواصل</th>
                    <th>اسم المكفول</th>
                    <th>السقف المالي للكفالة</th>
                    <th>صلاحية الكفالة</th>
                    <th>مستوى التوثيق</th>
                    <th>الحالة</th>
                    <th>المرفقات</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-guarantors-list"></tbody>
        </table>
    </div>
</div>
"""

# 2. Teacher Subjects Assignment (pg-teacher-subjects)
teacher_subjects_html = """
<div class="page" id="pg-teacher-subjects">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-chalkboard-user"></i> إسناد المواد وتوزيع النصاب للمعلمين</h2>
    </div>

    <div class="toolbar">
        <select id="tsYearTerm" style="width:180px;"><option>2026/2027 - الترم الأول</option></select>
        <select id="tsGradeFilter" onchange="renderTeacherSubjectsMatrix()" style="width:170px;">
            <option value="all">جميع الصفوف</option>
            <option value="الصف الثالث الثانوي">الصف الثالث الثانوي</option>
            <option value="الصف الثاني الثانوي">الصف الثاني الثانوي</option>
        </select>
        <button class="btn-add" onclick="openForm('teacher-subjects')"><i class="fa-solid fa-plus"></i> إسناد مادة لمعلم</button>
    </div>

    <!-- Qualification Matcher Warning Banner -->
    <div id="tsQualWarning" style="display:none;background:rgba(245,158,11,0.2);border:1px solid #f59e0b;color:#fbbf24;padding:10px 14px;border-radius:8px;margin-bottom:14px;font-weight:700;">
        <i class="fa-solid fa-triangle-exclamation"></i> تنبيه ملاءمة التخصص: المعلم أ. إبراهيم علي تخصص كيمياء، تم إسناد مادة الرياضيات بناءً على استثناء إداري!
    </div>

    <!-- Teacher Workload Matrix -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المعلم / المحاضر</th>
                    <th>المادة الدراسية</th>
                    <th>الصف والشعبة</th>
                    <th>نوع التكليف</th>
                    <th>عدد الحصص الأسبوعية</th>
                    <th>النصاب المسند / الأقصى</th>
                    <th>ملاءمة التخصص</th>
                    <th>المعلم المساند</th>
                    <th>حالة التكليف</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-teacher-subjects-matrix"></tbody>
        </table>
    </div>
</div>
"""

# 3. Employee Attendance & Discipline (pg-emp-attendance)
emp_attendance_html = """
<div class="page" id="pg-emp-attendance">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-fingerprint"></i> متابعة حضور وانضباط الموظفين اليومي</h2>
    </div>

    <!-- Daily Attendance KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>نسبة الحضور اليومي</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">95.2% (48/50)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>الحاضرون على الدوام</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">45 موظف</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>المتأخرون</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">3 موظفين</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>الغائبون دون عذر</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">2 موظف</p></div>
        </div>
    </div>

    <div class="toolbar">
        <input type="date" id="eaDate" onchange="renderEmpAttendanceGrid()" style="width:160px;">
        <select id="eaDept" onchange="renderEmpAttendanceGrid()" style="width:160px;">
            <option value="all">جميع الأقسام</option>
            <option value="قسم الحاسوب">قسم الحاسوب</option>
            <option value="القسم العلمي">القسم العلمي</option>
        </select>
        <button class="btn-add" onclick="saveEmpAttendance()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-floppy-disk"></i> حفظ كشف الحضور والانضباط</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>بيانات الموظف</th>
                    <th>وردية العمل</th>
                    <th>الدخول الفعلي</th>
                    <th>الخروج الفعلي</th>
                    <th>التأخير / الانصراف</th>
                    <th>حالة الحضور</th>
                    <th>مصدر التسجيل</th>
                    <th>موقف العذر</th>
                    <th>المخالفة الانضباطية</th>
                    <th>الجزاء المتخذ</th>
                    <th>المرفقات</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-emp-attendance-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Employee Notifications & Alerts (pg-emp-notices)
emp_notices_html = """
<div class="page" id="pg-emp-notices">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-bullhorn"></i> مركز التعاميم والإشعارات والتنبيهات الإدارية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('emp-notices')"><i class="fa-solid fa-paper-plane"></i> إرسال تعميم / إشعار موجه</button>
        <select id="enCategoryFilter" onchange="renderEmpNoticesGrid()" style="width:160px;">
            <option value="all">جميع التصنيفات</option>
            <option value="أكاديمي">أكاديمي</option>
            <option value="إداري">إداري</option>
            <option value="مالي">مالي</option>
            <option value="انضباط">انضباط</option>
        </select>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الإشعار</th>
                    <th>عنوان التنبيه / التعميم</th>
                    <th>محتوى الإشعار</th>
                    <th>التصنيف</th>
                    <th>الأولوية</th>
                    <th>المُرسِل</th>
                    <th>المستهدفون</th>
                    <th>قناة التوصيل</th>
                    <th>تاريخ الإرسال</th>
                    <th>حالة الاستلام والقراءة</th>
                    <th>رابط الإجراء</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-emp-notices-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Employee Contracts & Positions (pg-emp-contracts)
emp_contracts_html = """
<div class="page" id="pg-emp-contracts">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-contract"></i> دليل عقود الموظفين والدرجات الوظيفية</h2>
    </div>

    <!-- Contract Status KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>العقود السارية النشطة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">42 عقد</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>عقود تنتهي خلال 30 يوماً</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">3 عقود</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>تحت فترة التجربة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">5 موظفين</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('contract')"><i class="fa-solid fa-plus"></i> إنشاء عقد عمل جديد</button>
        <select id="ecFilterStatus" onchange="renderEmpContractsGrid()" style="width:160px;">
            <option value="all">جميع حالات العقود</option>
            <option value="ساري">ساري (Active)</option>
            <option value="قيد التجديد">قيد التجديد</option>
            <option value="منتهي">منتهي</option>
        </select>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم العقد</th>
                    <th>اسم الموظف</th>
                    <th>المسمى الوظيفي والدرجة</th>
                    <th>القسم / الإدارة</th>
                    <th>نوع العقد</th>
                    <th>تاريخ البداية والنهاية</th>
                    <th>فترة التجربة</th>
                    <th>الراتب الأساسي</th>
                    <th>إجمالي البدلات</th>
                    <th>ساعات الدوام</th>
                    <th>حالة العقد</th>
                    <th>العقد المكتمل PDF</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-emp-contracts-grid"></tbody>
        </table>
    </div>
</div>
"""

# 6. Employee Loans & Advances (pg-emp-advances)
emp_advances_html = """
<div class="page" id="pg-emp-advances">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-hand-holding-dollar"></i> سلفيات وقروض الموظفين والتسديد</h2>
    </div>

    <!-- Loans KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي السلف الممنوحة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">15,000 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>المبالغ المحصلة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">8,500 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>الأقساط المستحقة هذا الشهر</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">1,200 $</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('advance')"><i class="fa-solid fa-plus"></i> تقديم طلب سلفة / قرض</button>
        <div class="search-box" style="flex:1;max-width:280px;"><i class="fa-solid fa-magnifying-glass"></i><input id="searchEmpAdvances" placeholder="بحث باسم الموظف أو رقم السلفة..." oninput="renderEmpAdvancesGrid()"></div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم السلفة</th>
                    <th>اسم الموظف</th>
                    <th>نوع الطلب</th>
                    <th>مبلغ السلفة</th>
                    <th>سقف الراتب والخصم</th>
                    <th>عدد الأقساط والقسط الشهري</th>
                    <th>تاريخ بدء الخصم</th>
                    <th>اسم الضامن والكفيل</th>
                    <th>طريقة السداد</th>
                    <th>المسدد / المتبقي</th>
                    <th>سبب السلفة</th>
                    <th>حالة السلفة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-emp-advances-grid"></tbody>
        </table>
    </div>
</div>
"""

# 7. Leave Management System (pg-leave-management - RE-ADDED)
leave_mgmt_html = """
<div class="page" id="pg-leave-management">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-xmark"></i> نظام إدارة إجازات الموظفين والأرصدة</h2>
    </div>

    <!-- Leave Balance KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>رصيد الإجازات السنوية المتاح</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">21 يوماً</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>الإجازات المرضية المستهلكة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">3 أيام</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>طلبات الإجازة المعلقة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">2 طلب</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('leave_request')"><i class="fa-solid fa-plus"></i> تقديم طلب إجازة جديد</button>
        <select id="lmTypeFilter" onchange="renderLeaveManagementGrid()" style="width:160px;">
            <option value="all">جميع أنواع الإجازات</option>
            <option value="سنوية">إجازة سنوية</option>
            <option value="مرضية">إجازة مرضية</option>
            <option value="اضطرارية">إجازة اضطرارية</option>
        </select>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم الطلب</th>
                    <th>اسم الموظف والقسم</th>
                    <th>نوع الإجازة</th>
                    <th>تاريخ البداية والنهاية</th>
                    <th>عدد الأيام الفعلي</th>
                    <th>الرصيد المتبقي</th>
                    <th>الموظف البديل</th>
                    <th>المرفقات والتقارير</th>
                    <th>مسار الموافقات</th>
                    <th>الأثر المالي</th>
                    <th>إجراءات / اعتماد</th>
                </tr>
            </thead>
            <tbody id="tbl-leave-management-grid"></tbody>
        </table>
    </div>
</div>
"""

# 8. Payroll Master Processing (pg-payroll)
payroll_html = """
<div class="page" id="pg-payroll">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-money-check-dollar"></i> مسير ومعالجة الرواتب والاستقطاعات الشهرية</h2>
    </div>

    <!-- Payroll Batch Header & KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>التكلفة الكلية للرواتب</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">62,500 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>صافي المبالغ المستحقة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">54,200 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>إجمالي البدلات والمكافآت</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">8,200 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>إجمالي الاستقطاعات والخصوم</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">-16,500 $</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="payrollMonth" style="width:160px;"><option>أغسطس 2026</option><option>يوليو 2026</option></select>
        <button class="btn-add" onclick="runPayrollCalculation()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-calculator"></i> تشغيل محرك الاحتساب الآلي للرواتب</button>
        <button class="btn-add" onclick="exportBankWPSFile()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-export"></i> تصدير ملف التحويل البنكي (WPS)</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشف المسير المعتمد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>الموظف والرمز</th>
                    <th>القسم والمسمى الوظيفي</th>
                    <th>الراتب الأساسي</th>
                    <th>إجمالي البدلات</th>
                    <th>الإضافي والمكافآت</th>
                    <th>استقطاعات الانضباط</th>
                    <th>خصم السلف والقروض</th>
                    <th>الضرائب والتقاعد</th>
                    <th>إجمالي الاستقطاعات</th>
                    <th>صافي الراتب المستحق</th>
                    <th>طريقة الصرف و IBAN</th>
                    <th>حالة الراتب</th>
                    <th>قسيمة الراتب (Payslip)</th>
                </tr>
            </thead>
            <tbody id="tbl-payroll-master-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-guarantors', guarantors_html)
html = replace_or_add_page(html, 'pg-teacher-subjects', teacher_subjects_html)
html = replace_or_add_page(html, 'pg-emp-attendance', emp_attendance_html)
html = replace_or_add_page(html, 'pg-emp-notices', emp_notices_html)
html = replace_or_add_page(html, 'pg-emp-contracts', emp_contracts_html)
html = replace_or_add_page(html, 'pg-emp-advances', emp_advances_html)
html = replace_or_add_page(html, 'pg-leave-management', leave_mgmt_html)
performance_html = '''<div class="page" id="pg-performance-eval">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-star"></i> نظام تقييم الأداء والكفاءة الوظيفية (Performance Appraisal)</h2>
    </div>

    <!-- Executive KPI Summary Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>التقدير العام للدورة</h3><p style="color:#10b981;font-weight:800;font-size:1.2rem;">يتجاوز التوقعات (92.5%)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المُقيّمون المكتملون</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">18 / 20 موظف</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>مراجعات HR المعلقة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">2 نموذج</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="evalCycleSelect" onchange="renderPerformanceEvals()" style="width:200px;">
            <option>تقييم النصف الأول 2026</option>
            <option>التقييم السنوي 2025</option>
        </select>
        <button class="btn-add" onclick="openForm('performance_eval')"><i class="fa-solid fa-plus"></i> تقييم جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المُقيَّم (الموظف)</th>
                    <th>المسمى الوظيفي</th>
                    <th>المُقيّم (المدير)</th>
                    <th>دورة التقييم</th>
                    <th>الدرجة الموزونة</th>
                    <th>التقدير النهائي</th>
                    <th>حالة الاعتماد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-performance-list"></tbody>
        </table>
    </div>
</div>'''
html = replace_or_add_page(html, 'pg-performance-eval', performance_html)
html = replace_or_add_page(html, 'pg-payroll', payroll_html)

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

print("HR & Staff HTML update completed successfully!")
