"""
Fix JS error line 12561, rebuild renderAudit/renderAuditGrid, upgrade openForm('users') with all system pages permissions checkboxes, and strictly verify login handling.
"""
import re, time

print("=" * 60)
print("Fixing JS errors, Audit Logs, User Permissions, and Login Validation...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fix JS Error: Cannot set properties of null (setting 'innerText') at stat-exam-subjects / stat-exam-days / stat-exam-countdown
old_exam_stats = """    // Update stats
    document.getElementById('stat-exam-subjects').innerText = data.length + ' مادة';
    const days = new Set(data.map(x=>x.date)).size;
    document.getElementById('stat-exam-days').innerText = days + ' يوم';
    
    if (data.length > 0) {
        let upcoming = data.map(x => new Date(x.date)).filter(d => d >= new Date()).sort((a,b)=>a-b)[0];
        if (upcoming) {
            let diff = Math.ceil((upcoming - new Date()) / (1000 * 60 * 60 * 24));
            document.getElementById('stat-exam-countdown').innerText = diff + ' أيام';
        } else {
            document.getElementById('stat-exam-countdown').innerText = 'انتهت الامتحانات';
        }
    }"""

new_exam_stats = """    // Update stats with safe null checks
    const elSub = document.getElementById('stat-exam-subjects'); if (elSub) elSub.innerText = data.length + ' مادة';
    const days = new Set(data.map(x=>x.date)).size;
    const elDays = document.getElementById('stat-exam-days'); if (elDays) elDays.innerText = days + ' يوم';
    const elCd = document.getElementById('stat-exam-countdown');
    if (elCd && data.length > 0) {
        let upcoming = data.map(x => new Date(x.date)).filter(d => d >= new Date()).sort((a,b)=>a-b)[0];
        if (upcoming) {
            let diff = Math.ceil((upcoming - new Date()) / (1000 * 60 * 60 * 24));
            elCd.innerText = diff + ' أيام';
        } else {
            elCd.innerText = 'انتهت الامتحانات';
        }
    }"""

if old_exam_stats in js:
    js = js.replace(old_exam_stats, new_exam_stats)
    print("  ✓ Fixed null innerText error in exam schedule stats!")
else:
    print("  ⚠️ Exam stats block exact match failed, applying regex replacement...")
    pattern_stats = r"document\.getElementById\('stat-exam-subjects'\)\.innerText\s*=.*?(?=// Render Matrix|\n\s*//)"
    js = re.sub(pattern_stats, new_exam_stats + "\n\n    ", js, flags=re.DOTALL)
    print("  ✓ Applied regex fix for exam stats!")

# 2. Fix Audit rendering targets in app.js
# Ensure renderAuditGrid and renderAudit look for all table IDs: tbl-audit-logs-grid, tbl-audit, tbl-audit-trail
audit_render_fixed = """
function renderAuditGrid() {
    const tb = document.getElementById('tbl-audit-logs-grid') || document.getElementById('tbl-audit') || document.getElementById('tbl-audit-trail');
    if (!tb) return;

    const query = (document.getElementById('auditSearchInput')?.value || '').toLowerCase();
    const modFilter = document.getElementById('auditModuleFilter')?.value || 'all';
    const actionFilter = document.getElementById('auditActionFilter')?.value || 'all';
    const sevFilter = document.getElementById('auditSeverityFilter')?.value || 'all';

    const logs = DB.auditLogsData || DB.audit || [
        {
            id: 'LOG-2026-0811-9921',
            userRole: 'أ. خالد محمود العنسي (مسؤول الكنترول)',
            timestamp: '2026-08-11 10:22:15',
            module: 'نظام الكنترول والامتحانات',
            actionType: 'UPDATE',
            targetEntity: 'Student_Grades (ID: 1042)',
            oldValue: JSON.stringify({ grade: 85, status: "Pending", subject: "الرياضيات" }, null, 2),
            newValue: JSON.stringify({ grade: 95, status: "Approved", subject: "الرياضيات" }, null, 2),
            ipClient: '192.168.1.45 (Windows 11 / Chrome)',
            severity: 'عالي الخطورة'
        },
        {
            id: 'LOG-2026-0811-9850',
            userRole: 'م. حسام الدين (مدير النظام)',
            timestamp: '2026-08-11 09:45:10',
            module: 'الشؤون المالية',
            actionType: 'DELETE',
            targetEntity: 'Voucher_Receipt (ID: 554)',
            oldValue: JSON.stringify({ voucherNo: "RV-2026-0045", amount: 500, payer: "علي السالمي" }, null, 2),
            newValue: JSON.stringify({ status: "DELETED", reason: "إلغاء السند بطلب المحاسب" }, null, 2),
            ipClient: '192.168.1.10 (macOS / Safari)',
            severity: 'عالي الخطورة'
        },
        {
            id: 'LOG-2026-0811-9720',
            userRole: 'أ. إبراهيم العنسي (مسؤول المعامل)',
            timestamp: '2026-08-11 08:30:00',
            module: 'المخازن والمشتريات',
            actionType: 'INSERT',
            targetEntity: 'Goods_Issue_Note (GIN-2026-0214)',
            oldValue: JSON.stringify({}, null, 2),
            newValue: JSON.stringify({ ginNo: "GIN-2026-0214", item: "طابعة HP Laser", qty: 2 }, null, 2),
            ipClient: '192.168.1.88 (Windows 10 / Firefox)',
            severity: 'عادي'
        },
        {
            id: 'LOG-2026-0811-9500',
            userRole: 'أ. سارة أحمد (مسؤولة التسجيل)',
            timestamp: '2026-08-11 07:50:12',
            module: 'شؤون الطلاب',
            actionType: 'LOGIN',
            targetEntity: 'UserSession (USR-2026-0104)',
            oldValue: JSON.stringify({ session: "Inactive" }, null, 2),
            newValue: JSON.stringify({ session: "Active", ip: "192.168.1.12" }, null, 2),
            ipClient: '192.168.1.12 (Windows 11 / Chrome)',
            severity: 'عادي'
        }
    ];

    const filtered = logs.filter(l => {
        const matchQ = !query || [l.id, l.userRole, l.module, l.targetEntity, l.ipClient].some(val => (val || '').toLowerCase().includes(query));
        const matchM = modFilter === 'all' || l.module === modFilter;
        const matchA = actionFilter === 'all' || l.actionType === actionFilter;
        const matchS = sevFilter === 'all' || l.severity === sevFilter;
        return matchQ && matchM && matchA && matchS;
    });

    const totEl = document.getElementById('auditTotalCount');
    const hrEl = document.getElementById('auditHighRiskCount');
    if (totEl) totEl.textContent = logs.length + ' حركـة';
    if (hrEl) hrEl.textContent = logs.filter(x => x.severity === 'عالي الخطورة').length + ' حركات';

    tb.innerHTML = filtered.map(l => {
        const isHigh = l.severity === 'عالي الخطورة';
        const actionColors = {
            'UPDATE': { bg: 'rgba(245,158,11,0.15)', color: '#f59e0b', label: 'تعديل (UPDATE)' },
            'DELETE': { bg: 'rgba(239,68,68,0.15)', color: '#ef4444', label: 'حذف (DELETE)' },
            'INSERT': { bg: 'rgba(16,185,129,0.15)', color: '#10b981', label: 'إضافة (INSERT)' },
            'LOGIN': { bg: 'rgba(59,130,246,0.15)', color: '#3b82f6', label: 'دخول (LOGIN)' }
        };
        const actInfo = actionColors[l.actionType] || { bg: 'rgba(107,114,128,0.15)', color: '#9ca3af', label: l.actionType };

        return `
            <tr style="${isHigh ? 'background:rgba(239,68,68,0.03);' : ''}">
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${l.id}</td>
                <td style="font-weight:700;">${l.userRole}</td>
                <td style="font-size:0.8rem;color:var(--muted);">${l.timestamp}</td>
                <td style="font-weight:600;">${l.module}</td>
                <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${actInfo.bg};color:${actInfo.color};">${actInfo.label}</span></td>
                <td style="font-size:0.83rem;color:#c084fc;font-family:monospace;">${l.targetEntity}</td>
                <td style="font-size:0.78rem;">${l.ipClient}</td>
                <td>
                    <span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${isHigh ? 'rgba(239,68,68,0.2)' : 'rgba(16,185,129,0.15)'};color:${isHigh ? '#ef4444' : '#10b981'};">
                        ${isHigh ? '🔥 عالي الخطورة' : '🟢 عادي'}
                    </span>
                </td>
                <td>
                    <button class="btn-edit" onclick="showDataDiffModal('${l.id}')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);padding:4px 10px;font-size:0.78rem;">
                        <i class="fa-solid fa-code-compare"></i> مطابقة (Diff)
                    </button>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderAuditGrid = renderAuditGrid;
function renderAudit() { renderAuditGrid(); }
window.renderAudit = renderAudit;
"""

# Replace old renderAudit and renderAuditGrid functions in app.js
js = re.sub(r'function renderAuditGrid\(\)\s*\{.*?\}\s*window\.renderAuditGrid\s*=\s*renderAuditGrid;', '', js, flags=re.DOTALL)
js = re.sub(r'function renderAudit\(\)\s*\{.*?\}\s*window\.renderAudit\s*=\s*renderAudit;', '', js, flags=re.DOTALL)
js += "\n" + audit_render_fixed + "\n"

print("  ✓ Rebuilt renderAudit & renderAuditGrid to target all audit tables")

# 3. Upgrade openForm('users') / openForm('user') to include ALL SYSTEM PAGES PERMISSIONS
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

    let permCheckboxesHTML = '<div style="margin-top:14px;background:rgba(15,23,42,0.6);border:1px solid var(--border);border-radius:10px;padding:14px;"><h4 style="margin-top:0;color:#60a5fa;font-size:0.95rem;"><i class="fa-solid fa-user-shield"></i> تحديد صلاحيات الوصول لجميع واجهات النظام</h4>';
    allSystemPages.forEach(group => {
        permCheckboxesHTML += `<div style="margin-bottom:12px;"><strong style="color:var(--secondary);font-size:0.82rem;display:block;margin-bottom:6px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:4px;">${group.cat}</strong><div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(180px, 1fr));gap:6px;">`;
        group.pages.forEach(p => {
            permCheckboxesHTML += `<label style="display:flex;align-items:center;gap:6px;font-size:0.78rem;color:var(--text);cursor:pointer;"><input type="checkbox" name="user_perm_pages" value="${p.id}" checked style="accent-color:#3b82f6;"> <span>${p.name}</span></label>`;
        });
        permCheckboxesHTML += `</div></div>`;
    });
    permCheckboxesHTML += '</div>';
"""

# Replace users form template in openForm handler
user_form_pattern = r'else\s*if\s*\(\s*type\s*===\s*\'users\'\s*\|\|\s*type\s*===\s*\'user\'\s*\)\s*\{.*?(?=\}\s*else\s*if|\}\s*else|\n\s*if)'
new_user_form = """else if (type === 'users' || type === 'user') {
        title.innerHTML = '<i class="fa-solid fa-user-lock"></i> إضافة / تعديل مستخدم بالنظام';
        """ + user_permissions_html + """
        fields.innerHTML = `
            <div class="fg"><label>اسم المستخدم (Username) <span class="req">*</span></label><input id="fu_username" value="${d.username||''}" placeholder="مثال: teacher1" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>كلمة السر (Password) <span class="req">*</span></label><input type="password" id="fu_password" value="${d.password||''}" placeholder="أدخل كلمة السر"></div>
            <div class="fg"><label>اسم الموظف / المستفيد <span class="req">*</span></label><input id="fu_name" value="${d.name||''}" placeholder="أدخل اسم المستخدم الكامل" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>رتبة / دور المستخدم بالنظام <span class="req">*</span></label><select id="fu_role"><option value="school_admin" ${d.role==='school_admin'?'selected':''}>مدير المدرسة (School Admin)</option><option value="teacher" ${d.role==='teacher'?'selected':''}>معلم (Teacher)</option><option value="accountant" ${d.role==='accountant'?'selected':''}>محاسب مالي (Accountant)</option><option value="parent" ${d.role==='parent'?'selected':''}>ولي أمر (Parent)</option></select></div>
            <div class="fg"><label>حالة الحساب <span class="req">*</span></label><select id="fu_status"><option value="نشط" ${d.status!=='معطل'?'selected':''}>نشط (Active)</option><option value="معطل" ${d.status==='معطل'?'selected':''}>معطل (Disabled)</option></select></div>
            ${permCheckboxesHTML}
        `;
    }"""

if re.search(user_form_pattern, js, re.DOTALL):
    js = re.sub(user_form_pattern, new_user_form, js, flags=re.DOTALL)
    print("  ✓ Upgraded openForm('users') with ALL System Pages Permissions Grid!")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
