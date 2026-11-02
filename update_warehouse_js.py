"""
Python script to append Warehouse & Purchasing logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Warehouse & Purchasing Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

wh_db_additions = """
// Data collections for Warehouse & Purchasing modules
if (!DB.itemCategoriesGridData) DB.itemCategoriesGridData = [
    { code: 'CAT-IT-002', name: 'أجهزة ومستلزمات المعامل الرقمية', parent: 'الأصول والتجهيزات التقنية', uom: 'قطعة / جهاز', valuation: 'الوارد أولاً يصرف أولاً (FIFO)', reorder: 10, nature: 'أصل ثابت (Asset)', depRate: '15% سنوياً', glAccount: 'مخزون الأجهزة الرقمية (120401)', status: 'نشطة (Active)' },
    { code: 'CAT-STAT-001', name: 'القرطاسية والمستلزمات المكتبية', parent: 'المواد الاستهلاكية', uom: 'باكيت / كرتون', valuation: 'المتوسط الموزون', reorder: 50, nature: 'صنف استهلاكي', depRate: '0%', glAccount: 'مخزون القرطاسية (120502)', status: 'نشطة (Active)' }
];

if (!DB.inventoryItemsGridData) DB.inventoryItemsGridData = [
    { sku: 'SKU-LAP-2026-001', name: 'حاسوب محمول للمعامل الرقمية Dell XPS 15', category: 'الأجهزة الرقمية -> أجهزة محمول', barcode: '6291100293812', uomConv: 'شراء: كرتون (24 قطعة) | صرف: قطعة', limits: 'إعادة الطلب: 5 | الأقصى: 30 قطعة', avgCost: 850, sellRate: 950, location: 'المخزن الرئيسي - الرف B-04', status: 'نشط (Active)' },
    { sku: 'SKU-PAP-2026-004', name: 'ورق طباعة A4 فاخر (80 جرام)', category: 'القرطاسية -> الأوراق', barcode: '6291100293899', uomConv: 'شراء: كرتون (5 رزمة) | صرف: رزمة', limits: 'إعادة الطلب: 20 | الأقصى: 100 رزمة', avgCost: 4, sellRate: 5, location: 'المخزن الفرعي - الرف A-01', status: 'نشط (Active)' }
];

if (!DB.supplyOrdersGridData) DB.supplyOrdersGridData = [
    { grnNo: 'GRN-2026-0415', poRef: 'PO-2026-0089', supplier: 'شركة التقنية المتقدمة - فاتورة (8821)', warehouse: 'المخزن الرئيسي - الأجهزة الرقمية', receiptTime: '2026-08-08 10:30 AM', itemsQty: 'حاسوب محمول (مطلوب 10 / مستلم 10)', inspection: 'مقبول بالكامل', rejected: '0 قطعة', receivedBy: 'أ. إبراهيم العنسي (أمين المخزن)', status: 'مُرحّل (Posted)' }
];

if (!DB.suppliersGridData) DB.suppliersGridData = [
    { code: 'SUP-2026-012', name: 'شركة التقنية المتقدمة للمستلزمات', category: 'تجهيزات تقنية - أجهزة حاسوب ومعامل', rating: 'مورد معتمد ممتاز (Grade A - 94%)', taxCr: 'س.ت: 101088492 | ضريبي: 30048291', contact: 'م. أحمد السالمي (0501234567 - info@tech.com)', terms: 'آجل (Credit) - سداد خلال 30 يوماً', limit: 50000, balance: '12,500 $ (دائن - مستحق)', status: 'معتمد (Active)' }
];

if (!DB.inventoryReportsGridData) DB.inventoryReportsGridData = [
    { stkId: 'STK-2026-004', warehouse: 'المخزن الرئيسي - قاعة الأصول', dateType: '2026-08-31 - جرد دوري ربع سنوي', itemBarcode: 'حاسوب محمول Dell (SKU-LAP-2026-001)', bookQty: 25, physQty: 23, varianceQty: '-2 قطعة (عجز)', varianceVal: '-1,700 $ (خسارة فروقات)', adjStatus: 'تمت التسوية (قيد ADJ-102)', valuation: '45,800 $ (المتوسط الموزون)', committee: 'أ. إبراهيم العنسي + م. خالد' }
];
"""

wh_modules_js = """

// ==================== 1. ITEM CATEGORIES ====================
function renderItemCategoriesGrid() {
    const tb = document.getElementById('tbl-item-categories-grid');
    if (!tb) return;

    const list = DB.itemCategoriesGridData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.code}</td>
            <td style="font-weight:700;">${c.name}</td>
            <td>${c.parent}</td>
            <td>${c.uom}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${c.valuation}</span></td>
            <td style="font-weight:700;color:#f59e0b;">${c.reorder} قطعة</td>
            <td>${c.nature}</td>
            <td style="color:#ef4444;">${c.depRate}</td>
            <td style="font-size:0.83rem;">${c.glAccount}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${c.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('item-categories', ${JSON.stringify(c).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}

function toggleCategoryTreeView() {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;

    title.innerHTML = '<i class="fa-solid fa-sitemap"></i> شجرة التصنيفات والمخزون متعددة المستويات (Category Tree)';
    fields.innerHTML = `
        <div style="background:rgba(15,23,42,0.9);border:1px solid rgba(59,130,246,0.3);padding:15px;border-radius:12px;color:#fff;margin-bottom:12px;font-size:0.9rem;">
            <div style="font-weight:700;color:#60a5fa;margin-bottom:8px;">📁 الأصول والتجهيزات التقنية (CAT-ASSET)</div>
            <div style="padding-right:20px;display:flex;flex-direction:column;gap:6px;">
                <div>└─ 📁 أجهزة ومستلزمات المعامل الرقمية (CAT-IT-002)</div>
                <div style="padding-right:20px;">└─ 💻 أجهزة الحاسوب المحمولة (Laptops) - [24 صنف]</div>
                <div style="padding-right:20px;">└─ 🖥️ أجهزة الحاسوب المكتبية (Desktops) - [18 صنف]</div>
                <div>└─ 📁 القرطاسية والمستلزمات المكتبية (CAT-STAT-001)</div>
            </div>
        </div>
        <button class="btn-cancel" onclick="document.getElementById('formModal').classList.remove('active');" style="width:100%;"><i class="fa-solid fa-xmark"></i> إغلاق الشجرة</button>
    `;
    document.getElementById('formModal').classList.add('active');
}


// ==================== 2. INVENTORY ITEMS ====================
function renderInventoryItemsGrid() {
    const tb = document.getElementById('tbl-inventory-items-grid');
    if (!tb) return;

    const list = DB.inventoryItemsGridData || [];
    tb.innerHTML = list.map(i => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${i.sku}</td>
            <td style="font-weight:700;">${i.name}</td>
            <td>${i.category}</td>
            <td style="font-weight:700;color:#38bdf8;"><i class="fa-solid fa-barcode"></i> ${i.barcode}</td>
            <td style="font-size:0.8rem;">${i.uomConv}</td>
            <td style="font-size:0.8rem;color:#fbbf24;font-weight:700;">${i.limits}</td>
            <td style="font-weight:800;color:#34d399;">${i.avgCost.toLocaleString()} $</td>
            <td style="font-weight:800;color:#60a5fa;">${i.sellRate.toLocaleString()} $</td>
            <td style="font-size:0.83rem;">${i.location}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${i.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('inventory-items', ${JSON.stringify(i).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 3. SUPPLY ORDERS / GRN ====================
function renderSupplyOrdersGrid() {
    const tb = document.getElementById('tbl-supply-orders-grid');
    if (!tb) return;

    const list = DB.supplyOrdersGridData || [];
    tb.innerHTML = list.map(g => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${g.grnNo}</td>
            <td style="font-weight:700;color:#c084fc;">${g.poRef}</td>
            <td style="font-weight:700;">${g.supplier}</td>
            <td>${g.warehouse}</td>
            <td style="font-size:0.8rem;">${g.receiptTime}</td>
            <td style="font-size:0.83rem;">${g.itemsQty}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${g.inspection}</span></td>
            <td style="color:#ef4444;font-weight:700;">${g.rejected}</td>
            <td style="font-size:0.8rem;">${g.receivedBy}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${g.status}</span></td>
            <td><button class="btn-edit" onclick="toast('معاينة إذن التوريد والترحيل PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}

function postGRNToInventory() {
    toast('⚡ جاري ترحيل كميات أذونات التوريد المقبولة للمخزون الفعلي وتوليد القيد...');
    setTimeout(() => { renderSupplyOrdersGrid(); toast('✅ تم ترحيل إذن التوريد للمخزون والقيد المحاسبي بنجاح!'); }, 700);
}


// ==================== 4. SUPPLIERS DIRECTORY ====================
function renderSuppliersGrid() {
    const tb = document.getElementById('tbl-suppliers-grid');
    if (!tb) return;

    const list = DB.suppliersGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.code}</td>
            <td style="font-weight:700;">${s.name}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${s.category}</span></td>
            <td style="color:#10b981;font-weight:700;">${s.rating}</td>
            <td style="font-size:0.8rem;">${s.taxCr}</td>
            <td style="font-size:0.8rem;">${s.contact}</td>
            <td>${s.terms}</td>
            <td style="font-weight:800;color:#60a5fa;">${s.limit.toLocaleString()} $</td>
            <td style="font-weight:800;color:#fbbf24;">${s.balance}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${s.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('suppliers', ${JSON.stringify(s).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 5. INVENTORY REPORTS & STOCKTAKE ====================
function renderInventoryReportsGrid() {
    const tb = document.getElementById('tbl-inventory-reports-grid');
    if (!tb) return;

    const list = DB.inventoryReportsGridData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.stkId}</td>
            <td>${r.warehouse}</td>
            <td style="font-size:0.8rem;">${r.dateType}</td>
            <td style="font-weight:700;">${r.itemBarcode}</td>
            <td style="font-weight:700;">${r.bookQty} قطعة</td>
            <td style="font-weight:700;color:#34d399;">${r.physQty} قطعة</td>
            <td style="color:#ef4444;font-weight:800;">${r.varianceQty}</td>
            <td style="color:#ef4444;font-weight:800;">${r.varianceVal}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${r.adjStatus}</span></td>
            <td style="font-weight:800;color:#60a5fa;">${r.valuation}</td>
            <td style="font-size:0.8rem;">${r.committee}</td>
            <td><button class="btn-edit" onclick="toast('معاينة محضر الجرد والتسوية PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}
"""

if 'WAREHOUSE & PURCHASING MODULES' not in js:
    js += wh_db_additions + "\n" + wh_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Warehouse & Purchasing logic in app.js successfully!")
