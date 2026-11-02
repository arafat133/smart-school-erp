"""
Python script to append Goods Issue Notes (pg-issue-orders) & logic for all reported pages in app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Goods Issue Notes & Reported Pages Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

issue_orders_db_additions = """
// Data collections for Goods Issue Notes (GIN) and reported pages
if (!DB.issueOrdersGridData) DB.issueOrdersGridData = [
    { ginNo: 'GIN-2026-0214', reqRef: 'REQ-2026-0092', unitCostCenter: 'إدارة الشؤون الأكاديمية - معامل الكمبيوتر', warehouse: 'المخزن الرئيسي - قسم الأجهزة والشبكات', issueTime: '2026-08-09 11:00 AM', itemsQty: 'طابعة HP Laser (مطلوب 2 / مصروف 2)', stockBal: '15 قطعة (متوفر وجاهز للصرف)', recipient: 'أ. إبراهيم العنسي (مسؤول المعامل)', status: 'مُرحّل ومخصوم (Posted & Deducted)', storekeeper: 'م. خالد محمود (أمين المخزن الرئيسي)' }
];

if (!DB.classTimesGridData) DB.classTimesGridData = [
    { period: 1, type: 'حصة دراسية', start: '07:30 AM', end: '08:15 AM', duration: '45 دقيقة', status: 'نشط (Active)' },
    { period: 2, type: 'حصة دراسية', start: '08:15 AM', end: '09:00 AM', duration: '45 دقيقة', status: 'نشط (Active)' },
    { period: 3, type: 'استراحة / فسحة', start: '09:45 AM', end: '10:15 AM', duration: '30 دقيقة', status: 'نشط (Active)' }
];

if (!DB.promotionWorkflowGridData) DB.promotionWorkflowGridData = [
    { id: '20261042', name: 'عبدالرحمن محمد علي السالمي', currentGrade: 'الثاني الثانوي', result: 'ناجح (Pass)', gpa: '89.5%', nextGrade: 'الثالث الثانوي - شعبة (أ)', status: 'جاهز للترفيع' }
];
"""

issue_orders_modules_js = """

// ==================== GOODS ISSUE NOTES (GIN) ====================
function renderIssueOrdersGrid() {
    const tb = document.getElementById('tbl-issue-orders-grid');
    if (!tb) return;

    const list = DB.issueOrdersGridData || [];
    tb.innerHTML = list.map(g => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${g.ginNo}</td>
            <td style="font-weight:700;color:#c084fc;">${g.reqRef}</td>
            <td style="font-weight:700;">${g.unitCostCenter}</td>
            <td>${g.warehouse}</td>
            <td style="font-size:0.8rem;">${g.issueTime}</td>
            <td style="font-size:0.83rem;">${g.itemsQty}</td>
            <td style="font-weight:700;color:#34d399;">${g.stockBal}</td>
            <td style="font-size:0.83rem;">${g.recipient}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${g.status}</span></td>
            <td style="font-size:0.8rem;">${g.storekeeper}</td>
            <td><button class="btn-edit" onclick="toast('معاينة إذن الصرف المخزني PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}

function postGINToInventory() {
    toast('⚡ جاري اعتماد إذن الصرف وخصم الكميات من المخزون المتاح وتوجيه التكلفة...');
    setTimeout(() => { renderIssueOrdersGrid(); toast('✅ تم خصم الأصناف من المستودع وتوليد التغيرات المحاسبية بنجاح!'); }, 700);
}


// ==================== CLASS TIMES ====================
function renderClassTimesGrid() {
    const tb = document.getElementById('tbl-class-times-grid');
    if (!tb) return;

    const list = DB.classTimesGridData || [];
    tb.innerHTML = list.map(c => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">الحصة (${c.period})</td>
            <td style="font-weight:700;">${c.type}</td>
            <td style="font-weight:800;color:#34d399;">${c.start}</td>
            <td style="font-weight:800;color:#f87171;">${c.end}</td>
            <td>${c.duration}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${c.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('class-times', ${JSON.stringify(c).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== PROMOTION WORKFLOW ====================
function renderPromotionBatch() {
    const tb = document.getElementById('tbl-promotion-workflow-grid') || document.getElementById('tbl-promotion');
    if (!tb) return;

    const list = DB.promotionWorkflowGridData || [];
    tb.innerHTML = list.map(p => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${p.id}</td>
            <td style="font-weight:700;">${p.name}</td>
            <td>${p.currentGrade}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${p.result}</span></td>
            <td style="font-weight:800;color:#60a5fa;">${p.gpa}</td>
            <td style="font-weight:700;color:#fbbf24;">${p.nextGrade}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(59,130,246,0.15);color:#60a5fa;">${p.status}</span></td>
            <td><button class="btn-add" onclick="toast('تم ترفيع الطالب بنجاح')" style="padding:3px 8px;font-size:0.75rem;"><i class="fa-solid fa-turn-up"></i> ترفيع</button></td>
        </tr>
    `).join('');
}

function executeBatchPromotion() {
    toast('🚀 جاري تنفيذ قرار الترفيع الجماعي لجميع الطلاب الناجحين...');
    setTimeout(() => { renderPromotionBatch(); toast('🎉 تم ترفيع جميع الطلاب الناجحين للعام الدراسي الجديد بنجاح!'); }, 800);
}
"""

issue_orders_form_code = """
// ==================== ISSUE ORDERS FORM MODAL ====================
const _origOpenFormIssueOrdersModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'issue-orders') {
        title.innerHTML = '<i class="fa-solid fa-dolly"></i> إنشاء إذن صرف وتسليم مخزني (GIN)';
        fields.innerHTML = `
            <div class="fg"><label>رقم إذن الصرف (GIN)</label><input placeholder="GIN-2026-0214" value="GIN-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>رقم طلب الصرف المرتبط (REQ)</label><input placeholder="REQ-2026-0092"></div>
            <div class="fg"><label>الجهة الطالبة / مركز التكلفة</label><input placeholder="إدارة الشؤون الأكاديمية - معامل الكمبيوتر"></div>
            <div class="fg"><label>المستودع المصدر</label><select><option>المخزن الرئيسي - قسم الأجهزة والشبكات</option></select></div>
            <div class="fg"><label>الأصناف والكميات المطلوب صرفها</label><input placeholder="طابعة HP Laser (مطلوب 2 / مصروف 2)"></div>
            <div class="fg"><label>اسم الموظف المستلم المخول</label><input placeholder="أ. إبراهيم العنسي (مسؤول المعامل)"></div>
            <div class="fg"><label>أمين المخزن المنفّذ</label><input placeholder="م. خالد محمود"></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء إذن الصرف وحفظ المسودة بنجاح'); document.getElementById('formModal').classList.remove('active'); renderIssueOrdersGrid();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-paper-plane"></i> إصدار إذن الصرف</button>
        `;
    } else if (type === 'class-times') {
        title.innerHTML = '<i class="fa-solid fa-clock"></i> إضافة / تعديل توقيت حصة دراسية';
        fields.innerHTML = `
            <div class="fg"><label>رقم الحصة</label><input type="number" placeholder="1" value="${d.period || ''}"></div>
            <div class="fg"><label>نوع الفترة / الحصة</label><select><option>حصة دراسية</option><option>استراحة / فسحة</option><option>طابور صباحي</option></select></div>
            <div class="fg"><label>وقت البداية</label><input type="time" value="07:30"></div>
            <div class="fg"><label>وقت النهاية</label><input type="time" value="08:15"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ توقيت الحصة بنجاح'); document.getElementById('formModal').classList.remove('active'); renderClassTimesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ التوقيت</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormIssueOrdersModals) {
        _origOpenFormIssueOrdersModals(type, editData);
    }
};
"""

if 'GOODS ISSUE NOTES MODULE' not in js:
    js += issue_orders_db_additions + "\n" + issue_orders_modules_js + "\n" + issue_orders_form_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Goods Issue Notes & Reported Pages logic in app.js successfully!")
