"""
Python script to update school.html according to explicit user request:
1. DELETE pages:
   - pg-departments (دليل الأقسام)
   - pg-nationalities (دليل الجنسيات)
   - pg-visitors (سجل الزوار)
   - pg-behavior (السلوك والمخالفات)
   - pg-library (إدارة المكتبة)
   - pg-leave-management (إدارة الإجازات في شؤون الطلاب)
2. Remove Hub links (Exams, SMS, Inventory) from Student Affairs navigation section.
3. RE-ARCHITECT & UPDATE pages:
   - pg-academic-calendar (التقويم المدرسي)
   - pg-classrooms (القاعات الدراسية)
   - pg-timetable-builder / pg-schedule (بناء الجدول الدراسي)
   - pg-homework-tracker (متابعة الواجبات)
   - pg-performance-eval (تقييم الأداء)
   - pg-promotion-workflow (الترفيع الجماعي)
   - pg-student-docs (وثائق الطلاب مع نافذة منبثقة تفاعلية للمرحلة والصف والطالب)
   - pg-section-distribution (توزيع الطلاب على الشعب)
   - pg-discontinued (الطلاب غير المستمرين)
   - pg-class-notes (ملاحظات رائد الفصل)
   - pg-enrollment (التسجيل والرسوم)
"""
import re, time

print("=" * 60)
print("Updating school.html according to exact user directives...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. DELETE PAGES
pages_to_delete = [
    'pg-departments', 'pg-nationalities', 'pg-visitors', 
    'pg-behavior', 'pg-library', 'pg-leave-management'
]

for p_id in pages_to_delete:
    pattern = rf'<div class="page" id="{p_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html, re.DOTALL):
        html = re.sub(pattern, '', html, flags=re.DOTALL)
        print(f"  ✓ Removed page: {p_id}")
    
    # Remove sidebar link
    link_pattern = rf'<a[^>]*goTo\([\'"]{p_id}[\'"]\)[^>]*>.*?</a>'
    html = re.sub(link_pattern, '', html, flags=re.DOTALL)
    print(f"  ✓ Removed sidebar link for: {p_id}")


# Helper function to replace/insert page content
def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page content for: {page_id}")
    else:
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added page content for: {page_id}")
    return html_text

# 2. RE-ARCHITECTED HTML CONTENT

# A. Academic Calendar (pg-academic-calendar)
calendar_html = """
<div class="page" id="pg-academic-calendar">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-days"></i> التقويم المدرسي والفعاليات الأكاديمية</h2>
    </div>

    <!-- Switcher, Tags & Filters -->
    <div class="toolbar" style="margin-bottom:16px;flex-wrap:wrap;gap:12px;">
        <div class="tab-nav" style="margin:0;border:none;padding:0;">
            <button class="tab-btn active" onclick="switchCalView('month', this)"><i class="fa-solid fa-calendar-grid"></i> شهري</button>
            <button class="tab-btn" onclick="switchCalView('week', this)"><i class="fa-solid fa-calendar-week"></i> أسبوعي</button>
            <button class="tab-btn" onclick="switchCalView('day', this)"><i class="fa-solid fa-calendar-day"></i> يومي</button>
            <button class="tab-btn" onclick="switchCalView('agenda', this)"><i class="fa-solid fa-list-ol"></i> أجندة الفعاليات</button>
        </div>

        <select id="calFilterStage" onchange="renderAcademicCalendar()" style="width:140px;">
            <option value="all">جميع المراحل</option>
            <option value="ابتدائية">الابتدائية</option>
            <option value="ثانوية">الثانوية</option>
        </select>

        <select id="calFilterAudience" onchange="renderAcademicCalendar()" style="width:140px;">
            <option value="all">جميع الفئات</option>
            <option value="طلاب">الطلاب</option>
            <option value="معلمين">المعلمين</option>
            <option value="أولياء أمور">أولياء الأمور</option>
        </select>

        <button class="btn-add" onclick="openForm('academic-calendar')"><i class="fa-solid fa-plus"></i> إضافة حدث جديد</button>
    </div>

    <!-- Color-coded Tags Legend -->
    <div style="display:flex;gap:16px;margin-bottom:16px;background:rgba(255,255,255,0.03);padding:10px 16px;border-radius:10px;border:1px solid var(--border);flex-wrap:wrap;">
        <span style="font-size:0.83rem;font-weight:700;color:var(--muted);"><i class="fa-solid fa-tags"></i> دليل الألوان:</span>
        <span style="font-size:0.83rem;color:#60a5fa;"><i class="fa-solid fa-circle" style="color:#3b82f6;"></i> أيام دراسية</span>
        <span style="font-size:0.83rem;color:#f87171;"><i class="fa-solid fa-circle" style="color:#ef4444;"></i> إجازات رسمية</span>
        <span style="font-size:0.83rem;color:#fbbf24;"><i class="fa-solid fa-circle" style="color:#f59e0b;"></i> اختبارات امتحانات</span>
        <span style="font-size:0.83rem;color:#34d399;"><i class="fa-solid fa-circle" style="color:#10b981;"></i> أنشطة ورحلات</span>
    </div>

    <!-- Calendar View Wrapper -->
    <div class="form-card" style="padding:16px;" id="calViewContainer">
        <!-- Rendered Calendar Grid / Agenda List -->
    </div>
</div>
"""

# B. Classrooms (pg-classrooms)
classrooms_html = """
<div class="page" id="pg-classrooms">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-chalkboard"></i> دليل القاعات والمعامل الدراسية وتتبع الإشغال</h2>
    </div>

    <div class="toolbar">
        <select id="crFilterBuilding" onchange="renderClassroomsGrid()" style="width:160px;">
            <option value="all">جميع المباني والأدوار</option>
            <option value="مبنى 1 - الدور 1">مبنى 1 - الدور الأول</option>
            <option value="مبنى 1 - الدور 2">مبنى 1 - الدور الثاني</option>
        </select>
        <select id="crFilterType" onchange="renderClassroomsGrid()" style="width:150px;">
            <option value="all">جميع الأنواع</option>
            <option value="فصل عادي">فصل عادي</option>
            <option value="معمل حاسوب">معمل حاسوب</option>
            <option value="مختبر كيمياء">مختبر كيمياء</option>
        </select>
        <button class="btn-add" onclick="openForm('classrooms')"><i class="fa-solid fa-plus"></i> إضافة قاعة جديدة</button>
    </div>

    <!-- Color Legend -->
    <div style="display:flex;gap:16px;margin-bottom:16px;background:rgba(0,0,0,0.2);padding:10px 14px;border-radius:8px;font-size:0.83rem;">
        <span style="color:#10b981;font-weight:700;"><i class="fa-solid fa-square"></i> أخضر = شاغرة (متاحة)</span>
        <span style="color:#ef4444;font-weight:700;"><i class="fa-solid fa-square"></i> أحمر = مشغولة بحصة</span>
        <span style="color:#f59e0b;font-weight:700;"><i class="fa-solid fa-square"></i> أصفر = قيد الصيانة</span>
    </div>

    <!-- Interactive Floor Grid -->
    <div id="classroomsFloorGrid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;margin-bottom:20px;">
        <!-- Rendered cards -->
    </div>
</div>
"""

# C. Timetable Builder (pg-timetable-builder / pg-schedule)
timetable_html = """
<div class="page" id="pg-timetable-builder">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-table-columns"></i> بناء الجدول الدراسي التفاعلي وتفادي التعارضات</h2>
    </div>

    <div class="toolbar" style="flex-wrap:wrap;gap:10px;">
        <select id="ttYearTerm" style="width:170px;"><option>2026/2027 - الترم الأول</option></select>
        <select id="ttGradeSection" onchange="renderInteractiveTimetable()" style="width:180px;">
            <option value="الصف الأول الثانوي - شعبة (أ)">الصف الأول الثانوي - شعبة (أ)</option>
            <option value="الصف الثاني الثانوي - شعبة (أ)">الصف الثاني الثانوي - شعبة (أ)</option>
            <option value="الصف الثالث الثانوي - شعبة (ب)">الصف الثالث الثانوي - شعبة (ب)</option>
        </select>
        <button class="btn-add" onclick="autoGenerateTimetable()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-wand-magic-sparkles"></i> التوليد الآلي الذكي</button>
        <button class="btn-add" onclick="saveTimetablePublish()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check"></i> اعتماد ونشر الجدول</button>
    </div>

    <!-- Conflict Warning Banner -->
    <div id="ttConflictBanner" style="display:none;background:rgba(239,68,68,0.2);border:1px solid #ef4444;color:#f87171;padding:10px 14px;border-radius:8px;margin-bottom:14px;font-weight:700;">
        <i class="fa-solid fa-triangle-exclamation"></i> تنبيه تعارض: المعلم م. إبراهيم علي مشغول في القاعة 102 في نفس التوقيت!
    </div>

    <!-- Main Schedule Workspace Grid + Unassigned Pool -->
    <div style="display:grid;grid-template-columns:1fr 280px;gap:18px;">
        <div>
            <div id="interactiveTimetableMatrix" class="timetable-grid">
                <!-- Rendered Matrix -->
            </div>
        </div>

        <div class="form-card" style="padding:14px;">
            <h4 style="color:#93c5fd;font-size:0.9rem;margin-bottom:10px;"><i class="fa-solid fa-list-check"></i> الحصص المتبقية (Unassigned Pool)</h4>
            <div id="ttUnassignedPool" style="display:flex;flex-direction:column;gap:8px;max-height:450px;overflow-y:auto;">
                <!-- Unassigned subjects cards -->
            </div>
        </div>
    </div>
</div>
"""

# D. Homework Tracker (pg-homework-tracker)
homework_html = """
<div class="page" id="pg-homework-tracker">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-book-open-reader"></i> متابعة الواجبات المدرسية والتصحيح</h2>
    </div>

    <!-- Role Based Tabs -->
    <div class="tab-nav">
        <button class="tab-btn active" onclick="switchHwRole('teacher', this)"><i class="fa-solid fa-chalkboard-user"></i> واجهة المعلم (إسناد وتصحيح)</button>
        <button class="tab-btn" onclick="switchHwRole('student', this)"><i class="fa-solid fa-user-graduate"></i> واجهة الطالب (رفع الحلول)</button>
        <button class="tab-btn" onclick="switchHwRole('parent', this)"><i class="fa-solid fa-people-roof"></i> واجهة ولي الأمر / الإدارة</button>
    </div>

    <!-- KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>الواجبات النشطة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">8 واجبات</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>قيد التصحيح</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">3 واجبات</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>المكتملة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">15 واجب</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('homework')"><i class="fa-solid fa-plus"></i> إنشاء واجب جديد</button>
        <select id="hwFilterSubject" onchange="renderHomeworkList()" style="width:150px;"><option value="all">جميع المواد</option><option value="كيمياء">كيمياء</option><option value="رياضيات">رياضيات</option></select>
        <select id="hwFilterStatus" onchange="renderHomeworkList()" style="width:140px;"><option value="all">جميع الحالات</option><option value="نشط">نشط</option><option value="قيد التصحيح">قيد التصحيح</option><option value="مكتمل">مكتمل</option></select>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>تاريخ الإسناد</th>
                    <th>المادة الدراسية</th>
                    <th>الصف والشعبة</th>
                    <th>عنوان الواجب</th>
                    <th>تاريخ الاستحقاق</th>
                    <th>الحالة والوسم</th>
                    <th>نسبة التسليم</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-homework-list"></tbody>
        </table>
    </div>
</div>
"""

# E. Performance Evaluation (pg-performance-eval)
performance_html = """
<div class="page" id="pg-performance-eval">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-star"></i> نظام تقييم الأداء والكفاءة الوظيفية (Performance Appraisal)</h2>
    </div>

    <!-- Executive KPI Summary Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>التقدير العام للدورة</h3><p style="color:#10b981;font-weight:800;font-size:1.2rem;">يتجاوز التوقعات (92.5%)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المُقيّمون المكتملون</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">18 / 20 موظف</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>مراجعات HR المعلقة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">2 نموذج</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="evalCycleSelect" onchange="renderPerformanceEvals()" style="width:200px;">
            <option>تقييم النصف الأول 2026</option>
            <option>التقييم السنوي 2025</option>
        </select>
        <button class="btn-add" onclick="openForm('performance_eval')"><i class="fa-solid fa-plus"></i> تقييم جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المُقيَّم (الموظف)</th>
                    <th>المسمى الوظيفي</th>
                    <th>المُقيّم (المدير)</th>
                    <th>دورة التقييم</th>
                    <th>الدرجة الموزونة</th>
                    <th>التقدير النهائي</th>
                    <th>حالة الاعتماد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-performance-list"></tbody>
        </table>
    </div>
</div>
"""

# F. Promotion Workflow (pg-promotion-workflow)
promotion_html = """
<div class="page" id="pg-promotion-workflow">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-turn-up"></i> الترفيع الجماعي للطلاب وتوزيع الدفعات</h2>
    </div>

    <!-- Source & Target Context Selection -->
    <div class="form-card" style="margin-bottom:16px;">
        <h4 style="color:#93c5fd;font-size:0.95rem;margin-bottom:12px;"><i class="fa-solid fa-route"></i> تحديد المصدر والوجهة الأكاديمية</h4>
        <div class="form-row">
            <div class="fg">
                <label>السنة والصف الحالي (المصدر)</label>
                <select id="promoSourceGrade" onchange="renderPromotionBatch()">
                    <option value="2025/2026 - الأول الثانوي - شعبة (أ)">2025/2026 - الأول الثانوي - شعبة (أ)</option>
                    <option value="2025/2026 - الثاني الثانوي - شعبة (أ)">2025/2026 - الثاني الثانوي - شعبة (أ)</option>
                </select>
            </div>
            <div class="fg">
                <label>السنة والصف المستهدف (الوجهة)</label>
                <select id="promoTargetGrade">
                    <option value="2026/2027 - الثاني الثانوي">2026/2027 - الثاني الثانوي</option>
                    <option value="2026/2027 - الثالث الثانوي">2026/2027 - الثالث الثانوي</option>
                </select>
            </div>
            <div class="fg">
                <label>قاعدة الترفيع الآلية</label>
                <select id="promoRule">
                    <option value="standard">ترحيل الناجحين + المنقولين بمادة واحدة</option>
                    <option value="strict">الناجحين فقط (بدون رسوب في أي مادة)</option>
                </select>
            </div>
        </div>
    </div>

    <div class="toolbar" style="margin-bottom:12px;">
        <button class="btn-add" onclick="executeBatchPromotion()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check-double"></i> اعتماد وتنفيذ الترفيع الجماعي</button>
        <button class="btn-add" onclick="toast('تم استعراض تقرير الترفيع التجريبي')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-eye"></i> الترفيع التجريبي (Dry Run)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th><input type="checkbox" onclick="toggleAllPromo(this)" checked></th>
                    <th>الرقم الأكاديمي والاسم</th>
                    <th>المعدل والنتيجة</th>
                    <th>المواد المتبقية</th>
                    <th>موانع الترفيع (مالي/وثائقي)</th>
                    <th>الحالة المقترحة</th>
                    <th>الشعبة المستهدفة</th>
                    <th>تعديل القرار</th>
                </tr>
            </thead>
            <tbody id="tbl-promotion-batch"></tbody>
        </table>
    </div>
</div>
"""

# G. Student Docs with Popup Flow (pg-student-docs)
student_docs_html = """
<div class="page" id="pg-student-docs">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-folder-open"></i> وثائق الطلاب والمرفقات الرسمية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openStudentDocModalFlow()"><i class="fa-solid fa-plus"></i> إضافة وثيقة لـ طالب محدد</button>
        <div class="search-box" style="flex:1;max-width:300px;"><i class="fa-solid fa-magnifying-glass"></i><input id="searchStudentDocs" placeholder="بحث بالوثيقة أو اسم الطالب..." oninput="renderStudentDocs()"></div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اسم الطالب</th>
                    <th>الصف الدراسي</th>
                    <th>نوع الوثيقة</th>
                    <th>تاريخ الإضافة</th>
                    <th>الحالة والتصديق</th>
                    <th>معاينة الوثيقة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-student-docs"></tbody>
        </table>
    </div>
</div>
"""

# H. Section Distribution (pg-section-distribution)
section_dist_html = """
<div class="page" id="pg-section-distribution">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-arrows-split-up-and-left"></i> توزيع الطلاب الذكي على الشعب والقاعات</h2>
    </div>

    <!-- Header & Algorithm Selection -->
    <div class="form-card" style="margin-bottom:16px;">
        <div class="form-row">
            <div class="fg">
                <label>الصف الدراسي</label>
                <select id="sdGradeSelect" onchange="renderSectionDistributionWorkspace()">
                    <option value="الصف الأول الثانوي">الصف الأول الثانوي</option>
                    <option value="الصف الثاني الثانوي">الصف الثاني الثانوي</option>
                </select>
            </div>
            <div class="fg">
                <label>خوارزمية التوزيع التلقائي</label>
                <select id="sdAlgorithm">
                    <option value="alphabetical">أبجدي (حسب اسم الطالب)</option>
                    <option value="gpa">حسب المعدل الأكاديمي (توازن المستويات)</option>
                    <option value="gender">توازن الجنسين</option>
                    <option value="random">عشوائي متساوي</option>
                </select>
            </div>
            <div class="fg" style="display:flex;align-items:flex-end;">
                <button class="btn-add" onclick="executeSmartSectionDistribution()" style="width:100%;height:42px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-wand-magic-sparkles"></i> تنفيذ التوزيع التلقائي الذكي</button>
            </div>
        </div>
    </div>

    <!-- Main Drag & Drop Workspace -->
    <div style="display:grid;grid-template-columns:260px 1fr;gap:18px;margin-bottom:16px;">
        <!-- Unassigned Student Pool -->
        <div class="form-card" style="padding:14px;">
            <h4 style="color:#93c5fd;font-size:0.9rem;margin-bottom:10px;"><i class="fa-solid fa-users"></i> قائمة المنتظر توزيعهم (<span id="sdUnassignedCount">0</span>)</h4>
            <div id="sdUnassignedStudentPool" style="display:flex;flex-direction:column;gap:6px;max-height:420px;overflow-y:auto;">
                <!-- Cards -->
            </div>
        </div>

        <!-- Target Cards Grid (Section A, B, C) -->
        <div id="sdTargetSectionsGrid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:14px;">
            <!-- Target Section Cards -->
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="saveSectionDistribution()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check"></i> اعتماد وحفظ التوزيع</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشوفات الشعب</button>
    </div>
</div>
"""

# I. Discontinued Students (pg-discontinued)
discontinued_html = """
<div class="page" id="pg-discontinued">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-xmark"></i> سجل وإدارة الطلاب غير المستمرين (المنقطعين / المنسحبين)</h2>
    </div>

    <!-- KPI Summary -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>إجمالي غير المستمرين</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">12 طالب</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>موقوفون لـ أسباب مالية</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">4 طلاب</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>طلبات إعادة القيد المعلقة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">2 طلب</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('discontinued')"><i class="fa-solid fa-user-slash"></i> تحويل طالب لـ غير مستمر</button>
        <div class="search-box" style="flex:1;max-width:280px;"><i class="fa-solid fa-magnifying-glass"></i><input id="searchDiscontinued" placeholder="بحث بالاسم أو السبب..." oninput="renderDiscontinuedList()"></div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اسم الطالب</th>
                    <th>الصف الدراسي</th>
                    <th>نوع التوقف</th>
                    <th>تاريخ السريان</th>
                    <th>السبب والتنبيهات</th>
                    <th>إخلاء الطرف والعهد</th>
                    <th>الموقف المالي</th>
                    <th>إجراءات / عودة</th>
                </tr>
            </thead>
            <tbody id="tbl-discontinued-list"></tbody>
        </table>
    </div>
</div>
"""

# J. Class Notes (pg-class-notes)
class_notes_html = """
<div class="page" id="pg-class-notes">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-note-sticky"></i> سجل وملاحظات رائد الفصل الإرشادية</h2>
    </div>

    <div class="toolbar" style="flex-wrap:wrap;">
        <select id="cnSectionSelect" onchange="renderClassNotesTimeline()" style="width:180px;">
            <option value="الصف الثالث متوسط - شعبة (ب)">الصف الثالث متوسط - شعبة (ب)</option>
            <option value="الصف الثاني الثانوي - شعبة (أ)">الصف الثاني الثانوي - شعبة (أ)</option>
        </select>
        <button class="btn-add" onclick="openForm('class-notes')"><i class="fa-solid fa-plus"></i> إضافة ملاحظة تربوية جديدة</button>
    </div>

    <!-- Timeline Feed Container -->
    <div class="form-card" style="padding:16px;">
        <h4 style="color:#93c5fd;font-size:0.95rem;margin-bottom:14px;"><i class="fa-solid fa-timeline"></i> السجل الزمني لملاحظات الشعبة</h4>
        <div id="cnNotesTimeline" style="display:flex;flex-direction:column;gap:12px;">
            <!-- Rendered notes timeline -->
        </div>
    </div>
</div>
"""

# K. Registration & Fees (pg-enrollment)
enrollment_html = """
<div class="page" id="pg-enrollment">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-invoice"></i> إدارة القبول والتسجيل والرسوم الدراسية الشاملة</h2>
    </div>

    <!-- Financial KPI Status Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي عقود الرسوم</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">450,000 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>الخصومات الممنوحة</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">45,000 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي المحصل</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">280,000 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>المتبقي المتأخر</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">125,000 $</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('enrollment')"><i class="fa-solid fa-user-plus"></i> تسجيل عقد طالب جديد وحساب الرسوم</button>
        <div class="search-box" style="flex:1;max-width:280px;"><i class="fa-solid fa-magnifying-glass"></i><input id="searchEnrollment" placeholder="بحث بالطلب أو اسم الطالب..." oninput="renderEnrollmentList()"></div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم التسجيل</th>
                    <th>اسم الطالب والصف</th>
                    <th>نوع التسجيل</th>
                    <th>الرسوم الأساسية</th>
                    <th>الخدمات المضافة</th>
                    <th>الخصم المالي</th>
                    <th>إجمالي الصافي</th>
                    <th>المسدد</th>
                    <th>المتبقي</th>
                    <th>حالة السداد</th>
                    <th>إجراءات / تحصيل</th>
                </tr>
            </thead>
            <tbody id="tbl-enrollment-list"></tbody>
        </table>
    </div>
</div>
"""

# Replace or add all pages in html
html = replace_or_add_page(html, 'pg-academic-calendar', calendar_html)
html = replace_or_add_page(html, 'pg-classrooms', classrooms_html)
html = replace_or_add_page(html, 'pg-timetable-builder', timetable_html)
html = replace_or_add_page(html, 'pg-homework-tracker', homework_html)
html = replace_or_add_page(html, 'pg-performance-eval', performance_html)
html = replace_or_add_page(html, 'pg-promotion-workflow', promotion_html)
html = replace_or_add_page(html, 'pg-student-docs', student_docs_html)
html = replace_or_add_page(html, 'pg-section-distribution', section_dist_html)
html = replace_or_add_page(html, 'pg-discontinued', discontinued_html)
html = replace_or_add_page(html, 'pg-class-notes', class_notes_html)
html = replace_or_add_page(html, 'pg-enrollment', enrollment_html)

# Clean up sidebar links for deleted items
links_to_remove = ['pg-departments', 'pg-nationalities', 'pg-visitors', 'pg-behavior', 'pg-library', 'pg-leave-management']
for l_id in links_to_remove:
    link_pattern = rf'<a[^>]*goTo\([\'"]{l_id}[\'"]\)[^>]*>.*?</a>'
    html = re.sub(link_pattern, '', html, flags=re.DOTALL)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

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

print("HTML update completed successfully!")
