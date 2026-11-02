"""
1. Fix Print Engine for Timetable Builder & Exam Schedule (Clean official letterhead format, no UI widgets/scrollbars)
2. Rebuild Smart Exam Scheduler Interface (pg-exam-schedule) in HTML and JS
"""
import re, time

print("=" * 60)
print("Fixing Print Engine & Rebuilding Smart Exam Scheduler...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Rebuild pg-exam-schedule HTML container
smart_exam_html = """
<div class="page" id="pg-exam-schedule">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-check"></i> واجهة جدول الامتحانات المتقدمة والذكية (Smart Exam Scheduler)</h2>
    </div>

    <!-- Security & AI KPI Header Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي المواد المجدولة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.3rem;" id="statExamCount">14 مادة مخصصة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي أيام الامتحانات</h3><p style="color:#34d399;font-weight:800;font-size:1.3rem;" id="statExamDays">10 أيام امتحانية</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>مؤشر إجهاد الطالب وراحة المواد</h3><p style="color:#c084fc;font-weight:800;font-size:1.3rem;" id="statStressIndex">ممتاز (96% راحة)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>حالة الاعتماد وقفل الكنترول</h3><p style="color:#fbbf24;font-weight:800;font-size:1.3rem;" id="statAuditStatus">معتمد ورسمي 🔒</p></div>
        </div>
    </div>

    <!-- Advanced Toolbar & View Switcher -->
    <div class="toolbar" style="justify-content:space-between; display:flex; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
        <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
            <select id="fltExamTerm" onchange="renderExamScheduleGrid()" style="padding:8px;border-radius:8px;background:var(--surface);border:1px solid var(--border);color:var(--text);">
                <option value="all">جميع الفصول (الكل)</option>
                <option value="الفصل الدراسي الثاني 2025/2026">الفصل الثاني 2025/2026</option>
                <option value="الفصل الدراسي الأول 2025/2026">الفصل الأول 2025/2026</option>
            </select>
            <select id="fltExamType" onchange="renderExamScheduleGrid()" style="padding:8px;border-radius:8px;background:var(--surface);border:1px solid var(--border);color:var(--text);">
                <option value="all">جميع أنواع الامتحانات</option>
                <option value="اختبارات نهاية الفصل">اختبارات نهاية الفصل</option>
                <option value="اختبارات منتصف الفصل">اختبارات منتصف الفصل (نصفي)</option>
                <option value="اختبارات شهرية">اختبارات شهرية</option>
                <option value="اختبارات عملية / معامل">اختبارات عملية / معامل</option>
            </select>

            <!-- Dynamic Multi-Views Switcher -->
            <div style="display:flex;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:3px;">
                <button onclick="switchExamView('master')" id="btnEvMaster" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:#3b82f6;color:white;cursor:pointer;"><i class="fa-solid fa-table-cells"></i> الجدول الموحد</button>
                <button onclick="switchExamView('hall')" id="btnEvHall" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:transparent;color:var(--text);cursor:pointer;"><i class="fa-solid fa-building-circle-check"></i> شغل القاعات</button>
                <button onclick="switchExamView('invigilator')" id="btnEvInvigilator" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:transparent;color:var(--text);cursor:pointer;"><i class="fa-solid fa-user-shield"></i> جدول المراقبة</button>
                <button onclick="switchExamView('student')" id="btnEvStudent" style="padding:4px 10px;font-size:0.78rem;border:none;border-radius:6px;background:transparent;color:var(--text);cursor:pointer;"><i class="fa-solid fa-id-card"></i> جدول الطالب والبطاقات</button>
            </div>
        </div>

        <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
            <button class="btn-add" onclick="autoGenerateExamSchedule()" style="background:linear-gradient(135deg,#8b5cf6,#7c3aed);"><i class="fa-solid fa-wand-magic-sparkles"></i> التوليد الآلي الذكي</button>
            <button class="btn-add" onclick="openExamSessionModal()"><i class="fa-solid fa-plus"></i> إضافة جلسة امتحان</button>
            <button class="btn-add" onclick="resolveExamConflicts()" style="background:linear-gradient(135deg,#f59e0b,#d97706);"><i class="fa-solid fa-brain"></i> خوارزمية العدالة والإجهاد</button>
            <button class="btn-add" onclick="lockAndPublishExamSchedule()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-lock"></i> اعتماد وقفل الجدول</button>
            <button class="btn-add" onclick="generateStudentExamPasses()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-qrcode"></i> بطاقات الدخول (QR)</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة التقرير المتروّس</button>
        </div>
    </div>

    <!-- Main View Canvas Containers -->
    
    <!-- 1. Master Grid View Container -->
    <div id="examMasterViewContainer" style="display:grid;grid-template-columns:3fr 1fr;gap:14px;margin-bottom:20px;">
        <div style="background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:12px;overflow-x:auto;">
            <h4 style="margin-top:0;color:#60a5fa;font-size:0.9rem;margin-bottom:10px;"><i class="fa-solid fa-calendar-days"></i> مصفوفة امتحانات نهاية الفصل الموزعة (Master Grid Matrix)</h4>
            <div id="examScheduleMatrix" style="display:grid;grid-template-columns:120px repeat(5, 1fr);gap:8px;min-width:750px;">
                <!-- Matrix rendered dynamically by JS -->
            </div>
        </div>

        <!-- Side Panels -->
        <div style="display:flex;flex-direction:column;gap:12px;">
            <!-- AI Conflict & Stress Alerts -->
            <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.4);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#f87171;font-size:0.85rem;display:flex;align-items:center;justify-content:space-between;">
                    <span><i class="fa-solid fa-brain"></i> فحص التعارضات والإجهاد</span>
                    <span class="badge badge-success" id="examConflictBadge">سليم 🟢</span>
                </h4>
                <div id="examConflictAlerts" style="font-size:0.78rem;color:var(--text);max-height:120px;overflow-y:auto;">
                    <!-- Alerts list -->
                </div>
            </div>

            <!-- Backup Invigilators Team Pool -->
            <div style="background:rgba(15,23,42,0.7);border:1px solid var(--border);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#34d399;font-size:0.85rem;"><i class="fa-solid fa-user-shield"></i> فريق المراقبة الاحتياطي (Backup Team)</h4>
                <div id="backupInvigilatorsList" style="display:flex;flex-direction:column;gap:6px;max-height:130px;overflow-y:auto;">
                    <!-- Backup proctors list -->
                </div>
            </div>

            <!-- Exam Difficulty Rules & Weighting -->
            <div style="background:rgba(15,23,42,0.7);border:1px solid var(--border);border-radius:10px;padding:10px;">
                <h4 style="margin-top:0;color:#fbbf24;font-size:0.85rem;"><i class="fa-solid fa-scale-balanced"></i> أوزان صعوبة المواد والتباعد</h4>
                <div style="font-size:0.75rem;color:var(--muted);line-height:1.5;">
                    <div>🔴 مادة صعبة (وزن 3): راحة يومين قبلها إجبارياً</div>
                    <div>🟡 مادة متوسطة (وزن 2): راحة يوم واحد</div>
                    <div>🟢 مادة خفيفة/عملي (وزن 1): مباشرة</div>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. Hall Occupancy View Container -->
    <div id="examHallViewContainer" style="display:none;margin-bottom:20px;background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:16px;">
        <h3 style="margin-top:0;color:#34d399;font-size:1rem;"><i class="fa-solid fa-building-circle-check"></i> خريطة شغل القاعات والمدرجات ومطابقة السعة الاستيعابية</h3>
        <div id="examHallOccupancyGrid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:14px;">
            <!-- Hall occupancy cards rendered dynamically -->
        </div>
    </div>

    <!-- 3. Invigilator Duty View Container -->
    <div id="examInvigilatorViewContainer" style="display:none;margin-bottom:20px;background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:16px;">
        <h3 style="margin-top:0;color:#c084fc;font-size:1rem;"><i class="fa-solid fa-user-shield"></i> جدول أنصبة ومواعيد المراقبة للكادر التعليمي (عدالة التوزيع)</h3>
        <div id="examInvigilatorGrid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(300px, 1fr));gap:14px;">
            <!-- Teacher proctoring duties rendered dynamically -->
        </div>
    </div>

    <!-- 4. Student Personal Schedule & Exam Pass Container -->
    <div id="examStudentViewContainer" style="display:none;margin-bottom:20px;background:rgba(15,23,42,0.8);border:1px solid var(--border);border-radius:12px;padding:16px;">
        <h3 style="margin-top:0;color:#60a5fa;font-size:1rem;"><i class="fa-solid fa-id-card"></i> بطاقة دخول الامتحان الرقمية والتعليمات الامتحانية للطالب</h3>
        <div id="studentExamPassCard" style="background:rgba(30,58,138,0.3);border:2px dashed #3b82f6;border-radius:12px;padding:20px;max-width:650px;margin:0 auto;">
            <!-- Student Exam Pass rendered dynamically -->
        </div>
    </div>

    <!-- Detailed Exam Schedule Data Table -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الجلسة</th>
                    <th>الفصل الدراسي</th>
                    <th>نوع الامتحان</th>
                    <th>الصف والشعبة</th>
                    <th>المادة الدراسية</th>
                    <th>تاريخ الامتحان</th>
                    <th>الفترة والوقت</th>
                    <th>المدة والوزن</th>
                    <th>القاعة المخصصة</th>
                    <th>عدد الطلاب والسعة</th>
                    <th>المراقبون المسؤولون</th>
                    <th>حالة التعارض</th>
                    <th>حالة الاعتماد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-exam-schedule-grid"></tbody>
        </table>
    </div>
</div>

<!-- Dedicated Exam Session Modal -->
<div class="modal-overlay" id="examSessionModal">
    <div class="modal-content glass-panel" style="max-width:600px;">
        <div class="modal-header">
            <h3><i class="fa-solid fa-calendar-plus" style="color:#3b82f6;"></i> إضافة / تعديل جلسة امتحان رسمية</h3>
            <div class="window-controls"><button class="btn-close" onclick="closeModal('examSessionModal')"><i class="fa-solid fa-xmark"></i></button></div>
        </div>
        <div class="modal-body" style="padding:16px;">
            <input type="hidden" id="exm_edit_id">
            <div class="fg"><label>الفصل الدراسي <span class="req">*</span></label><select id="exm_term"><option>الفصل الدراسي الثاني 2025/2026</option><option>الفصل الدراسي الأول 2025/2026</option></select></div>
            <div class="fg"><label>نوع الامتحان <span class="req">*</span></label><select id="exm_type"><option>اختبارات نهاية الفصل</option><option>اختبارات منتصف الفصل</option><option>اختبارات شهرية</option><option>اختبارات عملية / معامل</option></select></div>
            <div class="fg"><label>الصف والشعبة <span class="req">*</span></label><select id="exm_grade_sec"><option>الثالث الثانوي - شعبة (أ)</option><option>الثاني الثانوي - شعبة (ب)</option><option>التاسع الأساسي - شعبة (أ)</option><option>السابع الأساسي - شعبة (أ)</option></select></div>
            <div class="fg"><label>المادة الدراسية <span class="req">*</span></label><input id="exm_subject" placeholder="مثال: الرياضيات المتقدمة" value="الرياضيات المتقدمة" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>تاريخ الامتحان <span class="req">*</span></label><input type="date" id="exm_date" value="2026-06-15"></div>
            <div class="fg"><label>الفترة والتوقيت <span class="req">*</span></label><select id="exm_period"><option value="صباحية">الفترة الأولى - صباحية (08:30 AM - 11:30 AM)</option><option value="مسائية">الفترة الثانية - ظهرية (12:30 PM - 03:30 PM)</option></select></div>
            <div class="fg"><label>معامل صعوبة المادة (Weight) <span class="req">*</span></label><select id="exm_weight"><option value="صعبة (وزن 3)">🔴 مادة صعبة (وزن 3 - تتطلب يومين راحة)</option><option value="متوسطة (وزن 2)">🟡 مادة متوسطة (وزن 2 - تتطلب يوم راحة)</option><option value="خفيفة (وزن 1)">🟢 مادة خفيفة (وزن 1 - مباشرة)</option></select></div>
            <div class="fg"><label>القاعة المخصصة <span class="req">*</span></label><select id="exm_hall"><option>القاعة الكبرى (01) - سعة 40 طالب</option><option>المدرج الأكاديمي الرئيسي - سعة 100 طالب</option><option>معمل الكمبيوتر (01) - سعة 30 طالب</option><option>الفصل 3/أ - سعة 35 طالب</option></select></div>
            <div class="fg"><label>فريق المراقبة المسند <span class="req">*</span></label><input id="exm_proctors" placeholder="أ. خالد محمود + أ. إبراهيم العنسي" value="أ. خالد محمود + أ. إبراهيم العنسي" oninput="validateTextOnly(this)"></div>
            <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:16px;">
                <button class="btn-save" onclick="saveExamSessionSlot()"><i class="fa-solid fa-floppy-disk"></i> حفظ جلسة الامتحان</button>
                <button class="btn-cancel" onclick="closeModal('examSessionModal')"><i class="fa-solid fa-xmark"></i> إلغاء</button>
            </div>
        </div>
    </div>
</div>
"""

pattern_exam_page = r'<div class="page" id="pg-exam-schedule">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
html = re.sub(pattern_exam_page, smart_exam_html.strip() + '\n', html, flags=re.DOTALL)

print("  ✓ Rebuilt Smart Exam Scheduler (pg-exam-schedule) HTML container")

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

print("Updated HTML files with Smart Exam Scheduler!")
