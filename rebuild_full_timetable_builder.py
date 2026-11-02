"""
Rebuild Timetable Builder (pg-timetable-builder) HTML and JS Engine completely!
"""
import re, time

print("=" * 60)
print("Rebuilding Timetable Builder (pg-timetable-builder) HTML & JS...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Rebuild pg-timetable-builder HTML container
timetable_html = """
<div class="page" id="pg-timetable-builder">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-days"></i> بناء الجدول الدراسي التفاعلي (Interactive Timetable Builder)</h2>
    </div>

    <!-- Advanced Toolbar & Actions -->
    <div class="toolbar" style="justify-content:space-between; display:flex; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
            <select id="ttbStageFilter" onchange="renderInteractiveTimetable()" style="padding:8px;border-radius:8px;background:var(--surface);border:1px solid var(--border);color:var(--text);">
                <option value="all">جميع الصفوف (الكل)</option>
                <option value="الثالث الثانوي">الثالث الثانوي</option>
                <option value="الثاني الثانوي">الثاني الثانوي</option>
                <option value="التاسع الأساسي">التاسع الأساسي</option>
                <option value="السابع الأساسي">السابع الأساسي</option>
            </select>
            <select id="ttbSectionFilter" onchange="renderInteractiveTimetable()" style="padding:8px;border-radius:8px;background:var(--surface);border:1px solid var(--border);color:var(--text);">
                <option value="all">جميع الشعب (أ، ب، ج)</option>
                <option value="أ">شعبة (أ)</option>
                <option value="ب">شعبة (ب)</option>
                <option value="ج">شعبة (ج)</option>
            </select>

            <!-- View Mode Switcher -->
            <div style="display:flex;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:3px;">
                <button onclick="switchTimetableView('class')" id="btnTtViewClass" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:#3b82f6;color:white;cursor:pointer;"><i class="fa-solid fa-graduation-cap"></i> حسب الفصل</button>
                <button onclick="switchTimetableView('teacher')" id="btnTtViewTeacher" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:transparent;color:var(--text);cursor:pointer;"><i class="fa-solid fa-chalkboard-user"></i> حسب المعلم</button>
                <button onclick="switchTimetableView('room')" id="btnTtViewRoom" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:transparent;color:var(--text);cursor:pointer;"><i class="fa-solid fa-door-open"></i> حسب القاعة</button>
            </div>
        </div>

        <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
            <button class="btn-add" onclick="autoGenerateTimetable()" style="background:linear-gradient(135deg,#8b5cf6,#7c3aed);"><i class="fa-solid fa-wand-magic-sparkles"></i> التوليد الآلي الذكي</button>
            <button class="btn-add" onclick="openTimetableAssign()"><i class="fa-solid fa-plus"></i> إسناد حصة</button>
            <button class="btn-add" onclick="checkTimetableConflicts()" style="background:linear-gradient(135deg,#f59e0b,#d97706);"><i class="fa-solid fa-triangle-exclamation"></i> كشف التعارضات</button>
            <button class="btn-add" onclick="publishTimetable()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-paper-plane"></i> نشر الجدول</button>
            <button class="btn-edit" onclick="undoTimetableAction()" title="تراجع (Undo)"><i class="fa-solid fa-rotate-left"></i></button>
            <button class="btn-edit" onclick="redoTimetableAction()" title="إعادة (Redo)"><i class="fa-solid fa-rotate-right"></i></button>
            <button class="btn-add" onclick="exportTimetable('pdf')" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-file-pdf"></i> تصدير PDF</button>
        </div>
    </div>

    <!-- Color Legend Bar -->
    <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:8px 14px;background:rgba(15,23,42,0.6);border:1px solid var(--border);border-radius:8px;margin-bottom:14px;font-size:0.8rem;">
        <span style="font-weight:700;color:var(--muted);"><i class="fa-solid fa-palette"></i> دليل أنواع الجلسات:</span>
        <span style="display:flex;align-items:center;gap:4px;color:#60a5fa;"><i class="fa-solid fa-circle" style="color:#3b82f6;font-size:0.7rem;"></i> نظري (أزرق)</span>
        <span style="display:flex;align-items:center;gap:4px;color:#c084fc;"><i class="fa-solid fa-circle" style="color:#8b5cf6;font-size:0.7rem;"></i> عملي/مختبر (بنفسجي)</span>
        <span style="display:flex;align-items:center;gap:4px;color:#34d399;"><i class="fa-solid fa-circle" style="color:#10b981;font-size:0.7rem;"></i> رياضي (أخضر)</span>
        <span style="display:flex;align-items:center;gap:4px;color:#fbbf24;"><i class="fa-solid fa-circle" style="color:#f59e0b;font-size:0.7rem;"></i> ثقافي (ذهبي)</span>
        <span style="display:flex;align-items:center;gap:4px;color:#9ca3af;"><i class="fa-solid fa-circle" style="color:#6b7280;font-size:0.7rem;"></i> استراحة (رمادي)</span>
    </div>

    <!-- Main Grid Canvas (2 Columns: 3fr Matrix + 1fr Control Sidebar) -->
    <div style="display:grid;grid-template-columns:3fr 1fr;gap:14px;margin-bottom:20px;">
        
        <!-- Left: Interactive Matrix Grid Canvas -->
        <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:12px;overflow-x:auto;">
            <div id="interactiveTimetableMatrix" style="display:grid;grid-template-columns:110px repeat(5, 1fr);gap:8px;min-width:700px;">
                <!-- Matrix rendered dynamically by JS -->
            </div>
        </div>

        <!-- Right Sidebar Panels -->
        <div style="display:flex;flex-direction:column;gap:12px;">
            
            <!-- Conflict Alerts Panel -->
            <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.4);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#f87171;font-size:0.85rem;display:flex;align-items:center;justify-content:space-between;">
                    <span><i class="fa-solid fa-triangle-exclamation"></i> التنبيهات والتعارضات</span>
                    <span class="badge" style="background:#ef4444;color:white;font-size:0.7rem;" id="ttConflictBadge">0 تعارض</span>
                </h4>
                <div id="conflictAlerts" style="font-size:0.78rem;color:var(--text);max-height:120px;overflow-y:auto;">
                    <!-- Conflict messages -->
                </div>
            </div>

            <!-- Unassigned Subjects Pool -->
            <div style="background:rgba(15,23,42,0.7);border:1px solid var(--border);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#60a5fa;font-size:0.85rem;"><i class="fa-solid fa-boxes-packing"></i> مواد غير مسكنة (سحب وإفلات)</h4>
                <div id="ttUnassignedPool" style="display:flex;flex-direction:column;gap:6px;max-height:140px;overflow-y:auto;">
                    <!-- Draggable subject cards -->
                </div>
            </div>

            <!-- Teacher Workload Progress -->
            <div style="background:rgba(15,23,42,0.7);border:1px solid var(--border);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#34d399;font-size:0.85rem;"><i class="fa-solid fa-user-clock"></i> نصاب وحمولات المعلمين</h4>
                <div id="teacherLoadList" style="display:flex;flex-direction:column;gap:6px;max-height:130px;overflow-y:auto;">
                    <!-- Teacher load bars -->
                </div>
            </div>

            <!-- Room Capacity Panel -->
            <div style="background:rgba(15,23,42,0.7);border:1px solid var(--border);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#fbbf24;font-size:0.85rem;"><i class="fa-solid fa-door-closed"></i> إشغال القاعات والمعامل</h4>
                <div id="roomCapacityList" style="display:flex;flex-direction:column;gap:4px;max-height:120px;overflow-y:auto;">
                    <!-- Room usage status -->
                </div>
            </div>

        </div>

    </div>

    <!-- Detailed Timetable Table Grid -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>الفصل / الترم</th>
                    <th>الصف والشعبة</th>
                    <th>اليوم والحصة</th>
                    <th>المادة الدراسية</th>
                    <th>المعلم المسؤول</th>
                    <th>القاعة / المكان</th>
                    <th>نصاب المعلم</th>
                    <th>حالة التعارض</th>
                    <th>نوع الجلسة</th>
                    <th>حالة النشر</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-schedule-grid"></tbody>
        </table>
    </div>
</div>

<!-- Timetable Assignment Dedicated Modal Overlay -->
<div class="modal-overlay" id="timetableAssignModal">
    <div class="modal-content glass-panel" style="max-width:550px;">
        <div class="modal-header">
            <h3><i class="fa-solid fa-calendar-plus" style="color:#3b82f6;"></i> إسناد مادة وتحديد موعد حصة دراسية</h3>
            <div class="window-controls"><button class="btn-close" onclick="closeModal('timetableAssignModal')"><i class="fa-solid fa-xmark"></i></button></div>
        </div>
        <div class="modal-body" style="padding:16px;">
            <input type="hidden" id="tta_edit_id">
            <div class="fg"><label>الصف والشعبة <span class="req">*</span></label><select id="tta_grade_sec"><option>الثالث الثانوي - شعبة (أ)</option><option>الثاني الثانوي - شعبة (ب)</option><option>التاسع الأساسي - شعبة (أ)</option><option>السابع الأساسي - شعبة (أ)</option></select></div>
            <div class="fg"><label>اليوم الدراسي <span class="req">*</span></label><select id="tta_day"><option value="السبت">السبت</option><option value="الأحد">الأحد</option><option value="الاثنين">الاثنين</option><option value="الثلاثاء">الثلاثاء</option><option value="الأربعاء">الأربعاء</option></select></div>
            <div class="fg"><label>رقم الحصة التوقيت <span class="req">*</span></label><select id="tta_period_idx"><option value="0">الحصة 1 (07:30 - 08:15)</option><option value="1">الحصة 2 (08:20 - 09:05)</option><option value="2">الحصة 3 (09:10 - 09:55)</option><option value="4">الحصة 4 (10:25 - 11:10)</option><option value="5">الحصة 5 (11:15 - 12:00)</option><option value="6">الحصة 6 (12:05 - 12:50)</option></select></div>
            <div class="fg"><label>المادة الدراسية <span class="req">*</span></label><input id="tta_subject" placeholder="مثال: الرياضيات المتقدمة" value="الرياضيات المتقدمة" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>المعلم المسؤول <span class="req">*</span></label><select id="tta_teacher"><option>أ. خالد محمود العنسي</option><option>أ. إبراهيم العنسي</option><option>د. عبدالملك الشامي</option><option>أ. سارة أحمد</option></select></div>
            <div class="fg"><label>القاعة / المكان <span class="req">*</span></label><select id="tta_room"><option>الفصل 3/أ</option><option>معمل الكمبيوتر (01)</option><option>مختبر العلوم الرئيسي</option><option>القاعة الكبرى</option><option>الملعب الرياضي</option></select></div>
            <div class="fg"><label>نوع الجلسة <span class="req">*</span></label><select id="tta_session_type"><option value="نظري">نظري (أزرق)</option><option value="عملي مختبر">عملي / مختبر (بنفسجي)</option><option value="رياضي">رياضي (أخضر)</option><option value="ثقافي">ثقافي (ذهبي)</option></select></div>
            <div id="ttaConflictWarning" style="display:none;background:rgba(239,68,68,0.15);border:1px solid #ef4444;border-radius:6px;padding:8px;margin-top:10px;color:#ef4444;font-size:0.8rem;"></div>
            <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px;">
                <button class="btn-save" onclick="saveTimetableSlot()"><i class="fa-solid fa-floppy-disk"></i> حفظ الحصة</button>
                <button class="btn-cancel" onclick="closeModal('timetableAssignModal')"><i class="fa-solid fa-xmark"></i> إلغاء</button>
            </div>
        </div>
    </div>
</div>
"""

pattern_tt_page = r'<div class="page" id="pg-timetable-builder">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
html = re.sub(pattern_tt_page, timetable_html.strip() + '\n', html, flags=re.DOTALL)

print("  ✓ Rebuilt pg-timetable-builder HTML & added dedicated assignment modal")

# Update cache timestamps in HTML
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

print("Updated HTML files with new timetable structure!")
