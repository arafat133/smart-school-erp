"""
Script to add form modal handlers for:
- cashbox
- vreceipt
- vpayment
- vtransfer
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

extra_forms_code = """
// ==================== REMAINING FINANCIAL FORMS ====================
const _origOpenFormFinancialExtra = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'cashbox') {
        title.innerHTML = '<i class="fa-solid fa-vault"></i> بطاقة تعريف صندوق نقدية / عهدة';
        fields.innerHTML = `
            <div class="fg"><label><i class="fa-solid fa-barcode"></i> كود الصندوق</label><input id="f_cb_code" placeholder="CB-101" value="${d.code || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-font"></i> اسم الصندوق (بالعربية)</label><input id="f_cb_name" placeholder="صندوق مبيعات الفرع الرئيسي" value="${d.name || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-font"></i> Fund Name (English)</label><input id="f_cb_nameEn" placeholder="Main Branch Cash Box" value="${d.nameEn || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-sitemap"></i> الحساب المحاسبي المرتبط</label>
                <select id="f_cb_account">
                    ${(DB.accounts || []).filter(a => a.postingType === 'فرعي').map(a => `<option value="${a.code}" ${d.accountCode === a.code ? 'selected' : ''}>[${a.code}] ${a.name}</option>`).join('')}
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-building"></i> الفرع / القسم</label><input id="f_cb_branch" placeholder="فرع صنعاء - إدارة المبيعات" value="${d.branch || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-user"></i> أمين الصندوق / المسؤول</label><input id="f_cb_cashier" placeholder="أحمد محمد (رقم الموظف: 402)" value="${d.cashier || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-coins"></i> العملة الأساسية</label>
                <select id="f_cb_currency">
                    <option value="YER" ${d.currency === 'YER' ? 'selected' : ''}>YER (ريال يمني)</option>
                    <option value="USD" ${d.currency === 'USD' ? 'selected' : ''}>USD (دولار أمريكي)</option>
                    <option value="SAR" ${d.currency === 'SAR' ? 'selected' : ''}>SAR (ريال سعودي)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-tags"></i> نوع الصندوق</label>
                <select id="f_cb_type">
                    <option value="رئيسي" ${d.type === 'رئيسي' ? 'selected' : ''}>رئيسي</option>
                    <option value="فرعي" ${d.type === 'فرعي' ? 'selected' : ''}>فرعي</option>
                    <option value="عهدة مستديمة" ${d.type === 'عهدة مستديمة' ? 'selected' : ''}>عهدة مستديمة</option>
                    <option value="مبيعات يومية" ${d.type === 'مبيعات يومية' ? 'selected' : ''}>مبيعات يومية</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-arrow-up"></i> سقف الصندوق الأقصى</label><input type="number" id="f_cb_maxLimit" placeholder="5000000" value="${d.maxLimit || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-arrow-down"></i> حد إعادة التغذية (الأدنى)</label><input type="number" id="f_cb_minLimit" placeholder="100000" value="${d.minLimit || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-ban"></i> السماح بالسالب</label>
                <select id="f_cb_allowNegative">
                    <option value="غير مسموح" ${d.allowNegative === 'غير مسموح' ? 'selected' : ''}>غير مسموح (Disabled)</option>
                    <option value="مسموح" ${d.allowNegative === 'مسموح' ? 'selected' : ''}>مسموح (Enabled)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-power-off"></i> حالة الصندوق</label>
                <select id="f_cb_status">
                    <option value="Active" ${d.status === 'Active' ? 'selected' : ''}>نشط (Active)</option>
                    <option value="Inactive" ${d.status === 'Inactive' ? 'selected' : ''}>موقف (Inactive)</option>
                </select>
            </div>
            <button class="btn-save" onclick="saveCashboxForm()" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ بطاقة الصندوق</button>
        `;
    } else if (type === 'vreceipt') {
        title.innerHTML = '<i class="fa-solid fa-arrow-down" style="color:#10b981;"></i> إنشاء سند قبض مالي (Receipt Voucher)';
        fields.innerHTML = `
            <div class="fg"><label><i class="fa-solid fa-barcode"></i> رقم السند (تلقائي)</label><input id="f_vr_no" readonly value="${d.number || 'RV-2026-' + String((DB.vreceipts||[]).length + 1).padStart(5, '0')}" style="background:rgba(0,0,0,0.4);font-weight:700;color:#60a5fa;"></div>
            <div class="fg"><label><i class="fa-solid fa-calendar"></i> تاريخ السند</label><input type="date" id="f_vr_date" value="${d.date || new Date().toISOString().slice(0,10)}"></div>
            <div class="fg"><label><i class="fa-solid fa-vault"></i> حساب النقدية / البنك (المقبوض له)</label>
                <select id="f_vr_cashAccount">
                    <option value="صندوق المبيعات الرئيسي">صندوق المبيعات الرئيسي (CB-101)</option>
                    <option value="بنك اليمن والكويت">بنك اليمن والكويت (YKB-01)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-user"></i> الطرف الآخر / الحساب (المُسلّم)</label><input id="f_vr_account" placeholder="شركة الأمل للتجارة (عميل) / اسم الطالب" value="${d.account || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-credit-card"></i> طريقة الدفع</label>
                <select id="f_vr_method" onchange="toggleChequeFields('vr', this.value)">
                    <option value="نقداً">نقداً (Cash)</option>
                    <option value="شيك">شيك بنكي (Cheque)</option>
                    <option value="تحويل بنكي">تحويل بنكي (Bank Transfer)</option>
                    <option value="بطاقة ائتمان / POS">بطاقة ائتمان / POS</option>
                </select>
            </div>
            <div id="vr_cheque_fields" style="display:none;background:rgba(255,255,255,0.03);padding:10px;border-radius:8px;margin-bottom:12px;">
                <div class="fg"><label>رقم الشيك / التحويل</label><input id="f_vr_ref" placeholder="88412"></div>
                <div class="fg"><label>تاريخ الاستحقاق</label><input type="date" id="f_vr_dueDate"></div>
                <div class="fg"><label>البنك المسحوب عليه</label><input id="f_vr_bank" placeholder="بنك اليمن والكويت"></div>
            </div>
            <div class="fg"><label><i class="fa-solid fa-money-bill-wave"></i> المبلغ والعملة</label>
                <div style="display:flex;gap:8px;">
                    <input type="number" id="f_vr_amount" placeholder="1500" value="${d.amount || ''}" style="flex:2;">
                    <select id="f_vr_currency" style="flex:1;"><option value="YER">YER</option><option value="USD">USD</option><option value="SAR">SAR</option></select>
                </div>
            </div>
            <div class="fg"><label><i class="fa-solid fa-building"></i> مركز التكلفة</label><input id="f_vr_costCenter" placeholder="عام / مشروع التوسع" value="${d.costCenter || 'عام'}"></div>
            <div class="fg"><label><i class="fa-solid fa-align-right"></i> البيان / الشرح</label><textarea id="f_vr_desc" placeholder="دفعة تحت الحساب لقاء فاتورة...">${d.desc || ''}</textarea></div>
            <div class="fg"><label><i class="fa-solid fa-upload"></i> المرفقات (صورة الشيك/الإشعار)</label><input type="file" id="f_vr_file"></div>
            <button class="btn-save" onclick="saveVoucherForm('receipt')" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-floppy-disk"></i> حفظ وإعتماد سند القبض</button>
        `;
    } else if (type === 'vpayment') {
        title.innerHTML = '<i class="fa-solid fa-arrow-up" style="color:#ef4444;"></i> إنشاء سند صرف مالي (Payment Voucher)';
        fields.innerHTML = `
            <div class="fg"><label><i class="fa-solid fa-barcode"></i> رقم السند (تلقائي)</label><input id="f_vp_no" readonly value="${d.number || 'PV-2026-' + String((DB.vpayments||[]).length + 1).padStart(5, '0')}" style="background:rgba(0,0,0,0.4);font-weight:700;color:#f87171;"></div>
            <div class="fg"><label><i class="fa-solid fa-calendar"></i> تاريخ السند</label><input type="date" id="f_vp_date" value="${d.date || new Date().toISOString().slice(0,10)}"></div>
            <div class="fg"><label><i class="fa-solid fa-vault"></i> حساب النقدية / البنك (المصروف منه)</label>
                <select id="f_vp_cashAccount">
                    <option value="صندوق المبيعات الرئيسي">صندوق المبيعات الرئيسي (CB-101)</option>
                    <option value="بنك اليمن والكويت">بنك اليمن والكويت (YKB-01)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-user"></i> الحساب المقابل / المستلم</label><input id="f_vp_account" placeholder="مؤسسة النور للقرطاسية (مورد) / اسم الموظف" value="${d.account || ''}"></div>
            <div class="fg"><label><i class="fa-solid fa-credit-card"></i> طريقة الدفع</label>
                <select id="f_vp_method" onchange="toggleChequeFields('vp', this.value)">
                    <option value="نقداً">نقداً (Cash)</option>
                    <option value="شيك">شيك بنكي (Cheque)</option>
                    <option value="تحويل بنكي">تحويل بنكي (Bank Transfer)</option>
                </select>
            </div>
            <div id="vp_cheque_fields" style="display:none;background:rgba(255,255,255,0.03);padding:10px;border-radius:8px;margin-bottom:12px;">
                <div class="fg"><label>رقم الشيك / التحويل</label><input id="f_vp_ref" placeholder="77410"></div>
                <div class="fg"><label>تاريخ الاستحقاق</label><input type="date" id="f_vp_dueDate"></div>
            </div>
            <div class="fg"><label><i class="fa-solid fa-money-bill-wave"></i> المبلغ والعملة</label>
                <div style="display:flex;gap:8px;">
                    <input type="number" id="f_vp_amount" placeholder="25000" value="${d.amount || ''}" style="flex:2;">
                    <select id="f_vp_currency" style="flex:1;"><option value="YER">YER</option><option value="USD">USD</option><option value="SAR">SAR</option></select>
                </div>
            </div>
            <div class="fg"><label><i class="fa-solid fa-building"></i> مركز التكلفة</label><input id="f_vp_costCenter" placeholder="عام / إدارة المشاريع" value="${d.costCenter || 'عام'}"></div>
            <div class="fg"><label><i class="fa-solid fa-align-right"></i> البيان / الشرح</label><textarea id="f_vp_desc" placeholder="صرف قيمة أدوات مكتبية وشراء مستلزمات...">${d.desc || ''}</textarea></div>
            <button class="btn-save" onclick="saveVoucherForm('payment')" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-floppy-disk"></i> حفظ وإعتماد سند الصرف</button>
        `;
    } else if (type === 'vtransfer') {
        title.innerHTML = '<i class="fa-solid fa-right-left" style="color:#3b82f6;"></i> تحويل داخلي بين الصناديق والبنوك';
        fields.innerHTML = `
            <div class="fg"><label><i class="fa-solid fa-barcode"></i> رقم التحويل</label><input id="f_vt_no" readonly value="TRF-2026-${String(Date.now()).slice(-4)}" style="background:rgba(0,0,0,0.4);font-weight:700;color:#60a5fa;"></div>
            <div class="fg"><label><i class="fa-solid fa-calendar"></i> التاريخ</label><input type="date" id="f_vt_date" value="${new Date().toISOString().slice(0,10)}"></div>
            <div class="fg"><label><i class="fa-solid fa-arrow-up"></i> من حساب (المُحوِّل)</label>
                <select id="f_vt_from">
                    <option value="صندوق المبيعات الرئيسي">صندوق المبيعات الرئيسي (CB-101)</option>
                    <option value="بنك اليمن والكويت">بنك اليمن والكويت (YKB-01)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-arrow-down"></i> إلى حساب (المُحوَّل إليه)</label>
                <select id="f_vt_to">
                    <option value="بنك اليمن والكويت">بنك اليمن والكويت (YKB-01)</option>
                    <option value="صندوق المبيعات الرئيسي">صندوق المبيعات الرئيسي (CB-101)</option>
                </select>
            </div>
            <div class="fg"><label><i class="fa-solid fa-money-bill-wave"></i> المبلغ المحوّل</label><input type="number" id="f_vt_amount" placeholder="100000"></div>
            <div class="fg"><label><i class="fa-solid fa-align-right"></i> البيان</label><input id="f_vt_desc" value="تغذية حساب البنك من نقدية الصندوق"></div>
            <button class="btn-save" onclick="saveVoucherForm('transfer')" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-floppy-disk"></i> إتمام التحويل الداخلي</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormFinancialExtra) {
        _origOpenFormFinancialExtra(type, editData);
    }
};

function toggleChequeFields(prefix, val) {
    const div = document.getElementById(prefix + '_cheque_fields');
    if (div) div.style.display = (val === 'شيك' || val === 'تحويل بنكي') ? 'block' : 'none';
}

function saveCashboxForm() {
    const code = document.getElementById('f_cb_code')?.value || 'CB-' + Date.now();
    const name = document.getElementById('f_cb_name')?.value || 'صندوق جديد';
    const nameEn = document.getElementById('f_cb_nameEn')?.value || '';
    const accountCode = document.getElementById('f_cb_account')?.value || '110101';
    const branch = document.getElementById('f_cb_branch')?.value || 'الفرع الرئيسي';
    const cashier = document.getElementById('f_cb_cashier')?.value || 'مسؤول الصندوق';
    const currency = document.getElementById('f_cb_currency')?.value || 'YER';
    const type = document.getElementById('f_cb_type')?.value || 'مبيعات';
    const maxLimit = parseFloat(document.getElementById('f_cb_maxLimit')?.value) || 1000000;
    const minLimit = parseFloat(document.getElementById('f_cb_minLimit')?.value) || 50000;
    const allowNegative = document.getElementById('f_cb_allowNegative')?.value || 'غير مسموح';
    const status = document.getElementById('f_cb_status')?.value || 'Active';

    if (!DB.cashboxes) DB.cashboxes = [];
    const idx = DB.cashboxes.findIndex(c => c.code === code);
    const boxObj = { code, name, nameEn, accountCode, branch, cashier, currency, type, maxLimit, minLimit, balance: idx>=0?DB.cashboxes[idx].balance:0, allowNegative, status };

    if (idx >= 0) DB.cashboxes[idx] = boxObj;
    else DB.cashboxes.push(boxObj);

    logAudit('المحاسب', 'إضافة', 'دليل الصناديق', 'حفظ بطاقة الصندوق ' + name);
    toast('✅ تم حفظ بطاقة الصندوق بنجاح');
    document.getElementById('formModal')?.classList.remove('active');
    renderCashboxes();
}

function saveVoucherForm(vType) {
    if (vType === 'receipt') {
        const number = document.getElementById('f_vr_no')?.value;
        const date = document.getElementById('f_vr_date')?.value;
        const cashAccount = document.getElementById('f_vr_cashAccount')?.value;
        const account = document.getElementById('f_vr_account')?.value || 'عميل / طالب';
        const method = document.getElementById('f_vr_method')?.value;
        const amount = parseFloat(document.getElementById('f_vr_amount')?.value) || 0;
        const costCenter = document.getElementById('f_vr_costCenter')?.value || 'عام';
        const desc = document.getElementById('f_vr_desc')?.value || 'سند قبض';

        if (!DB.vreceipts) DB.vreceipts = [];
        DB.vreceipts.unshift({ id: Date.now(), number, date, cashAccount, account, method, amount, costCenter, desc });
        logAudit('المحاسب', 'إضافة', 'سندات القبض', 'إصدار سند قبض رقم ' + number);
        toast('✅ تم حفظ وإعتماد سند القبض رقم ' + number);
    } else if (vType === 'payment') {
        const number = document.getElementById('f_vp_no')?.value;
        const date = document.getElementById('f_vp_date')?.value;
        const cashAccount = document.getElementById('f_vp_cashAccount')?.value;
        const account = document.getElementById('f_vp_account')?.value || 'مورد / موظف';
        const method = document.getElementById('f_vp_method')?.value;
        const amount = parseFloat(document.getElementById('f_vp_amount')?.value) || 0;
        const costCenter = document.getElementById('f_vp_costCenter')?.value || 'عام';
        const desc = document.getElementById('f_vp_desc')?.value || 'سند صرف';

        if (!DB.vpayments) DB.vpayments = [];
        DB.vpayments.unshift({ id: Date.now(), number, date, cashAccount, account, method, amount, costCenter, desc });
        logAudit('المحاسب', 'إضافة', 'سندات الصرف', 'إصدار سند صرف رقم ' + number);
        toast('✅ تم حفظ وإعتماد سند الصرف رقم ' + number);
    } else if (vType === 'transfer') {
        const number = document.getElementById('f_vt_no')?.value;
        const date = document.getElementById('f_vt_date')?.value;
        const from = document.getElementById('f_vt_from')?.value;
        const to = document.getElementById('f_vt_to')?.value;
        const amount = parseFloat(document.getElementById('f_vt_amount')?.value) || 0;
        const desc = document.getElementById('f_vt_desc')?.value || 'تحويل داخلي';

        if (!DB.vtransfers) DB.vtransfers = [];
        DB.vtransfers.unshift({ id: Date.now(), number, date, cashAccount: from, account: 'تحويل إلى: ' + to, method: 'تحويل داخلي', amount, costCenter: 'عام', desc });
        toast('✅ تم حفظ التحويل الداخلي بنجاح');
    }
    document.getElementById('formModal')?.classList.remove('active');
    renderVouchers();
}
"""

if 'REMAINING FINANCIAL FORMS' not in js:
    js += extra_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended extra financial forms successfully!")
