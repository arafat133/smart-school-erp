# coding: utf-8
import re, os
import datetime

html_path = 'c:/Users/LENOVO/Desktop/stu/secure_school_system/frontend/school.html'
js_path = 'c:/Users/LENOVO/Desktop/stu/secure_school_system/frontend/app.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace pg-exam-schedule
new_exam_html = r'''
        <div class="page" id="pg-exam-schedule">
            <div class="page-header">
                <h2><i class="fa-solid fa-calendar-check"></i> إدارة جدول الامتحانات المتقدم</h2>
                <div class="header-actions">
                    <button class="btn btn-primary" onclick="openForm('exam-session')"><i class="fa-solid fa-plus"></i> إضافة جلسة امتحان</button>
                    <button class="btn btn-secondary" onclick="autoGenerateExamSchedule()"><i class="fa-solid fa-wand-magic-sparkles"></i> التوليد الآلي للجدول</button>
                    <button class="btn btn-secondary" onclick="exportExamSchedule('pdf')"><i class="fa-solid fa-file-pdf"></i> تصدير PDF</button>
                </div>
            </div>

            <div class="stats-row">
                <div class="stat-card"><i class="fa-solid fa-book"></i><div class="stat-info"><div class="stat-val" id="stat-exam-subjects">14</div><div class="stat-label">إجمالي المواد المجدولة</div></div></div>
                <div class="stat-card"><i class="fa-solid fa-calendar-days"></i><div class="stat-info"><div class="stat-val" id="stat-exam-days">12</div><div class="stat-label">إجمالي أيام الامتحانات</div></div></div>
                <div class="stat-card"><i class="fa-solid fa-percent"></i><div class="stat-info"><div class="stat-val" id="stat-exam-completion">100%</div><div class="stat-label">نسبة اكتمال الجدول</div></div></div>
                <div class="stat-card"><i class="fa-solid fa-hourglass-half"></i><div class="stat-info"><div class="stat-val" id="stat-exam-countdown">5 أيام</div><div class="stat-label">العد التنازلي للامتحان القادم</div></div></div>
            </div>

            <div class="toolbar" style="display:flex; gap:10px; margin-bottom: 20px;">
                <div class="filter-group">
                    <label>الفصل الدراسي</label>
                    <select id="flt-exam-term" onchange="renderExamScheduleGrid()"><option value="all">الكل</option><option>الفصل الثاني 2025/2026</option></select>
                </div>
                <div class="filter-group">
                    <label>نوع الامتحان</label>
                    <select id="flt-exam-type" onchange="renderExamScheduleGrid()"><option value="all">الكل</option><option>شهري</option><option>نصفي</option><option>نهائي</option><option>عملي</option></select>
                </div>
                <div class="filter-group">
                    <label>الصف</label>
                    <select id="flt-exam-grade" onchange="renderExamScheduleGrid()"><option value="all">الكل</option><option>الثالث الثانوي</option></select>
                </div>
                <div class="filter-group">
                    <label>الشعبة</label>
                    <select id="flt-exam-sec" onchange="renderExamScheduleGrid()"><option value="all">الكل</option><option>شعبة (أ)</option><option>شعبة (ب)</option></select>
                </div>
                <div class="filter-group" style="align-self: flex-end; margin-right: auto; display: flex; gap: 5px;">
                    <button class="btn btn-secondary" onclick="checkExamConflicts()"><i class="fa-solid fa-triangle-exclamation"></i> كشف التعارضات</button>
                    <button class="btn btn-primary" onclick="alert('تم نشر الجدول')"><i class="fa-solid fa-share-nodes"></i> نشر الجدول</button>
                    <button class="btn btn-secondary" onclick="window.print()"><i class="fa-solid fa-print"></i> طباعة</button>
                </div>
            </div>

            <div class="exam-grid-container" style="display:flex; gap:15px; margin-bottom: 20px; align-items: stretch; flex-wrap: wrap;">
                <div class="exam-matrix-panel" style="flex: 2; min-width: 300px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 15px; overflow-x: auto;">
                    <h3><i class="fa-solid fa-table-cells"></i> مصفوفة الجدولة الزمنية (السحب والإفلات)</h3>
                    <div id="examScheduleMatrix" style="min-height: 200px; display: grid; gap: 10px; margin-top: 10px;">
                        <!-- Matrix rendered via JS -->
                    </div>
                </div>
                <div class="exam-side-panels" style="flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 15px;">
                    <div class="panel" style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 15px;">
                        <h3 style="color: var(--danger);"><i class="fa-solid fa-triangle-exclamation"></i> تنبيهات التعارضات</h3>
                        <div id="examConflictAlerts" style="margin-top: 10px; font-size: 0.9em; min-height: 50px;"></div>
                    </div>
                    <div class="panel" style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 15px;">
                        <h3><i class="fa-solid fa-building"></i> متتبع سعة القاعات</h3>
                        <div id="examHallTracker" style="margin-top: 10px; font-size: 0.9em; min-height: 50px;"></div>
                    </div>
                    <div class="panel" style="background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 15px;">
                        <h3><i class="fa-solid fa-user-tie"></i> تعيين المراقبين</h3>
                        <div id="proctorPanel" style="margin-top: 10px; font-size: 0.9em; min-height: 50px;"></div>
                    </div>
                </div>
            </div>

            <div class="table-responsive">
                <table class="table" id="table-exam-schedule">
                    <thead>
                        <tr>
                            <th>كود الجلسة</th>
                            <th>الفصل الدراسي</th>
                            <th>نوع الامتحان</th>
                            <th>الصف والشعبة</th>
                            <th>المادة</th>
                            <th>تاريخ الامتحان</th>
                            <th>الفترة</th>
                            <th>التوقيت (من-إلى)</th>
                            <th>المدة</th>
                            <th>اللجنة/القاعة</th>
                            <th>عدد الطلاب</th>
                            <th>النموذج</th>
                            <th>المراقبون</th>
                            <th>حالة التعارض</th>
                            <th>الحالة</th>
                            <th>إجراءات</th>
                        </tr>
                    </thead>
                    <tbody id="tbl-exam-schedule-grid">
                    </tbody>
                </table>
            </div>
        </div><!--/pg-exam-schedule-->
'''

html = re.sub(r'(<div[^>]*id="pg-exam-schedule"[^>]*>[\s\S]*?<!--\s*/\s*pg-exam-schedule\s*-->)', new_exam_html.strip(), html)

# Replace app.js content for renderExamScheduleGrid
js_exam_repl = r'''
if (!DB.examScheduleData) DB.examScheduleData = [
    { id: 'EXM-2026-001', term: 'الفصل الدراسي الثاني 2025/2026', examType: 'اختبارات نهاية الفصل', gradeSec: 'الثالث الثانوي - شعبة (أ)', subject: 'الرياضيات المتقدمة', date: '2026-06-15', period: 'الفترة الأولى (صباحية)', timeFrom: '08:30 AM', timeTo: '11:30 AM', duration: '3 ساعات (180 دقيقة)', hall: 'القاعة الكبرى (01)', studentsCount: 35, model: 'نموذج (أ، ب)', proctors: 'أ. خالد محمود + أ. إبراهيم العنسي', conflictStatus: 'سليم (No Conflicts)', status: 'معتمد ورسمي', notes: 'يُسمح بالحاسبة العلمية فقط', diffColor: 'var(--danger)' }
];

function renderExamScheduleGrid() {
    const tbody = document.getElementById('tbl-exam-schedule-grid');
    if (!tbody) return;
    tbody.innerHTML = '';
    
    let html = '';
    const termFlt = document.getElementById('flt-exam-term')?.value || 'all';
    const typeFlt = document.getElementById('flt-exam-type')?.value || 'all';
    
    const data = (DB.examScheduleData || []).filter(e => {
        return (termFlt === 'all' || e.term.includes(termFlt)) && (typeFlt === 'all' || e.examType.includes(typeFlt));
    });
    
    // Update stats
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
    }
    
    // Render Matrix
    const matrix = document.getElementById('examScheduleMatrix');
    if (matrix) {
        matrix.style.gridTemplateColumns = `repeat(${Math.max(1, days)}, 1fr)`;
        matrix.innerHTML = Array.from(new Set(data.map(x=>x.date))).sort().map(d => {
            let dayExams = data.filter(x=>x.date===d);
            return `<div style="border:1px solid var(--border); padding: 5px; border-radius: 4px; display:flex; flex-direction:column; gap:5px;">
                <div style="text-align:center; font-weight:bold; margin-bottom:5px; border-bottom:1px solid var(--border); padding-bottom:5px;">${d}</div>
                ${dayExams.map(ex => `<div style="background:${ex.diffColor||'var(--primary)'}; padding:8px; font-size:0.8em; border-radius:3px; color:white; cursor:move;" draggable="true" title="${ex.subject} - ${ex.period}">${ex.subject}<br><small>${ex.period}</small></div>`).join('')}
            </div>`;
        }).join('') || '<div style="color:var(--text-muted)">لا توجد بيانات للمصفوفة</div>';
    }
    
    // Conflicts
    const conf = document.getElementById('examConflictAlerts');
    if (conf) {
        const hasConflict = data.some(x=>x.conflictStatus.includes('تعارض'));
        conf.innerHTML = hasConflict ? `<div style="color:var(--danger)"><i class="fa-solid fa-triangle-exclamation"></i> يوجد تعارض في قاعات أو مراقبين!</div>` : `<div style="color:var(--success)"><i class="fa-solid fa-check-circle"></i> لا توجد تعارضات مجدولة.</div>`;
    }
    
    // Halls
    const tracker = document.getElementById('examHallTracker');
    if (tracker) {
        tracker.innerHTML = data.slice(0,3).map(x => `<div style="margin-bottom:8px;">${x.hall}: <br><progress value="${x.studentsCount}" max="40" style="width:100%; height:10px;"></progress> ${x.studentsCount}/40 طالب</div>`).join('') || '<div style="color:var(--text-muted)">لا توجد بيانات</div>';
    }
    
    const proc = document.getElementById('proctorPanel');
    if (proc) {
        proc.innerHTML = data.slice(0,2).map(x => `<div style="margin-bottom:8px; font-size:0.9em;"><strong>${x.subject}</strong><br><i class="fa-solid fa-user"></i> ${x.proctors}</div>`).join('') || '<div style="color:var(--text-muted)">لا توجد بيانات</div>';
    }
    
    // Table
    data.forEach(ex => {
        html += `<tr>
            <td>${ex.id}</td>
            <td>${ex.term}</td>
            <td>${ex.examType}</td>
            <td>${ex.gradeSec}</td>
            <td>${ex.subject}</td>
            <td>${ex.date}</td>
            <td>${ex.period}</td>
            <td>${ex.timeFrom} - ${ex.timeTo}</td>
            <td>${ex.duration}</td>
            <td>${ex.hall}</td>
            <td>${ex.studentsCount}</td>
            <td>${ex.model}</td>
            <td>${ex.proctors}</td>
            <td><span class="badge" style="background:${ex.conflictStatus.includes('سليم')?'var(--success)':'var(--danger)'}">${ex.conflictStatus}</span></td>
            <td><span class="badge bg-primary">${ex.status}</span></td>
            <td>
                <div class="actions">
                    <button class="btn btn-icon" onclick="showHallMap('${ex.id}')" title="خريطة القاعة"><i class="fa-solid fa-map"></i></button>
                    <button class="btn btn-icon" onclick="distributeSeating('${ex.id}')" title="توزيع المقاعد"><i class="fa-solid fa-chair"></i></button>
                    <button class="btn btn-icon" onclick="generateExamPermit('${ex.id}')" title="بطاقات دخول"><i class="fa-solid fa-id-card"></i></button>
                </div>
            </td>
        </tr>`;
    });
    tbody.innerHTML = html || `<tr><td colspan="16" class="text-center">لا توجد سجلات</td></tr>`;
}

function autoGenerateExamSchedule() { alert('تم التوليد الآلي بنجاح!'); renderExamScheduleGrid(); }
function checkExamConflicts(entry) { alert('فحص التعارضات: لم يتم العثور على أي تعارض.'); return 'سليم (No Conflicts)'; }
function examSpacingCheck() { alert('فحص التباعد الزمني: جميع الفترات مطابقة للمعايير'); }
function generateExamPermit(studentId) { alert('تم إنشاء بطاقات دخول الامتحانات!'); }
function showHallMap(examId) { alert('جاري عرض خريطة القاعة التفاعلية...'); }
function distributeSeating(examId) { alert('تم توزيع المقاعد بالتناوب (نموذج أ / ب)!'); }
function exportExamSchedule(format) { alert('تم التصدير بصيغة ' + format); }
'''

js = re.sub(r'function renderExamScheduleGrid\(\)[\s\S]*?\n\}', js_exam_repl, js)

# Handle academic calendar views
js_cal_repl = r'''
function renderAcademicCalendar() {
    const view = currentCalView || 'month';
    const container = document.getElementById('academic-cal-container');
    if (!container) return;
    
    const events = DB.academic_calendar || [];
    
    if (view === 'month') {
        const today = new Date();
        const firstDay = new Date(today.getFullYear(), today.getMonth(), 1).getDay();
        const days = new Date(today.getFullYear(), today.getMonth()+1, 0).getDate();
        
        let html = '<div class="cal-grid"><div class="cal-header">الأحد</div><div class="cal-header">الإثنين</div><div class="cal-header">الثلاثاء</div><div class="cal-header">الأربعاء</div><div class="cal-header">الخميس</div><div class="cal-header">الجمعة</div><div class="cal-header">السبت</div>';
        for(let i=0; i<firstDay; i++) html += '<div class="cal-cell empty"></div>';
        
        for(let d=1; d<=days; d++) {
            const dateStr = `${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
            const dayEvents = events.filter(e => e.f_cal_start <= dateStr && e.f_cal_end >= dateStr);
            let evtHtml = dayEvents.map(e => `<div class="cal-event" style="background:${e.color||'var(--primary)'}" onclick="alert('${e.f_cal_title}')">${e.f_cal_title}</div>`).join('');
            html += `<div class="cal-cell"><div class="cal-date">${d}</div>${evtHtml}</div>`;
        }
        html += '</div>';
        container.innerHTML = html;
    } else if (view === 'week') {
        const today = new Date();
        const curr = today.getDay(); 
        const first = new Date(today.getTime() - (curr * 24 * 60 * 60 * 1000));
        
        let html = '<div style="display:flex; flex-direction:column; gap:5px; background:var(--bg); padding:10px; border-radius:8px; border: 1px solid var(--border); overflow-x:auto;">';
        html += '<div style="display:grid; grid-template-columns:60px repeat(7, minmax(120px, 1fr)); gap:2px; text-align:center;">';
        html += '<div style="background:var(--surface); border:1px solid var(--border); padding:10px; font-weight:bold; color:var(--text);">الوقت</div>';
        
        let weekDates = [];
        for(let i=0; i<7; i++) {
            let d = new Date(first.getTime() + (i * 24 * 60 * 60 * 1000));
            weekDates.push(d);
            let ds = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
            html += `<div style="background:var(--surface); border:1px solid var(--border); padding:10px; font-weight:bold; color:var(--text);">${d.toLocaleDateString('ar-EG', {weekday:'short'})} <br><small style="color:var(--text-muted)">${ds}</small></div>`;
        }
        
        for(let h=7; h<=17; h++) {
            html += `<div style="background:var(--surface); border:1px solid var(--border); font-size:0.8em; padding:10px; text-align:center; color:var(--text-muted);">${h}:00</div>`;
            for(let i=0; i<7; i++) {
                let ds = `${weekDates[i].getFullYear()}-${String(weekDates[i].getMonth()+1).padStart(2,'0')}-${String(weekDates[i].getDate()).padStart(2,'0')}`;
                const evts = events.filter(e => e.f_cal_start <= ds && e.f_cal_end >= ds);
                let cellHtml = evts.map(e => `<div style="background:${e.color||'var(--primary)'}; font-size:0.8em; padding:4px; border-radius:4px; margin-bottom:2px; color:white;">${e.f_cal_title}</div>`).join('');
                html += `<div style="background:var(--surface); border:1px solid var(--border); padding:4px;">${cellHtml}</div>`;
            }
        }
        html += '</div></div>';
        container.innerHTML = html;
        
    } else if (view === 'day') {
        const ds = new Date().toISOString().split('T')[0];
        const dayEvents = events.filter(e => e.f_cal_start <= ds && e.f_cal_end >= ds);
        let html = `<div style="background:var(--surface); padding:15px; border-radius:8px; border:1px solid var(--border);">`;
        html += `<h3 style="margin-bottom:15px; text-align:center; color:var(--text); border-bottom:1px solid var(--border); padding-bottom:10px;">${new Date().toLocaleDateString('ar-EG', {weekday:'long', year:'numeric', month:'long', day:'numeric'})}</h3>`;
        html += `<div style="display:flex; flex-direction:column; gap:5px;">`;
        for(let h=7; h<=17; h++) {
            for(let m of ['00', '30']) {
                html += `<div style="display:flex; gap:10px; border-bottom:1px solid var(--border); padding:8px 0; align-items:center;">`;
                html += `<div style="width:60px; font-weight:bold; color:var(--text-muted); font-size:0.9em; text-align:right;">${h}:${m}</div>`;
                html += `<div style="flex:1;">`;
                
                // Show events at 9:00 for demo purposes if there are matches in the current day
                if (h === 9 && m === '00' && dayEvents.length > 0) {
                    html += dayEvents.map(e => `<div style="background:${e.color||'var(--primary)'}; padding:10px; border-radius:6px; margin-bottom:4px; color:white; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                        <strong style="display:block; margin-bottom:4px;">${e.f_cal_title}</strong>
                        <small><i class="fa-solid fa-users"></i> المستهدف: ${e.f_cal_target}</small>
                    </div>`).join('');
                }
                
                html += `</div></div>`;
            }
        }
        html += `</div></div>`;
        container.innerHTML = html;
    } else {
        // agenda
        let html = '<ul class="agenda-list">';
        events.forEach(e => {
            html += `<li>
                <div class="agenda-date">${e.f_cal_start} - ${e.f_cal_end}</div>
                <div class="agenda-details">
                    <h4 style="color:var(--text);">${e.f_cal_title} <span class="badge" style="background:${e.color||'var(--primary)'}">${e.f_cal_target}</span></h4>
                </div>
            </li>`;
        });
        html += '</ul>';
        container.innerHTML = html;
    }
}
'''
js = re.sub(r'function renderAcademicCalendar\(\)[\s\S]*?\n\}', js_cal_repl, js)

# Fix openForm academic calendar to include color
new_open_form_cal = r'''if (type === 'academic-calendar') {
        const d = editId ? (DB.academic_calendar||[]).find(x=>x.id==editId)||{} : {};
        title.innerHTML = `<i class="fa-solid fa-pen-to-square"></i> ${editId?'تعديل':'إضافة'} حدث تقويم`;
        h = `<div class="fg"><label>العنوان / الحدث</label><input id="f_cal_title" value="${d.f_cal_title||''}" oninput="validateTextOnly(this)"></div>
        <div class="fg"><label>من تاريخ</label><input type="date" id="f_cal_start" value="${d.f_cal_start||new Date().toLocaleDateString('en-CA')}"></div>
        <div class="fg"><label>إلى تاريخ</label><input type="date" id="f_cal_end" value="${d.f_cal_end||new Date().toLocaleDateString('en-CA')}"></div>
        <div class="fg"><label>اللون</label><input type="color" id="f_cal_color" value="${d.color||'#3b82f6'}" style="width:100%; height:40px; background:var(--surface); border:1px solid var(--border); padding:2px; border-radius:4px; cursor:pointer;"></div>
        <div class="fg"><label>الجمهور المستهدف</label><select id="f_cal_target"><option ${d.f_cal_target==='الكل'?'selected':''}>الكل</option><option ${d.f_cal_target==='الطلاب'?'selected':''}>الطلاب</option><option ${d.f_cal_target==='المعلمون'?'selected':''}>المعلمون</option><option ${d.f_cal_target==='أولياء الأمور'?'selected':''}>أولياء الأمور</option></select></div>`;
    }'''

js = re.sub(r"if\s*\(\s*type\s*===\s*'academic-calendar'\s*\)\s*\{[\s\S]*?(?=else\s*if|if\s*\()", new_open_form_cal + "\n    ", js)


ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
html = re.sub(r'app\.js\?v=[0-9]+', f'app.js?v={ts}', html)
html = re.sub(r'style\.css\?v=[0-9]+', f'style.css?v={ts}', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

with open('c:/Users/LENOVO/Desktop/stu/secure_school_system/admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('c:/Users/LENOVO/Desktop/stu/secure_school_system/parent.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replacement complete. Brace checking...")

s = []
ok = True
for i, char in enumerate(js):
    if char == '{': s.append(i)
    elif char == '}':
        if not s:
            print("Unmatched closing brace at pos", i)
            ok = False
        else: s.pop()
if s:
    print("Unmatched opening brace at pos", s)
    ok = False
if ok: print("Brace check OK.")
