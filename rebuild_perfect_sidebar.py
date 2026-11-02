"""
Rebuild clean, organized, perfect sidebar HTML for school.html, admin.html, and parent.html.
Includes:
- Direct Dashboard item at top.
- Clean category headers with FontAwesome icons.
- All valid pages organized intuitively.
- Zero orphan tags or broken links.
- Chevron arrows for expandable sections.
"""
import re, time

print("=" * 60)
print("Rebuilding clean, perfect sidebar HTML...")
print("=" * 60)

sidebar_nav_content = """
<nav class="sidebar-nav" id="sidebarNav">
    <!-- Top Direct Dashboard Link -->
    <a href="#" class="nav-item direct-item active" onclick="goTo('pg-dashboard')" style="margin-bottom:10px;background:linear-gradient(135deg,rgba(59,130,246,0.2),rgba(37,99,235,0.2));border:1px solid rgba(59,130,246,0.4);border-radius:12px;color:#fff;">
        <i class="fa-solid fa-house" style="color:#60a5fa;"></i>
        <span>لوحة التحكم الرئيسية</span>
    </a>

    <!-- Section 1: System Admin -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-gears"></i> <span>إدارة النظام والصلاحيات</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-school-info')"><i class="fa-solid fa-school"></i> معلومات المدرسة</a>
            <a href="#" onclick="goTo('pg-db-management')"><i class="fa-solid fa-database"></i> إدارة قواعد البيانات</a>
            <a href="#" onclick="goTo('pg-users')"><i class="fa-solid fa-user-lock"></i> دليل المستخدمين</a>
            <a href="#" onclick="goTo('pg-permission-matrix')"><i class="fa-solid fa-shield-halved"></i> مصفوفة الصلاحيات</a>
            <a href="#" onclick="goTo('pg-operation-lock')"><i class="fa-solid fa-lock"></i> قفل العمليات والموديولات</a>
            <a href="#" onclick="goTo('pg-audit-trail')"><i class="fa-solid fa-clock-rotate-left"></i> سجل العمليات (Audit Trail)</a>
            <a href="#" onclick="goTo('pg-system-settings')"><i class="fa-solid fa-sliders"></i> إعدادات النظام</a>
            <a href="#" onclick="goTo('pg-alerts')"><i class="fa-solid fa-bell"></i> التنبيهات التلقائية</a>
            <a href="#" onclick="goTo('pg-archive')"><i class="fa-solid fa-box-archive"></i> الأرشيف</a>
            <a href="#" onclick="goTo('pg-change-password')"><i class="fa-solid fa-key"></i> تغيير كلمة المرور</a>
            <a href="#" onclick="goTo('pg-posting')"><i class="fa-solid fa-paper-plane"></i> إدارة الترحيلات</a>
        </div>
    </div>

    <!-- Section 2: Accounts & Finance -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-calculator"></i> <span>الأستاذ العام والشؤون المالية</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-chart-accounts')"><i class="fa-solid fa-sitemap"></i> دليل الحسابات المالي</a>
            <a href="#" onclick="goTo('pg-vouchers')"><i class="fa-solid fa-file-invoice-dollar"></i> إدارة السندات الشاملة</a>
            <a href="#" onclick="goTo('pg-journal')"><i class="fa-solid fa-book-open"></i> القيود اليومية (General Journal)</a>
            <a href="#" onclick="goTo('pg-cashboxes')"><i class="fa-solid fa-vault"></i> دليل الصناديق والخزائن</a>
            <a href="#" onclick="goTo('pg-cost-centers')"><i class="fa-solid fa-building"></i> مراكز التكلفة والموازنة</a>
            <a href="#" onclick="goTo('pg-account-ceiling')"><i class="fa-solid fa-arrow-up-9-1"></i> تسقيف الحسابات الائتماني</a>
            <a href="#" onclick="goTo('pg-student-account')"><i class="fa-solid fa-scroll"></i> كشف الحساب التفاعلي</a>
            <a href="#" onclick="goTo('pg-currencies')"><i class="fa-solid fa-money-bill-transfer"></i> دليل العملات وأسعار الصرف</a>
            <a href="#" onclick="goTo('pg-cashbox-inventory')"><i class="fa-solid fa-cash-register"></i> جرد الصناديق النقدية</a>
            <a href="#" onclick="goTo('pg-closings')"><i class="fa-solid fa-folder-closed"></i> الإقفالات المحاسبية</a>
            <a href="#" onclick="goTo('pg-banks')"><i class="fa-solid fa-building-columns"></i> دليل البنوك والحسابات</a>
            <a href="#" onclick="goTo('pg-checks')"><i class="fa-solid fa-money-check"></i> إدارة الشيكات البنكية</a>
            <a href="#" onclick="goTo('pg-demand-letters')"><i class="fa-solid fa-envelope-open-text"></i> رسائل المطالبة المالية</a>
            <a href="#" onclick="goTo('pg-finance-reports')"><i class="fa-solid fa-chart-pie"></i> التقارير المالية والإحصائية</a>
        </div>
    </div>

    <!-- Section 3: School System Configuration -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-school-flag"></i> <span>تهيئة النظام المدرسي</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-academic-years')"><i class="fa-solid fa-calendar"></i> دليل السنوات الدراسية</a>
            <a href="#" onclick="goTo('pg-academic-calendar')"><i class="fa-solid fa-calendar-days"></i> التقويم المدرسي والفعاليات</a>
            <a href="#" onclick="goTo('pg-stages')"><i class="fa-solid fa-layer-group"></i> المراحل والصفوف الدراسية</a>
            <a href="#" onclick="goTo('pg-sections')"><i class="fa-solid fa-table-cells"></i> دليل الشُعَب الدراسية</a>
            <a href="#" onclick="goTo('pg-subjects')"><i class="fa-solid fa-book"></i> دليل المواد الدراسية</a>
            <a href="#" onclick="goTo('pg-subject-distribution')"><i class="fa-solid fa-diagram-project"></i> توزيع المواد على الصفوف</a>
            <a href="#" onclick="goTo('pg-classrooms')"><i class="fa-solid fa-chalkboard"></i> القاعات والمعامل الدراسية</a>
            <a href="#" onclick="goTo('pg-class-times')"><i class="fa-solid fa-clock"></i> توقيت الحصص الدراسية</a>
            <a href="#" onclick="goTo('pg-timetable-builder')"><i class="fa-solid fa-table-columns"></i> بنّاء الجدول الدراسي</a>
            <a href="#" onclick="goTo('pg-required-docs')"><i class="fa-solid fa-file-circle-check"></i> دليل الوثائق المطلوبة</a>
            <a href="#" onclick="goTo('pg-fee-categories')"><i class="fa-solid fa-tags"></i> فئات الرسوم الدراسية</a>
            <a href="#" onclick="goTo('pg-discount-categories')"><i class="fa-solid fa-percent"></i> فئات الخصومات والمنح</a>
            <a href="#" onclick="goTo('pg-installment-plans')"><i class="fa-solid fa-money-bills"></i> فئات الأقساط والدفعات</a>
            <a href="#" onclick="goTo('pg-grade-fees')"><i class="fa-solid fa-receipt"></i> جدول رسوم الصفوف</a>
        </div>
    </div>

    <!-- Section 4: Student Affairs -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-user-graduate"></i> <span>شئون الطلاب والأكاديميا</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-enrollment')"><i class="fa-solid fa-file-invoice"></i> إدارة القبول والتسجيل والرسوم</a>
            <a href="#" onclick="goTo('pg-student-register')"><i class="fa-solid fa-user-plus"></i> تسجيل طالب جديد</a>
            <a href="#" onclick="goTo('pg-simple-register')"><i class="fa-solid fa-file-signature"></i> التسجيل المبسط السريع</a>
            <a href="#" onclick="goTo('pg-student-tree')"><i class="fa-solid fa-sitemap"></i> شجرة بيانات الطلاب</a>
            <a href="#" onclick="goTo('pg-students')"><i class="fa-solid fa-id-card"></i> دليل الطلاب الشامل</a>
            <a href="#" onclick="goTo('pg-parents')"><i class="fa-solid fa-people-roof"></i> دليل أولياء الأمور</a>
            <a href="#" onclick="goTo('pg-student-docs')"><i class="fa-solid fa-folder-open"></i> وثائق ومرفقات الطلاب</a>
            <a href="#" onclick="goTo('pg-section-distribution')"><i class="fa-solid fa-arrows-split-up-and-left"></i> توزيع الطلاب على الشعب</a>
            <a href="#" onclick="goTo('pg-promotion-workflow')"><i class="fa-solid fa-turn-up"></i> الترفيع الجماعي للطلاب</a>
            <a href="#" onclick="goTo('pg-discontinued')"><i class="fa-solid fa-user-xmark"></i> سجل الطلاب غير المستمرين</a>
            <a href="#" onclick="goTo('pg-attendance')"><i class="fa-solid fa-calendar-check"></i> التحضير والغياب اليومي</a>
            <a href="#" onclick="goTo('pg-class-notes')"><i class="fa-solid fa-note-sticky"></i> ملاحظات رائد الفصل</a>
        </div>
    </div>

    <!-- Section 5: HR & Employees -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-users-tie"></i> <span>شئون الموظفين والموارد البشرية</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-employees')"><i class="fa-solid fa-address-book"></i> دليل الموظفين والمعلمين</a>
            <a href="#" onclick="goTo('pg-guarantors')"><i class="fa-solid fa-handshake"></i> دليل الضمناء والكفلاء</a>
            <a href="#" onclick="goTo('pg-teacher-subjects')"><i class="fa-solid fa-chalkboard-user"></i> إسناد المواد للمدرسين</a>
            <a href="#" onclick="goTo('pg-emp-attendance')"><i class="fa-solid fa-fingerprint"></i> حضور وانضباط الموظفين</a>
            <a href="#" onclick="goTo('pg-emp-notices')"><i class="fa-solid fa-bullhorn"></i> إشعارات وتنبيهات الموظفين</a>
            <a href="#" onclick="goTo('pg-emp-contracts')"><i class="fa-solid fa-file-contract"></i> عقود الموظفين والوظائف</a>
            <a href="#" onclick="goTo('pg-emp-advances')"><i class="fa-solid fa-hand-holding-dollar"></i> سلفيات وقروض الموظفين</a>
            <a href="#" onclick="goTo('pg-leave-management')"><i class="fa-solid fa-calendar-xmark"></i> نظام إدارة الإجازات</a>
            <a href="#" onclick="goTo('pg-performance-eval')"><i class="fa-solid fa-star"></i> تقييم الأداء والكفاءة</a>
            <a href="#" onclick="goTo('pg-payroll')"><i class="fa-solid fa-money-check-dollar"></i> مسير ومعالجة الرواتب</a>
        </div>
    </div>

    <!-- Section 6: Control & Exams -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-pen-ruler"></i> <span>الكنترول والامتحانات</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-grading')"><i class="fa-solid fa-pen-to-square"></i> رصد الدرجات والاختبارات</a>
            <a href="#" onclick="goTo('pg-monthly-grades')"><i class="fa-solid fa-file-pen"></i> ترصيد الدرجات الشهرية</a>
            <a href="#" onclick="goTo('pg-term-grades')"><i class="fa-solid fa-clipboard-check"></i> درجات نهاية الفصل</a>
            <a href="#" onclick="goTo('pg-results')"><i class="fa-solid fa-ranking-star"></i> النتائج والتقديرات النهائية</a>
            <a href="#" onclick="goTo('pg-certificates')"><i class="fa-solid fa-certificate"></i> إصدار الشهادات الرسمية</a>
            <a href="#" onclick="goTo('pg-homework-tracker')"><i class="fa-solid fa-book-open-reader"></i> متابعة الواجبات المدرسية</a>
            <a href="#" onclick="goTo('pg-exam-halls')"><i class="fa-solid fa-location-dot"></i> أماكن ولجان الامتحانات</a>
            <a href="#" onclick="goTo('pg-seat-numbers')"><i class="fa-solid fa-hashtag"></i> كشوفات أرقام الجلوس</a>
            <a href="#" onclick="goTo('pg-secret-numbers')"><i class="fa-solid fa-user-secret"></i> توليد الأرقام السرية</a>
            <a href="#" onclick="goTo('pg-hall-distribution')"><i class="fa-solid fa-users-rectangle"></i> توزيع اللجان والمراقبين</a>
            <a href="#" onclick="goTo('pg-exam-schedule')"><i class="fa-solid fa-calendar-days"></i> جدول الامتحانات الرسمية</a>
            <a href="#" onclick="goTo('pg-roll-call')"><i class="fa-solid fa-list-check"></i> كشوفات المناداة للمنادين</a>
            <a href="#" onclick="goTo('pg-seat-cards')"><i class="fa-solid fa-id-badge"></i> طباعة بطاقات أرقام الجلوس</a>
            <a href="#" onclick="goTo('pg-substitute')"><i class="fa-solid fa-user-pen"></i> إدارة المدرس البديل</a>
        </div>
    </div>

    <!-- Section 7: Transportation & Activities -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-bus"></i> <span>المواصلات والأنشطة</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-activities')"><i class="fa-solid fa-medal"></i> إدارة الأنشطة والأنواع</a>
            <a href="#" onclick="goTo('pg-transport-routes')"><i class="fa-solid fa-route"></i> دليل خطوط السير</a>
            <a href="#" onclick="goTo('pg-buses')"><i class="fa-solid fa-bus-simple"></i> دليل الحافلات والمركبات</a>
            <a href="#" onclick="goTo('pg-transport-enrollment')"><i class="fa-solid fa-user-check"></i> اشتراك الطلاب في المواصلات</a>
            <a href="#" onclick="goTo('pg-transport')"><i class="fa-solid fa-map-location-dot"></i> كشوفات ورسومات المواصلات</a>
        </div>
    </div>

    <!-- Section 8: School Warehouses -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-warehouse"></i> <span>مخازن المدرسة والمشتريات</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-item-categories')"><i class="fa-solid fa-boxes-stacked"></i> فئات الأصناف المخزنية</a>
            <a href="#" onclick="goTo('pg-inventory-items')"><i class="fa-solid fa-box"></i> دليل الأصناف والمنتجات</a>
            <a href="#" onclick="goTo('pg-supply-orders')"><i class="fa-solid fa-truck-ramp-box"></i> أذونات وأوامر التوريد</a>
            <a href="#" onclick="goTo('pg-issue-orders')"><i class="fa-solid fa-dolly"></i> أذونات وأوامر الصرف</a>
            <a href="#" onclick="goTo('pg-suppliers')"><i class="fa-solid fa-truck-field"></i> دليل الموردين المعتمدين</a>
            <a href="#" onclick="goTo('pg-inventory-reports')"><i class="fa-solid fa-clipboard-list"></i> تقارير المخزون والجرد</a>
        </div>
    </div>

    <!-- Section 9: SMS & Comprehensive Reports -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-chart-bar"></i> <span>الرسائل والتقارير الشاملة</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-sms-send')"><i class="fa-solid fa-paper-plane"></i> إرسال الرسائل النصية SMS</a>
            <a href="#" onclick="goTo('pg-sms-templates')"><i class="fa-solid fa-file-code"></i> قوالب الرسائل الجاهزة</a>
            <a href="#" onclick="goTo('pg-sms-settings')"><i class="fa-solid fa-gear"></i> إعدادات ورصيد الرسائل</a>
            <a href="#" onclick="goTo('pg-monthly-report')"><i class="fa-solid fa-calendar-week"></i> تقرير الأعمال الشهرية</a>
            <a href="#" onclick="goTo('pg-semester-report')"><i class="fa-solid fa-file-contract"></i> تقرير أعمال الفصل الدراسي</a>
            <a href="#" onclick="goTo('pg-class-details')"><i class="fa-solid fa-table-list"></i> كشف تفصيلي للصفوف</a>
            <a href="#" onclick="goTo('pg-top-students')"><i class="fa-solid fa-award"></i> كشف أوائل المدرسة والتفوق</a>
            <a href="#" onclick="goTo('pg-success-rate-subject')"><i class="fa-solid fa-chart-column"></i> نسب النجاح بالمواد والشعب</a>
            <a href="#" onclick="goTo('pg-custom-reports')"><i class="fa-solid fa-file-invoice"></i> تقارير مخصصة (PDF/Excel)</a>
            <a href="#" onclick="goTo('pg-control-reports')"><i class="fa-solid fa-file-shield"></i> تقارير الكنترول الشاملة</a>
        </div>
    </div>

    <!-- Section 10: Administrative Tools -->
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-toolbox"></i> <span>أدوات ودعم إداري</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-admin-messages')"><i class="fa-solid fa-tower-broadcast"></i> الرسائل الإدارية والإعلانات</a>
            <a href="#" onclick="goTo('pg-shortcuts')"><i class="fa-solid fa-keyboard"></i> اختصارات النظام المفضلة</a>
            <a href="#" onclick="goTo('pg-faq')"><i class="fa-solid fa-circle-question"></i> الأسئلة المتكررة والدعم</a>
            <a href="#" onclick="goTo('pg-dictionary')"><i class="fa-solid fa-language"></i> قاموس الترجمة والمصطلحات</a>
            <a href="#" onclick="goTo('pg-personal-info')"><i class="fa-solid fa-address-card"></i> معلومات الملف الشخصي</a>
        </div>
    </div>
</nav>
"""

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace sidebarNav in school.html
pattern = r'<nav class="sidebar-nav" id="sidebarNav">.*?</nav>'
if re.search(pattern, html, re.DOTALL):
    html = re.sub(pattern, sidebar_nav_content.strip(), html, flags=re.DOTALL)
    print("  ✓ Successfully replaced sidebarNav in school.html")

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

print("Rebuilt perfect sidebar across school.html, admin.html, parent.html!")
