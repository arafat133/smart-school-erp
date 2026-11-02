import os
import re
from master_fix_all import MODULES

html_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\school.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the entire sidebar nav section
sidebar_nav_content = """<nav class="sidebar-nav" id="sidebarNav">
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-gears"></i> <span>إدارة النظام</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-school-info')"><i class="fa-solid fa-school"></i> معلومات المدرسة</a>
            <a href="#" onclick="goTo('pg-db-management')"><i class="fa-solid fa-database"></i> إدارة قواعد البيانات</a>
            <a href="#" onclick="goTo('pg-users')"><i class="fa-solid fa-user-lock"></i> دليل المستخدمين</a>
            <a href="#" onclick="goTo('pg-operation-lock')"><i class="fa-solid fa-lock"></i> قفل العمليات</a>
            <a href="#" onclick="goTo('pg-system-settings')"><i class="fa-solid fa-sliders"></i> إعدادات النظام</a>
            <a href="#" onclick="goTo('pg-audit')"><i class="fa-solid fa-clock-rotate-left"></i> المحفوظات وسجل العمليات</a>
            <a href="#" onclick="goTo('pg-alerts')"><i class="fa-solid fa-bell"></i> التنبيهات التلقائية</a>
            <a href="#" onclick="goTo('pg-archive')"><i class="fa-solid fa-box-archive"></i> الأرشيف</a>
            <a href="#" onclick="goTo('pg-change-password')"><i class="fa-solid fa-key"></i> تغيير كلمة المرور</a>
            <a href="#" onclick="goTo('pg-posting')"><i class="fa-solid fa-paper-plane"></i> إدارة الترحيلات</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-calculator"></i> <span>الأستاذ العام</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-chart-accounts')"><i class="fa-solid fa-sitemap"></i> دليل الحسابات</a>
            <a href="#" onclick="goTo('pg-currencies')"><i class="fa-solid fa-money-bill-transfer"></i> دليل العملات</a>
            <a href="#" onclick="goTo('pg-cashboxes')"><i class="fa-solid fa-vault"></i> دليل الصناديق</a>
            <a href="#" onclick="goTo('pg-cost-centers')"><i class="fa-solid fa-building"></i> مراكز التكلفة</a>
            <a href="#" onclick="goTo('pg-account-ceiling')"><i class="fa-solid fa-arrow-up-9-1"></i> تسقيف الحسابات</a>
            <a href="#" onclick="goTo('pg-voucher-payment')"><i class="fa-solid fa-arrow-up"></i> سند صرف</a>
            <a href="#" onclick="goTo('pg-voucher-receipt')"><i class="fa-solid fa-arrow-down"></i> سند قبض</a>
            <a href="#" onclick="goTo('pg-journal')"><i class="fa-solid fa-book-open"></i> القيود اليومية</a>
            <a href="#" onclick="goTo('pg-cashbox-inventory')"><i class="fa-solid fa-cash-register"></i> جرد الصندوق</a>
            <a href="#" onclick="goTo('pg-closings')"><i class="fa-solid fa-folder-closed"></i> الإقفالات المحاسبية</a>
            <a href="#" onclick="goTo('pg-banks')"><i class="fa-solid fa-building-columns"></i> دليل البنوك</a>
            <a href="#" onclick="goTo('pg-checks')"><i class="fa-solid fa-money-check"></i> إدارة الشيكات</a>
            <a href="#" onclick="goTo('pg-acc-statement')"><i class="fa-solid fa-scroll"></i> كشف الحساب</a>
            <a href="#" onclick="goTo('pg-trial-balance')"><i class="fa-solid fa-scale-balanced"></i> ميزان المراجعة</a>
            <a href="#" onclick="goTo('pg-income-stmt')"><i class="fa-solid fa-chart-line"></i> قائمة الدخل</a>
            <a href="#" onclick="goTo('pg-balance-sheet')"><i class="fa-solid fa-landmark"></i> قائمة المركز المالي</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-school-flag"></i> <span>تهيئة النظام</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-academic-years')"><i class="fa-solid fa-calendar"></i> دليل السنوات</a>
            <a href="#" onclick="goTo('pg-departments')"><i class="fa-solid fa-building-user"></i> دليل الأقسام</a>
            <a href="#" onclick="goTo('pg-stages')"><i class="fa-solid fa-layer-group"></i> المراحل والصفوف</a>
            <a href="#" onclick="goTo('pg-required-docs')"><i class="fa-solid fa-file-circle-check"></i> الوثائق المطلوبة</a>
            <a href="#" onclick="goTo('pg-nationalities')"><i class="fa-solid fa-flag"></i> دليل الجنسيات</a>
            <a href="#" onclick="goTo('pg-violations-catalog')"><i class="fa-solid fa-triangle-exclamation"></i> المخالفات السلوكية</a>
            <a href="#" onclick="goTo('pg-visitors')"><i class="fa-solid fa-person-walking-arrow-right"></i> سجل الزوار</a>
            <a href="#" onclick="goTo('pg-academic-calendar')"><i class="fa-solid fa-calendar-days"></i> التقويم المدرسي</a>
            <a href="#" onclick="goTo('pg-classrooms')"><i class="fa-solid fa-chalkboard"></i> القاعات الدراسية</a>
            <a href="#" onclick="goTo('pg-grade-progression')"><i class="fa-solid fa-stairs"></i> تدرج الصفوف</a>
            <a href="#" onclick="goTo('pg-sections')"><i class="fa-solid fa-table-cells"></i> دليل الشُعَب</a>
            <a href="#" onclick="goTo('pg-subjects')"><i class="fa-solid fa-book"></i> دليل المواد</a>
            <a href="#" onclick="goTo('pg-subject-distribution')"><i class="fa-solid fa-diagram-project"></i> توزيع المواد</a>
            <a href="#" onclick="goTo('pg-grade-types')"><i class="fa-solid fa-list-ol"></i> أنواع الدرجات</a>
            <a href="#" onclick="goTo('pg-grade-ratings')"><i class="fa-solid fa-star"></i> دليل التقديرات</a>
            <a href="#" onclick="goTo('pg-fee-categories')"><i class="fa-solid fa-tags"></i> فئات الرسوم</a>
            <a href="#" onclick="goTo('pg-discount-categories')"><i class="fa-solid fa-percent"></i> فئات الخصم</a>
            <a href="#" onclick="goTo('pg-installment-plans')"><i class="fa-solid fa-money-bills"></i> فئات الأقساط</a>
            <a href="#" onclick="goTo('pg-grade-fees')"><i class="fa-solid fa-receipt"></i> رسوم الصفوف</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-user-graduate"></i> <span>شئون الطلاب</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-student-tree')"><i class="fa-solid fa-sitemap"></i> شجرة الطلاب</a>
            <a href="#" onclick="goTo('pg-students')"><i class="fa-solid fa-id-card"></i> دليل الطلاب</a>
            <a href="#" onclick="goTo('pg-parents')"><i class="fa-solid fa-people-roof"></i> دليل أولياء الأمور</a>
            <a href="#" onclick="goTo('pg-student-docs')"><i class="fa-solid fa-folder-open"></i> وثائق الطلاب</a>
            <a href="#" onclick="goTo('pg-section-distribution')"><i class="fa-solid fa-arrows-split-up-and-left"></i> توزيع الطلاب</a>
            <a href="#" onclick="goTo('pg-discontinued')"><i class="fa-solid fa-user-xmark"></i> الطلاب غير المستمرين</a>
            <a href="#" onclick="goTo('pg-attendance')"><i class="fa-solid fa-calendar-check"></i> التحضير اليومي</a>
            <a href="#" onclick="goTo('pg-behavior')"><i class="fa-solid fa-clipboard-list"></i> السلوك والمخالفات</a>
            <a href="#" onclick="goTo('pg-class-notes')"><i class="fa-solid fa-note-sticky"></i> ملاحظات الرائد</a>
            <a href="#" onclick="goTo('pg-enrollment')"><i class="fa-solid fa-file-invoice"></i> التسجيل والرسوم</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-users-tie"></i> <span>شئون الموظفين</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-employees')"><i class="fa-solid fa-address-book"></i> دليل الموظفين</a>
            <a href="#" onclick="goTo('pg-guarantors')"><i class="fa-solid fa-handshake"></i> دليل الضمناء</a>
            <a href="#" onclick="goTo('pg-teacher-subjects')"><i class="fa-solid fa-chalkboard-user"></i> إسناد المواد</a>
            <a href="#" onclick="goTo('pg-emp-attendance')"><i class="fa-solid fa-fingerprint"></i> حضور الموظفين</a>
            <a href="#" onclick="goTo('pg-emp-notices')"><i class="fa-solid fa-bullhorn"></i> إشعارات وتنبيهات</a>
            <a href="#" onclick="goTo('pg-emp-contracts')"><i class="fa-solid fa-file-contract"></i> عقود الموظفين</a>
            <a href="#" onclick="goTo('pg-emp-advances')"><i class="fa-solid fa-hand-holding-dollar"></i> سلفيات الموظفين</a>
            <a href="#" onclick="goTo('pg-payroll')"><i class="fa-solid fa-money-check-dollar"></i> مسير الرواتب</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-pen-ruler"></i> <span>الكنترول والامتحانات</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-grading')"><i class="fa-solid fa-pen-to-square"></i> رصد الدرجات</a>
            <a href="#" onclick="goTo('pg-results')"><i class="fa-solid fa-ranking-star"></i> النتائج النهائية</a>
            <a href="#" onclick="goTo('pg-exam-halls')"><i class="fa-solid fa-location-dot"></i> أماكن اللجان</a>
            <a href="#" onclick="goTo('pg-seat-numbers')"><i class="fa-solid fa-hashtag"></i> أرقام الجلوس</a>
            <a href="#" onclick="goTo('pg-secret-numbers')"><i class="fa-solid fa-user-secret"></i> الأرقام السرية</a>
            <a href="#" onclick="goTo('pg-hall-distribution')"><i class="fa-solid fa-users-rectangle"></i> توزيع اللجان</a>
            <a href="#" onclick="goTo('pg-exam-schedule')"><i class="fa-solid fa-calendar-days"></i> جدول الامتحانات</a>
            <a href="#" onclick="goTo('pg-roll-call')"><i class="fa-solid fa-list-check"></i> كشوفات المناداة</a>
            <a href="#" onclick="goTo('pg-seat-cards')"><i class="fa-solid fa-id-badge"></i> بطاقات أرقام الجلوس</a>
            <a href="#" onclick="goTo('pg-schedule')"><i class="fa-solid fa-table-columns"></i> الجدول الدراسي</a>
            <a href="#" onclick="goTo('pg-certificates')"><i class="fa-solid fa-certificate"></i> الشهادات</a>
            <a href="#" onclick="goTo('pg-promotion')"><i class="fa-solid fa-turn-up"></i> ترفيع الطلاب</a>
            <a href="#" onclick="goTo('pg-substitute')"><i class="fa-solid fa-user-pen"></i> المدرس البديل</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-trophy"></i> <span>الأنشطة الطلابية</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-activity-types')"><i class="fa-solid fa-icons"></i> أنواع الأنشطة</a>
            <a href="#" onclick="goTo('pg-activities')"><i class="fa-solid fa-medal"></i> إدارة الأنشطة</a>
            <a href="#" onclick="goTo('pg-activity-supervisors')"><i class="fa-solid fa-person-chalkboard"></i> المرافقون في الأنشطة</a>
            <a href="#" onclick="goTo('pg-activity-enrollment')"><i class="fa-solid fa-clipboard-user"></i> اشتراك الطلاب</a>
            <a href="#" onclick="goTo('pg-activity-reports')"><i class="fa-solid fa-file-waveform"></i> كشوفات الأنشطة</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-bus"></i> <span>المواصلات</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-transport-routes')"><i class="fa-solid fa-route"></i> دليل خطوط السير</a>
            <a href="#" onclick="goTo('pg-buses')"><i class="fa-solid fa-bus-simple"></i> دليل الحافلات</a>
            <a href="#" onclick="goTo('pg-transport-enrollment')"><i class="fa-solid fa-user-check"></i> اشتراك الطلاب</a>
            <a href="#" onclick="goTo('pg-transport')"><i class="fa-solid fa-map-location-dot"></i> كشوفات المواصلات</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-coins"></i> <span>الشؤون المالية</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-fee-receipt')"><i class="fa-solid fa-receipt"></i> سند قبض الرسوم</a>
            <a href="#" onclick="goTo('pg-demand-letters')"><i class="fa-solid fa-envelope-open-text"></i> رسائل المطالبة</a>
            <a href="#" onclick="goTo('pg-student-account')"><i class="fa-solid fa-file-invoice-dollar"></i> كشف حساب الطالب</a>
            <a href="#" onclick="goTo('pg-finance-reports')"><i class="fa-solid fa-chart-pie"></i> التقارير المالية</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-warehouse"></i> <span>مخازن المدرسة</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-item-categories')"><i class="fa-solid fa-boxes-stacked"></i> فئات الأصناف</a>
            <a href="#" onclick="goTo('pg-inventory-items')"><i class="fa-solid fa-box"></i> الأصناف المخزنية</a>
            <a href="#" onclick="goTo('pg-supply-orders')"><i class="fa-solid fa-truck-ramp-box"></i> أوامر التوريد</a>
            <a href="#" onclick="goTo('pg-issue-orders')"><i class="fa-solid fa-dolly"></i> أوامر الصرف</a>
            <a href="#" onclick="goTo('pg-suppliers')"><i class="fa-solid fa-truck-field"></i> دليل الموردين</a>
            <a href="#" onclick="goTo('pg-inventory-reports')"><i class="fa-solid fa-clipboard-list"></i> تقارير المخزون</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-comment-sms"></i> <span>الرسائل القصيرة</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-sms-settings')"><i class="fa-solid fa-gear"></i> إعدادات الربط</a>
            <a href="#" onclick="goTo('pg-sms-send')"><i class="fa-solid fa-paper-plane"></i> إرسال الرسائل</a>
            <a href="#" onclick="goTo('pg-sms-templates')"><i class="fa-solid fa-file-code"></i> قوالب الرسائل</a>
            <a href="#" onclick="goTo('pg-sms-balance')"><i class="fa-solid fa-coins"></i> الاشتراك والرصيد</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-chart-bar"></i> <span>التقارير الشاملة</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-monthly-report')"><i class="fa-solid fa-calendar-week"></i> تقرير الأعمال الشهرية</a>
            <a href="#" onclick="goTo('pg-semester-report')"><i class="fa-solid fa-file-contract"></i> تقرير أعمال الفصل</a>
            <a href="#" onclick="goTo('pg-class-details')"><i class="fa-solid fa-table-list"></i> كشف تفصيلي للصفوف</a>
            <a href="#" onclick="goTo('pg-top-students')"><i class="fa-solid fa-award"></i> كشف أوائل المدرسة</a>
            <a href="#" onclick="goTo('pg-success-rate-subject')"><i class="fa-solid fa-chart-column"></i> نسبة النجاح بالمواد</a>
            <a href="#" onclick="goTo('pg-success-rate-section')"><i class="fa-solid fa-chart-area"></i> نسبة النجاح بالشعب</a>
            <a href="#" onclick="goTo('pg-control-reports')"><i class="fa-solid fa-file-shield"></i> تقارير الكنترول</a>
            <a href="#" onclick="goTo('pg-homework')"><i class="fa-solid fa-book-open-reader"></i> الواجبات اليومية</a>
        </div>
    </div>
    
    <div class="nav-section">
        <div class="nav-item has-sub" onclick="toggleSub(this)">
            <i class="fa-solid fa-toolbox"></i> <span>أدوات إدارية</span> <i class="fa-solid fa-chevron-down ms-auto" style="font-size:0.8rem"></i>
        </div>
        <div class="sub-menu">
            <a href="#" onclick="goTo('pg-admin-messages')"><i class="fa-solid fa-tower-broadcast"></i> الرسائل الإدارية</a>
            <a href="#" onclick="goTo('pg-shortcuts')"><i class="fa-solid fa-keyboard"></i> اختصارات النظام</a>
            <a href="#" onclick="goTo('pg-faq')"><i class="fa-solid fa-circle-question"></i> الأسئلة المتكررة</a>
            <a href="#" onclick="goTo('pg-dictionary')"><i class="fa-solid fa-language"></i> قاموس الترجمة</a>
            <a href="#" onclick="goTo('pg-personal-info')"><i class="fa-solid fa-address-card"></i> معلومات شخصية</a>
        </div>
    </div>
</nav>"""

# Replace in content
content = re.sub(r'<nav class="sidebar-nav" id="sidebarNav">.*?</nav>', sidebar_nav_content, content, flags=re.DOTALL)

# Find existing pages to not duplicate them
existing_pages = re.findall(r'<div class="page" id="([^"]+)">', content)

pages_data = [
    ("pg-school-info", "معلومات المدرسة", "fa-school", "table"),
    ("pg-db-management", "إدارة قواعد البيانات", "fa-database", "db"),
    ("pg-users", "دليل المستخدمين", "fa-user-lock", "table"),
    ("pg-operation-lock", "قفل العمليات", "fa-lock", "table"),
    ("pg-system-settings", "إعدادات النظام", "fa-sliders", "settings"),
    ("pg-audit", "المحفوظات وسجل العمليات", "fa-clock-rotate-left", "table"),
    ("pg-alerts", "التنبيهات التلقائية", "fa-bell", "table"),
    ("pg-archive", "الأرشيف", "fa-box-archive", "table"),
    ("pg-change-password", "تغيير كلمة المرور", "fa-key", "password"),
    ("pg-posting", "إدارة الترحيلات", "fa-paper-plane", "table"),
    
    ("pg-chart-accounts", "دليل الحسابات", "fa-sitemap", "table"),
    ("pg-currencies", "دليل العملات وأسعار الصرف", "fa-money-bill-transfer", "table"),
    ("pg-cashboxes", "دليل الصناديق", "fa-vault", "table"),
    ("pg-cost-centers", "مراكز التكلفة", "fa-building", "table"),
    ("pg-account-ceiling", "تسقيف الحسابات", "fa-arrow-up-9-1", "table"),
    ("pg-voucher-payment", "سند صرف", "fa-arrow-up", "table"),
    ("pg-voucher-receipt", "سند قبض", "fa-arrow-down", "table"),
    ("pg-journal", "القيود اليومية", "fa-book-open", "table"),
    ("pg-cashbox-inventory", "جرد الصندوق", "fa-cash-register", "table"),
    ("pg-closings", "الإقفالات المحاسبية", "fa-folder-closed", "table"),
    ("pg-banks", "دليل البنوك", "fa-building-columns", "table"),
    ("pg-checks", "إدارة الشيكات", "fa-money-check", "table"),
    ("pg-acc-statement", "كشف الحساب", "fa-scroll", "table"),
    ("pg-trial-balance", "ميزان المراجعة", "fa-scale-balanced", "table"),
    ("pg-income-stmt", "قائمة الدخل", "fa-chart-line", "table"),
    ("pg-balance-sheet", "قائمة المركز المالي", "fa-landmark", "table"),

    ("pg-academic-years", "دليل السنوات الدراسية", "fa-calendar", "table"),
    ("pg-departments", "دليل الأقسام", "fa-building-user", "table"),
    ("pg-stages", "المراحل والصفوف الدراسية", "fa-layer-group", "table"),
    ("pg-required-docs", "دليل الوثائق المطلوبة", "fa-file-circle-check", "table"),
    ("pg-nationalities", "دليل الجنسيات", "fa-flag", "table"),
    ("pg-violations-catalog", "دليل المخالفات السلوكية", "fa-triangle-exclamation", "table"),
    ("pg-visitors", "سجل الزوار", "fa-person-walking-arrow-right", "table"),
    ("pg-academic-calendar", "التقويم المدرسي", "fa-calendar-days", "calendar"),
    ("pg-classrooms", "القاعات الدراسية", "fa-chalkboard", "table"),
    ("pg-grade-progression", "تدرج الصفوف", "fa-stairs", "table"),
    ("pg-sections", "دليل الشُعَب", "fa-table-cells", "table"),
    ("pg-subjects", "دليل المواد الدراسية", "fa-book", "table"),
    ("pg-subject-distribution", "توزيع المواد على الصفوف", "fa-diagram-project", "table"),
    ("pg-grade-types", "أنواع الدرجات", "fa-list-ol", "table"),
    ("pg-grade-ratings", "دليل التقديرات", "fa-star", "table"),
    ("pg-fee-categories", "فئات الرسوم الدراسية", "fa-tags", "table"),
    ("pg-discount-categories", "فئات الخصم", "fa-percent", "table"),
    ("pg-installment-plans", "فئات الأقساط", "fa-money-bills", "table"),
    ("pg-grade-fees", "رسوم الصفوف", "fa-receipt", "table"),

    ("pg-student-tree", "شجرة بيانات الطلاب", "fa-sitemap", "table"),
    ("pg-students", "دليل الطلاب", "fa-id-card", "table"),
    ("pg-parents", "دليل أولياء الأمور", "fa-people-roof", "table"),
    ("pg-student-docs", "وثائق الطلاب", "fa-folder-open", "table"),
    ("pg-section-distribution", "توزيع الطلاب على الشعب", "fa-arrows-split-up-and-left", "table"),
    ("pg-discontinued", "الطلاب غير المستمرين", "fa-user-xmark", "table"),
    ("pg-attendance", "التحضير اليومي", "fa-calendar-check", "table"),
    ("pg-behavior", "السلوك والمخالفات", "fa-clipboard-list", "table"),
    ("pg-class-notes", "ملاحظات رائد الفصل", "fa-note-sticky", "table"),
    ("pg-enrollment", "التسجيل السنوي والرسوم", "fa-file-invoice", "table"),

    ("pg-employees", "دليل الموظفين", "fa-address-book", "table"),
    ("pg-guarantors", "دليل الضمناء", "fa-handshake", "table"),
    ("pg-teacher-subjects", "إسناد المواد للمدرسين", "fa-chalkboard-user", "table"),
    ("pg-emp-attendance", "حضور الموظفين", "fa-fingerprint", "table"),
    ("pg-emp-notices", "إشعارات وتنبيهات الموظفين", "fa-bullhorn", "table"),
    ("pg-emp-contracts", "عقود الموظفين", "fa-file-contract", "table"),
    ("pg-emp-advances", "سلفيات الموظفين", "fa-hand-holding-dollar", "table"),
    ("pg-payroll", "مسير الرواتب", "fa-money-check-dollar", "table"),

    ("pg-grading", "رصد الدرجات", "fa-pen-to-square", "table"),
    ("pg-results", "النتائج النهائية", "fa-ranking-star", "table"),
    ("pg-exam-halls", "دليل أماكن اللجان", "fa-location-dot", "table"),
    ("pg-seat-numbers", "أرقام الجلوس", "fa-hashtag", "table"),
    ("pg-secret-numbers", "الأرقام السرية", "fa-user-secret", "table"),
    ("pg-hall-distribution", "توزيع اللجان", "fa-users-rectangle", "table"),
    ("pg-exam-schedule", "جدول الامتحانات", "fa-calendar-days", "exam-schedule"),
    ("pg-roll-call", "كشوفات المناداة", "fa-list-check", "table"),
    ("pg-seat-cards", "بطاقات أرقام الجلوس", "fa-id-badge", "table"),
    ("pg-schedule", "الجدول الدراسي", "fa-table-columns", "schedule"),
    ("pg-certificates", "الشهادات", "fa-certificate", "table"),
    ("pg-promotion", "ترفيع الطلاب", "fa-turn-up", "table"),
    ("pg-substitute", "المدرس البديل", "fa-user-pen", "table"),

    ("pg-activity-types", "دليل أنواع الأنشطة", "fa-icons", "table"),
    ("pg-activities", "إدارة الأنشطة", "fa-medal", "table"),
    ("pg-activity-supervisors", "المرافقون في الأنشطة", "fa-person-chalkboard", "table"),
    ("pg-activity-enrollment", "اشتراك الطلاب في الأنشطة", "fa-clipboard-user", "table"),
    ("pg-activity-reports", "كشوفات الأنشطة", "fa-file-waveform", "table"),

    ("pg-transport-routes", "دليل خطوط السير", "fa-route", "table"),
    ("pg-buses", "دليل الحافلات", "fa-bus-simple", "table"),
    ("pg-transport-enrollment", "اشتراك الطلاب في المواصلات", "fa-user-check", "table"),
    ("pg-transport", "كشوفات المواصلات", "fa-map-location-dot", "table"),

    ("pg-fee-receipt", "سند قبض الرسوم الدراسية", "fa-receipt", "table"),
    ("pg-demand-letters", "رسائل المطالبة", "fa-envelope-open-text", "table"),
    ("pg-student-account", "كشف حساب الطالب", "fa-file-invoice-dollar", "table"),
    ("pg-finance-reports", "التقارير المالية للطلاب", "fa-chart-pie", "table"),

    ("pg-item-categories", "فئات الأصناف", "fa-boxes-stacked", "table"),
    ("pg-inventory-items", "الأصناف المخزنية", "fa-box", "table"),
    ("pg-supply-orders", "أوامر التوريد", "fa-truck-ramp-box", "table"),
    ("pg-issue-orders", "أوامر الصرف", "fa-dolly", "table"),
    ("pg-suppliers", "دليل الموردين", "fa-truck-field", "table"),
    ("pg-inventory-reports", "تقارير المخزون والجرد", "fa-clipboard-list", "table"),

    ("pg-sms-settings", "إعدادات الربط", "fa-gear", "table"),
    ("pg-sms-send", "إرسال الرسائل القصيرة", "fa-paper-plane", "sms"),
    ("pg-sms-templates", "قوالب الرسائل الجاهزة", "fa-file-code", "table"),
    ("pg-sms-balance", "الاشتراك والرصيد", "fa-coins", "sms-balance"),

    ("pg-monthly-report", "تقرير الأعمال الشهرية", "fa-calendar-week", "table"),
    ("pg-semester-report", "تقرير أعمال الفصل الدراسي", "fa-file-contract", "table"),
    ("pg-class-details", "كشف تفصيلي للصفوف", "fa-table-list", "table"),
    ("pg-top-students", "كشف أوائل المدرسة", "fa-award", "table"),
    ("pg-success-rate-subject", "نسبة النجاح بالمواد", "fa-chart-column", "table"),
    ("pg-success-rate-section", "نسبة النجاح بالشعب", "fa-chart-area", "table"),
    ("pg-control-reports", "تقارير الكنترول", "fa-file-shield", "table"),
    ("pg-homework", "الواجبات اليومية", "fa-book-open-reader", "table"),

    ("pg-admin-messages", "الرسائل الإدارية والإعلانات", "fa-tower-broadcast", "admin-messages"),
    ("pg-shortcuts", "اختصارات النظام", "fa-keyboard", "shortcuts"),
    ("pg-faq", "الأسئلة المتكررة", "fa-circle-question", "faq"),
    ("pg-dictionary", "قاموس الترجمة", "fa-language", "table"),
    ("pg-personal-info", "معلومات شخصية", "fa-address-card", "table"),
]

# Clean up redundant/duplicate pages if present in HTML content
redundant_page_ids = [
    "pg-user-groups", "pg-permissions", "pg-protected-groups",
    "pg-simple-entry", "pg-double-entry", "pg-class-times",
    "pg-student-register", "pg-simple-register", "pg-monthly-grades",
    "pg-term-grades", "pg-attendance-reports"
]
for r_id in redundant_page_ids:
    content = re.sub(fr'<div class="page"[^>]*id="{r_id}".*?</div>\s*(?=<div class="page"|<div id="toast"|</div>\s*<!-- toast|</div>\s*<div class="toast")', '', content, flags=re.DOTALL)


# We should REPLACE pg-schedule and pg-exam-schedule
# Let's remove them from content if they exist so we can recreate them
for target_id in ["pg-schedule", "pg-exam-schedule"]:
    # A basic regex to remove a div with a specific id
    content = re.sub(fr'<div class="page" id="{target_id}">.*?</div>\s*(?=<div class="page"|<div id="toast"|</div>\s*<!-- toast|</div>\s*<div class="toast")', '', content, flags=re.DOTALL)
    if target_id in existing_pages:
        existing_pages.remove(target_id)

new_pages_html = ""

for pg_id, title, icon, ptype in pages_data:
    if pg_id in existing_pages:
        continue
    
    html = f'''
<div class="page" id="{pg_id}">
    <div class="page-header"><button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button><h2><i class="fa-solid {icon}"></i> {title}</h2></div>'''

    if ptype == "table":
        raw = pg_id.replace("pg-", "")
        parts = raw.split("-")
        func_name = parts[0].capitalize() + "".join(p.capitalize() for p in parts[1:])
        
        headers = "<th>العنوان / الاسم</th><th>التفاصيل / البيان</th><th>إجراءات</th>"
        if raw in MODULES:
            headers = "".join([f"<th>{h}</th>" for h in MODULES[raw]['headers']])
        elif raw in ("operation-lock", "operation_lock"):
            func_name = "OperationLock"
            headers = "<th>اسم العملية / النظام</th><th>حالة القفل</th><th>تاريخ التعديل</th><th>السبب / التوضيح</th><th>إجراءات</th>"
        elif raw in ("alerts", "alert"):
            func_name = "Alerts"
            headers = "<th>عنوان التنبيه</th><th>نوع التنبيه</th><th>الفئة المستهدفة</th><th>الحالة</th><th>إجراءات</th>"
        elif raw == "archive":
            func_name = "Archive"
            headers = "<th>عنوان الوثيقة / السجل</th><th>التصنيف</th><th>رقم المرجع</th><th>التاريخ</th><th>إجراءات</th>"
        elif raw == "posting":
            func_name = "Posting"
            headers = "<th>اسم عملية الترحيل</th><th>نوع الترحيل</th><th>التاريخ</th><th>الحالة</th><th>إجراءات</th>"

        html += f'''
    <div class="toolbar">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="search{func_name}" placeholder="بحث..." oninput="render{func_name}()"></div>
        <button class="btn-add" onclick="openForm('{pg_id.replace("pg-", "")}')"><i class="fa-solid fa-plus"></i> إضافة</button>
    </div>
    <div class="table-wrapper"><table><thead><tr>{headers}</tr></thead><tbody id="tbl-{pg_id.replace('pg-', '')}"></tbody></table></div>'''
    
    elif ptype == "schedule":
        html += '''
    <div class="toolbar" style="justify-content:space-between; display:flex;">
        <div style="display:flex;gap:10px;">
            <div class="search-box">
                <select id="scheduleStageFilter" onchange="renderSchedule()">
                    <option value="">المرحلة</option>
                    <option value="الأساسية">الأساسية</option>
                    <option value="الثانوية">الثانوية</option>
                </select>
            </div>
            <div class="search-box">
                <select id="scheduleSectionFilter" onchange="renderSchedule()">
                    <option value="">الشعبة</option>
                    <option value="أ">أ</option>
                    <option value="ب">ب</option>
                </select>
            </div>
        </div>
        <div style="display:flex;gap:10px;align-items:center;">
            <span class="badge" style="background:var(--primary);color:white;padding:5px 10px;border-radius:6px;cursor:pointer;" onclick="openModal('termModal')"><i class="fa-solid fa-calendar-check"></i> <span id="currentTermSchedule">الفصل الدراسي الأول</span></span>
            <button class="btn-add" onclick="window.print()"><i class="fa-solid fa-print"></i> طباعة</button>
        </div>
    </div>
    <div class="table-wrapper" style="margin-bottom:20px;">
        <table class="matrix-table">
            <thead>
                <tr>
                    <th>اليوم / الحصة</th>
                    <th>الأولى</th><th>الثانية</th><th>الثالثة</th><th>الرابعة</th><th>الخامسة</th><th>السادسة</th><th>السابعة</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>السبت</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
                <tr><td>الأحد</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
                <tr><td>الإثنين</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
                <tr><td>الثلاثاء</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
                <tr><td>الأربعاء</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
            </tbody>
        </table>
    </div>
    <div class="table-wrapper">
        <table>
            <thead><tr><th>المادة</th><th>المدرس</th><th>الفصل</th><th>اليوم</th><th>الحصة</th></tr></thead>
            <tbody id="tbl-schedule-list"></tbody>
        </table>
    </div>'''
        
    elif ptype == "exam-schedule":
        html += '''
    <div class="toolbar" style="justify-content:space-between; display:flex;">
        <div style="display:flex;gap:10px;">
            <div class="search-box">
                <select id="examTypeFilter" onchange="renderExamSchedule()">
                    <option value="">نوع الامتحان</option>
                    <option value="اختبارات شهرية">اختبارات شهرية</option>
                    <option value="نهاية فصل">نهاية فصل</option>
                </select>
            </div>
            <div class="search-box">
                <select id="examStageFilter" onchange="renderExamSchedule()">
                    <option value="">المرحلة</option>
                </select>
            </div>
            <div class="search-box">
                <select id="examSectionFilter" onchange="renderExamSchedule()">
                    <option value="">الشعبة</option>
                </select>
            </div>
        </div>
        <div style="display:flex;gap:10px;align-items:center;">
            <span class="badge" style="background:var(--primary);color:white;padding:5px 10px;border-radius:6px;cursor:pointer;" onclick="openModal('termModal')"><i class="fa-solid fa-calendar-check"></i> <span id="currentTermExam">الفصل الدراسي الأول</span></span>
            <button class="btn-add" onclick="openForm('exam-schedule')"><i class="fa-solid fa-plus"></i> إضافة</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead><tr><th>الفصل الدراسي</th><th>نوع الامتحان</th><th>الصف</th><th>الشعبة</th><th>المادة</th><th>التاريخ</th><th>الوقت</th><th>القاعة</th><th>إجراءات</th></tr></thead>
            <tbody id="tbl-exam-schedule"></tbody>
        </table>
    </div>'''
        
    elif ptype == "db":
        html += '''
    <div style="padding:20px;display:flex;flex-direction:column;gap:15px;max-width:550px;background:var(--card-bg);border-radius:12px;box-shadow:var(--shadow-sm);margin:20px 0;">
        <h3 style="color:var(--text);font-size:1.05rem;"><i class="fa-solid fa-download text-blue-500"></i> إنشاء نسخة احتياطية من قاعدة البيانات</h3>
        <div style="display:flex;gap:10px;">
            <button class="btn-add" onclick="backupDB('db')" style="flex:1;"><i class="fa-solid fa-file-export"></i> تحميل كملف قاعدة بيانات (.db)</button>
            <button class="btn-add" onclick="backupDB('sql')" style="background:var(--accent);flex:1;"><i class="fa-solid fa-file-code"></i> تحميل كملف (.sql)</button>
        </div>
        <hr style="border:none;border-top:1px solid var(--border);margin:10px 0;">
        <h3 style="color:var(--text);font-size:1.05rem;"><i class="fa-solid fa-upload text-green-500"></i> استعادة نسخة احتياطية (.db / .sql / .json)</h3>
        <input type="file" id="restoreFile" accept=".db,.sql,.json" style="padding:10px;border:1px solid var(--border);border-radius:6px;background:var(--bg-elevated);color:var(--text);">
        <button class="btn-add" style="background:var(--secondary);" onclick="restoreDB()"><i class="fa-solid fa-rotate-left"></i> استعادة قاعدة البيانات الآن</button>
    </div>'''
        
    elif ptype == "settings":
        html += '''
    <div style="padding:20px;max-width:600px;">
        <div style="display:flex;justify-content:space-between;padding:15px;border-bottom:1px solid var(--border);">
            <span>السماح بتسجيل الدخول من أجهزة متعددة</span>
            <input type="checkbox" checked>
        </div>
        <div style="display:flex;justify-content:space-between;padding:15px;border-bottom:1px solid var(--border);">
            <span>تفعيل الإشعارات الصوتية</span>
            <input type="checkbox" checked>
        </div>
        <div style="display:flex;justify-content:space-between;padding:15px;border-bottom:1px solid var(--border);">
            <span>الوضع الليلي الافتراضي</span>
            <input type="checkbox">
        </div>
        <button class="btn-add" style="margin-top:20px;">حفظ الإعدادات</button>
    </div>'''
        
    elif ptype == "password":
        html += '''
    <div style="padding:20px;max-width:400px;display:flex;flex-direction:column;gap:15px;">
        <input type="password" placeholder="كلمة المرور الحالية" class="form-control" style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;">
        <input type="password" placeholder="كلمة المرور الجديدة" class="form-control" style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;">
        <input type="password" placeholder="تأكيد كلمة المرور الجديدة" class="form-control" style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;">
        <button class="btn-add">تغيير كلمة المرور</button>
    </div>'''

    elif ptype == "calendar":
        html += '''
    <div style="padding:20px;">
        <div style="background:white;padding:20px;border-radius:10px;text-align:center;border:1px solid var(--border);">
            <h3>Calendar View</h3>
            <p>Interactive calendar component goes here</p>
        </div>
    </div>'''
        
    elif ptype == "shortcuts":
        html += '''
    <div class="table-wrapper">
        <table>
            <thead><tr><th>الاختصار</th><th>الوصف</th></tr></thead>
            <tbody>
                <tr><td>Ctrl + S</td><td>حفظ البيانات</td></tr>
                <tr><td>Ctrl + P</td><td>طباعة الصفحة الحالية</td></tr>
                <tr><td>Alt + N</td><td>إضافة سجل جديد</td></tr>
            </tbody>
        </table>
    </div>'''
        
    elif ptype == "faq":
        html += '''
    <div style="padding:20px;max-width:800px;display:flex;flex-direction:column;gap:10px;">
        <details style="background:var(--bg);padding:15px;border-radius:8px;border:1px solid var(--border);">
            <summary style="font-weight:bold;cursor:pointer;">كيف يمكنني إضافة مستخدم جديد؟</summary>
            <p style="margin-top:10px;color:var(--text-light);">يمكنك إضافة مستخدم جديد من خلال الذهاب إلى قسم إدارة النظام ثم دليل المستخدمين والنقر على زر إضافة.</p>
        </details>
        <details style="background:var(--bg);padding:15px;border-radius:8px;border:1px solid var(--border);">
            <summary style="font-weight:bold;cursor:pointer;">كيف أقوم بعمل نسخة احتياطية؟</summary>
            <p style="margin-top:10px;color:var(--text-light);">اذهب إلى إدارة قواعد البيانات واضغط على زر إنشاء نسخة احتياطية.</p>
        </details>
    </div>'''

    elif ptype == "admin-messages":
        html += '''
    <div style="padding:20px;max-width:800px;display:flex;flex-direction:column;gap:15px;">
        <input type="text" placeholder="عنوان الرسالة" style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;">
        <textarea placeholder="محتوى الرسالة..." style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;min-height:150px;"></textarea>
        <div style="display:flex;gap:10px;">
            <select style="padding:10px;border:1px solid var(--border);border-radius:6px;flex:1;">
                <option value="">إلى جميع الموظفين</option>
                <option value="teachers">المعلمين فقط</option>
                <option value="admins">الإداريين فقط</option>
            </select>
            <button class="btn-add"><i class="fa-solid fa-paper-plane"></i> إرسال الإعلان</button>
        </div>
    </div>'''

    elif ptype == "sms":
        html += '''
    <div style="padding:20px;max-width:800px;display:flex;flex-direction:column;gap:15px;">
        <div style="display:flex;gap:10px;">
            <select style="padding:10px;border:1px solid var(--border);border-radius:6px;flex:1;">
                <option value="">اختيار المستلمين...</option>
                <option value="all_parents">جميع أولياء الأمور</option>
                <option value="all_teachers">جميع المعلمين</option>
            </select>
            <select style="padding:10px;border:1px solid var(--border);border-radius:6px;flex:1;">
                <option value="">استخدام قالب جاهز...</option>
                <option value="t1">إشعار غياب</option>
                <option value="t2">إشعار رسوم</option>
            </select>
        </div>
        <textarea placeholder="نص الرسالة القصيرة (SMS)..." style="padding:10px;border:1px solid var(--border);border-radius:6px;width:100%;min-height:100px;"></textarea>
        <div>عدد الحروف: 0 | عدد الرسائل: 1</div>
        <button class="btn-add"><i class="fa-solid fa-paper-plane"></i> إرسال SMS</button>
    </div>'''

    elif ptype == "sms-balance":
        html += '''
    <div style="padding:20px;">
        <div style="background:linear-gradient(135deg, #10b981, #059669);color:white;padding:30px;border-radius:15px;max-width:400px;box-shadow:0 10px 15px -3px rgba(16,185,129,0.3);">
            <h3 style="margin-bottom:15px;font-size:1.5rem;"><i class="fa-solid fa-coins"></i> رصيد الرسائل المتبقي</h3>
            <div style="font-size:3rem;font-weight:bold;margin-bottom:10px;">15,420</div>
            <p>رسالة نصية قصيرة (SMS)</p>
            <hr style="border-color:rgba(255,255,255,0.2);margin:20px 0;">
            <button style="background:white;color:#059669;border:none;padding:10px 20px;border-radius:8px;font-weight:bold;cursor:pointer;width:100%;">شحن الرصيد</button>
        </div>
    </div>'''

    html += '\n</div>\n'
    new_pages_html += html


# Insert new pages before the closing div of pageContainer
# Since it might be hard to find exactly `</div> <!-- end pageContainer -->` if it's not commented, 
# let's look for the toast div or the last script tag
toast_match = re.search(r'<div class="toast" id="toastMsg">', content)
if toast_match:
    insertion_point = toast_match.start()
    # Before the toast, but maybe there's a termModal? Let's check for termModal
    if "modal-overlay\" id=\"termModal\"" not in content:
        term_modal_html = '''
<div class="modal-overlay" id="termModal">
    <div class="modal-content glass-panel small-modal" style="max-width:520px;">
        <div class="modal-header">
            <h3><i class="fa-solid fa-calendar-check" style="color:#3b82f6;"></i> تحديد الفصل الدراسي</h3>
            <div class="window-controls"><button class="btn-close" onclick="closeModal('termModal')"><i class="fa-solid fa-xmark"></i></button></div>
        </div>
        <div class="modal-body" style="text-align:center;padding:25px;">
            <p style="font-size:1.05rem;color:var(--text);margin-bottom:25px;font-weight:600;">يرجى اختيار الفصل الدراسي:</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:15px;">
                <div onclick="selectTerm('الفصل الدراسي الأول')" style="background:linear-gradient(135deg, #1e3a8a, #3b82f6);color:white;padding:25px 15px;border-radius:14px;cursor:pointer;">
                    <i class="fa-solid fa-book-bookmark" style="font-size:2.2rem;margin-bottom:10px;display:block;"></i>
                    <strong style="font-size:1.1rem;">الفصل الدراسي الأول</strong>
                </div>
                <div onclick="selectTerm('الفصل الدراسي الثاني')" style="background:linear-gradient(135deg, #d97706, #f59e0b);color:white;padding:25px 15px;border-radius:14px;cursor:pointer;">
                    <i class="fa-solid fa-book-open" style="font-size:2.2rem;margin-bottom:10px;display:block;"></i>
                    <strong style="font-size:1.1rem;">الفصل الدراسي الثاني</strong>
                </div>
            </div>
        </div>
    </div>
</div>
'''
        new_pages_html += term_modal_html

    # But we need to be inside <div class="main-content"> ... <div class="page-container"> if the pages belong there.
    # Actually, in most structures, pages are siblings to each other. 
    # Let's find the end of the last <div class="page"...>
    last_page_match = list(re.finditer(r'<div class="page"[^>]*>.*?</div>\s*(?=<div class="page"|<div id="toast"|<div class="toast"|</div>\s*<script|</div>\s*</body>)', content, flags=re.DOTALL))
    if last_page_match:
        last_page = last_page_match[-1]
        insert_pos = last_page.end()
        content = content[:insert_pos] + "\n" + new_pages_html + content[insert_pos:]
    else:
        # Fallback to before Toast
        insert_pos = toast_match.start()
        content = content[:insert_pos] + new_pages_html + "\n" + content[insert_pos:]
else:
    # If no toast, append at the end of body
    content = content.replace("</body>", new_pages_html + "\n</body>")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete. Replaced sidebar nav and added new pages.")
