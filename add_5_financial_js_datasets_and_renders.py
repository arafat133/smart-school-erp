"""
Add rich initial datasets & render functions for 5 financial interfaces in app.js
"""
import re, time

print("=" * 60)
print("Injecting Datasets & Renders for 5 Financial Interfaces in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

financial_js_engine = """
// ==================== 5 FINANCIAL INTERFACES DATASETS & RENDERS ====================

// 1. Currencies & Exchange Rates Dataset
if (!DB.currenciesData) DB.currenciesData = [
    { isoCode: 'YER', nameArEn: 'ريال يمني | YEMENI RIAL', symbol: 'ر.ي', isBase: 'نعم (العملة المحلية القياسية)', officialRate: '1 YER = 1 YER', buySellRate: 'شراء: 1 YER | بيع: 1 YER', lastUpdated: '2026-08-12 - 08:00 AM', decimalPlaces: 2, fxAccount: 'حساب النقدية بالعملة المحلية (110101)', status: 'نشطة 🟢' },
    { isoCode: 'USD', nameArEn: 'دولار أمريكي | US Dollar', symbol: '$', isBase: 'لا', officialRate: '1 USD = 530 YER', buySellRate: 'شراء: 530 YER | بيع: 535 YER', lastUpdated: '2026-08-12 - 08:00 AM', decimalPlaces: 2, fxAccount: 'أرباح وخسائر فروق العملة (4102)', status: 'نشطة 🟢' },
    { isoCode: 'SAR', nameArEn: 'ريال سعودي | Saudi Riyal', symbol: 'ر.س', isBase: 'لا', officialRate: '1 SAR = 140 YER', buySellRate: 'شراء: 140 YER | بيع: 142 YER', lastUpdated: '2026-08-12 - 08:00 AM', decimalPlaces: 2, fxAccount: 'أرباح وخسائر فروق العملة (4102)', status: 'نشطة 🟢' }
];

function renderCurrenciesGrid() {
    const tb = document.getElementById('tbl-currencies-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchCurrencies')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('currenciesData') : DB.currenciesData).filter(c => {
        return !filter || c.isoCode.toLowerCase().includes(filter) || c.nameArEn.toLowerCase().includes(filter) || c.symbol.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(c => `
        <tr>
            <td style="font-weight:800;color:#60a5fa;font-family:monospace;font-size:0.9rem;">${c.isoCode}</td>
            <td style="font-weight:700;">${c.nameArEn}</td>
            <td style="font-weight:800;color:#34d399;font-size:0.95rem;">${c.symbol}</td>
            <td><span class="badge ${c.isBase.includes('نعم')?'badge-success':'badge-info'}">${c.isBase}</span></td>
            <td style="font-weight:700;color:#fbbf24;">${c.officialRate}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${c.buySellRate}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${c.lastUpdated}</td>
            <td>${c.decimalPlaces} خانات</td>
            <td style="font-size:0.78rem;">${c.fxAccount}</td>
            <td><span class="badge badge-success">${c.status}</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('currencies', '${c.isoCode}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                    <button class="btn-delete" onclick="deleteItem('currenciesData', '${c.isoCode}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderCurrenciesGrid = renderCurrenciesGrid;
function renderCurrencies() { renderCurrenciesGrid(); }
window.renderCurrencies = renderCurrencies;

// 2. Cashbox Inventory Audit Dataset
if (!DB.cashboxInventoryData) DB.cashboxInventoryData = [
    { id: 'AUD-CASH-2026-0089', safeName: 'خزينة التحصيل الرئيسية - الفرع الرئيسي', auditTime: '2026-08-12 - 03:30 PM', bookBalance: '1,250,000 YER', physicalCash: '1,245,000 YER', variance: 'عجز بمبلغ 5,000 YER 🔴', cashier: 'أ. إبراهيم العنسي', auditor: 'أ. خالد محمود العنسي (المراجع)', adjAccount: 'حساب عجز الصناديق / عهدة أمين الصندوق', status: 'معتمد ومرحّل (Approved) 🟢' },
    { id: 'AUD-CASH-2026-0090', safeName: 'صندوق رسوم التسجيل والأنشطة', auditTime: '2026-08-12 - 04:15 PM', bookBalance: '2,500,000 YER', physicalCash: '2,500,000 YER', variance: 'مطابق (0 فرق) 🟢', cashier: 'أ. سارة أحمد', auditor: 'أ. خالد محمود العنسي', adjAccount: 'حساب التسويات النقدية', status: 'معتمد ومرحّل (Approved) 🟢' }
];

function renderCashboxInventoryGrid() {
    const tb = document.getElementById('tbl-cashbox-inventory-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchCashboxInventory')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('cashboxInventoryData') : DB.cashboxInventoryData).filter(c => {
        return !filter || c.id.toLowerCase().includes(filter) || c.safeName.toLowerCase().includes(filter) || c.cashier.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${c.id}</td>
            <td style="font-weight:700;">🏫 ${c.safeName}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${c.auditTime}</td>
            <td style="font-weight:700;color:#60a5fa;">${c.bookBalance}</td>
            <td style="font-weight:700;color:#34d399;">${c.physicalCash}</td>
            <td><strong style="color:${c.variance.includes('عجز')?'#ef4444':'#10b981'};">${c.variance}</strong></td>
            <td>👤 ${c.cashier}</td>
            <td>👤 ${c.auditor}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${c.adjAccount}</td>
            <td><span class="badge badge-success">${c.status}</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('cashbox_inventory', '${c.id}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                    <button class="btn-delete" onclick="deleteItem('cashboxInventoryData', '${c.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderCashboxInventoryGrid = renderCashboxInventoryGrid;
function renderCashboxInventory() { renderCashboxInventoryGrid(); }
window.renderCashboxInventory = renderCashboxInventory;

// 3. Period-End Closures Dataset
if (!DB.closingsData) DB.closingsData = [
    { id: 'CLS-2026-M08', periodScope: 'إقفال شهر أغسطس 2026', closingType: 'إقفال شهري دوري', preCheckStatus: 'سليم وجاهز (0 معلقات) 🟢', closingJournalRef: 'JV-CLOSE-2026-08', netResult: 'صافي ربح: 12,450,000 YER', lockStatus: 'مغلقة ومقفلة بالكامل (Locked) 🔒', closedBy: 'أ. خالد محمود العنسي (المدير المالي)', timestamp: '2026-08-12 - 11:45 PM', targetFiscalYear: 'السنة المالية 2026' },
    { id: 'CLS-2025-FY', periodScope: 'الإقفال الختامي للسنة المالية 2025', closingType: 'إقفال ختامي للسنة المالية', preCheckStatus: 'سليم ومرحّل بالكامل 🟢', closingJournalRef: 'JV-CLOSE-2025-FY', netResult: 'صافي ربح: 105,000,000 YER', lockStatus: 'مغلقة ومقفلة نهائياً (Locked) 🔒', closedBy: 'أ. خالد محمود العنسي', timestamp: '2025-12-31 - 11:59 PM', targetFiscalYear: 'السنة المالية 2026' }
];

function renderClosingsGrid() {
    const tb = document.getElementById('tbl-closings-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchClosings')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('closingsData') : DB.closingsData).filter(c => {
        return !filter || c.id.toLowerCase().includes(filter) || c.periodScope.toLowerCase().includes(filter) || c.closingType.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${c.id}</td>
            <td style="font-weight:700;">${c.periodScope}</td>
            <td><span class="badge badge-info">${c.closingType}</span></td>
            <td><span class="badge badge-success">${c.preCheckStatus}</span></td>
            <td style="font-weight:700;font-family:monospace;color:#fbbf24;">${c.closingJournalRef}</td>
            <td style="font-weight:800;color:#34d399;">${c.netResult}</td>
            <td><strong style="color:#ef4444;">${c.lockStatus}</strong></td>
            <td>👤 ${c.closedBy}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${c.timestamp}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${c.targetFiscalYear}</td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="toast('🔒 الفترة الدفترية مقفلة نهائياً بموجب السياسات المحاسبية')" style="background:#4b5563;"><i class="fa-solid fa-lock"></i> مقفلة</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderClosingsGrid = renderClosingsGrid;
function renderClosings() { renderClosingsGrid(); }
window.renderClosings = renderClosings;

function executePeriodClosing() {
    toast('⚡ جاري فحص الحسابات الاسمية وتوليد قيد الإقفال الفتراتي الآلي...');
    setTimeout(() => {
        renderClosingsGrid();
        toast('🎉 تم تنفيذ الإقفال المحاسبي الفتراتي وتدوير الأرصدة بنجاح!');
    }, 800);
}
window.executePeriodClosing = executePeriodClosing;

// 4. Bank Accounts Directory Dataset
if (!DB.banksData) DB.banksData = [
    { id: 'BNK-ACC-2026-001', bankNameBranch: 'بنك التضامن - الفرع الرئيسي (صنعاء)', accNumber: '102030405060', ibanSwift: 'YE32 TBSB 0000 0010 2030 4050 / TBSBYESA', chartLink: 'حساب بنك التضامن - محلي (11020101)', currency: 'ريال يمني (YER)', bookBalance: '45,200,000 YER', accType: 'حساب جاري (Current)', checkbookSeq: 'من شيك 5001 إلى 5100', status: 'نشط ومعتمد (Active) 🟢' },
    { id: 'BNK-ACC-2026-002', bankNameBranch: 'بنك اليمن الدولي - فرع حدة', accNumber: '908070605040', ibanSwift: 'YE99 IBYE 0000 0090 8070 6050 / IBYEYESA', chartLink: 'حساب بنك اليمن الدولي - دولار (11020102)', currency: 'دولار أمريكي (USD)', bookBalance: '$ 85,400.00', accType: 'حساب تحصيل رسوم', checkbookSeq: 'من شيك 1001 إلى 1100', status: 'نشط ومعتمد (Active) 🟢' }
];

function renderBanksGrid() {
    const tb = document.getElementById('tbl-banks-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchBanks')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('banksData') : DB.banksData).filter(b => {
        return !filter || b.id.toLowerCase().includes(filter) || b.bankNameBranch.toLowerCase().includes(filter) || b.accNumber.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(b => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${b.id}</td>
            <td style="font-weight:700;">🏛️ ${b.bankNameBranch}</td>
            <td style="font-weight:700;font-family:monospace;color:#fbbf24;">${b.accNumber}</td>
            <td style="font-size:0.72rem;font-family:monospace;color:var(--muted);">${b.ibanSwift}</td>
            <td style="font-size:0.78rem;color:#34d399;">${b.chartLink}</td>
            <td><span class="badge badge-info">${b.currency}</span></td>
            <td style="font-weight:800;color:#34d399;">${b.bookBalance}</td>
            <td style="font-size:0.78rem;">${b.accType}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${b.checkbookSeq}</td>
            <td><span class="badge badge-success">${b.status}</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('banks', '${b.id}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                    <button class="btn-delete" onclick="deleteItem('banksData', '${b.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderBanksGrid = renderBanksGrid;
function renderBanks() { renderBanksGrid(); }
window.renderBanks = renderBanks;

// 5. Dunning & Payment Demand Letters Dataset
if (!DB.demandLettersData) DB.demandLettersData = [
    { id: 'DUN-2026-0412', payerName: 'أ. عبد الله علي العنسي', studentGrade: 'محمد عبد الله العنسي (الثالث الثانوي - شعبة أ)', stage: 'المستوى الثاني (إشعار تأخير رسمي) 🔴', overdueAmount: '150,000 YER', daysOverdue: '30 يوماً متأخرة', channel: 'رسالة واتساب معتمدة + SMS', payLink: 'https://pay.school.edu.ye/pay/DUN-0412', deliveryStatus: 'تم التسليم والفتح (Read & Delivered) 🟢', sentDeadline: 'أرسلت: 2026-08-12 | آخر مهلة: 2026-08-20' },
    { id: 'DUN-2026-0413', payerName: 'أ. أحمد السالمي', studentGrade: 'ياسر أحمد السالمي (الثاني الثانوي - شعبة ب)', stage: 'المستوى الأول (تذكير ودّي) 🟡', overdueAmount: '80,000 YER', daysOverdue: '10 أيام متأخرة', channel: 'إشعار تطبيق Push', payLink: 'https://pay.school.edu.ye/pay/DUN-0413', deliveryStatus: 'تم التسليم (Delivered) 🟢', sentDeadline: 'أرسلت: 2026-08-10 | آخر مهلة: 2026-08-25' }
];

function renderDemandLettersGrid() {
    const tb = document.getElementById('tbl-demand-letters-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchDemandLetters')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('demandLettersData') : DB.demandLettersData).filter(d => {
        return !filter || d.id.toLowerCase().includes(filter) || d.payerName.toLowerCase().includes(filter) || d.studentGrade.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(d => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${d.id}</td>
            <td style="font-weight:700;">👤 ${d.payerName}</td>
            <td style="font-size:0.8rem;color:#1e3a8a;">${d.studentGrade}</td>
            <td><strong style="color:#ef4444;font-size:0.78rem;">${d.stage}</strong></td>
            <td style="font-weight:800;color:#ef4444;">${d.overdueAmount}</td>
            <td><span class="badge badge-warning">${d.daysOverdue}</span></td>
            <td><span class="badge badge-info">${d.channel}</span></td>
            <td style="font-size:0.7rem;font-family:monospace;"><a href="#" onclick="toast('🔗 تم نسخ رابط السداد المباشر!');return false;" style="color:#60a5fa;">رابط سداد مالي 🔗</a></td>
            <td><span class="badge badge-success">${d.deliveryStatus}</span></td>
            <td style="font-size:0.75rem;color:var(--muted);">${d.sentDeadline}</td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('demand_letters', '${d.id}')"><i class="fa-solid fa-paper-plane"></i> إعادة إرسال</button>
                    <button class="btn-delete" onclick="deleteItem('demandLettersData', '${d.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderDemandLettersGrid = renderDemandLettersGrid;
function renderDemandLetters() { renderDemandLettersGrid(); }
window.renderDemandLetters = renderDemandLetters;
"""

if 'window.renderCurrenciesGrid = renderCurrenciesGrid' not in js:
    js += "\n" + financial_js_engine + "\n"
    print("  ✓ Appended 5 Financial Interfaces datasets & renders to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
