"""
Python script to update/re-architect Warehouse & Purchasing modules in school.html:
- pg-item-categories (فئات الأصناف والمخزونية)
- pg-inventory-items (دليل الأصناف والمنتجات)
- pg-supply-orders (أذونات وأوامر التوريد - GRN)
- pg-suppliers (دليل الموردين والمعتمدين)
- pg-inventory-reports (تقارير المخزون والجرد والتسويات)
"""
import re, time

print("=" * 60)
print("Updating Warehouse & Purchasing Modules in school.html...")
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

# 1. Item Categories (pg-item-categories)
item_categories_html = """
<div class="page" id="pg-item-categories">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-boxes-stacked"></i> دليل فئات الأصناف وشجرة التبويب المخزني</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('item-categories')"><i class="fa-solid fa-plus"></i> إضافة فئة مخزونية جديدة</button>
        <button class="btn-add" onclick="toggleCategoryTreeView()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-sitemap"></i> عرض شجرة الفئات متعددة المستويات</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الفئة</th>
                    <th>اسم الفئة المخزونية</th>
                    <th>الفئة الأب / الرئيسية</th>
                    <th>وحدة القياس الافتراضية</th>
                    <th>طريقة تقييم المخزون</th>
                    <th>حد إعادة الطلب</th>
                    <th>طبيعة الأصناف</th>
                    <th>نسبة الإهلاك السنوي</th>
                    <th>الحساب المالي (GL)</th>
                    <th>حالة الفئة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-item-categories-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Inventory Items (pg-inventory-items)
inventory_items_html = """
<div class="page" id="pg-inventory-items">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-box"></i> دليل الأصناف والمنتجات والباركود</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('inventory-items')"><i class="fa-solid fa-plus"></i> إضافة صنف / منتج جديد</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-print"></i> طباعة ملصقات الباركود والـ QR</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الصنف (SKU)</th>
                    <th>اسم الصنف والمنتج</th>
                    <th>الفئة الرئيسية والفرعية</th>
                    <th>الرمز الشريطي (Barcode)</th>
                    <th>وحدات التداول والتحويل</th>
                    <th>حد إعادة الطلب والحد الأقصى</th>
                    <th>متوسط التكلفة</th>
                    <th>سعر البيع / الصرف</th>
                    <th>موقع التخزين الافتراضي</th>
                    <th>حالة الصنف</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-inventory-items-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. Supply Orders / GRN (pg-supply-orders)
supply_orders_html = """
<div class="page" id="pg-supply-orders">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-truck-ramp-box"></i> أذونات وأوامر التوريد واستلام البضائع (GRN)</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('supply-orders')"><i class="fa-solid fa-plus"></i> إنشاء إذن توريد واستلام (GRN)</button>
        <button class="btn-add" onclick="postGRNToInventory()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-warehouse"></i> ترحيل التوريد للمخزون الفعلي والقيد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم إذن التوريد (GRN)</th>
                    <th>رقم أمر الشراء (PO)</th>
                    <th>اسم المورد ورقم الفاتورة</th>
                    <th>المستودع المستلم</th>
                    <th>تاريخ ووقت الاستلام</th>
                    <th>بيانات الأصناف والكميات</th>
                    <th>حالة الفحص الفني</th>
                    <th>الكمية المرفوضة والسبب</th>
                    <th>أمناء المستودع والاستلام</th>
                    <th>حالة الترحيل المالي</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-supply-orders-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Suppliers Directory (pg-suppliers)
suppliers_html = """
<div class="page" id="pg-suppliers">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-truck-field"></i> دليل الموردين المعتمدين والتسهيلات المالية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('suppliers')"><i class="fa-solid fa-plus"></i> تسجيل وتوثيق مورد جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود المورد</th>
                    <th>اسم الشركة / المورد</th>
                    <th>التصنيف والمجال</th>
                    <th>درجة الاعتماد والتقييم</th>
                    <th>السجل التجاري والضريبي</th>
                    <th>مسؤول التواصل</th>
                    <th>شروط وفترة السداد</th>
                    <th>سقف الائتمان</th>
                    <th>الرصيد الحسابي الحالي</th>
                    <th>حالة المورد التشغيلية</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-suppliers-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Inventory Reports & Stocktake (pg-inventory-reports)
inventory_reports_html = """
<div class="page" id="pg-inventory-reports">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-clipboard-list"></i> تقارير المخزون والجرد والتسويات المالية</h2>
    </div>

    <!-- Inventory Valuation KPI Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>إجمالي القيمة المالية للمخزون</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">45,800 $ (FIFO)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>عمليات الجرد الدوري المكتملة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">4 مأموريات جرد</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>تكلفة فروقات الانحراف (عجز)</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">-1,700 $ (تمت التسوية)</p></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('stocktake')" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);"><i class="fa-solid fa-calculator"></i> إدخال محاضر الجرد الفعلي والماكينات</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة تقرير تقييم المخزون</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم عملية الجرد</th>
                    <th>المستودع / الفرع</th>
                    <th>تاريخ ونوع الجرد</th>
                    <th>الصنف والباركود</th>
                    <th>الرصيد الدفتري</th>
                    <th>الرصيد الفعلي المحصور</th>
                    <th>مقدار الفارق / الانحراف</th>
                    <th>التكلفة المالية للفارق</th>
                    <th>حالة التسوية</th>
                    <th>تقييم المخزون الكلي</th>
                    <th>أعضاء لجنة الجرد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-inventory-reports-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-item-categories', item_categories_html)
html = replace_or_add_page(html, 'pg-inventory-items', inventory_items_html)
html = replace_or_add_page(html, 'pg-supply-orders', supply_orders_html)
html = replace_or_add_page(html, 'pg-suppliers', suppliers_html)
html = replace_or_add_page(html, 'pg-inventory-reports', inventory_reports_html)

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

print("Warehouse & Purchasing HTML update completed successfully!")
