"""
Python script to append SMS & Comprehensive Reports logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with SMS & Comprehensive Reports Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

sms_reports_db_additions = """
// Data collections for SMS & Comprehensive Reports modules
if (!DB.smsSendGridData) DB.smsSendGridData = [
    { id: 'SMS-2026-0891', target: 'أولياء أمور الثالث الثانوي (علمي)', type: 'إشعار غياب يومي', template: 'قالب غياب طالب (TMPL-ABS-01)', content: 'ولي أمر الطالب {عبدالرحمن}، نود إحاطتكم بغياب ابنكم عن الحصة الأولى اليوم الموافق 2026-08-08', chars: '135 حرفاً (1 Segment)', recipients: 145, schedule: 'إرسال فوري (10:15 AM)', gateway: 'Yemen Mobile API', status: 'تم الإرسال (142 نجاح / 3 فشل)', costBalance: 'المستهلك: 145 (المتبقي: 8,500)' }
];

if (!DB.smsTemplatesGridData) DB.smsTemplatesGridData = [
    { code: 'TMPL-ABS-001', name: 'قالب إشعار غياب طالب عن الحصة', module: 'النقليات والحضور', channel: 'SMS / WhatsApp', trigger: 'تسجيل غياب بدون عذر مقبول', body: 'ولي أمر الطالب {اسم_الطالب}، نحيطكم بغيابه اليوم الموافق {التاريخ} عن مادة {المادة}.', placeholders: '{اسم_الطالب}, {التاريخ}, {المادة}', encoding: 'اللغة العربية (UTF-8)', estLen: '110 محارف (1 Segment)', status: 'معتمد ومفعل (Approved)' }
];

if (!DB.smsSettingsGridData) DB.smsSettingsGridData = [
    { provider: 'Yemen Mobile API', senderId: 'AL-AMAL SCH', apiKey: 'sk_live_992083810abf...', balance: '12,450 رسالة ($150.00)', alertLimit: '1,000 رسالة', cost: '0.015 $ / رسالة', window: 'من 07:00 ص إلى 09:00 م', dailyCap: '2,000 رسالة / يوم', status: 'نشط ومتصل (Online)', lastRecharge: '2026-08-01 (10,000 رسالة)' }
];

if (!DB.monthlyReportGridData) DB.monthlyReportGridData = [
    { id: 'REP-M-2026-08', period: 'أغسطس 2026', scope: 'الأكاديمي والمالي والمخازن', studentAtt: '94.5% (ارتفاع 1.2%)', staffAtt: '98.0% (14 حصة احتياط)', revenue: '45,000 $ (تحصيل 88%)', expenses: '12,300 $ (ضمن الميزانية)', inventory: '115 إذن صرف ($2,800)', transport: '1,200 رحلة حافلة (99%)', plan: 'تطبيق خطة صيانة الحافلات وتحديث الباركود' }
];

if (!DB.semesterReportGridData) DB.semesterReportGridData = [
    { id: 'REP-SEM-2026-01', term: 'الفصل الأول (2025/2026)', passRate: '92.4% (ارتفاع 2.1%)', avgGpa: '84.5 / 100', attDropout: 'حضور 96.2% | تسرب 0.3%', revenue: '185,000 $ (تحصيل 94%)', dues: '11,800 $ (متبقي قسط)', facultyScore: '95% من المناهج المكتملة', inventorySpent: '14,200 $ (قرطاسية ومعامل)', approval: 'معتمد من المدير التنفيذي' }
];

if (!DB.classDetailsGridData) DB.classDetailsGridData = [
    { id: '20261042', name: 'عبدالرحمن محمد علي السالمي', gradeSec: 'الثالث الثانوي - شعبة (أ)', status: 'مستمر (Active)', advisor: 'أ. خالد محمود العنسي', attRate: '96.5% (غياب يومين بعذر)', gpa: '89.5% (ممتاز)', tuition: 'مسدد بالكامل', contact: 'محمد علي السالمي (770000000)', transport: 'مشترك - خط حدة (حافلة 08)' }
];

if (!DB.topStudentsGridData) DB.topStudentsGridData = [
    { rank: 'المركز الأول على المدرسة', id: '20261042', name: 'عبدالرحمن محمد علي السالمي', gradeSec: 'الثالث الثانوي - شعبة (أ)', totalPct: '995 / 1000 (99.5%)', gpa: '3.98 / 4.00', conduct: '100% (ممتاز بدون مخالفات)', tieBreaker: 'المجموع الأعلى في المواد العلمية', certStatus: 'تم الإصدار (تفوق أكاديمي)', parentNotified: 'تم الإرسال (SMS & WhatsApp)' },
    { rank: 'المركز الثاني على المدرسة', id: '20261045', name: 'أسامة عبدالله أحمد السالمي', gradeSec: 'الثالث الثانوي - شعبة (أ)', totalPct: '988 / 1000 (98.8%)', gpa: '3.95 / 4.00', conduct: '100% (ممتاز)', tieBreaker: 'مجموع الكيمياء والفيزياء', certStatus: 'تم الإصدار', parentNotified: 'تم الإرسال' }
];

if (!DB.successRateSubjectGridData) DB.successRateSubjectGridData = [
    { code: 'SUB-MATH-102 (SEC-A)', subject: 'الرياضيات العامة (Advanced Math)', gradeSec: 'الثالث الثانوي - شعبة (أ)', teacher: 'أ. خالد محمود العنسي', total: 30, passedFailed: 'الناجحين: 27 | الراسبين: 3', passPct: '90.0% (نطاق ممتاز)', avgScore: '82.5 / 100', minMax: 'أعلى: 99 | أدنى: 42', statusAlert: 'مقبول (مستوى مرتفع)' }
];

if (!DB.customReportsGridData) DB.customReportsGridData = [
    { id: 'RPT-CUST-2026-012', title: 'تقرير تحصيل رسوم المواصلات حسب الأحياء والصفوف', source: 'اشتراكات المواصلات + التحصيل المالي', fields: 'اسم الطالب، الصف، الحي، الحافلة، المبلغ', filters: 'الحالة = نشط AND التاريخ >= 2026-01-01', grouping: 'تجميع حسب الحي | فرز المبلغ', aggOps: 'SUM(المبلغ) | COUNT(الطلاب)', vizType: 'جدول محوري (Pivot) + رسم بياني', schedule: 'إرسال أسبوعي (كل أحد - 08:00 AM)', access: 'خاص بمصمم التقرير + المالية' }
];

if (!DB.controlReportsGridData) DB.controlReportsGridData = [
    { id: 'CTRL-RPT-2026-08', term: 'العام الدراسي 2025/2026 - الفصل الثاني', gradeStage: 'الصف الثالث الثانوي - الفرع العلمي', reportType: 'المشيت الرسمي الموحد (Master Sheet)', registered: 120, entryProgress: '100% (مكتمل ومغلق للتعديل)', secretStatus: 'تم فك التشفير والمطابقة المعتمدة', summary: 'ناجح: 108 (90%) | مكمل: 10 (8.3%) | راسب: 2', signoff: 'معتمد رسمياً (توقيع الكنترول والمدير)', stamp: 'رمز QR موثق ومختوم للطباعة' }
];
"""

sms_reports_modules_js = """

// ==================== 1. SMS SEND ====================
function renderSmsSendGrid() {
    const tb = document.getElementById('tbl-sms-send-grid');
    if (!tb) return;

    const list = DB.smsSendGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.id}</td>
            <td style="font-weight:700;">${s.target}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${s.type}</span></td>
            <td>${s.template}</td>
            <td style="font-size:0.83rem;">${s.content}</td>
            <td style="font-size:0.8rem;color:#fbbf24;font-weight:700;">${s.chars}</td>
            <td style="font-weight:800;color:#34d399;">${s.recipients} مستلم</td>
            <td style="font-size:0.8rem;">${s.schedule}</td>
            <td>${s.gateway}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${s.status}</span></td>
            <td style="font-size:0.8rem;">${s.costBalance}</td>
            <td><button class="btn-edit" onclick="toast('معاينة تفاصيل دفعة الرسائل')"><i class="fa-solid fa-eye"></i></button></td>
        </tr>
    `).join('');
}


// ==================== 2. SMS TEMPLATES ====================
function renderSmsTemplatesGrid() {
    const tb = document.getElementById('tbl-sms-templates-grid');
    if (!tb) return;

    const list = DB.smsTemplatesGridData || [];
    tb.innerHTML = list.map(t => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${t.code}</td>
            <td style="font-weight:700;">${t.name}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(139,92,246,0.15);color:#c084fc;">${t.module}</span></td>
            <td>${t.channel}</td>
            <td style="font-size:0.83rem;">${t.trigger}</td>
            <td style="font-size:0.83rem;">${t.body}</td>
            <td style="color:#38bdf8;font-size:0.8rem;">${t.placeholders}</td>
            <td style="font-size:0.8rem;">${t.encoding}</td>
            <td style="font-size:0.8rem;">${t.estLen}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${t.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('sms-templates', ${JSON.stringify(t).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 3. SMS SETTINGS ====================
function renderSmsSettingsGrid() {
    const tb = document.getElementById('tbl-sms-settings-grid');
    if (!tb) return;

    const list = DB.smsSettingsGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.provider}</td>
            <td style="font-weight:800;color:#fbbf24;">${s.senderId}</td>
            <td style="font-size:0.8rem;color:#cbd5e1;">${s.apiKey}</td>
            <td style="font-weight:800;color:#34d399;">${s.balance}</td>
            <td style="color:#ef4444;font-size:0.8rem;">${s.alertLimit}</td>
            <td>${s.cost}</td>
            <td style="font-size:0.8rem;">${s.window}</td>
            <td>${s.dailyCap}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;"><i class="fa-solid fa-wifi"></i> ${s.status}</span></td>
            <td style="font-size:0.8rem;">${s.lastRecharge}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('sms-settings', ${JSON.stringify(s).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 4. MONTHLY REPORT ====================
function renderMonthlyReportGrid() {
    const tb = document.getElementById('tbl-monthly-report-grid');
    if (!tb) return;

    const list = DB.monthlyReportGridData || [];
    tb.innerHTML = list.map(m => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${m.id}</td>
            <td style="font-weight:700;">${m.period}</td>
            <td>${m.scope}</td>
            <td style="font-weight:700;color:#34d399;">${m.studentAtt}</td>
            <td>${m.staffAtt}</td>
            <td style="font-weight:800;color:#34d399;">${m.revenue}</td>
            <td style="color:#f87171;">${m.expenses}</td>
            <td style="font-size:0.83rem;">${m.inventory}</td>
            <td style="font-size:0.83rem;">${m.transport}</td>
            <td style="font-size:0.8rem;">${m.plan}</td>
            <td><button class="btn-edit" onclick="toast('معاينة التقرير التنفيذي الشهري PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}


// ==================== 5. SEMESTER REPORT ====================
function renderSemesterReportGrid() {
    const tb = document.getElementById('tbl-semester-report-grid');
    if (!tb) return;

    const list = DB.semesterReportGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.id}</td>
            <td style="font-weight:700;">${s.term}</td>
            <td style="font-weight:800;color:#34d399;">${s.passRate}</td>
            <td style="font-weight:800;color:#60a5fa;">${s.avgGpa}</td>
            <td style="font-size:0.83rem;">${s.attDropout}</td>
            <td style="font-weight:800;color:#34d399;">${s.revenue}</td>
            <td style="color:#f87171;">${s.dues}</td>
            <td>${s.facultyScore}</td>
            <td>${s.inventorySpent}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${s.approval}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة التقرير الفصلي الاستراتيجي PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}


// ==================== 6. CLASS DETAILS MANIFEST ====================
function renderClassDetailsGrid() {
    const tb = document.getElementById('tbl-class-details-grid');
    if (!tb) return;

    const list = DB.classDetailsGridData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.id}</td>
            <td style="font-weight:700;">${c.name}</td>
            <td>${c.gradeSec}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${c.status}</span></td>
            <td>${c.advisor}</td>
            <td style="font-weight:700;color:#34d399;">${c.attRate}</td>
            <td style="font-weight:800;color:#60a5fa;">${c.gpa}</td>
            <td style="color:#10b981;font-weight:700;">${c.tuition}</td>
            <td style="font-size:0.83rem;">${c.contact}</td>
            <td style="font-size:0.83rem;">${c.transport}</td>
            <td><button class="btn-edit" onclick="toast('استكشاف السجل الشامل للطالب')"><i class="fa-solid fa-id-card"></i> السجل</button></td>
        </tr>
    `).join('');
}


// ==================== 7. TOP STUDENTS & HONORS ====================
function renderTopStudentsGrid() {
    const tb = document.getElementById('tbl-top-students-grid');
    if (!tb) return;

    const list = DB.topStudentsGridData || [];
    tb.innerHTML = list.map(t => `
        <tr>
            <td style="font-weight:800;color:#fbbf24;font-size:1.05rem;"><i class="fa-solid fa-trophy"></i> ${t.rank}</td>
            <td style="font-weight:700;color:#60a5fa;">${t.id}</td>
            <td style="font-weight:700;">${t.name}</td>
            <td>${t.gradeSec}</td>
            <td style="font-weight:800;color:#34d399;">${t.totalPct}</td>
            <td style="font-weight:800;color:#60a5fa;">${t.gpa}</td>
            <td style="color:#10b981;font-weight:700;">${t.conduct}</td>
            <td style="font-size:0.8rem;">${t.tieBreaker}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${t.certStatus}</span></td>
            <td style="color:#10b981;font-weight:700;">${t.parentNotified}</td>
            <td><button class="btn-edit" onclick="toast('طباعة شهادة التقدير والتفوق PDF')"><i class="fa-solid fa-award"></i> شهادة</button></td>
        </tr>
    `).join('');
}

function generateBulkHonorCertificates() {
    toast('🏆 جاري توليد شهادات التقدير للطلاب المتفوقين وإرسال التهاني لأولياء الأمور...');
    setTimeout(() => { renderTopStudentsGrid(); toast('✅ تم إرسال رسائل التهنئة وتوليد شهادات التقدير بنجاح!'); }, 800);
}


// ==================== 8. SUCCESS RATE BY SUBJECT ====================
function renderSuccessRateSubjectGrid() {
    const tb = document.getElementById('tbl-success-rate-subject-grid');
    if (!tb) return;

    const list = DB.successRateSubjectGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.code}</td>
            <td style="font-weight:700;">${s.subject}</td>
            <td>${s.gradeSec}</td>
            <td>${s.teacher}</td>
            <td style="font-weight:700;">${s.total} طالب</td>
            <td style="font-size:0.83rem;">${s.passedFailed}</td>
            <td style="font-weight:800;color:#34d399;font-size:1.05rem;">${s.passPct}</td>
            <td style="font-weight:800;color:#60a5fa;">${s.avgScore}</td>
            <td style="font-size:0.8rem;">${s.minMax}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${s.statusAlert}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة الرسم البياني للدرجات')"><i class="fa-solid fa-chart-pie"></i> رسوم</button></td>
        </tr>
    `).join('');
}


// ==================== 9. CUSTOM DYNAMIC REPORTS ====================
function renderCustomReportsGrid() {
    const tb = document.getElementById('tbl-custom-reports-grid');
    if (!tb) return;

    const list = DB.customReportsGridData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.id}</td>
            <td style="font-weight:700;">${r.title}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(139,92,246,0.15);color:#c084fc;">${r.source}</span></td>
            <td style="font-size:0.83rem;">${r.fields}</td>
            <td style="font-size:0.8rem;color:#fbbf24;">${r.filters}</td>
            <td style="font-size:0.83rem;">${r.grouping}</td>
            <td style="font-size:0.83rem;">${r.aggOps}</td>
            <td>${r.vizType}</td>
            <td style="font-size:0.8rem;">${r.schedule}</td>
            <td style="font-size:0.8rem;">${r.access}</td>
            <td><button class="btn-add" onclick="toast('تشغيل التقرير المخصص وتوليد المخرجات')" style="padding:3px 8px;font-size:0.75rem;"><i class="fa-solid fa-play"></i> تشغيل</button></td>
        </tr>
    `).join('');
}


// ==================== 10. COMPREHENSIVE CONTROL REPORTS ====================
function renderControlReportsGrid() {
    const tb = document.getElementById('tbl-control-reports-grid');
    if (!tb) return;

    const list = DB.controlReportsGridData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.id}</td>
            <td style="font-weight:700;">${c.term}</td>
            <td>${c.gradeStage}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${c.reportType}</span></td>
            <td style="font-weight:700;">${c.registered} طالب</td>
            <td style="font-weight:800;color:#34d399;">${c.entryProgress}</td>
            <td style="font-size:0.8rem;">${c.secretStatus}</td>
            <td style="font-size:0.83rem;">${c.summary}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${c.signoff}</span></td>
            <td style="font-size:0.8rem;color:#38bdf8;"><i class="fa-solid fa-qrcode"></i> ${c.stamp}</td>
            <td><button class="btn-edit" onclick="toast('معاينة وطباعة المشيت الرسمي المعتمد PDF')"><i class="fa-solid fa-print"></i> المشيت</button></td>
        </tr>
    `).join('');
}
"""

if 'SMS & COMPREHENSIVE REPORTS MODULES' not in js:
    js += sms_reports_db_additions + "\n" + sms_reports_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended SMS & Comprehensive Reports logic in app.js successfully!")
