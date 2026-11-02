"""
Python script to append HR & Staff module logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with HR & Staff Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

hr_db_additions = """
// Data collections for HR & Staff modules
if (!DB.guarantorsData) DB.guarantorsData = [
    { id: 'SPN-2026-014', name: 'علي محمد أحمد المقطري', type: 'ضمانة تجارية', crNo: '1019928374', employer: 'محلات الأمل للمواد الغذائية (مالك)', contact: 'صنعاء - شارع حدة / 771234567', guaranteedPerson: 'أحمد علي محمد (طالب / موظف)', limit: 5000, validDates: '2026-09-01 - 2027-08-31', status: 'سارية وموثقة', verification: 'موثق من المحكمة الابتدائية', docPdf: 'Guaranty_Doc.pdf' }
];

if (!DB.teacherSubjectsData) DB.teacherSubjectsData = [
    { teacher: 'أ. إبراهيم علي (EMP-088)', subject: 'الكيمياء العامة', gradeSec: 'الصف الثالث الثانوي - شعبة (أ)', termYear: '2026/2027 - الترم الأول', role: 'مدرس رئيسي', hours: 4, workload: '18 / 24 حصة', qualMatch: 'مطابق', coTeacher: 'أ. خالد محمود (مدرس معمل)', status: 'مفعل (Active)' }
];

if (!DB.empAttendanceData) DB.empAttendanceData = [
    { empInfo: 'EMP-104 - د. حسام العنسي', dateDay: '2026-08-08 - السبت', shift: 'الدوام الصباحي (08:00 - 03:00)', inTime: '08:14 AM', outTime: '03:02 PM', lateMins: 'تأخير 14 دقيقة', status: 'متأخر', source: 'بصمة الوجه (Device-02)', justification: 'عذر مقبول (مهمة خارجية)', violation: 'تأخير يتجاوز 15 دقيقة', action: 'تنبيه كتابي', attachment: 'Permit_Doc.pdf' }
];

if (!DB.empNoticesData) DB.empNoticesData = [
    { id: 'NTF-2026-9902', title: 'تذكير: رفع درجات اختبارات المنتصف', body: 'يرجى إدخال درجات المنتصف لشعبة (أ) قبل يوم الخميس القادم', category: 'أكاديمي', priority: 'مهمة', sender: 'أ.د. مدير الشؤون الأكاديمية', recipients: 'جميع معلمي المواد العلمية (24 موظف)', channel: 'تطبيق الجوال (Push)', sentTime: '2026-08-08 10:30 AM', readStatus: 'تمت القراءة (10:35 AM)', actionLink: 'pg-grading', expiryDate: '2026-08-15' }
];

if (!DB.empContractsData) DB.empContractsData = [
    { id: 'CNT-2026-042', name: 'د. عبدالله صالح علي (EMP-112)', title: 'أستاذ حاسوب مشارك', dept: 'قسم الأمن السيبراني', type: 'محدد المدة (سنوي)', dates: '2026-09-01 - 2027-08-31', probation: '90 يوماً (تنتهي 2026-11-30)', basic: 1200, allowances: 250, hours: '40 ساعة / أسبوعياً', status: 'ساري (Active)', docPdf: 'Contract_Signed.pdf' }
];

if (!DB.empAdvancesData) DB.empAdvancesData = [
    { id: 'LON-2026-019', name: 'م. أحمد حسن العنسي (EMP-204)', type: 'سلفة طارئة على الراتب', requested: 1000, salaryContext: 'الراتب: 800 $ (الخصم 25%)', installments: '10 أشهر (100 $ / شهرياً)', startDate: 'مسير راتب سبتمبر 2026', guarantor: 'د. خالد عبدالله (EMP-108)', method: 'خصم آلي من الرواتب', paidVsBalance: 'المسدد: 400 $ | المتبقي: 600 $', reason: 'ظرف صحي طارئ', status: 'سارية (قيد الخصم)' }
];

if (!DB.leaveRequestsData) DB.leaveRequestsData = [
    { id: 'LV-2026-088', empDept: 'علي الكبسي - أمن المعلومات (EMP-114)', type: 'إجازة سنوية', dates: '2026-08-10 - 2026-08-17', totalDays: '5 أيام عمل', remainingBal: 'المتاح: 21 يوماً', substitute: 'م. حسام العنسي (EMP-204)', docPdf: 'Medical_Report.pdf', workflow: 'موافقة المدير (تم) -> HR (معلق)', impact: 'خصم من الرصيد السنوي', remarks: 'سفر شخصي' }
];

if (!DB.payrollMasterData) DB.payrollMasterData = [
    { batchId: 'PAY-2026-08', empInfo: 'د. حسام العنسي (EMP-204)', deptTitle: 'قسم الحاسوب - أستاذ مشارك', basic: 1200, allowances: 250, overtime: 100, attDeductions: -30, loanDeductions: -100, taxSocial: -95, totalDeductions: -225, netPayable: 1325, paymentRef: 'تحويل بنكي - الكريمي (YE882000...)', status: 'معتمد (Approved)' }
];
"""

hr_modules_js = """

// ==================== 1. GUARANTORS MODULE ====================
function renderGuarantorsList() {
    const tb = document.getElementById('tbl-guarantors-list');
    if (!tb) return;

    const query = (document.getElementById('searchGuarantors')?.value || '').toLowerCase();
    const typeFilter = document.getElementById('filterGuaranteeType')?.value || 'all';
    const statusFilter = document.getElementById('filterGuaranteeStatus')?.value || 'all';

    const list = (DB.guarantorsData || []).filter(g => {
        const matchQ = !query || (g.name || '').toLowerCase().includes(query) || (g.guaranteedPerson || '').toLowerCase().includes(query);
        const matchT = typeFilter === 'all' || g.type === typeFilter;
        const matchS = statusFilter === 'all' || g.status === statusFilter;
        return matchQ && matchT && matchS;
    });

    tb.innerHTML = list.map(g => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${g.id}</td>
            <td style="font-weight:700;">${g.name}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${g.type}</span></td>
            <td>${g.crNo}</td>
            <td>${g.employer}</td>
            <td style="font-size:0.8rem;">${g.contact}</td>
            <td style="font-weight:700;color:#38bdf8;">${g.guaranteedPerson}</td>
            <td style="font-weight:800;color:#34d399;">${(g.limit || 0).toLocaleString()} $</td>
            <td style="font-size:0.8rem;">${g.validDates}</td>
            <td>${g.verification}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${g.status}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة وثيقة الضمانة PDF')"><i class="fa-solid fa-file-pdf"></i></button></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('guarantors', ${JSON.stringify(g).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('') || '<tr><td colspan="13" style="text-align:center;color:var(--muted);">لا يوجد ضمناء أو كفلاء مسجلين</td></tr>';
}


// ==================== 2. TEACHER SUBJECTS MATRIX ====================
function renderTeacherSubjectsMatrix() {
    const tb = document.getElementById('tbl-teacher-subjects-matrix');
    if (!tb) return;

    const list = DB.teacherSubjectsData || [];
    tb.innerHTML = list.map(t => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${t.teacher}</td>
            <td style="font-weight:700;">${t.subject}</td>
            <td>${t.gradeSec}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(139,92,246,0.15);color:#c084fc;">${t.role}</span></td>
            <td>${t.hours} حصص</td>
            <td style="font-weight:800;color:#34d399;">${t.workload}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${t.qualMatch}</span></td>
            <td>${t.coTeacher}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${t.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="toast('تعديل إسناد المادة')"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 3. EMPLOYEE ATTENDANCE ====================
function renderEmpAttendanceGrid() {
    const tb = document.getElementById('tbl-emp-attendance-grid');
    if (!tb) return;

    const list = DB.empAttendanceData || [];
    tb.innerHTML = list.map(a => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${a.empInfo}</td>
            <td>${a.shift}</td>
            <td style="color:#10b981;font-weight:700;">${a.inTime}</td>
            <td style="color:#ef4444;font-weight:700;">${a.outTime}</td>
            <td style="color:#f59e0b;font-weight:700;">${a.lateMins}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(245,158,11,0.15);color:#fbbf24;">${a.status}</span></td>
            <td style="font-size:0.8rem;">${a.source}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${a.justification}</span></td>
            <td>${a.violation}</td>
            <td style="color:#f87171;font-weight:700;">${a.action}</td>
            <td><button class="btn-edit" onclick="toast('معاينة إذن المهمة')"><i class="fa-solid fa-paperclip"></i></button></td>
            <td><button class="btn-add" onclick="toast('قبول عذر / خصم')" style="padding:3px 6px;font-size:0.75rem;"><i class="fa-solid fa-shield"></i> معالجة</button></td>
        </tr>
    `).join('');
}

function saveEmpAttendance() {
    toast('✅ تم حفظ وتقييد سجل حضور وانضباط الموظفين بنجاح');
}


// ==================== 4. EMPLOYEE NOTICES ====================
function renderEmpNoticesGrid() {
    const tb = document.getElementById('tbl-emp-notices-grid');
    if (!tb) return;

    const list = DB.empNoticesData || [];
    tb.innerHTML = list.map(n => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${n.id}</td>
            <td style="font-weight:700;">${n.title}</td>
            <td style="font-size:0.83rem;">${n.body}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${n.category}</span></td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(245,158,11,0.15);color:#fbbf24;font-weight:700;">${n.priority}</span></td>
            <td>${n.sender}</td>
            <td style="font-size:0.8rem;">${n.recipients}</td>
            <td>${n.channel}</td>
            <td>${n.sentTime}</td>
            <td style="color:#10b981;font-weight:700;">${n.readStatus}</td>
            <td><button class="btn-edit" onclick="goTo('${n.actionLink}')"><i class="fa-solid fa-arrow-right-to-bracket"></i> توجيه</button></td>
            <td><button class="btn-delete" onclick="toast('إلغاء أو أرشفة الإشعار')"><i class="fa-solid fa-trash"></i></button></td>
        </tr>
    `).join('');
}


// ==================== 5. EMPLOYEE CONTRACTS ====================
function renderEmpContractsGrid() {
    const tb = document.getElementById('tbl-emp-contracts-grid');
    if (!tb) return;

    const list = DB.empContractsData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.id}</td>
            <td style="font-weight:700;">${c.name}</td>
            <td>${c.title}</td>
            <td>${c.dept}</td>
            <td>${c.type}</td>
            <td style="font-size:0.8rem;">${c.dates}</td>
            <td style="font-size:0.8rem;">${c.probation}</td>
            <td style="font-weight:800;color:#60a5fa;">${c.basic.toLocaleString()} $</td>
            <td style="color:#34d399;">+${c.allowances.toLocaleString()} $</td>
            <td>${c.hours}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${c.status}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة العقد الموقّع PDF')"><i class="fa-solid fa-file-pdf"></i></button></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('contract', ${JSON.stringify(c).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 6. EMPLOYEE ADVANCES & LOANS ====================
function renderEmpAdvancesGrid() {
    const tb = document.getElementById('tbl-emp-advances-grid');
    if (!tb) return;

    const list = DB.empAdvancesData || [];
    tb.innerHTML = list.map(l => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${l.id}</td>
            <td style="font-weight:700;">${l.name}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(239,68,68,0.15);color:#f87171;">${l.type}</span></td>
            <td style="font-weight:800;color:#60a5fa;">${l.requested.toLocaleString()} $</td>
            <td style="font-size:0.8rem;">${l.salaryContext}</td>
            <td style="font-weight:700;color:#34d399;">${l.installments}</td>
            <td>${l.startDate}</td>
            <td>${l.guarantor}</td>
            <td>${l.method}</td>
            <td style="font-size:0.8rem;font-weight:700;color:#fbbf24;">${l.paidVsBalance}</td>
            <td style="font-size:0.83rem;">${l.reason}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${l.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="toast('تعديل القسط أو السداد المبكر')"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 7. LEAVE MANAGEMENT SYSTEM ====================
function renderLeaveManagementGrid() {
    const tb = document.getElementById('tbl-leave-management-grid');
    if (!tb) return;

    const list = DB.leaveRequestsData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.id}</td>
            <td style="font-weight:700;">${r.empDept}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${r.type}</span></td>
            <td>${r.dates}</td>
            <td style="font-weight:700;color:#34d399;">${r.totalDays}</td>
            <td>${r.remainingBal}</td>
            <td>${r.substitute}</td>
            <td><button class="btn-edit" onclick="toast('معاينة التقرير الطبي')"><i class="fa-solid fa-file-pdf"></i></button></td>
            <td style="font-size:0.8rem;">${r.workflow}</td>
            <td>${r.impact}</td>
            <td><div class="act"><button class="btn-add" onclick="toast('قبول واعتماد الإجازة')" style="padding:3px 6px;font-size:0.75rem;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check"></i> اعتماد</button></div></td>
        </tr>
    `).join('');
}


// ==================== 8. PAYROLL MASTER PROCESSING ====================
function renderPayrollMasterGrid() {
    const tb = document.getElementById('tbl-payroll-master-grid');
    if (!tb) return;

    const list = DB.payrollMasterData || [];
    tb.innerHTML = list.map(p => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${p.empInfo}</td>
            <td>${p.deptTitle}</td>
            <td style="font-weight:700;">${p.basic.toLocaleString()} $</td>
            <td style="color:#34d399;">+${p.allowances.toLocaleString()} $</td>
            <td style="color:#60a5fa;">+${p.overtime.toLocaleString()} $</td>
            <td style="color:#ef4444;">${p.attDeductions} $</td>
            <td style="color:#ef4444;">${p.loanDeductions} $</td>
            <td style="color:#ef4444;">${p.taxSocial} $</td>
            <td style="color:#ef4444;font-weight:700;">${p.totalDeductions} $</td>
            <td style="font-weight:800;color:#10b981;font-size:1.05rem;">${p.netPayable.toLocaleString()} $</td>
            <td style="font-size:0.8rem;">${p.paymentRef}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${p.status}</span></td>
            <td><button class="btn-edit" onclick="toast('طباعة قسيمة الراتب (Payslip)')"><i class="fa-solid fa-print"></i> قسيمة</button></td>
        </tr>
    `).join('');
}

function runPayrollCalculation() {
    toast('⚡ جاري تشغيل محرك الاحتساب الآلي للرواتب والاستقطاعات...');
    setTimeout(() => { renderPayrollMasterGrid(); toast('✅ تم حساب واحتساب كشف الرواتب بنجاح!'); }, 800);
}
function exportBankWPSFile() {
    toast('تم تصدير ملف التحويل البنكي (WPS) بنجاح');
}

// Hook into window.goTo
const _origGoToHrStaff = window.goTo;
if (_origGoToHrStaff) {
    window.goTo = function(id) {
        _origGoToHrStaff(id);
        if (id === 'pg-guarantors') renderGuarantorsList();
        if (id === 'pg-teacher-subjects') renderTeacherSubjectsMatrix();
        if (id === 'pg-emp-attendance') renderEmpAttendanceGrid();
        if (id === 'pg-emp-notices') renderEmpNoticesGrid();
        if (id === 'pg-emp-contracts') renderEmpContractsGrid();
        if (id === 'pg-emp-advances') renderEmpAdvancesGrid();
        if (id === 'pg-leave-management') renderLeaveManagementGrid();
        if (id === 'pg-payroll') renderPayrollMasterGrid();
    };
}
"""

if 'GUARANTORS MODULE' not in js:
    js += hr_db_additions + "\n" + hr_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended HR & Staff logic in app.js successfully!")
