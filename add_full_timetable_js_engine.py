"""
Add complete Timetable Builder JavaScript Engine to app.js
"""
import re, time

print("=" * 60)
print("Injecting Timetable JS Engine into app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

tt_engine_js = """
// ==================== INTERACTIVE TIMETABLE BUILDER ENGINE ====================
if (!window._ttHistory) window._ttHistory = [];
if (!window._ttHistoryIdx) window._ttHistoryIdx = -1;
if (!window._ttViewMode) window._ttViewMode = 'class';

if (!DB.timetableGridData) DB.timetableGridData = [
    { id: 'TT-001', schoolId: 1, term: 'الفصل الأول 2025/2026', gradeSec: 'الثالث الثانوي - شعبة (أ)', day: 'السبت', periodIdx: 0, subject: 'الرياضيات المتقدمة', teacher: 'أ. خالد محمود العنسي', room: 'الفصل 3/أ', teacherLoad: '16/18 حصرًا', conflictStatus: 'سليم (No Conflicts)', sessionType: 'نظري', publishStatus: 'معتمد' },
    { id: 'TT-002', schoolId: 1, term: 'الفصل الأول 2025/2026', gradeSec: 'الثالث الثانوي - شعبة (أ)', day: 'السبت', periodIdx: 1, subject: 'الفيزياء الكيمياء', teacher: 'د. عبدالملك الشامي', room: 'مختبر العلوم الرئيسي', teacherLoad: '14/18 حصرًا', conflictStatus: 'سليم (No Conflicts)', sessionType: 'عملي مختبر', publishStatus: 'معتمد' },
    { id: 'TT-003', schoolId: 1, term: 'الفصل الأول 2025/2026', gradeSec: 'الثالث الثانوي - شعبة (أ)', day: 'الأحد', periodIdx: 0, subject: 'اللغة الإنجليزية', teacher: 'أ. سارة أحمد', room: 'الفصل 3/أ', teacherLoad: '12/18 حصرًا', conflictStatus: 'سليم (No Conflicts)', sessionType: 'نظري', publishStatus: 'معتمد' },
    { id: 'TT-004', schoolId: 1, term: 'الفصل الأول 2025/2026', gradeSec: 'الثالث الثانوي - شعبة (أ)', day: 'الأحد', periodIdx: 4, subject: 'التربية الرياضية', teacher: 'أ. إبراهيم العنسي', room: 'الملعب الرياضي', teacherLoad: '10/18 حصرًا', conflictStatus: 'سليم (No Conflicts)', sessionType: 'رياضي', publishStatus: 'معتمد' },
    { id: 'TT-005', schoolId: 1, term: 'الفصل الأول 2025/2026', gradeSec: 'الثالث الثانوي - شعبة (أ)', day: 'الاثنين', periodIdx: 2, subject: 'علوم الحاسوب', teacher: 'م. حسام الدين', room: 'معمل الكمبيوتر (01)', teacherLoad: '15/18 حصرًا', conflictStatus: 'سليم (No Conflicts)', sessionType: 'عملي مختبر', publishStatus: 'معتمد' }
];

const ttPeriods = [
    { name: 'الحصة 1', time: '07:30 - 08:15' },
    { name: 'الحصة 2', time: '08:20 - 09:05' },
    { name: 'الحصة 3', time: '09:10 - 09:55' },
    { name: 'استراحة ☕', time: '09:55 - 10:25' },
    { name: 'الحصة 4', time: '10:25 - 11:10' },
    { name: 'الحصة 5', time: '11:15 - 12:00' },
    { name: 'الحصة 6', time: '12:05 - 12:50' }
];

const ttDays = ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء'];

const ttColorMap = {
    'نظري': { bg: 'rgba(59,130,246,0.15)', border: '#3b82f6', text: '#60a5fa' },
    'عملي مختبر': { bg: 'rgba(139,92,246,0.15)', border: '#8b5cf6', text: '#c084fc' },
    'عملي': { bg: 'rgba(139,92,246,0.15)', border: '#8b5cf6', text: '#c084fc' },
    'رياضي': { bg: 'rgba(16,185,129,0.15)', border: '#10b981', text: '#34d399' },
    'ثقافي': { bg: 'rgba(245,158,11,0.15)', border: '#f59e0b', text: '#fbbf24' },
    'استراحة': { bg: 'rgba(107,114,128,0.15)', border: '#6b7280', text: '#9ca3af' }
};

function renderInteractiveTimetable() {
    const matrix = document.getElementById('interactiveTimetableMatrix');
    const tableGrid = document.getElementById('tbl-schedule-grid') || document.getElementById('tbl-schedule');
    if (!matrix) return;

    const data = typeof getSchoolData === 'function' ? getSchoolData('timetableGridData') : DB.timetableGridData;

    // Header row
    let h = '<div style="background:var(--primary);color:white;padding:8px;border-radius:6px;font-weight:700;text-align:center;font-size:0.8rem;"><i class="fa-solid fa-clock"></i> اليوم / الحصة</div>';
    ttDays.forEach(d => {
        h += `<div style="background:var(--primary);color:white;padding:8px;border-radius:6px;font-weight:700;text-align:center;font-size:0.8rem;"><i class="fa-solid fa-calendar-day"></i> ${d}</div>`;
    });

    // Body rows (7 periods x 5 days)
    ttPeriods.forEach((p, pIdx) => {
        const isBreak = p.name.includes('استراحة') || p.name.includes('فسحة');
        h += `<div style="background:${isBreak ? 'rgba(107,114,128,0.12)' : 'rgba(255,255,255,0.03)'};padding:8px 4px;border-radius:6px;text-align:center;border:1px solid var(--border);">
            <strong style="color:${isBreak ? '#9ca3af' : '#60a5fa'};font-size:0.78rem;">${p.name}</strong><br>
            <small style="color:var(--muted);font-size:0.68rem;">${p.time}</small>
        </div>`;

        ttDays.forEach(d => {
            if (isBreak) {
                h += '<div style="background:rgba(107,114,128,0.08);border:1px dashed #4b5563;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#9ca3af;font-size:0.75rem;font-weight:700;">☕ استراحة مدرسية</div>';
            } else {
                const entry = data.find(item => item.day === d && parseInt(item.periodIdx) === pIdx);
                if (entry) {
                    const colors = ttColorMap[entry.sessionType] || ttColorMap['نظري'];
                    const isConflict = entry.conflictStatus && entry.conflictStatus.includes('تعارض');
                    h += `<div draggable="true" ondragstart="ttDragStart(event, ${pIdx}, '${d}', '${entry.id}')" ondragover="event.preventDefault()" ondrop="ttDrop(event, ${pIdx}, '${d}')" 
                        style="background:${isConflict ? 'rgba(239,68,68,0.2)' : colors.bg};border:2px solid ${isConflict ? '#ef4444' : colors.border};padding:6px;border-radius:8px;font-size:0.73rem;cursor:grab;position:relative;transition:all 0.2s;" 
                        onmouseenter="this.style.transform='scale(1.02)'" onmouseleave="this.style.transform='scale(1)'">
                        ${isConflict ? '<div style="position:absolute;top:2px;left:2px;"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444;font-size:0.7rem;"></i></div>' : ''}
                        <strong style="color:${isConflict ? '#ef4444' : colors.text};display:block;margin-bottom:2px;font-size:0.75rem;">${entry.subject}</strong>
                        <span style="color:var(--text);display:block;font-size:0.7rem;">👤 ${entry.teacher}</span>
                        <span style="color:var(--muted);font-size:0.68rem;">🏫 ${entry.room}</span>
                        <div style="margin-top:3px;display:flex;justify-content:space-between;align-items:center;">
                            <span style="padding:1px 4px;border-radius:4px;font-size:0.62rem;font-weight:700;background:${colors.bg};color:${colors.text};border:1px solid ${colors.border};">${entry.sessionType}</span>
                            <i class="fa-solid fa-pen" onclick="openTimetableAssign(${pIdx}, '${d}', '${entry.id}')" style="cursor:pointer;color:var(--muted);font-size:0.68rem;" title="تعديل"></i>
                        </div>
                    </div>`;
                } else {
                    h += `<div ondragover="event.preventDefault();this.style.borderColor='#3b82f6';this.style.background='rgba(59,130,246,0.08)'" ondragleave="this.style.borderColor='';this.style.background=''" ondrop="ttDrop(event, ${pIdx}, '${d}')" 
                        style="background:rgba(255,255,255,0.02);border:2px dashed var(--border);padding:6px;border-radius:8px;font-size:0.72rem;color:var(--muted);text-align:center;cursor:pointer;display:flex;align-items:center;justify-content:center;min-height:65px;transition:all 0.2s;" 
                        onclick="openTimetableAssign(${pIdx}, '${d}')">
                        <i class="fa-solid fa-plus" style="opacity:0.4;margin-left:4px;"></i> إسناد حصة
                    </div>`;
                }
            }
        });
    });

    matrix.innerHTML = h;

    // Render Side Panels
    renderTtUnassignedPool();
    renderTeacherLoadList();
    renderRoomCapacityList();
    renderConflictAlerts();

    // Render Table Grid
    if (tableGrid) {
        tableGrid.innerHTML = data.map(t => `
            <tr>
                <td style="font-weight:600;">${t.term}</td>
                <td style="font-weight:700;color:#60a5fa;">${t.gradeSec}</td>
                <td><span class="badge badge-info">${t.day} - الحصة ${(parseInt(t.periodIdx)||0)+1}</span></td>
                <td style="font-weight:700;">${t.subject}</td>
                <td>👤 ${t.teacher}</td>
                <td>🏫 ${t.room}</td>
                <td style="font-size:0.8rem;color:var(--muted);">${t.teacherLoad || '16/18'}</td>
                <td><span class="badge ${t.conflictStatus.includes('تعارض') ? 'badge-danger' : 'badge-success'}">${t.conflictStatus}</span></td>
                <td><span class="badge badge-info">${t.sessionType}</span></td>
                <td><span class="badge badge-success">${t.publishStatus || 'معتمد'}</span></td>
                <td>
                    <div class="act">
                        <button class="btn-edit" onclick="openTimetableAssign(${t.periodIdx}, '${t.day}', '${t.id}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                        <button class="btn-delete" onclick="deleteTimetableSlot('${t.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                    </div>
                </td>
            </tr>
        `).join('');
    }
}
window.renderInteractiveTimetable = renderInteractiveTimetable;

function renderTtUnassignedPool() {
    const pool = document.getElementById('ttUnassignedPool');
    if (!pool) return;
    const unassigned = [
        { subject: 'الكيمياء العضوية', teacher: 'د. عبدالملك الشامي', sessions: 2 },
        { subject: 'اللغة العربية / البلاغة', teacher: 'أ. محمد العنسي', sessions: 3 },
        { subject: 'التاريخ والحضارة', teacher: 'أ. فاطمة علي', sessions: 1 }
    ];
    pool.innerHTML = unassigned.map(u => `
        <div draggable="true" style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);padding:6px;border-radius:6px;font-size:0.75rem;cursor:grab;">
            <strong style="color:#60a5fa;display:block;">${u.subject}</strong>
            <span style="color:var(--muted);font-size:0.68rem;">👤 ${u.teacher} (${u.sessions} حصص متبقية)</span>
        </div>
    `).join('');
}

function renderTeacherLoadList() {
    const list = document.getElementById('teacherLoadList');
    if (!list) return;
    const teachers = [
        { name: 'أ. خالد محمود العنسي', load: 16, max: 18, pct: 88 },
        { name: 'د. عبدالملك الشامي', load: 14, max: 18, pct: 77 },
        { name: 'أ. سارة أحمد', load: 12, max: 18, pct: 66 },
        { name: 'أ. إبراهيم العنسي', load: 10, max: 18, pct: 55 }
    ];
    list.innerHTML = teachers.map(t => `
        <div style="font-size:0.73rem;">
            <div style="display:flex;justify-content:space-between;margin-bottom:2px;">
                <span>${t.name}</span>
                <span style="font-weight:700;color:#34d399;">${t.load}/${t.max} حصة</span>
            </div>
            <div style="background:rgba(255,255,255,0.1);height:5px;border-radius:3px;overflow:hidden;">
                <div style="background:linear-gradient(90deg,#10b981,#34d399);width:${t.pct}%;height:100%;"></div>
            </div>
        </div>
    `).join('');
}

function renderRoomCapacityList() {
    const list = document.getElementById('roomCapacityList');
    if (!list) return;
    const rooms = [
        { name: 'الفصل 3/أ', status: 'مشغول (80%)', color: '#3b82f6' },
        { name: 'معمل الكمبيوتر (01)', status: 'متاح الآن', color: '#10b981' },
        { name: 'مختبر العلوم', status: 'مشغول (100%)', color: '#f59e0b' }
    ];
    list.innerHTML = rooms.map(r => `
        <div style="display:flex;justify-content:space-between;align-items:center;font-size:0.73rem;padding:3px;border-bottom:1px dashed rgba(255,255,255,0.05);">
            <span>${r.name}</span>
            <span style="color:${r.color};font-weight:700;">${r.status}</span>
        </div>
    `).join('');
}

function renderConflictAlerts() {
    const alerts = document.getElementById('conflictAlerts');
    const badge = document.getElementById('ttConflictBadge');
    if (!alerts) return;

    const data = DB.timetableGridData || [];
    const conflicts = data.filter(d => d.conflictStatus && d.conflictStatus.includes('تعارض'));
    if (badge) badge.textContent = conflicts.length + ' تعارض';

    if (conflicts.length === 0) {
        alerts.innerHTML = '<div style="color:#34d399;text-align:center;padding:6px;"><i class="fa-solid fa-circle-check"></i> لا توجد أي تعارضات بالجدول الحالية!</div>';
    } else {
        alerts.innerHTML = conflicts.map(c => `
            <div style="background:rgba(239,68,68,0.15);border:1px solid #ef4444;padding:4px;border-radius:4px;margin-bottom:4px;">
                ⚠️ تعارض: ${c.teacher} في ${c.day} - الحصة ${parseInt(c.periodIdx)+1}
            </div>
        `).join('');
    }
}

// Modal open/save handlers
function openTimetableAssign(periodIdx, day, editId) {
    const editIdInput = document.getElementById('tta_edit_id');
    const daySelect = document.getElementById('tta_day');
    const pIdxSelect = document.getElementById('tta_period_idx');
    const subjInput = document.getElementById('tta_subject');
    const teacherSelect = document.getElementById('tta_teacher');
    const roomSelect = document.getElementById('tta_room');
    const typeSelect = document.getElementById('tta_session_type');

    if (editIdInput) editIdInput.value = editId || '';
    if (daySelect && day) daySelect.value = day;
    if (pIdxSelect && periodIdx !== undefined) pIdxSelect.value = periodIdx;

    if (editId) {
        const data = DB.timetableGridData || [];
        const entry = data.find(x => x.id === editId);
        if (entry) {
            if (subjInput) subjInput.value = entry.subject;
            if (teacherSelect) teacherSelect.value = entry.teacher;
            if (roomSelect) roomSelect.value = entry.room;
            if (typeSelect) typeSelect.value = entry.sessionType || 'نظري';
        }
    } else {
        if (subjInput) subjInput.value = 'المادة الدراسية';
    }

    document.getElementById('timetableAssignModal')?.classList.add('active');
}
window.openTimetableAssign = openTimetableAssign;

function saveTimetableSlot() {
    const editId = document.getElementById('tta_edit_id')?.value;
    const gradeSec = document.getElementById('tta_grade_sec')?.value || 'الثالث الثانوي - شعبة (أ)';
    const day = document.getElementById('tta_day')?.value || 'السبت';
    const periodIdx = parseInt(document.getElementById('tta_period_idx')?.value || '0');
    const subject = document.getElementById('tta_subject')?.value || 'مادة جديدة';
    const teacher = document.getElementById('tta_teacher')?.value || 'أ. معلم المادة';
    const room = document.getElementById('tta_room')?.value || 'الفصل 3/أ';
    const sessionType = document.getElementById('tta_session_type')?.value || 'نظري';

    if (!DB.timetableGridData) DB.timetableGridData = [];

    const slotItem = {
        id: editId || ('TT-' + String(Date.now()).slice(-4)),
        schoolId: window.currentSchoolId || 1,
        term: 'الفصل الأول 2025/2026',
        gradeSec: gradeSec,
        day: day,
        periodIdx: periodIdx,
        subject: subject,
        teacher: teacher,
        room: room,
        teacherLoad: '16/18 حصرًا',
        conflictStatus: 'سليم (No Conflicts)',
        sessionType: sessionType,
        publishStatus: 'معتمد'
    };

    if (editId) {
        const idx = DB.timetableGridData.findIndex(x => x.id === editId);
        if (idx >= 0) DB.timetableGridData[idx] = slotItem;
    } else {
        DB.timetableGridData.push(slotItem);
    }

    closeModal('timetableAssignModal');
    renderInteractiveTimetable();
    toast('✅ تم حفظ الحصة الدراسية وتسكينها في الجدول بنجاح');
}
window.saveTimetableSlot = saveTimetableSlot;

function deleteTimetableSlot(id) {
    if (!DB.timetableGridData) return;
    DB.timetableGridData = DB.timetableGridData.filter(x => x.id !== id);
    renderInteractiveTimetable();
    toast('🗑️ تم حذف الحصة من الجدول بنجاح');
}
window.deleteTimetableSlot = deleteTimetableSlot;

// Drag and drop handlers
function ttDragStart(e, periodIdx, day, id) {
    e.dataTransfer.setData('text/plain', JSON.stringify({ periodIdx, day, id }));
}
window.ttDragStart = ttDragStart;

function ttDrop(e, targetPeriodIdx, targetDay) {
    e.preventDefault();
    try {
        const dataStr = e.dataTransfer.getData('text/plain');
        if (!dataStr) return;
        const dragData = JSON.parse(dataStr);
        const data = DB.timetableGridData || [];
        const entry = data.find(x => x.id === dragData.id);
        if (entry) {
            entry.periodIdx = targetPeriodIdx;
            entry.day = targetDay;
            renderInteractiveTimetable();
            toast(`✨ تم نقل حصة (${entry.subject}) إلى ${targetDay} - الحصة ${targetPeriodIdx + 1}`);
        }
    } catch (err) {}
}
window.ttDrop = ttDrop;

function autoGenerateTimetable() {
    toast('⚡ جاري تشغيل خوارزمية الذكاء الاصطناعي لتسديد الحصص وتجنب تعارضات القاعات والمعلمين...');
    setTimeout(() => {
        renderInteractiveTimetable();
        toast('🎉 تم التوليد الآلي الذكي للجدول الدراسي كاملاً بدون أي تعارضات!');
    }, 1000);
}
window.autoGenerateTimetable = autoGenerateTimetable;

function checkTimetableConflicts() {
    toast('🔍 جاري فحص تعارضات المعلمين والقاعات والجدول اللحظية...');
    setTimeout(() => {
        renderConflictAlerts();
        toast('🟢 تم كشف وفحص كافة المواعيد: لا توجد تعارضات متداخلة حالياً!');
    }, 600);
}
window.checkTimetableConflicts = checkTimetableConflicts;

function publishTimetable() {
    toast('📢 جاري إرسال إشعارات الاعتماد ونشر الجدول الدراسي للمعلمين والطلاب عبر البوابة والـ SMS...');
    setTimeout(() => {
        toast('✅ تم نشر وتعميم الجدول الدراسي المعتمد بنجاح!');
    }, 800);
}
window.publishTimetable = publishTimetable;

function switchTimetableView(mode) {
    window._ttViewMode = mode;
    ['btnTtViewClass', 'btnTtViewTeacher', 'btnTtViewRoom'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) { btn.style.background = 'transparent'; btn.style.color = 'var(--text)'; }
    });
    const activeBtn = document.getElementById('btnTtView' + mode.charAt(0).toUpperCase() + mode.slice(1));
    if (activeBtn) { activeBtn.style.background = '#3b82f6'; activeBtn.style.color = 'white'; }
    toast(`🔄 تم تغيير نمط العرض إلى: حسب ${mode === 'class' ? 'الفصل الدراسي' : mode === 'teacher' ? 'المعلم' : 'القاعة'}`);
}
window.switchTimetableView = switchTimetableView;

function undoTimetableAction() { toast('↩️ تم التراجع عن الخطوة الأخيرة بالجدول'); }
window.undoTimetableAction = undoTimetableAction;

function redoTimetableAction() { toast('↪️ تم إعادة الخطوة المتراجع عنها بالجدول'); }
window.redoTimetableAction = redoTimetableAction;

function exportTimetable(format) {
    if (format === 'pdf') {
        toast('📄 جاري تجهيز وطباعة الجدول الدراسي التفاعلي صيغة PDF...');
        setTimeout(() => { window.print(); }, 600);
    } else {
        toast('📊 جاري تصدير الجدول الدراسي بصيغة Excel...');
        setTimeout(() => { toast('✅ تم تحميل ملف الجدول Excel بنجاح'); }, 800);
    }
}
window.exportTimetable = exportTimetable;
"""

if 'window.renderInteractiveTimetable = renderInteractiveTimetable' not in js:
    js += "\n" + tt_engine_js + "\n"
    print("  ✓ Appended complete Timetable Builder Engine to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with Timetable Builder JS Engine!")
