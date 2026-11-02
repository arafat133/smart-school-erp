"""
Verify openForm for users/user and inject permissions grid
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

user_permissions_html = """
    const allSystemPages = [
        { cat: 'إدارة النظام', pages: [
            { id: 'pg-school-info', name: 'معلومات المدرسة' },
            { id: 'pg-db-management', name: 'إدارة قواعد البيانات' },
            { id: 'pg-users', name: 'دليل المستخدمين' },
            { id: 'pg-operation-lock', name: 'قفل العمليات' },
            { id: 'pg-system-settings', name: 'إعدادات النظام' },
            { id: 'pg-audit', name: 'سجل العمليات والمحفوظات' },
            { id: 'pg-alerts', name: 'التنبيهات التلقائية' },
            { id: 'pg-archive', name: 'الأرشيف' }
        ]},
        { cat: 'الأستاذ العام والمحاسبة', pages: [
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
        { cat: 'تهيئة النظام المدرسي', pages: [
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
        { cat: 'شؤون الطلاب', pages: [
            { id: 'pg-student-register', name: 'تسجيل طالب جديد' },
            { id: 'pg-students', name: 'دليل الطلاب' },
            { id: 'pg-student-tree', name: 'شجرة الطلاب' },
            { id: 'pg-parents', name: 'دليل أولياء الأمور' },
            { id: 'pg-section-distribution', name: 'توزيع الطلاب على الشعب' },
            { id: 'pg-attendance', name: 'التحضير والحضور اليومي' },
            { id: 'pg-behavior', name: 'السلوك والمخالفات' },
            { id: 'pg-class-notes', name: 'ملاحظات رائد الفصل' }
        ]},
        { cat: 'شؤون الموظفين', pages: [
            { id: 'pg-employees', name: 'دليل الموظفين' },
            { id: 'pg-emp-contracts', name: 'عقود الموظفين' },
            { id: 'pg-emp-attendance', name: 'حضور وانضباط الموظفين' },
            { id: 'pg-emp-advances', name: 'سلفيات وقروض الموظفين' },
            { id: 'pg-payroll', name: 'مسير الرواتب' },
            { id: 'pg-teacher-subjects', name: 'إسناد المواد للمعلمين' }
        ]},
        { cat: 'الكنترول والامتحانات', pages: [
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
        { cat: 'الأنشطة والمواصلات', pages: [
            { id: 'pg-activities', name: 'إدارة الأنشطة والفعاليات' },
            { id: 'pg-transport-routes', name: 'خطوط السير والمسارات' },
            { id: 'pg-buses', name: 'أسطول الحافلات' },
            { id: 'pg-transport-enrollment', name: 'اشتراك المواصلات' },
            { id: 'pg-transport', name: 'كشوفات الحافلة اليومية' }
        ]},
        { cat: 'مخازن المدرسة والمشتريات', pages: [
            { id: 'pg-item-categories', name: 'فئات الأصناف' },
            { id: 'pg-inventory-items', name: 'دليل الأصناف المخزنية' },
            { id: 'pg-supply-orders', name: 'أوامر التوريد (GRN)' },
            { id: 'pg-issue-orders', name: 'أوامر الصرف (GIN)' },
            { id: 'pg-suppliers', name: 'دليل الموردين' },
            { id: 'pg-inventory-reports', name: 'تقارير المخزون والجرد' }
        ]},
        { cat: 'الرسائل القصيرة (SMS) والتقارير', pages: [
            { id: 'pg-sms-send', name: 'إرسال الرسائل النصية' },
            { id: 'pg-sms-templates', name: 'قوالب الرسائل' },
            { id: 'pg-monthly-report', name: 'التقرير الشهري PDF' },
            { id: 'pg-semester-report', name: 'تقرير الفصل الدراسي' },
            { id: 'pg-custom-reports', name: 'منشئ التقارير المخصصة' },
            { id: 'pg-admin-messages', name: 'التعاميم والرسائل الإدارية' }
        ]}
    ];

    let permCheckboxesHTML = '<div style="margin-top:14px;background:rgba(15,23,42,0.6);border:1px solid var(--border);border-radius:10px;padding:14px;"><h4 style="margin-top:0;color:#60a5fa;font-size:0.95rem;"><i class="fa-solid fa-user-shield"></i> تحديد صلاحيات الوصول لجميع واجهات النظام (13 قسم)</h4>';
    allSystemPages.forEach(group => {
        permCheckboxesHTML += `<div style="margin-bottom:12px;"><strong style="color:var(--secondary);font-size:0.82rem;display:block;margin-bottom:6px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:4px;">${group.cat}</strong><div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(180px, 1fr));gap:6px;">`;
        group.pages.forEach(p => {
            permCheckboxesHTML += `<label style="display:flex;align-items:center;gap:6px;font-size:0.78rem;color:var(--text);cursor:pointer;"><input type="checkbox" name="user_perm_pages" value="${p.id}" checked style="accent-color:#3b82f6;"> <span>${p.name}</span></label>`;
        });
        permCheckboxesHTML += `</div></div>`;
    });
    permCheckboxesHTML += '</div>';
"""

new_user_handler = """        } else if (type === 'users' || type === 'user') {
            title.innerHTML = '<i class="fa-solid fa-user-lock"></i> إضافة / تعديل مستخدم بالنظام';
            """ + user_permissions_html + """
            fields.innerHTML = `
                <div class="fg"><label>اسم المستخدم (Username) <span class="req">*</span></label><input id="fu_username" value="${d.username||''}" placeholder="مثال: teacher1" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>كلمة السر (Password) <span class="req">*</span></label><input type="password" id="fu_password" value="${d.password||''}" placeholder="أدخل كلمة السر"></div>
                <div class="fg"><label>اسم الموظف / المستفيد <span class="req">*</span></label><input id="fu_name" value="${d.name||''}" placeholder="أدخل اسم المستخدم الكامل" oninput="validateTextOnly(this)"></div>
                <div class="fg"><label>رتبة / دور المستخدم بالنظام <span class="req">*</span></label><select id="fu_role"><option value="school_admin" ${d.role==='school_admin'?'selected':''}>مدير المدرسة (School Admin)</option><option value="teacher" ${d.role==='teacher'?'selected':''}>معلم (Teacher)</option><option value="accountant" ${d.role==='accountant'?'selected':''}>محاسب مالي (Accountant)</option><option value="parent" ${d.role==='parent'?'selected':''}>ولي أمر (Parent)</option></select></div>
                <div class="fg"><label>حالة الحساب <span class="req">*</span></label><select id="fu_status"><option value="نشط" ${d.status!=='معطل'?'selected':''}>نشط (Active)</option><option value="معطل" ${d.status==='معطل'?'selected':''}>معطل (Disabled)</option></select></div>
                ${permCheckboxesHTML}
            `;"""

if "allSystemPages = [" not in js:
    # Find user handler in openForm and replace
    pattern = r'\}\s*else\s*if\s*\(\s*type\s*===\s*\'users\'\s*\|\|\s*type\s*===\s*\'user\'\s*\)\s*\{.*?(?=\}\s*else\s*if|\}\s*else)'
    js = re.sub(pattern, new_user_handler, js, flags=re.DOTALL)
    print("  ✓ Injected permissions grid into openForm('users')")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated openForm('users') permissions grid!")
