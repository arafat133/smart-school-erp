"""
Consolidate goTo page render handlers and fix renderPerformanceEvals and renderLeaveManagementGrid
"""
import re, time

print("=" * 60)
print("Fixing Leave Management and Performance Evaluation renders...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fixed renderPerformanceEvals implementation
new_perf_eval_code = """
function renderPerformanceEvals() {
    const tb = document.getElementById('tbl-performance-list') || document.getElementById('tbl-performance');
    if (!tb) return;

    if (!DB.performanceEvalsData) {
        DB.performanceEvalsData = [
            { id: 1, appraisee: 'م. أحمد خالد', job: 'مهندس أمن سيبراني', evaluator: 'د. محمد سعيد', cycle: 'تقييم النصف الأول 2026', score: '92.5%', rating: 'يتجاوز التوقعات', status: 'مكتمل (معتمد)' },
            { id: 2, appraisee: 'أ. إبراهيم علي', job: 'معلم كيمياء', evaluator: 'أ.د. المدير الأكاديمي', cycle: 'تقييم النصف الأول 2026', score: '88.0%', rating: 'ممتاز', status: 'قيد مراجعة HR' },
            { id: 3, appraisee: 'علي الكبسي', job: 'أخصائي شبكات', evaluator: 'د. محمد سعيد', cycle: 'التقييم السنوي 2025', score: '84.0%', rating: 'جيد جداً', status: 'مكتمل (معتمد)' }
        ];
    }

    const cycleFilter = document.getElementById('evalCycleSelect')?.value || 'all';
    const list = DB.performanceEvalsData;

    tb.innerHTML = list.map(e => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${e.appraisee}</td>
            <td>${e.job}</td>
            <td>${e.evaluator}</td>
            <td>${e.cycle}</td>
            <td style="font-weight:800;color:#34d399;font-size:1.05rem;">${e.score}</td>
            <td><span style="padding:4px 10px;border-radius:6px;font-size:0.78rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${e.rating}</span></td>
            <td><span style="padding:2px 8px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${e.status}</span></td>
            <td><button class="btn-edit" onclick="openPerformanceEvalDetailModal('${e.appraisee}')"><i class="fa-solid fa-eye"></i> عرض التفاصيل</button></td>
        </tr>
    `).join('');
}

function openPerformanceEvalDetailModal(name) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;

    title.innerHTML = '<i class="fa-solid fa-star"></i> استمارة التقييم الموزونة والمقارنة (360-Degree Evaluation)';
    fields.innerHTML = `
        <div style="background:rgba(255,255,255,0.03);padding:12px;border-radius:8px;margin-bottom:12px;font-size:0.88rem;">
            <strong>المُقيّم المعني:</strong> ${name} | <strong>دورة التقييم:</strong> تقييم النصف الأول 2026
        </div>
        <div class="table-wrapper" style="margin-bottom:12px;">
            <table>
                <thead>
                    <tr>
                        <th>المعيار / الجدارة (KPI)</th>
                        <th>الوزن %</th>
                        <th>التقييم الذاتي</th>
                        <th>تقييم المشرف</th>
                        <th>الدرجة الموزونة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>إنجاز المشاريع في الموعد (KPI)</td><td>30%</td><td>4.5 / 5</td><td>4.8 / 5</td><td style="color:#34d399;font-weight:700;">28.8%</td></tr>
                    <tr><td>إدارة التكتيك والأمن (Technical)</td><td>40%</td><td>4.0 / 5</td><td>4.5 / 5</td><td style="color:#34d399;font-weight:700;">36.0%</td></tr>
                    <tr><td>العمل الجماعي والانضباط (Behavior)</td><td>30%</td><td>4.5 / 5</td><td>4.6 / 5</td><td style="color:#34d399;font-weight:700;">27.6%</td></tr>
                </tbody>
            </table>
        </div>
        <div style="padding:10px;background:rgba(16,185,129,0.15);border:1px solid #10b981;color:#10b981;border-radius:8px;font-weight:700;margin-bottom:12px;">
            المجموع الموزون النهائي: 92.4% (يتجاوز التوقعات - التوصية: ترقية + دورة CISSP)
        </div>
        <button class="btn-cancel" onclick="document.getElementById('formModal').classList.remove('active');" style="width:100%;"><i class="fa-solid fa-xmark"></i> إغلاق النافذة</button>
    `;
    document.getElementById('formModal').classList.add('active');
}
"""

# 2. Fixed renderLeaveManagementGrid implementation
new_leave_code = """
function renderLeaveManagementGrid() {
    const tb = document.getElementById('tbl-leave-management-grid') || document.getElementById('tbl-leave-requests') || document.getElementById('tbl-leave');
    if (!tb) return;

    if (!DB.leaveRequestsData) {
        DB.leaveRequestsData = [
            { id: 'LV-2026-088', empDept: 'علي الكبسي - أمن المعلومات (EMP-114)', type: 'إجازة سنوية', dates: '2026-08-10 - 2026-08-17', totalDays: '5 أيام عمل', remainingBal: 'المتاح: 21 يوماً', substitute: 'م. حسام العنسي (EMP-204)', docPdf: 'Medical_Report.pdf', workflow: 'موافقة المدير (تم) -> HR (معلق)', impact: 'خصم من الرصيد السنوي', remarks: 'سفر شخصي' },
            { id: 'LV-2026-092', empDept: 'د. حسام العنسي - قسم الحاسوب (EMP-204)', type: 'إجازة مرضية', dates: '2026-08-01 - 2026-08-03', totalDays: '3 أيام عمل', remainingBal: 'المتاح: 12 يوماً', substitute: 'أ. إبراهيم علي (EMP-088)', docPdf: 'Sick_Leave.pdf', workflow: 'موافقة HR (تم)', impact: 'إجازة مرضية مدفوعة الأجر', remarks: 'ظرف صحي' }
        ];
    }

    const typeFilter = document.getElementById('lmTypeFilter')?.value || 'all';
    const list = DB.leaveRequestsData.filter(r => typeFilter === 'all' || r.type === typeFilter);

    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.id}</td>
            <td style="font-weight:700;">${r.empDept}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${r.type}</span></td>
            <td>${r.dates}</td>
            <td style="font-weight:700;color:#34d399;">${r.totalDays}</td>
            <td>${r.remainingBal}</td>
            <td>${r.substitute}</td>
            <td><button class="btn-edit" onclick="toast('معاينة التقرير الطبي PDF')"><i class="fa-solid fa-file-pdf"></i></button></td>
            <td style="font-size:0.8rem;">${r.workflow}</td>
            <td>${r.impact}</td>
            <td><div class="act"><button class="btn-add" onclick="toast('تم قبول واعتماد طلب الإجازة بنجاح')" style="padding:3px 6px;font-size:0.75rem;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check"></i> اعتماد</button></div></td>
        </tr>
    `).join('');
}
function renderLeaveRequests() { renderLeaveManagementGrid(); }
"""

# Replace renderPerformanceEvals in app.js
pattern_perf = r'function\s+renderPerformanceEvals\(\)\s*\{.*?\n\}'
if re.search(pattern_perf, js, re.DOTALL):
    js = re.sub(pattern_perf, new_perf_eval_code.strip(), js, flags=re.DOTALL)
    print("  ✓ Replaced renderPerformanceEvals in app.js")

# Replace renderLeaveManagementGrid in app.js
pattern_leave = r'function\s+renderLeaveManagementGrid\(\)\s*\{.*?\n\}'
if re.search(pattern_leave, js, re.DOTALL):
    js = re.sub(pattern_leave, new_leave_code.strip(), js, flags=re.DOTALL)
    print("  ✓ Replaced renderLeaveManagementGrid in app.js")

# Centralized Master Master goTo Dispatcher
master_goto_code = """
// Master Central Dispatcher for Page Renders
const _origMasterGoTo = window.goTo;
window.goTo = function(id) {
    if (_origMasterGoTo) {
        try { _origMasterGoTo(id); } catch(e){}
    }
    
    // Explicit guaranteed dispatcher for all pages
    if (id === 'pg-leave-management') renderLeaveManagementGrid();
    if (id === 'pg-performance-eval') renderPerformanceEvals();
    if (id === 'pg-guarantors') renderGuarantorsList();
    if (id === 'pg-teacher-subjects') renderTeacherSubjectsMatrix();
    if (id === 'pg-emp-attendance') renderEmpAttendanceGrid();
    if (id === 'pg-emp-notices') renderEmpNoticesGrid();
    if (id === 'pg-emp-contracts') renderEmpContractsGrid();
    if (id === 'pg-emp-advances') renderEmpAdvancesGrid();
    if (id === 'pg-payroll') renderPayrollMasterGrid();
    if (id === 'pg-academic-calendar') renderAcademicCalendar();
    if (id === 'pg-classrooms') renderClassroomsGrid();
    if (id === 'pg-timetable-builder') renderInteractiveTimetable();
    if (id === 'pg-homework-tracker') renderHomeworkList();
    if (id === 'pg-promotion-workflow') renderPromotionBatch();
    if (id === 'pg-student-docs') renderStudentDocs();
    if (id === 'pg-section-distribution') renderSectionDistributionWorkspace();
    if (id === 'pg-discontinued') renderDiscontinuedList();
    if (id === 'pg-class-notes') renderClassNotesTimeline();
    if (id === 'pg-enrollment') renderEnrollmentList();
    if (id === 'pg-operation-lock') renderOperationLock();
    if (id === 'pg-chart-accounts') renderChartAccountsTree();
    if (id === 'pg-journal') renderJournalList();
    if (id === 'pg-cashboxes') renderCashboxes();
    if (id === 'pg-cost-centers') renderCostCenters();
    if (id === 'pg-account-ceiling') renderAccountCeiling();
    if (id === 'pg-vouchers') renderVouchers();
    if (id === 'pg-student-account') renderStatementOfAccount();
};
"""

if 'Master Central Dispatcher for Page Renders' not in js:
    js += "\n" + master_goto_code.strip() + "\n"

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync HTML cache timestamp
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

print(f"Fixed renderLeaveManagementGrid and renderPerformanceEvals! Timestamp v={ts}")
