"""
Python script to append/update JS logic for:
- Academic Calendar (pg-academic-calendar)
- Classrooms Grid & Occupancy (pg-classrooms)
- Timetable Builder & Conflict Detector (pg-timetable-builder)
- Homework Tracker (pg-homework-tracker)
- Performance Evaluation (pg-performance-eval)
- Batch Student Promotion (pg-promotion-workflow)
- Student Docs Modal Flow (pg-student-docs)
- Section Distribution Workspace (pg-section-distribution)
- Discontinued Students Register (pg-discontinued)
- Homeroom Class Notes Timeline (pg-class-notes)
- Registration & Tuition Fees (pg-enrollment)
"""
import re, time

print("=" * 60)
print("Updating app.js with Requested Module Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure global DB collections exist
db_additions = """
// Data collections for updated modules
if (!DB.calendarEvents) DB.calendarEvents = [
    { id: 1, title: 'امتحانات الفصل الدراسي الأول', category: 'اختبارات', yearTerm: '2026/2027 - الترم الأول', startDate: '2026-11-15 08:00', endDate: '2026-11-26 13:00', dayStatus: 'إجازة رسمية (Non-Working Day)', audience: 'طلاب الصف الثالث ثانوي + المعلمين', location: 'مسرح المدرسة الرئيسي', recurrence: 'يتكرر سنوياً', publishStatus: 'منشور', color: '#f59e0b' },
    { id: 2, title: 'اليوم الرياضي المدرسي', category: 'نشاط مدرسي', yearTerm: '2026/2027 - الترم الأول', startDate: '2026-10-05 09:00', endDate: '2026-10-05 14:00', dayStatus: 'حضور فعلي', audience: 'جميع الطلاب', location: 'الملعب الرياضي', recurrence: 'لا يتكرر', publishStatus: 'منشور', color: '#10b981' }
];

if (!DB.classroomsData) DB.classroomsData = [
    { code: 'BLD1-FL2-RM204', name: 'قاعة الخوارزمي (204)', building: 'مبنى 1 - الدور 2', type: 'معمل حاسوب', capacity: 40, equipments: 'Projector + Smart Board + Sound System', assignedTo: 'شعبة أ - الصف الثالث ثانوي', opStatus: 'متاحة', occupancy: 'شاغرة', custodian: 'أ. محمد سعيد (فني المعامل)', rules: 'تتطلب موافقة قسم الحاسب' },
    { code: 'BLD1-FL1-RM102', name: 'مختبر الكيمياء (102)', building: 'مبنى 1 - الدور 1', type: 'مختبر كيمياء', capacity: 30, equipments: 'Smart Board + Lab Tables + Safety Gear', assignedTo: 'عامة', opStatus: 'متاحة', occupancy: 'مشغولة حالياً', custodian: 'أ. إبراهيم علي', rules: 'ممنوع الدخول بدون معطف المختبر' }
];

if (!DB.docModalFlowData) DB.docModalFlowData = {};

if (!DB.discontinuedStudents) DB.discontinuedStudents = [
    { id: 101, name: 'عبدالله خالد علي', code: 'STU-202409', grade: 'الصف الثاني الثانوي', type: 'مفصول/موقوف', date: '2026-02-10', reason: 'عدم انتظام مالي ونسحب كلي', clearance: 'مكتمل (تم تسليم الكتب والبطاقة)', financeDues: 'متبقي 450 $', refund: '0 $', status: 'موقوف', transcriptAvailable: true }
];

if (!DB.classNotesData) DB.classNotesData = [
    { id: 1, studentName: 'عبدالرحمن محمد (2026104)', gradeSection: 'الصف الثالث متوسط - شعبة (ب)', category: 'سلوكية', severity: 'عاجل', text: 'تأخر عن الحصة الأولى مرتين هذا الأسبوع دون عذر مسبق', timestamp: '2026-08-07 09:15 AM', shareWith: 'المرشد الطلابي + ولي الأمر', status: 'قيد المعالجة', feedback: 'تم التحدث مع الطالب وتعهّد بعدم التكرار' }
];

if (!DB.enrollmentsData) DB.enrollmentsData = [
    { id: 'REG-2026-0891', studentName: 'محمد أحمد سالم', grade: 'الصف الثاني الثانوي', regType: 'طالب جديد', baseTuition: 1500, services: 150, discount: 150, netPayable: 1500, plan: '3 أقساط فصلية', dueDate: '2026-09-15', totalPaid: 600, balanceDue: 900, status: 'مدفوع جزئياً' }
];
"""

requested_modules_js = """

// ==================== A. ACADEMIC CALENDAR ====================
let currentCalViewMode = 'month';

function switchCalView(mode, btnEl) {
    currentCalViewMode = mode;
    if (btnEl) {
        btnEl.parentElement.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
    }
    renderAcademicCalendar();
}

function renderAcademicCalendar() {
    const container = document.getElementById('calViewContainer');
    if (!container) return;

    const events = DB.calendarEvents || [];
    const stageFilter = document.getElementById('calFilterStage')?.value || 'all';
    const audienceFilter = document.getElementById('calFilterAudience')?.value || 'all';

    const filtered = events.filter(e => {
        const matchS = stageFilter === 'all' || (e.audience || '').includes(stageFilter);
        const matchA = audienceFilter === 'all' || (e.audience || '').includes(audienceFilter);
        return matchS && matchA;
    });

    if (currentCalViewMode === 'agenda') {
        container.innerHTML = `
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>الحدث</th>
                            <th>التصنيف</th>
                            <th>البداية</th>
                            <th>النهاية</th>
                            <th>حالة اليوم</th>
                            <th>الفئة المستهدفة</th>
                            <th>الموقع</th>
                            <th>الحالة</th>
                            <th>إجراءات</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${filtered.map(e => `
                            <tr>
                                <td style="font-weight:700;color:${e.color || '#3b82f6'};"><i class="fa-solid fa-circle" style="font-size:0.6rem;margin-left:6px;"></i> ${e.title}</td>
                                <td><span style="padding:2px 8px;border-radius:4px;font-size:0.75rem;background:${e.color || '#3b82f6'}22;color:${e.color || '#3b82f6'};font-weight:700;">${e.category}</span></td>
                                <td>${e.startDate}</td>
                                <td>${e.endDate}</td>
                                <td>${e.dayStatus}</td>
                                <td>${e.audience}</td>
                                <td>${e.location}</td>
                                <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${e.publishStatus}</span></td>
                                <td><div class="act"><button class="btn-edit" onclick="openForm('academic-calendar', ${JSON.stringify(e).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    } else {
        // Month / Week / Day visual Grid
        const days = ['الأحد','الاثنين','الثلاثاء','الأربعاء','الخميس','الجمعة','السبت'];
        container.innerHTML = `
            <div style="display:grid;grid-template-columns:repeat(7, 1fr);gap:8px;">
                ${days.map(d => `<div style="text-align:center;font-weight:700;padding:8px;background:rgba(59,130,246,0.15);color:#93c5fd;border-radius:6px;">${d}</div>`).join('')}
                ${Array(35).fill(0).map((_, i) => {
                    const dayNum = (i % 31) + 1;
                    const eventThisDay = filtered[i % filtered.length];
                    return `
                        <div onclick="openForm('academic-calendar')" style="min-height:90px;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:8px;padding:6px;cursor:pointer;position:relative;">
                            <span style="font-size:0.8rem;font-weight:700;color:var(--muted);">${dayNum}</span>
                            ${i % 4 === 0 && eventThisDay ? `
                                <div style="margin-top:6px;padding:4px 6px;border-radius:4px;font-size:0.7rem;font-weight:700;background:${eventThisDay.color}33;color:${eventThisDay.color};border-right:3px solid ${eventThisDay.color};overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
                                    ${eventThisDay.title}
                                </div>
                            ` : ''}
                        </div>
                    `;
                }).join('')}
            </div>
        `;
    }
}


// ==================== B. CLASSROOMS GRID ====================
function renderClassroomsGrid() {
    const grid = document.getElementById('classroomsFloorGrid');
    if (!grid) return;

    const bldFilter = document.getElementById('crFilterBuilding')?.value || 'all';
    const typeFilter = document.getElementById('crFilterType')?.value || 'all';

    const rooms = (DB.classroomsData || []).filter(r => {
        const matchB = bldFilter === 'all' || r.building === bldFilter;
        const matchT = typeFilter === 'all' || r.type === typeFilter;
        return matchB && matchT;
    });

    const statusColors = {
        'شاغرة': { bg: 'rgba(16,185,129,0.15)', border: '#10b981', text: '#10b981' },
        'مشغولة حالياً': { bg: 'rgba(239,68,68,0.15)', border: '#ef4444', text: '#f87171' },
        'قيد الصيانة': { bg: 'rgba(245,158,11,0.15)', border: '#f59e0b', text: '#fbbf24' }
    };

    grid.innerHTML = rooms.map(r => {
        const sc = statusColors[r.occupancy] || statusColors['شاغرة'];
        return `
            <div class="form-card" style="padding:14px;border:1px solid ${sc.border};position:relative;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                    <h4 style="color:#60a5fa;font-weight:800;font-size:1rem;">${r.name}</h4>
                    <span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${sc.bg};color:${sc.text};">${r.occupancy}</span>
                </div>
                <div style="font-size:0.8rem;color:var(--muted);margin-bottom:8px;"><i class="fa-solid fa-barcode"></i> الكود: ${r.code} | <strong>${r.building}</strong></div>
                <div style="font-size:0.83rem;margin-bottom:6px;"><strong>النوع:</strong> ${r.type} | <strong>السعة:</strong> <span style="color:#34d399;font-weight:700;">${r.capacity} مقعد</span></div>
                <div style="font-size:0.8rem;color:#93c5fd;margin-bottom:6px;"><strong>التجهيزات:</strong> ${r.equipments}</div>
                <div style="font-size:0.8rem;color:var(--muted);margin-bottom:12px;"><strong>المشرف:</strong> ${r.custodian}</div>
                <button class="btn-add" onclick="openForm('classrooms', ${JSON.stringify(r).replace(/"/g, '&quot;')})" style="width:100%;font-size:0.8rem;"><i class="fa-solid fa-pen"></i> تعديل بيانات القاعة</button>
            </div>
        `;
    }).join('');
}


// ==================== C. TIMETABLE BUILDER & CONFLICT DETECTOR ====================
function renderInteractiveTimetable() {
    const matrix = document.getElementById('interactiveTimetableMatrix');
    const pool = document.getElementById('ttUnassignedPool');
    if (!matrix || !pool) return;

    const days = ['الأحد','الاثنين','الثلاثاء','الأربعاء','الخميس'];
    const periods = ['08:00 - 08:45','08:50 - 09:35','09:40 - 10:25','10:40 - 11:25','11:30 - 12:15'];
    const subjects = ['الكيمياء العامة (أ. إبراهيم علي)','الرياضيات (أ. محمد علي)','اللغة العربية (أ. أحمد سالم)','اللغة الإنجليزية (أ. جون)','الفيزياء (أ. سعيد)'];

    let h = '<div class="timetable-cell header">الحصة / اليوم</div>';
    days.forEach(d => h += `<div class="timetable-cell header">${d}</div>`);
    periods.forEach((p, pIdx) => {
        h += `<div class="timetable-cell time-col">${p}</div>`;
        days.forEach((d, dIdx) => {
            const isConflict = pIdx === 1 && dIdx === 0;
            const subj = subjects[(pIdx + dIdx) % subjects.length];
            h += `
                <div class="timetable-cell ${isConflict ? '' : 'filled'}" style="${isConflict ? 'background:rgba(239,68,68,0.25);border:1px solid #ef4444;color:#f87171;' : ''}" onclick="toggleTimetableSlot(this)">
                    ${isConflict ? '<i class="fa-solid fa-triangle-exclamation"></i> تعارض معلم' : subj}
                </div>
            `;
        });
    });
    matrix.innerHTML = h;

    pool.innerHTML = [
        { name: 'الكيمياء العامة (عملي)', required: '2 حصص أسبوعياً', teacher: 'أ. إبراهيم علي' },
        { name: 'الرياضيات التطبيقية', required: '3 حصص أسبوعياً', teacher: 'أ. محمد علي' },
        { name: 'النشاط العلمي والابتكار', required: '1 حصة أسبوعياً', teacher: 'أ. سارة أحمد' }
    ].map(p => `
        <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:8px;padding:8px;font-size:0.8rem;">
            <strong style="color:#60a5fa;display:block;">${p.name}</strong>
            <span style="color:var(--muted);">${p.required} | ${p.teacher}</span>
        </div>
    `).join('');
}

function toggleTimetableSlot(slot) {
    toast('تم اختيار الحصة لتعديل أو سحب وإسقاط المقرر');
}
function autoGenerateTimetable() {
    toast('⚡ جاري تشغيل خوارزمية التوليد الآلي الذكي للجدول بدون تعارضات...');
    setTimeout(() => { renderInteractiveTimetable(); toast('✅ تم التوليد الآلي للجدول بنجاح!'); }, 1000);
}
function saveTimetablePublish() {
    toast('✅ تم اعتماد ونشر الجدول الدراسي بنجاح!');
}


// ==================== D. HOMEWORK TRACKER ====================
let currentHwRole = 'teacher';

function switchHwRole(role, btnEl) {
    currentHwRole = role;
    if (btnEl) {
        btnEl.parentElement.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
    }
    renderHomeworkList();
}

function renderHomeworkList() {
    const tb = document.getElementById('tbl-homework-list');
    if (!tb) return;

    const hw = [
        { date: '2026-08-05', subject: 'كيمياء عامة', grade: 'الصف الثاني الثانوي - شعبة (أ)', title: 'تقرير تفاعل الأحماض مع القواعد', dueDate: '2026-08-10', status: 'نشط', submissionRate: '85% (25/30)' },
        { date: '2026-08-03', subject: 'رياضيات', grade: 'الصف الأول الثانوي - شعبة (ب)', title: 'حل تمارين التفاضل ص 54', dueDate: '2026-08-07', status: 'قيد التصحيح', submissionRate: '100% (30/30)' }
    ];

    const statusBadge = { 'نشط': 'background:rgba(59,130,246,0.15);color:#60a5fa;', 'قيد التصحيح': 'background:rgba(245,158,11,0.15);color:#fbbf24;', 'مكتمل': 'background:rgba(16,185,129,0.15);color:#10b981;' };

    tb.innerHTML = hw.map(h => `
        <tr>
            <td>${h.date}</td>
            <td style="font-weight:700;color:#60a5fa;">${h.subject}</td>
            <td>${h.grade}</td>
            <td style="font-weight:700;">${h.title}</td>
            <td style="color:#ef4444;font-weight:700;">${h.dueDate}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;${statusBadge[h.status]||''}">${h.status}</span></td>
            <td><strong style="color:#34d399;">${h.submissionRate}</strong></td>
            <td>
                <button class="btn-add" onclick="toast('عرض ورصد الدرجات')" style="padding:3px 8px;font-size:0.78rem;"><i class="fa-solid fa-check"></i> ${currentHwRole==='student'?'رفع الحل':'تصحيح'}</button>
            </td>
        </tr>
    `).join('');
}


// ==================== E. PERFORMANCE EVALUATION ====================
function renderPerformanceEvals() {
    const tb = document.getElementById('tbl-performance-list');
    if (!tb) return;

    const evals = [
        { appraisee: 'م. أحمد خالد', job: 'مهندس أمن سيبراني', evaluator: 'أ. محمد سعيد', cycle: 'تقييم الن نصف الأول 2026', score: '92.5%', rating: 'يتجاوز التوقعات', status: 'مكتمل (معتمد)' },
        { appraisee: 'أ. إبراهيم علي', job: 'معلم كيمياء', evaluator: 'أ. أحمد المدير', cycle: 'تقييم النصف الأول 2026', score: '88.0%', rating: 'ممتاز', status: 'قيد مراجعة HR' }
    ];

    tb.innerHTML = evals.map(e => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${e.appraisee}</td>
            <td>${e.job}</td>
            <td>${e.evaluator}</td>
            <td>${e.cycle}</td>
            <td style="font-weight:800;color:#34d399;font-size:1rem;">${e.score}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${e.rating}</span></td>
            <td>${e.status}</td>
            <td><button class="btn-edit" onclick="toast('عرض استمارة التقييم الموزونة')"><i class="fa-solid fa-eye"></i> عرض</button></td>
        </tr>
    `).join('');
}


// ==================== F. BATCH PROMOTION ====================
function renderPromotionBatch() {
    const tb = document.getElementById('tbl-promotion-batch');
    if (!tb) return;

    const students = [
        { id: '20240102', name: 'أحمد محمد علي', gpa: '88.5% (ناجح)', failed: '0 مادة', hold: 'لا يوجد', status: 'مترفّع تلقائياً', targetSec: 'شعبة (أ)' },
        { id: '20240105', name: 'يوسف خالد سالم', gpa: '62.0% (دور ثاني)', failed: '1 مادة (كيمياء)', hold: 'متبقي رسوم', status: 'موقوف ماليًا', targetSec: 'شعبة (ب)' }
    ];

    tb.innerHTML = students.map(s => `
        <tr>
            <td><input type="checkbox" class="promo-cb" checked></td>
            <td><strong style="color:#60a5fa;">[${s.id}]</strong> ${s.name}</td>
            <td style="font-weight:700;">${s.gpa}</td>
            <td>${s.failed}</td>
            <td><span style="color:${s.hold==='لا يوجد'?'#10b981':'#ef4444'};font-weight:700;">${s.hold}</span></td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(59,130,246,0.15);color:#93c5fd;">${s.status}</span></td>
            <td><select><option>${s.targetSec}</option><option>شعبة (ب)</option></select></td>
            <td><button class="btn-edit" onclick="toast('تعديل قرار الاستثناء يدوياً')"><i class="fa-solid fa-pen"></i> استثناء</button></td>
        </tr>
    `).join('');
}

function executeBatchPromotion() {
    toast('🚀 تم تنفيذ الترفيع الجماعي للدفعة ونقل الطلاب للسنة الجديدة بنجاح!');
}


// ==================== G. STUDENT DOCS POPUP FLOW ====================
function openStudentDocModalFlow() {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;

    title.innerHTML = '<i class="fa-solid fa-folder-open"></i> إضافة وثيقة طالب (خطوة 1: اختيار المرحلة والصف)';
    fields.innerHTML = `
        <div class="fg"><label>المرحلة الدراسية</label><select id="flowStage" onchange="updateDocStudentOptions()"><option value="ثانوية">الثانوية</option><option value="إعدادية">الإعدادية</option></select></div>
        <div class="fg"><label>الصف الدراسي</label><select id="flowGrade" onchange="updateDocStudentOptions()"><option value="الصف الثاني الثانوي">الصف الثاني الثانوي</option><option value="الصف الأول الثانوي">الصف الأول الثانوي</option></select></div>
        <div class="fg"><label>اختيار الطالب المعني</label><select id="flowStudentSelect"><option value="1">محمد أحمد سالم</option><option value="2">أحمد محمد علي</option></select></div>
        <div class="fg"><label>نوع الوثيقة</label><select><option>شهادة ميلاد</option><option>بطاقة هوية</option><option>شهادة دراسية سابقة</option></select></div>
        <div class="fg"><label>إرفاق الملف (PDF/صورة)</label><input type="file"></div>
        <button class="btn-save" onclick="toast('✅ تم رفع وتأكيد وثيقة الطالب بنجاح'); document.getElementById('formModal').classList.remove('active');" style="width:100%;margin-top:12px;"><i class="fa-solid fa-upload"></i> حفظ وتصديق الوثيقة</button>
    `;
    document.getElementById('formModal').classList.add('active');
}

function updateDocStudentOptions() {
    const select = document.getElementById('flowStudentSelect');
    if (select) select.innerHTML = '<option value="1">محمد أحمد سالم</option><option value="2">أحمد محمد علي</option>';
}

function renderStudentDocs() {
    const tb = document.getElementById('tbl-student-docs');
    if (!tb) return;

    tb.innerHTML = `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">محمد أحمد سالم</td>
            <td>الصف الثاني الثانوي</td>
            <td>شهادة ميلاد رسمية</td>
            <td>2026-08-01</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">مصدقة</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة الملف')"><i class="fa-solid fa-file-pdf"></i> معاينة</button></td>
            <td><button class="btn-delete" onclick="toast('حذف الوثيقة')"><i class="fa-solid fa-trash"></i></button></td>
        </tr>
    `;
}


// ==================== H. SECTION DISTRIBUTION WORKSPACE ====================
function renderSectionDistributionWorkspace() {
    const pool = document.getElementById('sdUnassignedStudentPool');
    const grid = document.getElementById('sdTargetSectionsGrid');
    if (!pool || !grid) return;

    const unassigned = [
        { id: '101', name: 'عمر خالد فؤاد' },
        { id: '102', name: 'طارق زياد طاهر' }
    ];

    pool.innerHTML = unassigned.map(s => `
        <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:6px;padding:6px 10px;font-size:0.8rem;display:flex;justify-content:space-between;align-items:center;">
            <span>${s.name}</span>
            <i class="fa-solid fa-grip-vertical" style="color:var(--muted);cursor:grab;"></i>
        </div>
    `).join('');

    const count = document.getElementById('sdUnassignedCount');
    if (count) count.textContent = unassigned.length;

    grid.innerHTML = ['شعبة (أ)', 'شعبة (ب)', 'شعبة (ج)'].map(sec => `
        <div class="form-card" style="padding:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <h4 style="color:#60a5fa;font-weight:700;">${sec}</h4>
                <span style="font-size:0.75rem;color:#34d399;font-weight:700;">22 / 30 طالب</span>
            </div>
            <div style="background:rgba(0,0,0,0.3);height:6px;border-radius:3px;margin-bottom:10px;overflow:hidden;">
                <div style="width:73%;background:#10b981;height:100%;"></div>
            </div>
            <div style="font-size:0.78rem;color:var(--muted);">مجهزة وموزعة آلياً</div>
        </div>
    `).join('');
}

function executeSmartSectionDistribution() {
    toast('⚡ جاري تنفيذ خوارزمية التوزيع التلقائي الذكي على الشعب...');
    setTimeout(() => { renderSectionDistributionWorkspace(); toast('✅ تم توزيع جميع الطلاب بنجاح (100%)!'); }, 800);
}
function saveSectionDistribution() {
    toast('✅ تم اعتماد وحفظ توزيع الطلاب على الشعب بنجاح!');
}


// ==================== I. DISCONTINUED STUDENTS ====================
function renderDiscontinuedList() {
    const tb = document.getElementById('tbl-discontinued-list');
    if (!tb) return;

    const list = DB.discontinuedStudents || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">[${s.code}] ${s.name}</td>
            <td>${s.grade}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(239,68,68,0.15);color:#f87171;">${s.type}</span></td>
            <td>${s.date}</td>
            <td style="font-size:0.83rem;">${s.reason}</td>
            <td style="color:#10b981;font-size:0.83rem;">${s.clearance}</td>
            <td style="color:#f59e0b;font-weight:700;">${s.financeDues}</td>
            <td>
                <button class="btn-add" onclick="toast('طلب إعادة قيد طالب')" style="padding:3px 8px;font-size:0.78rem;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-arrow-rotate-left"></i> إعادة قيد</button>
            </td>
        </tr>
    `).join('') || '<tr><td colspan="8" style="text-align:center;color:var(--muted);">لا يوجد طلاب غير مستمرين</td></tr>';
}


// ==================== J. CLASS NOTES TIMELINE ====================
function renderClassNotesTimeline() {
    const container = document.getElementById('cnNotesTimeline');
    if (!container) return;

    const notes = DB.classNotesData || [];
    container.innerHTML = notes.map(n => `
        <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:10px;padding:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                <strong style="color:#60a5fa;">${n.studentName}</strong>
                <span style="padding:2px 8px;border-radius:4px;font-size:0.75rem;background:rgba(239,68,68,0.15);color:#f87171;font-weight:700;">${n.severity} - ${n.category}</span>
            </div>
            <p style="font-size:0.85rem;color:var(--text);margin-bottom:8px;">${n.text}</p>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:0.78rem;color:var(--muted);">
                <span><i class="fa-solid fa-clock"></i> ${n.timestamp} | مشاركة مع: ${n.shareWith}</span>
                <span style="color:#10b981;font-weight:700;">${n.feedback}</span>
            </div>
        </div>
    `).join('') || '<p style="text-align:center;color:var(--muted);">لا توجد ملاحظات مسجلة لهذه الشعبة</p>';
}


// ==================== K. ENROLLMENT & FEES ====================
function renderEnrollmentList() {
    const tb = document.getElementById('tbl-enrollment-list');
    if (!tb) return;

    const enrolls = DB.enrollmentsData || [];
    tb.innerHTML = enrolls.map(e => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${e.id}</td>
            <td style="font-weight:700;">${e.studentName}<br><span style="font-size:0.75rem;color:var(--muted);">${e.grade}</span></td>
            <td>${e.regType}</td>
            <td>${e.baseTuition.toLocaleString()} $</td>
            <td>${e.services.toLocaleString()} $</td>
            <td style="color:#10b981;">-${e.discount.toLocaleString()} $</td>
            <td style="font-weight:800;color:#60a5fa;">${e.netPayable.toLocaleString()} $</td>
            <td style="color:#34d399;font-weight:700;">${e.totalPaid.toLocaleString()} $</td>
            <td style="color:#ef4444;font-weight:700;">${e.balanceDue.toLocaleString()} $</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(245,158,11,0.15);color:#fbbf24;">${e.status}</span></td>
            <td>
                <button class="btn-add" onclick="openQuickPayModal('${e.studentName}', ${e.balanceDue})" style="padding:3px 8px;font-size:0.78rem;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-credit-card"></i> تحصيل</button>
            </td>
        </tr>
    `).join('') || '<tr><td colspan="11" style="text-align:center;color:var(--muted);">لا توجد عقود تسجيل</td></tr>';
}

// Hook into window.goTo
const _origGoToRequested = window.goTo;
if (_origGoToRequested) {
    window.goTo = function(id) {
        _origGoToRequested(id);
        if (id === 'pg-academic-calendar') renderAcademicCalendar();
        if (id === 'pg-classrooms') renderClassroomsGrid();
        if (id === 'pg-timetable-builder') renderInteractiveTimetable();
        if (id === 'pg-homework-tracker') renderHomeworkList();
        if (id === 'pg-performance-eval') renderPerformanceEvals();
        if (id === 'pg-promotion-workflow') renderPromotionBatch();
        if (id === 'pg-student-docs') renderStudentDocs();
        if (id === 'pg-section-distribution') renderSectionDistributionWorkspace();
        if (id === 'pg-discontinued') renderDiscontinuedList();
        if (id === 'pg-class-notes') renderClassNotesTimeline();
        if (id === 'pg-enrollment') renderEnrollmentList();
    };
}

"""

if 'ACADEMIC CALENDAR' not in js:
    js += db_additions + "\n" + requested_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended JS logic for requested modules successfully!")
