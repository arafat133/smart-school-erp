"""
Python script to update/re-architect Activities & Transportation modules in school.html:
- pg-activities (إدارة الأنشطة والأنواع)
- pg-transport-routes (دليل خطوط السير)
- pg-buses (دليل الحافلات والمركبات)
- pg-transport-enrollment (اشتراك الطلاب في المواصلات)
- pg-transport (كشوفات ورسومات المواصلات)
"""
import re, time

print("=" * 60)
print("Updating Activities & Transportation Modules in school.html...")
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

# 1. Activities Management (pg-activities)
activities_html = """
<div class="page" id="pg-activities">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-medal"></i> إدارة الأنشطة والأنواع والتخطيط والرسوم</h2>
    </div>

    <!-- Stats KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي الأنشطة المفتوحة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">12 نشاطاً</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>الطلاب المشاركون</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">185 طالباً</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>إجمالي الميزانيات المعتمدة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">4,500 $</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('activities')"><i class="fa-solid fa-plus"></i> إضافة وتخطيط نشاط جديد</button>
        <select id="actTypeFilter" onchange="renderActivitiesGrid()" style="width:170px;">
            <option value="all">جميع التصنيفات</option>
            <option value="نشاط علمي / تكنولوجي">نشاط علمي / تكنولوجي</option>
            <option value="نشاط رياضي">نشاط رياضي</option>
            <option value="رحلة ميدانية">رحلة ميدانية</option>
        </select>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود النشاط</th>
                    <th>اسم النشاط</th>
                    <th>تصنيف النشاط</th>
                    <th>المشرف المسؤول</th>
                    <th>السعة الاستيعابية</th>
                    <th>الفئة المستهدفة</th>
                    <th>النطاق الزمني</th>
                    <th>مكان التنفيذ</th>
                    <th>رسوم الاشتراك</th>
                    <th>الميزانية المعتمدة</th>
                    <th>حالة النشاط</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-activities-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Transport Routes Directory (pg-transport-routes)
routes_html = """
<div class="page" id="pg-transport-routes">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-route"></i> دليل خطوط السير والمسارات والمحطات</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('transport-routes')"><i class="fa-solid fa-plus"></i> إضافة خط سير جديد</button>
        <button class="btn-add" onclick="openRouteMapModal()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-map-location-dot"></i> الخريطة التفاعلية للمسارات</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الخط</th>
                    <th>اسم الخط والحي</th>
                    <th>نقطة البداية والنهاية</th>
                    <th>عدد محطات التوقف</th>
                    <th>الحافلة المخصصة</th>
                    <th>طاقم الحافلة (سائق/مشرفة)</th>
                    <th>زمن الرحلة التقديري</th>
                    <th>مواعيد الانطلاق</th>
                    <th>رسوم الاشتراك</th>
                    <th>الطاقة الاستيعابية والمقاعد</th>
                    <th>حالة الخط</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-transport-routes-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. Buses & Fleet Management (pg-buses)
buses_html = """
<div class="page" id="pg-buses">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-bus-simple"></i> دليل أسطول الحافلات والمركبات والسلامة</h2>
    </div>

    <!-- Fleet Status KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>الحافلات النشطة في الخدمة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">8 حافلات</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>قيد الصيانة والفحص</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">1 حافلة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>أجهزة التتبع GPS المتصلة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">9 / 9 أجهزة (Online)</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('buses')"><i class="fa-solid fa-plus"></i> إضافة حافلة / مركبة جديدة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الحافلة</th>
                    <th>رقم اللوحة المعدنية</th>
                    <th>الماركة والموديل</th>
                    <th>السعة الاستيعابية</th>
                    <th>نوع الوقود والمحرك</th>
                    <th>خط السير المسند</th>
                    <th>طاقم الحافلة المكلف</th>
                    <th>عداد الكيلومترات</th>
                    <th>صلاحية الترخيص والتأمين</th>
                    <th>تجهيزات الأمان والـ GPS</th>
                    <th>الحالة التشغيلية</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-buses-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Student Transport Enrollment (pg-transport-enrollment)
enrollment_html = """
<div class="page" id="pg-transport-enrollment">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-user-check"></i> اشتراك الطلاب في المواصلات وتوليد بطاقة الحافلة</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('transport-enrollment')"><i class="fa-solid fa-plus"></i> تسجيل اشتراك طالب في المواصلات</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كرت الحافلة (Bus Pass)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الاشتراك</th>
                    <th>بيانات الطالب والأكاديمي</th>
                    <th>خط السير المحدد</th>
                    <th>محطة التوقف والركوب</th>
                    <th>نوع الاشتراك</th>
                    <th>الحافلة والمشرفة</th>
                    <th>رسوم الخدمة</th>
                    <th>حالة السداد المالي</th>
                    <th>حالة الاشتراك</th>
                    <th>كود صعود الحافلة (QR)</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-transport-enrollment-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Transport Manifests & Analytics (pg-transport)
transport_html = """
<div class="page" id="pg-transport">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-map-location-dot"></i> كشوفات ركاب المواصلات والتحصيل المالي والخرائط</h2>
    </div>

    <!-- Occupancy KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>نسبة إشغال مقاعد أسطول النقل</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">82.5% (198/240 مقعد)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي التحصيل المالي للمواصلات</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">32,400 $</p></div>
        </div>
    </div>

    <div class="toolbar">
        <select id="trRouteSelect" onchange="renderTransportManifestGrid()" style="width:200px;"><option value="ROUTE-0103">خط حدة - الأصبحي ( حافلة 08 )</option></select>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشف ركاب الحافلة اليومي (PDF)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود التقرير</th>
                    <th>اسم الخط والحافلة</th>
                    <th>نوع الكشف</th>
                    <th>بيانات الطالب</th>
                    <th>محطة الصعود / النزول</th>
                    <th>إجمالي الرسم المالي</th>
                    <th>المحصل والمتبقي</th>
                    <th>حالة السداد المالي</th>
                    <th>نسبة إشغال المقاعد</th>
                    <th>طاقم الرحلة والتوقيع</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-transport-manifest-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-activities', activities_html)
html = replace_or_add_page(html, 'pg-transport-routes', routes_html)
html = replace_or_add_page(html, 'pg-buses', buses_html)
html = replace_or_add_page(html, 'pg-transport-enrollment', enrollment_html)
html = replace_or_add_page(html, 'pg-transport', transport_html)

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

print("Activities & Transport HTML update completed successfully!")
