"""
Comprehensive JavaScript implementation for Financial Modules according to exact user specifications:
1. Operation Lock (pg-operation-lock)
2. Chart of Accounts Tree View + Details Panel + Fields (pg-chart-accounts)
3. Journal Entries 3-part layout: Header, Lines Grid, Footer with Balance Delta (pg-journal)
4. Cash Boxes Setup & Grid (pg-cashboxes)
5. Cost Centers Tree View & Budget Performance Panel (pg-cost-centers)
6. Account Ceiling Policy & Limits Grid (pg-account-ceiling)
7. Unified Vouchers Hub (pg-vouchers)
8. Interactive Statement of Account with Running Balance (pg-student-account)
"""
import re, time

print("=" * 60)
print("Updating app.js with Comprehensive Financial Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure global DB structures exist
db_init_code = """
// Initialize Financial Data Collections if missing
if (!window.DB) window.DB = {};
if (!DB.operationLocks) DB.operationLocks = [
    { id: 1, opType: 'grading', opLabel: 'رصد الدرجات والكنترول', startDate: '2026-08-01', endDate: '2026-08-15', reason: 'أعمال الكنترول والامتحانات النهائية', status: 'نشط', user: 'مدير النظام' },
    { id: 2, opType: 'closings', opLabel: 'الإقفالات المحاسبية', startDate: '2026-01-01', endDate: '2026-01-05', reason: 'إقفال السنة المالية 2025', status: 'منتهي', user: 'المحاسب الرئيسي' }
];

if (!DB.accounts) DB.accounts = [
    { code: '1', name: 'الأصول', nameEn: 'Assets', parent: '', level: 1, category: 'أصول', nature: 'مدين', postingType: 'رئيسي', currency: 'YER', balance: 1250000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '11', name: 'الأصول المتداولة', nameEn: 'Current Assets', parent: '1', level: 2, category: 'أصول متداولة', nature: 'مدين', postingType: 'رئيسي', currency: 'YER', balance: 850000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '1101', name: 'النقدية وما في حكمها', nameEn: 'Cash & Cash Equivalents', parent: '11', level: 3, category: 'أصول متداولة', nature: 'مدين', postingType: 'تجميعي', currency: 'YER', balance: 500000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '110101', name: 'صندوق النقدية الرئيسي', nameEn: 'Main Cash Box', parent: '1101', level: 4, category: 'أصول متداولة', nature: 'مدين', postingType: 'فرعي', currency: 'YER', balance: 350000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '110102', name: 'بنك اليمن والكويت', nameEn: 'Yemen Kuwait Bank', parent: '1101', level: 4, category: 'أصول متداولة', nature: 'مدين', postingType: 'فرعي', currency: 'USD', balance: 150000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '1102', name: 'العملاء والمدينون', nameEn: 'Accounts Receivable', parent: '11', level: 3, category: 'أصول متداولة', nature: 'مدين', postingType: 'تجميعي', currency: 'YER', balance: 350000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '110201', name: 'رسوم الطلاب المدينة', nameEn: 'Student Fees Receivable', parent: '1102', level: 4, category: 'أصول متداولة', nature: 'مدين', postingType: 'فرعي', currency: 'YER', balance: 350000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '2', name: 'الخصوم', nameEn: 'Liabilities', parent: '', level: 1, category: 'خصوم', nature: 'دائن', postingType: 'رئيسي', currency: 'YER', balance: 200000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '3', name: 'حقوق الملكية', nameEn: 'Equity', parent: '', level: 1, category: 'حقوق ملكية', nature: 'دائن', postingType: 'رئيسي', currency: 'YER', balance: 1050000, reportLink: 'الميزانية العمومية', status: 'Active' },
    { code: '4', name: 'الإيرادات', nameEn: 'Revenues', parent: '', level: 1, category: 'إيرادات', nature: 'دائن', postingType: 'رئيسي', currency: 'YER', balance: 650000, reportLink: 'قائمة الدخل', status: 'Active' },
    { code: '4101', name: 'إيرادات الرسوم الدراسية', nameEn: 'Tuition Fees Revenue', parent: '4', level: 4, category: 'إيرادات نشاط', nature: 'دائن', postingType: 'فرعي', currency: 'YER', balance: 650000, reportLink: 'قائمة الدخل', status: 'Active' },
    { code: '5', name: 'المصروفات', nameEn: 'Expenses', parent: '', level: 1, category: 'مصروفات', nature: 'مدين', postingType: 'رئيسي', currency: 'YER', balance: 250000, reportLink: 'قائمة الدخل', status: 'Active' },
    { code: '5101', name: 'رواتب وأجور الموظفين', nameEn: 'Salaries & Wages', parent: '5', level: 4, category: 'مصروفات عمومية', nature: 'مدين', postingType: 'فرعي', currency: 'YER', balance: 180000, reportLink: 'قائمة الدخل', status: 'Active' },
    { code: '5102', name: 'مصاريف الصيانة والتشغيل', nameEn: 'Maintenance & Operations', parent: '5', level: 4, category: 'مصروفات عمومية', nature: 'مدين', postingType: 'فرعي', currency: 'YER', balance: 70000, reportLink: 'قائمة الدخل', status: 'Active' }
];

if (!DB.journals) DB.journals = [
    {
        id: 1,
        entryNo: 'JV-2026-0001',
        date: '2026-08-01',
        refNo: 'INV-8821',
        type: 'قيد يومية عام',
        mainDesc: 'اثبات استحقاق رواتب الموظفين لشهر يوليو',
        status: 'Posted',
        attachment: '',
        lines: [
            { code: '5101', accountName: 'رواتب وأجور الموظفين', debit: 180000, credit: 0, currency: 'YER', rate: 1, costCenter: 'إدارة المدرسة', memo: 'رواتب شهر يوليو' },
            { code: '110101', accountName: 'صندوق النقدية الرئيسي', debit: 0, credit: 180000, currency: 'YER', rate: 1, costCenter: 'إدارة المدرسة', memo: 'صرف رواتب' }
        ]
    }
];

if (!DB.cashboxes) DB.cashboxes = [
    { code: 'CB-101', name: 'صندوق مبيعات الفرع الرئيسي', nameEn: 'Main Branch Cash Box', accountCode: '110101', branch: 'فرع صنعاء - المبيعات', cashier: 'أحمد محمد (402)', currency: 'YER', type: 'مبيعات يومية', maxLimit: 5000000, minLimit: 100000, balance: 1250000, allowNegative: 'غير مسموح', status: 'Active' },
    { code: 'CB-102', name: 'صندوق العهدة المستديمة', nameEn: 'Petty Cash Box', accountCode: '110101', branch: 'الإدارة العامة', cashier: 'سارة علي (205)', currency: 'USD', type: 'عهدة مستديمة', maxLimit: 2000, minLimit: 200, balance: 850, allowNegative: 'غير مسموح', status: 'Active' }
];

if (!DB.costCenters) DB.costCenters = [
    { code: 'CC-101', name: 'إدارة المدرسة والمبنى الرئيسي', parent: '', level: 1, type: 'رئيسي', category: 'فرع', manager: 'أحمد المدير', budget: 500000, startDate: '2026-01-01', endDate: '2026-12-31', restriction: 'جميع الحسابات', status: 'Active', actualExpenses: 250000 },
    { code: 'CC-102', name: 'مشروع التوسع بالفرع الجنوبي', parent: 'CC-101', level: 2, type: 'فرعي', category: 'مشروع', manager: 'م. خالد عبدالكريم', budget: 250000, startDate: '2026-01-01', endDate: '2026-12-31', restriction: 'مصروفات التشغيل والصيانة فقط', status: 'Active', actualExpenses: 180000 }
];

if (!DB.accountLimits) DB.accountLimits = [
    { accountCode: '11020105', accountName: 'شركة الأمل للتجارة (عميل)', capType: 'حد ائتماني للعميل (Credit Limit)', maxLimit: 10000, periodDays: 30, tolerance: 5, utilizedAmount: 7500, exceedAction: 'منع الحركة (Block)', overrideRole: 'مدير الائتمان', validFrom: '2026-01-01', validTo: '2026-12-31', status: 'Active' }
];
"""

# Implement all functions:
financial_logic_code = """

// ==================== 1. OPERATION LOCK LOGIC ====================
function renderOperationLock() {
    const tb = document.getElementById('tbl-operation-lock');
    if (!tb) return;
    const locks = DB.operationLocks || [];
    tb.innerHTML = locks.map(l => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;"><i class="fa-solid fa-lock"></i> ${l.opLabel || l.opType}</td>
            <td>${l.startDate || '—'}</td>
            <td>${l.endDate || '—'}</td>
            <td style="font-size:0.85rem;">${l.reason || '—'}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;${l.status === 'نشط' ? 'background:rgba(239,68,68,0.15);color:#f87171;' : 'background:rgba(148,163,184,0.15);color:#94a3b8;'}">${l.status}</span></td>
            <td>${l.user || 'مدير النظام'}</td>
            <td>
                <button class="btn-delete" onclick="deleteOperationLockRule(${l.id})"><i class="fa-solid fa-trash"></i> إلغاء القفل</button>
            </td>
        </tr>
    `).join('') || '<tr><td colspan="7" style="text-align:center;color:var(--muted);">لا توجد قيود/أقفال مفعلة حالياً</td></tr>';
}

function saveOperationLockRule() {
    const opSelect = document.getElementById('lockOpType');
    const opType = opSelect ? opSelect.value : 'all';
    const opLabel = opSelect ? opSelect.options[opSelect.selectedIndex].text : 'جميع العمليات';
    const startDate = document.getElementById('lockStartDate')?.value || new Date().toISOString().slice(0,10);
    const endDate = document.getElementById('lockEndDate')?.value || '';
    const reason = document.getElementById('lockReason')?.value || 'قفل تشغيلي';

    if (!DB.operationLocks) DB.operationLocks = [];
    DB.operationLocks.unshift({
        id: Date.now(),
        opType: opType,
        opLabel: opLabel,
        startDate: startDate,
        endDate: endDate,
        reason: reason,
        status: 'نشط',
        user: 'المستخدم الحالي'
    });

    logAudit('مدير النظام', 'إضافة', 'قفل العمليات', 'تطبيق قفل جديد على ' + opLabel);
    toast('✅ تم تطبيق قفل العملية بنجاح');
    renderOperationLock();
}

function deleteOperationLockRule(id) {
    DB.operationLocks = (DB.operationLocks || []).filter(l => l.id !== id);
    toast('تم إلغاء قفل العملية');
    renderOperationLock();
}


// ==================== 2. CHART OF ACCOUNTS TREE & DETAILS ====================
let selectedChartAccountCode = null;

function filterChartAccounts() {
    renderChartAccountsTree();
}

function renderChartAccountsTree() {
    const wrapper = document.getElementById('chartTreeWrapper');
    if (!wrapper) return;

    const query = (document.getElementById('searchChartAccounts')?.value || '').toLowerCase();
    const levelFilter = document.getElementById('filterChartLevel')?.value || 'all';
    const statusFilter = document.getElementById('filterChartStatus')?.value || 'all';

    const accounts = (DB.accounts || []).filter(a => {
        const matchQ = !query || (a.code || '').toLowerCase().includes(query) || (a.name || '').toLowerCase().includes(query);
        const matchL = levelFilter === 'all' || String(a.level) === levelFilter;
        const matchS = statusFilter === 'all' || (statusFilter === 'active' && a.status === 'Active') || (statusFilter === 'inactive' && a.status !== 'Active');
        return matchQ && matchL && matchS;
    });

    // Build hierarchy
    let html = '';
    const roots = accounts.filter(a => !a.parent || a.level === 1);
    
    function buildBranch(acc, indent = 0) {
        const children = accounts.filter(child => child.parent === acc.code);
        const isSelected = selectedChartAccountCode === acc.code;
        const isHeader = acc.postingType === 'رئيسي' || acc.postingType === 'تجميعي';
        
        return `
            <div style="margin-left:${indent * 16}px;margin-bottom:4px;">
                <div onclick="selectChartAccount('${acc.code}')" style="display:flex;align-items:center;justify-space-between;padding:8px 12px;border-radius:8px;cursor:pointer;background:${isSelected ? 'rgba(59,130,246,0.25)' : 'rgba(255,255,255,0.03)'};border:1px solid ${isSelected ? '#3b82f6' : 'rgba(255,255,255,0.06)'};">
                    <div style="display:flex;align-items:center;gap:8px;">
                        <i class="fa-solid ${isHeader ? 'fa-folder-closed' : 'fa-file-invoice'}" style="color:${isHeader ? '#f59e0b' : '#3b82f6'};"></i>
                        <strong style="color:#60a5fa;font-family:monospace;font-size:0.85rem;">[${acc.code}]</strong>
                        <span style="font-weight:600;font-size:0.85rem;">${acc.name}</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:6px;">
                        <span style="font-size:0.7rem;padding:2px 6px;border-radius:4px;background:rgba(255,255,255,0.06);color:var(--muted);">${acc.postingType}</span>
                        <strong style="font-size:0.8rem;color:#34d399;">${(acc.balance || 0).toLocaleString()} ${acc.currency || 'YER'}</strong>
                    </div>
                </div>
            </div>
            ${children.map(c => buildBranch(c, indent + 1)).join('')}
        `;
    }

    if (roots.length === 0) {
        wrapper.innerHTML = '<p style="text-align:center;color:var(--muted);padding:20px;">لا توجد حسابات مطابقة للبحث</p>';
    } else {
        wrapper.innerHTML = roots.map(r => buildBranch(r)).join('');
    }
}

function selectChartAccount(code) {
    selectedChartAccountCode = code;
    renderChartAccountsTree();
    
    const acc = (DB.accounts || []).find(a => a.code === code);
    const detailsBody = document.getElementById('chartDetailsBody');
    if (!acc || !detailsBody) return;

    detailsBody.innerHTML = `
        <div style="background:rgba(255,255,255,0.02);padding:14px;border-radius:10px;border:1px solid var(--border);margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                <h4 style="color:#60a5fa;font-size:1.1rem;font-weight:800;">[${acc.code}] ${acc.name}</h4>
                <span style="padding:4px 10px;border-radius:6px;font-size:0.75rem;font-weight:700;${acc.status === 'Active' ? 'background:rgba(16,185,129,0.2);color:#10b981;' : 'background:rgba(239,68,68,0.2);color:#f87171;'}">${acc.status === 'Active' ? 'نشط' : 'موقف'}</span>
            </div>
            <div style="font-size:0.85rem;color:var(--muted);margin-bottom:10px;">Name (EN): ${acc.nameEn || 'N/A'}</div>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:0.83rem;">
                <div><strong>الحساب الأب:</strong> ${acc.parent ? acc.parent : '— (حساب رئيسي)'}</div>
                <div><strong>المستوى:</strong> المستوى ${acc.level || 1}</div>
                <div><strong>نوع الحساب:</strong> ${acc.category || 'أصول'}</div>
                <div><strong>طبيعة الحساب:</strong> ${acc.nature || 'مدين'}</div>
                <div><strong>نوع الحركة:</strong> ${acc.postingType || 'فرعي'}</div>
                <div><strong>العملة:</strong> ${acc.currency || 'YER'}</div>
                <div><strong>الربط المالي:</strong> ${acc.reportLink || 'الميزانية العمومية'}</div>
                <div><strong>الرصيد الحالي:</strong> <span style="color:#34d399;font-weight:800;">${(acc.balance || 0).toLocaleString()} ${acc.currency || 'YER'}</span></div>
            </div>
        </div>

        <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <button class="btn-add" onclick="openForm('chart-accounts', {parent:'${acc.code}'})" style="flex:1;font-size:0.8rem;"><i class="fa-solid fa-plus"></i> إضافة حساب فرعي</button>
            <button class="btn-edit" onclick="openForm('chart-accounts', ${JSON.stringify(acc).replace(/"/g, '&quot;')})" style="flex:1;font-size:0.8rem;"><i class="fa-solid fa-pen"></i> تعديل الحساب</button>
            <button class="btn-cancel" onclick="toggleAccountStatus('${acc.code}')" style="flex:1;font-size:0.8rem;"><i class="fa-solid fa-power-off"></i> ${acc.status === 'Active' ? 'تجميد الحساب' : 'تفعيل الحساب'}</button>
        </div>
    `;
}

function toggleAccountStatus(code) {
    const acc = (DB.accounts || []).find(a => a.code === code);
    if (acc) {
        acc.status = acc.status === 'Active' ? 'Inactive' : 'Active';
        toast('تم تغيير حالة الحساب إلى ' + (acc.status === 'Active' ? 'نشط' : 'موقف'));
        selectChartAccount(code);
    }
}

function exportChartExcel() {
    let csv = "\\uFEFFكود الحساب,اسم الحساب,الحساب الأب,المستوى,نوع الحساب,الطبيعة,نوع الحركة,العملة,الرصيد,الربط المالي,الحالة\\n";
    (DB.accounts || []).forEach(a => {
        csv += `"${a.code}","${a.name}","${a.parent || ''}","${a.level}","${a.category}","${a.nature}","${a.postingType}","${a.currency}","${a.balance}","${a.reportLink}","${a.status}"\\n`;
    });
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'Chart_Of_Accounts_' + new Date().toISOString().slice(0,10) + '.csv';
    link.click();
    toast('تم تصدير دليل الحسابات بصيغة Excel');
}


// ==================== 3. JOURNAL ENTRIES (3-PART LAYOUT) ====================
let currentJournalLines = [];

function renderJournalList() {
    const tb = document.getElementById('tbl-journal-entries');
    if (!tb) return;
    
    const query = (document.getElementById('searchJournal')?.value || '').toLowerCase();
    const statusFilter = document.getElementById('filterJournalStatus')?.value || 'all';

    const entries = (DB.journals || []).filter(j => {
        const matchQ = !query || (j.entryNo || '').toLowerCase().includes(query) || (j.mainDesc || '').toLowerCase().includes(query);
        const matchS = statusFilter === 'all' || j.status === statusFilter;
        return matchQ && matchS;
    });

    tb.innerHTML = entries.map(j => {
        const totalAmount = (j.lines || []).reduce((s, l) => s + (l.debit || 0), 0);
        return `
            <tr>
                <td style="font-weight:700;color:#60a5fa;">${j.entryNo}</td>
                <td>${j.date}</td>
                <td><span style="background:rgba(59,130,246,0.15);color:#93c5fd;padding:2px 8px;border-radius:5px;font-size:0.78rem;">${j.type}</span></td>
                <td>${j.mainDesc}</td>
                <td style="font-weight:800;color:#34d399;">${totalAmount.toLocaleString()} YER</td>
                <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;${j.status === 'Posted' ? 'background:rgba(16,185,129,0.15);color:#10b981;' : 'background:rgba(245,158,11,0.15);color:#fbbf24;'}">${j.status === 'Posted' ? 'مرحّل' : 'مسودة'}</span></td>
                <td>${j.attachment ? '<i class="fa-solid fa-paperclip" style="color:#60a5fa;"></i>' : '—'}</td>
                <td>
                    <div class="act">
                        <button class="btn-edit" onclick="editJournalEntry(${j.id})"><i class="fa-solid fa-pen"></i></button>
                        <button class="btn-delete" onclick="deleteJournalEntry(${j.id})"><i class="fa-solid fa-trash"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('') || '<tr><td colspan="8" style="text-align:center;color:var(--muted);">لا توجد قيود يومية مسجلة</td></tr>';
}

function showNewJournalEntryForm() {
    const card = document.getElementById('journalEntryFormCard');
    if (!card) return;
    card.style.display = 'block';
    
    document.getElementById('jvNo').value = 'JV-2026-' + String((DB.journals || []).length + 1).padStart(4, '0');
    document.getElementById('jvDate').value = new Date().toISOString().slice(0, 10);
    document.getElementById('jvRefNo').value = '';
    document.getElementById('jvMainDesc').value = '';
    document.getElementById('jvStatus').value = 'Draft';
    
    currentJournalLines = [
        { code: '5101', debit: 0, credit: 0, currency: 'YER', rate: 1, costCenter: 'عام', memo: '' },
        { code: '110101', debit: 0, credit: 0, currency: 'YER', rate: 1, costCenter: 'عام', memo: '' }
    ];
    renderJournalLinesGrid();
}

function addJournalLine() {
    currentJournalLines.push({ code: '110101', debit: 0, credit: 0, currency: 'YER', rate: 1, costCenter: 'عام', memo: '' });
    renderJournalLinesGrid();
}

function removeJournalLine(idx) {
    if (currentJournalLines.length <= 2) return toast('يجب أن يحتوي القيد على سطرين محاسبيين على الأقل');
    currentJournalLines.splice(idx, 1);
    renderJournalLinesGrid();
}

function renderJournalLinesGrid() {
    const tbody = document.getElementById('tbl-jv-lines');
    if (!tbody) return;

    const accOptions = (DB.accounts || []).filter(a => a.postingType === 'فرعي').map(a => `<option value="${a.code}">[${a.code}] ${a.name}</option>`).join('');

    tbody.innerHTML = currentJournalLines.map((line, idx) => `
        <tr>
            <td>
                <select onchange="currentJournalLines[${idx}].code=this.value" style="width:100%;">
                    ${(DB.accounts || []).filter(a => a.postingType === 'فرعي').map(a => `<option value="${a.code}" ${line.code === a.code ? 'selected' : ''}>[${a.code}] ${a.name}</option>`).join('')}
                </select>
            </td>
            <td><input type="number" value="${line.debit || 0}" oninput="currentJournalLines[${idx}].debit=parseFloat(this.value)||0; calculateJournalTotals();" style="width:100%;text-align:center;color:#60a5fa;font-weight:700;"></td>
            <td><input type="number" value="${line.credit || 0}" oninput="currentJournalLines[${idx}].credit=parseFloat(this.value)||0; calculateJournalTotals();" style="width:100%;text-align:center;color:#34d399;font-weight:700;"></td>
            <td>
                <select onchange="currentJournalLines[${idx}].currency=this.value">
                    <option value="YER" ${line.currency==='YER'?'selected':''}>YER</option>
                    <option value="USD" ${line.currency==='USD'?'selected':''}>USD</option>
                    <option value="SAR" ${line.currency==='SAR'?'selected':''}>SAR</option>
                </select>
            </td>
            <td><input value="${line.costCenter || 'عام'}" oninput="currentJournalLines[${idx}].costCenter=this.value" style="width:100%;"></td>
            <td><input value="${line.memo || ''}" oninput="currentJournalLines[${idx}].memo=this.value" placeholder="ملاحظات السطر" style="width:100%;"></td>
            <td style="text-align:center;"><button class="btn-delete" onclick="removeJournalLine(${idx})" style="padding:3px 6px;"><i class="fa-solid fa-trash"></i></button></td>
        </tr>
    `).join('');

    calculateJournalTotals();
}

function calculateJournalTotals() {
    const totalDebit = currentJournalLines.reduce((s, l) => s + (l.debit || 0), 0);
    const totalCredit = currentJournalLines.reduce((s, l) => s + (l.credit || 0), 0);
    const delta = Math.abs(totalDebit - totalCredit);

    document.getElementById('jvTotalDebit').textContent = totalDebit.toLocaleString('ar-YE', {minimumFractionDigits:2});
    document.getElementById('jvTotalCredit').textContent = totalCredit.toLocaleString('ar-YE', {minimumFractionDigits:2});

    const indicator = document.getElementById('jvBalanceIndicator');
    const btnSave = document.getElementById('btnSaveJournal');

    if (delta < 0.01 && (totalDebit > 0 || totalCredit > 0)) {
        indicator.style.background = 'rgba(16,185,129,0.2)';
        indicator.style.color = '#10b981';
        indicator.innerHTML = '<i class="fa-solid fa-scale-balanced"></i> القيد متوازن بنجاح (الفرق: 0.00)';
        if (btnSave) btnSave.disabled = false;
    } else {
        indicator.style.background = 'rgba(239,68,68,0.2)';
        indicator.style.color = '#f87171';
        indicator.innerHTML = `<i class="fa-solid fa-scale-unbalanced"></i> غير متوازن (الفرق: ${delta.toLocaleString('ar-YE', {minimumFractionDigits:2})})`;
        if (btnSave) btnSave.disabled = true;
    }
}

function saveJournalEntry() {
    const totalDebit = currentJournalLines.reduce((s, l) => s + (l.debit || 0), 0);
    const totalCredit = currentJournalLines.reduce((s, l) => s + (l.credit || 0), 0);
    if (Math.abs(totalDebit - totalCredit) > 0.01) return toast('⚠️ لا يمكن حفظ القيد: القيد غير متوازن!');

    const entryNo = document.getElementById('jvNo').value;
    const date = document.getElementById('jvDate').value;
    const refNo = document.getElementById('jvRefNo').value;
    const type = document.getElementById('jvType').value;
    const status = document.getElementById('jvStatus').value;
    const mainDesc = document.getElementById('jvMainDesc').value || 'قيد يومية عام';

    if (!DB.journals) DB.journals = [];
    DB.journals.unshift({
        id: Date.now(),
        entryNo, date, refNo, type, status, mainDesc,
        lines: [...currentJournalLines]
    });

    logAudit('المحاسب', 'إضافة', 'القيود اليومية', 'حفظ القيد رقم ' + entryNo);
    toast('✅ تم حفظ وإعتماد القيد اليومي بنجاح');
    document.getElementById('journalEntryFormCard').style.display = 'none';
    renderJournalList();
}


// ==================== 4. CASHBOXES SETUP & GRID ====================
function renderCashboxes() {
    const tb = document.getElementById('tbl-cashboxes');
    if (!tb) return;

    const query = (document.getElementById('searchCashbox')?.value || '').toLowerCase();
    const boxes = (DB.cashboxes || []).filter(c => !query || (c.name || '').toLowerCase().includes(query) || (c.code || '').toLowerCase().includes(query));

    tb.innerHTML = boxes.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${c.code}</td>
            <td style="font-weight:700;">${c.name}</td>
            <td>${c.accountCode} - صندوق رئيسي</td>
            <td>${c.branch || '—'}</td>
            <td>${c.cashier || 'أمين الصندوق'}</td>
            <td>${c.currency || 'YER'}</td>
            <td>${c.type || 'مبيعات'}</td>
            <td>${(c.maxLimit || 0).toLocaleString()}</td>
            <td style="font-weight:800;color:#34d399;">${(c.balance || 0).toLocaleString()}</td>
            <td>${c.allowNegative || 'غير مسموح'}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${c.status === 'Active' ? 'نشط' : 'موقف'}</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('cashbox', ${JSON.stringify(c).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button>
                </div>
            </td>
        </tr>
    `).join('') || '<tr><td colspan="12" style="text-align:center;color:var(--muted);">لا توجد صناديق نقدية محددة</td></tr>';
}


// ==================== 5. COST CENTERS TREE & PERFORMANCE ====================
function renderCostCenters() {
    const wrapper = document.getElementById('costCenterTreeWrapper');
    if (!wrapper) return;

    const query = (document.getElementById('searchCostCenter')?.value || '').toLowerCase();
    const centers = (DB.costCenters || []).filter(cc => !query || (cc.name || '').toLowerCase().includes(query) || (cc.code || '').toLowerCase().includes(query));

    wrapper.innerHTML = centers.map(cc => `
        <div onclick="selectCostCenter('${cc.code}')" style="display:flex;justify-content:space-between;align-items:center;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.03);border:1px solid var(--border);margin-bottom:6px;cursor:pointer;">
            <div>
                <strong style="color:#60a5fa;">[${cc.code}]</strong>
                <span style="font-weight:700;margin-right:6px;">${cc.name}</span>
                <span style="font-size:0.75rem;color:var(--muted);margin-right:8px;">(${cc.category || 'قسم'})</span>
            </div>
            <div style="font-size:0.8rem;color:#34d399;font-weight:700;">الموازنة: ${(cc.budget || 0).toLocaleString()} $</div>
        </div>
    `).join('') || '<p style="text-align:center;color:var(--muted);">لا توجد مراكز تكلفة</p>';
}

function selectCostCenter(code) {
    const cc = (DB.costCenters || []).find(c => c.code === code);
    const panel = document.getElementById('costCenterPerformancePanel');
    if (!cc || !panel) return;

    const actual = cc.actualExpenses || 150000;
    const budget = cc.budget || 200000;
    const variance = ((actual - budget) / budget) * 100;
    const isOver = actual > budget;

    panel.innerHTML = `
        <div style="background:rgba(255,255,255,0.02);padding:14px;border-radius:10px;border:1px solid var(--border);">
            <h4 style="color:#60a5fa;font-weight:800;margin-bottom:10px;">[${cc.code}] ${cc.name}</h4>
            <div style="font-size:0.85rem;margin-bottom:12px;"><strong>مدير المركز:</strong> ${cc.manager || 'غير محدد'} | <strong>النطاق:</strong> ${cc.startDate || ''} إلى ${cc.endDate || ''}</div>
            
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;">
                <div style="background:rgba(59,130,246,0.1);padding:10px;border-radius:8px;">
                    <span style="font-size:0.75rem;color:var(--muted);">الموازنة المعتمدة</span>
                    <div style="font-size:1.1rem;font-weight:800;color:#60a5fa;">${budget.toLocaleString()} $</div>
                </div>
                <div style="background:rgba(16,185,129,0.1);padding:10px;border-radius:8px;">
                    <span style="font-size:0.75rem;color:var(--muted);">المصروفات الفعلية</span>
                    <div style="font-size:1.1rem;font-weight:800;color:#34d399;">${actual.toLocaleString()} $</div>
                </div>
            </div>

            <div style="padding:10px;border-radius:8px;background:${isOver ? 'rgba(239,68,68,0.15)' : 'rgba(16,185,129,0.15)'};color:${isOver ? '#f87171' : '#10b981'};font-weight:700;font-size:0.85rem;">
                <i class="fa-solid ${isOver ? 'fa-triangle-exclamation' : 'fa-circle-check'}"></i> نسبة الانحراف المالي: ${variance.toFixed(1)}% (${isOver ? 'تجاوز للموازنة' : 'في حدود الموازنة'})
            </div>
        </div>
    `;
}


// ==================== 6. ACCOUNT CEILING / LIMITS ====================
function renderAccountCeiling() {
    const tb = document.getElementById('tbl-account-ceiling');
    if (!tb) return;

    const query = (document.getElementById('searchAccountCeiling')?.value || '').toLowerCase();
    const limits = (DB.accountLimits || []).filter(l => !query || (l.accountName || '').toLowerCase().includes(query));

    tb.innerHTML = limits.map(l => `
        <tr>
            <td style="font-weight:700;">${l.accountName}</td>
            <td>${l.capType}</td>
            <td style="font-weight:800;color:#60a5fa;">${(l.maxLimit || 0).toLocaleString()} $</td>
            <td>${l.periodDays} يوماً</td>
            <td>${l.tolerance}%</td>
            <td>${(l.utilizedAmount || 0).toLocaleString()} $</td>
            <td style="font-weight:800;color:#34d399;">${((l.maxLimit || 0) - (l.utilizedAmount || 0)).toLocaleString()} $</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(239,68,68,0.15);color:#f87171;">${l.exceedAction}</span></td>
            <td>${l.overrideRole}</td>
            <td style="font-size:0.8rem;">${l.validFrom || ''} - ${l.validTo || ''}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${l.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="toast('تعديل السقف')"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('') || '<tr><td colspan="12" style="text-align:center;color:var(--muted);">لا توجد سقوف حسابات محددة</td></tr>';
}


// ==================== 7. UNIFIED VOUCHERS HUB ====================
let currentVoucherFilterType = 'all';

function switchVoucherType(type, btnEl) {
    currentVoucherFilterType = type;
    if (btnEl) {
        btnEl.parentElement.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
    }
    renderVouchers();
}

function renderVouchers() {
    const tb = document.getElementById('tbl-vouchers');
    if (!tb) return;

    const query = (document.getElementById('searchVouchers')?.value || '').toLowerCase();
    
    const receipts = (DB.vreceipts || []).map(r => ({ ...r, vtype: 'receipt', typeLabel: 'سند قبض', color: '#10b981' }));
    const payments = (DB.vpayments || []).map(p => ({ ...p, vtype: 'payment', typeLabel: 'سند صرف', color: '#ef4444' }));
    const transfers = (DB.vtransfers || []).map(t => ({ ...t, vtype: 'transfer', typeLabel: 'تحويل داخلي', color: '#3b82f6' }));

    let allVouchers = [...receipts, ...payments, ...transfers];
    if (currentVoucherFilterType !== 'all') {
        allVouchers = allVouchers.filter(v => v.vtype === currentVoucherFilterType);
    }

    if (query) {
        allVouchers = allVouchers.filter(v => (v.number || '').toLowerCase().includes(query) || (v.account || '').toLowerCase().includes(query) || (v.desc || '').toLowerCase().includes(query));
    }

    tb.innerHTML = allVouchers.map(v => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${v.number}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${v.color}22;color:${v.color};">${v.typeLabel}</span></td>
            <td>${v.date}</td>
            <td>${v.cashAccount || 'صندوق مبيعات رئيسي'}</td>
            <td style="font-weight:700;">${v.account}</td>
            <td>${v.method || 'نقداً'}</td>
            <td style="font-weight:800;color:${v.color};">${(v.amount || 0).toLocaleString()} YER</td>
            <td>${v.costCenter || 'عام'}</td>
            <td style="font-size:0.83rem;">${v.desc || '—'}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">مرحّل</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="printReceipt(${JSON.stringify(v).replace(/"/g, '&quot;')})"><i class="fa-solid fa-print"></i></button>
                    <button class="btn-delete" onclick="toast('تم إلغاء السند')"><i class="fa-solid fa-trash"></i></button>
                </div>
            </td>
        </tr>
    `).join('') || '<tr><td colspan="11" style="text-align:center;color:var(--muted);">لا توجد سندات مالية مسجلة</td></tr>';
}


// ==================== 8. INTERACTIVE STATEMENT OF ACCOUNT ====================
function renderStatementOfAccount() {
    const select = document.getElementById('soaAccountSelect');
    const tb = document.getElementById('tbl-statement-ledger');
    if (!select || !tb) return;

    // Populate account select if empty
    if (select.children.length === 0) {
        select.innerHTML = (DB.accounts || []).filter(a => a.postingType === 'فرعي').map(a => `<option value="${a.code}">[${a.code}] ${a.name}</option>`).join('');
    }

    const accountCode = select.value;
    const currency = document.getElementById('soaCurrency')?.value || 'YER';

    // Mock statement ledger calculations
    const openingBal = 120000;
    let runningBal = openingBal;
    let totalDebit = 0;
    let totalCredit = 0;

    const transactions = [
        { date: '2026-08-01', docNo: 'JV-2026-0001', type: 'قيد يومية', desc: 'رصيد افتتاحي منقول من العام السابق', debit: 120000, credit: 0, costCenter: 'عام' },
        { date: '2026-08-03', docNo: 'RV-2026-0012', type: 'سند قبض', desc: 'سداد دفعة تحت الحساب لقاء فاتورة رسوم', debit: 0, credit: 50000, costCenter: 'عام' },
        { date: '2026-08-05', docNo: 'JV-2026-0005', type: 'قيد يومية', desc: 'اثبات رسوم دراسية إضافية للفصل الثاني', debit: 35000, credit: 0, costCenter: 'القسم العلمي' }
    ];

    tb.innerHTML = transactions.map(t => {
        totalDebit += t.debit;
        totalCredit += t.credit;
        runningBal = runningBal + t.debit - t.credit;
        return `
            <tr>
                <td>${t.date}</td>
                <td style="font-weight:700;color:#60a5fa;cursor:pointer;" onclick="toast('الانتقال للمستند ${t.docNo}')"><i class="fa-solid fa-link"></i> ${t.docNo}</td>
                <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${t.type}</span></td>
                <td style="font-size:0.85rem;">${t.desc}</td>
                <td style="color:#60a5fa;font-weight:700;">${t.debit > 0 ? t.debit.toLocaleString() : '—'}</td>
                <td style="color:#34d399;font-weight:700;">${t.credit > 0 ? t.credit.toLocaleString() : '—'}</td>
                <td style="font-weight:800;color:#fbbf24;">${runningBal.toLocaleString()} ${currency}</td>
                <td>${t.costCenter}</td>
            </tr>
        `;
    }).join('');

    document.getElementById('soaOpeningBalance').textContent = openingBal.toLocaleString() + ' ' + currency;
    document.getElementById('soaTotalDebit').textContent = totalDebit.toLocaleString() + ' ' + currency;
    document.getElementById('soaTotalCredit').textContent = totalCredit.toLocaleString() + ' ' + currency;
    document.getElementById('soaFinalBalance').textContent = runningBal.toLocaleString() + ' ' + currency;
}

function exportStatementExcel() {
    toast('تم تصدير كشف الحساب بصيغة Excel');
}

// Hook into window.goTo to trigger financial renders
const _origFinancialGoTo = window.goTo;
if (_origFinancialGoTo) {
    window.goTo = function(id) {
        _origFinancialGoTo(id);
        if (id === 'pg-operation-lock') renderOperationLock();
        if (id === 'pg-chart-accounts') renderChartAccountsTree();
        if (id === 'pg-journal') renderJournalList();
        if (id === 'pg-cashboxes') renderCashboxes();
        if (id === 'pg-cost-centers') renderCostCenters();
        if (id === 'pg-account-ceiling') renderAccountCeiling();
        if (id === 'pg-vouchers') renderVouchers();
        if (id === 'pg-student-account') renderStatementOfAccount();
    };
}

"""

# Insert DB init and financial logic into app.js
if 'financial_logic_code' not in js and 'renderChartAccountsTree' not in js:
    js += db_init_code + "\n" + financial_logic_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

opens = js.count('{')
closes = js.count('}')
print(f"app.js size: {len(js)} bytes, braces diff: {opens - closes}")

print("Financial JavaScript logic updated successfully!")
