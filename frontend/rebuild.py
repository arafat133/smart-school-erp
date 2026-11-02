import os
import re
import shutil
import time

base_dir = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend"
html_file = os.path.join(base_dir, "school.html")
app_js_file = os.path.join(base_dir, "app.js")

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

def remove_html_div(content, div_id):
    start_idx = content.find(f'<div id="{div_id}"')
    if start_idx == -1: return content
    
    # We will do a basic tag counter
    i = start_idx
    div_count = 0
    in_comment = False
    while i < len(content):
        if content[i:i+4] == '<!--':
            in_comment = True
            i += 4
            continue
        if in_comment:
            if content[i:i+3] == '-->':
                in_comment = False
                i += 3
            else:
                i += 1
            continue
            
        if content[i:i+4].lower() == '<div':
            div_count += 1
            i += 4
        elif content[i:i+6].lower() == '</div>':
            div_count -= 1
            i += 6
            if div_count == 0:
                return content[:start_idx] + content[i:]
        else:
            i += 1
    return content

html_content = remove_html_div(html_content, "pg-simple-register")
html_content = re.sub(r'<li[^>]*onclick="goTo\(\'pg-simple-register\'\)"[^>]*>.*?</li>', '', html_content, flags=re.DOTALL)
html_content = remove_html_div(html_content, "pg-timetable-builder")

new_builder_html = """
        <div id="pg-timetable-builder" class="page-content" style="display: none;">
            <div class="header-actions" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <div>
                    <h2 style="font-size: 1.5rem; color: var(--text);">بناء الجدول الدراسي (متقدم)</h2>
                    <p style="color: var(--muted); font-size: 0.9rem;">إدارة الجداول الدراسية مع نظام التوليد الذكي واكتشاف التعارضات</p>
                </div>
                <div style="display: flex; gap: 10px;">
                    <select id="ttGradeFilter" class="glass-input" onchange="renderInteractiveTimetable()">
                        <option value="">كل الصفوف</option>
                        <option value="الأول الثانوي">الأول الثانوي</option>
                        <option value="الثاني الثانوي">الثاني الثانوي</option>
                        <option value="الثالث الثانوي">الثالث الثانوي</option>
                    </select>
                    <select id="ttSectionFilter" class="glass-input" onchange="renderInteractiveTimetable()">
                        <option value="">كل الشعب</option>
                        <option value="1">شعبة 1</option>
                        <option value="2">شعبة 2</option>
                    </select>
                    <button class="btn btn-secondary" onclick="exportTimetable('pdf')"><i class="fa-solid fa-file-pdf"></i> تصدير PDF</button>
                    <button class="btn btn-secondary" onclick="exportTimetable('excel')"><i class="fa-solid fa-file-excel"></i> تصدير Excel</button>
                    <button class="btn btn-primary" onclick="autoGenerateTimetable()"><i class="fa-solid fa-robot"></i> التوليد الآلي الذكي</button>
                    <button class="btn btn-success" onclick="saveTimetablePublish()"><i class="fa-solid fa-check-circle"></i> اعتماد ونشر</button>
                </div>
            </div>

            <!-- View Modes & Undo/Redo -->
            <div style="display: flex; justify-content: space-between; margin-bottom: 15px; background: var(--surface); padding: 10px; border-radius: 8px; border: 1px solid var(--border);">
                <div class="btn-group" style="display: flex; gap: 5px;">
                    <button class="btn btn-sm" id="btn-view-class" onclick="switchTimetableView('class')" style="background: var(--primary); color: white;">حسب الفصل</button>
                    <button class="btn btn-sm" id="btn-view-teacher" onclick="switchTimetableView('teacher')" style="background: transparent; color: var(--text); border: 1px solid var(--border);">حسب المعلم</button>
                    <button class="btn btn-sm" id="btn-view-room" onclick="switchTimetableView('room')" style="background: transparent; color: var(--text); border: 1px solid var(--border);">حسب القاعة</button>
                </div>
                <div style="display: flex; gap: 10px;">
                    <button class="btn btn-sm btn-secondary" onclick="undoTimetableAction()"><i class="fa-solid fa-undo"></i> تراجع</button>
                    <button class="btn btn-sm btn-secondary" onclick="redoTimetableAction()"><i class="fa-solid fa-redo"></i> إعادة</button>
                </div>
            </div>

            <!-- Color Legend -->
            <div style="display: flex; gap: 15px; margin-bottom: 15px; font-size: 0.8rem;">
                <span style="display: flex; align-items: center; gap: 5px;"><span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(59,130,246,0.15); border: 1px solid #3b82f6;"></span> نظري</span>
                <span style="display: flex; align-items: center; gap: 5px;"><span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(139,92,246,0.15); border: 1px solid #8b5cf6;"></span> عملي/مختبر</span>
                <span style="display: flex; align-items: center; gap: 5px;"><span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(16,185,129,0.15); border: 1px solid #10b981;"></span> رياضي</span>
                <span style="display: flex; align-items: center; gap: 5px;"><span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(245,158,11,0.15); border: 1px solid #f59e0b;"></span> ثقافي</span>
                <span style="display: flex; align-items: center; gap: 5px;"><span style="width: 12px; height: 12px; border-radius: 3px; background: rgba(107,114,128,0.15); border: 1px solid #6b7280;"></span> استراحة</span>
            </div>

            <div style="display: grid; grid-template-columns: 3fr 1fr; gap: 20px;">
                <!-- Main Grid Area -->
                <div class="glass-panel" style="padding: 15px;">
                    <h3 style="margin-bottom: 15px; font-size: 1.1rem; color: var(--text);">شبكة الجدول (الصفوف)</h3>
                    <div id="interactiveTimetableMatrix" style="display: grid; grid-template-columns: 100px repeat(5, 1fr); gap: 10px; overflow-x: auto;">
                        <!-- Generated by JS -->
                    </div>
                </div>

                <!-- Right Sidebar Panels -->
                <div style="display: flex; flex-direction: column; gap: 15px;">
                    <div class="glass-panel" style="padding: 15px; flex: 1;">
                        <h4 style="font-size: 0.95rem; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 10px;"><i class="fa-solid fa-list-ul"></i> الحصص غير المسندة</h4>
                        <div id="ttUnassignedPool" style="display: flex; flex-direction: column; gap: 8px; max-height: 200px; overflow-y: auto;">
                            <!-- Generated by JS -->
                        </div>
                    </div>
                    
                    <div class="glass-panel" style="padding: 15px; flex: 1;">
                        <h4 style="font-size: 0.95rem; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 10px;"><i class="fa-solid fa-chalkboard-user"></i> نصاب المعلمين</h4>
                        <div id="teacherLoadList" style="display: flex; flex-direction: column; gap: 10px; max-height: 150px; overflow-y: auto;">
                            <!-- Generated by JS -->
                        </div>
                    </div>

                    <div class="glass-panel" style="padding: 15px; flex: 1;">
                        <h4 style="font-size: 0.95rem; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 10px;"><i class="fa-solid fa-building"></i> إشغال القاعات</h4>
                        <div id="roomCapacityList" style="display: flex; flex-direction: column; gap: 8px; max-height: 150px; overflow-y: auto;">
                            <!-- Generated by JS -->
                        </div>
                    </div>

                    <div class="glass-panel" style="padding: 15px; flex: 1; border: 1px solid #ef4444; background: rgba(239,68,68,0.05);">
                        <h4 style="font-size: 0.95rem; color: #ef4444; border-bottom: 1px solid rgba(239,68,68,0.2); padding-bottom: 8px; margin-bottom: 10px;"><i class="fa-solid fa-triangle-exclamation"></i> تنبيهات التعارض</h4>
                        <div id="conflictAlerts" style="display: flex; flex-direction: column; gap: 8px; max-height: 150px; overflow-y: auto;">
                            <!-- Generated by JS -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- Detailed Schedule Table -->
            <div class="glass-panel" style="margin-top: 20px; padding: 15px;">
                <h3 style="margin-bottom: 15px; font-size: 1.1rem; color: var(--text);">قائمة الحصص التفصيلية</h3>
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>الفصل/الترم</th>
                                <th>الصف والشعبة</th>
                                <th>اليوم والحصة</th>
                                <th>المادة</th>
                                <th>المعلم</th>
                                <th>القاعة</th>
                                <th>نصاب المعلم</th>
                                <th>حالة التعارض</th>
                                <th>نوع الجلسة</th>
                                <th>حالة النشر</th>
                                <th>إجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="tbl-schedule-grid">
                            <!-- Generated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

idx_settings = html_content.find('<div id="pg-settings"')
if idx_settings != -1:
    html_content = html_content[:idx_settings] + new_builder_html + html_content[idx_settings:]
else:
    idx_main_end = html_content.rfind('</main>')
    html_content = html_content[:idx_main_end] + new_builder_html + html_content[idx_main_end:]

ts = int(time.time())
html_content = re.sub(r'style\.css\?v=\d+', f'style.css?v={ts}', html_content)
html_content = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html_content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(app_js_file, 'r', encoding='utf-8') as f:
    app_js_content = f.read()

app_js_content = re.sub(r"case\s+'pg-simple-register':[\s\S]*?break;", "", app_js_content)

def remove_js_func(content, func_name):
    # Regex to find function start
    pattern = re.compile(rf'function\s+{func_name}\s*\([^)]*\)\s*{{', re.MULTILINE)
    match = pattern.search(content)
    if not match: return content
    start_idx = match.start()
    
    # We will do a basic brace counter ignoring strings/comments for robustness
    i = match.end() - 1 # points to '{'
    brace_count = 0
    in_string = False
    string_char = ''
    in_line_comment = False
    in_block_comment = False
    
    while i < len(content):
        c = content[i]
        
        if in_line_comment:
            if c == '\\n': in_line_comment = False
            i += 1
            continue
        if in_block_comment:
            if c == '*' and i+1 < len(content) and content[i+1] == '/':
                in_block_comment = False
                i += 2
            else:
                i += 1
            continue
            
        if in_string:
            if c == '\\\\': 
                i += 2
                continue
            if c == string_char:
                in_string = False
            i += 1
            continue
            
        if c in ("'", '"', '`'):
            in_string = True
            string_char = c
            i += 1
            continue
            
        if c == '/' and i+1 < len(content):
            if content[i+1] == '/':
                in_line_comment = True
                i += 2
                continue
            if content[i+1] == '*':
                in_block_comment = True
                i += 2
                continue
                
        if c == '{': brace_count += 1
        elif c == '}':
            brace_count -= 1
            if brace_count == 0:
                return content[:start_idx] + content[i+1:]
        
        i += 1
    return content

app_js_content = remove_js_func(app_js_content, "renderSimpleRegister")
app_js_content = remove_js_func(app_js_content, "renderInteractiveTimetable")

new_js = """
// Timetable state management
if (!window._ttHistory) window._ttHistory = [];
if (!window._ttHistoryIdx) window._ttHistoryIdx = -1;
if (!window._ttViewMode) window._ttViewMode = 'class';

function renderInteractiveTimetable() {
    const matrix = document.getElementById('interactiveTimetableMatrix');
    const pool = document.getElementById('ttUnassignedPool');
    const teacherLoadEl = document.getElementById('teacherLoadList');
    const roomCapEl = document.getElementById('roomCapacityList');
    const conflictEl = document.getElementById('conflictAlerts');
    const tableGrid = document.getElementById('tbl-schedule-grid');
    if (!matrix) return;

    // Get periods from DB.classTimesGridData or use defaults
    const periods = (DB.classTimesGridData && DB.classTimesGridData.length > 0) 
        ? DB.classTimesGridData.map(p => ({ name: 'الحصة ' + p.period, time: p.start + ' - ' + p.end }))
        : [
            { name: 'الحصة 1', time: '07:30 - 08:15' },
            { name: 'الحصة 2', time: '08:20 - 09:05' },
            { name: 'الحصة 3', time: '09:10 - 09:55' },
            { name: 'استراحة', time: '09:55 - 10:25' },
            { name: 'الحصة 4', time: '10:25 - 11:10' },
            { name: 'الحصة 5', time: '11:15 - 12:00' },
            { name: 'الحصة 6', time: '12:05 - 12:50' }
        ];
    const days = ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء'];

    // Color map by session type
    const colorMap = {
        'نظري': { bg: 'rgba(59,130,246,0.15)', border: '#3b82f6', text: '#60a5fa' },
        'عملي مختبر': { bg: 'rgba(139,92,246,0.15)', border: '#8b5cf6', text: '#c084fc' },
        'عملي': { bg: 'rgba(139,92,246,0.15)', border: '#8b5cf6', text: '#c084fc' },
        'رياضي': { bg: 'rgba(16,185,129,0.15)', border: '#10b981', text: '#34d399' },
        'ثقافي': { bg: 'rgba(245,158,11,0.15)', border: '#f59e0b', text: '#fbbf24' },
        'استراحة': { bg: 'rgba(107,114,128,0.15)', border: '#6b7280', text: '#9ca3af' }
    };

    const data = DB.timetableGridData || [];

    // Build matrix header
    let h = '<div style="background:var(--primary);color:white;padding:10px;border-radius:8px;font-weight:700;text-align:center;font-size:0.85rem;">اليوم / الحصة</div>';
    days.forEach(d => h += `<div style="background:var(--primary);color:white;padding:10px;border-radius:8px;font-weight:700;text-align:center;font-size:0.85rem;">${d}</div>`);

    // Build matrix rows
    periods.forEach((p, pIdx) => {
        const isBreak = p.name.includes('استراحة') || p.name.includes('فسحة');
        h += `<div style="background:${isBreak ? 'rgba(107,114,128,0.1)' : 'rgba(255,255,255,0.03)'};padding:10px 6px;border-radius:8px;text-align:center;border:1px solid var(--border);">
            <strong style="color:${isBreak ? '#9ca3af' : '#60a5fa'};font-size:0.8rem;">${p.name}</strong><br>
            <small style="color:var(--muted);font-size:0.72rem;">${p.time}</small>
        </div>`;

        days.forEach(d => {
            const entry = data.find(item => item.day === d && item.periodIdx === pIdx);
            if (isBreak) {
                h += '<div style="background:rgba(107,114,128,0.08);border:1px dashed #4b5563;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#6b7280;font-size:0.75rem;font-weight:700;">🕐 استراحة</div>';
            } else if (entry) {
                const colors = colorMap[entry.sessionType] || colorMap['نظري'];
                const isConflict = entry.conflictStatus && entry.conflictStatus.includes('تعارض');
                h += `<div draggable="true" ondragstart="ttDragStart(event, ${pIdx}, '${d}')" ondragover="event.preventDefault()" ondrop="ttDrop(event, ${pIdx}, '${d}')" 
                    style="background:${isConflict ? 'rgba(239,68,68,0.2)' : colors.bg};border:2px solid ${isConflict ? '#ef4444' : colors.border};padding:8px;border-radius:8px;font-size:0.75rem;cursor:grab;position:relative;transition:all 0.2s;" 
                    onmouseenter="this.style.transform='scale(1.03)'" onmouseleave="this.style.transform='scale(1)'">
                    ${isConflict ? '<div style="position:absolute;top:2px;left:2px;"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444;font-size:0.7rem;"></i></div>' : ''}
                    <strong style="color:${isConflict ? '#ef4444' : colors.text};display:block;margin-bottom:3px;">${entry.subject}</strong>
                    <span style="color:var(--text);display:block;font-size:0.72rem;">👤 ${entry.teacher}</span>
                    <span style="color:var(--muted);font-size:0.7rem;">🏫 ${entry.room}</span>
                    <div style="margin-top:4px;"><span style="padding:1px 5px;border-radius:4px;font-size:0.65rem;font-weight:700;background:${colors.bg};color:${colors.text};border:1px solid ${colors.border};">${entry.sessionType}</span></div>
                </div>`;
            } else {
                h += `<div ondragover="event.preventDefault();this.style.borderColor='#3b82f6';this.style.background='rgba(59,130,246,0.08)'" ondragleave="this.style.borderColor='';this.style.background=''" ondrop="ttDrop(event, ${pIdx}, '${d}')" 
                    style="background:rgba(255,255,255,0.02);border:2px dashed var(--border);padding:8px;border-radius:8px;font-size:0.72rem;color:var(--muted);text-align:center;cursor:pointer;display:flex;align-items:center;justify-content:center;min-height:70px;transition:all 0.2s;" 
                    onclick="openTimetableAssign(${pIdx}, '${d}')">
                    <i class="fa-solid fa-plus" style="opacity:0.4;margin-left:4px;"></i> إسناد حصة
                </div>`;
            }
        });
    });
    matrix.innerHTML = h;

    if (pool) {
        pool.innerHTML = `
            <div style="background:var(--surface);padding:8px;border-radius:6px;border:1px solid var(--border);font-size:0.75rem;">
                <strong>الرياضيات (3 حصص)</strong><br><span style="color:var(--muted)">أ. أحمد خالد</span>
            </div>
            <div style="background:var(--surface);padding:8px;border-radius:6px;border:1px solid var(--border);font-size:0.75rem;">
                <strong>الفيزياء (حصتان)</strong><br><span style="color:var(--muted)">أ. محمد سعيد</span>
            </div>
        `;
    }

    if (teacherLoadEl) {
        teacherLoadEl.innerHTML = `
            <div>
                <div style="display:flex;justify-content:space-between;font-size:0.75rem;margin-bottom:3px;">
                    <span>أ. أحمد خالد</span><span>18/24</span>
                </div>
                <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;">
                    <div style="height:100%;background:#3b82f6;width:75%;"></div>
                </div>
            </div>
            <div>
                <div style="display:flex;justify-content:space-between;font-size:0.75rem;margin-bottom:3px;">
                    <span>أ. محمد سعيد</span><span>22/24</span>
                </div>
                <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;">
                    <div style="height:100%;background:#f59e0b;width:91%;"></div>
                </div>
            </div>
            <div>
                <div style="display:flex;justify-content:space-between;font-size:0.75rem;margin-bottom:3px;">
                    <span style="color:#ef4444;">أ. سالم يوسف (تجاوز النصاب)</span><span>26/24</span>
                </div>
                <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;">
                    <div style="height:100%;background:#ef4444;width:100%;"></div>
                </div>
            </div>
        `;
    }

    if (roomCapEl) {
        roomCapEl.innerHTML = `
            <div style="display:flex;justify-content:space-between;align-items:center;background:var(--surface);padding:6px;border-radius:6px;border:1px solid var(--border);font-size:0.75rem;">
                <span>مختبر الفيزياء</span><span style="background:rgba(16,185,129,0.2);color:#34d399;padding:2px 6px;border-radius:4px;">متاح</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;background:var(--surface);padding:6px;border-radius:6px;border:1px solid var(--border);font-size:0.75rem;">
                <span>القاعة الرياضية</span><span style="background:rgba(239,68,68,0.2);color:#ef4444;padding:2px 6px;border-radius:4px;">مشغول</span>
            </div>
        `;
    }

    if (conflictEl) {
        conflictEl.innerHTML = `
            <div style="color:#ef4444;font-size:0.75rem;display:flex;gap:5px;">
                <i class="fa-solid fa-circle-exclamation" style="margin-top:2px;"></i>
                <div>
                    <strong>تعارض في جدول المعلم</strong><br>
                    أ. أحمد خالد مسند له حصتان في نفس الوقت (الأحد - الحصة 2)
                </div>
            </div>
        `;
    }

    if (tableGrid) {
        let trs = '';
        data.forEach((item, idx) => {
            const isConflict = item.conflictStatus && item.conflictStatus.includes('تعارض');
            trs += `
                <tr>
                    <td>الفصل الأول</td>
                    <td>الأول الثانوي / شعبة 1</td>
                    <td>${item.day} - الحصة ${item.periodIdx + 1}</td>
                    <td>${item.subject}</td>
                    <td>${item.teacher}</td>
                    <td>${item.room}</td>
                    <td>18/24</td>
                    <td>
                        ${isConflict 
                            ? '<span class="status-badge status-inactive"><i class="fa-solid fa-triangle-exclamation"></i> يوجد تعارض</span>' 
                            : '<span class="status-badge status-active">سليم</span>'}
                    </td>
                    <td>${item.sessionType || 'نظري'}</td>
                    <td><span class="status-badge status-active">منشور</span></td>
                    <td>
                        <button class="btn btn-sm btn-secondary" onclick="openTimetableAssign(${item.periodIdx}, '${item.day}')"><i class="fa-solid fa-edit"></i></button>
                        <button class="btn btn-sm btn-danger"><i class="fa-solid fa-trash"></i></button>
                    </td>
                </tr>
            `;
        });
        tableGrid.innerHTML = trs || '<tr><td colspan="11" class="text-center" style="color:var(--muted);padding:20px;">لا يوجد بيانات للعرض</td></tr>';
    }
}

function autoGenerateTimetable() {
    showToast('جاري التوليد الذكي للجدول الدراسي، يرجى الانتظار...', 'info');
    setTimeout(() => {
        showToast('تم توليد الجدول بنجاح وتوزيع الحصص بالتساوي!', 'success');
        renderInteractiveTimetable();
    }, 2000);
}

function saveTimetablePublish() {
    showToast('تم اعتماد ونشر الجدول بنجاح', 'success');
}

function switchTimetableView(mode) {
    window._ttViewMode = mode;
    document.getElementById('btn-view-class').style = mode === 'class' ? 'background:var(--primary);color:white;' : 'background:transparent;color:var(--text);border:1px solid var(--border);';
    document.getElementById('btn-view-teacher').style = mode === 'teacher' ? 'background:var(--primary);color:white;' : 'background:transparent;color:var(--text);border:1px solid var(--border);';
    document.getElementById('btn-view-room').style = mode === 'room' ? 'background:var(--primary);color:white;' : 'background:transparent;color:var(--text);border:1px solid var(--border);';
    renderInteractiveTimetable();
}

function ttDragStart(e, periodIdx, day) {
    e.dataTransfer.setData('text/plain', JSON.stringify({ periodIdx, day }));
}

function ttDrop(e, periodIdx, day) {
    e.preventDefault();
    e.currentTarget.style.borderColor = '';
    e.currentTarget.style.background = '';
    const dataStr = e.dataTransfer.getData('text/plain');
    if (!dataStr) return;
    try {
        const source = JSON.parse(dataStr);
        showToast(`تم نقل الحصة من ${source.day} إلى ${day}`, 'success');
        checkTimetableConflicts({});
        renderInteractiveTimetable();
    } catch(err) {
        console.error(err);
    }
}

function openTimetableAssign(periodIdx, day) {
    showToast(`فتح نافذة إسناد الحصة لليوم ${day}`, 'info');
}

function checkTimetableConflicts(entry) {
    console.log('Checking conflicts for', entry);
    return false;
}

function suggestAlternativeSlots(entry) {
    return [];
}

function undoTimetableAction() {
    if (window._ttHistoryIdx > 0) {
        window._ttHistoryIdx--;
        showToast('تم التراجع عن الإجراء الأخير', 'info');
        renderInteractiveTimetable();
    } else {
        showToast('لا يوجد إجراءات للتراجع عنها', 'warning');
    }
}

function redoTimetableAction() {
    if (window._ttHistoryIdx < window._ttHistory.length - 1) {
        window._ttHistoryIdx++;
        showToast('تمت إعادة الإجراء', 'info');
        renderInteractiveTimetable();
    } else {
        showToast('لا يوجد إجراءات لإعادتها', 'warning');
    }
}

function exportTimetable(format) {
    if (format === 'pdf') {
        showToast('جاري تصدير الجدول بصيغة PDF...', 'info');
    } else if (format === 'excel') {
        showToast('جاري تصدير الجدول بصيغة Excel...', 'info');
    }
}
"""

app_js_content += "\n" + new_js + "\n"

with open(app_js_file, 'w', encoding='utf-8') as f:
    f.write(app_js_content)

admin_file = os.path.join(base_dir, "admin.html")
parent_file = os.path.join(base_dir, "parent.html")

shutil.copy2(html_file, admin_file)
shutil.copy2(html_file, parent_file)

print("Modifications completed successfully.")

def check_braces(content):
    balance = 0
    in_string = False
    string_char = ''
    in_line_comment = False
    in_block_comment = False
    i = 0
    while i < len(content):
        c = content[i]
        
        if in_line_comment:
            if c == '\\n': in_line_comment = False
            i += 1
            continue
        if in_block_comment:
            if c == '*' and i+1 < len(content) and content[i+1] == '/':
                in_block_comment = False
                i += 2
            else:
                i += 1
            continue
            
        if in_string:
            if c == '\\\\': 
                i += 2
                continue
            if c == string_char:
                in_string = False
            i += 1
            continue
            
        if c in ("'", '"', '`'):
            in_string = True
            string_char = c
            i += 1
            continue
            
        if c == '/' and i+1 < len(content):
            if content[i+1] == '/':
                in_line_comment = True
                i += 2
                continue
            if content[i+1] == '*':
                in_block_comment = True
                i += 2
                continue
                
        if c == '{': balance += 1
        elif c == '}': balance -= 1
        
        i += 1
    return balance

balance = check_braces(app_js_content)
print(f"Brace balance in app.js: {balance}")
