"""
Python script to update/re-architect Control & Examination modules in school.html:
1. DELETE pages:
   - pg-monthly-grades (ترصيد الدرجات الشهرية)
   - pg-term-grades (درجات نهاية الفصل)
2. RE-ARCHITECT & UPDATE pages:
   - pg-grading (رصد الدرجات والاختبارات)
   - pg-results (النتائج والتقديرات النهائية)
   - pg-certificates (إصدار الشهادات الرسمية)
   - pg-homework-tracker (متابعة الواجبات المدرسية)
   - pg-exam-halls (أماكن ولجان الامتحانات)
   - pg-seat-numbers (كشوفات وأرقام الجلوس)
   - pg-secret-numbers (توليد الأرقام السرية وتشفير أوراق الإجابة)
   - pg-hall-distribution (توزيع اللجان والمراقبين)
   - pg-exam-schedule (جدول الامتحانات الرسمية)
   - pg-roll-call (كشوفات المناداة للمنادين)
   - pg-seat-cards (طباعة بطاقات أرقام الجلوس)
   - pg-substitute (إدارة المدرس البديل)
"""
import re, time

print("=" * 60)
print("Updating Control & Exam Modules in school.html...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. DELETE PAGES
pages_to_delete = ['pg-monthly-grades', 'pg-term-grades']

for p_id in pages_to_delete:
    pattern = rf'<div class="page" id="{p_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html, re.DOTALL):
        html = re.sub(pattern, '', html, flags=re.DOTALL)
        print(f"  ✓ Removed page: {p_id}")
    
    # Remove sidebar links
    link_pattern = rf'<a[^>]*goTo\([\'"]{p_id}[\'"]\)[^>]*>.*?</a>'
    html = re.sub(link_pattern, '', html, flags=re.DOTALL)
    print(f"  ✓ Removed sidebar link for: {p_id}")

def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page content for: {page_id}")
    else:
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added page content for: {page_id}")
    return html_text

# 2. HTML CONTENT DEFINITIONS

# A. Grading & Assessments (pg-grading)
grading_html = """
<div class="page" id="pg-grading">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-pen-to-square"></i> شيت رصد الدرجات والاختبارات التفاعلي</h2>
    </div>

    <!-- Academic Scope Filters & Lock Toolbar -->
    <div class="toolbar" style="flex-wrap:wrap;gap:10px;">
        <select id="grYearTerm" style="width:170px;"><option>2026/2027 - الترم الأول</option></select>
        <select id="grSubject" onchange="renderInteractiveGradingGrid()" style="width:160px;">
            <option value="اللغة العربية">اللغة العربية</option>
            <option value="الكيمياء العامة">الكيمياء العامة</option>
            <option value="الرياضيات">الرياضيات</option>
        </select>
        <select id="grGradeSec" onchange="renderInteractiveGradingGrid()" style="width:180px;">
            <option value="الصف الثاني الثانوي - شعبة (أ)">الصف الثاني الثانوي - شعبة (أ)</option>
            <option value="الصف الثالث الثانوي - شعبة (ب)">الصف الثالث الثانوي - شعبة (ب)</option>
        </select>
        <select id="grAssessType" onchange="renderInteractiveGradingGrid()" style="width:150px;">
            <option value="اختبار منتصف الفصل">اختبار منتصف الفصل</option>
            <option value="أعمال سنة">أعمال سنة</option>
            <option value="اختبار نهائي">اختبار نهائي</option>
        </select>

        <button class="btn-add" id="btnLockGrading" onclick="toggleGradingLock()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-lock"></i> قفل واعتماد الشيت</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة مسودة الكنترول</button>
    </div>

    <!-- Lock Status Indicator -->
    <div id="grLockBanner" style="display:flex;justify-content:space-between;align-items:center;background:rgba(16,185,129,0.15);border:1px solid #10b981;color:#10b981;padding:8px 14px;border-radius:8px;margin-bottom:14px;font-weight:700;">
        <span><i class="fa-solid fa-lock-open"></i> حالة الشيت: مفتوح للرصد وتعديل الدرجات</span>
        <span style="font-size:0.83rem;">الدرجة العظمى للمادة: <strong id="grMaxScoreDisp">40</strong> | نجاح: <strong id="grPassScoreDisp">20</strong></span>
    </div>

    <!-- Interactive Grading Grid -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>الرقم السري (SEC)</th>
                    <th>بيانات الطالب ورقم الجلوس</th>
                    <th>أعمال السنة (20)</th>
                    <th>الدرجة المدخلة (40)</th>
                    <th>المجموع الكلي (100)</th>
                    <th>التقدير الرمزي</th>
                    <th>نتيجة المادة</th>
                    <th>حالة القفل</th>
                    <th>ملاحظات الكنترول</th>
                </tr>
            </thead>
            <tbody id="tbl-interactive-grading"></tbody>
        </table>
    </div>
</div>
"""

# B. Final Results & Transcripts (pg-results)
results_html = """
<div class="page" id="pg-results">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-ranking-star"></i> نتائج وتقديرات الطلاب النهائية والتراكمي</h2>
    </div>

    <!-- KPI Summary Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>نسبة النجاح العامة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">94.5% (113/120)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>المرتفعون بمرتبة الشرف</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">15 طالب</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>منقولون بمواد (دور ثاني)</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">5 طلاب</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>نتائج محجوبة (مانع مالي)</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">2 طالب</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="rsBatchSelect" onchange="renderFinalResultsGrid()" style="width:200px;"><option value="الصف الثاني الثانوي">الصف الثاني الثانوي</option><option value="الصف الثالث الثانوي">الصف الثالث الثانوي</option></select>
        <button class="btn-add" onclick="calculateFinalResultsGPA()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-calculator"></i> معالجة واحتساب النتائج والتراكمي آلياً</button>
        <button class="btn-add" onclick="togglePublishResults()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-globe"></i> اعتماد ونشر النتائج للبوابة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>بيانات الطالب الأكاديمية</th>
                    <th>المجموع المكتسب</th>
                    <th>النسبة المئوية</th>
                    <th>المعدل التراكمي (CGPA)</th>
                    <th>التقدير العام</th>
                    <th>الترتيب على الدفعة</th>
                    <th>مرتبة الشرف</th>
                    <th>القرار والحالة النهائية</th>
                    <th>المواد المتبقية</th>
                    <th>حالة حجب النتيجة</th>
                    <th>حالة النشر والاعتماد</th>
                    <th>إجراءات / الشهادة</th>
                </tr>
            </thead>
            <tbody id="tbl-final-results-grid"></tbody>
        </table>
    </div>
</div>
"""

# C. Official Certificates (pg-certificates)
certificates_html = """
<div class="page" id="pg-certificates">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-certificate"></i> إصدار الشهادات الرسمية والتوثيق الرقمي (QR)</h2>
    </div>

    <div class="toolbar">
        <select id="certGradeFilter" onchange="renderCertificatesGrid()" style="width:180px;"><option value="الصف الثالث الثانوي">الصف الثالث الثانوي</option><option value="الصف الثاني الثانوي">الصف الثاني الثانوي</option></select>
        <button class="btn-add" onclick="generateBulkCertificates()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-gears"></i> توليد وتشفير الشهادات جماعياً</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة الشهادات المعتمدة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم التسلسل المرجعي</th>
                    <th>بيانات الطالب ورقم الجلوس</th>
                    <th>المؤهل / الصف</th>
                    <th>المعدل والتقدير العام</th>
                    <th>عام التخرج</th>
                    <th>رمز التحقق الرقمي (QR)</th>
                    <th>نوع الوثيقة</th>
                    <th>حالة التوقيع والختم</th>
                    <th>حالة الطباعة والتسليم</th>
                    <th>تاريخ الإصدار</th>
                    <th>معاينة وطباعة</th>
                </tr>
            </thead>
            <tbody id="tbl-certificates-grid"></tbody>
        </table>
    </div>
</div>
"""

# D. Exam Halls & Capacity (pg-exam-halls)
exam_halls_html = """
<div class="page" id="pg-exam-halls">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-location-dot"></i> تهيئة أماكن ولجان الامتحانات والسعة الاستيعابية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('exam_halls')"><i class="fa-solid fa-plus"></i> إضافة لجنة / قاعة امتحانية</button>
        <button class="btn-add" onclick="autoBuildSeating()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-wand-magic-sparkles"></i> التوزيع الآلي لأرقام الجلوس</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم / اسم اللجنة</th>
                    <th>المبنى والدور والقاعة</th>
                    <th>السعة الاستيعابية</th>
                    <th>الصفوف والشعب المستهدفة</th>
                    <th>نطاق أرقام الجلوس</th>
                    <th>نمط التوزيع</th>
                    <th>رئيس اللجنة (المشرف)</th>
                    <th>الملاحظون / المراقبون</th>
                    <th>حالة جاهزية القاعة</th>
                    <th>كشوف التوقيع (PDF)</th>
                    <th>ملصقات الطاولات</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-exam-halls-grid"></tbody>
        </table>
    </div>
</div>
"""

# E. Seating Numbers (pg-seat-numbers)
seat_numbers_html = """
<div class="page" id="pg-seat-numbers">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-hashtag"></i> كشوفات وتوليد أرقام الجلوس والباركود</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="generateAutoRollNumbers()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-gears"></i> توليد تسلسل أرقام الجلوس آلياً</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-print"></i> طباعة كشوفات التعليق العامة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم الجلوس</th>
                    <th>اسم الطالب الكامل</th>
                    <th>الرقم الأكاديمي والصورة</th>
                    <th>الصف والشعبة</th>
                    <th>رقم واسم اللجنة</th>
                    <th>رقم المقعد والطاولة</th>
                    <th>المبنى والدور</th>
                    <th>الرمز المشفر (Barcode)</th>
                    <th>نوع الكشف</th>
                    <th>حالة الطباعة الإشارات</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-seat-numbers-grid"></tbody>
        </table>
    </div>
</div>
"""

# F. Secret Numbers & Anonymity (pg-secret-numbers)
secret_numbers_html = """
<div class="page" id="pg-secret-numbers">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-secret"></i> توليد الأرقام السرية وتشفير أوراق الإجابة</h2>
    </div>

    <!-- Security Lock Status Banner -->
    <div style="display:flex;justify-content:space-between;align-items:center;background:rgba(239,68,68,0.2);border:1px solid #ef4444;color:#f87171;padding:10px 14px;border-radius:8px;margin-bottom:14px;font-weight:700;">
        <span><i class="fa-solid fa-user-shield"></i> حالة التشفير: جدول الأسماء والسرية مُقفل ومحمي بكلمة مرور الكنترول</span>
        <button class="btn-add" onclick="toggleSecretDeanonymize()" style="padding:4px 10px;font-size:0.8rem;background:#ef4444;"><i class="fa-solid fa-key"></i> فك التشفير (خاص برئيس الكنترول)</button>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="generateSecretCodes()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-dice"></i> تشغيل خوارزمية التشفير العشوائي</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-print"></i> طباعة ملصقات التشفير (Stickers)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم الجلوس (مخفي للعامة)</th>
                    <th>الرقم السري (Secret Code)</th>
                    <th>المادة والاختبار</th>
                    <th>الصف والشعبة</th>
                    <th>نمط التشفير</th>
                    <th>رمز لون الدفتر</th>
                    <th>تاريخ ووقت التوليد</th>
                    <th>مسؤول الكنترول</th>
                    <th>حالة التشفير</th>
                    <th>حالة فك التشفير</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-secret-numbers-grid"></tbody>
        </table>
    </div>
</div>
"""

# G. Hall Distribution & Invigilators (pg-hall-distribution)
hall_dist_html = """
<div class="page" id="pg-hall-distribution">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-users-rectangle"></i> توزيع اللجان والمراقبين والملاحظين</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('hall-distribution')"><i class="fa-solid fa-plus"></i> تكليف مراقب في لجنة</button>
        <button class="btn-add" onclick="autoDistributeProctors()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-wand-magic-sparkles"></i> التوزيع التلقائي الذكي للمراقبين</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم التكليف</th>
                    <th>اسم المراقب / الملاحظ</th>
                    <th>الدور الإشرافي</th>
                    <th>اسم / رقم اللجنة</th>
                    <th>المبنى والقاعة</th>
                    <th>المادة وتاريخ الامتحان</th>
                    <th>الفترة / الوردية</th>
                    <th>فحص النزاهة والتضارب</th>
                    <th>نصاب المراقبة</th>
                    <th>حالة الإشعار</th>
                    <th>حالة الحضور</th>
                    <th>البديل الطارئ</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-hall-distribution-grid"></tbody>
        </table>
    </div>
</div>
"""

# H. Exam Schedule (pg-exam-schedule)
exam_sched_html = """
<div class="page" id="pg-exam-schedule">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-calendar-days"></i> جدول الامتحانات الرسمية والتوقيتات</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('exam_schedule')"><i class="fa-solid fa-plus"></i> إضافة اختبار إلى الجدول</button>
        <button class="btn-add" onclick="publishExamSchedule()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-globe"></i> اعتماد ونشر الجدول لـ تطبيق الطلاب</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الجدول</th>
                    <th>العام الدراسي والفصل</th>
                    <th>المرحلة والصف</th>
                    <th>اسم المادة الدراسية</th>
                    <th>اليوم والتاريخ</th>
                    <th>الفترة / الوردية</th>
                    <th>وقت البداية والنهاية</th>
                    <th>مدة الامتحان</th>
                    <th>القاعات المخصصة</th>
                    <th>حالة النشر</th>
                    <th>تعليمات الامتحان</th>
                    <th>مسؤول الإعداد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-exam-schedule-grid"></tbody>
        </table>
    </div>
</div>
"""

# I. Roll Call Sheets (pg-roll-call)
roll_call_html = """
<div class="page" id="pg-roll-call">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-list-check"></i> كشوفات المناداة للمنادين وتوقيعات الاستلام</h2>
    </div>

    <div class="toolbar">
        <select id="rcCommitteeSelect" onchange="renderRollCallGrid()" style="width:180px;"><option value="لجنة رقم (12)">لجنة رقم (12) - القاعة A</option><option value="لجنة رقم (05)">لجنة رقم (05) - القاعة B</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشف مناداة اللجنة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم المقعد</th>
                    <th>رقم الجلوس</th>
                    <th>صورة واسم الطالب</th>
                    <th>المادة والصف</th>
                    <th>توقيع حضور الطالب</th>
                    <th>تسلسل دفتر الإجابة (Barcode)</th>
                    <th>حالة الحضور والغياب</th>
                    <th>حالة تسليم الدفتر</th>
                    <th>اسم المنادي / الملاحظ</th>
                    <th>ملاحظات محضر اللجنة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-roll-call-grid"></tbody>
        </table>
    </div>
</div>
"""

# J. Seat Cards Printing (pg-seat-cards)
seat_cards_html = """
<div class="page" id="pg-seat-cards">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-id-badge"></i> طباعة بطاقات أرقام الجلوس ومستندات الطاولات</h2>
    </div>

    <div class="toolbar">
        <select id="scLayoutSelect" style="width:180px;"><option>4 بطاقات / صفحة A4</option><option>6 بطاقات / صفحة A4</option><option>بطاقة بلاستيكية PVC فردية</option></select>
        <button class="btn-add" onclick="previewSeatCardsModal()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-eye"></i> المعاينة الحية والتأمين الرقمي</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة البطاقات المحددة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اسم الطالب الرباعي</th>
                    <th>رقم الجلوس</th>
                    <th>الصورة الشخصية</th>
                    <th>الصف / التخصص</th>
                    <th>اسم المركز والقاعة</th>
                    <th>رمز الـ QR / الباركود</th>
                    <th>جدول الامتحانات المختصر</th>
                    <th>ختم وتوقيع رئيس الكنترول</th>
                    <th>تعليمات دخول اللجنة</th>
                    <th>طباعة وطرد الحزمة</th>
                </tr>
            </thead>
            <tbody id="tbl-seat-cards-grid"></tbody>
        </table>
    </div>
</div>
"""

# K. Substitute Teachers Management (pg-substitute)
substitute_html = """
<div class="page" id="pg-substitute">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-pen"></i> إدارة المدرس البديل وحصص الاحتياط</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('substitute')"><i class="fa-solid fa-plus"></i> تكليف مدرس بديل لحصة</button>
        <button class="btn-add" onclick="autoSuggestSubstitute()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-wand-magic-sparkles"></i> محرك التوزيع الذكي للبدلاء</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>المعلم الأصلي (الغائب)</th>
                    <th>الصف والحصة والقاعة</th>
                    <th>المادة والدرس المقرر</th>
                    <th>المعلم البديل المقترح</th>
                    <th>معيار الاختيار والعدالة</th>
                    <th>حالة التكليف</th>
                    <th>محتوى التغطية</th>
                    <th>الأجر / التقييم</th>
                    <th>ملاحظات سير الحصة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-substitute-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-grading', grading_html)
html = replace_or_add_page(html, 'pg-results', results_html)
html = replace_or_add_page(html, 'pg-certificates', certificates_html)
html = replace_or_add_page(html, 'pg-exam-halls', exam_halls_html)
html = replace_or_add_page(html, 'pg-seat-numbers', seat_numbers_html)
html = replace_or_add_page(html, 'pg-secret-numbers', secret_numbers_html)
html = replace_or_add_page(html, 'pg-hall-distribution', hall_dist_html)
html = replace_or_add_page(html, 'pg-exam-schedule', exam_sched_html)
html = replace_or_add_page(html, 'pg-roll-call', roll_call_html)
html = replace_or_add_page(html, 'pg-seat-cards', seat_cards_html)
html = replace_or_add_page(html, 'pg-substitute', substitute_html)

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

print("Control & Exam HTML update completed successfully!")
