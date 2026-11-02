# 🏛️ دليل نظام التصميم المعياري (Smart School ERP Design System)

تم توحيد واعتماد التصميم الزجاجي العصري (Modern Glassmorphism UI) ليكون هو المعيار الثابت في كافة واجهات النظام (105+ واجهة).

---

## 📐 الهيكل المعياري لكل صفحة داخل النظام:

```html
<div class="page" id="pg-example">
    <!-- 1. الترويسة القياسية -->
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-icon-name"></i> عنوان الصفحة بالعربية (English Title)</h2>
    </div>

    <!-- 2. بطاقات المؤشرات (KPIs) -->
    <div class="stats-row">
        <div class="stat-card" style="border-right: 4px solid #3b82f6;">
            <div class="stat-info">
                <h3><i class="fa-solid fa-users"></i> إجمالي السجلات</h3>
                <p id="kpiTotal">0</p>
                <small>الوصف الإحصائي</small>
            </div>
        </div>
    </div>

    <!-- 3. شريط الأدوات والعمليات -->
    <div class="toolbar">
        <div class="search-box">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input id="searchExample" placeholder="بحث...">
        </div>
        <div class="toolbar-actions">
            <button class="btn-add" onclick="openForm('example')"><i class="fa-solid fa-plus"></i> إضافة جديد</button>
            <button class="btn-add btn-print" onclick="triggerOfficialPrint()"><i class="fa-solid fa-print"></i> طباعة</button>
        </div>
    </div>

    <!-- 4. جدول عرض البيانات -->
    <div class="table-wrapper">
        <table class="data-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>الاسم</th>
                    <th>الحالة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-example-grid"></tbody>
        </table>
    </div>
</div>
```

---

## 🔒 كيف يضمن النظام ثبات التصميم حتى لو عُدلت الصفحة؟
1. **قواعد CSS شاملة ودفاعية (Defensive CSS Rules):** تم برمجة `main.css` بحيث يفرض التصميم الزجاجي والمحاذاة والظلال والألوان تلقائياً على كل عنصر داخل `.page` حتى لو كتب المطور HTML بسيطاً.
2. **قوالب الماكرو الجاهزة (`templates/partials/_ui_macros.html`):** تتيح توليد الترويسة والبطاقات وشريط الأدوات بأسطر Jinja2 قصيرة وثابتة.
3. **تدرج الألوان المعتمد:**
   * 🔵 **الأزرق (#3b82f6):** للإحصائيات العامة والروابط الأساسية.
   * 🟢 **الأخضر (#10b981):** للعمليات الإيجابية، السجلات النشطة، والإضافات.
   * 🔴 **الأحمر (#ef4444):** للتنبيهات، المعطلين، والحذف.
   * 🟡 **الكهرماني (#f59e0b):** للحالات المعلقة وقيد المراجعة.
