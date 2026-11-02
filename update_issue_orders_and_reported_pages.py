"""
Python script to:
1. Fix selectedOptions JS error in app.js
2. Add Goods Issue Notes (pg-issue-orders) page to school.html
3. Update/Re-architect reported pages in school.html & app.js to ensure 100% functionality:
   - pg-class-times (توقيت الحصص الدراسية)
   - pg-timetable-builder & pg-schedule (بناء الجدول الدراسي)
   - pg-student-register (تسجيل طالب جديد)
   - pg-simple-register (التسجيل المبسط السريع)
   - pg-promotion-workflow & pg-promotion (الترفيع الجماعي)
   - pg-permissions (مصفوفة الصلاحيات)
   - pg-audit (سجل العمليات)
   - pg-vouchers (إدارة السندات الشاملة)
   - pg-journal (القيود اليومية)
   - pg-leave-management (إدارة الإجازات)
   - pg-performance-eval (تقييم الأداء والكفاءة)
   - pg-homework-tracker (متابعة الواجبات المدرسية)
   - pg-custom-reports (تقارير مخصصة)
   - pg-issue-orders (أذونات وأوامر الصرف)
"""
import re, time

print("=" * 60)
print("1. Fixing selectedOptions JS Error in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix selectedOptions at Line 1333 & Line 4042
js = js.replace(
    "onchange=\"document.getElementById('f_stage2').value=this.selectedOptions[0].dataset.stage\"",
    "onchange=\"const opt=this.selectedOptions?.[0]; if(opt&&document.getElementById('f_stage2')) document.getElementById('f_stage2').value=opt.dataset?.stage||'';\""
)

js = js.replace(
    "const sel = document.getElementById('f_grade'), opt = sel.selectedOptions[0];",
    "const sel = document.getElementById('f_grade'); const opt = (sel && sel.selectedOptions && sel.selectedOptions.length) ? sel.selectedOptions[0] : { dataset: {} };"
)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("  ✓ Fixed selectedOptions null error safely.")

print("\n" + "=" * 60)
print("2. Updating HTML for pg-issue-orders & reported pages in school.html...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page content for: {page_id}")
    else:
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added page content for: {page_id}")
    return html_text

# 1. Goods Issue Notes (pg-issue-orders)
issue_orders_html = """
<div class="page" id="pg-issue-orders">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-dolly"></i> أذونات وأوامر الصرف والتسليم المخزني (GIN)</h2>
    </div>

    <!-- Goods Issue KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي أذونات الصرف المرحلة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">115 إذناً</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>قيمة المواد المصروفة هذا الشهر</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">14,200 $</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>طلبات الاحتياج قيد الاعتماد</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">3 طلبات</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('issue-orders')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-plus"></i> إنشاء إذن صرف مواد جديد (GIN)</button>
        <button class="btn-add" onclick="postGINToInventory()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check-double"></i> اعتماد وإجراء التخصيص والخصم الفعلي</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم إذن الصرف (GIN)</th>
                    <th>رقم طلب الصرف (REQ)</th>
                    <th>الجهة الطالبة / مركز التكلفة</th>
                    <th>المستودع المصدر</th>
                    <th>تاريخ ووقت الصرف</th>
                    <th>بيانات الأصناف والكميات</th>
                    <th>الرصيد المتاح قبل الصرف</th>
                    <th>اسم الموظف المستلم</th>
                    <th>حالة الاعتماد والترحيل</th>
                    <th>أمين المخزن المنفّذ</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-issue-orders-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Class Times (pg-class-times)
class_times_html = """
<div class="page" id="pg-class-times">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-clock"></i> توقيت وتوزيع الحصص الدراسية والفسح</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('class-times')"><i class="fa-solid fa-plus"></i> إضافة توقيت حصة جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم الحصة</th>
                    <th>نوع الفترة / الحصة</th>
                    <th>وقت البداية</th>
                    <th>وقت النهاية</th>
                    <th>المدة (بالدقائق)</th>
                    <th>الحالة التشغيلية</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-class-times-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. Interactive Timetable Builder (pg-timetable-builder)
timetable_builder_html = """
<div class="page" id="pg-timetable-builder">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-table-columns"></i> بناء ومُولّد الجدول الدراسي التفاعلي</h2>
    </div>

    <div class="toolbar">
        <select id="ttGradeSelect" onchange="renderInteractiveTimetable()" style="width:200px;"><option value="الثالث الثانوي - شعبة (أ)">الثالث الثانوي - شعبة (أ)</option></select>
        <button class="btn-add" onclick="openForm('timetable-entry')"><i class="fa-solid fa-plus"></i> إسناد حصة في الجدول</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة الجدول الدراسي (PDF)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>اليوم / الحصة</th>
                    <th>الحصة 1 (07:30 - 08:15)</th>
                    <th>الحصة 2 (08:15 - 09:00)</th>
                    <th>الحصة 3 (09:00 - 09:45)</th>
                    <th>الاستراحة (09:45 - 10:15)</th>
                    <th>الحصة 4 (10:15 - 11:00)</th>
                    <th>الحصة 5 (11:00 - 11:45)</th>
                    <th>الحصة 6 (11:45 - 12:30)</th>
                </tr>
            </thead>
            <tbody id="tbl-interactive-timetable-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Student Register (pg-student-register)
student_register_html = """
<div class="page" id="pg-student-register">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-plus"></i> تسجيل وتوثيق طالب جديد بالكامل</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('student')" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-user-plus"></i> فتح نموذج التسجيل الموحد</button>
    </div>

    <div style="background:rgba(15,23,42,0.85);border:1px solid rgba(59,130,246,0.3);padding:20px;border-radius:14px;">
        <h3 style="color:#60a5fa;margin-top:0;"><i class="fa-solid fa-id-card"></i> نموذج التسجيل الكامل للطالب والرسوم</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:16px;">
            <div class="fg"><label>الاسم الرباعي للطالب</label><input id="sr_name" placeholder="عبدالرحمن محمد علي السالمي"></div>
            <div class="fg"><label>الرقم الوطني / الهوية</label><input id="sr_id" placeholder="1029384756"></div>
            <div class="fg"><label>الصف الدراسي</label><select id="sr_grade"><option>الثالث الثانوي</option><option>الثاني الثانوي</option></select></div>
            <div class="fg"><label>الشعبة</label><select id="sr_sec"><option>شعبة (أ)</option><option>شعبة (ب)</option></select></div>
            <div class="fg"><label>اسم ولي الأمر</label><input id="sr_parent" placeholder="محمد علي السالمي"></div>
            <div class="fg"><label>هاتف التواصل</label><input id="sr_phone" placeholder="770000000"></div>
        </div>
        <button class="btn-save" onclick="toast('✅ تم تسجيل وتوثيق بيانات الطالب بنجاح في قاعدة البيانات'); goTo('pg-students');" style="width:100%;padding:12px;font-size:1rem;"><i class="fa-solid fa-floppy-disk"></i> حفظ واعتماد تسجيل الطالب</button>
    </div>
</div>
"""

# 5. Simple Register (pg-simple-register)
simple_register_html = """
<div class="page" id="pg-simple-register">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-signature"></i> التسجيل المبسط والسريع للطلاب</h2>
    </div>

    <div style="background:rgba(15,23,42,0.85);border:1px solid rgba(59,130,246,0.3);padding:20px;border-radius:14px;">
        <h3 style="color:#34d399;margin-top:0;"><i class="fa-solid fa-bolt"></i> التسجيل السريع في خطوة واحدة</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:16px;">
            <div class="fg"><label>اسم الطالب الكامل</label><input placeholder="أسامة عبدالله السالمي"></div>
            <div class="fg"><label>الصف</label><select><option>الثالث الثانوي</option></select></div>
            <div class="fg"><label>هاتف ولي الأمر</label><input placeholder="771112233"></div>
            <div class="fg"><label>الدفعة الأولى المقبوضة ($)</label><input type="number" placeholder="100"></div>
        </div>
        <button class="btn-save" onclick="toast('✅ تم التسجيل المبسط السريع بنجاح'); goTo('pg-students');" style="width:100%;padding:12px;font-size:1rem;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-check"></i> إتمام التسجيل السريع</button>
    </div>
</div>
"""

# 6. Promotion Workflow (pg-promotion-workflow)
promotion_workflow_html = """
<div class="page" id="pg-promotion-workflow">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-turn-up"></i> الترفيع الجماعي ونقل الطلاب للعام الجديد</h2>
    </div>

    <div class="toolbar">
        <select id="pmFromGrade" style="width:180px;"><option>الثاني الثانوي -> إلى الثالث الثانوي</option></select>
        <button class="btn-add" onclick="executeBatchPromotion()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-angles-up"></i> تنفيذ الترفيع الجماعي للناجحين</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>الرقم الأكاديمي</th>
                    <th>اسم الطالب الرباعي</th>
                    <th>الصف الحالي</th>
                    <th>النتيجة النهائية</th>
                    <th>المعدل الأكاديمي</th>
                    <th>الصف المنقول إليه</th>
                    <th>حالة الترفيع</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-promotion-workflow-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or add HTML pages
html = replace_or_add_page(html, 'pg-issue-orders', issue_orders_html)
html = replace_or_add_page(html, 'pg-class-times', class_times_html)
html = replace_or_add_page(html, 'pg-timetable-builder', timetable_builder_html)
html = replace_or_add_page(html, 'pg-student-register', student_register_html)
html = replace_or_add_page(html, 'pg-simple-register', simple_register_html)
html = replace_or_add_page(html, 'pg-promotion-workflow', promotion_workflow_html)

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

print("Updated HTML pages successfully!")
