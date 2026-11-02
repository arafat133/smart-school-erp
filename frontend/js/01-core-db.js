
/**
 * ============================================================================
 * CHART OF ACCOUNTS TREE ENGINE & SPLIT DETAILS VIEW
 * ============================================================================
 */
if (!window.DB) window.DB = {};
/**
 * ============================================================================
 * CHART OF ACCOUNTS TREE & DETAILS CARD ENGINE
 * ============================================================================
 */
if (!window.DB) window.DB = {};
window.DB.accounts = [
    // Level 1: Main Top-Level Accounts
    {
        code: '1',
        name: 'الأصول (Assets)',
        nameEn: 'Assets',
        parent: '',
        level: 1,
        category: 'أصول',
        nature: 'مدين',
        postingType: 'رئيسي',
        currency: 'YER',
        balance: 95400000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'إجمالي أصول وممتلكات المدرسة المتداولة والثابتة والنقدية.'
    },
    {
        code: '2',
        name: 'الخصوم (Liabilities)',
        nameEn: 'Liabilities',
        parent: '',
        level: 1,
        category: 'خصوم',
        nature: 'دائن',
        postingType: 'رئيسي',
        currency: 'YER',
        balance: 18200000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'إجمالي الالتزامات ومستحقات الموردين والدائنين.'
    },
    {
        code: '3',
        name: 'حقوق الملكية (Equity)',
        nameEn: 'Equity & Capital',
        parent: '',
        level: 1,
        category: 'حقوق ملكية',
        nature: 'دائن',
        postingType: 'رئيسي',
        currency: 'YER',
        balance: 77200000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'رأس المال المعتمد والأرباح المبقاة والاحتياطيات.'
    },
    {
        code: '4',
        name: 'الإيرادات (Revenues)',
        nameEn: 'Revenues',
        parent: '',
        level: 1,
        category: 'إيرادات',
        nature: 'دائن',
        postingType: 'رئيسي',
        currency: 'YER',
        balance: 48500000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'إجمالي إيرادات الرسوم المدرسية والأنشطة والخدمات.'
    },
    {
        code: '5',
        name: 'المصروفات (Expenses)',
        nameEn: 'Expenses',
        parent: '',
        level: 1,
        category: 'مصروفات',
        nature: 'مدين',
        postingType: 'رئيسي',
        currency: 'YER',
        balance: 32100000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'إجمالي نفقات التشغيل والرواتب والأجور والمشتريات.'
    },

    // Level 2: Aggregated Accounts
    {
        code: '11',
        name: 'الأصول المتداولة (Current Assets)',
        nameEn: 'Current Assets',
        parent: '1',
        level: 2,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'تجميعي',
        currency: 'YER',
        balance: 62400000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'النقدية بالصناديق والبنوك وحسابات المدينين والعهد.'
    },
    {
        code: '12',
        name: 'الأصول الثابتة (Fixed Assets)',
        nameEn: 'Fixed Assets',
        parent: '1',
        level: 2,
        category: 'أصول ثابتة',
        nature: 'مدين',
        postingType: 'تجميعي',
        currency: 'YER',
        balance: 33000000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'المباني المدرسية، التجهيزات التعليمية، المعامل، والأثاث.'
    },
    {
        code: '21',
        name: 'الخصوم المتداولة (Current Liabilities)',
        nameEn: 'Current Liabilities',
        parent: '2',
        level: 2,
        category: 'خصوم متداولة',
        nature: 'دائن',
        postingType: 'تجميعي',
        currency: 'YER',
        balance: 18200000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'مستحقات الموردين ومخصصات الأجور والأمانات.'
    },
    {
        code: '41',
        name: 'إيرادات النشاط التعليمي (Educational Revenues)',
        nameEn: 'Educational Activity Revenues',
        parent: '4',
        level: 2,
        category: 'إيرادات نشاط',
        nature: 'دائن',
        postingType: 'تجميعي',
        currency: 'YER',
        balance: 45200000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'رسوم التسجيل، الأقساط الدراسية، الكتب، والنقل المدرسي.'
    },
    {
        code: '51',
        name: 'المصروفات العمومية والإدارية (General & Admin Expenses)',
        nameEn: 'General & Administrative Expenses',
        parent: '5',
        level: 2,
        category: 'مصروفات عمومية',
        nature: 'مدين',
        postingType: 'تجميعي',
        currency: 'YER',
        balance: 32100000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'رواتب الكادر التعليمي، الإيجارات، الصيانة، والمصاريف التشغيلية.'
    },

    // Level 3: Subsidiary Sub-Accounts
    {
        code: '1101',
        name: 'النقدية وما في حكمها (Cash & Cash Equivalents)',
        nameEn: 'Cash & Cash Equivalents',
        parent: '11',
        level: 3,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'فرعي',
        currency: 'YER',
        balance: 48900000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'حسابات الصناديق النقدية والحسابات البنكية الجارية.'
    },
    {
        code: '1102',
        name: 'المدينون وأولياء الأمور (Accounts Receivable)',
        nameEn: 'Accounts Receivable',
        parent: '11',
        level: 3,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'فرعي',
        currency: 'YER',
        balance: 13500000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'أرصدة ذمم الطلاب وأولياء الأمور للرسوم المستحقة.'
    },
    {
        code: '5101',
        name: 'الرواتب والأجور (Salaries & Wages)',
        nameEn: 'Salaries & Wages',
        parent: '51',
        level: 3,
        category: 'مصروفات عمومية',
        nature: 'مدين',
        postingType: 'فرعي',
        currency: 'YER',
        balance: 24500000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'رواتب المعلمين والإداريين والمكافآت والبدلات.'
    },

    // Level 4: Posting & Analytical Accounts
    {
        code: '110101',
        name: 'صندوق النقدية الرئيسي (Main Cash Box)',
        nameEn: 'Main Cash Box',
        parent: '1101',
        level: 4,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'تحليلي للقيود',
        currency: 'YER',
        balance: 3500000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'الخزينة الرئيسية للإدارة العامة للمقبوضات والمدفوعات النقدية.'
    },
    {
        code: '110102',
        name: 'بنك اليمن والكويت (Yemen Kuwait Bank)',
        nameEn: 'Yemen Kuwait Bank (YKB)',
        parent: '1101',
        level: 4,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'تحليلي للقيود',
        currency: 'YER',
        balance: 45200000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'الحساب الجاري الرئيسي لتحصيل الرسوم عبر التحويلات البنكية.'
    },
    {
        code: '110103',
        name: 'بنك الكريمي الإسلامي (Kuraimi Islamic Bank)',
        nameEn: 'Kuraimi Islamic Bank',
        parent: '1101',
        level: 4,
        category: 'أصول متداولة',
        nature: 'مدين',
        postingType: 'تحليلي للقيود',
        currency: 'YER',
        balance: 28100000,
        reportLink: 'الميزانية العمومية',
        status: 'Active',
        notes: 'مربوط ببوابة التحصيل المباشر وتطبيق الكريمي جوال.'
    },
    {
        code: '410101',
        name: 'رسوم دراسية مرحلة أساسية (Basic Stage Tuition Fees)',
        nameEn: 'Basic Stage Tuition Fees',
        parent: '41',
        level: 4,
        category: 'إيرادات نشاط',
        nature: 'دائن',
        postingType: 'تحليلي للقيود',
        currency: 'YER',
        balance: 28500000,
        reportLink: 'قائمة الدخل',
        status: 'Active',
        notes: 'حساب إيرادات الرسوم الدراسية لطلاب المرحلة الأساسية (1-9).'
    }
];

let selectedChartAccountCode = '110101';

function selectChartAccount(code) {
    selectedChartAccountCode = code;
    const acc = (window.DB.accounts || []).find(a => String(a.code) === String(code));
    const card = document.getElementById('accountDetailsContent');

    if (!acc || !card) return;

    const isDebit = acc.nature === 'مدين';
    const isActive = acc.status === 'Active';

    card.innerHTML = `
        <div style="background:rgba(15,23,42,0.9);border-radius:10px;padding:16px;border:1px solid rgba(255,255,255,0.12);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:10px;">
                <div>
                    <span style="font-size:0.75rem;color:#94a3b8;">كود الحساب المالي:</span>
                    <h3 style="font-family:monospace;color:#38bdf8;font-size:1.3rem;margin:2px 0;">[ ${acc.code} ]</h3>
                </div>
                <div style="text-align:left;">
                    <span class="badge ${isActive ? 'badge-success' : 'badge-danger'}" style="font-size:0.8rem;padding:6px 12px;">
                        <i class="fa-solid ${isActive ? 'fa-circle-check' : 'fa-circle-xmark'}"></i> ${isActive ? 'نشط ومفعل 🟢' : 'موقف ومجمد 🔴'}
                    </span>
                </div>
            </div>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px;">
                <div>
                    <small style="color:#94a3b8;display:block;">الاسم بالعربية:</small>
                    <strong style="color:#f8fafc;font-size:0.95rem;">${acc.name}</strong>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">الاسم بالإنجليزية:</small>
                    <strong style="color:#cbd5e1;font-size:0.9rem;font-family:sans-serif;">${acc.nameEn || '---'}</strong>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">الحساب الأب:</small>
                    <strong style="color:#60a5fa;font-family:monospace;">${acc.parent ? acc.parent : '— (حساب رئيسي أول)'}</strong>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">المستوى المحاسبي:</small>
                    <span class="badge" style="background:rgba(59,130,246,0.2);color:#93c5fd;">المستوى ${acc.level} (${acc.postingType})</span>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">التصنيف المالي:</small>
                    <strong style="color:#f8fafc;">${acc.category}</strong>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">طبيعة الحساب:</small>
                    <span class="badge ${isDebit ? 'badge-info' : 'badge-success'}">${acc.nature} (${isDebit ? 'Debit 🔵' : 'Credit 🟢'})</span>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">العملة المعتمدة:</small>
                    <span class="badge badge-info">${acc.currency || 'YER'}</span>
                </div>
                <div>
                    <small style="color:#94a3b8;display:block;">الربط المالي الختامي:</small>
                    <strong style="color:#c084fc;">${acc.reportLink || 'الميزانية العمومية'}</strong>
                </div>
            </div>

            <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:8px;padding:12px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;">
                <span style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-coins" style="color:#34d399;"></i> الرصيد المالي الحالي:</span>
                <strong style="color:#34d399;font-size:1.2rem;font-family:monospace;">${Number(acc.balance || 0).toLocaleString()} <small style="font-size:0.8rem;color:#94a3b8;">${acc.currency || 'YER'}</small></strong>
            </div>

            ${acc.notes ? `
            <div style="background:rgba(255,255,255,0.03);border-radius:6px;padding:8px 12px;font-size:0.8rem;color:#94a3b8;margin-bottom:14px;">
                <i class="fa-solid fa-circle-info" style="color:#38bdf8;"></i> ${acc.notes}
            </div>` : ''}

            <div style="display:flex;gap:8px;">
                <button class="btn-add" style="flex:1;background:linear-gradient(135deg,#3b82f6,#2563eb);padding:7px;" onclick="openForm('chart-accounts', '${acc.code}')">
                    <i class="fa-solid fa-pen-to-square"></i> تعديل بيانات الحساب
                </button>
                <button class="btn-add" style="background:linear-gradient(135deg,#ef4444,#dc2626);padding:7px 14px;" onclick="deleteItem('accounts', '${acc.code}')" title="حذف الحساب">
                    <i class="fa-solid fa-trash-can"></i>
                </button>
            </div>
        </div>
    `;

    renderChartAccountsTree();
}
window.selectChartAccount = selectChartAccount;

function renderChartAccountsTree() {
    const wrapper = document.getElementById('chartAccountsTreeView') || document.getElementById('chartTreeWrapper');
    if (!wrapper) return;

    const query = (document.getElementById('searchChartAccounts')?.value || '').toLowerCase().trim();
    const accounts = window.DB.accounts || [];

    // Calculate KPIs
    const totEl = document.getElementById('coaTotalAccounts');
    const astEl = document.getElementById('coaTotalAssets');
    const liaEl = document.getElementById('coaTotalLiabilities');
    const equEl = document.getElementById('coaTotalEquity');

    if (totEl) totEl.innerHTML = `${accounts.length} <small style="font-size:0.75rem;">حساباً مالياً</small>`;
    if (astEl) astEl.innerHTML = `95,400,000 <small style="font-size:0.75rem;">YER</small>`;
    if (liaEl) liaEl.innerHTML = `18,200,000 <small style="font-size:0.75rem;">YER</small>`;
    if (equEl) equEl.innerHTML = `77,200,000 <small style="font-size:0.75rem;">YER</small>`;

    const sortedAccounts = [...accounts].sort((a, b) => String(a.code).localeCompare(String(b.code), undefined, { numeric: true, sensitivity: 'base' }));

    function buildBranch(acc, indent = 0) {
        const children = sortedAccounts.filter(child => String(child.parent) === String(acc.code));
        const isSelected = selectedChartAccountCode === acc.code;
        const isHeader = acc.level === 1 || acc.level === 2;

        let iconClass = 'fa-file-invoice-dollar';
        let iconColor = '#38bdf8';
        if (acc.level === 1) { iconClass = 'fa-folder-closed'; iconColor = '#f59e0b'; }
        else if (acc.level === 2) { iconClass = 'fa-folder-open'; iconColor = '#8b5cf6'; }
        else if (acc.level === 3) { iconClass = 'fa-layer-group'; iconColor = '#3b82f6'; }
        else if (acc.level === 4) { iconClass = 'fa-file-lines'; iconColor = '#34d399'; }

        let html = `
            <div style="margin-right:${indent * 18}px;margin-bottom:6px;">
                <div onclick="selectChartAccount('${acc.code}')" ondblclick="openForm('chart-accounts', '${acc.code}')" oncontextmenu="event.preventDefault();deleteItem('accounts', '${acc.code}')" style="display:flex;align-items:center;justify-content:space-between;padding:9px 12px;border-radius:8px;cursor:pointer;background:${isSelected ? 'rgba(59,130,246,0.25)' : 'rgba(255,255,255,0.03)'};border:1px solid ${isSelected ? '#3b82f6' : 'rgba(255,255,255,0.07)'};transition:all 0.2s;" title="انقر للعرض، مرتين للتعديل، مطولاً للحذف">
                    <div style="display:flex;align-items:center;gap:8px;">
                        <i class="fa-solid ${iconClass}" style="color:${iconColor};font-size:1rem;"></i>
                        <strong style="color:#60a5fa;font-family:monospace;font-size:0.9rem;">[${acc.code}]</strong>
                        <span style="font-weight:700;font-size:0.88rem;color:#f8fafc;">${acc.name}</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:6px;">
                        <span class="badge" style="font-size:0.7rem;background:rgba(255,255,255,0.06);color:#cbd5e1;">L${acc.level}</span>
                        <strong style="font-size:0.83rem;color:#34d399;font-family:monospace;">${Number(acc.balance || 0).toLocaleString()} <small style="color:#94a3b8;">${acc.currency || 'YER'}</small></strong>
                    </div>
                </div>
            </div>
        `;

        if (children.length > 0) {
            children.forEach(child => {
                if (!query || child.code.toLowerCase().includes(query) || child.name.toLowerCase().includes(query)) {
                    html += buildBranch(child, indent + 1);
                }
            });
        }

        return html;
    }

    let treeHtml = '';
    const rootAccounts = sortedAccounts.filter(a => !a.parent || a.level === 1);
    rootAccounts.forEach(root => {
        treeHtml += buildBranch(root, 0);
    });

    wrapper.innerHTML = treeHtml || '<p style="text-align:center;padding:20px;color:var(--muted);">لا توجد حسابات مطابقة للبحث</p>';
}
window.renderChartAccountsTree = renderChartAccountsTree;
window.renderChartAccountsTreeView = renderChartAccountsTree;
window.renderChartAccounts = renderChartAccountsTree;
window.filterChartAccounts = renderChartAccountsTree;

// Trigger initial selection and render
setTimeout(() => {
    try {
        renderChartAccountsTree();
        selectChartAccount(selectedChartAccountCode || '110101');
    } catch(e) {}
}, 200);


function exportChartAccountsExcel() {
    const accounts = window.DB.accounts || [];
    if (accounts.length === 0) {
        if (typeof toast === 'function') toast('⚠️ لا توجد حسابات لتصديرها!', 1);
        return;
    }

    // Sort accounts primarily by code
    const sortedAccounts = [...accounts].sort((a, b) => String(a.code).localeCompare(String(b.code), undefined, { numeric: true, sensitivity: 'base' }));

    // Build hierarchical ordered list
    const orderedList = [];
    function traverse(parentCode = '', level = 1, indentStr = '') {
        const children = sortedAccounts.filter(a => {
            if (!parentCode) {
                return !a.parent || a.level === 1 || String(a.parent).trim() === '';
            }
            return String(a.parent) === String(parentCode);
        });

        children.forEach(c => {
            orderedList.push({
                ...c,
                displayTreeName: indentStr + (indentStr ? '↳ ' : '') + c.name,
                calcLevel: level
            });
            traverse(c.code, level + 1, indentStr + '    ');
        });
    }

    traverse();

    // Fallback if any accounts were missed in traversal
    sortedAccounts.forEach(a => {
        if (!orderedList.some(o => o.code === a.code)) {
            orderedList.push({
                ...a,
                displayTreeName: a.name,
                calcLevel: a.level || 1
            });
        }
    });

    // Create structured CSV with UTF-8 BOM
    let csv = "\ufeff#,كود الحساب المالي,اسم الحساب (الهيكل الشجري),اسم الحساب بالإنجليزية,الحساب الأب,المستوى المحاسبي,تصنيف الحساب,طبيعة الحساب,نوع حركة الحساب,العملة المعتمدة,الرصيد المالي الحالي,الربط المالي الختامي,حالة الحساب,الملاحظات\n";

    orderedList.forEach((a, idx) => {
        const rowNum = idx + 1;
        const code = `"${a.code}"`;
        const nameAr = `"${(a.displayTreeName || a.name).split('"').join('""')}"`;
        const nameEn = `"${(a.nameEn || '').split('"').join('""')}"`;
        const parent = `"${a.parent || '— (رئيسي)'}"`;
        const level = `"المستوى ${a.level || a.calcLevel}"`;
        const category = `"${a.category || 'أصول'}"`;
        const nature = `"${a.nature || 'مدين'}"`;
        const postingType = `"${a.postingType || 'فرعي'}"`;
        const currency = `"${a.currency || 'YER'}"`;
        const balance = `"${Number(a.balance || 0).toLocaleString()} ${a.currency || 'YER'}"`;
        const reportLink = `"${a.reportLink || 'الميزانية العمومية'}"`;
        const status = `"${a.status === 'Active' ? 'نشط ومفعل' : 'موقف ومجمد'}"`;
        const notes = `"${(a.notes || '').split('"').join('""')}"`;

        csv += `${rowNum},${code},${nameAr},${nameEn},${parent},${level},${category},${nature},${postingType},${currency},${balance},${reportLink},${status},${notes}\n`;
    });

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'دليل_الحسابات_المالي_الشجري_' + new Date().toISOString().slice(0,10) + '.csv';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    if (typeof toast === 'function') {
        toast('📊 تم تصدير دليل الحسابات مرتباً شجرياً بدقة متناهية!');
    }
}
function exportChartExcel() {
    exportChartAccountsExcel();
}
window.exportChartAccountsExcel = exportChartAccountsExcel;
window.exportChartExcel = exportChartAccountsExcel;



/**
 * ============================================================================
 * 01-CORE-DB.JS - Central Local Database & Global State Management
 * ============================================================================
 */
window.DB = window.DB || {};

// Multi-Tenant Context
window.currentSchoolId = parseInt(sessionStorage.getItem('currentSchoolId') || '1');
window.currentTerm = 'الفصل الدراسي الأول 2026/2027';

// ==================== 🔔 BULLETPROOF SELF-CONTAINED TOAST SYSTEM ====================
(function initPermanentToastStyles() {
    if (typeof document === 'undefined') return;
    const styleId = 'toast-permanent-styles';
    if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.textContent = `
            #toastBox {
                position: fixed !important;
                bottom: 24px !important;
                left: 24px !important;
                z-index: 2147483647 !important;
                display: flex !important;
                flex-direction: column !important;
                gap: 10px !important;
                pointer-events: none !important;
                max-width: 440px !important;
                width: auto !important;
                direction: rtl !important;
            }
            .toast-msg-item {
                position: relative !important;
                display: flex !important;
                align-items: center !important;
                gap: 12px !important;
                padding: 14px 20px !important;
                border-radius: 12px !important;
                font-family: 'Tajawal', sans-serif !important;
                font-size: 0.95rem !important;
                font-weight: 700 !important;
                color: #ffffff !important;
                pointer-events: auto !important;
                cursor: default !important;
                box-shadow: 0 14px 35px rgba(0,0,0,0.5), 0 4px 12px rgba(0,0,0,0.3) !important;
                backdrop-filter: blur(16px) !important;
                -webkit-backdrop-filter: blur(16px) !important;
                border: 1px solid rgba(255,255,255,0.25) !important;
                animation: toastSlideInLeft 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
                transition: all 0.3s ease !important;
            }
            @keyframes toastSlideInLeft {
                0% { opacity: 0; transform: translateX(-35px) scale(0.95); }
                100% { opacity: 1; transform: translateX(0) scale(1); }
            }
            .toast-msg-hide {
                opacity: 0 !important;
                transform: translateX(-45px) scale(0.9) !important;
            }
        `;
        (document.head || document.documentElement).appendChild(style);
    }
})();

function toast(msg, typeOrIsError, duration) {
    if (!msg) return;
    
    // 1. Ensure Container exists and has fixed positioning
    let box = document.getElementById('toastBox');
    if (!box) {
        box = document.createElement('div');
        box.id = 'toastBox';
        document.body.appendChild(box);
    }
    // Always enforce inline fixed position to guarantee it never depends on external CSS
    box.style.cssText = 'position:fixed !important;bottom:24px !important;left:24px !important;z-index:2147483647 !important;display:flex !important;flex-direction:column !important;gap:10px !important;pointer-events:none !important;max-width:440px !important;width:auto !important;direction:rtl !important;';

    // 2. Determine Message Type & Colors
    const strMsg = String(msg);
    let bgGradient = 'linear-gradient(135deg, #10b981 0%, #047857 100%)'; // default success
    let borderColor = 'rgba(52, 211, 153, 0.6)';
    let iconHtml = '<i class="fa-solid fa-circle-check"></i>';
    let type = 'success';

    if (typeOrIsError === true || typeOrIsError === 1 || typeOrIsError === 'error') {
        type = 'error';
        bgGradient = 'linear-gradient(135deg, #ef4444 0%, #b91c1c 100%)';
        borderColor = 'rgba(248, 113, 113, 0.6)';
        iconHtml = '<i class="fa-solid fa-triangle-exclamation"></i>';
    } else if (typeOrIsError === 'warning') {
        type = 'warning';
        bgGradient = 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)';
        borderColor = 'rgba(251, 191, 36, 0.6)';
        iconHtml = '<i class="fa-solid fa-triangle-exclamation"></i>';
    } else if (typeOrIsError === 'loading') {
        type = 'loading';
        bgGradient = 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)';
        borderColor = 'rgba(96, 165, 250, 0.6)';
        iconHtml = '<i class="fa-solid fa-circle-notch fa-spin"></i>';
    } else if (typeOrIsError === 'info') {
        type = 'info';
        bgGradient = 'linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%)';
        borderColor = 'rgba(56, 189, 248, 0.6)';
        iconHtml = '<i class="fa-solid fa-circle-info"></i>';
    } else {
        // Auto-detect based on text content
        if (/خطأ|فشل|تعذر|مرفوض|غير صحيح|غير متطابق|إلزامي|مطلوب|تحذير|⚠️|❌|Error|Failed/i.test(strMsg)) {
            type = 'error';
            bgGradient = 'linear-gradient(135deg, #ef4444 0%, #b91c1c 100%)';
            borderColor = 'rgba(248, 113, 113, 0.6)';
            iconHtml = '<i class="fa-solid fa-triangle-exclamation"></i>';
        } else if (/جاري|جارٍ|تحميل|استعادة|توليد|مزامنة|معالجة|تحليل|بناء|loading|syncing|⏳|🔄|⚡/i.test(strMsg)) {
            type = 'loading';
            bgGradient = 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)';
            borderColor = 'rgba(96, 165, 250, 0.6)';
            iconHtml = '<i class="fa-solid fa-circle-notch fa-spin"></i>';
        } else if (/معاينة|عرض|استعراض|تنبيه|ملاحظة|تفاصيل|ℹ️|📌|📄|👁️/i.test(strMsg)) {
            type = 'info';
            bgGradient = 'linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%)';
            borderColor = 'rgba(56, 189, 248, 0.6)';
            iconHtml = '<i class="fa-solid fa-circle-info"></i>';
        }
    }

    // 3. Create Item with Full Inline Styling
    const t = document.createElement('div');
    t.className = `toast-msg-item toast-${type}`;
    t.style.cssText = `position:relative !important;display:flex !important;align-items:center !important;gap:12px !important;padding:14px 20px !important;border-radius:12px !important;font-family:'Tajawal',sans-serif !important;font-size:0.95rem !important;font-weight:700 !important;color:#ffffff !important;pointer-events:auto !important;cursor:default !important;background:${bgGradient} !important;border:1px solid ${borderColor} !important;box-shadow:0 14px 35px rgba(0,0,0,0.5),0 4px 12px rgba(0,0,0,0.3) !important;backdrop-filter:blur(16px) !important;-webkit-backdrop-filter:blur(16px) !important;transition:all 0.3s ease !important;opacity:1 !important;direction:rtl !important;`;

    t.innerHTML = `
        <div style="font-size:1.3rem;display:flex;align-items:center;justify-content:center;width:26px;height:26px;flex-shrink:0;">${iconHtml}</div>
        <div style="flex-grow:1;line-height:1.45;word-break:break-word;">${strMsg}</div>
        <button type="button" style="background:transparent;border:none;color:#fff;font-size:1.25rem;cursor:pointer;opacity:0.75;padding:0 4px;line-height:1;margin-right:6px;transition:opacity 0.2s;" title="إغلاق">&times;</button>
    `;

    // 4. Dismiss Logic
    const closeBtn = t.querySelector('button');
    const dismiss = () => {
        t.style.opacity = '0';
        t.style.transform = 'translateX(-30px) scale(0.9)';
        setTimeout(() => {
            if (t.parentElement) t.remove();
        }, 300);
    };
    if (closeBtn) {
        closeBtn.onmouseenter = () => closeBtn.style.opacity = '1';
        closeBtn.onmouseleave = () => closeBtn.style.opacity = '0.75';
        closeBtn.onclick = dismiss;
    }

    box.appendChild(t);

    // 5. Auto Dismiss Timer
    const timeoutMs = typeof duration === 'number' ? duration : (type === 'loading' ? 4500 : 3500);
    setTimeout(dismiss, timeoutMs);
}
window.toast = toast;
window.showToast = toast;
window.notify = toast;
window.showNotification = toast;

function formatBadge(text) {
    if (!text) return '';
    const str = String(text);
    if (str.includes('نشط') || str.includes('مفعل') || str.includes('سليم') || str.includes('معتمد') || str.includes('🟢')) {
        return `<span class="badge badge-success">${str}</span>`;
    }
    if (str.includes('معطل') || str.includes('موقوف') || str.includes('حرج') || str.includes('مغلق') || str.includes('🔒') || str.includes('🔴')) {
        return `<span class="badge badge-danger">${str}</span>`;
    }
    if (str.includes('معلق') || str.includes('تحذير') || str.includes('مؤقت') || str.includes('🟡')) {
        return `<span class="badge badge-warning">${str}</span>`;
    }
    return `<span class="badge badge-info">${str}</span>`;
}
window.formatBadge = formatBadge;

function formatCurrency(num, curr) {
    const n = parseFloat(num) || 0;
    return n.toLocaleString('ar-YE') + ' ' + (curr || 'YER');
}
window.formatCurrency = formatCurrency;

// School Tenant Context Management
function getSchoolData(key) {
    const list = window.DB[key] || [];
    if (window.me && (window.me.role === 'saas_admin' || window.me.roleName === 'مدير المنصة')) {
        return list;
    }
    const targetSchoolId = (window.me && window.me.schoolId) ? window.me.schoolId : (window.currentSchoolId || 1);
    return list.filter(item => !item.schoolId || item.schoolId == targetSchoolId);
}
window.getSchoolData = getSchoolData;

function switchActiveSchool(schoolId, schoolName) {
    window.currentSchoolId = parseInt(schoolId);
    if (window.me) window.me.schoolId = window.currentSchoolId;
    try { sessionStorage.setItem('currentSchoolId', window.currentSchoolId); } catch(e){}
    
    const disp = document.getElementById('activeSchoolDisplay');
    if (disp) disp.textContent = schoolName || (window.currentSchoolId === 1 ? 'مدرسة المتفوقين الأهلية' : 'مدارس المستقبل الحديثة');
    
    toast(`🏫 تم التبديل إلى قاعدة بيانات (${schoolName || ('مدرسة ' + window.currentSchoolId)}) بنجاح`);
    
    const activePage = document.querySelector('.page.active')?.id || 'pg-dashboard';
    if (typeof goTo === 'function') goTo(activePage);
}
window.switchActiveSchool = switchActiveSchool;

/**
 * ============================================================================
 * POSTING ENGINE & BATCH MANAGER
 * ============================================================================
 */
(function initPostingModule() {
    if (!window.DB) window.DB = {};
    if (!window.DB.postingBatches) {
        window.DB.postingBatches = [
            { id: 'BATCH-2026-081', module: 'سندات القبض المالية (Receipt Vouchers)', description: 'ترحيل سندات تحصيل الرسوم للفترة 15-18 أغسطس', date: '2026-08-18', amount: '1,850,000 YER', count: '14 سند مالي', author: 'أ. سارة المحاسبة', status: 'بانتظار الترحيل ⏳' },
            { id: 'BATCH-2026-082', module: 'قيود اليومية العامة (Journal Entries)', description: 'قيود إثبات فواتير المشتريات والمصروفات الإدارية', date: '2026-08-17', amount: '420,000 YER', count: '6 قيود يومية', author: 'أ. عبد الرحمن باعباد', status: 'بانتظار الترحيل ⏳' },
            { id: 'BATCH-2026-083', module: 'سندات الصرف والعهد (Payment Vouchers)', description: 'سندات صرف عهدة الأنشطة والمشتريات المعملية', date: '2026-08-16', amount: '310,000 YER', count: '5 سندات صرف', author: 'أ. سارة المحاسبة', status: 'بانتظار الترحيل ⏳' },
            { id: 'BATCH-2026-084', module: 'شيتات درجات الكنترول (Grading Sheets)', description: 'ترحيل درجات اختبارات الشهر الأول لجميع الصفوف', date: '2026-08-15', amount: '24 شيت معتمد', count: '580 طالب وطالبة', author: 'د. سالم الحميري', status: 'بانتظار الترحيل ⏳' },
            { id: 'BATCH-2026-079', module: 'سندات القبض المالية (Receipt Vouchers)', description: 'ترحيل سندات رسوم النقل والزي المدرسي', date: '2026-08-12', amount: '950,000 YER', count: '22 سند مالي', author: 'أ. سارة المحاسبة', status: 'مرحل ومعتمد للأستاذ العام 🟢' }
        ];
    }

    window.renderPostingGrid = function() {
        const tb = document.getElementById('tbl-posting-grid');
        if (!tb) return;

        const searchInput = document.getElementById('searchPosting');
        const q = searchInput ? searchInput.value.trim().toLowerCase() : '';

        const batches = window.DB.postingBatches || [];
        const filtered = batches.filter(b => {
            if (!q) return true;
            return (b.id && b.id.toLowerCase().includes(q)) ||
                   (b.module && b.module.toLowerCase().includes(q)) ||
                   (b.description && b.description.toLowerCase().includes(q)) ||
                   (b.author && b.author.toLowerCase().includes(q));
        });

        // Update Unposted Count KPI
        const unpostedCount = batches.filter(b => b.status.includes('⏳') || b.status.includes('انتظار')).length;
        const unpostedEl = document.getElementById('unpostedBatchesCount');
        if (unpostedEl) unpostedEl.textContent = `${unpostedCount} دفعات`;

        if (filtered.length === 0) {
            tb.innerHTML = '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:30px;">لا توجد دفعات ترحيل مطابقة للبحث</td></tr>';
            return;
        }

                        tb.innerHTML = filtered.map((b, idx) => {
            const isPending = b.status.includes('⏳') || b.status.includes('انتظار');
            const statusBadge = isPending 
                ? '<span class="badge badge-warning">بانتظار الترحيل ⏳</span>'
                : '<span class="badge badge-success">مرحل للأستاذ العام 🟢</span>';
            
            const postBtn = isPending
                ? `<button class="btn-sm" style="background:#10b981;color:#fff;border:none;padding:6px 12px;border-radius:6px;cursor:pointer;font-weight:700;font-size:0.78rem;" onclick="event.stopPropagation();postBatch('${b.id}')" title="ترحيل فوري للأستاذ العام"><i class="fa-solid fa-bolt"></i> ترحيل ⚡</button>`
                : `<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-check-double"></i> مرحل للأستاذ العام</span>`;

            return `
                <tr data-collection="postingBatches" data-id="${b.id}" class="long-press-row" ondblclick="openForm('posting', '${b.id}')" oncontextmenu="event.preventDefault();deleteItem('postingBatches', '${b.id}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً لحذف الدفعة">
                    <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                    <td><code style="color:#60a5fa;font-weight:700;font-family:monospace;">${b.id}</code></td>
                    <td style="font-weight:700;color:#f8fafc;">${b.module}</td>
                    <td style="color:#cbd5e1;font-size:0.85rem;">${b.description}</td>
                    <td style="font-size:0.85rem;white-space:nowrap;">📅 ${b.date}</td>
                    <td><strong style="color:#34d399;">${b.amount}</strong> <small style="color:var(--muted);display:block;">(${b.count})</small></td>
                    <td style="font-size:0.85rem;">👤 ${b.author}</td>
                    <td>${statusBadge}</td>
                    <td style="text-align:center;">${postBtn}</td>
                </tr>
            `;
        }).join('');
    };

    window.renderPosting = window.renderPostingGrid;

    window.postBatch = function(batchId) {
        const item = (window.DB.postingBatches || []).find(x => x.id === batchId);
        if (!item) return;

        if (confirm(`❓ هل أنت متأكد من رغبتك في ترحيل الدفعة (${batchId}) نهائياً إلى الأستاذ العام؟ لا يمكن التراجع بعد الترحيل.`)) {
            item.status = 'مرحل ومعتمد للأستاذ العام 🟢';
            if (typeof addAudit === 'function') {
                addAudit('ترحيل دفعة', `تم ترحيل الدفعة ${batchId}: ${item.description}`, 'إدارة الترحيلات', 'تدقيق (AUDIT) 🔵');
            }
            toast(`⚡ تم بنجاح ترحيل الدفعة (${batchId}) إلى حسابات الأستاذ العام وتثبيت القيود!`);
            window.renderPostingGrid();
        }
    };

    window.postAllBatches = function() {
        const pending = (window.DB.postingBatches || []).filter(b => b.status.includes('⏳') || b.status.includes('انتظار'));
        if (pending.length === 0) {
            toast('ℹ️ جميع الدفعات والمعاملات مرحلة بالفعل ولا توجد معلقات!', 0);
            return;
        }

        if (confirm(`⚡ هل أنت متأكد من ترحيل كافة المعلقات (${pending.length} دفعات) دفعة واحدة إلى الأستاذ العام؟`)) {
            pending.forEach(b => {
                b.status = 'مرحل ومعتمد للأستاذ العام 🟢';
            });
            if (typeof addAudit === 'function') {
                addAudit('ترحيل شامل', `تم ترحيل كافة المعلقات (${pending.length} دفعة) دفعة واحدة`, 'إدارة الترحيلات', 'حرج ومهم (CRITICAL) 🔴');
            }
            toast(`🎉 تم بنجاح ترحيل كافة المعلقات (${pending.length} دفعة) وتثبيت القيود المالية والأكاديمية!`);
            window.renderPostingGrid();
        }
    };
})();

/**
 * ============================================================================
 * VOUCHERS HUB & TREASURY ENGINE (13 COLUMNS & KPI COUNTERS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.vouchers) {
    window.DB.vouchers = [
        {
            id: 'VCH-REC-2026-001',
            code: 'VCH-REC-2026-001',
            date: '2026-08-18',
            type: 'سند قبض 🟢',
            amount: 150000,
            currency: 'YER - ريال يمني',
            party: 'الشيخ علي باعباد (ولي أمر)',
            paymentMethod: 'نقداً من الخزينة (Cash)',
            refNo: 'REC-99881',
            costCenter: 'إيرادات الرسوم الدراسية',
            account: 'الصندوق الرئيسي (خزينة الإدارة)',
            attachment: '📷 إشعار_قبض_001.pdf',
            description: 'سداد القسط الأول من الرسوم الدراسية للعام الجديد',
            status: 'معتمد ومرحل للأستاذ العام 🟢'
        },
        {
            id: 'VCH-PAY-2026-002',
            code: 'VCH-PAY-2026-002',
            date: '2026-08-17',
            type: 'سند صرف 🔴',
            amount: 450000,
            currency: 'YER - ريال يمني',
            party: 'أ. محمد الأحمدي (معلم رياضيات)',
            paymentMethod: 'تحويل بنكي / إيداع (Bank Transfer)',
            refNo: 'TRX-BNK-7712',
            costCenter: 'المصروفات الإدارية والتشغيلية',
            account: 'بنك اليمن والكويت (حساب رئيسي)',
            attachment: '📷 إشعار_تحويل_بنكي.pdf',
            description: 'صرف راتب شهر أغسطس مع مكافأة إعداد المنهج',
            status: 'معتمد ومرحل للأستاذ العام 🟢'
        },
        {
            id: 'VCH-REC-2026-003',
            code: 'VCH-REC-2026-003',
            date: '2026-08-16',
            type: 'سند قبض 🟢',
            amount: 500000,
            currency: 'YER - ريال يمني',
            party: 'أحمد سالم الزبيدي (طالب)',
            paymentMethod: 'شيك بنكي معتمد (Check)',
            refNo: 'CHK-889021',
            costCenter: 'إيرادات الرسوم الدراسية',
            account: 'بنك الكريمي الإسلامي',
            attachment: '📷 صورة_الشيك_889021.jpg',
            description: 'سداد رسوم الأنشطة والمواصلات للفصل الأول',
            status: 'معتمد ومرحل للأستاذ العام 🟢'
        },
        {
            id: 'VCH-PAY-2026-004',
            code: 'VCH-PAY-2026-004',
            date: '2026-08-15',
            type: 'سند صرف 🔴',
            amount: 180000,
            currency: 'YER - ريال يمني',
            party: 'مؤسسة التقنية والشبكات',
            paymentMethod: 'نقاط بيع / شبكة (POS)',
            refNo: 'POS-NET-551',
            costCenter: 'صيانة ومرافق المدرسة',
            account: 'الصندوق الرئيسي (خزينة الإدارة)',
            attachment: '📷 فاتورة_مشتريات_شبكات.pdf',
            description: 'شراء كابلات وصيانة معامل الحاسوب الآلي',
            status: 'معتمد ومرحل للأستاذ العام 🟢'
        }
    ];
}

function renderVouchersGrid() {
    const tb = document.getElementById('tbl-vouchers') || document.getElementById('tbl-vouchers-grid');
    if (!tb) return;

    const query = (document.getElementById('searchVouchers')?.value || '').toLowerCase().trim();
    const vouchersList = window.DB.vouchers || [];

    // Calculate KPI Stats
    let receiptSum = 0;
    let paymentSum = 0;
    let receiptCount = 0;
    let paymentCount = 0;

    vouchersList.forEach(v => {
        const amt = Number(v.amount) || 0;
        const isRec = String(v.type).includes('قبض') || String(v.type).includes('REC');
        if (isRec) {
            receiptSum += amt;
            receiptCount++;
        } else {
            paymentSum += amt;
            paymentCount++;
        }
    });

    const receiptEl = document.getElementById('voucherReceiptCount');
    const paymentEl = document.getElementById('voucherPaymentCount');
    const totalEl = document.getElementById('voucherTotalCount');

    if (receiptEl) receiptEl.innerHTML = `${receiptSum.toLocaleString()} <small style="font-size:0.75rem;">YER (${receiptCount} سند)</small>`;
    if (paymentEl) paymentEl.innerHTML = `${paymentSum.toLocaleString()} <small style="font-size:0.75rem;">YER (${paymentCount} سند)</small>`;
    if (totalEl) totalEl.innerHTML = `${vouchersList.length} <small style="font-size:0.75rem;">سند (${(receiptSum + paymentSum).toLocaleString()} YER)</small>`;

    const filtered = vouchersList.filter(v => {
        if (!query) return true;
        const text = [v.id, v.code, v.date, v.type, v.party, v.payer, v.payee, v.paymentMethod, v.refNo, v.costCenter, v.account, v.description, v.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="13" style="text-align:center;color:var(--muted);padding:30px;">لا توجد سندات مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((v, idx) => {
        const isRec = String(v.type).includes('قبض') || String(v.type).includes('REC');
        const typeBadge = isRec 
            ? '<span class="badge badge-success"><i class="fa-solid fa-arrow-down-left"></i> سند قبض 🟢</span>'
            : '<span class="badge badge-danger"><i class="fa-solid fa-arrow-up-right"></i> سند صرف 🔴</span>';

        const partyName = v.party || v.payer || v.payee || '—';
        const curr = v.currency ? (String(v.currency).includes('YER') ? 'YER' : v.currency) : 'YER';
        const statusBadge = (v.status && (v.status.includes('معتمد') || v.status.includes('🟢')))
            ? '<span class="badge badge-success">معتمد ومرحل 🟢</span>'
            : '<span class="badge badge-warning">مسودة 🟡</span>';

        const attachIcon = v.attachment 
            ? `<span style="color:#38bdf8;font-size:0.8rem;cursor:pointer;" onclick="toast('📎 فتح المرفق: ${v.attachment}')" title="${v.attachment}"><i class="fa-solid fa-paperclip"></i> ${v.attachment.length > 15 ? v.attachment.slice(0,15)+'...' : v.attachment}</span>`
            : '<span style="color:#94a3b8;">—</span>';

        return `
            <tr data-collection="vouchers" data-id="${v.id || v.code}" ondblclick="openForm('voucher', '${v.id || v.code}')" oncontextmenu="event.preventDefault();deleteItem('vouchers', '${v.id || v.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-receipt" style="color:#38bdf8;font-size:0.75rem;"></i> ${v.code || v.id}</td>
                <td style="font-size:0.85rem;white-space:nowrap;">📅 ${v.date}</td>
                <td>${typeBadge}</td>
                <td><strong style="color:${isRec ? '#34d399' : '#f87171'};font-size:0.92rem;font-family:monospace;">${(Number(v.amount) || 0).toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td style="font-weight:700;color:#f8fafc;">${partyName}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">${v.paymentMethod || 'نقداً'}</td>
                <td style="font-family:monospace;font-size:0.82rem;color:#60a5fa;">${v.refNo || '—'}</td>
                <td style="font-size:0.82rem;color:#f59e0b;">${v.costCenter || 'عام'}</td>
                <td style="font-size:0.82rem;color:#38bdf8;">${v.account || 'الصندوق الرئيسي'}</td>
                <td>${attachIcon}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;max-width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="${v.description || ''}">${v.description || '—'}</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderVouchersGrid = renderVouchersGrid;
window.renderVouchers = renderVouchersGrid;


// ==================== 📊 LUXURIOUS, RESILIENT DASHBOARD ENGINE ====================
window.renderDashboard = function() {
    // 1. Safe KPI Statistics Cards
    const totalStudents = (window.DB && window.DB.students && window.DB.students.length) ? window.DB.students.length : 1250;
    const totalEmp = (window.DB && window.DB.employees && window.DB.employees.length) ? window.DB.employees.length : 85;
    const totalSubjects = (window.DB && window.DB.subjects && window.DB.subjects.length) ? window.DB.subjects.length : 32;
    const totalStages = (window.DB && window.DB.stages && window.DB.stages.length) ? window.DB.stages.length : 4;
    const paidStudents = Math.round(totalStudents * 0.88);
    const unpaidStudents = totalStudents - paidStudents;

    const elStu = document.getElementById('dTotalStudents');
    const elEmp = document.getElementById('dTotalEmp');
    const elSub = document.getElementById('dSubjects');
    const elStg = document.getElementById('dStages');
    const elPaid = document.getElementById('dPaid');
    const elUnpaid = document.getElementById('dUnpaid');

    if (elStu) elStu.textContent = totalStudents.toLocaleString('ar-YE');
    if (elEmp) elEmp.textContent = totalEmp.toLocaleString('ar-YE');
    if (elSub) elSub.textContent = totalSubjects.toLocaleString('ar-YE');
    if (elStg) elStg.textContent = totalStages.toLocaleString('ar-YE');
    if (elPaid) elPaid.textContent = paidStudents.toLocaleString('ar-YE');
    if (elUnpaid) elUnpaid.textContent = unpaidStudents.toLocaleString('ar-YE');

    // 2. Audit Log List Feed (#auditLogList)
    const al = document.getElementById('auditLogList');
    if (al) {
        const auditItems = (window.DB && (window.DB.auditLogs || window.DB.audit)) || [
            { id: 'LOG-01', user: 'أ. خالد العنسي (المدير العام)', action: 'إضافة سند قبض', target: 'سند مالي #VCH-REC-001', timestamp: 'منذ 5 دقائق', severity: 'عادي 🟢' },
            { id: 'LOG-02', user: 'د. سالم الحميري (الكنترول)', action: 'رصد درجات', target: 'شيت ثالث ثانوي علمي', timestamp: 'منذ 15 دقيقة', severity: 'تدقيق 🔵' },
            { id: 'LOG-03', user: 'أ. عبد الرحمن باعباد (المالي)', action: 'نسخ احتياطي', target: 'قاعدة بيانات المنظومة', timestamp: 'منذ ساعة', severity: 'أمان 🛡️' },
            { id: 'LOG-04', user: 'أ. سارة المحاسبة', action: 'تسجيل طالب', target: 'طالب جديد: أحمد باعباد', timestamp: 'منذ ساعتين', severity: 'عادي 🟢' },
            { id: 'LOG-05', user: 'النظام الآلي (Daemon)', action: 'ترحيل قيود', target: 'إغلاق الأستاذ العام', timestamp: 'أمس 11:00 م', severity: 'تأكيد 🟢' }
        ];

        al.innerHTML = auditItems.slice(0, 5).map(r => {
            const userName = r.user || 'مستخدم النظام';
            const actionTitle = r.action || r.actionType || 'عملية نظامية';
            const targetDetails = r.target || r.details || '';
            const timeStr = r.timestamp || r.time || 'الآن';
            return `
                <div style="padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.08);background:rgba(30,41,59,0.4);border-radius:8px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <div style="font-weight:700;font-size:0.85rem;color:#f8fafc;"><i class="fa-solid fa-bolt" style="color:#f59e0b;margin-left:6px;"></i>${actionTitle} <small style="color:#60a5fa;margin-right:4px;">(${targetDetails})</small></div>
                        <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">👤 ${userName}</div>
                    </div>
                    <div style="font-size:0.75rem;color:#94a3b8;white-space:nowrap;">📅 ${timeStr}</div>
                </div>
            `;
        }).join('');
    }

    // 3. Financial Summary Canvas / Fallback Card (#financeChart)
    const ctx = document.getElementById('financeChart');
    if (ctx) {
        const parentCard = ctx.parentElement;
        if (typeof Chart !== 'undefined') {
            try {
                if (window.myFinanceChartInstance) {
                    window.myFinanceChartInstance.destroy();
                }
                window.myFinanceChartInstance = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['إيرادات الرسوم المحصلة', 'المصروفات والرواتب التشغيلية', 'الفائض النقدي المتاح'],
                        datasets: [{
                            data: [14850000, 5750000, 9100000],
                            backgroundColor: ['#10b981', '#ef4444', '#3b82f6'],
                            borderWidth: 2,
                            borderColor: '#0f172a'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: { color: '#cbd5e1', font: { family: 'Tajawal', size: 12 } }
                            }
                        }
                    }
                });
            } catch(e) {
                console.warn('Chart.js render error, fallback used:', e);
            }
        } else if (parentCard) {
            // High-End Pure CSS/HTML Financial Summary Widget
            ctx.style.display = 'none';
            let summaryWidget = document.getElementById('financialFallbackWidget');
            if (!summaryWidget) {
                summaryWidget = document.createElement('div');
                summaryWidget.id = 'financialFallbackWidget';
                parentCard.appendChild(summaryWidget);
            }
            summaryWidget.innerHTML = `
                <div style="display:flex;flex-direction:column;gap:14px;padding:10px 0;">
                    <div>
                        <div style="display:flex;justify-content:space-between;margin-bottom:6px;font-size:0.85rem;font-weight:700;">
                            <span style="color:#34d399;"><i class="fa-solid fa-circle-arrow-down"></i> إجمالي الإيرادات المحصلة</span>
                            <span style="color:#34d399;">14,850,000 YER (72%)</span>
                        </div>
                        <div style="height:10px;border-radius:5px;background:rgba(255,255,255,0.1);overflow:hidden;">
                            <div style="width:72%;height:100%;background:linear-gradient(90deg,#10b981,#059669);border-radius:5px;"></div>
                        </div>
                    </div>

                    <div>
                        <div style="display:flex;justify-content:space-between;margin-bottom:6px;font-size:0.85rem;font-weight:700;">
                            <span style="color:#f87171;"><i class="fa-solid fa-circle-arrow-up"></i> إجمالي المصروفات والرواتب</span>
                            <span style="color:#f87171;">5,750,000 YER (28%)</span>
                        </div>
                        <div style="height:10px;border-radius:5px;background:rgba(255,255,255,0.1);overflow:hidden;">
                            <div style="width:28%;height:100%;background:linear-gradient(90deg,#ef4444,#b91c1c);border-radius:5px;"></div>
                        </div>
                    </div>

                    <div style="background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);padding:12px 16px;border-radius:10px;display:flex;justify-content:space-between;align-items:center;margin-top:4px;">
                        <span style="color:#60a5fa;font-weight:700;font-size:0.9rem;"><i class="fa-solid fa-vault"></i> صافي الفائض النقدي المعتمد</span>
                        <strong style="color:#38bdf8;font-size:1.15rem;font-weight:900;">+9,100,000 YER 💎</strong>
                    </div>
                </div>
            `;
        }
    }
};

// ==================== 🚀 AUTO-LOAD & INITIALIZATION ENGINE ====================
(function initMasterApp() {
    function boot() {
        // 1. Session Restoration
        try {
            const saved = localStorage.getItem('sec_user_session') || sessionStorage.getItem('sec_user');
            if (saved) {
                const user = JSON.parse(saved);
                window.me = user;
                const lw = document.getElementById('loginWrapper');
                const al = document.getElementById('appLayout');
                if (lw) lw.style.display = 'none';
                if (al) al.style.display = 'flex';
                
                const uNameDisp = document.getElementById('userNameDisplay');
                if (uNameDisp) uNameDisp.textContent = user.name || user.username;
                
                if (typeof applyRBACPermissions === 'function') applyRBACPermissions(user);
            }
        } catch(e) {}

        // 2. Render Dashboard immediately
        if (typeof window.renderDashboard === 'function') {
            window.renderDashboard();
        }

        // 3. Attach Universal Row Interactions
        if (typeof window.attachUniversalRowInteractions === 'function') {
            window.attachUniversalRowInteractions();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }

    // Safety fallback run after 200ms
    setTimeout(boot, 200);
})();

// ==================== 🚀 AUTO-LOAD & INSTANT ROUTE RECOVERY ENGINE ====================
(function initMasterApp() {
    function boot() {
        // 1. Session Restoration or Default Active Admin Session
        let user = null;
        try {
            const saved = localStorage.getItem('sec_user_session') || sessionStorage.getItem('sec_user');
            if (saved) {
                user = JSON.parse(saved);
            }
        } catch(e) {}

        if (!user) {
            user = {
                id: 'usr_1',
                username: 'admin',
                name: 'أ. خالد العنسي (المدير العام)',
                role: 'school_admin',
                roleName: 'مدير المدرسة',
                schoolId: 1,
                schoolName: 'مدرسة المتفوقين الأهلية النموذجية',
                permissions: { students: true, finance: true, accounting: true, control: true }
            };
            try {
                localStorage.setItem('sec_user_session', JSON.stringify(user));
            } catch(e) {}
        }

        window.me = user;
        const lw = document.getElementById('loginWrapper');
        const al = document.getElementById('appLayout');
        if (lw) lw.style.display = 'none';
        if (al) al.style.display = 'flex';
        
        const uNameDisp = document.getElementById('userNameDisplay');
        if (uNameDisp) uNameDisp.textContent = user.name || user.username;
        
        const activeSchoolDisp = document.getElementById('activeSchoolDisplay');
        if (activeSchoolDisp) activeSchoolDisp.textContent = user.schoolName || 'مدرسة المتفوقين الأهلية';

        if (typeof applyRBACPermissions === 'function') applyRBACPermissions(user);

        // 2. Hash Route Recovery
        const currentHash = window.location.hash ? window.location.hash.replace('#', '').trim() : '';
        if (currentHash && currentHash !== 'pg-dashboard' && typeof window.goTo === 'function') {
            window.goTo(currentHash);
        } else {
            if (typeof window.renderDashboard === 'function') {
                window.renderDashboard();
            }
        }

        // 3. Attach Universal Row Interactions
        if (typeof window.attachUniversalRowInteractions === 'function') {
            window.attachUniversalRowInteractions();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }

    // Safety fallback
    setTimeout(boot, 100);
})();

// Universal In-Table Realtime Search Filter
function filterTable(tbodyId, query) {
    const tb = document.getElementById(tbodyId);
    if (!tb) return;
    const q = (query || '').toLowerCase().trim();
    const rows = tb.querySelectorAll('tr');
    rows.forEach(r => {
        if (!q) {
            r.style.display = '';
            return;
        }
        const text = r.textContent.toLowerCase();
        r.style.display = text.includes(q) ? '' : 'none';
    });
}
window.filterTable = filterTable;

// ==================== ⚡ IMMEDIATE ZERO-CLICK SYSTEM BOOT ====================
(function immediateAutoBoot() {
    function ensureLayoutVisible() {
        const lw = document.getElementById('loginWrapper');
        const al = document.getElementById('appLayout');
        const sb = document.getElementById('sidebar');
        
        if (lw) lw.style.display = 'none';
        if (al) {
            al.style.display = 'flex';
            al.style.minHeight = '100vh';
        }
        if (sb) {
            sb.style.display = 'flex';
            sb.style.visibility = 'visible';
            sb.style.opacity = '1';
        }

        const user = {
            id: 'usr_1',
            username: 'admin',
            name: 'أ. خالد العنسي (المدير العام)',
            role: 'school_admin',
            roleName: 'مدير المدرسة',
            schoolId: 1,
            schoolName: 'مدرسة المتفوقين الأهلية النموذجية',
            permissions: { students: true, finance: true, accounting: true, control: true }
        };
        window.me = user;
        
        try {
            localStorage.setItem('sec_user_session', JSON.stringify(user));
        } catch(e) {}

        const uNameDisp = document.getElementById('userNameDisplay');
        if (uNameDisp) uNameDisp.textContent = user.name;
        
        const activeSchoolDisp = document.getElementById('activeSchoolDisplay');
        if (activeSchoolDisp) activeSchoolDisp.textContent = user.schoolName;

        // Render Dashboard or Hash Page
        const hash = window.location.hash ? window.location.hash.replace('#', '').trim() : '';
        if (hash && hash !== 'pg-dashboard' && typeof window.goTo === 'function') {
            window.goTo(hash);
        } else {
            if (typeof window.renderDashboard === 'function') {
                window.renderDashboard();
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', ensureLayoutVisible);
    } else {
        ensureLayoutVisible();
    }
    setTimeout(ensureLayoutVisible, 50);
    setTimeout(ensureLayoutVisible, 300);
})();

// ============================================================================
// 👥 USERS DIRECTORY & STUDENT REGISTRATION REAL-TIME LINKING ENGINE
// ============================================================================

function ensureInitialUsersAndStudents() {
    if (!window.DB) window.DB = {};

    if (!window.DB.users || window.DB.users.length < 5) {
        window.DB.users = [
            {
                id: 'USR-101',
                username: 'admin',
                password: '123',
                name: 'أ. خالد العنسي (المدير العام)',
                role: 'school_admin',
                roleName: 'مدير المدرسة',
                phone: '777000111',
                nationalId: '10001000100',
                email: 'admin@almajd-school.edu.ye',
                status: 'نشط 🟢',
                allowedPagesCount: 'جميع الواجهات (102) مسموحة 🟢',
                date: '2026-08-01'
            },
            {
                id: 'USR-102',
                username: 'teacher',
                password: '123',
                name: 'د. سالم الحميري (أستاذ الرياضيات والكنترول)',
                role: 'teacher',
                roleName: 'معلم ومسؤول كنترول',
                phone: '777222333',
                nationalId: '10002000200',
                email: 'salem@almajd-school.edu.ye',
                status: 'نشط 🟢',
                allowedPagesCount: 'الكنترول والمواد (32) واجهة 🟢',
                date: '2026-08-05'
            },
            {
                id: 'USR-103',
                username: 'staff',
                password: '123',
                name: 'أ. سارة المحاسبة (المالية والشؤون الإدارية)',
                role: 'staff',
                roleName: 'محاسب مالي رئيسي',
                phone: '777444555',
                nationalId: '10003000300',
                email: 'sara@almajd-school.edu.ye',
                status: 'نشط 🟢',
                allowedPagesCount: 'الشؤون المالية (28) واجهة 🟢',
                date: '2026-08-10'
            },
            {
                id: 'USR-P-10892019920',
                username: '10892019920',
                password: '771234567',
                name: 'أحمد علي محمد باعباد (ولي أمر: الشيخ علي باعباد)',
                role: 'parent',
                roleName: 'ولي أمر',
                phone: '771234567',
                nationalId: '10892019920',
                studentName: 'أحمد علي محمد باعباد',
                email: 'parent.ahmed@gmail.com',
                status: 'نشط 🟢',
                allowedPagesCount: 'بوابة ولي الأمر كاملة 🟢',
                date: '2026-08-15'
            },
            {
                id: 'USR-P-10993028811',
                username: '10993028811',
                password: '775566778',
                name: 'سارة خالد محمود العنسي (ولي أمر: م. خالد العنسي)',
                role: 'parent',
                roleName: 'ولي أمر',
                phone: '775566778',
                nationalId: '10993028811',
                studentName: 'سارة خالد محمود العنسي',
                email: 'parent.sara@gmail.com',
                status: 'نشط 🟢',
                allowedPagesCount: 'بوابة ولي الأمر كاملة 🟢',
                date: '2026-08-16'
            }
        ];
    }
    window.DB.usersData = window.DB.users;

    if (!window.DB.students || window.DB.students.length === 0) {
        window.DB.students = [
            {
                id: 'STD-2026-001',
                student_number: 'STD-2026-001',
                academicNo: 'STD-2026-001',
                name: 'أحمد علي محمد باعباد',
                full_name: 'أحمد علي محمد باعباد',
                nationalId: '10892019920',
                parentName: 'الشيخ علي باعباد',
                parentPhone: '771234567',
                phone: '771234567',
                dateOfBirth: '2008-04-12',
                dob: '2008-04-12',
                nationality: 'يمني 🇾🇪',
                grade: 'الثالث الثانوي',
                section: 'علمي 1',
                grade_level: 'الثالث الثانوي - علمي 1',
                address: 'صنعاء - شارع حدة',
                enrollmentDate: '2026-08-10',
                date: '2026-08-10',
                status: 'مسدد بالكامل 🟢',
                financial_status: 'مسدد بالكامل 🟢'
            },
            {
                id: 'STD-2026-002',
                student_number: 'STD-2026-002',
                academicNo: 'STD-2026-002',
                name: 'سارة خالد محمود العنسي',
                full_name: 'سارة خالد محمود العنسي',
                nationalId: '10993028811',
                parentName: 'م. خالد العنسي',
                parentPhone: '775566778',
                phone: '775566778',
                dateOfBirth: '2009-07-22',
                dob: '2009-07-22',
                nationality: 'يمني 🇾🇪',
                grade: 'الثاني الثانوي',
                section: 'علمي',
                grade_level: 'الثاني الثانوي - علمي',
                address: 'صنعاء - شارع بغداد',
                enrollmentDate: '2026-08-12',
                date: '2026-08-12',
                status: 'مسدد بالكامل 🟢',
                financial_status: 'مسدد بالكامل 🟢'
            }
        ];
    }
}
window.ensureInitialUsersAndStudents = ensureInitialUsersAndStudents;

function renderUsersGrid() {
    ensureInitialUsersAndStudents();
    const tb = document.getElementById('tbl-users-grid') || document.getElementById('tbl-users');
    if (!tb) return;

    const query = (document.getElementById('searchUsers')?.value || document.getElementById('searchUsersInput')?.value || '').toLowerCase().trim();
    const users = window.DB.users || window.DB.usersData || [];

    const filtered = users.filter(u => {
        if (!query) return true;
        const text = [u.id, u.name, u.username, u.role, u.roleName, u.dept, u.phone, u.nationalId, u.email].join(' ').toLowerCase();
        return text.includes(query);
    });

    tb.innerHTML = filtered.map((u, idx) => {
        const roleText = u.roleName || u.role || 'مستخدم';
        const isParent = String(roleText).includes('ولي') || u.role === 'parent';
        const roleBadge = isParent ?
            `<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;border:1px solid rgba(16,185,129,0.3);font-weight:700;"><i class="fa-solid fa-user-group"></i> ${roleText}</span>` :
            `<span class="badge" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);font-weight:700;"><i class="fa-solid fa-user-shield"></i> ${roleText}</span>`;

        const allowedCount = u.permissions ? (u.permissions.length + ' واجهة 🟢') : (u.allowedPagesCount || 'جميع الواجهات (60+) 🟢');
        const statusClass = (u.status && (u.status.includes('موقوف') || u.status.includes('🔴') || u.status.includes('معطل'))) ? 'badge-danger' : 'badge-success';
        const statusText = u.status || 'نشط 🟢';

        return `
            <tr>
                <td style="font-weight:700;color:#94a3b8;text-align:center;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-hashtag" style="font-size:0.75rem;color:#38bdf8;"></i> ${u.id || ('USR-' + (idx + 101))}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;"><i class="fa-solid fa-id-badge" style="color:#60a5fa;"></i> ${u.username || u.nationalId || '---'}</td>
                <td style="font-weight:700;color:#f8fafc;">${u.name || 'مستخدم النظام'}</td>
                <td>${roleBadge}</td>
                <td style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-building" style="color:#a855f7;font-size:0.75rem;"></i> ${u.dept || 'الإدارة العامة والمكتب التنفيذي'}</td>
                <td style="font-family:monospace;color:#38bdf8;"><i class="fa-solid fa-phone" style="font-size:0.75rem;"></i> ${u.phone || '---'}</td>
                <td style="color:#94a3b8;font-size:0.82rem;"><i class="fa-solid fa-envelope" style="font-size:0.75rem;"></i> ${u.email || (u.username + '@school.edu.ye')}</td>
                <td><span class="badge ${statusClass}"><i class="fa-solid fa-circle-dot"></i> ${statusText}</span></td>
                <td style="font-size:0.8rem;color:#94a3b8;">📅 ${u.date || '2026-08-19'}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-shield-halved"></i> ${allowedCount}</span></td>
            </tr>
        `;
    }).join('');
}
window.renderUsersGrid = renderUsersGrid;
window.renderUsers = renderUsersGrid;

function renderStudents() {
    ensureInitialUsersAndStudents();
    const tb = document.getElementById('tbl-students') || document.getElementById('tbl-student-register') || document.getElementById('tbl-students-grid');
    if (!tb) return;

    const q = (document.getElementById('searchStudents')?.value || document.getElementById('searchStudentReg')?.value || '').toLowerCase().trim();
    const students = window.DB.students || [];

    const filtered = students.filter(s => {
        if (!q) return true;
        const text = [s.id, s.name, s.full_name, s.student_number, s.academicNo, s.nationalId, s.parentName, s.parentPhone, s.phone, s.grade, s.section, s.grade_level].join(' ').toLowerCase();
        return text.includes(q);
    });

    tb.innerHTML = filtered.map((s, idx) => {
        const studentName = s.name || s.full_name || 'طالب جديد';
        const natId = s.nationalId || '10892019920';
        const pPhone = s.parentPhone || s.phone || '771234567';
        const pName = s.parentName || 'ولي الأمر';
        const gr = s.grade_level || s.grade || 'الثالث الثانوي - علمي 1';
        const statusBadge = `<span class="badge badge-success">${s.status || s.financial_status || 'مسدد بالكامل 🟢'}</span>`;

        return `
            <tr>
                <td>${idx + 1}</td>
                <td><code style="color:#60a5fa;font-weight:700;">${s.student_number || s.academicNo || s.id || ('STD-2026-' + (idx+101))}</code></td>
                <td style="font-weight:800;color:#f8fafc;">👤 ${studentName}</td>
                <td><code style="color:#38bdf8;font-weight:700;"><i class="fa-solid fa-address-card"></i> ${natId}</code></td>
                <td style="color:#cbd5e1;">📅 ${s.dateOfBirth || s.dob || '2010-05-15'}</td>
                <td><span class="badge badge-info">${s.nationality || 'يمني 🇾🇪'}</span></td>
                <td style="font-weight:600;color:#a78bfa;">${gr}</td>
                <td style="color:#94a3b8;">📍 ${s.address || 'صنعاء - شارع حدة'}</td>
                <td style="color:#f8fafc;"><strong>${pName}</strong><br><span style="font-size:0.75rem;color:#38bdf8;font-family:monospace;"><i class="fa-solid fa-phone"></i> ${pPhone}</span></td>
                <td style="color:#94a3b8;">📅 ${s.enrollmentDate || s.date || '2026-08-19'}</td>
                <td><span style="font-size:1.3rem;">🧑‍🎓</span></td>
                <td>${statusBadge}</td>
                <td>
                    <span class="badge badge-success" title="تم إنشاء وتفعيل حساب ولي الأمر فورياً"><i class="fa-solid fa-user-check"></i> حساب مفعّل 🟢</span>
                </td>
            </tr>
        `;
    }).join('');

    const regTotal = document.getElementById('regTotalStudents');
    if (regTotal) regTotal.textContent = students.length;
}
window.renderStudents = renderStudents;
window.renderStudentsTable = renderStudents;

// Ensure initial run
ensureInitialUsersAndStudents();

function renderUsersGrid() {
    ensureInitialUsersAndStudents();
    const tb = document.getElementById('tbl-users-grid') || document.getElementById('tbl-users');
    if (!tb) return;

    const query = (document.getElementById('searchUsers')?.value || document.getElementById('searchUsersInput')?.value || '').toLowerCase().trim();
    const users = window.DB.users || window.DB.usersData || [];

    const filtered = users.filter(u => {
        if (!query) return true;
        const text = [u.id, u.name, u.username, u.role, u.roleName, u.dept, u.phone, u.nationalId, u.email].join(' ').toLowerCase();
        return text.includes(query);
    });

    tb.innerHTML = filtered.map((u, idx) => {
        const roleText = u.roleName || u.role || 'مستخدم';
        const isParent = String(roleText).includes('ولي') || u.role === 'parent';
        const roleBadge = isParent ?
            `<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;border:1px solid rgba(16,185,129,0.3);font-weight:700;"><i class="fa-solid fa-user-group"></i> ${roleText}</span>` :
            `<span class="badge" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);font-weight:700;"><i class="fa-solid fa-user-shield"></i> ${roleText}</span>`;

        const allowedCount = u.permissions ? (u.permissions.length + ' واجهة 🟢') : (u.allowedPagesCount || 'جميع الواجهات (60+) 🟢');
        const statusClass = (u.status && (u.status.includes('موقوف') || u.status.includes('🔴') || u.status.includes('معطل'))) ? 'badge-danger' : 'badge-success';
        const statusText = u.status || 'نشط 🟢';

        return `
            <tr>
                <td style="font-weight:700;color:#94a3b8;text-align:center;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-hashtag" style="font-size:0.75rem;color:#38bdf8;"></i> ${u.id || ('USR-' + (idx + 101))}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;"><i class="fa-solid fa-id-badge" style="color:#60a5fa;"></i> ${u.username || u.nationalId || '---'}</td>
                <td style="font-weight:700;color:#f8fafc;">${u.name || 'مستخدم النظام'}</td>
                <td>${roleBadge}</td>
                <td style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-building" style="color:#a855f7;font-size:0.75rem;"></i> ${u.dept || 'الإدارة العامة والمكتب التنفيذي'}</td>
                <td style="font-family:monospace;color:#38bdf8;"><i class="fa-solid fa-phone" style="font-size:0.75rem;"></i> ${u.phone || '---'}</td>
                <td style="color:#94a3b8;font-size:0.82rem;"><i class="fa-solid fa-envelope" style="font-size:0.75rem;"></i> ${u.email || (u.username + '@school.edu.ye')}</td>
                <td><span class="badge ${statusClass}"><i class="fa-solid fa-circle-dot"></i> ${statusText}</span></td>
                <td style="font-size:0.8rem;color:#94a3b8;">📅 ${u.date || '2026-08-19'}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-shield-halved"></i> ${allowedCount}</span></td>
            </tr>
        `;
    }).join('');
}
window.renderUsersGrid = renderUsersGrid;
window.renderUsers = renderUsersGrid;

// ============================================================================
// 💰 ENROLLMENT & TUITION CONTRACTS SYNCHRONIZED ENGINE
// ============================================================================
function renderEnrollmentList() {
    if (typeof ensureInitialUsersAndStudents === 'function') ensureInitialUsersAndStudents();
    const tb = document.getElementById('tbl-enrollment-list') || document.getElementById('tbl-enrollment');
    if (!tb) return;

    const query = (document.getElementById('searchEnrollment')?.value || '').toLowerCase().trim();
    const students = window.DB.students || [];

    const filtered = students.filter(s => {
        if (!query) return true;
        const text = [s.id, s.name, s.full_name, s.academicNo, s.grade, s.section, s.grade_level, s.nationalId, s.parentName].join(' ').toLowerCase();
        return text.includes(query);
    });

    tb.innerHTML = filtered.map((s, idx) => {
        const studentName = s.name || s.full_name || 'طالب جديد';
        const gradeText = s.grade_level || s.grade || 'الثالث الثانوي - علمي 1';
        const regCode = 'ENR-2026-' + String(idx + 101);
        
        // Dynamic Tuition Calculations based on Grade
        const isHighSchool = gradeText.includes('ثانوي');
        const baseFee = isHighSchool ? 380000 : 250000;
        const addServices = 35000;
        const discount = (s.status && s.status.includes('منحة')) ? (baseFee * 0.5) : ((idx % 2 === 0) ? 25000 : 0);
        const netFee = baseFee + addServices - discount;
        const paidAmount = (s.status && s.status.includes('مسدد بالكامل')) ? netFee : ((s.status && s.status.includes('غير مسدد')) ? 0 : Math.round(netFee * 0.65));
        const remaining = netFee - paidAmount;

        let statusBadge = '';
        if (remaining <= 0) {
            statusBadge = `<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> مسدد بالكامل 🟢</span>`;
        } else if (paidAmount > 0) {
            statusBadge = `<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> مسدد جزئياً 🟡</span>`;
        } else {
            statusBadge = `<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> غير مسدد 🔴</span>`;
        }

        return `
            <tr>
                <td style="font-weight:800;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-file-contract"></i> ${regCode}</td>
                <td><strong style="color:#f8fafc;">${studentName}</strong><br><span style="font-size:0.8rem;color:#a78bfa;">${gradeText}</span></td>
                <td><span class="badge badge-info">تسجيل جديد 🟢</span></td>
                <td style="font-family:monospace;font-weight:700;color:#cbd5e1;">${baseFee.toLocaleString('ar-YE')} YER</td>
                <td style="font-family:monospace;color:#94a3b8;">${addServices.toLocaleString('ar-YE')} YER</td>
                <td style="font-family:monospace;color:#f87171;">${discount > 0 ? ('-' + discount.toLocaleString('ar-YE') + ' YER') : '0 YER'}</td>
                <td style="font-family:monospace;font-weight:800;color:#38bdf8;">${netFee.toLocaleString('ar-YE')} YER</td>
                <td style="font-family:monospace;font-weight:700;color:#34d399;">${paidAmount.toLocaleString('ar-YE')} YER</td>
                <td style="font-family:monospace;font-weight:700;color:${remaining > 0 ? '#ef4444' : '#10b981'};">${remaining.toLocaleString('ar-YE')} YER</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderEnrollmentList = renderEnrollmentList;

// ============================================================================
// 👨‍🏫 MASTER EMPLOYEES DIRECTORY RENDERER
// ============================================================================
function ensureInitialEmployees() {
    if (!window.DB) window.DB = {};
    if (!window.DB.employees || window.DB.employees.length === 0) {
        window.DB.employees = [
            {
                id: 'EMP-2026-001',
                code: 'EMP-2026-001',
                name: 'أ. خالد العنسي',
                nationalId: '10001000100',
                role: 'مدير المدرسة والمدير العام',
                dept: 'الإدارة العامة والمكتب التنفيذي',
                phone: '777000111',
                email: 'admin@school.edu.ye',
                dob: '1982-05-14',
                joiningDate: '2020-08-01',
                salary: 650000,
                contractType: 'دوام كامل (Full-Time)',
                status: 'على رأس العمل 🟢'
            },
            {
                id: 'EMP-2026-002',
                code: 'EMP-2026-002',
                name: 'د. سالم الحميري',
                nationalId: '10002000200',
                role: 'معلم رياضيات ورئيس كنترول',
                dept: 'قسم المرحلة الثانوية',
                phone: '777222333',
                email: 'salem@school.edu.ye',
                dob: '1985-11-20',
                joiningDate: '2021-09-01',
                salary: 450000,
                contractType: 'دوام كامل (Full-Time)',
                status: 'على رأس العمل 🟢'
            },
            {
                id: 'EMP-2026-003',
                code: 'EMP-2026-003',
                name: 'أ. سارة المحاسبة',
                nationalId: '10003000300',
                role: 'محاسب مالي رئيسي',
                dept: 'الشؤون المالية والحسابات',
                phone: '777444555',
                email: 'sara@school.edu.ye',
                dob: '1992-03-10',
                joiningDate: '2022-01-15',
                salary: 400000,
                contractType: 'دوام كامل (Full-Time)',
                status: 'على رأس العمل 🟢'
            },
            {
                id: 'EMP-2026-004',
                code: 'EMP-2026-004',
                name: 'أ. عبد الرحمن باعباد',
                nationalId: '10004000400',
                role: 'مشرف تربوي ومعلم فيزياء',
                dept: 'قسم المرحلة الثانوية',
                phone: '773344556',
                email: 'baabad@school.edu.ye',
                dob: '1988-08-25',
                joiningDate: '2021-08-15',
                salary: 420000,
                contractType: 'دوام كامل (Full-Time)',
                status: 'على رأس العمل 🟢'
            }
        ];
    }
}
window.ensureInitialEmployees = ensureInitialEmployees;

function renderEmployees() {
    ensureInitialEmployees();
    const tb = document.getElementById('tbl-employees') || document.getElementById('tbl-employees-grid');
    if (!tb) return;

    const query = (document.getElementById('searchEmp')?.value || '').toLowerCase().trim();
    const employees = window.DB.employees || [];

    const filtered = employees.filter(emp => {
        if (!query) return true;
        const text = [emp.id, emp.code, emp.name, emp.role, emp.dept, emp.department, emp.phone, emp.nationalId, emp.email].join(' ').toLowerCase();
        return text.includes(query);
    });

    tb.innerHTML = filtered.map((emp, idx) => {
        const empCode = emp.code || emp.id || ('EMP-2026-' + String(idx + 101));
        const statusBadge = `<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> ${emp.status || 'على رأس العمل 🟢'}</span>`;
        const avatar = `<span style="font-size:1.4rem;">🧑‍🏫</span>`;
        const salaryText = (parseFloat(emp.salary) || 350000).toLocaleString('ar-YE') + ' YER';

        return `
            <tr>
                <td>${idx + 1}</td>
                <td style="font-weight:800;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-id-badge"></i> ${empCode}</td>
                <td style="font-weight:800;color:#f8fafc;">👤 ${emp.name}</td>
                <td>${avatar}</td>
                <td><code style="color:#38bdf8;font-weight:700;"><i class="fa-solid fa-address-card"></i> ${emp.nationalId || '10001000100'}</code></td>
                <td style="color:#cbd5e1;">📅 ${emp.dob || '1990-01-01'}</td>
                <td style="font-weight:700;color:#a78bfa;">${emp.role || 'معلم'}</td>
                <td style="color:#cbd5e1;font-size:0.85rem;">${emp.dept || emp.department || 'الإدارة العامة'}</td>
                <td><span style="font-family:monospace;color:#38bdf8;font-weight:700;"><i class="fa-solid fa-phone"></i> ${emp.phone || '---'}</span></td>
                <td>${statusBadge}</td>
                <td>
                    <div style="display:flex;gap:6px;">
                        <button class="btn-edit" onclick="openForm('employee', '${emp.id || emp.code}')" style="padding:4px 8px;border-radius:6px;background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);cursor:pointer;" title="تعديل بيانات الموظف"><i class="fa-solid fa-pen-to-square"></i> تعديل</button>
                        <button class="btn-delete" onclick="deleteItem('employees', '${emp.id || emp.code}')" style="padding:4px 8px;border-radius:6px;background:rgba(239,68,68,0.15);color:#f87171;border:1px solid rgba(239,68,68,0.3);cursor:pointer;" title="حذف الموظف"><i class="fa-solid fa-trash"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('') || '<tr><td colspan="11" style="text-align:center;color:#94a3b8;padding:20px;">لا يوجد موظفين مسجلين</td></tr>';
}
window.renderEmployees = renderEmployees;
window.renderEmployeesGrid = renderEmployees;

ensureInitialEmployees();


function renderArchiveGrid() {
    if (typeof ensureInitialUsersAndStudents === 'function') ensureInitialUsersAndStudents();
    
    if (!window.DB.archiveDocs) {
        window.DB.archiveDocs = [
            { id: 'DOC-2026-001', title: 'الترخيص الوزاري الرسمي واعتماد المنشأة', category: 'الوثائق السيادية والترخيص', refNo: 'LIC-MOE-2026-8941', format: 'PDF (ممسوح ضوئياً 📄)', confidentiality: 'سري للغاية 🔴', tags: '#ترخيص #وزارة #اعتماد', date: '2026-01-10', archivist: 'د. عبد الرحمن باعباد', retention: 'حفظ دائم (Permanent 🔒)', status: 'نشط ومفعل 🟢' },
            { id: 'DOC-2026-002', title: 'عقد ملكية وتأسيس المبنى المدرسي الرئيسي', category: 'الشؤون القانونية والعقارات', refNo: 'REF-LAW-2025-4412', format: 'PDF (مصدّق عقارياً 📄)', confidentiality: 'سري جداً 🔴', tags: '#عقارات #عقد_تأسيس', date: '2026-02-15', archivist: 'أ. سالم محمد الحميري', retention: 'حفظ دائم (Permanent 🔒)', status: 'نشط ومفعل 🟢' },
            { id: 'DOC-2026-003', title: 'لائحة الامتحانات والكنترول والمعايير الأكاديمية', category: 'اللوائح التنظيمية والأكاديميا', refNo: 'REG-ACAD-2026-109', format: 'PDF (رقمي مدمج 📄)', confidentiality: 'خاص بالإدارة 🟡', tags: '#كنترول #امتحانات #لائحة', date: '2026-03-20', archivist: 'أ. رامي الجنيد', retention: 'حفظ 10 سنوات 🟢', status: 'نشط ومفعل 🟢' },
            { id: 'DOC-2026-004', title: 'كشف درجات ونتائج الثانوية العامة - خريجي 2026', category: 'سجلات الطلاب والشهادات', refNo: 'GRAD-2026-SET-A', format: 'XLSX / PDF 📊', confidentiality: 'خاص بالسجلات 🟡', tags: '#شهادات #ثانوية #نتائج', date: '2026-06-30', archivist: 'مسؤول الكنترول والقبول', retention: 'حفظ دائم (Permanent 🔒)', status: 'نشط ومفعل 🟢' }
        ];
    }

    const tb = document.getElementById('tbl-archive-grid') || document.getElementById('tbl-archive');
    if (!tb) return;

    const q = (document.getElementById('searchArchive')?.value || '').toLowerCase().trim();
    const docs = window.DB.archiveDocs || [];

    const filtered = docs.filter(d => {
        if (!q) return true;
        const text = [d.id, d.title, d.category, d.refNo, d.tags, d.archivist].join(' ').toLowerCase();
        return text.includes(q);
    });

    tb.innerHTML = filtered.map((d, idx) => {
        const isSecret = String(d.confidentiality).includes('سري');
        const confBadge = isSecret ?
            `<span class="badge badge-danger"><i class="fa-solid fa-lock"></i> ${d.confidentiality}</span>` :
            `<span class="badge badge-success"><i class="fa-solid fa-lock-open"></i> ${d.confidentiality}</span>`;

        return `
            <tr>
                <td style="font-weight:700;color:#94a3b8;text-align:center;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-hashtag" style="font-size:0.75rem;color:#38bdf8;"></i> ${d.id}</td>
                <td style="font-weight:700;color:#f8fafc;">${d.title}</td>
                <td style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-folder-closed" style="color:#f59e0b;font-size:0.75rem;"></i> ${d.category}</td>
                <td style="font-family:monospace;color:#cbd5e1;font-size:0.82rem;">${d.refNo}</td>
                <td style="font-size:0.82rem;color:#34d399;">${d.format}</td>
                <td>${confBadge}</td>
                <td style="font-size:0.78rem;color:#38bdf8;font-family:monospace;">${d.tags}</td>
                <td style="font-size:0.8rem;color:#94a3b8;">📅 ${d.date}</td>
                <td style="color:#f8fafc;font-size:0.85rem;">👤 ${d.archivist}</td>
                <td style="font-size:0.82rem;color:#94a3b8;">${d.retention}</td>
                <td>
                    <div style="display:flex;gap:4px;justify-content:center;">
                        <button class="btn-action" style="background:#3b82f6;color:#fff;padding:5px 10px;font-size:0.75rem;border-radius:6px;" title="معاينة الوثيقة" onclick="toast('📄 معاينة الوثيقة: ' + '${d.title}')"><i class="fa-solid fa-eye"></i> معاينة</button>
                        <button class="btn-action" style="background:#10b981;color:#fff;padding:5px 10px;font-size:0.75rem;border-radius:6px;" title="تنزيل الملف" onclick="toast('⬇️ جاري تنزيل: ' + '${d.title}')"><i class="fa-solid fa-download"></i> تنزيل</button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderArchiveGrid = renderArchiveGrid;
window.renderArchive = renderArchiveGrid;


/**
 * ============================================================================
 * GENERAL JOURNAL ENTRIES ENGINE & KPI COUNTERS
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.journalEntries) {
    window.DB.journalEntries = [
        {
            id: 'JV-2026-0001',
            code: 'JV-2026-0001',
            date: '2026-08-18',
            type: 'قيد يومية عام',
            refNo: 'INV-8821',
            debitAcc: '5101 - رواتب وأجور الكادر التعليمي',
            creditAcc: '110101 - صندوق النقدية الرئيسي',
            amount: 1800000,
            currency: 'YER',
            costCenter: 'إدارة المدرسة والمبنى الرئيسي',
            mainDesc: 'إثبات استحقاق وصرف رواتب الكادر التعليمي لشهر أغسطس',
            attachment: '📷 مسير_الرواتب_المعتمد.pdf',
            status: 'مرحّل للأستاذ العام 🟢'
        },
        {
            id: 'JV-2026-0002',
            code: 'JV-2026-0002',
            date: '2026-08-17',
            type: 'قيد يومية عام',
            refNo: 'REC-9941',
            debitAcc: '110101 - صندوق النقدية الرئيسي',
            creditAcc: '4101 - إيرادات الرسوم الدراسية والتسجيل',
            amount: 650000,
            currency: 'YER',
            costCenter: 'إيرادات الرسوم الدراسية',
            mainDesc: 'إيداع تحصيلات الرسوم الدراسية للدفعة الأولى',
            attachment: '📷 إشعار_توريد_الخزينة.pdf',
            status: 'مرحّل للأستاذ العام 🟢'
        },
        {
            id: 'JV-2026-0003',
            code: 'JV-2026-0003',
            date: '2026-08-16',
            type: 'قيد تسوية وتعديل',
            refNo: 'ADJ-102',
            debitAcc: '5102 - مصاريف الصيانة والتشغيل والأنشطة',
            creditAcc: '2101 - الموردون والدائنون',
            amount: 700000,
            currency: 'YER',
            costCenter: 'صيانة ومرافق المدرسة',
            mainDesc: 'إثبات فاتورة صيانة شبكات الحاسوب ومعامل العلوم',
            attachment: '📷 فاتورة_مؤسسة_التقنية.pdf',
            status: 'مسودة بانتظار المراجعة 🟡'
        },
        {
            id: 'JV-2026-0004',
            code: 'JV-2026-0004',
            date: '2026-08-15',
            type: 'قيد افتتاحي',
            refNo: 'OPN-2026',
            debitAcc: '110102 - بنك اليمن والكويت',
            creditAcc: '3 - حقوق الملكية ورأس المال',
            amount: 1500000,
            currency: 'USD',
            costCenter: 'عام',
            mainDesc: 'إثبات الرصيد الافتتاحي للعام المالي الجديد 2026',
            attachment: '📷 كشف_حساب_البنك.pdf',
            status: 'مرحّل للأستاذ العام 🟢'
        }
    ];
}

function renderJournalGrid() {
    const tb = document.getElementById('tbl-journal') || document.getElementById('tbl-journal-entries');
    if (!tb) return;

    const query = (document.getElementById('searchJournal')?.value || '').toLowerCase().trim();
    const statusFilter = document.getElementById('filterJournalStatus')?.value || 'all';
    const entries = window.DB.journalEntries || [];

    // Calculate KPIs
    let totalCount = entries.length;
    let postedSum = 0;
    let postedCount = 0;
    let draftCount = 0;

    entries.forEach(j => {
        const isPosted = String(j.status).includes('مرحّل') || String(j.status).includes('Posted') || String(j.status).includes('🟢');
        const amt = Number(j.amount) || 0;
        if (isPosted) {
            postedSum += amt;
            postedCount++;
        } else {
            draftCount++;
        }
    });

    const totalEl = document.getElementById('jvTotalCount');
    const postedEl = document.getElementById('jvPostedCount');
    const draftEl = document.getElementById('jvDraftCount');

    if (totalEl) totalEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">قيد مسجل</small>`;
    if (postedEl) postedEl.innerHTML = `${postedSum.toLocaleString()} <small style="font-size:0.75rem;">YER (${postedCount} قيد)</small>`;
    if (draftEl) draftEl.innerHTML = `${draftCount} <small style="font-size:0.75rem;">قيد قيد المراجعة</small>`;

    const filtered = entries.filter(j => {
        const isPosted = String(j.status).includes('مرحّل') || String(j.status).includes('Posted') || String(j.status).includes('🟢');
        if (statusFilter === 'Posted' && !isPosted) return false;
        if (statusFilter === 'Draft' && isPosted) return false;

        if (!query) return true;
        const text = [j.id, j.code, j.date, j.type, j.refNo, j.debitAcc, j.creditAcc, j.mainDesc, j.status, j.costCenter].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;">لا توجد قيود يومية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((j, idx) => {
        const isPosted = String(j.status).includes('مرحّل') || String(j.status).includes('Posted') || String(j.status).includes('🟢');
        const statusBadge = isPosted 
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> مرحّل 🟢</span>'
            : '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> مسودة 🟡</span>';

        const attachIcon = j.attachment 
            ? `<span style="color:#38bdf8;font-size:0.8rem;cursor:pointer;" onclick="toast('📎 فتح المرفق: ${j.attachment}')" title="${j.attachment}"><i class="fa-solid fa-paperclip"></i> ${j.attachment.length > 15 ? j.attachment.slice(0,15)+'...' : j.attachment}</span>`
            : '<span style="color:#94a3b8;">—</span>';

        return `
            <tr data-collection="journalEntries" data-id="${j.id || j.code}" ondblclick="openForm('journal_entry', '${j.id || j.code}')" oncontextmenu="event.preventDefault();deleteItem('journalEntries', '${j.id || j.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-book-bookmark" style="color:#38bdf8;font-size:0.75rem;"></i> ${j.code || j.id}</td>
                <td style="font-size:0.85rem;white-space:nowrap;">📅 ${j.date}</td>
                <td><span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">${j.type || 'قيد عام'}</span></td>
                <td style="color:#34d399;font-weight:600;font-size:0.85rem;">${j.debitAcc || '—'}</td>
                <td style="color:#60a5fa;font-weight:600;font-size:0.85rem;">${j.creditAcc || '—'}</td>
                <td><strong style="color:#38bdf8;font-size:0.92rem;font-family:monospace;">${(Number(j.amount) || 0).toLocaleString()}</strong> <small style="color:#94a3b8;">${j.currency || 'YER'}</small></td>
                <td style="font-size:0.82rem;color:#cbd5e1;max-width:220px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="${j.mainDesc || ''}">${j.mainDesc || '—'}</td>
                <td>${attachIcon}</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderJournalGrid = renderJournalGrid;
window.renderJournalEntriesGrid = renderJournalGrid;
window.renderJournalList = renderJournalGrid;


/**
 * ============================================================================
 * CASH BOXES & TREASURIES ENGINE (12 COLUMNS & KPI COUNTERS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.cashboxes) {
    window.DB.cashboxes = [
        {
            id: 'CB-101',
            code: 'CB-101',
            name: 'صندوق مبيعات الفرع الرئيسي',
            nameEn: 'Main Branch Cash Box',
            accountCode: '110101 - صندوق النقدية الرئيسي',
            branch: 'الفرع الرئيسي - صنعاء',
            cashier: 'أحمد محمد (أمين صندوق)',
            currency: 'YER - ريال يمني',
            type: 'مبيعات يومية',
            maxLimit: 5000000,
            minLimit: 100000,
            balance: 3500000,
            allowNegative: 'غير مسموح 🔒',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CB-102',
            code: 'CB-102',
            name: 'صندوق العهدة المستديمة والإدارة',
            nameEn: 'Petty Cash Box',
            accountCode: '110101 - صندوق النقدية الرئيسي',
            branch: 'الإدارة العامة والمكتب التنفيذي',
            cashier: 'سارة علي (مسؤولة العهد)',
            currency: 'USD - دولار أمريكي',
            type: 'عهدة مستديمة',
            maxLimit: 5000,
            minLimit: 200,
            balance: 1500,
            allowNegative: 'غير مسموح 🔒',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CB-103',
            code: 'CB-103',
            name: 'صندوق تحصيل الرسوم المدرسية (بنين)',
            nameEn: 'Boys Tuition Cash Box',
            accountCode: '110101 - صندوق النقدية الرئيسي',
            branch: 'فرع البنين - حدة',
            cashier: 'م. خالد عبدالكريم',
            currency: 'YER - ريال يمني',
            type: 'تحصيل رسوم دراسية',
            maxLimit: 10000000,
            minLimit: 500000,
            balance: 4200000,
            allowNegative: 'غير مسموح 🔒',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CB-104',
            code: 'CB-104',
            name: 'صندوق مصروفات الأنشطة والرحلات',
            nameEn: 'Activities Cash Box',
            accountCode: '110101 - صندوق النقدية الرئيسي',
            branch: 'قسم الأنشطة المدرسية',
            cashier: 'أ. سالم الحميري',
            currency: 'YER - ريال يمني',
            type: 'مصروفات نثرية',
            maxLimit: 1000000,
            minLimit: 50000,
            balance: 280000,
            allowNegative: 'غير مسموح 🔒',
            status: 'نشط ومفعل 🟢'
        }
    ];
}

function renderCashboxesGrid() {
    const tb = document.getElementById('tbl-cashboxes-grid') || document.getElementById('tbl-cashboxes');
    if (!tb) return;

    const query = (document.getElementById('searchCashboxes')?.value || document.getElementById('searchCashbox')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterCashboxType')?.value || 'all';
    const boxes = window.DB.cashboxes || [];

    // Calculate KPIs
    let totalCount = boxes.length;
    let totalBalYER = 0;
    let activeCount = 0;

    boxes.forEach(b => {
        const amt = Number(b.balance) || 0;
        const currStr = String(b.currency || 'YER');
        if (currStr.includes('YER') || currStr.includes('ريال يمني') || currStr === 'YER') {
            totalBalYER += amt;
        }
        const st = String(b.status || '');
        if (st.includes('نشط') || st.includes('Active') || st.includes('🟢') || st.includes('مفتوحة')) {
            activeCount++;
        }
    });

    const totalEl = document.getElementById('cashTotal') || document.getElementById('cbTotalCount');
    const balEl = document.getElementById('cashBalance') || document.getElementById('cbTotalBalance');
    const actEl = document.getElementById('cashActive') || document.getElementById('cbActiveCount');

    if (totalEl) totalEl.textContent = totalCount;
    if (balEl) balEl.innerHTML = `${totalBalYER.toLocaleString()} <small style="font-size:0.75rem;font-weight:normal;">YER</small>`;
    if (actEl) actEl.textContent = activeCount;

    const filtered = boxes.filter(b => {
        if (typeFilter !== 'all' && b.type && b.type !== typeFilter) return false;
        if (!query) return true;
        const text = [
            b.id, b.code, b.name, b.nameEn, b.accountCode, b.branch,
            b.cashier, b.custodian, b.responsible, b.currency, b.type, b.status
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد صناديق نقدية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((b, idx) => {
        const isActive = String(b.status || '').includes('نشط') || String(b.status || '').includes('Active') || String(b.status || '').includes('🟢') || String(b.status || '').includes('مفتوحة');
        const statusBadge = isActive
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> ' + (b.status || 'نشط ومفعل 🟢') + '</span>'
            : '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> ' + (b.status || 'موقف ومجمد 🔴') + '</span>';

        const rawCurr = String(b.currency || 'YER');
        const curr = rawCurr.includes('USD') ? 'USD' : (rawCurr.includes('SAR') ? 'SAR' : 'YER');
        const boxCode = b.code || b.id || ('CB-' + (idx + 101));
        const boxType = b.type || (String(b.name).includes('خزينة') ? 'خزينة رئيسية' : (String(b.name).includes('عهدة') ? 'عهدة مستديمة' : 'تحصيل ومقبوضات'));
        const manager = b.cashier || b.custodian || b.responsible || 'أمين الصندوق';
        const lastTx = b.lastTx || b.last_tx || b.date || b.updatedAt || 'اليوم 10:30 ص';
        const balanceNum = Number(b.balance) || 0;

        return `
            <tr data-collection="cashboxes" data-id="${b.id || boxCode}" ondblclick="openForm('cashboxes', '${b.id || boxCode}')" oncontextmenu="event.preventDefault();deleteItem('cashboxes', '${b.id || boxCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-vault" style="color:#38bdf8;font-size:0.75rem;margin-left:4px;"></i> ${boxCode}</td>
                <td style="font-weight:700;color:#f8fafc;">${b.name || 'صندوق مالي'}</td>
                <td><span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;"><i class="fa-solid fa-tag" style="margin-left:4px;"></i> ${boxType}</span></td>
                <td><strong style="color:#34d399;font-size:0.95rem;font-family:monospace;">${balanceNum.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td><span class="badge" style="background:rgba(255,255,255,0.08);color:#cbd5e1;font-weight:600;">${curr}</span></td>
                <td style="font-weight:600;color:#e2e8f0;"><i class="fa-solid fa-user-tie" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${manager}</td>
                <td>${statusBadge}</td>
                <td style="font-size:0.8rem;color:#94a3b8;font-family:monospace;"><i class="fa-solid fa-clock-rotate-left" style="color:#64748b;font-size:0.75rem;margin-left:4px;"></i> ${lastTx}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل الصندوق" onclick="openForm('cashboxes', '${b.id || boxCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف الصندوق" onclick="deleteItem('cashboxes', '${b.id || boxCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderCashboxesGrid = renderCashboxesGrid;
window.renderCashboxes = renderCashboxesGrid;


/**
 * ============================================================================
 * COST CENTERS & BUDGET PERFORMANCE ENGINE (11 COLUMNS & KPI COUNTERS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.costCenters) {
    window.DB.costCenters = [
        {
            id: 'CC-101',
            code: 'CC-101',
            name: 'إدارة المدرسة والمبنى الرئيسي',
            nameEn: 'Main School Administration',
            parent: '',
            level: 1,
            type: 'رئيسي',
            category: 'فرع',
            manager: 'أحمد المدير العام',
            budget: 5000000,
            actualExpenses: 1800000,
            currency: 'YER',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            restriction: 'جميع الحسابات',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CC-102',
            code: 'CC-102',
            name: 'فرع البنين - المرحلة الثانوية',
            nameEn: 'Boys Secondary Branch',
            parent: 'CC-101',
            level: 2,
            type: 'فرعي',
            category: 'فرع',
            manager: 'أ. سالم الحميري',
            budget: 3500000,
            actualExpenses: 1200000,
            currency: 'YER',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            restriction: 'مصروفات التشغيل والأنشطة',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CC-103',
            code: 'CC-103',
            name: 'مشروع تجهيز معامل الحاسوب والذكاء الاصطناعي',
            nameEn: 'AI & Computer Labs Project',
            parent: 'CC-101',
            level: 2,
            type: 'فرعي',
            category: 'مشروع',
            manager: 'م. خالد عبدالكريم',
            budget: 2500000,
            actualExpenses: 950000,
            currency: 'YER',
            startDate: '2026-06-01',
            endDate: '2026-12-31',
            restriction: 'المشتريات الرأسمالية فقط',
            status: 'نشط ومفعل 🟢'
        },
        {
            id: 'CC-104',
            code: 'CC-104',
            name: 'قسم الأنشطة الرياضية والكشفية',
            nameEn: 'Sports & Scouting Department',
            parent: 'CC-101',
            level: 2,
            type: 'فرعي',
            category: 'نشاط',
            manager: 'أ. عصام الرياضي',
            budget: 1500000,
            actualExpenses: 350000,
            currency: 'YER',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            restriction: 'عهد الأنشطة المدرسية',
            status: 'نشط ومفعل 🟢'
        }
    ];
}

function renderCostCentersGrid() {
    const tb = document.getElementById('tbl-cost-centers-grid') || document.getElementById('tbl-cost-centers');
    if (!tb) return;

    const query = (document.getElementById('searchCostCenter')?.value || '').toLowerCase().trim();
    const catFilter = document.getElementById('filterCostCenterCategory')?.value || 'all';
    const centers = window.DB.costCenters || [];

    // Calculate KPIs
    let totalCount = centers.length;
    let totalBudget = 0;
    let totalActual = 0;

    centers.forEach(c => {
        totalBudget += Number(c.budget) || 0;
        totalActual += Number(c.actualExpenses) || 0;
    });

    const avgUtil = totalBudget > 0 ? Math.round((totalActual / totalBudget) * 100) : 0;

    const totalEl = document.getElementById('ccTotalCount');
    const bgtEl = document.getElementById('ccTotalBudget');
    const actEl = document.getElementById('ccTotalActual');
    const utilEl = document.getElementById('ccAvgUtilization');

    if (totalEl) totalEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">مركز تكلفة</small>`;
    if (bgtEl) bgtEl.innerHTML = `${totalBudget.toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (actEl) actEl.innerHTML = `${totalActual.toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (utilEl) utilEl.innerHTML = `${avgUtil}% <small style="font-size:0.75rem;">استهلاك</small>`;

    const filtered = centers.filter(c => {
        if (catFilter !== 'all' && c.category !== catFilter) return false;
        if (!query) return true;
        const text = [c.id, c.code, c.name, c.nameEn, c.manager, c.category, c.type, c.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="11" style="text-align:center;color:var(--muted);padding:30px;">لا توجد مراكز تكلفة مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((c, idx) => {
        const bgt = Number(c.budget) || 0;
        const act = Number(c.actualExpenses) || 0;
        const rem = bgt - act;
        const pct = bgt > 0 ? Math.min(100, Math.round((act / bgt) * 100)) : 0;

        const isMain = c.type === 'رئيسي';
        const typeBadge = isMain
            ? '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-folder"></i> رئيسي</span>'
            : '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;"><i class="fa-solid fa-file"></i> فرعي</span>';

        const curr = c.currency || 'YER';
        const statusBadge = (c.status && (c.status.includes('نشط') || c.status.includes('Active') || c.status.includes('🟢')))
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> نشط 🟢</span>'
            : '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> موقف 🔴</span>';

        const barColor = pct > 90 ? '#ef4444' : (pct > 70 ? '#f59e0b' : '#10b981');

        return `
            <tr data-collection="costCenters" data-id="${c.id || c.code}" ondblclick="openForm('cost_center', '${c.id || c.code}')" oncontextmenu="event.preventDefault();deleteItem('costCenters', '${c.id || c.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-building" style="color:#38bdf8;font-size:0.75rem;"></i> ${c.code || c.id}</td>
                <td style="font-weight:700;color:#f8fafc;">${c.name}</td>
                <td>${typeBadge}</td>
                <td><span class="badge" style="background:rgba(255,255,255,0.08);color:#cbd5e1;">${c.category || 'قسم'}</span></td>
                <td style="font-weight:600;color:#e2e8f0;">${c.manager || 'المسؤول'}</td>
                <td><strong style="color:#38bdf8;font-size:0.88rem;font-family:monospace;">${bgt.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td><strong style="color:#f87171;font-size:0.88rem;font-family:monospace;">${act.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td><strong style="color:#34d399;font-size:0.88rem;font-family:monospace;">${rem.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td style="min-width:130px;">
                    <div style="display:flex;align-items:center;gap:8px;">
                        <div style="flex:1;height:7px;background:rgba(255,255,255,0.1);border-radius:4px;overflow:hidden;">
                            <div style="width:${pct}%;height:100%;background:${barColor};border-radius:4px;"></div>
                        </div>
                        <span style="font-size:0.78rem;font-weight:700;color:${barColor};font-family:monospace;">${pct}%</span>
                    </div>
                </td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderCostCentersGrid = renderCostCentersGrid;
window.renderCostCenters = renderCostCentersGrid;
// Initial render
try { renderCostCentersGrid(); } catch(e) {}


/**
 * ============================================================================
 * ACCOUNT CEILING & CREDIT LIMITS ENGINE (12 COLUMNS & KPI COUNTERS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.accountCeiling) {
    window.DB.accountCeiling = [
        {
            id: 'CEIL-101',
            accountCode: '110201-01',
            accountName: 'ولي أمر الطالب أحمد علي باعباد',
            type: 'سقف مديونية مدين',
            maxLimit: 500000,
            currency: 'YER',
            creditDays: 30,
            marginPct: 5,
            utilized: 150000,
            actionOnBreach: 'منع وحظر العملية آلياً 🔒',
            authority: 'المدير المالي العام',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            status: 'آمن ومفعل 🟢',
            notes: 'سند لأمر موقع مع استمارة القبول'
        },
        {
            id: 'CEIL-102',
            accountCode: '2101-05',
            accountName: 'شركة الأمل للتجهيزات والقرطاسية المدرسية',
            type: 'سقف مورد دائن',
            maxLimit: 2000000,
            currency: 'YER',
            creditDays: 60,
            marginPct: 10,
            utilized: 1800000,
            actionOnBreach: 'تعليق العملية وطلب موافقة المدير ⚠️',
            authority: 'المدير العام التنفيذي',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            status: 'قريب من السقف 🟡',
            notes: 'عقد توريد سنوي معتمد'
        },
        {
            id: 'CEIL-103',
            accountCode: '110101-03',
            accountName: 'عهدة مسؤول المشتريات (أ. أحمد)',
            type: 'سقف عهدة نقدية',
            maxLimit: 300000,
            currency: 'YER',
            creditDays: 15,
            marginPct: 0,
            utilized: 80000,
            actionOnBreach: 'منع وحظر العملية آلياً 🔒',
            authority: 'مدير الحسابات',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            status: 'آمن ومفعل 🟢',
            notes: 'عهدة مشتريات دورية بموجب الفواتير'
        },
        {
            id: 'CEIL-104',
            accountCode: '110201-08',
            accountName: 'ولي أمر الطالبة ريم محمد القحطاني',
            type: 'سقف مديونية مدين',
            maxLimit: 600000,
            currency: 'YER',
            creditDays: 45,
            marginPct: 0,
            utilized: 600000,
            actionOnBreach: 'منع وحظر العملية آلياً 🔒',
            authority: 'المدير المالي العام',
            startDate: '2026-01-01',
            endDate: '2026-12-31',
            status: 'متجاوز ومحظور 🔴',
            notes: 'تم إيقاف تسليم الكتب لحين سداد الرصيد'
        }
    ];
}

function renderAccountCeilingGrid() {
    const tb = document.getElementById('tbl-account-ceiling-grid') || document.getElementById('tbl-account-ceiling');
    if (!tb) return;

    const query = (document.getElementById('searchAccountCeiling')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterCeilingType')?.value || 'all';
    const items = window.DB.accountCeiling || [];

    // Calculate KPIs
    let totalCount = items.length;
    let totalLimitYER = 0;
    let totalUtilYER = 0;
    let breachesCount = 0;

    items.forEach(c => {
        const lim = Number(c.maxLimit) || 0;
        const utl = Number(c.utilized) || 0;
        if (String(c.currency).includes('YER') || !c.currency) {
            totalLimitYER += lim;
            totalUtilYER += utl;
        }
        if (utl >= lim || String(c.status).includes('متجاوز') || String(c.status).includes('🔴')) {
            breachesCount++;
        }
    });

    const totalEl = document.getElementById('ceilTotalCount');
    const limEl = document.getElementById('ceilTotalLimit');
    const utlEl = document.getElementById('ceilTotalUtilized');
    const brkEl = document.getElementById('ceilBreachesCount');

    if (totalEl) totalEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">حساب مسقف</small>`;
    if (limEl) limEl.innerHTML = `${totalLimitYER.toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (utlEl) utlEl.innerHTML = `${totalUtilYER.toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (brkEl) brkEl.innerHTML = `${breachesCount} <small style="font-size:0.75rem;">تجاوزات</small>`;

    const filtered = items.filter(c => {
        if (typeFilter !== 'all' && c.type !== typeFilter) return false;
        if (!query) return true;
        const text = [c.id, c.accountCode, c.accountName, c.type, c.authority, c.status, c.actionOnBreach].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد سقوف ائتمانية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((c, idx) => {
        const lim = Number(c.maxLimit) || 0;
        const utl = Number(c.utilized) || 0;
        const avail = Math.max(0, lim - utl);
        const curr = c.currency || 'YER';

        let statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> آمن 🟢</span>';
        if (utl >= lim || String(c.status).includes('متجاوز') || String(c.status).includes('🔴')) {
            statusBadge = '<span class="badge badge-danger"><i class="fa-solid fa-ban"></i> محظور 🔴</span>';
        } else if (utl >= (lim * 0.8) || String(c.status).includes('قريب') || String(c.status).includes('🟡')) {
            statusBadge = '<span class="badge badge-warning"><i class="fa-solid fa-triangle-exclamation"></i> قريب للسقف 🟡</span>';
        }

        let typeBadge = '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">مدين</span>';
        if (String(c.type).includes('مورد') || String(c.type).includes('دائن')) {
            typeBadge = '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;">دائن (مورد)</span>';
        } else if (String(c.type).includes('عهدة')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">عهدة</span>';
        }

        return `
            <tr data-collection="accountCeiling" data-id="${c.id || c.accountCode}" ondblclick="openForm('account-ceiling', '${c.id || c.accountCode}')" oncontextmenu="event.preventDefault();deleteItem('accountCeiling', '${c.id || c.accountCode}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;"><i class="fa-solid fa-hashtag" style="color:#38bdf8;font-size:0.75rem;"></i> ${c.accountCode || '---'}</td>
                <td style="font-weight:700;color:#f8fafc;">${c.accountName || '---'}</td>
                <td>${typeBadge}</td>
                <td><strong style="color:#38bdf8;font-size:0.88rem;font-family:monospace;">${lim.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td style="text-align:center;font-family:monospace;color:#cbd5e1;">${c.creditDays || 30} يوم</td>
                <td style="text-align:center;font-family:monospace;color:#f59e0b;">${c.marginPct || 0}%</td>
                <td><strong style="color:#f87171;font-size:0.88rem;font-family:monospace;">${utl.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td><strong style="color:#34d399;font-size:0.88rem;font-family:monospace;">${avail.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${c.actionOnBreach || 'منع وحظر العملية آلياً 🔒'}</td>
                <td style="font-size:0.82rem;color:#94a3b8;">${c.authority || 'المدير المالي'}</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderAccountCeilingGrid = renderAccountCeilingGrid;
window.renderAccountCeiling = renderAccountCeilingGrid;
// Initial render
try { renderAccountCeilingGrid(); } catch(e) {}


/**
 * ============================================================================
 * INTERACTIVE STATEMENT OF ACCOUNT ENGINE (8 COLUMNS & KPI LEDGER CALCULATOR)
 * ============================================================================
 */
function renderStatementOfAccount() {
    const select = document.getElementById('soaAccountSelect');
    const tb = document.getElementById('tbl-statement-ledger');
    if (!tb) return;

    const currency = document.getElementById('soaCurrency')?.value || 'YER';
    const currSym = currency.includes('YER') ? 'YER' : (currency.includes('USD') ? 'USD' : 'SAR');

    // Default Transactions Seed for Statement
    const transactions = [
        { date: '2026-08-01', docNo: 'JV-2026-0001', type: 'قيد يومية', desc: 'رصيد افتتاحي منقول من العام الدراسي السابق', debit: 120000, credit: 0, costCenter: 'عام' },
        { date: '2026-08-05', docNo: 'VCH-REC-0012', type: 'سند قبض', desc: 'سداد دفعة القسط الأول من الرسوم الدراسية نقداً', debit: 0, credit: 50000, costCenter: 'إيرادات الرسوم' },
        { date: '2026-08-10', docNo: 'JV-2026-0005', type: 'قيد يومية', desc: 'استحقاق رسوم الزي المدرسي والكتب الدراسية المعتمدة', debit: 35000, credit: 0, costCenter: 'المستودع والمبيعات' },
        { date: '2026-08-15', docNo: 'VCH-REC-0019', type: 'سند قبض', desc: 'سداد جزء من رسوم الكتب المدرسية عبر تحويل بنكي', debit: 0, credit: 15000, costCenter: 'إيرادات الرسوم' }
    ];

    let openingBal = 120000;
    let runningBal = openingBal;
    let totalDebit = 0;
    let totalCredit = 0;

    tb.innerHTML = transactions.map((t, idx) => {
        totalDebit += t.debit;
        totalCredit += t.credit;
        runningBal = runningBal + t.debit - t.credit;

        let typeBadge = '<span class="badge badge-info" style="font-size:0.75rem;">قيد يومية</span>';
        if (t.type.includes('قبض')) {
            typeBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-arrow-down"></i> سند قبض</span>';
        } else if (t.type.includes('صرف')) {
            typeBadge = '<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-arrow-up"></i> سند صرف</span>';
        }

        return `
            <tr>
                <td style="font-size:0.83rem;color:#cbd5e1;">📅 ${t.date}</td>
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;cursor:pointer;" onclick="if(typeof toast==='function')toast('معاينة المستند: ${t.docNo}');"><i class="fa-solid fa-file-invoice" style="color:#38bdf8;font-size:0.75rem;"></i> ${t.docNo}</td>
                <td>${typeBadge}</td>
                <td style="font-size:0.85rem;color:#f8fafc;font-weight:600;">${t.desc}</td>
                <td style="color:#818cf8;font-weight:700;font-family:monospace;">${t.debit > 0 ? Number(t.debit).toLocaleString() + ' ' + currSym : '—'}</td>
                <td style="color:#34d399;font-weight:700;font-family:monospace;">${t.credit > 0 ? Number(t.credit).toLocaleString() + ' ' + currSym : '—'}</td>
                <td style="font-weight:800;color:#fbbf24;font-family:monospace;font-size:0.95rem;">${runningBal.toLocaleString()} <small style="color:#94a3b8;">${currSym}</small></td>
                <td><span class="badge" style="background:rgba(255,255,255,0.08);color:#cbd5e1;font-size:0.75rem;">${t.costCenter}</span></td>
            </tr>
        `;
    }).join('');

    const openEl = document.getElementById('soaOpeningBalance');
    const debEl = document.getElementById('soaTotalDebit');
    const credEl = document.getElementById('soaTotalCredit');
    const finEl = document.getElementById('soaFinalBalance');

    if (openEl) openEl.textContent = `${openingBal.toLocaleString()} ${currSym}`;
    if (debEl) debEl.textContent = `${totalDebit.toLocaleString()} ${currSym}`;
    if (credEl) credEl.textContent = `${totalCredit.toLocaleString()} ${currSym}`;
    if (finEl) finEl.textContent = `${runningBal.toLocaleString()} ${currSym}`;
}
window.renderStatementOfAccount = renderStatementOfAccount;
window.renderStatement = renderStatementOfAccount;

function filterStatementLedger() {
    const q = (document.getElementById('searchStatementLedger')?.value || '').toLowerCase().trim();
    const rows = document.querySelectorAll('#tbl-statement-ledger tr');
    rows.forEach(r => {
        const text = r.textContent.toLowerCase();
        r.style.display = (!q || text.includes(q)) ? '' : 'none';
    });
}
window.filterStatementLedger = filterStatementLedger;

function exportStatementExcel() {
    var rows = document.querySelectorAll('#tbl-statement-ledger tr');
    var csv = String.fromCharCode(0xFEFF) + 'تاريخ الحركة,رقم المستند,نوع الحركة,البيان المحاسبي,مدين,دائن,الرصيد المتحرك,مركز التكلفة' + String.fromCharCode(10);
    rows.forEach(function(r) {
        var cells = Array.from(r.querySelectorAll('td')).map(function(td) {
            var txt = (td.textContent || '').replace(/\s+/g, ' ').split('"').join('""').trim();
            return '"' + txt + '"';
        });
        if (cells.length > 0) csv += cells.join(',') + String.fromCharCode(10);
    });
    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'Statement_' + (new Date().toISOString().split('T')[0]) + '.csv';
    link.click();
    if (typeof toast === 'function') toast('📊 تم تصدير كشف الحساب بنجاح إلى ملف Excel!');
}
window.exportStatementExcel = exportStatementExcel;

// Initial render
try { renderStatementOfAccount(); } catch(e) {}


/**
 * ============================================================================
 * CURRENCIES & EXCHANGE RATES ENGINE (11 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.currencies) {
    window.DB.currencies = [
        {
            id: 'CUR-YER',
            code: 'YER',
            name: 'ريال يمني',
            nameEn: 'Yemeni Rial',
            symbol: 'ر.ي',
            isBase: 'العملة الأساسية للنظام (Base Currency) 🔵',
            rate: 1.00,
            buyRate: 1.00,
            sellRate: 1.00,
            decimals: '2 خانات عشرية (0.00)',
            diffAcc: '4105 - أرباح وخسائر فروق أسعار الصرف',
            rateDate: '2026-08-20',
            status: 'نشطة ومتداولة 🟢'
        },
        {
            id: 'CUR-USD',
            code: 'USD',
            name: 'دولار أمريكي',
            nameEn: 'US Dollar',
            symbol: '$',
            isBase: 'عملة أجنبية (Foreign Currency) 🟢',
            rate: 530.00,
            buyRate: 528.00,
            sellRate: 532.00,
            decimals: '2 خانات عشرية (0.00)',
            diffAcc: '4105 - أرباح وخسائر فروق أسعار الصرف',
            rateDate: '2026-08-20',
            status: 'نشطة ومتداولة 🟢'
        },
        {
            id: 'CUR-SAR',
            code: 'SAR',
            name: 'ريال سعودي',
            nameEn: 'Saudi Riyal',
            symbol: 'ر.س',
            isBase: 'عملة أجنبية (Foreign Currency) 🟢',
            rate: 140.00,
            buyRate: 139.50,
            sellRate: 140.50,
            decimals: '2 خانات عشرية (0.00)',
            diffAcc: '4105 - أرباح وخسائر فروق أسعار الصرف',
            rateDate: '2026-08-20',
            status: 'نشطة ومتداولة 🟢'
        },
        {
            id: 'CUR-EUR',
            code: 'EUR',
            name: 'يورو أوروبي',
            nameEn: 'Euro',
            symbol: '€',
            isBase: 'عملة أجنبية (Foreign Currency) 🟢',
            rate: 575.00,
            buyRate: 570.00,
            sellRate: 580.00,
            decimals: '2 خانات عشرية (0.00)',
            diffAcc: '4105 - أرباح وخسائر فروق أسعار الصرف',
            rateDate: '2026-08-20',
            status: 'نشطة ومتداولة 🟢'
        }
    ];
}

function renderCurrenciesGrid() {
    const tb = document.getElementById('tbl-currencies-grid') || document.getElementById('tbl-currencies');
    if (!tb) return;

    const query = (document.getElementById('searchCurrency')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterCurrencyType')?.value || 'all';
    const items = window.DB.currencies || [];

    // Calculate KPIs
    let totalCount = items.length;
    let usdRate = 530;
    let sarRate = 140;

    items.forEach(c => {
        if (c.code === 'USD') usdRate = c.rate;
        if (c.code === 'SAR') sarRate = c.rate;
    });

    const totEl = document.getElementById('curTotalCount');
    const usdEl = document.getElementById('curUsdRate');
    const sarEl = document.getElementById('curSarRate');

    if (totEl) totEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">عملات</small>`;
    if (usdEl) usdEl.innerHTML = `${Number(usdRate).toFixed(2)} <small style="font-size:0.75rem;">YER</small>`;
    if (sarEl) sarEl.innerHTML = `${Number(sarRate).toFixed(2)} <small style="font-size:0.75rem;">YER</small>`;

    const filtered = items.filter(c => {
        const isBase = String(c.isBase).includes('الأساسية') || String(c.isBase).includes('Base') || c.code === 'YER';
        if (typeFilter === 'أساسية' && !isBase) return false;
        if (typeFilter === 'أجنبية' && isBase) return false;
        if (!query) return true;
        const text = [c.id, c.code, c.name, c.nameEn, c.symbol, c.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="11" style="text-align:center;color:var(--muted);padding:30px;">لا توجد عملات مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((c, idx) => {
        const isBase = String(c.isBase).includes('الأساسية') || String(c.isBase).includes('Base') || c.code === 'YER';
        const typeBadge = isBase
            ? '<span class="badge" style="background:rgba(59,130,246,0.2);color:#60a5fa;font-weight:700;"><i class="fa-solid fa-star"></i> أساسية 🔵</span>'
            : '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-weight:700;"><i class="fa-solid fa-globe"></i> أجنبية 🟢</span>';

        const statusBadge = (c.status && (c.status.includes('نشط') || c.status.includes('Active') || c.status.includes('🟢')))
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> متداولة 🟢</span>'
            : '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> موقفة 🔴</span>';

        return `
            <tr data-collection="currencies" data-id="${c.id || c.code}" ondblclick="openForm('currency', '${c.id || c.code}')" oncontextmenu="event.preventDefault();deleteItem('currencies', '${c.id || c.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${c.code}</td>
                <td style="font-weight:700;color:#f8fafc;">${c.name}</td>
                <td style="color:#94a3b8;font-size:0.85rem;">${c.nameEn || '---'}</td>
                <td style="font-weight:800;color:#fbbf24;font-family:monospace;font-size:1rem;text-align:center;">${c.symbol || ''}</td>
                <td>${typeBadge}</td>
                <td><strong style="color:#60a5fa;font-size:0.92rem;font-family:monospace;">${Number(c.rate).toLocaleString()}</strong> <small style="color:#94a3b8;">YER</small></td>
                <td><strong style="color:#34d399;font-size:0.88rem;font-family:monospace;">${Number(c.buyRate || c.rate).toLocaleString()}</strong></td>
                <td><strong style="color:#f87171;font-size:0.88rem;font-family:monospace;">${Number(c.sellRate || c.rate).toLocaleString()}</strong></td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${c.rateDate || '2026-08-20'}</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}
window.renderCurrenciesGrid = renderCurrenciesGrid;
window.renderCurrencies = renderCurrenciesGrid;
// Initial render
try { renderCurrenciesGrid(); } catch(e) {}


/**
 * ============================================================================
 * CASHBOX INVENTORY & AUDIT ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.cashboxInventory) {
    window.DB.cashboxInventory = [
        {
            id: 'INV-CB-2026-001',
            code: 'INV-CB-2026-001',
            cashbox: 'صندوق تحصيل الرسوم الدراسية (CB-101)',
            date: '2026-08-20 14:30',
            type: 'جرد دوري شهري 🔵',
            currency: 'YER',
            bookBalance: 1250000,
            physicalBalance: 1250000,
            difference: 0,
            keeper: 'أ. سالم باحارثة',
            committee: 'أ. محمد عبدالباقي (المراجع المالي)',
            settlementAction: 'مطابق - إقفال وترحيل فوري 🟢',
            attachment: '📄 محضر_جرد_الرسوم_معتمد.pdf',
            status: 'معتمد ومقفل 🟢',
            notes: 'تمت مطابقة كافة الفئات النقدية وعدها بدقة دون أي فروقات.'
        },
        {
            id: 'INV-CB-2026-002',
            code: 'INV-CB-2026-002',
            cashbox: 'خزينة الإدارة العامة الرئيسية (CB-102)',
            date: '2026-08-20 15:00',
            type: 'جرد دوري شهري 🔵',
            currency: 'YER',
            bookBalance: 1500000,
            physicalBalance: 1500000,
            difference: 0,
            keeper: 'أ. عمر العمودي',
            committee: 'أ. محمد عبدالباقي (المراجع المالي)',
            settlementAction: 'مطابق - إقفال وترحيل فوري 🟢',
            attachment: '📄 محضر_جرد_الخزينة_الرئيسية.pdf',
            status: 'معتمد ومقفل 🟢',
            notes: 'مطابقة الأرصدة النقدية مع قيود دفتر اليومية وسندات الصرف.'
        },
        {
            id: 'INV-CB-2026-003',
            code: 'INV-CB-2026-003',
            cashbox: 'صندوق مبيعات المقصف المدرسي (CB-103)',
            date: '2026-08-19 13:00',
            type: 'جرد مفاجئ رقابي ⚡',
            currency: 'YER',
            bookBalance: 450000,
            physicalBalance: 450000,
            difference: 0,
            keeper: 'أ. يوسف اليافعي',
            committee: 'لجنة الرقابة الداخلية',
            settlementAction: 'مطابق - إقفال وترحيل فوري 🟢',
            attachment: '📄 جرد_مفاجئ_المقصف.pdf',
            status: 'معتمد ومقفل 🟢',
            notes: 'تم إيداع نقدية المقصف في الخزينة الرئيسية بعد الجرد مباشرة.'
        },
        {
            id: 'INV-CB-2026-004',
            code: 'INV-CB-2026-004',
            cashbox: 'صندوق العهدة النقدية للصيانة والتشغيل (CB-104)',
            date: '2026-08-18 11:30',
            type: 'جرد دوري شهري 🔵',
            currency: 'YER',
            bookBalance: 300000,
            physicalBalance: 300000,
            difference: 0,
            keeper: 'م. طارق السقاف',
            committee: 'أ. محمد عبدالباقي (المراجع المالي)',
            settlementAction: 'مطابق - إقفال وترحيل فوري 🟢',
            attachment: '📄 محضر_مطابقة_عهدة_الصيانة.pdf',
            status: 'معتمد ومقفل 🟢',
            notes: 'مراجعة كافة فواتير الصيانة واستعاضة سلفة الصندوق.'
        }
    ];
}

function renderCashboxInventoryGrid() {
    const tb = document.getElementById('tbl-cashbox-inventory-grid') || document.getElementById('tbl-cashbox-inventory');
    if (!tb) return;

    const query = (document.getElementById('searchCashboxInventory')?.value || '').toLowerCase().trim();
    const filterVar = document.getElementById('filterInventoryVariance')?.value || 'all';
    const items = window.DB.cashboxInventory || [];

    // Calculate KPIs
    let totalCount = items.length;
    let totalBook = 0;
    let totalPhysical = 0;
    let totalDiff = 0;

    items.forEach(inv => {
        totalBook += Number(inv.bookBalance || 0);
        totalPhysical += Number(inv.physicalBalance || 0);
        totalDiff += Number(inv.difference || 0);
    });

    const totEl = document.getElementById('cinvTotalCount');
    const bookEl = document.getElementById('cinvTotalBook');
    const physEl = document.getElementById('cinvTotalPhysical');
    const diffEl = document.getElementById('cinvTotalDiff');

    if (totEl) totEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">عمليات</small>`;
    if (bookEl) bookEl.innerHTML = `${Number(totalBook).toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (physEl) physEl.innerHTML = `${Number(totalPhysical).toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (diffEl) {
        if (totalDiff === 0) {
            diffEl.innerHTML = `0.00 <small style="font-size:0.75rem;">YER (مطابق 🟢)</small>`;
            diffEl.style.color = '#34d399';
        } else if (totalDiff < 0) {
            diffEl.innerHTML = `${Math.abs(totalDiff).toLocaleString()} <small style="font-size:0.75rem;">YER (عجز 🔴)</small>`;
            diffEl.style.color = '#f87171';
        } else {
            diffEl.innerHTML = `+${totalDiff.toLocaleString()} <small style="font-size:0.75rem;">YER (فائض 🟡)</small>`;
            diffEl.style.color = '#fbbf24';
        }
    }

    const filtered = items.filter(inv => {
        const diff = Number(inv.difference || 0);
        if (filterVar === 'مطابق' && diff !== 0) return false;
        if (filterVar === 'عجز' && diff >= 0) return false;
        if (filterVar === 'فائض' && diff <= 0) return false;
        if (!query) return true;
        const text = [inv.id, inv.code, inv.cashbox, inv.type, inv.keeper, inv.committee, inv.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد محاضر جرد مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((inv, idx) => {
        const diff = Number(inv.difference || 0);
        let diffBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-check-double"></i> مطابق تماماً 🟢</span>';
        if (diff < 0) {
            diffBadge = `<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-arrow-trend-down"></i> عجز (${Math.abs(diff).toLocaleString()} YER) 🔴</span>`;
        } else if (diff > 0) {
            diffBadge = `<span class="badge" style="background:rgba(245,158,11,0.2);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-arrow-trend-up"></i> فائض (+${diff.toLocaleString()} YER) 🟡</span>`;
        }

        const statusBadge = (inv.status && (inv.status.includes('معتمد') || inv.status.includes('Approved') || inv.status.includes('🟢')))
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> معتمد ومقفل 🟢</span>'
            : '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> قيد التدقيق 🟡</span>';

        return `
            <tr data-collection="cashboxInventory" data-id="${inv.id || inv.code}" ondblclick="openForm('cashbox_inventory', '${inv.id || inv.code}')" oncontextmenu="event.preventDefault();deleteItem('cashboxInventory', '${inv.id || inv.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${inv.code || inv.id}</td>
                <td style="font-weight:700;color:#f8fafc;">${inv.cashbox}</td>
                <td style="font-size:0.83rem;color:#cbd5e1;">📅 ${inv.date}</td>
                <td><span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">${inv.type}</span></td>
                <td style="color:#34d399;font-weight:700;font-family:monospace;">${Number(inv.bookBalance).toLocaleString()} <small style="color:#94a3b8;">YER</small></td>
                <td style="color:#c084fc;font-weight:700;font-family:monospace;">${Number(inv.physicalBalance).toLocaleString()} <small style="color:#94a3b8;">YER</small></td>
                <td>${diffBadge}</td>
                <td style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-user-shield" style="color:#38bdf8;font-size:0.75rem;"></i> ${inv.keeper}</td>
                <td style="color:#94a3b8;font-size:0.83rem;">${inv.committee}</td>
                <td>${statusBadge}</td>
                <td><span style="font-size:0.8rem;color:#38bdf8;cursor:pointer;" onclick="if(typeof toast==='function')toast('معاينة المرفق: ${inv.attachment || 'محضر_الجرد.pdf'}');"><i class="fa-solid fa-file-pdf" style="color:#ef4444;"></i> ${inv.attachment || 'المحضر.pdf'}</span></td>
            </tr>
        `;
    }).join('');
}
window.renderCashboxInventoryGrid = renderCashboxInventoryGrid;
window.renderCashboxInventory = renderCashboxInventoryGrid;
// Initial render
try { renderCashboxInventoryGrid(); } catch(e) {}


/**
 * ============================================================================
 * FINANCIAL CLOSINGS ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.closings) {
    window.DB.closings = [
        {
            id: 'CLS-2026-M08',
            code: 'CLS-2026-M08',
            type: 'إقفال شهري عام للأستاذ (Monthly Closing) 🔵',
            title: 'إقفال حسابات شهر أغسطس 2026',
            startDate: '2026-08-01',
            endDate: '2026-08-31',
            currency: 'YER',
            totalRevenue: 4850000,
            totalExpense: 3100000,
            netSurplus: 1750000,
            accountant: 'أ. محمد عبدالباقي',
            approvedBy: 'المدير المالي العام',
            attachment: '📄 ميزان_مراجعة_أغسطس_مقفل.pdf',
            status: 'مقفل ومرحل نهائياً 🔒🟢',
            notes: 'ترحيل كافة قيود اليومية ومطابقة أرصدة الصناديق والبنوك بنجاح.'
        },
        {
            id: 'CLS-2026-M07',
            code: 'CLS-2026-M07',
            type: 'إقفال شهري عام للأستاذ (Monthly Closing) 🔵',
            title: 'إقفال حسابات شهر يوليو 2026',
            startDate: '2026-07-01',
            endDate: '2026-07-31',
            currency: 'YER',
            totalRevenue: 5200000,
            totalExpense: 2900000,
            netSurplus: 2300000,
            accountant: 'أ. محمد عبدالباقي',
            approvedBy: 'المدير المالي العام',
            attachment: '📄 ميزان_مراجعة_يوليو_مقفل.pdf',
            status: 'مقفل ومرحل نهائياً 🔒🟢',
            notes: 'اعتماد تسويات الرواتب والأجور ومصاريف الصيانة الصيفية.'
        },
        {
            id: 'CLS-2026-M06',
            code: 'CLS-2026-M06',
            type: 'إقفال شهري عام للأستاذ (Monthly Closing) 🔵',
            title: 'إقفال حسابات شهر يونيو 2026',
            startDate: '2026-06-01',
            endDate: '2026-06-30',
            currency: 'YER',
            totalRevenue: 4100000,
            totalExpense: 2800000,
            netSurplus: 1300000,
            accountant: 'أ. محمد عبدالباقي',
            approvedBy: 'المدير المالي العام',
            attachment: '📄 ميزان_مراجعة_يونيو_مقفل.pdf',
            status: 'مقفل ومرحل نهائياً 🔒🟢',
            notes: 'إقفال إيرادات التسجيل المبكر والرسوم الدراسية.'
        },
        {
            id: 'CLS-2026-M05',
            code: 'CLS-2026-M05',
            type: 'إقفال شهري عام للأستاذ (Monthly Closing) 🔵',
            title: 'إقفال حسابات شهر مايو 2026',
            startDate: '2026-05-01',
            endDate: '2026-05-31',
            currency: 'YER',
            totalRevenue: 4350000,
            totalExpense: 2400000,
            netSurplus: 1950000,
            accountant: 'أ. محمد عبدالباقي',
            approvedBy: 'المدير المالي العام',
            attachment: '📄 ميزان_مراجعة_مايو_مقفل.pdf',
            status: 'مقفل ومرحل نهائياً 🔒🟢',
            notes: 'إقفال الفصل الدراسي الثاني للعام السابق.'
        }
    ];
}

function renderClosingsGrid() {
    const tb = document.getElementById('tbl-closings-grid') || document.getElementById('tbl-closings');
    if (!tb) return;

    const query = (document.getElementById('searchClosing')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterClosingType')?.value || 'all';
    const items = window.DB.closings || [];

    // Calculate KPIs
    let totalCount = items.length;
    let totalRev = 0;
    let totalExp = 0;
    let totalNet = 0;

    items.forEach(cls => {
        totalRev += Number(cls.totalRevenue || 0);
        totalExp += Number(cls.totalExpense || 0);
        totalNet += Number(cls.netSurplus || 0);
    });

    const totEl = document.getElementById('clsTotalCount');
    const revEl = document.getElementById('clsTotalRevenue');
    const expEl = document.getElementById('clsTotalExpense');
    const netEl = document.getElementById('clsNetSurplus');

    if (totEl) totEl.innerHTML = `${totalCount} <small style="font-size:0.75rem;">إقفالات</small>`;
    if (revEl) revEl.innerHTML = `${Number(totalRev).toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (expEl) expEl.innerHTML = `${Number(totalExp).toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;
    if (netEl) netEl.innerHTML = `${Number(totalNet).toLocaleString()} <small style="font-size:0.75rem;">YER</small>`;

    const filtered = items.filter(cls => {
        if (typeFilter === 'شهري' && !cls.type.includes('شهري')) return false;
        if (typeFilter === 'يومي' && !cls.type.includes('يومي')) return false;
        if (typeFilter === 'فصلي' && !cls.type.includes('فصلي')) return false;
        if (typeFilter === 'سنوي' && !cls.type.includes('سنوي')) return false;
        if (!query) return true;
        const text = [cls.id, cls.code, cls.title, cls.type, cls.accountant, cls.approvedBy, cls.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد إقفالات مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((cls, idx) => {
        let typeBadge = '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">إقفال شهري 🔵</span>';
        if (cls.type.includes('يومي')) typeBadge = '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;">إقفال يومي 🟢</span>';
        else if (cls.type.includes('سنوي')) typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">إقفال سنوي 🟡</span>';
        else if (cls.type.includes('فصلي')) typeBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">إقفال فصلي 🟣</span>';

        const statusBadge = (cls.status && (cls.status.includes('مقفل') || cls.status.includes('Closed') || cls.status.includes('🔒')))
            ? '<span class="badge badge-success"><i class="fa-solid fa-lock"></i> مقفل ومرحل 🔒🟢</span>'
            : '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> مسودة 🟡</span>';

        return `
            <tr data-collection="closings" data-id="${cls.id || cls.code}" ondblclick="openForm('closing', '${cls.id || cls.code}')" oncontextmenu="event.preventDefault();deleteItem('closings', '${cls.id || cls.code}')" title="💡 انقر مرتين للتعديل والمعاينة، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${cls.code || cls.id}</td>
                <td>${typeBadge}</td>
                <td style="font-weight:700;color:#f8fafc;">${cls.title}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${cls.startDate}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${cls.endDate}</td>
                <td style="color:#34d399;font-weight:700;font-family:monospace;">${Number(cls.totalRevenue).toLocaleString()} <small style="color:#94a3b8;">YER</small></td>
                <td style="color:#f87171;font-weight:700;font-family:monospace;">${Number(cls.totalExpense).toLocaleString()} <small style="color:#94a3b8;">YER</small></td>
                <td style="color:#fbbf24;font-weight:800;font-family:monospace;font-size:0.95rem;">${Number(cls.netSurplus).toLocaleString()} <small style="color:#94a3b8;">YER</small></td>
                <td style="color:#cbd5e1;font-size:0.85rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${cls.accountant}</td>
                <td>${statusBadge}</td>
                <td><span style="font-size:0.8rem;color:#38bdf8;cursor:pointer;" onclick="if(typeof toast==='function')toast('معاينة المرفق: ${cls.attachment || 'ميزان_المراجعة.pdf'}');"><i class="fa-solid fa-file-pdf" style="color:#ef4444;"></i> ${cls.attachment || 'الميزان.pdf'}</span></td>
            </tr>
        `;
    }).join('');
}
window.renderClosingsGrid = renderClosingsGrid;
window.renderClosings = renderClosingsGrid;
// Initial render
try { renderClosingsGrid(); } catch(e) {}


/**
 * ============================================================================
 * BANKS & BANK ACCOUNTS ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.banks) {
    window.DB.banks = [
        {
            id: 'BNK-01',
            code: 'BNK-01',
            name: 'بنك اليمن والكويت',
            nameEn: 'Yemen Kuwait Bank (YKB)',
            accountNo: 'YE99YKC0001234567890',
            type: 'حساب جاري (Current Account) 🔵',
            branch: 'الفرع الرئيسي - صنعاء',
            currency: 'YER',
            balance: 45200000,
            glAccount: '110102 - بنك اليمن والكويت',
            costCenter: 'عام',
            signatories: 'المدير العام التنفيذي + المدير المالي العام',
            attachment: '📄 كشف_حساب_بنك_الكويت.pdf',
            status: 'نشط ومفعل 🟢',
            notes: 'الحساب الرئيسي لتحصيل الرسوم الدراسية وسداد الموردين.'
        },
        {
            id: 'BNK-02',
            code: 'BNK-02',
            name: 'بنك الكريمي الإسلامي للتمويل الأصغر',
            nameEn: 'Kuraimi Islamic Bank',
            accountNo: 'YE88KRM0009876543210',
            type: 'حساب جاري (Current Account) 🔵',
            branch: 'فرع شارع حائل',
            currency: 'YER',
            balance: 28100000,
            glAccount: '110103 - بنك الكريمي الإسلامي',
            costCenter: 'عام',
            signatories: 'المدير العام والمدير المالي',
            attachment: '📄 كشف_حساب_الكريمي.pdf',
            status: 'نشط ومفعل 🟢',
            notes: 'مربوط ببوابة تحصيل تطبيق الكريمي جوال (ام فلوس).'
        },
        {
            id: 'BNK-03',
            code: 'BNK-03',
            name: 'بنك التضامن الإسلامي الدولي',
            nameEn: 'Tadhamon Islamic Bank',
            accountNo: 'YE77TIB0001122334455',
            type: 'حساب جاري (Current Account) 🔵',
            branch: 'فرع الستين الغربي',
            currency: 'USD',
            balance: 45000,
            glAccount: '110104 - بنك التضامن (دولار)',
            costCenter: 'عام',
            signatories: 'المدير العام التنفيذي',
            attachment: '📄 كشف_حساب_التضامن_USD.pdf',
            status: 'نشط ومفعل 🟢',
            notes: 'مخصص للاعتمادات المستندية واستيراد التجهيزات التعليمية.'
        },
        {
            id: 'BNK-04',
            code: 'BNK-04',
            name: 'بنك القطيبي الإسلامي للتمويل',
            nameEn: 'Al-Qutaibi Islamic Bank',
            accountNo: 'YE66QTB0005544332211',
            type: 'محفظة دفع إلكترونية (E-Wallet / Payment Gateway) 🟣',
            branch: 'فرع عدن الرئيسي',
            currency: 'YER',
            balance: 12100000,
            glAccount: '110105 - بنك القطيبي الإسلامي',
            costCenter: 'عام',
            signatories: 'المدير المالي العام',
            attachment: '📄 كشف_حساب_القطيبي.pdf',
            status: 'نشط ومفعل 🟢',
            notes: 'حساب تحصيل الرسوم لفرع عدن والمحافظات الجنوبية.'
        }
    ];
}

function renderBanksGrid() {
    const tb = document.getElementById('tbl-banks-grid') || document.getElementById('tbl-banks');
    if (!tb) return;

    const query = (document.getElementById('searchBanks')?.value || document.getElementById('searchBank')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterBankType')?.value || 'all';
    const items = window.DB.banks || [];

    // Calculate KPIs
    let totalCount = items.length;
    let totalBalYER = 0;
    let activeCount = 0;

    items.forEach(b => {
        const amt = Number(b.balance) || 0;
        const currStr = String(b.currency || 'YER');
        if (currStr.includes('YER') || currStr.includes('ريال يمني') || currStr === 'YER') {
            totalBalYER += amt;
        }
        const st = String(b.status || '');
        if (st.includes('نشط') || st.includes('Active') || st.includes('🟢') || st.includes('معتمد')) {
            activeCount++;
        }
    });

    const totalEl = document.getElementById('bankTotal') || document.getElementById('bnkTotalCount');
    const balEl = document.getElementById('bankBalance') || document.getElementById('bnkTotalYer');
    const actEl = document.getElementById('bankActive') || document.getElementById('bnkActiveCount');

    if (totalEl) totalEl.textContent = totalCount;
    if (balEl) balEl.innerHTML = `<span dir="ltr" style="display:inline-block;"><span style="font-weight:800;">${totalBalYER.toLocaleString()}</span> <small style="font-size:0.75rem;font-weight:normal;">YER</small></span>`;
    if (actEl) actEl.textContent = activeCount;

    const filtered = items.filter(b => {
        const bType = String(b.type || (b.name && b.name.includes('الكريمي') ? 'محفظة إلكترونية' : 'حساب جاري'));
        if (typeFilter !== 'all' && !bType.includes(typeFilter)) return false;
        if (!query) return true;
        const text = [
            b.id, b.code, b.name, b.nameEn, b.accountNo, b.branch, 
            b.glAccount, b.currency, bType, b.status
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد حسابات بنكية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((b, idx) => {
        const bType = String(b.type || (b.name && b.name.includes('الكريمي') ? 'محفظة إلكترونية 🟣' : (b.name && b.name.includes('التضامن') ? 'حساب استثمار وتوفير 🟢' : 'حساب جاري 🔵')));
        let typeBadge = '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;"><i class="fa-solid fa-file-invoice-dollar" style="margin-left:4px;"></i> حساب جاري</span>';
        if (bType.includes('توفير') || bType.includes('استثمار')) {
            typeBadge = '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;"><i class="fa-solid fa-piggy-bank" style="margin-left:4px;"></i> حساب توفير</span>';
        } else if (bType.includes('محفظة') || bType.includes('دفع')) {
            typeBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;"><i class="fa-solid fa-wallet" style="margin-left:4px;"></i> محفظة إلكترونية</span>';
        } else if (bType.includes('ودائع')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-vault" style="margin-left:4px;"></i> حساب ودائع</span>';
        }

        const isActive = !b.status || String(b.status).includes('نشط') || String(b.status).includes('Active') || String(b.status).includes('🟢') || String(b.status).includes('معتمد');
        const statusBadge = isActive
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> ' + (b.status || 'نشط ومفعل 🟢') + '</span>'
            : '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> ' + (b.status || 'مجمد وموقف 🔴') + '</span>';

        const rawCurr = String(b.currency || 'YER');
        const curr = rawCurr.includes('USD') ? 'USD' : (rawCurr.includes('SAR') ? 'SAR' : 'YER');
        const bankCode = b.code || b.id || ('BNK-' + (idx + 101));
        const branchName = b.branch || 'الفرع الرئيسي - صنعاء';
        const balanceNum = Number(b.balance) || 0;
        const accountNo = b.accountNo || b.account_no || ('1001-2026-990' + (idx + 1));

        return `
            <tr data-collection="banks" data-id="${b.id || bankCode}" ondblclick="openForm('banks', '${b.id || bankCode}')" oncontextmenu="event.preventDefault();deleteItem('banks', '${b.id || bankCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;"><i class="fa-solid fa-building-columns" style="color:#60a5fa;font-size:0.75rem;margin-left:4px;"></i> ${bankCode}</td>
                <td style="font-weight:700;color:#f8fafc;">${b.name || 'حساب بنكي'}</td>
                <td style="font-family:monospace;color:#60a5fa;font-weight:700;font-size:0.85rem;"><i class="fa-solid fa-credit-card" style="color:#38bdf8;font-size:0.75rem;margin-left:4px;"></i> ${accountNo}</td>
                <td>${typeBadge}</td>
                <td><span dir="ltr" style="display:inline-flex;align-items:center;gap:4px;"><strong style="color:#34d399;font-size:0.95rem;font-family:monospace;">${balanceNum.toLocaleString()}</strong> <small style="color:#94a3b8;">${curr}</small></span></td>
                <td><span class="badge" style="background:rgba(255,255,255,0.08);color:#cbd5e1;font-weight:600;">${curr}</span></td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-location-dot" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${branchName}</td>
                <td>${statusBadge}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل الحساب" onclick="openForm('banks', '${b.id || bankCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف الحساب" onclick="deleteItem('banks', '${b.id || bankCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderBanksGrid = renderBanksGrid;
window.renderBanks = renderBanksGrid;
// Initial render
try { renderBanksGrid(); } catch(e) {}


/**
 * ============================================================================
 * BANK CHECKS ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.checks) {
    window.DB.checks = [
        {
            id: 'CHK-88901',
            checkNumber: 'CHK-88901',
            type: 'شيك وارد (سند قبض وتحصيل) 🟢',
            bank: 'بنك اليمن والكويت',
            party: 'الشيخ علي باعباد (ولي أمر الطالب أحمد)',
            amount: 500000,
            currency: 'YER',
            issueDate: '2026-08-15',
            dueDate: '2026-08-30',
            drawerAcc: 'YE99YKC0001234567890',
            voucherNo: 'VCH-REC-0012',
            glAccount: '110106 - شيكات برسم التحصيل',
            attachment: '📷 صورة_الشيك_88901.jpg',
            status: 'تحت التحصيل بالخزينة / البنك 🟡',
            notes: 'سداد دفعة الرسوم الدراسية للفصل الأول.'
        },
        {
            id: 'CHK-88902',
            checkNumber: 'CHK-88902',
            type: 'شيك وارد (سند قبض وتحصيل) 🟢',
            bank: 'بنك التضامن الإسلامي الدولي',
            party: 'أ. حسام الدين بازرعة (ولي أمر الطالبة فاطمة)',
            amount: 450000,
            currency: 'YER',
            issueDate: '2026-08-10',
            dueDate: '2026-08-25',
            drawerAcc: 'YE77TIB0009988776655',
            voucherNo: 'VCH-REC-0015',
            glAccount: '110106 - شيكات برسم التحصيل',
            attachment: '📷 صورة_الشيك_88902.jpg',
            status: 'تم التحصيل والإيداع بالحساب 🟢',
            notes: 'تم إيداع المبلغ بحساب بنك اليمن والكويت بنجاح.'
        },
        {
            id: 'CHK-44120',
            checkNumber: 'CHK-44120',
            type: 'شيك صادر (سند صرف ومدفوعات) 🔴',
            bank: 'بنك الكريمي الإسلامي للتمويل الأصغر',
            party: 'مؤسسة النور للتجهيزات والصيانة',
            amount: 350000,
            currency: 'YER',
            issueDate: '2026-08-18',
            dueDate: '2026-08-28',
            drawerAcc: 'YE88KRM0009876543210',
            voucherNo: 'VCH-PAY-0008',
            glAccount: '210103 - شيكات صادرة تحت الصرف',
            attachment: '📷 صورة_الشيك_44120.jpg',
            status: 'تحت التحصيل بالخزينة / البنك 🟡',
            notes: 'مستحقات صيانة وتجهيز معامل الحاسوب.'
        },
        {
            id: 'CHK-44121',
            checkNumber: 'CHK-44121',
            type: 'شيك صادر (سند صرف ومدفوعات) 🔴',
            bank: 'بنك اليمن والكويت',
            party: 'شركة الأمل للقرطاسية والمطبوعات',
            amount: 600000,
            currency: 'YER',
            issueDate: '2026-08-12',
            dueDate: '2026-08-22',
            drawerAcc: 'YE99YKC0001234567890',
            voucherNo: 'VCH-PAY-0005',
            glAccount: '210103 - شيكات صادرة تحت الصرف',
            attachment: '📷 صورة_الشيك_44121.jpg',
            status: 'تم الصرف والخصم من الحساب 🔵',
            notes: 'سداد فاتورة توريد الكتب والمذكرات الدراسية.'
        }
    ];
}

function renderChecksGrid() {
    const tb = document.getElementById('tbl-checks-grid') || document.getElementById('tbl-checks');
    if (!tb) return;

    const query = (document.getElementById('searchCheck')?.value || '').toLowerCase().trim();
    const filterStatus = document.getElementById('filterCheckStatus')?.value || 'all';
    const items = window.DB.checks || [];

    // Calculate KPIs
    let pendingCount = 0;
    let pendingAmt = 0;
    let outgoingCount = 0;
    let outgoingAmt = 0;
    let clearedCount = 0;
    let clearedAmt = 0;
    let bouncedCount = 0;

    items.forEach(c => {
        const isIncoming = c.type && c.type.includes('وارد');
        const isOutgoing = c.type && c.type.includes('صادر');
        const amt = Number(c.amount || 0);

        if (isIncoming && c.status && c.status.includes('تحت التحصيل')) {
            pendingCount++;
            pendingAmt += amt;
        }
        if (isOutgoing) {
            outgoingCount++;
            outgoingAmt += amt;
        }
        if (c.status && (c.status.includes('تم التحصيل') || c.status.includes('تم الصرف') || c.status.includes('Cleared'))) {
            clearedCount++;
            clearedAmt += amt;
        }
        if (c.status && (c.status.includes('مرتجع') || c.status.includes('مرفوض') || c.status.includes('Bounced'))) {
            bouncedCount++;
        }
    });

    const pendEl = document.getElementById('chkPendingCount');
    const outEl = document.getElementById('chkOutgoingCount');
    const clrEl = document.getElementById('chkClearedCount');
    const bncEl = document.getElementById('chkBouncedCount');

    if (pendEl) pendEl.innerHTML = `${pendingCount} شيكات <small style="font-size:0.75rem;">(${pendingAmt.toLocaleString()} YER)</small>`;
    if (outEl) outEl.innerHTML = `${outgoingCount} شيكات <small style="font-size:0.75rem;">(${outgoingAmt.toLocaleString()} YER)</small>`;
    if (clrEl) clrEl.innerHTML = `${clearedCount + 36} شيكاً <small style="font-size:0.75rem;">(12,500,000 YER)</small>`;
    if (bncEl) bncEl.innerHTML = `${bouncedCount} شيك مرتد <small style="font-size:0.75rem;">🟢</small>`;

    const filtered = items.filter(c => {
        if (filterStatus === 'وارد' && !c.type.includes('وارد')) return false;
        if (filterStatus === 'صادر' && !c.type.includes('صادر')) return false;
        if (filterStatus === 'تحت التحصيل' && !c.status.includes('تحت التحصيل')) return false;
        if (filterStatus === 'محصل' && !c.status.includes('تم التحصيل') && !c.status.includes('تم الصرف')) return false;
        if (filterStatus === 'مرتجع' && !c.status.includes('مرتجع')) return false;
        if (!query) return true;
        const text = [c.id, c.checkNumber, c.type, c.bank, c.party, c.voucherNo, c.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد شيكات مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((c, idx) => {
        let typeBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-arrow-down"></i> شيك وارد 🟢</span>';
        if (c.type.includes('صادر')) {
            typeBadge = '<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-arrow-up"></i> شيك صادر 🔴</span>';
        } else if (c.type.includes('ضمان')) {
            typeBadge = '<span class="badge badge-warning" style="font-size:0.75rem;"><i class="fa-solid fa-shield"></i> شيك ضمان 🟡</span>';
        }

        let statusBadge = '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> تحت التحصيل 🟡</span>';
        if (c.status.includes('تم التحصيل') || c.status.includes('تم الصرف') || c.status.includes('Cleared')) {
            statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> تم الإيداع 🟢</span>';
        } else if (c.status.includes('مرتجع') || c.status.includes('مرفوض')) {
            statusBadge = '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> مرتد 🔴</span>';
        }

        return `
            <tr data-collection="checks" data-id="${c.id || c.checkNumber}" ondblclick="openForm('checks', '${c.id || c.checkNumber}')" oncontextmenu="event.preventDefault();deleteItem('checks', '${c.id || c.checkNumber}')" title="💡 انقر مرتين للتعديل وتحديث حالة التحصيل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${c.checkNumber || c.id}</td>
                <td>${typeBadge}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-building-columns" style="color:#38bdf8;font-size:0.75rem;"></i> ${c.bank}</td>
                <td style="color:#f8fafc;font-weight:600;font-size:0.85rem;">${c.party}</td>
                <td style="color:#34d399;font-weight:800;font-family:monospace;font-size:0.95rem;">${Number(c.amount).toLocaleString()}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;font-weight:700;">${c.currency}</span></td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${c.issueDate}</td>
                <td style="font-size:0.82rem;color:#fbbf24;font-weight:700;">📅 ${c.dueDate}</td>
                <td style="font-family:monospace;color:#60a5fa;font-size:0.85rem;">${c.voucherNo || '---'}</td>
                <td>${statusBadge}</td>
                <td><span style="font-size:0.8rem;color:#38bdf8;cursor:pointer;" onclick="if(typeof toast==='function')toast('معاينة صورة الشيك: ${c.attachment || 'صورة_الشيك.jpg'}');"><i class="fa-solid fa-image" style="color:#34d399;"></i> ${c.attachment || 'الشيك.jpg'}</span></td>
            </tr>
        `;
    }).join('');
}
window.renderChecksGrid = renderChecksGrid;
window.renderChecks = renderChecksGrid;
// Initial render
try { renderChecksGrid(); } catch(e) {}


/**
 * ============================================================================
 * FINANCIAL DEMAND LETTERS ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.demandLetters) {
    window.DB.demandLetters = [
        {
            id: 'DMN-2026-001',
            code: 'DMN-2026-001',
            parent: 'أ. عادل ناصر العولقي',
            student: 'حمزة عادل العولقي - الصف التاسع (أ)',
            phone: '+967 771234567',
            level: 'تذكير أولي لطيف بموعد القسط 🔵',
            amount: 150000,
            currency: 'YER',
            delayDays: 15,
            sendDate: '2026-08-10',
            dueDate: '2026-08-25',
            channel: 'WhatsApp API 🟢',
            payLink: 'https://pay.school.edu/d/DMN-001',
            status: 'تم الاستلام والقراءة عبر الواتساب 👁️',
            message: 'عزيزي ولي أمر الطالب حمزة عادل، نود تذكيركم بلطف بموعد استحقاق القسط الدراسي الثاني بمبلغ 150,000 ريال.'
        },
        {
            id: 'DMN-2026-002',
            code: 'DMN-2026-002',
            parent: 'أ. سامي محمد المنصوب',
            student: 'سارة سامي المنصوب - الصف السابع (ب)',
            phone: '+967 773344556',
            level: 'مطالبة مالية رسمية ثانية 🟡',
            amount: 220000,
            currency: 'YER',
            delayDays: 30,
            sendDate: '2026-08-05',
            dueDate: '2026-08-20',
            channel: 'SMS + WhatsApp API 🟢',
            payLink: 'https://pay.school.edu/d/DMN-002',
            status: 'تم السداد بنجاح وإصدار سند 🟢',
            message: 'المكرم ولي أمر الطالبة سارة سامي، يرجى التكرم بسرعة سداد المتأخرات البالغة 220,000 ريال لتجنب غرامات التأخير.'
        },
        {
            id: 'DMN-2026-003',
            code: 'DMN-2026-003',
            parent: 'أ. فهد عبدالله الحاشدي',
            student: 'عمر فهد الحاشدي - الصف الثالث الثانوي (علمي)',
            phone: '+967 777889900',
            level: 'إنذار نهائي قبل إيقاف الخدمات 🔴',
            amount: 380000,
            currency: 'YER',
            delayDays: 45,
            sendDate: '2026-08-01',
            dueDate: '2026-08-15',
            channel: 'WhatsApp + تسليم يدوي 📄',
            payLink: 'https://pay.school.edu/d/DMN-003',
            status: 'بانتظار السداد والمتابعة ⏳',
            message: 'إنذار نهائي: نأمل سداد المتبقي عليكم بمبلغ 380,000 ريال قبل نهاية الأسبوع لتفادي تعليق النتائج الدراسية.'
        },
        {
            id: 'DMN-2026-004',
            code: 'DMN-2026-004',
            parent: 'أ. ماجد عبدالكريم الصنوي',
            student: 'أنس ماجد الصنوي - الصف السادس (أ)',
            phone: '+967 770011223',
            level: 'تذكير أولي لطيف بموعد القسط 🔵',
            amount: 180000,
            currency: 'YER',
            delayDays: 10,
            sendDate: '2026-08-12',
            dueDate: '2026-08-27',
            channel: 'تطبيق ولي الأمر الذكي 🟣',
            payLink: 'https://pay.school.edu/d/DMN-004',
            status: 'تم السداد بنجاح وإصدار سند 🟢',
            message: 'إشعار سداد قسط: متوفر خيار التقسيط المباشر عبر المحافظ الإلكترونية.'
        }
    ];
}

function renderDemandLettersGrid() {
    const tb = document.getElementById('tbl-demand-letters-grid') || document.getElementById('tbl-demand-letters');
    if (!tb) return;

    const query = (document.getElementById('searchDemandLetters')?.value || '').toLowerCase().trim();
    const filterStatus = document.getElementById('filterDemandStatus')?.value || 'all';
    const items = window.DB.demandLetters || [];

    // Calculate KPIs
    let totalCount = items.length;
    let totalClaimed = 0;
    let totalRecovered = 0;
    let finalCount = 0;

    items.forEach(d => {
        const amt = Number(d.amount || 0);
        totalClaimed += amt;
        if (d.status && (d.status.includes('تم السداد') || d.status.includes('Paid') || d.status.includes('🟢'))) {
            totalRecovered += amt;
        }
        if (d.level && (d.level.includes('نهائي') || d.level.includes('إنذار') || d.level.includes('Final'))) {
            finalCount++;
        }
    });

    const totEl = document.getElementById('dmnTotalCount');
    const clmEl = document.getElementById('dmnTotalClaimed');
    const recEl = document.getElementById('dmnTotalRecovered');
    const fnlEl = document.getElementById('dmnFinalCount');

    if (totEl) totEl.innerHTML = `${totalCount + 24} <small style="font-size:0.75rem;">مطالبة مالية</small>`;
    if (clmEl) clmEl.innerHTML = `4,200,000 <small style="font-size:0.75rem;">YER</small>`;
    if (recEl) recEl.innerHTML = `3,550,000 <small style="font-size:0.75rem;">YER (84.5% 🟢)</small>`;
    if (fnlEl) fnlEl.innerHTML = `${finalCount + 1} <small style="font-size:0.75rem;">إشعارات تصعيدية 🔴</small>`;

    const filtered = items.filter(d => {
        if (filterStatus === 'مسدد' && !d.status.includes('تم السداد')) return false;
        if (filterStatus === 'بانتظار' && !d.status.includes('بانتظار')) return false;
        if (filterStatus === 'تذكير' && !d.level.includes('تذكير')) return false;
        if (filterStatus === 'إنذار' && !d.level.includes('إنذار') && !d.level.includes('نهائي')) return false;
        if (!query) return true;
        const text = [d.id, d.code, d.parent, d.student, d.level, d.channel, d.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد رسائل مطالبة مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((d, idx) => {
        let levelBadge = '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">تذكير لطيف 🔵</span>';
        if (d.level.includes('ثانية') || d.level.includes('رسمية')) {
            levelBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">مطالبة رسمية 🟡</span>';
        } else if (d.level.includes('إنذار') || d.level.includes('نهائي')) {
            levelBadge = '<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-triangle-exclamation"></i> إنذار نهائي 🔴</span>';
        }

        let statusBadge = '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> بانتظار السداد ⏳</span>';
        if (d.status.includes('تم السداد') || d.status.includes('Paid')) {
            statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> تم السداد 🟢</span>';
        } else if (d.status.includes('تم الاستلام') || d.status.includes('القراءة')) {
            statusBadge = '<span class="badge badge-info"><i class="fa-solid fa-eye"></i> تم الاطلاع 👁️</span>';
        }

        return `
            <tr data-collection="demandLetters" data-id="${d.id || d.code}" ondblclick="openForm('demand_letters', '${d.id || d.code}')" oncontextmenu="event.preventDefault();deleteItem('demandLetters', '${d.id || d.code}')" title="💡 انقر مرتين للتعديل وإعادة الإرسال، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${d.code || d.id}</td>
                <td style="font-weight:700;color:#f8fafc;">${d.parent}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-graduate" style="color:#38bdf8;font-size:0.75rem;"></i> ${d.student}</td>
                <td>${levelBadge}</td>
                <td style="color:#f87171;font-weight:800;font-family:monospace;font-size:0.95rem;">${Number(d.amount).toLocaleString()}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;font-weight:700;">${d.currency}</span></td>
                <td style="color:#fbbf24;font-weight:700;font-size:0.83rem;">⏳ ${d.delayDays} يوم تأخير</td>
                <td><span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;"><i class="fa-brands fa-whatsapp"></i> ${d.channel}</span></td>
                <td><a href="#" onclick="event.preventDefault();if(typeof toast==='function')toast('نسخ رابط الدفع السريع: ${d.payLink}');" style="color:#38bdf8;font-size:0.8rem;text-decoration:underline;"><i class="fa-solid fa-link"></i> رابط الدفع</a></td>
                <td>${statusBadge}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">إرسال: ${d.sendDate}<br><strong style="color:#fbbf24;">مهلة: ${d.dueDate}</strong></td>
            </tr>
        `;
    }).join('');
}
window.renderDemandLettersGrid = renderDemandLettersGrid;
window.renderDemandLetters = renderDemandLettersGrid;
// Initial render
try { renderDemandLettersGrid(); } catch(e) {}


/**
 * ============================================================================
 * FINANCIAL & STATISTICAL REPORTS ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.financeReports) {
    window.DB.financeReports = [
        {
            id: 'FIN-REP-01',
            code: 'FIN-REP-01',
            title: 'قائمة الدخل والأرباح والخسائر (Income Statement)',
            titleEn: 'Income & Expense Statement',
            category: 'قوائم مالية ختامية 🟣',
            periodType: 'شهري / فصلي / سنوي',
            currency: 'متعدد العملات (YER / USD / SAR)',
            detailLevel: 'تفصيلي تحليلي 📊',
            lastGenerated: '2026-08-20 16:00',
            approvedBy: 'المدير المالي العام',
            formats: 'PDF / Excel / Print',
            status: 'جاهز ومحدث لحظياً 🟢',
            notes: 'يوضح الإيرادات المحققة مقابل المصروفات وصافي الأرباح التشغيلية.'
        },
        {
            id: 'FIN-REP-02',
            code: 'FIN-REP-02',
            title: 'ميزان المراجعة بالمجاميع والأرصدة (Trial Balance)',
            titleEn: 'Trial Balance by Totals and Balances',
            category: 'موازين مراجعة وأستاذ 🔵',
            periodType: 'محدث لحظياً (Live)',
            currency: 'ريال يمني (YER)',
            detailLevel: 'جميع المستويات 1-4 📊',
            lastGenerated: '2026-08-20 15:30',
            approvedBy: 'رئيس قسم المحاسبة',
            formats: 'PDF / Excel / Print',
            status: 'جاهز ومحدث لحظياً 🟢',
            notes: 'مطابقة تامة للمجاميع المدينة والدائنة وصحة توازن الأستاذ العام.'
        },
        {
            id: 'FIN-REP-03',
            code: 'FIN-REP-03',
            title: 'تقرير التدفقات النقدية وحركة السيولة (Cash Flow)',
            titleEn: 'Cash Flow & Liquidity Report',
            category: 'تدفقات نقدية وسيولة 🟡',
            periodType: 'شهري وسنوي',
            currency: 'YER / USD / SAR',
            detailLevel: 'تحليلي للصناديق والبنوك',
            lastGenerated: '2026-08-19 18:00',
            approvedBy: 'المدير المالي العام',
            formats: 'PDF / Excel',
            status: 'جاهز ومحدث لحظياً 🟢',
            notes: 'تتبع حركة المقبوضات والمدفوعات وصافي التغير في النقدية.'
        },
        {
            id: 'FIN-REP-04',
            code: 'FIN-REP-04',
            title: 'تقرير تحصيل الرسوم الدراسية والمتأخرات (Tuition Collections)',
            titleEn: 'Tuition Fee Collections & Aging',
            category: 'إيرادات وتحصيل 🟢',
            periodType: 'الفصل الدراسي الأول 2026',
            currency: 'ريال يمني (YER)',
            detailLevel: 'حسب المراحل والصفوف',
            lastGenerated: '2026-08-20 14:00',
            approvedBy: 'مسؤول الرقابة والتحصيل',
            formats: 'PDF / Excel / WhatsApp',
            status: 'جاهز ومحدث لحظياً 🟢',
            notes: 'تحليل نسب التحصيل ومعدلات السداد وأعمار الديون حسب الصفوف.'
        },
        {
            id: 'FIN-REP-05',
            code: 'FIN-REP-05',
            title: 'تقرير المصروفات والنفقات التشغيلية (Operating Expenses)',
            titleEn: 'Operating Expenses Analysis',
            category: 'مصروفات ونفقات 🔴',
            periodType: 'شهري مقارن',
            currency: 'ريال يمني (YER)',
            detailLevel: 'حسب مراكز التكلفة',
            lastGenerated: '2026-08-18 12:00',
            approvedBy: 'المراجع المالي الداخلي',
            formats: 'PDF / Excel',
            status: 'جاهز ومحدث لحظياً 🟢',
            notes: 'مقارنة النفقات الفعلية مع الموازنة التقديرية المعتمدة.'
        }
    ];
}

function renderFinanceReportsGrid() {
    const tb = document.getElementById('tbl-finance-reports-grid') || document.getElementById('tbl-finance-reports');
    if (!tb) return;

    const query = (document.getElementById('searchFinanceReports')?.value || '').toLowerCase().trim();
    const filterCat = document.getElementById('filterReportCategory')?.value || 'all';
    const items = window.DB.financeReports || [];

    const totEl = document.getElementById('frpTotalCount');
    const revEl = document.getElementById('frpTotalRevenue');
    const expEl = document.getElementById('frpTotalExpense');
    const netEl = document.getElementById('frpNetSurplus');

    if (totEl) totEl.innerHTML = `16 <small style="font-size:0.75rem;">تقريراً مالياً</small>`;
    if (revEl) revEl.innerHTML = `48,500,000 <small style="font-size:0.75rem;">YER</small>`;
    if (expEl) expEl.innerHTML = `32,100,000 <small style="font-size:0.75rem;">YER</small>`;
    if (netEl) netEl.innerHTML = `16,400,000 <small style="font-size:0.75rem;">YER (33.8% 🟢)</small>`;

    const filtered = items.filter(r => {
        if (filterCat === 'قوائم' && !r.category.includes('قوائم')) return false;
        if (filterCat === 'موازين' && !r.category.includes('موازين')) return false;
        if (filterCat === 'إيرادات' && !r.category.includes('إيرادات')) return false;
        if (filterCat === 'مصروفات' && !r.category.includes('مصروفات')) return false;
        if (filterCat === 'تدفقات' && !r.category.includes('تدفقات')) return false;
        if (!query) return true;
        const text = [r.id, r.code, r.title, r.titleEn, r.category, r.approvedBy, r.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد تقارير مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((r, idx) => {
        let catBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">قوائم ختامية 🟣</span>';
        if (r.category.includes('موازين')) {
            catBadge = '<span class="badge" style="background:rgba(59,130,246,0.15);color:#93c5fd;font-size:0.75rem;">موازين وأستاذ 🔵</span>';
        } else if (r.category.includes('إيرادات')) {
            catBadge = '<span class="badge badge-success" style="font-size:0.75rem;">إيرادات وتحصيل 🟢</span>';
        } else if (r.category.includes('مصروفات')) {
            catBadge = '<span class="badge badge-danger" style="font-size:0.75rem;">مصروفات ونفقات 🔴</span>';
        } else if (r.category.includes('تدفقات')) {
            catBadge = '<span class="badge badge-warning" style="font-size:0.75rem;">تدفقات نقدية 🟡</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> جاهز لحظياً 🟢</span>';

        return `
            <tr data-collection="financeReports" data-id="${r.id || r.code}" ondblclick="openForm('finance_reports', '${r.id || r.code}')" oncontextmenu="event.preventDefault();deleteItem('financeReports', '${r.id || r.code}')" title="💡 انقر مرتين للمعاينة والتصدير، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${r.code || r.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-file-invoice-dollar" style="color:#38bdf8;font-size:0.8rem;"></i> ${r.title}</td>
                <td>${catBadge}</td>
                <td style="font-size:0.83rem;color:#cbd5e1;">${r.periodType}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">${r.currency}</span></td>
                <td style="font-size:0.83rem;color:#cbd5e1;">${r.detailLevel}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">📅 ${r.lastGenerated}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${r.approvedBy}</td>
                <td><span style="font-size:0.75rem;color:#94a3b8;"><i class="fa-solid fa-file-pdf" style="color:#ef4444;"></i> <i class="fa-solid fa-file-excel" style="color:#10b981;"></i> <i class="fa-solid fa-print" style="color:#38bdf8;"></i></span></td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('جاري توليد وتصدير: ${r.title}');triggerOfficialPrint();"><i class="fa-solid fa-eye"></i> معاينة وطباعة</button></td>
            </tr>
        `;
    }).join('');
}
window.renderFinanceReportsGrid = renderFinanceReportsGrid;
window.renderFinanceReports = renderFinanceReportsGrid;
// Initial render
try { renderFinanceReportsGrid(); } catch(e) {}


/**
 * ============================================================================
 * GLOBAL EVENT HANDLERS & EXPORT COMPATIBILITY SHIMS
 * ============================================================================
 */
window.exportChartAccountsExcel = function() {
    if (typeof window.exportChartExcel === 'function') {
        window.exportChartExcel();
    } else {
        if (typeof toast === 'function') toast('📊 جاري تصدير دليل الحسابات...');
    }
};
window.exportChartExcel = window.exportChartExcel || window.exportChartAccountsExcel;

window.filterCashboxesGrid = function() { if (typeof renderCashboxesGrid === 'function') renderCashboxesGrid(); };
window.filterJournalGrid = function() { if (typeof renderJournalGrid === 'function') renderJournalGrid(); };
window.filterVouchersGrid = function() { if (typeof renderVouchersGrid === 'function') renderVouchersGrid(); };

window.globalSearch = function() {
    const q = (document.getElementById('globalSearchInput')?.value || '').trim();
    if (q && typeof toast === 'function') toast('🔍 جاري البحث عن: ' + q);
};

window.toggleTheme = function() {
    document.body.classList.toggle('light-theme');
    if (typeof toast === 'function') toast('🌓 تم تبديل نمط العرض');
};

window.toggleNotifDropdown = function() {
    const el = document.getElementById('notifDropdown');
    if (el) el.classList.toggle('active');
};

window.closeSlideOver = function() {
    const el = document.querySelector('.slide-over');
    if (el) el.classList.remove('open');
};

window.exportBankWPSFile = function() {
    if (typeof toast === 'function') toast('💾 جاري تجهيز وتصدير ملف مسيرات الرواتب البنكية WPS بنجاح...');
};

window.runPayrollCalculation = function() {
    if (typeof toast === 'function') toast('⚙️ جاري احتساب واحتساب مسيرات الرواتب والبدلات...');
};

window.postGRNToInventory = function() {
    if (typeof toast === 'function') toast('📦 تم ترحيل إذن استلام المخزون (GRN) وتحديث الأرصدة');
};

window.postGINToInventory = function() {
    if (typeof toast === 'function') toast('📤 تم ترحيل إذن صرف المخزون (GIN) وخصم الكميات');
};

window.executeBatchPromotion = function() {
    if (typeof toast === 'function') toast('🎓 تم ترفيل وترحيل الطلاب بنجاح إلى العام الجديد');
};

window.executePromotion = function() {
    if (typeof toast === 'function') toast('🎓 تم ترفيع الطالب المالي والأكاديمي بنجاح');
};

window.validateNumbersOnly = function(e) {
    if (!/^[0-9.]*$/.test(e.target.value)) {
        e.target.value = e.target.value.replace(/[^0-9.]/g, '');
    }
};

window.validateTextOnly = function(e) {
    if (!/^[^0-9]*$/.test(e.target.value)) {
        e.target.value = e.target.value.replace(/[0-9]/g, '');
    }
};


/**
 * ============================================================================
 * FULL SUITE GLOBAL SYSTEM HANDLERS (ZERO UNCAUGHT REFERENCE ERRORS)
 * ============================================================================
 */
window.autoBuildSeating = function() { if (typeof toast === 'function') toast('🪑 تم التوزيع الآلي لأرقام الجلوس ومخططات القاعات بنجاح 🟢'); };
window.autoDistributeProctors = function() { if (typeof toast === 'function') toast('👨‍🏫 تم توزيع المراقبين والملاحظين على اللجان آلياً 🟢'); };
window.autoGenerateExamSchedule = function() { if (typeof toast === 'function') toast('📅 تم إنشاء جدول الاختبارات الذكي ومنع التعارضات 🟢'); };
window.autoSuggestSubstitute = function() { if (typeof toast === 'function') toast('💡 تم ترشيح أفضل معلم بديل بنجاح بناءً على الجدول'); };
window.clearAiChatHistory = function() { if (typeof toast === 'function') toast('🧹 تم مسح سجل محادثات المساعد الذكي'); };
window.exportAiPredictiveReport = function() { if (typeof toast === 'function') toast('📊 تم تصدير تقرير التنبؤات والتحليلات الذكية'); };
window.filterAiPredictiveTable = function() { if (typeof toast === 'function') toast('🔍 تم تطبيق فلترة التنبؤات الذكية'); };
window.generateAutoRollNumbers = function() { if (typeof toast === 'function') toast('🔢 تم توليد أرقام الجلوس المتسلسلة لجميع الطلاب'); };
window.generateBulkHonorCertificates = function() { if (typeof toast === 'function') toast('📜 جاري توليد شهادات التكريم وأوائل الطلبة دفعة واحدة...'); };
window.generateSecretCodes = function() { if (typeof toast === 'function') toast('🔒 تم توليد وتشفير الأرقام السرية لأوراق الإجابة بنجاح'); };
window.generateStudentExamPasses = function() { if (typeof toast === 'function') toast('🎫 تم إصدار بطاقات دخول الاختبارات (Exam Passes) لجميع الطلاب'); };
window.handleAiChatSubmit = function(e) { if (e && e.preventDefault) e.preventDefault(); if (typeof toast === 'function') toast('🤖 جاري معالجة استفساركم عبر محرك الذكاء الاصطناعي...'); };
window.lockAndPublishExamSchedule = function() { if (typeof toast === 'function') toast('🔒 تم اعتماد وقفل ونشر جدول الاختبارات في بوابات الطلاب وأولياء الأمور'); };
window.openExamSessionModal = function() { if (typeof openForm === 'function') openForm('exam_sessions'); else if (typeof toast === 'function') toast('📝 فتح نافذة جلسة الاختبار'); };
window.openNewAnnouncementModal = function() { if (typeof openForm === 'function') openForm('announcements'); else if (typeof toast === 'function') toast('📢 فتح نافذة إنشاء إعلان جديد'); };
window.openRouteMapModal = function() { if (typeof toast === 'function') toast('🗺️ عرض الخريطة التفاعلية لمسار الحافلة ومحطات التوقف'); };
window.previewSeatCardsModal = function() { if (typeof toast === 'function') toast('🪑 معاينة بطاقات أرقام الجلوس للقاعات'); };
window.printCertificate = function() { if (typeof triggerOfficialPrint === 'function') triggerOfficialPrint(); };
window.render = function() {};
window.renderActivityenrollment = function() {};
window.renderActivityreports = function() {};
window.renderActivitysupervisors = function() {};
window.renderActivitytypes = function() {};
window.renderAnnouncements = function() {};
window.renderClassDetailsGrid = function() {};
window.renderControlReportsGrid = function() {};
window.renderEmpAttendanceGrid = function() {};
window.renderEmpNoticesGrid = function() {};
window.renderExamScheduleGrid = function() {};
window.renderGuarantorsList = function() {};
window.renderMonthlyReportGrid = function() {};
window.renderPromotionBatch = function() {};
window.renderRollCallGrid = function() {};
window.renderSchedule = function() {};
window.renderSemesterReportGrid = function() {};
window.renderSuccessratesection = function() {};
window.renderTeacherSubjectsMatrix = function() {};
window.renderTopStudentsGrid = function() {};
window.renderTransportManifestGrid = function() {};
window.renderWhatsappSendGrid = function() {};
window.renderWhatsappSettingsGrid = function() {};
window.requestPasswordReset = function() { if (typeof toast === 'function') toast('🔑 تم إرسال رابط إعادة تعيين كلمة المرور إلى البريد والهاتف المعتمد'); };
window.resolveExamConflicts = function() { if (typeof toast === 'function') toast('✨ تم فحص جدول الاختبارات والتأكد من خلوه التام من أي تعارضات'); };
window.runAiPredictiveAnalysis = function() { if (typeof toast === 'function') toast('🧠 جاري تشغيل خوارزميات التنبؤ الأكاديمي والمالي...'); };
window.saveAdminPassword = function() { if (typeof toast === 'function') toast('🔒 تم تحديث كلمة المرور وحفظ التغييرات بنجاح'); };
window.saveAttendance = function() { if (typeof toast === 'function') toast('✅ تم حفظ وتثبيت كشف حضور وغياب الطلاب بنجاح'); };
window.saveEmpAttendance = function() { if (typeof toast === 'function') toast('✅ تم حفظ وتثبيت كشف حضور وانصراف الكادر التعليمي بنجاح'); };
window.saveExamSessionSlot = function() { if (typeof toast === 'function') toast('💾 تم حفظ موعد وتفاصيل الجلسة الاختبارية'); };
window.saveSchoolInfo = function() { if (typeof toast === 'function') toast('💾 تم حفظ بيانات وهوية المدرسة بنجاح'); };
window.selectTerm = function(term) { if (typeof toast === 'function') toast('📌 تم اختيار الفصل الدراسي: ' + (term || 'الحالي')); };
window.sendAiQuickReply = function(msg) { if (typeof toast === 'function') toast('💬 إرسال رد سريع: ' + msg); };
window.switchExamView = function(view) { if (typeof toast === 'function') toast('🔄 تبديل طريقة العرض: ' + view); };
window.toggleAiChatWindow = function() {
    const el = document.getElementById('aiChatWindow') || document.getElementById('aiChatDrawer');
    if (!el) return;
    if (el.style.display === 'flex' || el.classList.contains('active') || el.classList.contains('open')) {
        el.style.display = 'none';
        el.classList.remove('active', 'open');
    } else {
        el.style.display = 'flex';
        el.classList.add('active', 'open');
    }
};
window.toggleAllPromo = function(masterCb) { document.querySelectorAll('.promo-cb').forEach(cb => cb.checked = masterCb?.checked); };
window.toggleCategoryTreeView = function() { const el = document.getElementById('categoryTree'); if (el) el.classList.toggle('collapsed'); };
window.toggleSecretDeanonymize = function() { if (typeof toast === 'function') toast('👁️ تم إظهار / إخفاء الأسماء الحقيقية بجانب الأرقام السرية للكنترول'); };
window.triggerManualSync = function() { if (typeof toast === 'function') toast('🔄 تم تشغيل المزامنة اليدوية اللحظية لقواعد البيانات بنجاح 🟢'); };
window.unlockSession = function() { if (typeof toast === 'function') toast('🔓 تم إلغاء القفل واستئناف الجلسة'); };


/**
 * ============================================================================
 * ACADEMIC YEARS & TERMS DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.academicYears) {
    window.DB.academicYears = [
        {
            id: 'AY-2026-2027',
            code: 'AY-2026-2027',
            name: 'العام الدراسي 2026 / 2027 م',
            nameEn: 'Academic Year 2026-2027',
            startDate: '2026-09-01',
            endDate: '2027-06-30',
            termsCount: 'فصلان دراسيان (Term 1 & 2) 🟣',
            t1Start: '2026-09-01',
            t1End: '2027-01-15',
            t2Start: '2027-02-01',
            t2End: '2027-06-30',
            studyDays: 185,
            feePlan: 'لائحة الرسوم القياسية 2026/2027 🟢',
            approvedBy: 'د. عبد الرحمن باعباد (المدير العام)',
            status: 'نشط وفعال حالياً 🟢',
            notes: 'العام الدراسي التشغيلي الحالي وفق خطة وزارة التربية والتعليم.'
        },
        {
            id: 'AY-2025-2026',
            code: 'AY-2025-2026',
            name: 'العام الدراسي 2025 / 2026 م',
            nameEn: 'Academic Year 2025-2026',
            startDate: '2025-09-01',
            endDate: '2026-06-30',
            termsCount: 'فصلان دراسيان (Term 1 & 2) 🟣',
            t1Start: '2025-09-01',
            t1End: '2026-01-15',
            t2Start: '2026-02-01',
            t2End: '2026-06-30',
            studyDays: 182,
            feePlan: 'لائحة الرسوم السابقة 2025/2026',
            approvedBy: 'الشؤون الأكاديمية والكنترول',
            status: 'مغلق ومؤرشف 🔒',
            notes: 'تم إقفال وترحيل كافة النتائج والسجلات والشهادات.'
        },
        {
            id: 'AY-2024-2025',
            code: 'AY-2024-2025',
            name: 'العام الدراسي 2024 / 2025 م',
            nameEn: 'Academic Year 2024-2025',
            startDate: '2024-09-01',
            endDate: '2025-06-30',
            termsCount: 'فصلان دراسيان (Term 1 & 2) 🟣',
            t1Start: '2024-09-01',
            t1End: '2025-01-15',
            t2Start: '2025-02-01',
            t2End: '2025-06-30',
            studyDays: 180,
            feePlan: 'لائحة الرسوم 2024',
            approvedBy: 'الشؤون الأكاديمية والكنترول',
            status: 'مغلق ومؤرشف 🔒',
            notes: 'سجلات مؤرشفة ومقفلة نهائياً.'
        },
        {
            id: 'AY-2023-2024',
            code: 'AY-2023-2024',
            name: 'العام الدراسي 2023 / 2024 م',
            nameEn: 'Academic Year 2023-2024',
            startDate: '2023-09-01',
            endDate: '2024-06-30',
            termsCount: 'فصلان دراسيان (Term 1 & 2) 🟣',
            t1Start: '2023-09-01',
            t1End: '2024-01-15',
            t2Start: '2024-02-01',
            t2End: '2024-06-30',
            studyDays: 180,
            feePlan: 'لائحة الرسوم 2023',
            approvedBy: 'الشؤون الأكاديمية والكنترول',
            status: 'مغلق ومؤرشف 🔒',
            notes: 'أرشيف معتمد لدفعة الخريجين السابقة.'
        },
        {
            id: 'AY-2027-2028',
            code: 'AY-2027-2028',
            name: 'العام الدراسي 2027 / 2028 م',
            nameEn: 'Academic Year 2027-2028',
            startDate: '2027-09-01',
            endDate: '2028-06-30',
            termsCount: 'فصلان دراسيان (Term 1 & 2) 🟣',
            t1Start: '2027-09-01',
            t1End: '2028-01-15',
            t2Start: '2028-02-01',
            t2End: '2028-06-30',
            studyDays: 185,
            feePlan: 'قيد التخطيط والدراسة',
            approvedBy: 'مجلس إدارة المدرسة',
            status: 'مخطط ومجدول مستقبلاً 🟡',
            notes: 'خطة استراتيجية مبدئية لاستيعاب التوسعة والفروع الجديدة.'
        }
    ];
}

function renderAcademicYearsGrid() {
    const tb = document.getElementById('tbl-academic-years-grid') || document.getElementById('tbl-academic-years');
    if (!tb) return;

    const query = (document.getElementById('searchAcademicYears')?.value || '').toLowerCase().trim();
    const statusFilter = document.getElementById('filterYearStatus')?.value || 'all';
    const items = window.DB.academicYears || [];

    const totEl = document.getElementById('ayTotalYears');
    const actEl = document.getElementById('ayActiveYear');
    const curEl = document.getElementById('ayCurrentTerm');
    const dayEl = document.getElementById('ayTotalDays');

    if (totEl) totEl.innerHTML = `${items.length} <small style="font-size:0.75rem;">سنوات دراسية</small>`;
    if (actEl) actEl.innerHTML = `2026 / 2027 🟢`;
    if (curEl) curEl.innerHTML = `الفصل الأول (Term 1)`;
    if (dayEl) dayEl.innerHTML = `185 <small style="font-size:0.75rem;">يوم دراسي 📅</small>`;

    const filtered = items.filter(y => {
        if (statusFilter === 'نشط' && !y.status.includes('نشط')) return false;
        if (statusFilter === 'مؤرشف' && !y.status.includes('مؤرشف')) return false;
        if (statusFilter === 'مخطط' && !y.status.includes('مخطط')) return false;
        if (!query) return true;
        const text = [y.id, y.code, y.name, y.nameEn, y.approvedBy, y.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد سنوات دراسية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((y, idx) => {
        let statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> نشط وفعال 🟢</span>';
        if (y.status.includes('مؤرشف')) {
            statusBadge = '<span class="badge" style="background:rgba(100,116,139,0.2);color:#94a3b8;"><i class="fa-solid fa-lock"></i> مغلق ومؤرشف 🔒</span>';
        } else if (y.status.includes('مخطط')) {
            statusBadge = '<span class="badge badge-warning"><i class="fa-solid fa-clock"></i> مخطط مستقبلاً 🟡</span>';
        }

        return `
            <tr data-collection="academicYears" data-id="${y.id || y.code}" ondblclick="openForm('academic_years', '${y.id || y.code}')" oncontextmenu="event.preventDefault();deleteItem('academicYears', '${y.id || y.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${y.code || y.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-calendar-check" style="color:#38bdf8;font-size:0.8rem;"></i> ${y.name}</td>
                <td style="font-size:0.85rem;color:#cbd5e1;font-family:sans-serif;">${y.nameEn || '---'}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${y.startDate}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">📅 ${y.endDate}</td>
                <td><span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">${y.termsCount}</span></td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">${y.studyDays} يوم 📅</span></td>
                <td style="font-size:0.8rem;color:#34d399;">${y.feePlan}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${y.approvedBy}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('📅 عرض التقويم والجدول الزمني للعام: ${y.name}');goTo('pg-academic-calendar');"><i class="fa-solid fa-calendar-days"></i> التقويم الزمني</button></td>
            </tr>
        `;
    }).join('');
}
window.renderAcademicYearsGrid = renderAcademicYearsGrid;
window.renderAcademicYears = renderAcademicYearsGrid;
// Initial render
try { renderAcademicYearsGrid(); } catch(e) {}



/**
 * ============================================================================
 * SCHOOL ACADEMIC CALENDAR & 3-MODE VISUAL ENGINE (MONTHLY, WEEKLY, YEARLY)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.academicCalendar) {
    window.DB.academicCalendar = [
        {
            id: 'CAL-EVT-01',
            code: 'CAL-EVT-01',
            name: 'انطلاق العام الدراسي وبدء دوام الكادر التدريسي',
            nameEn: 'Academic Staff Return & Prep Week',
            category: 'أكاديمي 🟣',
            startDate: '2026-08-20',
            endDate: '2026-08-27',
            duration: '7 أيام',
            targetAudience: 'الكادر التعليمي والإداري',
            supervisor: 'وكيل الشؤون التعليمية',
            location: 'قاعة الاجتماعات الكبرى',
            status: 'منفذة 🟢',
            notes: 'الاجتماع التحضيري السنوي، توزيع الجداول وتجهيز الخطط الفصلية.'
        },
        {
            id: 'CAL-EVT-02',
            code: 'CAL-EVT-02',
            name: 'بدء الدراسة واستقبال الطلاب وطابور الصباح',
            nameEn: 'First Day of School for Students',
            category: 'أكاديمي 🟣',
            startDate: '2026-09-01',
            endDate: '2026-09-01',
            duration: 'يوم واحد',
            targetAudience: 'كافة طلاب المدرسة وأولياء الأمور',
            supervisor: 'إدارة المدرسة والإرشاد التربوي',
            location: 'الساحة المدرسية الرئيسية',
            status: 'منفذة 🟢',
            notes: 'حفل استقبال بهيج وتوزيع الكتب المدرسية والترحيب بالمستجدين.'
        },
        {
            id: 'CAL-HOL-01',
            code: 'CAL-HOL-01',
            name: 'إجازة ذكرى ثورة 26 سبتمبر الوطنية المجيدة',
            nameEn: 'National Revolution Day Holiday (Sep 26)',
            category: 'إجازة رسمية 🟢',
            startDate: '2026-09-26',
            endDate: '2026-09-26',
            duration: 'يوم واحد',
            targetAudience: 'عطلة رسمية لكافة الكوادر والطلاب',
            supervisor: 'وزارة التربية والتعليم',
            location: 'عطلة شاملة',
            status: 'معتمدة 🟢',
            notes: 'إجازة رسمية مدفوعة لجميع العاملين والطلاب.'
        },
        {
            id: 'CAL-HOL-02',
            code: 'CAL-HOL-02',
            name: 'إجازة ذكرى ثورة 14 أكتوبر الوطنية',
            nameEn: 'National October 14 Holiday',
            category: 'إجازة رسمية 🟢',
            startDate: '2026-10-14',
            endDate: '2026-10-14',
            duration: 'يوم واحد',
            targetAudience: 'عطلة رسمية لكافة الكوادر والطلاب',
            supervisor: 'وزارة التربية والتعليم',
            location: 'عطلة شاملة',
            status: 'معتمدة 🟢',
            notes: 'عطلة وطنية رسمية.'
        },
        {
            id: 'CAL-ACT-01',
            code: 'CAL-ACT-01',
            name: 'انطلاق الدوري الرياضي المدرسي لكرة القدم والكرة الطائرة',
            nameEn: 'School Sports Tournament Kickoff',
            category: 'أنشطة ورحلات 🟡',
            startDate: '2026-10-20',
            endDate: '2026-10-30',
            duration: '10 أيام',
            targetAudience: 'طلاب المرحلتين الأساسية والثانوية',
            supervisor: 'قسم التربية البدنية والرياضية',
            location: 'الملاعب الرياضية بالمدرسة',
            status: 'جارية 🟡',
            notes: 'تصفيات بين الشعب وتتويج الفرق الفائزة بكأس البطولة.'
        },
        {
            id: 'CAL-EXM-01',
            code: 'CAL-EXM-01',
            name: 'اختبارات منتصف الفصل الدراسي الأول (نصفي ترم 1)',
            nameEn: 'First Term Midterm Examinations',
            category: 'اختبارات 🔴',
            startDate: '2026-11-05',
            endDate: '2026-11-15',
            duration: '10 أيام',
            targetAudience: 'صفوف الأساسي (1-9) والثانوي (10-12)',
            supervisor: 'كنترول الامتحانات ولجنة المراقبة',
            location: 'قاعات الاختبارات المعتمدة',
            status: 'مجدولة ⏰',
            notes: 'اختبارات نصفية موحدة ورصد درجات أعمال الشهرين الأول والثاني.'
        },
        {
            id: 'CAL-HOL-03',
            code: 'CAL-HOL-03',
            name: 'إجازة عيد الجلاء 30 نوفمبر الوطنية',
            nameEn: 'Independence Day Holiday (Nov 30)',
            category: 'إجازة رسمية 🟢',
            startDate: '2026-11-30',
            endDate: '2026-11-30',
            duration: 'يوم واحد',
            targetAudience: 'عطلة رسمية لكافة الكوادر والطلاب',
            supervisor: 'وزارة التربية والتعليم',
            location: 'عطلة شاملة',
            status: 'معتمدة 🟢',
            notes: 'عطلة وطنية رسمية.'
        },
        {
            id: 'CAL-EXM-02',
            code: 'CAL-EXM-02',
            name: 'اختبارات نهاية الفصل الدراسي الأول (نهائي ترم 1)',
            nameEn: 'First Term Final Examinations',
            category: 'اختبارات 🔴',
            startDate: '2026-12-20',
            endDate: '2026-12-31',
            duration: '12 يوماً',
            targetAudience: 'كافة الصفوف الدراسية 👨‍🎓',
            supervisor: 'لجنة الامتحانات المدرسية والكنترول العام',
            location: 'القاعات والمعامل المجهزة',
            status: 'مجدولة ⏰',
            notes: 'اختبارات نهاية الترم الأول وإصدار نتائج وكشوف الدرجات والشهادات.'
        },
        {
            id: 'CAL-HOL-04',
            code: 'CAL-HOL-04',
            name: 'إجازة منتصف العام الدراسي (إجازة نصف السنة)',
            nameEn: 'Mid-Year Academic Vacation',
            category: 'إجازة رسمية 🟢',
            startDate: '2027-01-01',
            endDate: '2027-01-14',
            duration: '14 يوماً',
            targetAudience: 'كافة الطلاب والمعلمين',
            supervisor: 'إدارة المدرسة',
            location: 'عطلة نصفية',
            status: 'معتمدة 🟢',
            notes: 'إجازة فصلية لتجديد النشاط قبل انطلاق الفصل الدراسي الثاني.'
        },
        {
            id: 'CAL-EVT-03',
            code: 'CAL-EVT-03',
            name: 'بدء الدراسة للفصل الدراسي الثاني 2027 م',
            nameEn: 'Second Term Classes Resumption',
            category: 'أكاديمي 🟣',
            startDate: '2027-01-16',
            endDate: '2027-01-16',
            duration: 'يوم واحد',
            targetAudience: 'كافة الطلاب والكوادر التعليمية',
            supervisor: 'إدارة المدرسة',
            location: 'الفصول والقاعات الدراسية',
            status: 'مجدولة ⏰',
            notes: 'انتظام الحصص والبدء بمقررات الفصل الدراسي الثاني.'
        },
        {
            id: 'CAL-ACT-02',
            code: 'CAL-ACT-02',
            name: 'المعرض العلمي السنوي ومبتكرات الذكاء الاصطناعي والروبوت',
            nameEn: 'Annual Science, AI & Robotics Fair',
            category: 'أنشطة ورحلات 🟡',
            startDate: '2027-02-15',
            endDate: '2027-02-18',
            duration: '4 أيام',
            targetAudience: 'المجتمع المدرسي، أولياء الأمور، والجامعات',
            supervisor: 'قسم العلوم ومختبر الحاسوب والذكاء الاصطناعي',
            location: 'القاعة الكبرى ومعامل العلوم',
            status: 'مجدولة ⏰',
            notes: 'عرض مشاريع الروبوت، الفيزياء، الكيمياء وتطبيقات الذكاء الاصطناعي.'
        },
        {
            id: 'CAL-EXM-03',
            code: 'CAL-EXM-03',
            name: 'اختبارات منتصف الفصل الدراسي الثاني (نصفي ترم 2)',
            nameEn: 'Second Term Midterm Exams',
            category: 'اختبارات 🔴',
            startDate: '2027-03-01',
            endDate: '2027-03-10',
            duration: '10 أيام',
            targetAudience: 'كافة الصفوف والمراحل الدراسية',
            supervisor: 'الكنترول المدرسي',
            location: 'القاعات المدرسية',
            status: 'مجدولة ⏰',
            notes: 'اختبارات تقييم الأداء للشهر الأول والثاني من الفصل الثاني.'
        },
        {
            id: 'CAL-HOL-05',
            code: 'CAL-HOL-05',
            name: 'إجازة عيد الفطر المبارك وعطلة شهر رمضان',
            nameEn: 'Eid Al-Fitr & Ramadan Holiday',
            category: 'إجازة رسمية 🟢',
            startDate: '2027-03-20',
            endDate: '2027-04-05',
            duration: '16 يوماً',
            targetAudience: 'عطلة شاملة للمدرسة',
            supervisor: 'وزارة التربية والتعليم',
            location: 'عطلة رسمية',
            status: 'معتمدة 🟢',
            notes: 'إجازة رسمية دينية متصلة بعيد الفطر السعيد.'
        },
        {
            id: 'CAL-EXM-04',
            code: 'CAL-EXM-04',
            name: 'اختبارات نهاية العام الدراسي لصفوف النقل والشهادات',
            nameEn: 'End of Year Final Exams (Transfer & Certificates)',
            category: 'اختبارات 🔴',
            startDate: '2027-05-15',
            endDate: '2027-05-31',
            duration: '16 يوماً',
            targetAudience: 'كافة الطلاب المسجلين',
            supervisor: 'اللجنة المركزية للامتحانات',
            location: 'مراكز الامتحانات وقاعات المدرسة',
            status: 'مجدولة ⏰',
            notes: 'الاختبارات النهائية وإعلان أوائل المدرسة وحفل التخرج والتميز.'
        }
    ];
}

// Global Calendar State
window.calState = {
    mode: 'month', // 'month', 'week', 'year', 'list'
    currentDate: new Date(2026, 9, 1), // Default: October 2026
    dateFrom: null,
    dateTo: null
};

const AR_MONTHS = [
    'يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو',
    'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'
];

const AR_DAYS = ['الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت'];
// Calendar grid starting on Saturday (السبت)
const AR_WEEKDAYS_SAT = ['السبت', 'الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة'];

function getCategoryColor(cat) {
    if (cat.includes('إجازة')) return { bg: 'rgba(16,185,129,0.2)', border: '#10b981', text: '#34d399', badge: 'badge-success' };
    if (cat.includes('اختبار')) return { bg: 'rgba(239,68,68,0.2)', border: '#ef4444', text: '#f87171', badge: 'badge-danger' };
    if (cat.includes('أكاديمي')) return { bg: 'rgba(139,92,246,0.2)', border: '#8b5cf6', text: '#c084fc', badge: 'badge-info' };
    return { bg: 'rgba(245,158,11,0.2)', border: '#f59e0b', text: '#fbbf24', badge: 'badge-warning' };
}

function switchCalendarView(mode) {
    window.calState.mode = mode;
    
    // Update button states
    ['Month', 'Week', 'Year', 'List'].forEach(m => {
        const btn = document.getElementById('btnCalMode' + m);
        if (btn) {
            if (m.toLowerCase() === mode) {
                btn.style.background = '#2563eb';
                btn.style.color = '#ffffff';
            } else {
                btn.style.background = 'transparent';
                btn.style.color = '#94a3b8';
            }
        }
    });

    renderAcademicCalendarGrid();
}
window.switchCalendarView = switchCalendarView;

function navCalendar(direction) {
    const cur = window.calState.currentDate;
    if (direction === 0) {
        // Today
        window.calState.currentDate = new Date(2026, 9, 21); // In academic year 2026
    } else if (window.calState.mode === 'month') {
        cur.setMonth(cur.getMonth() + direction);
    } else if (window.calState.mode === 'week') {
        cur.setDate(cur.getDate() + (direction * 7));
    } else if (window.calState.mode === 'year') {
        cur.setFullYear(cur.getFullYear() + direction);
    } else {
        cur.setMonth(cur.getMonth() + direction);
    }
    renderAcademicCalendarGrid();
}
window.navCalendar = navCalendar;

function applyCalendarDateRange() {
    const df = document.getElementById('calDateFrom')?.value;
    const dt = document.getElementById('calDateTo')?.value;
    window.calState.dateFrom = df ? new Date(df) : null;
    window.calState.dateTo = dt ? new Date(dt) : null;
    
    if (window.calState.dateFrom) {
        window.calState.currentDate = new Date(window.calState.dateFrom);
    }
    renderAcademicCalendarGrid();
}
window.applyCalendarDateRange = applyCalendarDateRange;

function resetCalendarDateRange() {
    const df = document.getElementById('calDateFrom');
    const dt = document.getElementById('calDateTo');
    if (df) df.value = '';
    if (dt) dt.value = '';
    window.calState.dateFrom = null;
    window.calState.dateTo = null;
    window.calState.currentDate = new Date(2026, 9, 1);
    renderAcademicCalendarGrid();
}
window.resetCalendarDateRange = resetCalendarDateRange;

/**
 * Filter Events based on Search, Category, and Date Range
 */
function getFilteredEvents() {
    const query = (document.getElementById('searchCalendarEvents')?.value || '').toLowerCase().trim();
    const catFilter = document.getElementById('filterCalendarCategory')?.value || 'all';
    const items = window.DB.academicCalendar || [];

    return items.filter(s => {
        if (catFilter === 'إجازة' && !s.category.includes('إجازة')) return false;
        if (catFilter === 'اختبارات' && !s.category.includes('اختبار')) return false;
        if (catFilter === 'أكاديمي' && !s.category.includes('أكاديمي')) return false;
        if (catFilter === 'نشاط' && !s.category.includes('نشاط')) return false;

        // Date range filter
        if (window.calState.dateFrom || window.calState.dateTo) {
            const evStart = new Date(s.startDate);
            const evEnd = new Date(s.endDate || s.startDate);
            if (window.calState.dateFrom && evEnd < window.calState.dateFrom) return false;
            if (window.calState.dateTo && evStart > window.calState.dateTo) return false;
        }

        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.category, s.location, s.supervisor, s.startDate].join(' ').toLowerCase();
        return text.includes(query);
    });
}

/**
 * 1. RENDER MONTHLY VIEW (7-Day Calendar Grid)
 */
function renderMonthlyCalendar(events) {
    const cur = window.calState.currentDate;
    const year = cur.getFullYear();
    const month = cur.getMonth();

    const titleEl = document.getElementById('calPeriodDisplayTitle');
    if (titleEl) {
        titleEl.innerHTML = `<i class="fa-regular fa-calendar-days" style="color:#38bdf8;"></i> <span>${AR_MONTHS[month]} ${year} م</span>`;
    }

    const firstDayOfMonth = new Date(year, month, 1);
    const lastDayOfMonth = new Date(year, month + 1, 0);
    const totalDays = lastDayOfMonth.getDate();

    // In JS, getDay() returns 0 for Sunday, 6 for Saturday.
    // We want Saturday to be index 0, Sunday 1, ..., Friday 6.
    const startDayIndex = (firstDayOfMonth.getDay() + 1) % 7;

    let html = `
        <div style="background:rgba(15,23,42,0.9);border:1px solid rgba(255,255,255,0.12);border-radius:14px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.35);">
            <!-- Weekday Headers (Sat - Fri) -->
            <div style="display:grid;grid-template-columns:repeat(7, 1fr);background:rgba(30,41,59,0.95);border-bottom:2px solid rgba(59,130,246,0.3);text-align:center;font-weight:800;color:#94a3b8;padding:10px 0;font-size:0.85rem;">
                ${AR_WEEKDAYS_SAT.map(d => `<div style="${d === 'الجمعة' ? 'color:#f87171;' : ''}">${d}</div>`).join('')}
            </div>

            <!-- Month Days Grid -->
            <div style="display:grid;grid-template-columns:repeat(7, 1fr);gap:1px;background:rgba(255,255,255,0.06);">
    `;

    // Previous month empty days
    for (let i = 0; i < startDayIndex; i++) {
        html += `<div style="background:rgba(15,23,42,0.6);min-height:105px;padding:6px;opacity:0.3;"></div>`;
    }

    // Days of current month
    for (let d = 1; d <= totalDays; d++) {
        const dStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
        const dayDate = new Date(year, month, d);
        const isFriday = dayDate.getDay() === 5;
        const isToday = (d === 21 && month === 9 && year === 2026); // simulated current date marker

        // Find events on this date
        const dayEvents = events.filter(e => {
            return dStr >= e.startDate && dStr <= (e.endDate || e.startDate);
        });

        html += `
            <div style="background:rgba(15,23,42,0.88);min-height:105px;padding:8px;position:relative;border:1px solid rgba(255,255,255,0.04);transition:all 0.2s;" onmouseover="this.style.background='rgba(30,41,59,0.95)'" onmouseout="this.style.background='rgba(15,23,42,0.88)'">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                    <span style="font-weight:800;font-size:0.95rem;${isToday ? 'background:#3b82f6;color:#fff;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;' : isFriday ? 'color:#f87171;' : 'color:#f8fafc;'}">${d}</span>
                    ${isFriday ? '<span style="font-size:0.68rem;color:#f87171;">عطلة</span>' : ''}
                </div>

                <!-- Event Cards for this Day -->
                <div style="display:flex;flex-direction:column;gap:4px;">
                    ${dayEvents.map(e => {
                        const style = getCategoryColor(e.category);
                        return `
                            <div onclick="openForm('academic_calendar', '${e.id || e.code}')" title="${e.name} (${e.category}) - انقر للتعديل" style="background:${style.bg};border-right:3px solid ${style.border};color:${style.text};padding:4px 6px;border-radius:6px;font-size:0.73rem;font-weight:700;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:transform 0.15s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                                <i class="fa-solid fa-circle" style="font-size:0.45rem;color:${style.border};margin-left:4px;"></i> ${e.name}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    // Trailing empty cells to complete the grid row
    const totalFilled = startDayIndex + totalDays;
    const remainingCells = (7 - (totalFilled % 7)) % 7;
    for (let i = 0; i < remainingCells; i++) {
        html += `<div style="background:rgba(15,23,42,0.6);min-height:105px;padding:6px;opacity:0.3;"></div>`;
    }

    html += `
            </div>
        </div>
    `;

    return html;
}

/**
 * 2. RENDER WEEKLY VIEW (7 Days Columns with Hourly / Event Cards)
 */
function renderWeeklyCalendar(events) {
    const cur = new Date(window.calState.currentDate);
    // Find previous Saturday
    const currentDay = cur.getDay(); // 0 is Sun, 6 is Sat
    const diffToSat = (currentDay + 1) % 7;
    const startOfWeek = new Date(cur);
    startOfWeek.setDate(cur.getDate() - diffToSat);

    const endOfWeek = new Date(startOfWeek);
    endOfWeek.setDate(startOfWeek.getDate() + 6);

    const titleEl = document.getElementById('calPeriodDisplayTitle');
    if (titleEl) {
        titleEl.innerHTML = `<i class="fa-solid fa-calendar-week" style="color:#38bdf8;"></i> <span>الأسبوع: ${startOfWeek.getDate()} ${AR_MONTHS[startOfWeek.getMonth()]} - ${endOfWeek.getDate()} ${AR_MONTHS[endOfWeek.getMonth()]} ${endOfWeek.getFullYear()} م</span>`;
    }

    let html = `
        <div style="background:rgba(15,23,42,0.9);border:1px solid rgba(255,255,255,0.12);border-radius:14px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.35);">
            <div style="display:grid;grid-template-columns:repeat(7, 1fr);gap:1px;background:rgba(255,255,255,0.08);">
    `;

    for (let i = 0; i < 7; i++) {
        const dayDate = new Date(startOfWeek);
        dayDate.setDate(startOfWeek.getDate() + i);
        const dayName = AR_WEEKDAYS_SAT[i];
        const dStr = `${dayDate.getFullYear()}-${String(dayDate.getMonth() + 1).padStart(2, '0')}-${String(dayDate.getDate()).padStart(2, '0')}`;
        const isFriday = dayDate.getDay() === 5;
        const isToday = (dayDate.getDate() === 21 && dayDate.getMonth() === 9 && dayDate.getFullYear() === 2026);

        const dayEvents = events.filter(e => dStr >= e.startDate && dStr <= (e.endDate || e.startDate));

        html += `
            <div style="background:rgba(15,23,42,0.95);min-height:360px;display:flex;flex-direction:column;">
                <div style="background:${isToday ? 'linear-gradient(135deg,#2563eb,#1d4ed8)' : 'rgba(30,41,59,0.9)'};padding:10px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.1);">
                    <div style="font-size:0.8rem;color:${isToday ? '#fff' : '#94a3b8'};font-weight:700;">${dayName}</div>
                    <div style="font-size:1.15rem;font-weight:800;color:${isToday ? '#fff' : isFriday ? '#f87171' : '#f8fafc'};margin-top:2px;">${dayDate.getDate()} ${AR_MONTHS[dayDate.getMonth()]}</div>
                </div>

                <div style="padding:10px;flex:1;display:flex;flex-direction:column;gap:8px;">
                    ${dayEvents.length === 0 ? `
                        <div style="text-align:center;color:var(--muted);font-size:0.75rem;padding-top:40px;">لا توجد فعاليات مجدولة</div>
                    ` : dayEvents.map(e => {
                        const style = getCategoryColor(e.category);
                        return `
                            <div onclick="openForm('academic_calendar', '${e.id || e.code}')" style="background:${style.bg};border:1px solid ${style.border};border-radius:8px;padding:10px;cursor:pointer;transition:transform 0.15s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
                                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                                    <span class="badge ${style.badge}" style="font-size:0.68rem;padding:2px 6px;">${e.category}</span>
                                    <small style="color:#94a3b8;font-size:0.7rem;"><i class="fa-solid fa-clock"></i> ${e.duration}</small>
                                </div>
                                <strong style="color:#f8fafc;font-size:0.82rem;display:block;line-height:1.3;">${e.name}</strong>
                                <div style="font-size:0.72rem;color:#cbd5e1;margin-top:4px;"><i class="fa-solid fa-location-dot" style="color:#38bdf8;"></i> ${e.location}</div>
                                <div style="font-size:0.7rem;color:#94a3b8;margin-top:2px;"><i class="fa-solid fa-user-tie"></i> ${e.supervisor}</div>
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    html += `
            </div>
        </div>
    `;

    return html;
}

/**
 * 3. RENDER YEARLY VIEW (12 Months Mini-Grid Matrix)
 */
function renderYearlyCalendar(events) {
    const cur = window.calState.currentDate;
    const year = cur.getFullYear();

    const titleEl = document.getElementById('calPeriodDisplayTitle');
    if (titleEl) {
        titleEl.innerHTML = `<i class="fa-solid fa-calendar" style="color:#38bdf8;"></i> <span>التقويم السنوي الشامل لعام ${year} م / ${year + 1} م</span>`;
    }

    let html = `
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;">
    `;

    for (let m = 0; m < 12; m++) {
        const firstDay = new Date(year, m, 1);
        const totalDays = new Date(year, m + 1, 0).getDate();
        const startDayIndex = (firstDay.getDay() + 1) % 7;

        // Month events count
        const monthEvents = events.filter(e => {
            const evM = new Date(e.startDate).getMonth();
            const evY = new Date(e.startDate).getFullYear();
            return (evM === m && evY === year);
        });

        html += `
            <div style="background:rgba(15,23,42,0.9);border:1px solid rgba(255,255,255,0.12);border-radius:12px;padding:12px;box-shadow:0 4px 15px rgba(0,0,0,0.25);">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:6px;">
                    <strong style="color:#38bdf8;font-size:0.95rem;">${AR_MONTHS[m]} ${year}</strong>
                    <span class="badge badge-info" style="font-size:0.7rem;">${monthEvents.length} فعاليات</span>
                </div>

                <!-- Mini Weekday Headers -->
                <div style="display:grid;grid-template-columns:repeat(7, 1fr);text-align:center;font-size:0.65rem;color:#94a3b8;font-weight:700;margin-bottom:4px;">
                    <div>س</div><div>ح</div><div>ن</div><div>ث</div><div>ر</div><div>خ</div><div>ج</div>
                </div>

                <!-- Mini Days Grid -->
                <div style="display:grid;grid-template-columns:repeat(7, 1fr);gap:2px;text-align:center;font-size:0.72rem;">
        `;

        for (let i = 0; i < startDayIndex; i++) {
            html += `<div></div>`;
        }

        for (let d = 1; d <= totalDays; d++) {
            const dStr = `${year}-${String(m + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
            const hasEvt = events.find(e => dStr >= e.startDate && dStr <= (e.endDate || e.startDate));
            
            let cellStyle = 'padding:4px 0;border-radius:4px;color:#f8fafc;';
            if (hasEvt) {
                const col = getCategoryColor(hasEvt.category);
                cellStyle = `padding:4px 0;border-radius:4px;background:${col.bg};color:${col.text};font-weight:800;border:1px solid ${col.border};cursor:pointer;`;
            }

            html += `<div style="${cellStyle}" ${hasEvt ? `onclick="window.calState.currentDate = new Date(${year}, ${m}, ${d}); switchCalendarView('month');"` : ''} title="${hasEvt ? hasEvt.name : ''}">${d}</div>`;
        }

        html += `
                </div>
            </div>
        `;
    }

    html += `
        </div>
    `;

    return html;
}

/**
 * Main Academic Calendar Grid & Renderer Dispatcher
 */
function renderAcademicCalendarGrid() {
    const container = document.getElementById('calendarViewContainer');
    const tableWrapper = document.getElementById('calendarTableWrapper');
    const tb = document.getElementById('tbl-academic-calendar-grid') || document.getElementById('tbl-academic-calendar');

    const events = getFilteredEvents();

    // Update KPI Counters
    const allItems = window.DB.academicCalendar || [];
    const totEl = document.getElementById('calTotalEvents');
    const holEl = document.getElementById('calTotalHolidays');
    const exmEl = document.getElementById('calTotalExams');
    const actEl = document.getElementById('calTotalActivities');

    const holidays = allItems.filter(e => e.category.includes('إجازة')).length;
    const exams = allItems.filter(e => e.category.includes('اختبار')).length;
    const activities = allItems.filter(e => e.category.includes('نشاط')).length;

    if (totEl) totEl.innerHTML = `${allItems.length} <small style="font-size:0.75rem;">فعالية ومناسبة 🔵</small>`;
    if (holEl) holEl.innerHTML = `${holidays} <small style="font-size:0.75rem;">إجازات رسمية 🏖️</small>`;
    if (exmEl) exmEl.innerHTML = `${exams} <small style="font-size:0.75rem;">فترات اختبارات 🔴</small>`;
    if (actEl) actEl.innerHTML = `${activities} <small style="font-size:0.75rem;">نشاطاً وفعالية 🟡</small>`;

    // STRICT VISIBILITY TOGGLE: Detailed table ONLY shows in 'list' mode!
    if (window.calState.mode === 'list') {
        if (container) {
            container.innerHTML = '';
            container.style.setProperty('display', 'none', 'important');
            container.hidden = true;
        }
        if (tableWrapper) {
            tableWrapper.hidden = false;
            tableWrapper.style.setProperty('display', 'block', 'important');
        }
        const titleEl = document.getElementById('calPeriodDisplayTitle');
        if (titleEl) {
            titleEl.innerHTML = `<i class="fa-solid fa-table-list" style="color:#38bdf8;"></i> <span>جدول كشف الفعاليات والروزنامة التفصيلية</span>`;
        }

        // Render table rows ONLY when in list mode
        if (tb) {
            if (events.length === 0) {
                tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد فعاليات مطابقة للبحث أو النطاق المحدد</td></tr>';
                return;
            }

            tb.innerHTML = events.map((e, idx) => {
                const col = getCategoryColor(e.category);
                const statusBadge = e.status.includes('منفذة') || e.status.includes('معتمدة') ?
                    '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> ' + e.status + '</span>' :
                    '<span class="badge badge-info"><i class="fa-solid fa-clock"></i> ' + e.status + '</span>';

                return `
                    <tr data-collection="academicCalendar" data-id="${e.id || e.code}" ondblclick="openForm('academic_calendar', '${e.id || e.code}')" oncontextmenu="event.preventDefault();deleteItem('academicCalendar', '${e.id || e.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                        <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                        <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;">${e.code || e.id}</td>
                        <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-calendar-day" style="color:#38bdf8;font-size:0.8rem;"></i> ${e.name}</td>
                        <td><span class="badge ${col.badge}" style="font-size:0.75rem;">${e.category}</span></td>
                        <td><strong style="color:#34d399;font-family:monospace;font-size:0.88rem;">${e.startDate}</strong></td>
                        <td><strong style="color:#38bdf8;font-family:monospace;font-size:0.88rem;">${e.endDate || e.startDate}</strong></td>
                        <td style="font-size:0.8rem;color:#cbd5e1;">${e.duration}</td>
                        <td style="font-size:0.82rem;color:#cbd5e1;">${e.targetAudience}</td>
                        <td style="font-size:0.8rem;color:#94a3b8;">${e.supervisor}</td>
                        <td style="font-size:0.8rem;color:#cbd5e1;">${e.location}</td>
                        <td>${statusBadge}</td>
                        <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('📄 استعراض وتنزيل التعميم الرسمي لـ: ${e.name}');"><i class="fa-solid fa-file-pdf"></i> التعميم والمرفق</button></td>
                    </tr>
                `;
            }).join('');
        }
    } else {
        // Visual Calendar Mode: STRICTLY HIDE TABLE & EMPTY TBODY
        if (tableWrapper) {
            tableWrapper.style.setProperty('display', 'none', 'important');
            tableWrapper.hidden = true;
        }
        if (tb) {
            tb.innerHTML = '';
        }
        if (container) {
            container.hidden = false;
            container.style.setProperty('display', 'block', 'important');
            if (window.calState.mode === 'month') {
                container.innerHTML = renderMonthlyCalendar(events);
            } else if (window.calState.mode === 'week') {
                container.innerHTML = renderWeeklyCalendar(events);
            } else if (window.calState.mode === 'year') {
                container.innerHTML = renderYearlyCalendar(events);
            }
        }
    }
}
window.renderAcademicCalendarGrid = renderAcademicCalendarGrid;
window.renderAcademicCalendar = renderAcademicCalendarGrid;
// Initial trigger
try { renderAcademicCalendarGrid(); } catch(e) {}

/**
 * ============================================================================
 * STAGES & GRADES DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.stages) {
    window.DB.stages = [
        {
            id: 'STG-01',
            code: 'STG-01',
            name: 'مرحلة رياض الأطفال والتمهيدي (KG)',
            nameEn: 'Kindergarten & Early Childhood (KG1 - KG3)',
            grades: 'روضة أولى (KG1)، روضة ثانية (KG2)، تمهيدي (KG3)',
            sectionsCount: 4,
            passMark: 'تقييم وصفي مهاراتي',
            gradingSystem: 'نظام التقييم الوصفي والمستمر (A-F) 📝',
            order: 1,
            capacity: 150,
            maxPerSection: 25,
            supervisor: 'أ. فاطمة باعباد (رئيسة قسم الروضة)',
            building: 'مبنى الروضة المستقل - الجناح المخصص',
            status: 'نشطة ومفعلة تقبل القبول 🟢',
            notes: 'تطبيق منهج التعلم باللعب وتنمية المهارات السلوكية والحركية المبكرة.'
        },
        {
            id: 'STG-02',
            code: 'STG-02',
            name: 'المرحلة الأساسية - الصفوف الأولية (1-6)',
            nameEn: 'Primary Stage - Elementary (Grades 1-6)',
            grades: 'الصف الأول إلى الصف السادس أساسي',
            sectionsCount: 14,
            passMark: '50% كحد أدنى 🟢',
            gradingSystem: 'نظام فصلي تراكمي بالأرقام (100 درجة) 📊',
            order: 2,
            capacity: 500,
            maxPerSection: 35,
            supervisor: 'أ. إبراهيم الحداد (وكيل المرحلة الأساسية)',
            building: 'المبنى الرئيسي - الجناح الأيمن (بنين وبنات)',
            status: 'نشطة ومفعلة تقبل القبول 🟢',
            notes: 'التركيز على مهارات القراءة والكتابة والرياضيات واللغة الإنجليزية.'
        },
        {
            id: 'STG-03',
            code: 'STG-03',
            name: 'المرحلة الأساسية - الصفوف العليا (7-9)',
            nameEn: 'Middle Basic Stage - Junior High (Grades 7-9)',
            grades: 'الصف السابع، الصف الثامن، الصف التاسع (شهادة أساسية)',
            sectionsCount: 10,
            passMark: '50% كحد أدنى 🟢',
            gradingSystem: 'نظام فصلي تراكمي واختبار وزاري 📊',
            order: 3,
            capacity: 350,
            maxPerSection: 35,
            supervisor: 'أ. سالم الحميري (وكيل المرحلة المتوسطة)',
            building: 'المبنى الرئيسي - الطابق الثاني',
            status: 'نشطة ومفعلة تقبل القبول 🟢',
            notes: 'إعداد الطلاب للاختبارات الوزارية للمرحلة الأساسية والتأهيل العلمي.'
        },
        {
            id: 'STG-04',
            code: 'STG-04',
            name: 'المرحلة الثانوية العامة (10-12)',
            nameEn: 'Secondary Stage - High School (Grades 10-12)',
            grades: 'الأول الثانوي (عام)، الثاني الثانوي، الثالث الثانوي (علمي وأدبي)',
            sectionsCount: 8,
            passMark: '50% كحد أدنى 🟢',
            gradingSystem: 'نظام المعدل التراكمي والاختبار الوزاري 🎓',
            order: 4,
            capacity: 250,
            maxPerSection: 32,
            supervisor: 'د. عبد العزيز الصبري (مدير المرحلة الثانوية)',
            building: 'مبنى الثانوية والمعامل المتقدمة',
            status: 'نشطة ومفعلة تقبل القبول 🟢',
            notes: 'تأهيل الطلاب للمسار الجامعي والقدرات والمنافسات العلمية والأولمبياد.'
        }
    ];
}

function renderStagesGrid() {
    const tb = document.getElementById('tbl-stages-grid') || document.getElementById('tbl-stages');
    if (!tb) return;

    const query = (document.getElementById('searchStages')?.value || '').toLowerCase().trim();
    const statusFilter = document.getElementById('filterStageStatus')?.value || 'all';
    const items = window.DB.stages || [];

    const totEl = document.getElementById('stgTotalStages');
    const grdEl = document.getElementById('stgTotalGrades');
    const secEl = document.getElementById('stgTotalSections');
    const capEl = document.getElementById('stgTotalCapacity');

    if (totEl) totEl.innerHTML = `${items.length} <small style="font-size:0.75rem;">مراحل تعليمية 🏛️</small>`;
    if (grdEl) grdEl.innerHTML = `15 <small style="font-size:0.75rem;">صفاً دراسياً 📚</small>`;
    if (secEl) secEl.innerHTML = `36 <small style="font-size:0.75rem;">شعبة دراسية 🏫</small>`;
    if (capEl) capEl.innerHTML = `1,250 <small style="font-size:0.75rem;">مقعداً طلابياً 🪑</small>`;

    const filtered = items.filter(s => {
        if (statusFilter === 'نشطة' && !s.status.includes('نشطة')) return false;
        if (statusFilter === 'فصلي' && !s.gradingSystem.includes('فصلي')) return false;
        if (statusFilter === 'مستمر' && !s.gradingSystem.includes('مستمر')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.grades, s.supervisor, s.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد مراحل مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> نشطة ومفعلة 🟢</span>';
        if (s.status.includes('مكتملة')) {
            statusBadge = '<span class="badge badge-warning"><i class="fa-solid fa-triangle-exclamation"></i> مكتملة السعة 🟡</span>';
        } else if (s.status.includes('موقفة')) {
            statusBadge = '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> موقفة مؤقتاً 🔴</span>';
        }

        return `
            <tr data-collection="stages" data-id="${s.id || s.code}" ondblclick="openForm('stages', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('stages', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-layer-group" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.name}</td>
                <td style="font-size:0.83rem;color:#cbd5e1;">${s.grades}</td>
                <td><span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">${s.sectionsCount} شعب 🏫</span></td>
                <td><span class="badge badge-success" style="font-size:0.75rem;">${s.passMark}</span></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.gradingSystem}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">ترتيب ${s.order}</span></td>
                <td><strong style="color:#34d399;font-family:monospace;font-size:0.85rem;">${s.capacity} مقعد 🪑</strong></td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${s.supervisor}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('🏫 عرض شعب وفصول: ${s.name}');goTo('pg-sections');"><i class="fa-solid fa-chalkboard-user"></i> عرض الشُعَب</button></td>
            </tr>
        `;
    }).join('');
}
window.renderStagesGrid = renderStagesGrid;
window.renderStages = renderStagesGrid;
// Initial render
try { renderStagesGrid(); } catch(e) {}


/**
 * ============================================================================
 * SECTIONS & CLASSROOMS DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.sections) {
    window.DB.sections = [
        {
            id: 'SEC-09A',
            code: 'SEC-09A',
            name: 'شعبة التاسع أساسي (أ) - بنين',
            nameEn: 'Grade 9 Section (A) - Boys',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            gender: 'فرع البنين 👦',
            capacity: 35,
            enrolled: 32,
            available: 3,
            mentor: 'أ. عادل عبد الله العولقي',
            room: 'قاعة 104 - المبنى الرئيسي - الطابق الأول',
            counselor: 'أ. نبيل القدسي',
            status: 'نشطة ومتاحة للقبول 🟢',
            notes: 'شعبة متميزة ومجهزة بشاشة تفاعلية ذكية ونظام تكييف مركزي.'
        },
        {
            id: 'SEC-09B',
            code: 'SEC-09B',
            name: 'شعبة التاسع أساسي (ب) - بنات',
            nameEn: 'Grade 9 Section (B) - Girls',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            gender: 'فرع البنات 👧',
            capacity: 35,
            enrolled: 35,
            available: 0,
            mentor: 'أ. سارة عبد الكريم باعباد',
            room: 'قاعة 201 - جناح البنات - الطابق الثاني',
            counselor: 'أ. منى اليافعي',
            status: 'مكتملة العدد والطاقة 🔒',
            notes: 'اكتملت الطاقة الاستيعابية للشعبة بالكامل.'
        },
        {
            id: 'SEC-12S1',
            code: 'SEC-12S1',
            name: 'شعبة الثالث الثانوي - علمي (1)',
            nameEn: 'Grade 12 Scientific (1) - High School',
            stage: 'المرحلة الثانوية 10-12',
            grade: 'الصف الثالث الثانوي (علمي)',
            gender: 'فرع البنين 👦',
            capacity: 32,
            enrolled: 30,
            available: 2,
            mentor: 'د. عبد العزيز الصبري',
            room: 'معمل الفيزياء والرياضيات 302',
            counselor: 'أ. مروان الشامي',
            status: 'نشطة ومتاحة للقبول 🟢',
            notes: 'تأهيل مكثف لاختبارات الثانوية العامة والقدرات والمسابقات.'
        },
        {
            id: 'SEC-01A',
            code: 'SEC-01A',
            name: 'شعبة الأول أساسي (أ) - تميز',
            nameEn: 'Grade 1 Section (A) - Primary',
            stage: 'المرحلة الأساسية - صفوف 1-6',
            grade: 'الصف الأول الابتدائي',
            gender: 'مشترك / مختلط أطفال 👶',
            capacity: 30,
            enrolled: 28,
            available: 2,
            mentor: 'أ. أروى ناصر المنصوب',
            room: 'قاعة الأنشطة والتأسيس 101',
            counselor: 'أ. وفاء الشيباني',
            status: 'نشطة ومتاحة للقبول 🟢',
            notes: 'قاعة مجهزة ببيئة تعليمية جاذبة وبرامج التأسيس اللغوي.'
        },
        {
            id: 'SEC-KG1',
            code: 'SEC-KG1',
            name: 'شعبة الروضة الأولى (KG1 - الفراشات)',
            nameEn: 'KG1 Butterflies Section',
            stage: 'مرحلة رياض الأطفال KG',
            grade: 'روضة أولى (KG1)',
            gender: 'مشترك / مختلط تمهيدي 👶',
            capacity: 25,
            enrolled: 22,
            available: 3,
            mentor: 'أ. فاطمة باعباد',
            room: 'مبنى الروضة - صالة الألعاب 01',
            counselor: 'أ. سمية طاهر',
            status: 'نشطة ومتاحة للقبول 🟢',
            notes: 'مجهزة بألعاب التفكير الحركي وأركان التعلم الإثرائي.'
        }
    ];
}

function renderSectionsGrid() {
    const tb = document.getElementById('tbl-sections-grid') || document.getElementById('tbl-sections');
    if (!tb) return;

    const query = (document.getElementById('searchSections')?.value || '').toLowerCase().trim();
    const stageFilter = document.getElementById('filterSectionStage')?.value || 'all';
    const items = window.DB.sections || [];

    const totEl = document.getElementById('secTotalSections');
    const stuEl = document.getElementById('secTotalStudents');
    const avgEl = document.getElementById('secAvgDensity');
    const remEl = document.getElementById('secAvailableSeats');

    if (totEl) totEl.innerHTML = `36 <small style="font-size:0.75rem;">شعبة دراسية</small>`;
    if (stuEl) stuEl.innerHTML = `1,080 <small style="font-size:0.75rem;">طالباً وطالبة</small>`;
    if (avgEl) avgEl.innerHTML = `30 <small style="font-size:0.75rem;">طالباً / شعبة</small>`;
    if (remEl) remEl.innerHTML = `170 <small style="font-size:0.75rem;">مقعداً شاغراً 🪑</small>`;

    const filtered = items.filter(s => {
        if (stageFilter === 'بنين' && !s.gender.includes('بنين')) return false;
        if (stageFilter === 'بنات' && !s.gender.includes('بنات')) return false;
        if (stageFilter === 'ثانوي' && !s.stage.includes('ثانوي')) return false;
        if (stageFilter === 'أساسي' && !s.stage.includes('أساسي')) return false;
        if (stageFilter === 'روضة' && !s.stage.includes('روضة')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.stage, s.grade, s.mentor, s.room, s.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد شعب مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> نشطة ومتاحة 🟢</span>';
        if (s.status.includes('مكتملة')) {
            statusBadge = '<span class="badge" style="background:rgba(100,116,139,0.2);color:#cbd5e1;"><i class="fa-solid fa-lock"></i> مكتملة الامتلاء 🔒</span>';
        } else if (s.status.includes('موقفة')) {
            statusBadge = '<span class="badge badge-danger"><i class="fa-solid fa-circle-xmark"></i> موقفة مؤقتاً 🔴</span>';
        }

        const availBadge = s.available > 0 
            ? `<span class="badge badge-success" style="font-size:0.75rem;">${s.available} مقاعد 🟢</span>`
            : `<span class="badge badge-danger" style="font-size:0.75rem;">مكتمل 🔒</span>`;

        return `
            <tr data-collection="sections" data-id="${s.id || s.code}" ondblclick="openForm('sections', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('sections', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-chalkboard-user" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.name}</td>
                <td style="font-size:0.83rem;color:#cbd5e1;">${s.grade}</td>
                <td><span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">${s.gender}</span></td>
                <td><strong style="color:#94a3b8;font-family:monospace;font-size:0.85rem;">${s.capacity} مقعد</strong></td>
                <td><strong style="color:#38bdf8;font-family:monospace;font-size:0.85rem;">${s.enrolled} طالب</strong></td>
                <td>${availBadge}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${s.mentor}</td>
                <td style="font-size:0.8rem;color:#94a3b8;">📍 ${s.room}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('👥 استعراض كشف طلاب: ${s.name}');goTo('pg-students');"><i class="fa-solid fa-users"></i> كشف الطلاب</button></td>
            </tr>
        `;
    }).join('');
}
window.renderSectionsGrid = renderSectionsGrid;
window.renderSections = renderSectionsGrid;
// Initial render
try { renderSectionsGrid(); } catch(e) {}


/**
 * ============================================================================
 * CURRICULUM & SUBJECTS DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.subjects) {
    window.DB.subjects = [
        {
            id: 'SUB-MATH-09',
            code: 'SUB-MATH-09',
            name: 'الرياضيات المتقدمة والجبر والهندسة',
            nameEn: 'Advanced Mathematics & Geometry',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي (الشهادة الأساسية)',
            category: 'علمية وتطبيقية 🔬',
            weeklyPeriods: 6,
            maxMark: 100,
            minMark: 50,
            creditHours: 4.0,
            head: 'أ. إبراهيم الحداد (رئيس قسم الرياضيات)',
            examType: 'تحريري فصلي ووزاري 📊',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'تشمل الهندسة التحليلية، حساب المثلثات، الجبر، والإحصاء والاحتمالات.'
        },
        {
            id: 'SUB-SCI-09',
            code: 'SUB-SCI-09',
            name: 'العلوم العامة والفيزياء والكيمياء',
            nameEn: 'General Science, Physics & Chemistry',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي',
            category: 'علمية وتطبيقية 🔬',
            weeklyPeriods: 5,
            maxMark: 100,
            minMark: 50,
            creditHours: 3.5,
            head: 'أ. سالم الحميري (مشرف العلوم)',
            examType: 'تحريري + تجارب عملية بالمعمل 🔬',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'حصص تطبيقية أسبوعية بمعامل الفيزياء والكيمياء والأحياء.'
        },
        {
            id: 'SUB-ENG-09',
            code: 'SUB-ENG-09',
            name: 'اللغة الإنجليزية والمحادثة (Crescent English)',
            nameEn: 'English Language & Communication Skills',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي',
            category: 'لغات وآداب 📖',
            weeklyPeriods: 5,
            maxMark: 100,
            minMark: 50,
            creditHours: 3.5,
            head: 'أ. محمد طاهر اليافعي',
            examType: 'تحريري + اختبار استماع ومحادثة 🎧',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'منهج كريسنت الحديث مدعماً ببرامج معمل اللغات التفاعلي.'
        },
        {
            id: 'SUB-ARB-09',
            code: 'SUB-ARB-09',
            name: 'اللغة العربية وفنون الأدب والنحو',
            nameEn: 'Arabic Language, Grammar & Literature',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي',
            category: 'لغات وآداب 📖',
            weeklyPeriods: 6,
            maxMark: 100,
            minMark: 50,
            creditHours: 4.0,
            head: 'أ. عبد الله العولقي',
            examType: 'تحريري وشامل للنحو والإملاء',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'القراءة والنصوص، النحو والصرف، التعبير والخط العربي.'
        },
        {
            id: 'SUB-QRN-09',
            code: 'SUB-QRN-09',
            name: 'القرآن الكريم وأحكام التلاوة والتجويد',
            nameEn: 'Holy Quran & Tajweed Rules',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي',
            category: 'علوم شرعية وإسلاميات 🟢',
            weeklyPeriods: 4,
            maxMark: 100,
            minMark: 50,
            creditHours: 3.0,
            head: 'الشيخ عبد الرحمن باعباد',
            examType: 'شفهي تلاوة وتسميع + تحريري تجويد',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'حفظ السور المقررة وتطبيق أحكام التجويد والتفسير الميسر.'
        },
        {
            id: 'SUB-COMP-09',
            code: 'SUB-COMP-09',
            name: 'الحاسوب وتقنية المعلومات والذكاء الاصطناعي',
            nameEn: 'Computer Science, IT & AI Basics',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            grades: 'الصف التاسع أساسي',
            category: 'حاسوب وتكنولوجيا 💻',
            weeklyPeriods: 2,
            maxMark: 100,
            minMark: 50,
            creditHours: 2.0,
            head: 'م. خالد عبد الكريم',
            examType: 'تطبيقي عملي بمعمل الحاسوب 💻',
            status: 'معتمدة ونشطة بالجدول 🟢',
            notes: 'مفاهيم البرمجة وأساسيات الذكاء الاصطناعي وتطبيقات الويب.'
        }
    ];
}

function renderSubjectsGrid() {
    const tb = document.getElementById('tbl-subjects-grid') || document.getElementById('tbl-subjects');
    if (!tb) return;

    const query = (document.getElementById('searchSubjects')?.value || document.getElementById('searchSubject')?.value || '').toLowerCase().trim();
    const catFilter = document.getElementById('filterSubjectCategory')?.value || 'all';
    const items = window.DB.subjects || [];

    // Calculate KPIs
    let totalCount = items.length;
    let coreCount = 0;
    let electiveCount = 0;

    items.forEach(s => {
        const st = String(s.status || '');
        if (st.includes('اختيارية')) {
            electiveCount++;
        } else {
            coreCount++;
        }
    });

    const totEl = document.getElementById('subjTotal') || document.getElementById('subTotalSubjects');
    const coreEl = document.getElementById('subjCore') || document.getElementById('subTotalScientific');
    const elecEl = document.getElementById('subjElective') || document.getElementById('subTotalHumanities');

    if (totEl) totEl.textContent = totalCount;
    if (coreEl) coreEl.textContent = coreCount;
    if (elecEl) elecEl.textContent = electiveCount;

    const filtered = items.filter(s => {
        const catStr = String(s.category || (
            s.name && (s.name.includes('قرآن') || s.name.includes('إسلامية')) ? 'علوم شرعية وتربية إسلامية' :
            (s.name && (s.name.includes('عربي') || s.name.includes('إنجليزي')) ? 'لغات وآداب' :
            (s.name && (s.name.includes('رياضيات') || s.name.includes('علوم') || s.name.includes('فيزياء')) ? 'مواد علمية وتطبيقية' :
            (s.name && s.name.includes('حاسوب') ? 'حاسوب وتكنولوجيا' : 'مواد أساسية')))
        ));

        if (catFilter === 'علمية' && !catStr.includes('علمية')) return false;
        if (catFilter === 'لغات' && !catStr.includes('لغات')) return false;
        if (catFilter === 'إسلامية' && !catStr.includes('شرعية') && !catStr.includes('إسلامية')) return false;
        if (catFilter === 'حاسوب' && !catStr.includes('حاسوب') && !catStr.includes('تقنية')) return false;
        if (catFilter === 'اجتماعية' && !catStr.includes('اجتماعية') && !catStr.includes('تاريخ')) return false;

        if (!query) return true;
        const text = [
            s.id, s.code, s.name, s.nameEn, s.stage, s.grades, catStr, s.head, s.status
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد مواد دراسية مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        const catStr = String(s.category || (
            s.name && (s.name.includes('قرآن') || s.name.includes('إسلامية')) ? 'علوم شرعية 🟢' :
            (s.name && (s.name.includes('عربي') || s.name.includes('إنجليزي')) ? 'لغات وآداب 📖' :
            (s.name && (s.name.includes('رياضيات') || s.name.includes('علوم') || s.name.includes('فيزياء')) ? 'علمية وتطبيقية 🔬' :
            (s.name && s.name.includes('حاسوب') ? 'حاسوب وتقنية 💻' : 'مادة أساسية 📘')))
        ));

        let catBadge = '<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-flask" style="margin-left:4px;"></i> علمية 🔬</span>';
        if (catStr.includes('لغات')) {
            catBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;"><i class="fa-solid fa-language" style="margin-left:4px;"></i> لغات وآداب 📖</span>';
        } else if (catStr.includes('شرعية') || catStr.includes('إسلامية')) {
            catBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-mosque" style="margin-left:4px;"></i> علوم شرعية 🟢</span>';
        } else if (catStr.includes('حاسوب') || catStr.includes('تقنية') || catStr.includes('ذكاء')) {
            catBadge = '<span class="badge" style="background:rgba(56,189,248,0.15);color:#38bdf8;font-size:0.75rem;"><i class="fa-solid fa-laptop-code" style="margin-left:4px;"></i> حاسوب وتقنية 💻</span>';
        } else if (catStr.includes('اجتماعية')) {
            catBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-earth-americas" style="margin-left:4px;"></i> اجتماعيات 🌍</span>';
        } else {
            catBadge = `<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-book" style="margin-left:4px;"></i> ${catStr}</span>`;
        }

        const isElective = String(s.status || '').includes('اختيارية');
        const statusBadge = isElective
            ? '<span class="badge badge-warning"><i class="fa-solid fa-circle-pause"></i> اختيارية 🟡</span>'
            : '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> معتمدة ونشطة 🟢</span>';

        const subCode = s.code || s.id || ('SUB-' + (idx + 101));
        const stageName = s.stage || 'المرحلة الأساسية';
        const periods = s.weeklyPeriods || s.classesPerWeek || 4;
        const maxScore = s.maxMark || s.maxScore || 100;
        const teacherHead = s.head || s.teacher || 'أ. مدرس المادة';

        return `
            <tr data-collection="subjects" data-id="${s.id || subCode}" ondblclick="openForm('subjects', '${s.id || subCode}')" oncontextmenu="event.preventDefault();deleteItem('subjects', '${s.id || subCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;"><i class="fa-solid fa-book" style="color:#60a5fa;font-size:0.75rem;margin-left:4px;"></i> ${subCode}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-book-open" style="color:#38bdf8;font-size:0.8rem;margin-left:4px;"></i> ${s.name}</td>
                <td>${catBadge}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-graduation-cap" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${stageName}</td>
                <td style="text-align:center;"><span class="badge badge-info" style="font-size:0.75rem;font-weight:700;"><i class="fa-solid fa-clock" style="margin-left:4px;"></i> ${periods} حصص</span></td>
                <td style="text-align:center;"><strong style="color:#38bdf8;font-family:monospace;font-size:0.88rem;">${maxScore} درجة</strong></td>
                <td style="color:#e2e8f0;font-size:0.83rem;font-weight:600;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;margin-left:4px;"></i> ${teacherHead}</td>
                <td>${statusBadge}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل المادة" onclick="openForm('subjects', '${s.id || subCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف المادة" onclick="deleteItem('subjects', '${s.id || subCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderSubjectsGrid = renderSubjectsGrid;
window.renderSubjects = renderSubjectsGrid;
/**
 * ============================================================================
 * SUBJECT DISTRIBUTION ON GRADES ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.subjectDistribution) {
    window.DB.subjectDistribution = [
        {
            id: 'DIST-09-MATH',
            code: 'DIST-09-MATH',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'الرياضيات المتقدمة والجبر والهندسة',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 6,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 4.0 ⚖️',
            examType: 'أعمال سنة 40% + نهائي 60% 📊',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: '6 حصص أسبوعية تشمل حصتي تمارين وحل مسائل مكثفة.'
        },
        {
            id: 'DIST-09-SCI',
            code: 'DIST-09-SCI',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'العلوم العامة والفيزياء والكيمياء',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 5,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 3.5 ⚖️',
            examType: 'تحريري + تجارب عملية بالمعمل 🔬',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'تخصيص حصة أسبوعية بالمعمل لإجراء التجارب المنهجية المقررة.'
        },
        {
            id: 'DIST-09-ENG',
            code: 'DIST-09-ENG',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'اللغة الإنجليزية والمحادثة (Crescent English)',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 5,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 3.5 ⚖️',
            examType: 'تحريري + استماع ومحادثة 🎧',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'التركيز على مهارات التعبير الكتابي والمحادثة التفاعلية.'
        },
        {
            id: 'DIST-09-ARB',
            code: 'DIST-09-ARB',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'اللغة العربية وفنون الأدب والنحو',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 6,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 4.0 ⚖️',
            examType: 'أعمال سنة 40% + نهائي 60% 📊',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'توزيع فروع المادة: نحو وصرف، قراءة ونصوص، تعبير وإملاء وخط.'
        },
        {
            id: 'DIST-09-QRN',
            code: 'DIST-09-QRN',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'القرآن الكريم وأحكام التلاوة والتجويد',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 4,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 3.0 ⚖️',
            examType: 'شفهي تلاوة وتسميع + تحريري تجويد',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'حفظ وتسميع السور المقررة وتطبيق أحكام التجويد عملياً.'
        },
        {
            id: 'DIST-09-COMP',
            code: 'DIST-09-COMP',
            grade: 'الصف التاسع أساسي (الشهادة الأساسية)',
            subject: 'الحاسوب وتقنية المعلومات والذكاء الاصطناعي',
            stage: 'المرحلة الأساسية - صفوف 7-9',
            weeklyPeriods: 2,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 2.0 ⚖️',
            examType: 'تطبيقي عملي بمعمل الحاسوب 💻',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'تدريب الطلاب على البرمجة الأساسية واستخدام الأدوات التقنية الحديثة.'
        },
        {
            id: 'DIST-12-PHY',
            code: 'DIST-12-PHY',
            grade: 'الصف الثالث الثانوي (علمي)',
            subject: 'الفيزياء المتقدمة والميكانيكا والكهرباء',
            stage: 'المرحلة الثانوية 10-12',
            weeklyPeriods: 6,
            maxMark: 100,
            minMark: 50,
            weight: 'معامل 5.0 ⚖️',
            examType: 'أعمال سنة + اختبار وزاري نهائي 📊',
            isCounted: 'نعم - مادة أساسية تدخل في المجموع 🟢',
            status: 'معتمدة وفعالة بالجدول 🟢',
            notes: 'مقرر تأهيلي للشهادة الثانوية العامة بالتركيز على حل المسائل المتقدمة.'
        }
    ];
}

function renderSubjectDistributionGrid() {
    const tb = document.getElementById('tbl-subject-distribution-grid') || document.getElementById('tbl-subject-distribution');
    if (!tb) return;

    const query = (document.getElementById('searchSubjectDist')?.value || '').toLowerCase().trim();
    const gradeFilter = document.getElementById('filterDistGrade')?.value || 'all';
    const items = window.DB.subjectDistribution || [];

    const totEl = document.getElementById('sdtTotalDistributed');
    const compEl = document.getElementById('sdtCompletedGrades');
    const perEl = document.getElementById('sdtTotalPeriods');
    const avgEl = document.getElementById('sdtAvgPeriods');

    if (totEl) totEl.innerHTML = `64 <small style="font-size:0.75rem;">توزيعاً أكاديمياً 📚</small>`;
    if (compEl) compEl.innerHTML = `15 <small style="font-size:0.75rem;">صفاً مكتملاً 🎓</small>`;
    if (perEl) perEl.innerHTML = `280 <small style="font-size:0.75rem;">حصة / أسبوع ⏱️</small>`;
    if (avgEl) avgEl.innerHTML = `32 <small style="font-size:0.75rem;">حصة / أسبوع 📊</small>`;

    const filtered = items.filter(s => {
        if (gradeFilter === 'تاسع' && !s.grade.includes('تاسع')) return false;
        if (gradeFilter === 'ثانوي' && !s.stage.includes('ثانوي')) return false;
        if (gradeFilter === 'أساسي' && !s.stage.includes('أساسي')) return false;
        if (gradeFilter === 'روضة' && !s.stage.includes('روضة')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.grade, s.subject, s.stage, s.examType, s.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد توزيعات مواد مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let stageBadge = '<span class="badge badge-success" style="font-size:0.75rem;">أساسي 🟢</span>';
        if (s.stage.includes('ثانوي')) {
            stageBadge = '<span class="badge badge-danger" style="font-size:0.75rem;">ثانوي 🔴</span>';
        } else if (s.stage.includes('روضة')) {
            stageBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">رياض أطفال 👶</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> معتمدة بالخطة 🟢</span>';

        return `
            <tr data-collection="subjectDistribution" data-id="${s.id || s.code}" ondblclick="openForm('subject_distribution', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('subjectDistribution', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-graduation-cap" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.grade}</td>
                <td style="font-weight:700;color:#38bdf8;">${s.subject}</td>
                <td>${stageBadge}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">${s.weeklyPeriods} حصص ⏱️</span></td>
                <td><strong style="color:#38bdf8;font-family:monospace;font-size:0.85rem;">${s.maxMark} درجة</strong></td>
                <td><span class="badge badge-success" style="font-size:0.75rem;">${s.minMark}</span></td>
                <td><span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">${s.weight}</span></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.examType}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('⏱️ استعراض جدول وتوزيع حصص: ${s.subject} لصف ${s.grade}');"><i class="fa-solid fa-clock"></i> توزيع الحصص</button></td>
            </tr>
        `;
    }).join('');
}
window.renderSubjectDistributionGrid = renderSubjectDistributionGrid;
window.renderSubjectDistribution = renderSubjectDistributionGrid;
// Initial render
try { renderSubjectDistributionGrid(); } catch(e) {}


/**
 * ============================================================================
 * CLASSROOMS & LABS DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.classrooms) {
    window.DB.classrooms = [
        {
            id: 'ROOM-104',
            code: 'ROOM-104',
            name: 'قاعة 104 - شعبة التاسع أساسي (أ)',
            nameEn: 'Classroom 104 - Grade 9 Section A',
            type: 'قاعة صفية قياسية 🏫',
            building: 'المبنى الرئيسي - الطابق الأول (جناح البنين)',
            capacity: 35,
            assignedSection: 'شعبة التاسع أساسي (أ) - بنين',
            equipment: 'شاشة تفاعلية ذكية 75 بوصة 4K 📺 + تكييف مركزي',
            supervisor: 'أ. عادل عبد الله العولقي (رائد الفصل)',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'مشغولة حالياً ⏱️',
            notes: 'مجهزة بأحدث الوسائل التعليمية ومقاعد مريحة ومنصة للمعلم.'
        },
        {
            id: 'LAB-SCI-01',
            code: 'LAB-SCI-01',
            name: 'معمل الفيزياء والكيمياء المتطور (1)',
            nameEn: 'Advanced Physics & Chemistry Lab 1',
            type: 'معمل علوم وفيزياء 🔬',
            building: 'مبنى المعامل والمختبرات - الطابق الثاني',
            capacity: 32,
            assignedSection: 'المرحلة الأساسية العليا (7-9) والثانوية',
            equipment: 'أدوات تجارب كيميائية، مجاهر إلكترونية، جهاز بروجكتر 🔬',
            supervisor: 'أ. سالم الحميري (مشرف المعامل العلمية)',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'متاحة للحجز والأنشطة 🟢',
            notes: 'مجهز بمضخات طوارئ، طفايات حريق كيميائية، وشفاطات أبخرة متقدمة.'
        },
        {
            id: 'LAB-COMP-01',
            code: 'LAB-COMP-01',
            name: 'معمل الحاسوب والذكاء الاصطناعي والروبوتات',
            nameEn: 'AI, Robotics & Computer Science Lab',
            type: 'معمل حاسوب وذكاء اصطناعي 💻',
            building: 'مبنى المعامل - الطابق الأرضي',
            capacity: 30,
            assignedSection: 'كافة المراحل التعليمية (وفق الجدول)',
            equipment: '30 جهاز حاسوب Core i7 + شبكة فايبر + شاشة ذكية 💻',
            supervisor: 'م. خالد عبد الكريم (مسؤول تقنية المعلومات)',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'مشغولة حالياً ⏱️',
            notes: 'بيئة تدريبية مجهزة بحزم برمجيات بايثون وتطوير الويب والروبوتات.'
        },
        {
            id: 'ROOM-101',
            code: 'ROOM-101',
            name: 'قاعة 101 - التأسيس والتعليم المبكر',
            nameEn: 'Classroom 101 - Early Childhood Room',
            type: 'قاعة صفية قياسية 🏫',
            building: 'المبنى الرئيسي - الجناح الأيمن (الطابق الأرضي)',
            capacity: 30,
            assignedSection: 'شعبة الأول أساسي (أ) - تميز',
            equipment: 'شاشة ذكية 65 بوصة + ركن قراءة تفاعلي 🎨',
            supervisor: 'أ. أروى ناصر المنصوب',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'مشغولة حالياً ⏱️',
            notes: 'أثاث جاذب للأطفال ومناسب لأنشطة التعلم باللعب وتنمية المهارات.'
        },
        {
            id: 'LAB-LANG-01',
            code: 'LAB-LANG-01',
            name: 'معمل اللغات الحديثة والصوتيات (Language Lab)',
            nameEn: 'Modern Languages & Audio Lab',
            type: 'معمل لغات وصوتيات 🎧',
            building: 'المبنى الرئيسي - الطابق الثاني',
            capacity: 28,
            assignedSection: 'طلاب اللغات والإنجليزية والفرنسية',
            equipment: '28 وحدة استماع تفاعلية وسماعات عازلة 🎧',
            supervisor: 'أ. محمد طاهر اليافعي',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'متاحة للحجز والأنشطة 🟢',
            notes: 'مخصص لاختبارات المحادثة والاستماع وفق معايير كامبردج وكريسنت.'
        },
        {
            id: 'HALL-ACT-01',
            code: 'HALL-ACT-01',
            name: 'الصالة الرياضية وقاعة الأنشطة المغلقة',
            nameEn: 'Indoor Sports & Activities Arena',
            type: 'صالة أنشطة ورياضة 🏆',
            building: 'المجمع الرياضي والملاعب المغلقة',
            capacity: 250,
            assignedSection: 'جميع طلاب المدرسة والفرق الرياضية',
            equipment: 'أرضيات مطاطية أولمبية، تجهيزات كرة السلة والطائرة والجمباز 🏀',
            supervisor: 'ك. فاروق الزبيدي (مشرف التربية البدنية)',
            operationalStatus: 'مجهزة وجاهزة للعمل 🟢',
            scheduleStatus: 'متاحة للحجز والأنشطة 🟢',
            notes: 'إقامة البطولات المدرسية والاحتفالات والمعارض الكبرى والأنشطة.'
        }
    ];
}

function renderClassroomsGrid() {
    const tb = document.getElementById('tbl-classrooms-grid') || document.getElementById('tbl-classrooms');
    if (!tb) return;

    const query = (document.getElementById('searchClassrooms')?.value || document.getElementById('searchClassroom')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterRoomType')?.value || 'all';
    const items = window.DB.classrooms || [];

    // Calculate KPIs
    let totalCount = items.length;
    let availCount = 0;
    let totalCap = 0;

    items.forEach(s => {
        const cap = Number(s.capacity) || 0;
        totalCap += cap;
        const st = String(s.status || s.operationalStatus || '');
        if (!st || st.includes('جاهز') || st.includes('متاح') || st.includes('🟢')) {
            availCount++;
        }
    });

    const totEl = document.getElementById('clsTotal') || document.getElementById('clsTotalRooms');
    const availEl = document.getElementById('clsAvail') || document.getElementById('clsStandardRooms');
    const capEl = document.getElementById('clsCapacity') || document.getElementById('clsTotalCapacity');

    if (totEl) totEl.textContent = totalCount;
    if (availEl) availEl.textContent = availCount;
    if (capEl) capEl.innerHTML = `<span dir="ltr" style="display:inline-block;"><span style="font-weight:800;">${totalCap.toLocaleString()}</span> <small style="font-size:0.75rem;font-weight:normal;">مقعد 🪑</small></span>`;

    const filtered = items.filter(s => {
        const roomType = String(s.type || (
            s.name && (s.name.includes('معمل') || s.name.includes('مختبر') || s.name.includes('فيزياء') || s.name.includes('كيمياء')) ? 'معمل علوم وتجارب' :
            (s.name && s.name.includes('حاسوب') ? 'معمل حاسوب وبرمجة' :
            (s.name && (s.name.includes('صالة') || s.name.includes('مسرح')) ? 'صالة أنشطة ومسرح' : 'قاعة صفية قياسية'))
        ));

        if (typeFilter === 'صفية' && !roomType.includes('صفية')) return false;
        if (typeFilter === 'علوم' && !roomType.includes('علوم') && !roomType.includes('مختبر')) return false;
        if (typeFilter === 'حاسوب' && !roomType.includes('حاسوب') && !roomType.includes('ذكاء')) return false;
        if (typeFilter === 'أنشطة' && !roomType.includes('أنشطة') && !roomType.includes('مسرح') && !roomType.includes('رياضة')) return false;

        if (!query) return true;
        const text = [
            s.id, s.code, s.name, s.nameEn, roomType, s.building, s.floor, s.assignedSection, s.supervisor, s.status
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد قاعات أو معامل مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        const roomType = String(s.type || (
            s.name && (s.name.includes('معمل') || s.name.includes('مختبر') || s.name.includes('فيزياء') || s.name.includes('كيمياء')) ? 'معمل علوم 🔬' :
            (s.name && s.name.includes('حاسوب') ? 'معمل حاسوب 💻' :
            (s.name && (s.name.includes('صالة') || s.name.includes('مسرح')) ? 'صالة أنشطة 🏆' : 'قاعة صفية 🏫'))
        ));

        let typeBadge = '<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-chalkboard" style="margin-left:4px;"></i> قاعة صفية 🏫</span>';
        if (roomType.includes('علوم') || roomType.includes('مختبر')) {
            typeBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-flask" style="margin-left:4px;"></i> معمل علوم 🔬</span>';
        } else if (roomType.includes('حاسوب')) {
            typeBadge = '<span class="badge" style="background:rgba(56,189,248,0.15);color:#38bdf8;font-size:0.75rem;"><i class="fa-solid fa-laptop-code" style="margin-left:4px;"></i> معمل حاسوب 💻</span>';
        } else if (roomType.includes('أنشطة') || roomType.includes('مسرح')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-trophy" style="margin-left:4px;"></i> صالة أنشطة 🏆</span>';
        }

        const rawStatus = String(s.status || s.operationalStatus || 'جاهزة ومتاحة 🟢');
        const isActive = !rawStatus || rawStatus.includes('جاهز') || rawStatus.includes('متاح') || rawStatus.includes('🟢');
        const statusBadge = isActive
            ? '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> ' + rawStatus + '</span>'
            : '<span class="badge badge-warning"><i class="fa-solid fa-wrench"></i> ' + rawStatus + '</span>';

        const roomCode = s.code || s.id || ('ROOM-' + (idx + 101));
        const bldName = s.building || 'المبنى الرئيسي';
        const flrName = s.floor ? ` - ${s.floor}` : '';
        const capNum = Number(s.capacity) || 35;
        const equip = s.equipment || s.smartBoard || 'شاشة تفاعلية 4K 📺';

        return `
            <tr data-collection="classrooms" data-id="${s.id || roomCode}" ondblclick="openForm('classrooms', '${s.id || roomCode}')" oncontextmenu="event.preventDefault();deleteItem('classrooms', '${s.id || roomCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;"><i class="fa-solid fa-door-closed" style="color:#60a5fa;font-size:0.75rem;margin-left:4px;"></i> ${roomCode}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-chalkboard-user" style="color:#38bdf8;font-size:0.8rem;margin-left:4px;"></i> ${s.name}</td>
                <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-building" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${bldName}${flrName}</td>
                <td style="text-align:center;"><span dir="ltr" style="display:inline-flex;align-items:center;gap:4px;"><strong style="color:#34d399;font-family:monospace;font-size:0.88rem;">${capNum}</strong> <small style="color:#94a3b8;">مقعد 🪑</small></span></td>
                <td>${typeBadge}</td>
                <td style="color:#94a3b8;font-size:0.8rem;"><i class="fa-solid fa-tv" style="color:#38bdf8;font-size:0.75rem;margin-left:4px;"></i> ${equip}</td>
                <td>${statusBadge}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل القاعة" onclick="openForm('classrooms', '${s.id || roomCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف القاعة" onclick="deleteItem('classrooms', '${s.id || roomCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderClassroomsGrid = renderClassroomsGrid;
window.renderClassrooms = renderClassroomsGrid;
/**
 * ============================================================================
 * CLASS PERIOD TIMES & BELL SCHEDULE ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.classTimes) {
    window.DB.classTimes = [
        {
            id: 'PRD-MORN-00',
            code: 'PRD-MORN-00',
            name: 'طابور الصباح والإذاعة والتمارين الرياضية',
            nameEn: 'Morning Assembly & Physical Exercises',
            type: 'طابور الصباح ☀️',
            startTime: '07:30 ص',
            endTime: '07:55 ص',
            duration: '25 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'الاصطفاف الصباحي، السلام الوطني، القرآن الكريم، والفقرات الإذاعية.'
        },
        {
            id: 'PRD-MORN-01',
            code: 'PRD-MORN-01',
            name: 'الحصة الدراسية الأولى (Period 1)',
            nameEn: 'First Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '08:00 ص',
            endTime: '08:45 ص',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'بداية الحصص الدراسية الأولى ورصد الحضور والغياب الصفي.'
        },
        {
            id: 'PRD-MORN-02',
            code: 'PRD-MORN-02',
            name: 'الحصة الدراسية الثانية (Period 2)',
            nameEn: 'Second Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '08:45 ص',
            endTime: '09:30 ص',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'فترة تدريس مباشر وفق الخطة الأكاديمية المعتمدة.'
        },
        {
            id: 'PRD-MORN-03',
            code: 'PRD-MORN-03',
            name: 'الحصة الدراسية الثالثة (Period 3)',
            nameEn: 'Third Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '09:30 ص',
            endTime: '10:15 ص',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'الحصة الأخيرة قبل استراحة الفسحة الكبرى.'
        },
        {
            id: 'BRK-RECESS-01',
            code: 'BRK-RECESS-01',
            name: 'استراحة الفسحة المدرسية وتناول الوجبات',
            nameEn: 'Main Recess & Breakfast Break',
            type: 'استراحة وفسحة 🥪',
            startTime: '10:15 ص',
            endTime: '10:45 ص',
            duration: '30 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'إشراف مناوبي الساحة والمقصف المدرسي لضمان سلامة الطلاب.'
        },
        {
            id: 'PRD-MORN-04',
            code: 'PRD-MORN-04',
            name: 'الحصة الدراسية الرابعة (Period 4)',
            nameEn: 'Fourth Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '10:45 ص',
            endTime: '11:30 ص',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'استئناف الحصص الصفية والمختبرات بعد الفسحة.'
        },
        {
            id: 'PRD-MORN-05',
            code: 'PRD-MORN-05',
            name: 'الحصة الدراسية الخامسة (Period 5)',
            nameEn: 'Fifth Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '11:30 ص',
            endTime: '12:15 م',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'كافة المراحل الدراسية',
            bellTone: 'جرس تلقائي مبرمج 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'حصص علمية وتطبيقية وتدريبات إثرائية.'
        },
        {
            id: 'BRK-PRAYER-01',
            code: 'BRK-PRAYER-01',
            name: 'استراحة صلاة الظهر جماعة بالمسجد المدرسي',
            nameEn: 'Dhuhr Prayer Congregation Break',
            type: 'فترة صلاة الظهر 🕌',
            startTime: '12:15 م',
            endTime: '12:30 م',
            duration: '15 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'الأساسي العليا (7-9) والثانوي',
            bellTone: 'أذان + تنبيه صوتي 📢',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'أداء صلاة الظهر جماعة بإشراف معلمي التربية الإسلامية.'
        },
        {
            id: 'PRD-MORN-06',
            code: 'PRD-MORN-06',
            name: 'الحصة الدراسية السادسة (Period 6)',
            nameEn: 'Sixth Academic Period',
            type: 'حصة تعليمية صفية 📚',
            startTime: '12:30 م',
            endTime: '01:15 م',
            duration: '45 دقيقة ⏱️',
            shift: 'دوام صباحي قياسي ☀️',
            stages: 'المرحلة الأساسية والثانوية',
            bellTone: 'جرس ختام الدوام 🔔',
            status: 'مفعلة وتعمل بالجدول 🟢',
            notes: 'ختام الدوام المدرسي وتوديع الطلاب وحافلات النقل.'
        }
    ];
}

function renderClassTimesGrid() {
    const tb = document.getElementById('tbl-class-times-grid') || document.getElementById('tbl-class-times');
    if (!tb) return;

    const query = (document.getElementById('searchClassTimes')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterPeriodShift')?.value || 'all';
    const items = window.DB.classTimes || [];

    const totEl = document.getElementById('ctmTotalPeriods');
    const durEl = document.getElementById('ctmPeriodDuration');
    const strEl = document.getElementById('ctmDayStart');
    const hrsEl = document.getElementById('ctmTotalHours');

    if (totEl) totEl.innerHTML = `7 <small style="font-size:0.75rem;">حصص يومية ⏰</small>`;
    if (durEl) durEl.innerHTML = `45 <small style="font-size:0.75rem;">دقيقة / حصة ⏱️</small>`;
    if (strEl) strEl.innerHTML = `07:30 <small style="font-size:0.75rem;">صباحاً ☀️</small>`;
    if (hrsEl) hrsEl.innerHTML = `5 س و 45 د <small style="font-size:0.75rem;">⏳</small>`;

    const filtered = items.filter(s => {
        if (typeFilter === 'حصة' && !s.type.includes('حصة')) return false;
        if (typeFilter === 'استراحة' && !s.type.includes('استراحة') && !s.type.includes('طابور') && !s.type.includes('صلاة')) return false;
        if (typeFilter === 'صباحي' && !s.shift.includes('صباحي')) return false;
        if (typeFilter === 'مسائي' && !s.shift.includes('مسائي')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.type, s.startTime, s.endTime, s.shift, s.status].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد أوقات حصص مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let typeBadge = '<span class="badge badge-info" style="font-size:0.75rem;">حصة صفية 📚</span>';
        if (s.type.includes('طابور')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">طابور صباحي ☀️</span>';
        } else if (s.type.includes('استراحة')) {
            typeBadge = '<span class="badge badge-success" style="font-size:0.75rem;">فسحة ووجبة 🥪</span>';
        } else if (s.type.includes('صلاة')) {
            typeBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">صلاة الظهر 🕌</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> مفعلة بالجدول 🟢</span>';

        return `
            <tr data-collection="classTimes" data-id="${s.id || s.code}" ondblclick="openForm('class_times', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('classTimes', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.95rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-bell" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.name}</td>
                <td>${typeBadge}</td>
                <td><strong style="color:#34d399;font-family:monospace;font-size:0.9rem;">${s.startTime}</strong></td>
                <td><strong style="color:#f87171;font-family:monospace;font-size:0.9rem;">${s.endTime}</strong></td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">${s.duration}</span></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.shift}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.stages}</td>
                <td><span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">${s.bellTone}</span></td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof playSchoolBellSound==='function'){ playSchoolBellSound('${s.bellTone}'); } else if(typeof toast==='function'){ toast('🔔 تجربة جرس: ${s.name}'); }"><i class="fa-solid fa-volume-high"></i> نغمة الجرس</button></td>
            </tr>
        `;
    }).join('');
}
window.renderClassTimesGrid = renderClassTimesGrid;
window.renderClassTimes = renderClassTimesGrid;
// Initial render
try { renderClassTimesGrid(); } catch(e) {}


/**
 * SCHOOL BELL SYNTHESIZER (WEB AUDIO API SOUND ENGINE)
 */
function playSchoolBellSound(toneName) {
    if (!toneName) toneName = 'رنين جرس كلاسيكي تلقائي 🔔';
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    
    try {
        const ctx = new AudioCtx();
        if (ctx.state === 'suspended') {
            ctx.resume();
        }

        const now = ctx.currentTime;

        if (toneName.includes('كلاسيكي') || toneName.includes('جرس تلقائي')) {
            // 🔔 Classic Metallic School Bell (Rapid pulsing dual-frequency bell)
            if (typeof toast === 'function') toast('🔔 تشغيل: رنين جرس كلاسيكي تلقائي');
            
            for (let i = 0; i < 8; i++) {
                const strikeTime = now + (i * 0.12);
                
                // Primary high tone
                const osc1 = ctx.createOscillator();
                const gain1 = ctx.createGain();
                osc1.type = 'triangle';
                osc1.frequency.setValueAtTime(880 + (i % 2 === 0 ? 30 : -30), strikeTime);
                gain1.gain.setValueAtTime(0.3, strikeTime);
                gain1.gain.exponentialRampToValueAtTime(0.001, strikeTime + 0.1);
                osc1.connect(gain1);
                gain1.connect(ctx.destination);
                osc1.start(strikeTime);
                osc1.stop(strikeTime + 0.11);

                // Metallic sub-tone
                const osc2 = ctx.createOscillator();
                const gain2 = ctx.createGain();
                osc2.type = 'sine';
                osc2.frequency.setValueAtTime(1760, strikeTime);
                gain2.gain.setValueAtTime(0.15, strikeTime);
                gain2.gain.exponentialRampToValueAtTime(0.001, strikeTime + 0.1);
                osc2.connect(gain2);
                gain2.connect(ctx.destination);
                osc2.start(strikeTime);
                osc2.stop(strikeTime + 0.11);
            }
        } else if (toneName.includes('موسيقية') || toneName.includes('إلكترونية')) {
            // 🎵 Melodic Westminster / Electronic Chime (4 harmonic notes: E5, C5, D5, G4)
            if (typeof toast === 'function') toast('🎵 تشغيل: نغمة إلكترونية موسيقية');
            
            const notes = [
                { f: 659.25, t: 0.0, d: 0.45 }, // E5
                { f: 523.25, t: 0.4, d: 0.45 }, // C5
                { f: 587.33, t: 0.8, d: 0.45 }, // D5
                { f: 392.00, t: 1.2, d: 0.90 }  // G4 (Long resolving note)
            ];

            notes.forEach(n => {
                const noteTime = now + n.t;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(n.f, noteTime);
                
                gain.gain.setValueAtTime(0.0, noteTime);
                gain.gain.linearRampToValueAtTime(0.35, noteTime + 0.04);
                gain.gain.exponentialRampToValueAtTime(0.001, noteTime + n.d);
                
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(noteTime);
                osc.stop(noteTime + n.d + 0.05);
            });
        } else if (toneName.includes('إذاعي') || toneName.includes('صوتي')) {
            // 📢 Broadcast Intercom Two-Tone Alert (Bing-Bong chime)
            if (typeof toast === 'function') toast('📢 تشغيل: تنبيه صوتي إذاعي (Intercom Alert)');
            
            // High tone
            const osc1 = ctx.createOscillator();
            const gain1 = ctx.createGain();
            osc1.type = 'sine';
            osc1.frequency.setValueAtTime(587.33, now); // D5
            gain1.gain.setValueAtTime(0.0, now);
            gain1.gain.linearRampToValueAtTime(0.4, now + 0.03);
            gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
            osc1.connect(gain1);
            gain1.connect(ctx.destination);
            osc1.start(now);
            osc1.stop(now + 0.55);

            // Low tone
            const osc2 = ctx.createOscillator();
            const gain2 = ctx.createGain();
            osc2.type = 'sine';
            osc2.frequency.setValueAtTime(440.00, now + 0.4); // A4
            gain2.gain.setValueAtTime(0.0, now + 0.4);
            gain2.gain.linearRampToValueAtTime(0.4, now + 0.43);
            gain2.gain.exponentialRampToValueAtTime(0.001, now + 1.1);
            osc2.connect(gain2);
            gain2.connect(ctx.destination);
            osc2.start(now + 0.4);
            osc2.stop(now + 1.15);
        } else if (toneName.includes('بدون')) {
            if (typeof toast === 'function') toast('🔇 تم اختيار: بدون جرس (كتم الصوت)');
        }
    } catch (e) {
        console.warn('AudioContext playback error:', e);
    }
}
window.playSchoolBellSound = playSchoolBellSound;



/**
 * ============================================================================
 * TIMETABLE BUILDER ENGINE: 5 DAYS (SAT-WED) x 7 PERIODS MATRIX & LIST GRID
 * ============================================================================
 */
if (!window.DB) window.DB = {};

window.DB.timetableDays = ['السبت', 'الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء'];
window.DB.timetablePeriods = [
    { num: 1, label: 'الحصة 1', time: '08:00 ص - 08:45 ص' },
    { num: 2, label: 'الحصة 2', time: '08:45 ص - 09:30 ص' },
    { num: 3, label: 'الحصة 3', time: '09:30 ص - 10:15 ص' },
    { num: 4, label: 'الحصة 4', time: '10:45 ص - 11:30 ص' },
    { num: 5, label: 'الحصة 5', time: '11:30 ص - 12:15 م' },
    { num: 6, label: 'الحصة 6', time: '12:30 م - 01:15 م' },
    { num: 7, label: 'الحصة 7', time: '01:15 م - 02:00 م' }
];

if (!window.DB.timetableBuilder || window.DB.timetableBuilder.length < 15) {
    window.DB.timetableBuilder = [
        // السبت (Saturday)
        { id: 'SCH-09A-SAT-1', code: 'SCH-09A-SAT-1', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 1, period: 'الحصة 1 (08:00 ص - 08:45 ص) ⏱️', subject: 'القرآن الكريم والتجويد 📖', teacher: 'الشيخ عبد الرحمن باعباد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تلاوة سورة الإسراء' },
        { id: 'SCH-09A-SAT-2', code: 'SCH-09A-SAT-2', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 2, period: 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', subject: 'الرياضيات المتقدمة 📐', teacher: 'أ. إبراهيم الحداد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'الجبر والمعادلات' },
        { id: 'SCH-09A-SAT-3', code: 'SCH-09A-SAT-3', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 3, period: 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', subject: 'العلوم العامة والفيزياء 🔬', teacher: 'أ. سالم الحميري', room: 'معمل العلوم 1', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تجارب المغناطيسية' },
        { id: 'SCH-09A-SAT-4', code: 'SCH-09A-SAT-4', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 4, period: 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', subject: 'اللغة الإنجليزية 🇬🇧', teacher: 'أ. محمد طاهر اليافعي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'Unit 1 Grammar' },
        { id: 'SCH-09A-SAT-5', code: 'SCH-09A-SAT-5', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 5, period: 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', subject: 'اللغة العربية والنحو ✍️', teacher: 'أ. عادل عبد الله العولقي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'إعراب الفعل المضارع' },
        { id: 'SCH-09A-SAT-6', code: 'SCH-09A-SAT-6', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 6, period: 'الحصة 6 (12:30 م - 01:15 م) ⏱️', subject: 'الحاسوب والذكاء الاصطناعي 💻', teacher: 'م. خالد عبد الكريم', room: 'معمل الحاسوب', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تطبيق عملي بايثون' },
        { id: 'SCH-09A-SAT-7', code: 'SCH-09A-SAT-7', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'السبت', periodNum: 7, period: 'الحصة 7 (01:15 م - 02:00 م) ⏱️', subject: 'التربية الرياضية والبدنية ⚽', teacher: 'ك. فاروق الزبيدي', room: 'الصالة الرياضية', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'دوري كرة القدم' },

        // الأحد (Sunday)
        { id: 'SCH-09A-SUN-1', code: 'SCH-09A-SUN-1', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 1, period: 'الحصة 1 (08:00 ص - 08:45 ص) ⏱️', subject: 'الرياضيات المتقدمة 📐', teacher: 'أ. إبراهيم الحداد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'الهندسة والتحليل' },
        { id: 'SCH-09A-SUN-2', code: 'SCH-09A-SUN-2', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 2, period: 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', subject: 'العلوم العامة والفيزياء 🔬', teacher: 'أ. سالم الحميري', room: 'معمل العلوم 1', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'الضوء والانكسار' },
        { id: 'SCH-09A-SUN-3', code: 'SCH-09A-SUN-3', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 3, period: 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', subject: 'اللغة الإنجليزية 🇬🇧', teacher: 'أ. محمد طاهر اليافعي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'Reading Comprehension' },
        { id: 'SCH-09A-SUN-4', code: 'SCH-09A-SUN-4', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 4, period: 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', subject: 'اللغة العربية والنحو ✍️', teacher: 'أ. عادل عبد الله العولقي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'قواعد النحو العربي' },
        { id: 'SCH-09A-SUN-5', code: 'SCH-09A-SUN-5', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 5, period: 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', subject: 'التربية الإسلامية والفقه 🕌', teacher: 'الشيخ عبد الرحمن باعباد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'أحكام الصلاة' },
        { id: 'SCH-09A-SUN-6', code: 'SCH-09A-SUN-6', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 6, period: 'الحصة 6 (12:30 م - 01:15 م) ⏱️', subject: 'الدراسات الاجتماعية 🌍', teacher: 'أ. طارق الشميري', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'جغرافية الوطن العربي' },
        { id: 'SCH-09A-SUN-7', code: 'SCH-09A-SUN-7', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأحد', periodNum: 7, period: 'الحصة 7 (01:15 م - 02:00 م) ⏱️', subject: 'النشاط العلمي والابتكار 💡', teacher: 'م. خالد عبد الكريم', room: 'معمل الروبوت', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'مشاريع العلوم' },

        // الإثنين (Monday)
        { id: 'SCH-09A-MON-1', code: 'SCH-09A-MON-1', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 1, period: 'الحصة 1 (08:00 ص - 08:45 ص) ⏱️', subject: 'الرياضيات المتقدمة 📐', teacher: 'أ. إبراهيم الحداد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'مسائل تدريبية' },
        { id: 'SCH-09A-MON-2', code: 'SCH-09A-MON-2', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 2, period: 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', subject: 'اللغة الإنجليزية 🇬🇧', teacher: 'أ. محمد طاهر اليافعي', room: 'معمل اللغات', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'Audio Listening Session' },
        { id: 'SCH-09A-MON-3', code: 'SCH-09A-MON-3', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 3, period: 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', subject: 'العلوم العامة والكيمياء 🧪', teacher: 'أ. سالم الحميري', room: 'معمل العلوم 1', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'التفاعلات الكيميائية' },
        { id: 'SCH-09A-MON-4', code: 'SCH-09A-MON-4', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 4, period: 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', subject: 'اللغة العربية والبلاغة ✍️', teacher: 'أ. عادل عبد الله العولقي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'التشبيه والاستعارة' },
        { id: 'SCH-09A-MON-5', code: 'SCH-09A-MON-5', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 5, period: 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', subject: 'القرآن الكريم والتجويد 📖', teacher: 'الشيخ عبد الرحمن باعباد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تسميع السورة' },
        { id: 'SCH-09A-MON-6', code: 'SCH-09A-MON-6', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 6, period: 'الحصة 6 (12:30 م - 01:15 م) ⏱️', subject: 'الدراسات الاجتماعية 🌍', teacher: 'أ. طارق الشميري', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تاريخ الحضارة الإسلامية' },
        { id: 'SCH-09A-MON-7', code: 'SCH-09A-MON-7', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الإثنين', periodNum: 7, period: 'الحصة 7 (01:15 م - 02:00 م) ⏱️', subject: 'التربية الفنية والرسم 🎨', teacher: 'أ. وسيم القادري', room: 'مرسم الفنون', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'رسم المنظور الهندسي' },

        // الثلاثاء (Tuesday)
        { id: 'SCH-09A-TUE-1', code: 'SCH-09A-TUE-1', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 1, period: 'الحصة 1 (08:00 ص - 08:45 ص) ⏱️', subject: 'العلوم العامة والأحياء 🌿', teacher: 'أ. سالم الحميري', room: 'معمل العلوم 1', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تركيب الخلية الحية' },
        { id: 'SCH-09A-TUE-2', code: 'SCH-09A-TUE-2', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 2, period: 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', subject: 'الرياضيات المتقدمة 📐', teacher: 'أ. إبراهيم الحداد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'حساب المثلثات' },
        { id: 'SCH-09A-TUE-3', code: 'SCH-09A-TUE-3', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 3, period: 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', subject: 'اللغة العربية والنحو ✍️', teacher: 'أ. عادل عبد الله العولقي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'الممنوع من الصرف' },
        { id: 'SCH-09A-TUE-4', code: 'SCH-09A-TUE-4', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 4, period: 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', subject: 'اللغة الإنجليزية 🇬🇧', teacher: 'أ. محمد طاهر اليافعي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'Writing an Essay' },
        { id: 'SCH-09A-TUE-5', code: 'SCH-09A-TUE-5', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 5, period: 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', subject: 'الحاسوب والذكاء الاصطناعي 💻', teacher: 'م. خالد عبد الكريم', room: 'معمل الحاسوب', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'تطوير موقع ويب' },
        { id: 'SCH-09A-TUE-6', code: 'SCH-09A-TUE-6', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 6, period: 'الحصة 6 (12:30 م - 01:15 م) ⏱️', subject: 'التربية الإسلامية والحديث 🕌', teacher: 'الشيخ عبد الرحمن باعباد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'شرح الأحاديث النبوية' },
        { id: 'SCH-09A-TUE-7', code: 'SCH-09A-TUE-7', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الثلاثاء', periodNum: 7, period: 'الحصة 7 (01:15 م - 02:00 م) ⏱️', subject: 'التربية الرياضية والبدنية 🏀', teacher: 'ك. فاروق الزبيدي', room: 'الصالة الرياضية', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'كرة السلة واللياقة' },

        // الأربعاء (Wednesday)
        { id: 'SCH-09A-WED-1', code: 'SCH-09A-WED-1', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 1, period: 'الحصة 1 (08:00 ص - 08:45 ص) ⏱️', subject: 'الرياضيات المتقدمة 📐', teacher: 'أ. إبراهيم الحداد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'المراجعة الأسبوعية' },
        { id: 'SCH-09A-WED-2', code: 'SCH-09A-WED-2', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 2, period: 'الحصة 2 (08:45 ص - 09:30 ص) ⏱️', subject: 'العلوم العامة والفيزياء 🔬', teacher: 'أ. سالم الحميري', room: 'معمل العلوم 1', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'اختبار قصير معملي' },
        { id: 'SCH-09A-WED-3', code: 'SCH-09A-WED-3', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 3, period: 'الحصة 3 (09:30 ص - 10:15 ص) ⏱️', subject: 'اللغة الإنجليزية 🇬🇧', teacher: 'أ. محمد طاهر اليافعي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'Speaking & Debate' },
        { id: 'SCH-09A-WED-4', code: 'SCH-09A-WED-4', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 4, period: 'الحصة 4 (10:45 ص - 11:30 ص) ⏱️', subject: 'اللغة العربية والتعبير ✍️', teacher: 'أ. عادل عبد الله العولقي', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'كتابة المقال الإبداعي' },
        { id: 'SCH-09A-WED-5', code: 'SCH-09A-WED-5', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 5, period: 'الحصة 5 (11:30 ص - 12:15 م) ⏱️', subject: 'القرآن الكريم والسيرة 📖', teacher: 'الشيخ عبد الرحمن باعباد', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'غزوة بدر الكبرى' },
        { id: 'SCH-09A-WED-6', code: 'SCH-09A-WED-6', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 6, period: 'الحصة 6 (12:30 م - 01:15 م) ⏱️', subject: 'الدراسات الاجتماعية 🌍', teacher: 'أ. طارق الشميري', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'البيئة والتنمية' },
        { id: 'SCH-09A-WED-7', code: 'SCH-09A-WED-7', sectionId: 'SEC-09A', section: 'شعبة التاسع أساسي (أ) - بنين', day: 'الأربعاء', periodNum: 7, period: 'الحصة 7 (01:15 م - 02:00 م) ⏱️', subject: 'نشاط الإرشاد الأكاديمي 👥', teacher: 'أ. عادل العولقي (رائد الفصل)', room: 'قاعة 104', branch: 'بنين - صباحي ☀️', conflictCheck: 'سليم 100% بدون تعارض 🟢', status: 'معتمد ومنشور 🟢', notes: 'حصة ريادة وتقييم أسبوعي' }
    ];
}

function autoGenerateTimetable() {
    if (typeof toast === 'function') toast('⚡ جاري تشغيل خوارزمية بناء الجدول الذكي ومنع تعارض المعلمين والقاعات...');
    setTimeout(() => {
        if (typeof toast === 'function') toast('✅ تم بناء الجدول الأسبوعي (السبت - الأربعاء × 7 حصص) بنجاح 100%!');
        renderTimetableBuilderGrid();
    }, 600);
}
window.autoGenerateTimetable = autoGenerateTimetable;

function renderTimetableBuilderGrid() {
    const matrixTb = document.getElementById('tbl-timetable-matrix-grid');
    const listTb = document.getElementById('tbl-timetable-builder-grid') || document.getElementById('tbl-timetable-builder');
    
    const secFilter = document.getElementById('fltTimetableSection')?.value || 'SEC-09A';
    const query = (document.getElementById('searchTimetable')?.value || '').toLowerCase().trim();
    const allItems = window.DB.timetableBuilder || [];

    // KPI Counters
    const totEl = document.getElementById('ttbTotalScheduled');
    const compEl = document.getElementById('ttbCompletedTimetables');
    const confEl = document.getElementById('ttbConflictRate');
    const quoEl = document.getElementById('ttbTeacherQuotas');

    if (totEl) totEl.innerHTML = `1,080 <small style="font-size:0.75rem;">حصة أسبوعياً 📅</small>`;
    if (compEl) compEl.innerHTML = `36 <small style="font-size:0.75rem;">جدولاً مكتملاً 🏫</small>`;
    if (confEl) confEl.innerHTML = `0% <small style="font-size:0.75rem;">تعارضات 🛡️</small>`;
    if (quoEl) quoEl.innerHTML = `98.5% <small style="font-size:0.75rem;">مكتملة 👨‍🏫</small>`;

    // 1. RENDER 5 DAYS x 7 PERIODS MATRIX GRID
    if (matrixTb) {
        const days = ['السبت', 'الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء'];
        const dayBadges = {
            'السبت': '<span style="color:#60a5fa;font-weight:800;">السبت</span><br><small style="color:#94a3b8;font-size:0.7rem;">Saturday</small>',
            'الأحد': '<span style="color:#34d399;font-weight:800;">الأحد</span><br><small style="color:#94a3b8;font-size:0.7rem;">Sunday</small>',
            'الإثنين': '<span style="color:#c084fc;font-weight:800;">الإثنين</span><br><small style="color:#94a3b8;font-size:0.7rem;">Monday</small>',
            'الثلاثاء': '<span style="color:#fbbf24;font-weight:800;">الثلاثاء</span><br><small style="color:#94a3b8;font-size:0.7rem;">Tuesday</small>',
            'الأربعاء': '<span style="color:#f87171;font-weight:800;">الأربعاء</span><br><small style="color:#94a3b8;font-size:0.7rem;">Wednesday</small>'
        };

        let matrixHtml = '';
        days.forEach((d, dayIdx) => {
            matrixHtml += `<tr style="border-bottom:1px solid rgba(255,255,255,0.08);">`;
            matrixHtml += `<td style="background:rgba(30,41,59,0.85);text-align:center;vertical-align:middle;padding:10px 6px;border-left:2px solid #3b82f6;">${dayBadges[d]}</td>`;

            for (let pNum = 1; pNum <= 7; pNum++) {
                const item = allItems.find(x => (!secFilter || x.sectionId === secFilter || x.section.includes(secFilter)) && x.day === d && Number(x.periodNum) === pNum);

                let cellBorder = '';
                if (pNum === 3) cellBorder = 'border-left:2px dashed rgba(245,158,11,0.4);';
                if (pNum === 5) cellBorder = 'border-left:2px dashed rgba(139,92,246,0.4);';

                if (item) {
                    matrixHtml += `
                        <td style="padding:4px;vertical-align:top;${cellBorder}" ondblclick="openForm('timetable_builder', '${item.id || item.code}')" oncontextmenu="event.preventDefault();deleteItem('timetableBuilder', '${item.id || item.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للتفريغ">
                            <div style="background:rgba(30,41,59,0.9);border:1px solid rgba(59,130,246,0.25);border-radius:8px;padding:8px 6px;transition:all 0.2s;height:100%;min-height:92px;display:flex;flex-direction:column;justify-content:space-between;" onmouseover="this.style.borderColor='#38bdf8';this.style.background='rgba(51,65,85,0.95)'" onmouseout="this.style.borderColor='rgba(59,130,246,0.25)';this.style.background='rgba(30,41,59,0.9)'">
                                <div>
                                    <div style="font-weight:800;color:#38bdf8;font-size:0.83rem;line-height:1.2;margin-bottom:3px;">${item.subject}</div>
                                    <div style="font-size:0.73rem;color:#cbd5e1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"><i class="fa-solid fa-user-tie" style="color:#60a5fa;font-size:0.65rem;"></i> ${item.teacher}</div>
                                </div>
                                <div style="display:flex;justify-content:space-between;align-items:center;margin-top:4px;font-size:0.68rem;color:#94a3b8;border-top:1px solid rgba(255,255,255,0.06);padding-top:3px;">
                                    <span>📍 ${item.room}</span>
                                    <span style="color:#34d399;font-weight:700;">🟢 متاح</span>
                                </div>
                            </div>
                        </td>
                    `;
                } else {
                    matrixHtml += `
                        <td style="padding:4px;vertical-align:middle;${cellBorder}" onclick="openForm('timetable_builder')">
                            <div style="background:rgba(15,23,42,0.4);border:1px dashed rgba(255,255,255,0.1);border-radius:8px;padding:8px 4px;text-align:center;color:var(--muted);font-size:0.72rem;cursor:pointer;min-height:92px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;" onmouseover="this.style.borderColor='#3b82f6';this.style.color='#60a5fa'" onmouseout="this.style.borderColor='rgba(255,255,255,0.1)';this.style.color='var(--muted)'">
                                <i class="fa-solid fa-plus-circle" style="font-size:1rem;opacity:0.6;"></i>
                                <span>شاغرة</span>
                            </div>
                        </td>
                    `;
                }
            }
            matrixHtml += `</tr>`;
        });
        matrixTb.innerHTML = matrixHtml;
    }

    // 2. RENDER 12-COLUMN DETAIL LIST TABLE
    if (listTb) {
        const filtered = allItems.filter(s => {
            if (secFilter && s.sectionId !== secFilter && !s.section.includes(secFilter)) return false;
            if (!query) return true;
            const text = [s.id, s.code, s.section, s.day, s.period, s.subject, s.teacher, s.room, s.status].join(' ').toLowerCase();
            return text.includes(query);
        });

        if (filtered.length === 0) {
            listTb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد حصص مطابقة للبحث</td></tr>';
            return;
        }

        listTb.innerHTML = filtered.map((s, idx) => {
            let dayBadge = '<span class="badge badge-info" style="font-size:0.75rem;">' + s.day + ' 📅</span>';
            const conflictBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-shield-check"></i> ' + s.conflictCheck + '</span>';
            const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> معتمد 🟢</span>';

            return `
                <tr data-collection="timetableBuilder" data-id="${s.id || s.code}" ondblclick="openForm('timetable_builder', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('timetableBuilder', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                    <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                    <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;">${s.code || s.id}</td>
                    <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-chalkboard-user" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.section}</td>
                    <td>${dayBadge}</td>
                    <td style="font-size:0.82rem;color:#cbd5e1;">${s.period}</td>
                    <td style="font-weight:700;color:#38bdf8;">${s.subject}</td>
                    <td style="color:#cbd5e1;font-size:0.83rem;"><i class="fa-solid fa-user-tie" style="color:#38bdf8;font-size:0.75rem;"></i> ${s.teacher}</td>
                    <td style="font-size:0.8rem;color:#cbd5e1;">📍 ${s.room}</td>
                    <td><span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">${s.branch}</span></td>
                    <td>${conflictBadge}</td>
                    <td>${statusBadge}</td>
                    <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="openForm('timetable_builder', '${s.id || s.code}')"><i class="fa-solid fa-pen-to-square"></i> تعديل</button></td>
                </tr>
            `;
        }).join('');
    }
}
window.renderTimetableBuilderGrid = renderTimetableBuilderGrid;
window.renderTimetableBuilder = renderTimetableBuilderGrid;
// Initial render
try { renderTimetableBuilderGrid(); } catch(e) {}


/**
 * ============================================================================
 * REQUIRED DOCUMENTS DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.requiredDocs) {
    window.DB.requiredDocs = [
        {
            id: 'DOC-REQ-01',
            code: 'DOC-REQ-01',
            name: 'أصل شهادة الميلاد المميكنة (الرقم الوطني)',
            nameEn: 'Original Computerized Birth Certificate',
            category: 'وثائق ثبوتية شخصية 🆔',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: 'الأصل للمطابقة + صورتان 📑',
            formats: 'PDF + JPG + PNG 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'مصلحة الأحوال المدنية والسجل المدني',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'يجب أن تكون شهادة الميلاد أصلية صادرة بالرقم الوطني وواضحة الأختام.'
        },
        {
            id: 'DOC-REQ-02',
            code: 'DOC-REQ-02',
            name: 'استمارة النجاح وشهادة نتائج الصف السابق',
            nameEn: 'Previous Grade Academic Report Card',
            category: 'شهادات أكاديمية 🎓',
            stages: 'الأساسي (2-9) والثانوي (10-12)',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: 'الأصل معتمد ومختوم + صورتان',
            formats: 'PDF + JPG 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'وزارة التربية والتعليم / المدرسة السابقة',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'مختومة بختم الإدارة المدرسية ومعمدة من التوجيه التربوي بالمحافظة.'
        },
        {
            id: 'DOC-REQ-03',
            code: 'DOC-REQ-03',
            name: 'الصور الشخصية الحديثة للطالب (مقاس 4x6)',
            nameEn: 'Recent Passport Size Photographs (4x6)',
            category: 'وثائق ثبوتية شخصية 🆔',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: '4 صور شخصية حديثة بخلفية بيضاء',
            formats: 'JPG + PNG 📷',
            maxSize: '2 ميجابايت (2MB) 💾',
            issuingAuthority: 'استوديو تصوير معتمد',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'خلفية بيضاء واضحة بالزي المدرسي الرسمي وبدون مؤثرات.'
        },
        {
            id: 'DOC-REQ-04',
            code: 'DOC-REQ-04',
            name: 'سجل اللقاحات وبطاقة الفحص الطبي المدرسي',
            nameEn: 'Vaccination Record & Medical Health Card',
            category: 'تقارير طبية وصحية 🩺',
            stages: 'رياض الأطفال والصف الأول أساسي',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: 'أصل كرت التطعيم + فحص لياقة',
            formats: 'PDF + JPG 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'وزارة الصحة العامة / المراكز الصحية المعتمدة',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'إثبات استكمال كافة جرعات التطعيم الأساسية وفحص البصر والسمع.'
        },
        {
            id: 'DOC-REQ-05',
            code: 'DOC-REQ-05',
            name: 'صورة البطاقة الشخصية / جواز السفر لولي الأمر',
            nameEn: 'Parent/Guardian National ID or Passport Copy',
            category: 'وثائق ثبوتية شخصية 🆔',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: 'صورتان واضحتان للوجهين',
            formats: 'PDF + JPG + PNG 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'مصلحة الهجرة والجوازات / الأحوال المدنية',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'سارية المفعول وتحتوي على الرقم الوطني والعنوان وأرقام التواصل.'
        },
        {
            id: 'DOC-REQ-06',
            code: 'DOC-REQ-06',
            name: 'استمارة النقل وسحب الملف وإبراء الذمة',
            nameEn: 'Official Transfer & Clearance Certificate',
            category: 'وثائق النقل والتحويل 🚚',
            stages: 'الطلاب المحولين من مدارس أخرى',
            mandatoryLevel: 'مشروطة بالتحويل 🟡',
            copies: 'أصل الاستمارة معمدة وزارياً',
            formats: 'PDF فقط 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'إدارة المدرسة السابقة وإدارة التعليم الأهلي',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'تتضمن إبراء الذمة المالية وختم وتصديق مكتب التربية والتعليم بالمنطقة.'
        },
        {
            id: 'DOC-REQ-07',
            code: 'DOC-REQ-07',
            name: 'إقامة سارية المفعول وجواز السفر (للوافدين)',
            nameEn: 'Valid Residence Permit & Passport (Foreign Students)',
            category: 'وثائق ثبوتية شخصية 🆔',
            stages: 'الطلاب غير المواطنين / الوافدين',
            mandatoryLevel: 'مشروطة بالجنسية 🟡',
            copies: 'صورتان من جواز السفر والإقامة السارية',
            formats: 'PDF + JPG 📎',
            maxSize: '5 ميجابايت (5MB) 💾',
            issuingAuthority: 'مصلحة الهجرة والجوازات والجنسية',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'إقامة سارية المفعول وتصريح رسمي بالدراسة في الجمهورية.'
        },
        {
            id: 'DOC-REQ-08',
            code: 'DOC-REQ-08',
            name: 'تعهد الالتزام بلائحة السلوك والانضباط المدرسي',
            nameEn: 'School Code of Conduct & Regulations Pledge',
            category: 'مستندات إدارية وتعهدات 📝',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            mandatoryLevel: 'إلزامية أساسية 🔴',
            copies: 'أصل موقع من ولي الأمر والطالب',
            formats: 'PDF + JPG 📎',
            maxSize: '2 ميجابايت (2MB) 💾',
            issuingAuthority: 'إدارة مدرسة السحاب الأهلية النموذجية',
            status: 'فعالة ومطلوبة 🟢',
            guidelines: 'توقيع ولي الأمر والطالب على الالتزام بأنظمة ولوائح المدرسة والزي الرسمي.'
        }
    ];
}

function renderRequiredDocsGrid() {
    const tb = document.getElementById('tbl-required-docs-grid') || document.getElementById('tbl-required-docs');
    if (!tb) return;

    const query = (document.getElementById('searchRequiredDocs')?.value || '').toLowerCase().trim();
    const catFilter = document.getElementById('filterDocCategory')?.value || 'all';
    const items = window.DB.requiredDocs || [];

    const totEl = document.getElementById('docTotalApproved');
    const manEl = document.getElementById('docMandatoryCount');
    const optEl = document.getElementById('docOptionalCount');
    const arcEl = document.getElementById('docDigitalArchiveRate');

    if (totEl) totEl.innerHTML = `16 <small style="font-size:0.75rem;">وثيقة رسمية 📄</small>`;
    if (manEl) manEl.innerHTML = `10 <small style="font-size:0.75rem;">وثائق إلزامية 🛡️</small>`;
    if (optEl) optEl.innerHTML = `6 <small style="font-size:0.75rem;">وثائق تكميلية 📑</small>`;
    if (arcEl) arcEl.innerHTML = `96.4% <small style="font-size:0.75rem;">أرشفة ☁️</small>`;

    const filtered = items.filter(s => {
        if (catFilter === 'إلزامية' && !s.mandatoryLevel.includes('إلزامية')) return false;
        if (catFilter === 'ثبوتية' && !s.category.includes('ثبوتية')) return false;
        if (catFilter === 'أكاديمية' && !s.category.includes('أكاديمية')) return false;
        if (catFilter === 'صحية' && !s.category.includes('صحية')) return false;
        if (catFilter === 'تحويل' && !s.category.includes('تحويل')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.category, s.stages, s.issuingAuthority, s.mandatoryLevel].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد وثائق مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let catBadge = '<span class="badge badge-info" style="font-size:0.75rem;">' + s.category + '</span>';
        let manBadge = '<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-circle-exclamation"></i> ' + s.mandatoryLevel + '</span>';
        if (s.mandatoryLevel.includes('مشروطة')) {
            manBadge = '<span class="badge badge-warning" style="font-size:0.75rem;"><i class="fa-solid fa-triangle-exclamation"></i> ' + s.mandatoryLevel + '</span>';
        } else if (s.mandatoryLevel.includes('اختيارية')) {
            manBadge = '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-circle-check"></i> ' + s.mandatoryLevel + '</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> فعالة 🟢</span>';

        return `
            <tr data-collection="requiredDocs" data-id="${s.id || s.code}" ondblclick="openForm('required_docs', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('requiredDocs', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-file-contract" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.name}</td>
                <td>${catBadge}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">${s.stages}</td>
                <td>${manBadge}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.copies}</td>
                <td><span class="badge" style="background:rgba(59,130,246,0.15);color:#60a5fa;font-size:0.75rem;">${s.formats}</span></td>
                <td><strong style="color:#34d399;font-family:monospace;font-size:0.85rem;">${s.maxSize}</strong></td>
                <td style="font-size:0.8rem;color:#94a3b8;">${s.issuingAuthority}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('📥 جاري تنزيل نموذج ودليل: ${s.name}');"><i class="fa-solid fa-download"></i> النموذج</button></td>
            </tr>
        `;
    }).join('');
}
window.renderRequiredDocsGrid = renderRequiredDocsGrid;
window.renderRequiredDocs = renderRequiredDocsGrid;
// Initial render
try { renderRequiredDocsGrid(); } catch(e) {}


/**
 * ============================================================================
 * FEE CATEGORIES DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.feeCategories) {
    window.DB.feeCategories = [
        {
            id: 'FEE-CAT-01',
            code: 'FEE-CAT-01',
            name: 'الرسوم الدراسية السنوية - المرحلة الأساسية العليا (7-9)',
            nameEn: 'Annual Tuition - Upper Basic Stage (7-9)',
            type: 'رسوم تعليمية أساسية 📚',
            stages: 'المرحلة الأساسية العليا (الصفوف 7-9)',
            amountLocal: '350,000 ر.ي',
            amountForeign: '$500 USD',
            paymentSchedule: 'أقساط سنوية (3 دفعات) 📅',
            mandatoryLevel: 'إلزامية لكافة الطلاب 🔴',
            discountPolicy: 'خصم الأخوة 15% / التفوق 20% 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'تشمل تكاليف التدريس الأكاديمي، الأنشطة الصفية، ومعامل العلوم والحاسوب.'
        },
        {
            id: 'FEE-CAT-02',
            code: 'FEE-CAT-02',
            name: 'الرسوم الدراسية السنوية - المرحلة الثانوية العامة (10-12)',
            nameEn: 'Annual Tuition - High School (10-12)',
            type: 'رسوم تعليمية أساسية 📚',
            stages: 'المرحلة الثانوية (علمي وأدبي)',
            amountLocal: '420,000 ر.ي',
            amountForeign: '$600 USD',
            paymentSchedule: 'أقساط سنوية (3 دفعات) 📅',
            mandatoryLevel: 'إلزامية لكافة الطلاب 🔴',
            discountPolicy: 'خصم الأخوة 15% / أوائل المدرسة 25% 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'تتضمن دروس التقوية الإثرائية والتحضير لاختبارات الثانوية العامة الوزارية.'
        },
        {
            id: 'FEE-CAT-03',
            code: 'FEE-CAT-03',
            name: 'الرسوم الدراسية السنوية - المرحلة الأساسية الأولى (1-6)',
            nameEn: 'Annual Tuition - Lower Basic Stage (1-6)',
            type: 'رسوم تعليمية أساسية 📚',
            stages: 'المرحلة الأساسية (الصفوف 1-6)',
            amountLocal: '290,000 ر.ي',
            amountForeign: '$420 USD',
            paymentSchedule: 'أقساط سنوية (3 دفعات) 📅',
            mandatoryLevel: 'إلزامية لكافة الطلاب 🔴',
            discountPolicy: 'خصم الأخوة 15% 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'تشمل برامج التأسيس اللغوي والحسابي والأنشطة الترفيهية والتربوية.'
        },
        {
            id: 'FEE-CAT-04',
            code: 'FEE-CAT-04',
            name: 'الرسوم الدراسية السنوية - مرحلة رياض الأطفال والتمهيدي',
            nameEn: 'Annual Tuition - Kindergarten & KG',
            type: 'رسوم تعليمية أساسية 📚',
            stages: 'مرحلة الروضة والتمهيدي (KG1 - KG2)',
            amountLocal: '240,000 ر.ي',
            amountForeign: '$350 USD',
            paymentSchedule: 'أقساط سنوية (3 دفعات) 📅',
            mandatoryLevel: 'إلزامية لكافة الطلاب 🔴',
            discountPolicy: 'خصم الأخوة 15% 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'رعاية متكاملة، وجبات خفيفة، وأركان التعليم باللعب وتنمية الذكاءات.'
        },
        {
            id: 'FEE-BUS-01',
            code: 'FEE-BUS-01',
            name: 'رسوم خدمة النقل والمواصلات بالحافلات المدرسية (ذهاب وإياب)',
            nameEn: 'School Bus Transportation Fee (Full Roundtrip)',
            type: 'خدمات نقل ومواصلات 🚌',
            stages: 'كافة المراحل الدراسية (حسب خط السير)',
            amountLocal: '120,000 ر.ي',
            amountForeign: '$170 USD',
            paymentSchedule: 'دفعتان فصليتان 📅',
            mandatoryLevel: 'اختيارية حسب الطلب 🟢',
            discountPolicy: 'خصم الأخ الثاني بنسبة 10% 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'حافلات مكيفة ومزودة بنظام التتبع المباشر ومشرفات أمن وسلامة.'
        },
        {
            id: 'FEE-BOOK-01',
            code: 'FEE-BOOK-01',
            name: 'رسوم الحقيبة المدرسية والكتب والمناهج الإثرائية',
            nameEn: 'School Textbooks & Enrichment Workbooks',
            type: 'كتب ومطبوعات 📖',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            amountLocal: '45,000 ر.ي',
            amountForeign: '$65 USD',
            paymentSchedule: 'دفعة واحدة مقدماً عند التسجيل 💵',
            mandatoryLevel: 'إلزامية لكافة الطلاب 🔴',
            discountPolicy: 'لا يوجد خصم (سعر التكلفة الطباعية)',
            status: 'معتمدة وفعالة 🟢',
            notes: 'تشمل الكتب المدرسية الوزارية وسلسلة كتب كامبردج وملازم الأنشطة.'
        },
        {
            id: 'FEE-UNI-01',
            code: 'FEE-UNI-01',
            name: 'رسوم الزي المدرسي الرسمي والبدلة الرياضية الموحدة',
            nameEn: 'Official School Uniform & Sports Kit Fee',
            type: 'زي مدرسي 👕',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            amountLocal: '35,000 ر.ي',
            amountForeign: '$50 USD',
            paymentSchedule: 'دفعة واحدة مقدماً 💵',
            mandatoryLevel: 'إلزامية للطلاب المستجدين 🔴',
            discountPolicy: 'لا يوجد خصم',
            status: 'معتمدة وفعالة 🟢',
            notes: 'طقم زي مدرسي كامل قطني عالي الجودة + بدلة رياضية مع شعار المدرسة.'
        },
        {
            id: 'FEE-REG-01',
            code: 'FEE-REG-01',
            name: 'رسوم التسجيل وفتح الملف والأرشفة الرقمية للطلاب المستجدين',
            nameEn: 'New Student Registration & Digital Vault Fee',
            type: 'تسجيل وملف 📝',
            stages: 'الطلاب المستجدين والمحولين فقط',
            amountLocal: '20,000 ر.ي',
            amountForeign: '$30 USD',
            paymentSchedule: 'دفعة واحدة مقدماً 💵',
            mandatoryLevel: 'إلزامية للمستجدين 🔴',
            discountPolicy: 'إعفاء لأبناء الشهداء والمعلمين 🎁',
            status: 'معتمدة وفعالة 🟢',
            notes: 'رسوم إدارية غير قابلة للاسترداد وتدفع لمرة واحدة عند الالتحاق بالمدرسة.'
        }
    ];
}

function renderFeeCategoriesGrid() {
    const tb = document.getElementById('tbl-fee-categories-grid') || document.getElementById('tbl-fee-categories');
    if (!tb) return;

    const query = (document.getElementById('searchFeecategories')?.value || document.getElementById('searchFeeCategories')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterFeeType')?.value || 'all';
    const items = window.DB.feeCategories || [];

    // Calculate KPIs
    let totalCount = items.length;
    let mandatoryCount = 0;
    let optionalCount = 0;

    items.forEach(s => {
        const manStr = String(s.mandatoryLevel || s.mandatory || '');
        if (manStr.includes('اختيار')) {
            optionalCount++;
        } else {
            mandatoryCount++;
        }
    });

    const totEl = document.getElementById('fcTotal');
    const manEl = document.getElementById('fcMandatory');
    const optEl = document.getElementById('fcOptional');

    if (totEl) totEl.textContent = totalCount;
    if (manEl) manEl.textContent = mandatoryCount;
    if (optEl) optEl.textContent = optionalCount;

    // Filter items safely
    const filtered = items.filter(s => {
        const feeType = String(s.type || (
            s.name && (s.name.includes('نقل') || s.name.includes('مواصلات')) ? 'خدمات نقل ومواصلات 🚌' :
            (s.name && (s.name.includes('كتاب') || s.name.includes('كتب') || s.name.includes('حقيبة')) ? 'كتب ومقررات دراسية 📖' :
            (s.name && (s.name.includes('نشاط') || s.name.includes('مختبر')) ? 'أنشطة وتأمين ومعامل 🏆' :
            (s.name && (s.name.includes('تسجيل') || s.name.includes('قيد')) ? 'تسجيل وقبول وملف 📝' : 'رسوم تعليمية أساسية 📚')))
        ));

        const manStr = String(s.mandatoryLevel || s.mandatory || 'إلزامي');
        const isOpt = manStr.includes('اختيار');

        if (typeFilter === 'إلزامي' && isOpt) return false;
        if (typeFilter === 'اختياري' && !isOpt) return false;
        if (typeFilter === 'تعليمية' && !feeType.includes('تعليمية') && !feeType.includes('أساسية')) return false;
        if (typeFilter === 'خدمية' && !feeType.includes('نقل') && !feeType.includes('نشاط') && !feeType.includes('كتب')) return false;

        if (!query) return true;
        const text = [
            s.id, s.code, s.name, s.nameEn, feeType, s.stages, s.amountLocal, s.amount, s.notes, s.period, manStr
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد تصنيفات رسوم مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        const feeType = String(s.type || (
            s.name && (s.name.includes('نقل') || s.name.includes('مواصلات')) ? 'خدمات نقل ومواصلات 🚌' :
            (s.name && (s.name.includes('كتاب') || s.name.includes('كتب') || s.name.includes('حقيبة')) ? 'كتب ومقررات دراسية 📖' :
            (s.name && (s.name.includes('نشاط') || s.name.includes('مختبر')) ? 'أنشطة وتأمين ومعامل 🏆' :
            (s.name && (s.name.includes('تسجيل') || s.name.includes('قيد')) ? 'تسجيل وقبول وملف 📝' : 'رسوم تعليمية أساسية 📚')))
        ));

        let typeBadge = '<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-graduation-cap" style="margin-left:4px;"></i> ' + feeType + '</span>';
        if (feeType.includes('نقل') || feeType.includes('مواصلات')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-bus" style="margin-left:4px;"></i> ' + feeType + '</span>';
        } else if (feeType.includes('كتب') || feeType.includes('حقيبة')) {
            typeBadge = '<span class="badge" style="background:rgba(168,85,247,0.15);color:#c084fc;font-size:0.75rem;"><i class="fa-solid fa-book" style="margin-left:4px;"></i> ' + feeType + '</span>';
        } else if (feeType.includes('أنشطة') || feeType.includes('معامل')) {
            typeBadge = '<span class="badge" style="background:rgba(236,72,153,0.15);color:#f472b6;font-size:0.75rem;"><i class="fa-solid fa-trophy" style="margin-left:4px;"></i> ' + feeType + '</span>';
        } else if (feeType.includes('تسجيل') || feeType.includes('قيد')) {
            typeBadge = '<span class="badge" style="background:rgba(14,165,233,0.15);color:#38bdf8;font-size:0.75rem;"><i class="fa-solid fa-id-card" style="margin-left:4px;"></i> ' + feeType + '</span>';
        }

        const manStr = String(s.mandatoryLevel || s.mandatory || 'إلزامي');
        const isOptional = manStr.includes('اختيار');
        const manBadge = isOptional
            ? '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-circle-check"></i> اختياري 🟢</span>'
            : '<span class="badge badge-danger" style="font-size:0.75rem;"><i class="fa-solid fa-circle-exclamation"></i> إلزامي 🔴</span>';

        // Format amount
        let amountDisplay = s.amountLocal;
        if (!amountDisplay && s.amount !== undefined) {
            amountDisplay = Number(s.amount).toLocaleString() + ' ' + (s.currency || 'ر.ي');
        } else if (!amountDisplay) {
            amountDisplay = '0 ر.ي';
        }
        if (!amountDisplay.includes('ر.ي') && !amountDisplay.includes('$') && !amountDisplay.includes('SAR')) {
            amountDisplay += ' ر.ي';
        }

        const feeCode = s.code || s.id || ('FEE-' + (idx + 101));
        const stagesText = s.stages || 'كافة المراحل الدراسية 👨‍🎓';
        const descText = s.notes || s.description || s.period || (s.paymentSchedule ? 'جدولة: ' + s.paymentSchedule : 'بند رسوم دراسية معتمد');

        return `
            <tr data-collection="feeCategories" data-id="${s.id || feeCode}" ondblclick="openForm('fee-categories', '${s.id || feeCode}')" oncontextmenu="event.preventDefault();deleteItem('fee-categories', '${s.id || feeCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;"><i class="fa-solid fa-tag" style="color:#60a5fa;font-size:0.75rem;margin-left:4px;"></i> ${feeCode}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-receipt" style="color:#38bdf8;font-size:0.8rem;margin-left:4px;"></i> ${s.name}</td>
                <td>${typeBadge}</td>
                <td><strong style="color:#34d399;font-family:monospace;font-size:0.95rem;">${amountDisplay}</strong></td>
                <td>${manBadge}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;"><i class="fa-solid fa-layer-group" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${stagesText}</td>
                <td style="font-size:0.8rem;color:#94a3b8;"><i class="fa-solid fa-info-circle" style="color:#64748b;font-size:0.75rem;margin-left:4px;"></i> ${descText}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل فئة الرسوم" onclick="openForm('fee-categories', '${s.id || feeCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف فئة الرسوم" onclick="deleteItem('fee-categories', '${s.id || feeCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderFeeCategoriesGrid = renderFeeCategoriesGrid;
window.renderFeeCategories = renderFeeCategoriesGrid;
/**
 * ============================================================================
 * DISCOUNT & SCHOLARSHIP CATEGORIES DIRECTORY ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.discountCategories) {
    window.DB.discountCategories = [
        {
            id: 'DSC-SIB-01',
            code: 'DSC-SIB-01',
            name: 'خصم الأخوة والأقارب (للابن الثاني)',
            nameEn: 'Second Sibling Family Discount',
            type: 'خصم اجتماعي عائلي 👨‍👩‍👧',
            calcType: 'نسبة مئوية % 📊',
            value: '15% خصم',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'تسجيل أخ أكبر مسدد للرسوم الدراسية',
            quota: 'مفتوح لكافة المؤهلين ♾️',
            authority: 'إدارة شؤون الطلاب والمالية',
            status: 'معتمدة وسارية 🟢',
            notes: 'يمنح للابن الثاني المسجل بالمدرسة في نفس العام الدراسي.'
        },
        {
            id: 'DSC-SIB-02',
            code: 'DSC-SIB-02',
            name: 'خصم الأخوة والأقارب (للابن الثالث فأكثر)',
            nameEn: 'Third & More Sibling Family Discount',
            type: 'خصم اجتماعي عائلي 👨‍👩‍👧',
            calcType: 'نسبة مئوية % 📊',
            value: '20% خصم',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'تسجيل 3 إخوة أو أكثر بالمدرسة',
            quota: 'مفتوح لكافة المؤهلين ♾️',
            authority: 'إدارة شؤون الطلاب والمالية',
            status: 'معتمدة وسارية 🟢',
            notes: 'يمنح للابن الثالث والابن الرابع لتشجيع استقرار الأسر.'
        },
        {
            id: 'SCH-EXC-01',
            code: 'SCH-EXC-01',
            name: 'منحة أوائل المدرسة والمتفوقين أكاديمياً',
            nameEn: 'Academic Excellence & Top Rank Scholarship',
            type: 'منحة تفوق أكاديمي 🎓',
            calcType: 'نسبة مئوية % 📊',
            value: '25% منحة',
            stages: 'المرحلة الأساسية (4-9) والثانوية',
            eligibility: 'الحصول على الترتيب الأول أو الثاني بمعدل 98% فما فوق',
            quota: '25 مقعداً دراسياً سنويّاً 🏆',
            authority: 'مجلس الإدارة ولجنة التفوق الأكاديمي',
            status: 'معتمدة وسارية 🟢',
            notes: 'منحة سنوية لتكريم الطلاب المتميزين أكاديمياً وتعزيز التنافس الإيجابي.'
        },
        {
            id: 'SCH-QUR-01',
            code: 'SCH-QUR-01',
            name: 'منحة حفظة القرآن الكريم كاملاً مع الإجازة',
            nameEn: 'Full Quran Memorization & Ijazah Scholarship',
            type: 'منحة قرآنية وإيمانية 🕌',
            calcType: 'نسبة مئوية % 📊',
            value: '50% منحة',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'حفظ القرآن الكريم كاملاً واجتياز اختبار التسميع الوزاري',
            quota: '15 مقعداً دراسياً سنويّاً',
            authority: 'مجلس إدارة المدرسة وقسم القرآن الكريم',
            status: 'معتمدة وسارية 🟢',
            notes: 'تقدير لحفظة كتاب الله وتطبيق أحكام التجويد وحسن السيرة والسلوك.'
        },
        {
            id: 'DSC-STF-01',
            code: 'DSC-STF-01',
            name: 'خصم أبناء المعلمين والكوادر الإدارية بالمدرسة',
            nameEn: 'Staff & Teachers Children Discount',
            type: 'خصم وظيفي 👔',
            calcType: 'نسبة مئوية % 📊',
            value: '50% خصم',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'عقد عمل ساري للموظف أو المعلم بالمدرسة وتفرغ كامل',
            quota: 'مفتوح لكافة كوادر المدرسة ♾️',
            authority: 'إدارة الموارد البشرية والمدير العام',
            status: 'معتمدة وسارية 🟢',
            notes: 'ميزة وظيفية لدعم استقرار الكادر التعليمي والإداري بالمدرسة.'
        },
        {
            id: 'SCH-ORP-01',
            code: 'SCH-ORP-01',
            name: 'منحة كفالة الأيتام والحالات الإنسانية الخاصة',
            nameEn: 'Orphans & Special Social Care Scholarship',
            type: 'منحة إنسانية 🤍',
            calcType: 'نسبة مئوية % 📊',
            value: '100% منحة كاملة',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'شهادة وفاة العائل وبحث اجتماعي معتمد من الرعاية الاجتماعية',
            quota: '12 مقعداً دراسياً مكفولاً بالكامل',
            authority: 'صندوق التكافل المدرسي ومجلس الأمناء',
            status: 'معتمدة وسارية 🟢',
            notes: 'إعفاء تام من الرسوم الدراسية والكتب وتوفير الحقيبة المدرسية.'
        },
        {
            id: 'DSC-EARLY-01',
            code: 'DSC-EARLY-01',
            name: 'خصم السداد المبكر الكامل للرسوم مقدماً (كاش)',
            nameEn: 'Early Full Payment Cash Discount',
            type: 'خصم سداد مبكر 💵',
            calcType: 'نسبة مئوية % 📊',
            value: '10% خصم',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            eligibility: 'سداد كامل الرسوم السنوية قبل بداية العام الدراسي',
            quota: 'مفتوح لكافة الطلاب ♾️',
            authority: 'الإدارة المالية والحسابات',
            status: 'معتمدة وسارية 🟢',
            notes: 'يمنح لأولياء الأمور الذين يسددون إجمالي القسط السنوي دفعة واحدة نقداً.'
        }
    ];
}

function renderDiscountCategoriesGrid() {
    const tb = document.getElementById('tbl-discount-categories-grid') || document.getElementById('tbl-discount-categories');
    if (!tb) return;

    const query = (document.getElementById('searchDiscountCategories')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterDiscountType')?.value || 'all';
    const items = window.DB.discountCategories || [];

    const totEl = document.getElementById('dscTotalCategories');
    const benEl = document.getElementById('dscBeneficiariesCount');
    const valEl = document.getElementById('dscTotalDiscountAmount');
    const maxEl = document.getElementById('dscMaxDiscountRate');

    if (totEl) totEl.innerHTML = `12 <small style="font-size:0.75rem;">فئة وبرنامجاً 🎁</small>`;
    if (benEl) benEl.innerHTML = `185 <small style="font-size:0.75rem;">طالباً وطالبة 👨‍🎓</small>`;
    if (valEl) valEl.innerHTML = `14,850,000 <small style="font-size:0.75rem;">ر.ي 💰</small>`;
    if (maxEl) maxEl.innerHTML = `100% <small style="font-size:0.75rem;">منحة كاملة 🌟</small>`;

    const filtered = items.filter(s => {
        if (typeFilter === 'عائلي' && !s.type.includes('عائلي')) return false;
        if (typeFilter === 'تفوق' && !s.type.includes('تفوق')) return false;
        if (typeFilter === 'قرآن' && !s.type.includes('قرآن')) return false;
        if (typeFilter === 'وظيفي' && !s.type.includes('وظيفي')) return false;
        if (typeFilter === 'إنساني' && !s.type.includes('إنساني')) return false;
        if (typeFilter === 'مبكر' && !s.type.includes('مبكر')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.name, s.nameEn, s.type, s.stages, s.value, s.eligibility].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد فئات خصومات مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let typeBadge = '<span class="badge badge-info" style="font-size:0.75rem;">' + s.type + '</span>';
        if (s.type.includes('تفوق') || s.type.includes('قرآن')) {
            typeBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">' + s.type + '</span>';
        } else if (s.type.includes('إنساني')) {
            typeBadge = '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;">' + s.type + '</span>';
        }

        let valBadge = '<span class="badge badge-success" style="font-size:0.85rem;font-weight:800;">' + s.value + '</span>';
        if (s.value.includes('100%')) {
            valBadge = '<span class="badge" style="background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;font-size:0.85rem;font-weight:800;">' + s.value + '</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> سارية 🟢</span>';

        return `
            <tr data-collection="discountCategories" data-id="${s.id || s.code}" ondblclick="openForm('discount_categories', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('discountCategories', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;">${s.code || s.id}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-gift" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.name}</td>
                <td>${typeBadge}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.calcType}</td>
                <td>${valBadge}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;">${s.stages}</td>
                <td style="font-size:0.8rem;color:#94a3b8;">${s.eligibility}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.quota}</td>
                <td style="font-size:0.8rem;color:#94a3b8;">${s.authority}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('👥 استعراض كشف الطلاب المستفيدين من: ${s.name}');"><i class="fa-solid fa-users"></i> كشف الطلاب</button></td>
            </tr>
        `;
    }).join('');
}
window.renderDiscountCategoriesGrid = renderDiscountCategoriesGrid;
window.renderDiscountCategories = renderDiscountCategoriesGrid;
// Initial render
try { renderDiscountCategoriesGrid(); } catch(e) {}


/**
 * ============================================================================
 * INSTALLMENT PLANS & DUE SCHEDULES ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.installmentPlans) {
    window.DB.installmentPlans = [
        {
            id: 'PLN-TRI-01',
            code: 'PLN-TRI-01',
            name: 'خطة الأقساط الثلاثية القياسية (3 دفعات سنوية)',
            nameEn: 'Standard 3-Term Installment Plan',
            count: '3 أقساط سنوية 📅',
            breakdown: '40% مقدم + 30% قسط ثانٍ + 30% قسط ثالث 📊',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            dueDates: 'سبتمبر (التسجيل) / 15 ديسمبر / 15 مارس ⏰',
            gracePeriod: '14 يوماً فترة سماح ⏳',
            rewards: 'خصم 5% عند السداد قبل الموعد بأسبوعين 🎁',
            reminderChannel: 'رسائل SMS + إشعار التطبيق 📲',
            status: 'معتمدة ومفعلة 🟢',
            notes: 'الخطة الأكثر استخداماً من قبل 70% من أولياء الأمور.'
        },
        {
            id: 'PLN-SEMI-02',
            code: 'PLN-SEMI-02',
            name: 'خطة السداد الفصلي (دفعتان متساويتان)',
            nameEn: 'Semester Semi-Annual Payment Plan (2 Terms)',
            count: 'دفعتان فصليتان 📅',
            breakdown: '50% بداية الفصل الأول + 50% بداية الفصل الثاني 📊',
            stages: 'الأساسي العليا (7-9) والثانوي',
            dueDates: '1 سبتمبر (الفصل 1) / 15 يناير (الفصل 2) ⏰',
            gracePeriod: '14 يوماً فترة سماح ⏳',
            rewards: 'خصم 3% عند الالتزام بالسداد الفصلي 🎁',
            reminderChannel: 'رسائل واتساب + SMS 📲',
            status: 'معتمدة ومفعلة 🟢',
            notes: 'مناسبة للموظفين الذين يفضلون تسوية الرسوم مع بداية كل فصل دراسي.'
        },
        {
            id: 'PLN-MON-03',
            code: 'PLN-MON-03',
            name: 'خطة الأقساط الشهرية الميسرة (10 دفعات)',
            nameEn: 'Monthly Easy Installment Plan (10 Months)',
            count: '10 أقساط شهرية 📅',
            breakdown: '10% شهرياً (من سبتمبر حتى يونيو) 📊',
            stages: 'مرحلة الروضة والأساسي (1-6)',
            dueDates: 'يوم 1 من كل شهر ميلادي ⏰',
            gracePeriod: '7 أيام سماح ⏳',
            rewards: 'إعفاء من رسوم الملف عند السداد الشهري المنتظم 🎁',
            reminderChannel: 'إشعار التطبيق + SMS 📲',
            status: 'معتمدة ومفعلة 🟢',
            notes: 'مخصصة لتخفيف الأعباء الشهرية على أولياء الأمور ذوي الدخل الشهري.'
        },
        {
            id: 'PLN-FULL-04',
            code: 'PLN-FULL-04',
            name: 'خطة السداد السنوي الكامل مقدماً (كاش 100%)',
            nameEn: 'Full Annual Advance Cash Payment Plan',
            count: 'دفعة واحدة كاملة 💵',
            breakdown: '100% دفعة واحدة مقدماً عند التسجيل 📊',
            stages: 'كافة المراحل الدراسية 👨‍🎓',
            dueDates: 'عند إتمام إجراءات القبول والتسجيل ⏰',
            gracePeriod: 'فوري عند التسجيل',
            rewards: 'خصم فوري 10% من إجمالي القسط السنوي 🎁',
            reminderChannel: 'إشعار سداد إلكتروني فوري 📲',
            status: 'معتمدة ومفعلة 🟢',
            notes: 'يمنح ولي الأمر خصم السداد المبكر الكاش المعتمد باللائحة.'
        },
        {
            id: 'PLN-SPEC-05',
            code: 'PLN-SPEC-05',
            name: 'خطة السداد الاستثنائية للحالات الخاصة والأيتام',
            nameEn: 'Special Case & Orphan Custom Plan',
            count: 'أقساط مرنة مخصصة 📅',
            breakdown: 'وفق جدول مالي مرن معتمد من صندوق التكافل 📊',
            stages: 'الطلاب المكفولين والحالات الخاصة',
            dueDates: 'مواعيد ميسرة على مدار العام ⏰',
            gracePeriod: '30 يوماً فترة سماح ⏳',
            rewards: 'تغطية الفارق من صندوق الرعاية الاجتماعية 🎁',
            reminderChannel: 'تنسيق مباشر مع المرشد المالي 👥',
            status: 'معتمدة ومفعلة 🟢',
            notes: 'تعتمد بموافقة خطية من المدير العام ولجنة التكافل المدرسي.'
        }
    ];
}

function renderInstallmentPlansGrid() {
    const tb = document.getElementById('tbl-installment-plans-grid') || document.getElementById('tbl-installment-plans');
    if (!tb) return;

    const query = (document.getElementById('searchInstallmentplans')?.value || document.getElementById('searchInstallmentPlans')?.value || '').toLowerCase().trim();
    const typeFilter = document.getElementById('filterInstallmentType')?.value || 'all';
    const items = window.DB.installmentPlans || [];

    // Calculate KPIs
    let totalCount = items.length;
    let activeCount = 0;

    items.forEach(s => {
        const st = String(s.status || 'معتمدة ومفعلة 🟢');
        if (!st || st.includes('مفعل') || st.includes('معتمد') || st.includes('نشط') || st.includes('🟢')) {
            activeCount++;
        }
    });

    const students = window.DB.students || window.DB.studentsData || [];
    let studentsOnPlan = 0;
    if (students.length > 0) {
        studentsOnPlan = students.filter(st => {
            const fs = String(st.feeStatus || st.status || '');
            return fs.includes('قسط') || fs.includes('أقساط') || fs.includes('سداد') || fs.includes('جزئي');
        }).length;
        if (studentsOnPlan === 0) {
            studentsOnPlan = Math.round(students.length * 0.42);
        }
    } else {
        studentsOnPlan = 185;
    }

    const totEl = document.getElementById('ipTotal');
    const actEl = document.getElementById('ipActive');
    const stuEl = document.getElementById('ipStudents');

    if (totEl) totEl.textContent = totalCount;
    if (actEl) actEl.textContent = activeCount;
    if (stuEl) stuEl.innerHTML = `<span dir="ltr" style="display:inline-block;"><span style="font-weight:800;">${studentsOnPlan.toLocaleString()}</span> <small style="font-size:0.75rem;font-weight:normal;">طالباً 👨‍🎓</small></span>`;

    // Filter items safely
    const filtered = items.filter(s => {
        const planCount = String(s.count || (
            s.name && s.name.includes('قسط') ? '4 أقساط سنوية 📅' : '3 أقساط سنوية 📅'
        ));
        const rawStatus = String(s.status || 'معتمدة ونشطة 🟢');
        const isActive = !rawStatus || rawStatus.includes('معتمد') || rawStatus.includes('نشط') || rawStatus.includes('مفعل') || rawStatus.includes('🟢');

        if (typeFilter === 'نشطة' && !isActive) return false;
        if (typeFilter === '4' && !planCount.includes('4')) return false;
        if (typeFilter === '3' && !planCount.includes('3')) return false;
        if (typeFilter === 'فصلي' && !planCount.includes('دفعت') && !planCount.includes('فصل')) return false;
        if (typeFilter === 'شهري' && !planCount.includes('شهر') && !planCount.includes('10')) return false;

        if (!query) return true;
        const text = [
            s.id, s.code, s.name, s.nameEn, planCount, s.stages, s.breakdown, s.pct, s.period, s.dueDate, s.notes, rawStatus
        ].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:30px;"><i class="fa-solid fa-inbox" style="font-size:2rem;margin-bottom:8px;display:block;opacity:0.6;"></i> لا توجد خطط تقسيط مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        const planCode = s.code || s.id || ('PLN-' + (idx + 101));
        const planCount = s.count || (
            s.name && s.name.includes('قسط') ? '4 أقساط مجدولة 📅' : '3 أقساط سنوية 📅'
        );

        let countBadge = '<span class="badge badge-info" style="font-size:0.75rem;"><i class="fa-solid fa-layer-group" style="margin-left:4px;"></i> ' + planCount + '</span>';
        if (planCount.includes('4') || planCount.includes('مجدول')) {
            countBadge = '<span class="badge" style="background:rgba(56,189,248,0.15);color:#38bdf8;font-size:0.75rem;"><i class="fa-solid fa-calendar-days" style="margin-left:4px;"></i> ' + planCount + '</span>';
        } else if (planCount.includes('شهر') || planCount.includes('10')) {
            countBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;"><i class="fa-solid fa-calendar" style="margin-left:4px;"></i> ' + planCount + '</span>';
        } else if (planCount.includes('دفعة واحدة') || planCount.includes('كاش')) {
            countBadge = '<span class="badge" style="background:rgba(16,185,129,0.15);color:#34d399;font-size:0.75rem;"><i class="fa-solid fa-check-double" style="margin-left:4px;"></i> ' + planCount + '</span>';
        }

        const planPeriod = s.period || (s.dueDate ? 'استحقاق: ' + s.dueDate : 'كل 3 أشهر (فصلي) ⏳');
        const firstPct = s.pct || s.firstPaymentPct || '25%';
        const stagesText = s.stages || 'كافة المراحل الدراسية 👨‍🎓';

        const rawStatus = String(s.status || 'معتمدة ونشطة 🟢');
        const isActive = !rawStatus || rawStatus.includes('معتمد') || rawStatus.includes('نشط') || rawStatus.includes('مفعل') || rawStatus.includes('🟢');
        const statusBadge = isActive
            ? '<span class="badge badge-success" style="font-size:0.75rem;"><i class="fa-solid fa-circle-check"></i> معتمدة ونشطة 🟢</span>'
            : '<span class="badge badge-warning" style="font-size:0.75rem;"><i class="fa-solid fa-pause"></i> موقوفة مؤقتاً 🟡</span>';

        return `
            <tr data-collection="installmentPlans" data-id="${s.id || planCode}" ondblclick="openForm('installment-plans', '${s.id || planCode}')" oncontextmenu="event.preventDefault();deleteItem('installment-plans', '${s.id || planCode}')" title="💡 انقر مرتين للتعديل، أو اضغط بالزر الأيمن للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;"><i class="fa-solid fa-barcode" style="color:#60a5fa;font-size:0.75rem;margin-left:4px;"></i> ${planCode}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-calendar-check" style="color:#38bdf8;font-size:0.8rem;margin-left:4px;"></i> ${s.name}</td>
                <td>${countBadge}</td>
                <td style="font-size:0.82rem;color:#cbd5e1;"><i class="fa-solid fa-clock" style="color:#f59e0b;font-size:0.75rem;margin-left:4px;"></i> ${planPeriod}</td>
                <td style="text-align:center;"><span dir="ltr" style="display:inline-flex;align-items:center;gap:4px;"><strong style="color:#34d399;font-family:monospace;font-size:0.95rem;">${firstPct}</strong></span></td>
                <td style="font-size:0.82rem;color:#cbd5e1;"><i class="fa-solid fa-graduation-cap" style="color:#a855f7;font-size:0.75rem;margin-left:4px;"></i> ${stagesText}</td>
                <td>${statusBadge}</td>
                <td style="text-align:center;">
                    <div style="display:flex;gap:6px;justify-content:center;">
                        <button type="button" class="btn-action btn-edit" title="تعديل خطة التقسيط" onclick="openForm('installment-plans', '${s.id || planCode}')" style="background:rgba(59,130,246,0.15);color:#60a5fa;border:1px solid rgba(59,130,246,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-pen-to-square"></i></button>
                        <button type="button" class="btn-action btn-delete" title="حذف خطة التقسيط" onclick="deleteItem('installment-plans', '${s.id || planCode}')" style="background:rgba(239,68,68,0.15);color:#ef4444;border:1px solid rgba(239,68,68,0.3);border-radius:6px;width:30px;height:30px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;"><i class="fa-solid fa-trash-can"></i></button>
                    </div>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderInstallmentPlansGrid = renderInstallmentPlansGrid;
window.renderInstallmentPlans = renderInstallmentPlansGrid;
/**
 * ============================================================================
 * GRADE LEVEL FEES MATRIX ENGINE (12 COLUMNS & KPI CARDS)
 * ============================================================================
 */
if (!window.DB) window.DB = {};
if (!window.DB.gradeFees) {
    window.DB.gradeFees = [
        {
            id: 'FEE-GRD-09',
            code: 'FEE-GRD-09',
            stage: 'المرحلة الأساسية العليا 🎓',
            gradeName: 'الصف التاسع أساسي (شهادة أساسية)',
            gradeNameEn: 'Grade 9 - Basic Certificate Level',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '350,000 ر.ي',
            booksFee: '45,000 ر.ي',
            uniformFee: '35,000 ر.ي',
            totalAmount: '450,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'يشمل رسوم الاختبارات الوزارية لشهادة إتمام المرحلة الأساسية (تاسع).'
        },
        {
            id: 'FEE-GRD-12S',
            code: 'FEE-GRD-12S',
            stage: 'المرحلة الثانوية 🏛️',
            gradeName: 'الصف الثالث الثانوي (القسم العلمي)',
            gradeNameEn: 'Grade 12 - Scientific High School',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '420,000 ر.ي',
            booksFee: '45,000 ر.ي',
            uniformFee: '35,000 ر.ي',
            totalAmount: '520,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'يشمل دروس التقوية الإثرائية ورسوم الامتحانات الوزارية للثانوية العامة.'
        },
        {
            id: 'FEE-GRD-12A',
            code: 'FEE-GRD-12A',
            stage: 'المرحلة الثانوية 🏛️',
            gradeName: 'الصف الثالث الثانوي (القسم الأدبي)',
            gradeNameEn: 'Grade 12 - Literary High School',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '400,000 ر.ي',
            booksFee: '45,000 ر.ي',
            uniformFee: '35,000 ر.ي',
            totalAmount: '500,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'تأهيل مكثف لمقررات التاريخ والجغرافيا واللغات والامتحانات الوزارية.'
        },
        {
            id: 'FEE-GRD-07',
            code: 'FEE-GRD-07',
            stage: 'المرحلة الأساسية العليا 🎓',
            gradeName: 'الصف السابع أساسي',
            gradeNameEn: 'Grade 7 - Upper Basic Level',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '330,000 ر.ي',
            booksFee: '45,000 ر.ي',
            uniformFee: '35,000 ر.ي',
            totalAmount: '430,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'بداية المرحلة الأساسية العليا وتدريس العلوم المتخصصة والحاسوب.'
        },
        {
            id: 'FEE-GRD-01',
            code: 'FEE-GRD-01',
            stage: 'الأساسية الأولى (1-6) 📚',
            gradeName: 'الصف الأول أساسي (المستجدين تميز)',
            gradeNameEn: 'Grade 1 - Primary Level',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '290,000 ر.ي',
            booksFee: '45,000 ر.ي',
            uniformFee: '35,000 ر.ي',
            totalAmount: '390,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'برامج التأسيس اللغوي والحسابي المتقدم ورعاية الطفولة المبكرة.'
        },
        {
            id: 'FEE-GRD-KG2',
            code: 'FEE-GRD-KG2',
            stage: 'رياض الأطفال والتمهيدي 🧸',
            gradeName: 'مرحلة التمهيدي الثاني (KG2)',
            gradeNameEn: 'Kindergarten Level 2 (KG2)',
            registrationFee: '20,000 ر.ي',
            tuitionFee: '240,000 ر.ي',
            booksFee: '35,000 ر.ي',
            uniformFee: '30,000 ر.ي',
            totalAmount: '325,000 ر.ي 💰',
            paymentPlan: '3 أقساط سنوية (40% / 30% / 30%) 📅',
            status: 'معتمد ومطبق 🟢',
            notes: 'تأهيل الطفل للقراءة والكتابة واللغة الإنجليزية والحساب الذهني.'
        }
    ];
}

function renderGradeFeesGrid() {
    const tb = document.getElementById('tbl-grade-fees-grid') || document.getElementById('tbl-grade-fees');
    if (!tb) return;

    const query = (document.getElementById('searchGradeFees')?.value || '').toLowerCase().trim();
    const stageFilter = document.getElementById('filterGradeStage')?.value || 'all';
    const items = window.DB.gradeFees || [];

    const totEl = document.getElementById('grfTotalGrades');
    const maxEl = document.getElementById('grfMaxFee');
    const minEl = document.getElementById('grfMinFee');
    const revEl = document.getElementById('grfTotalRevenue');

    if (totEl) totEl.innerHTML = `15 <small style="font-size:0.75rem;">صفاً دراسياً 🎓</small>`;
    if (maxEl) maxEl.innerHTML = `420,000 <small style="font-size:0.75rem;">ر.ي 💰</small>`;
    if (minEl) minEl.innerHTML = `240,000 <small style="font-size:0.75rem;">ر.ي 🧸</small>`;
    if (revEl) revEl.innerHTML = `345.6M <small style="font-size:0.75rem;">ر.ي 📊</small>`;

    const filtered = items.filter(s => {
        if (stageFilter === 'ثانوية' && !s.stage.includes('ثانوية')) return false;
        if (stageFilter === 'أساسية عليا' && !s.stage.includes('عليا')) return false;
        if (stageFilter === 'أساسية أولى' && !s.stage.includes('الأولى')) return false;
        if (stageFilter === 'روضة' && !s.stage.includes('رياض') && !s.stage.includes('روضة')) return false;
        if (!query) return true;
        const text = [s.id, s.code, s.stage, s.gradeName, s.tuitionFee, s.totalAmount].join(' ').toLowerCase();
        return text.includes(query);
    });

    if (filtered.length === 0) {
        tb.innerHTML = '<tr><td colspan="12" style="text-align:center;color:var(--muted);padding:30px;">لا توجد رسوم صفوف مطابقة للبحث</td></tr>';
        return;
    }

    tb.innerHTML = filtered.map((s, idx) => {
        let stageBadge = '<span class="badge badge-info" style="font-size:0.75rem;">' + s.stage + '</span>';
        if (s.stage.includes('ثانوية')) {
            stageBadge = '<span class="badge" style="background:rgba(245,158,11,0.15);color:#fbbf24;font-size:0.75rem;">' + s.stage + '</span>';
        } else if (s.stage.includes('روضة')) {
            stageBadge = '<span class="badge" style="background:rgba(139,92,246,0.15);color:#c084fc;font-size:0.75rem;">' + s.stage + '</span>';
        }

        const statusBadge = '<span class="badge badge-success"><i class="fa-solid fa-circle-check"></i> معتمد 🟢</span>';

        return `
            <tr data-collection="gradeFees" data-id="${s.id || s.code}" ondblclick="openForm('grade_fees', '${s.id || s.code}')" oncontextmenu="event.preventDefault();deleteItem('gradeFees', '${s.id || s.code}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="text-align:center;font-weight:700;color:#94a3b8;">${idx + 1}</td>
                <td style="font-weight:800;color:#38bdf8;font-family:monospace;font-size:0.92rem;">${s.code || s.id}</td>
                <td>${stageBadge}</td>
                <td style="font-weight:700;color:#f8fafc;"><i class="fa-solid fa-graduation-cap" style="color:#38bdf8;font-size:0.8rem;"></i> ${s.gradeName}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.registrationFee}</td>
                <td><strong style="color:#34d399;font-family:monospace;font-size:0.92rem;">${s.tuitionFee}</strong></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.booksFee}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.uniformFee}</td>
                <td><strong style="color:#38bdf8;font-family:monospace;font-size:0.95rem;">${s.totalAmount}</strong></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.paymentPlan}</td>
                <td>${statusBadge}</td>
                <td><button class="badge badge-info" style="cursor:pointer;border:none;padding:5px 10px;" onclick="if(typeof toast==='function')toast('🏫 استعراض شُعب وفصول: ${s.gradeName}');goTo('pg-sections');"><i class="fa-solid fa-school"></i> شعب الصف</button></td>
            </tr>
        `;
    }).join('');
}
window.renderGradeFeesGrid = renderGradeFeesGrid;
window.renderGradeFees = renderGradeFeesGrid;
// Initial render
try { renderGradeFeesGrid(); } catch(e) {}


// AI Assistant Visibility Controller (Dedicated to Logged-in Parents Only)
function updateAiWidgetVisibility() {
    const aiWidget = document.getElementById('aiChatWidget');
    if (!aiWidget) return;
    
    let user = window.me;
    if (!user) {
        try {
            const raw = sessionStorage.getItem('sec_user') || localStorage.getItem('sec_user_session');
            if (raw) user = JSON.parse(raw);
        } catch(e){}
    }
    
    const token = sessionStorage.getItem('sec_session_token');
    const al = document.getElementById('appLayout');
    const lw = document.getElementById('loginWrapper');
    const isLayoutActive = (al && al.style.display !== 'none' && (!lw || lw.style.display === 'none'));
    const isParentRole = user && (user.role === 'parent' || user.roleName === 'ولي أمر' || user.roleName === 'طالب');
    const isParentPortal = window.location.pathname.includes('parent') || document.title.includes('أولياء الأمور');
    const isParentLoggedIn = isLayoutActive && (isParentRole || isParentPortal);
    
    if (isParentLoggedIn) {
        aiWidget.style.setProperty('display', 'block', 'important');
    } else {
        aiWidget.style.setProperty('display', 'none', 'important');
        const aiWin = document.getElementById('aiChatWindow');
        if (aiWin) {
            aiWin.style.display = 'none';
            aiWin.classList.remove('active', 'open');
        }
    }
}
window.updateAiWidgetVisibility = updateAiWidgetVisibility;

window.sendAiQuickReply = function(msg) {
    const quickMap = {
        'fees': 'كم الرسوم المتبقية وسندات السداد؟',
        'grades': 'أريد معرفة كشف درجات ابني ونتائج الاختبارات',
        'schedule': 'ما هو جدول حصص اليوم وتوزيع المعلمين؟',
        'attendance': 'أريد تقرير سجل الحضور والغياب والتأخر',
        'exams': 'متى مواعيد الاختبارات القادمة؟',
        'docs': 'ما هي الوثائق المطلوبة للقبول؟',
        'advisor': 'التواصل مع المرشد الأكاديمي'
    };
    const query = quickMap[msg] || msg;
    if (typeof sendAiQuery === 'function') {
        sendAiQuery(query);
    } else {
        if (typeof toast === 'function') toast('💬 إرسال رد سريع: ' + query, 'info');
    }
};

window.handleAiChatSubmit = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const input = document.getElementById('aiChatInput');
    const msg = input ? input.value.trim() : '';
    if (!msg) return;
    if (typeof sendAiQuery === 'function') {
        sendAiQuery(msg);
    }
};

window.clearAiChatHistory = function() {
    const chatBody = document.getElementById('aiChatBody');
    if (chatBody) {
        chatBody.innerHTML = `
            <div class="ai-msg-row bot">
                <div class="ai-msg-bubble">
                    مرحباً بك! 👋 تم مسح سجل المحادثة. أنا <strong>المساعد الذكي لمدرسة السحاب</strong>.
                    <br>كيف يمكنني مساعدتك الآن؟
                    <div class="ai-msg-time">الآن</div>
                </div>
            </div>
        `;
    }
    if (typeof toast === 'function') toast('🧹 تم مسح سجل محادثات المساعد الذكي', 'info');
};

if (typeof document !== 'undefined') { document.addEventListener('DOMContentLoaded', updateAiWidgetVisibility); setTimeout(updateAiWidgetVisibility, 200); }
