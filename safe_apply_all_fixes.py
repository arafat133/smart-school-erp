"""
Safe apply all fixes to app.js
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fix null innerText in exam schedule stats
old_stats = """document.getElementById('stat-exam-subjects').innerText = data.length + ' مادة';"""
new_stats = """const elSub = document.getElementById('stat-exam-subjects'); if (elSub) elSub.innerText = data.length + ' مادة';"""
js = js.replace(old_stats, new_stats)

old_days = """document.getElementById('stat-exam-days').innerText = days + ' يوم';"""
new_days = """const elDays = document.getElementById('stat-exam-days'); if (elDays) elDays.innerText = days + ' يوم';"""
js = js.replace(old_days, new_days)

old_cd1 = """document.getElementById('stat-exam-countdown').innerText = diff + ' أيام';"""
new_cd1 = """const elCd = document.getElementById('stat-exam-countdown'); if (elCd) elCd.innerText = diff + ' أيام';"""
js = js.replace(old_cd1, new_cd1)

old_cd2 = """document.getElementById('stat-exam-countdown').innerText = 'انتهت الامتحانات';"""
new_cd2 = """const elCd = document.getElementById('stat-exam-countdown'); if (elCd) elCd.innerText = 'انتهت الامتحانات';"""
js = js.replace(old_cd2, new_cd2)

print("  ✓ Fixed null innerText in exam schedule stats safely")

# 2. Add System Pages Permissions Checkboxes into openForm('users') / openForm('user')
permissions_block = """
        const allSystemPages = [
            { cat: 'إدارة النظام (System Admin)', pages: [
                { id: 'pg-school-info', name: 'معلومات المدرسة' },
                { id: 'pg-db-management', name: 'إدارة قواعد البيانات' },
                { id: 'pg-users', name: 'دليل المستخدمين' },
                { id: 'pg-operation-lock', name: 'قفل العمليات' },
                { id: 'pg-system-settings', name: 'إعدادات النظام' },
                { id: 'pg-audit', name: 'سجل العمليات والمحفوظات' },
                { id: 'pg-alerts', name: 'التنبيهات التلقائية' },
                { id: 'pg-archive', name: 'الأرشيف' }
            ]},
            { cat: 'الأستاذ العام والمحاسبة (Accounts)', pages: [
                { id: 'pg-chart-accounts', name: 'دليل الحسابات' },
                { id: 'pg-currencies', name: 'دليل العملات' },
                { id: 'pg-cashboxes', name: 'دليل الصناديق' },
                { id: 'pg-cost-centers', name: 'مراكز التكلفة' },
                { id: 'pg-voucher-payment', name: 'سندات الصرف' },
                { id: 'pg-voucher-receipt', name: 'سندات القبض' },
                { id: 'pg-journal', name: 'القيود اليومية' },
                { id: 'pg-cashbox-inventory', name: 'جرد الصندوق' },
                { id: 'pg-acc-statement', name: 'كشف الحساب' },
                { id: 'pg-income-stmt', name: 'قائمة الدخل' },
                { id: 'pg-trial-balance', name: 'ميزان المراجعة' }
            ]},
            { cat: 'تهيئة النظام المدرسي (School Config)', pages: [
                { id: 'pg-academic-years', name: 'السنوات الدراسية' },
                { id: 'pg-departments', name: 'دليل الأقسام' },
                { id: 'pg-stages', name: 'المراحل والصفوف' },
                { id: 'pg-class-times', name: 'توقيت الحصص' },
                { id: 'pg-academic-calendar', name: 'التقويم المدرسي' },
                { id: 'pg-classrooms', name: 'القاعات والمعامل' },
                { id: 'pg-sections', name: 'دليل الشعب' },
                { id: 'pg-subjects', name: 'دليل المواد' },
                { id: 'pg-fee-categories', name: 'فئات الرسوم والخصومات' }
            ]},
            { cat: 'شؤون الطلاب (Student Affairs)', pages: [
                { id: 'pg-student-register', name: 'تسجيل طالب جديد' },
                { id: 'pg-students', name: 'دليل الطلاب' },
                { id: 'pg-student-tree', name: 'شجرة الطلاب' },
                { id: 'pg-parents', name: 'دليل أولياء الأمور' },
                { id: 'pg-section-distribution', name: 'توزيع الطلاب على الشعب' },
                { id: 'pg-attendance', name: 'التحضير والحضور اليومي' },
                { id: 'pg-behavior', name: 'السلوك والمخالفات' },
                { id: 'pg-class-notes', name: 'ملاحظات رائد الفصل' }
            ]},
            { cat: 'شؤون الموظفين (Employee Affairs)', pages: [
                { id: 'pg-employees', name: 'دليل الموظفين' },
                { id: 'pg-emp-contracts', name: 'عقود الموظفين' },
                { id: 'pg-emp-attendance', name: 'حضور وانضباط الموظفين' },
                { id: 'pg-emp-advances', name: 'سلفيات وقروض الموظفين' },
                { id: 'pg-payroll', name: 'مسير الرواتب' },
                { id: 'pg-teacher-subjects', name: 'إسناد المواد للمعلمين' }
            ]},
            { cat: 'الكنترول والامتحانات (Control & Exams)', pages: [
                { id: 'pg-grading', name: 'رصد الدرجات والشيت' },
                { id: 'pg-results', name: 'النتائج النهائية' },
                { id: 'pg-exam-schedule', name: 'جدول الامتحانات' },
                { id: 'pg-timetable-builder', name: 'بناء الجدول الدراسي' },
                { id: 'pg-seat-numbers', name: 'أرقام الجلوس والباركود' },
                { id: 'pg-secret-numbers', name: 'الأرقام السرية' },
                { id: 'pg-roll-call', name: 'كشوفات المناداة' },
                { id: 'pg-seat-cards', name: 'بطاقات أرقام الجلوس' },
                { id: 'pg-certificates', name: 'إصدار الشهادات' },
                { id: 'pg-promotion', name: 'ترفيع الطلاب' }
            ]},
            { cat: 'الأنشطة والمواصلات (Activities & Transport)', pages: [
                { id: 'pg-activities', name: 'إدارة الأنشطة والفعاليات' },
                { id: 'pg-transport-routes', name: 'خطوط السير والمسارات' },
                { id: 'pg-buses', name: 'أسطول الحافلات' },
                { id: 'pg-transport-enrollment', name: 'اشتراك المواصلات' },
                { id: 'pg-transport', name: 'كشوفات الحافلة اليومية' }
            ]},
            { cat: 'مخازن المدرسة والمشتريات (Warehouse)', pages: [
                { id: 'pg-item-categories', name: 'فئات الأصناف' },
                { id: 'pg-inventory-items', name: 'دليل الأصناف المخزنية' },
                { id: 'pg-supply-orders', name: 'أوامر التوريد (GRN)' },
                { id: 'pg-issue-orders', name: 'أوامر الصرف (GIN)' },
                { id: 'pg-suppliers', name: 'دليل الموردين' },
                { id: 'pg-inventory-reports', name: 'تقارير المخزون والجرد' }
            ]},
            { cat: 'الرسائل والتقارير الأسلحة الإدارية (SMS & Reports)', pages: [
                { id: 'pg-sms-send', name: 'إرسال الرسائل النصية' },
                { id: 'pg-sms-templates', name: 'قوالب الرسائل' },
                { id: 'pg-monthly-report', name: 'التقرير الشهري PDF' },
                { id: 'pg-semester-report', name: 'تقرير الفصل الدراسي' },
                { id: 'pg-custom-reports', name: 'منشئ التقارير المخصصة' },
                { id: 'pg-admin-messages', name: 'التعاميم والرسائل الإدارية' }
            ]}
        ];

        let permCheckboxesHTML = '<div style="margin-top:14px;background:rgba(15,23,42,0.6);border:1px solid var(--border);border-radius:10px;padding:14px;"><h4 style="margin-top:0;color:#60a5fa;font-size:0.95rem;"><i class="fa-solid fa-user-shield"></i> تحديد صلاحيات الوصول لكافة واجهات النظام الإدارية والأكاديمية</h4>';
        allSystemPages.forEach(group => {
            permCheckboxesHTML += `<div style="margin-bottom:12px;"><strong style="color:var(--secondary);font-size:0.82rem;display:block;margin-bottom:6px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:4px;">${group.cat}</strong><div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(180px, 1fr));gap:6px;">`;
            group.pages.forEach(p => {
                permCheckboxesHTML += `<label style="display:flex;align-items:center;gap:6px;font-size:0.78rem;color:var(--text);cursor:pointer;"><input type="checkbox" name="user_perm_pages" value="${p.id}" checked style="accent-color:#3b82f6;"> <span>${p.name}</span></label>`;
            });
            permCheckboxesHTML += `</div></div>`;
        });
        permCheckboxesHTML += '</div>';
"""

# Replace users handler inside openForm
old_users_handler = "fields.innerHTML = `<div class=\"fg\"><label>اسم المستخدم</label>"
if old_users_handler in js:
    js = js.replace(old_users_handler, permissions_block + "\n        " + old_users_handler.replace('`<div', '`${permCheckboxesHTML}<div'))
    print("  ✓ Added permissions grid to openForm('users')")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
