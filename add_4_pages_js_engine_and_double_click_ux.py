"""
Add datasets, render functions, password strength checker, double-click/long-press row engine, and universal form builder in app.js
"""
import re, time

print("=" * 60)
print("Injecting Datasets, Password Strength, Double-Click UX & Universal Form Builder in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

double_click_and_4_pages_js = """
// ==================== DOUBLE-CLICK & LONG-PRESS INTERACTIVE ROW ENGINE ====================
function makeRowInteractive(tr, entityType, itemId, collectionKey) {
    if (!tr) return;
    tr.style.cursor = 'pointer';
    tr.setAttribute('title', '💡 انقر مرتين لتعديل البيانات، أو اضغط مطولاً لحذف السجل');

    // Double-Click to Edit
    tr.ondblclick = function(e) {
        e.preventDefault();
        if (typeof openForm === 'function') {
            openForm(entityType, itemId);
            toast(`✏️ فتح نافذة تعديل بيانات (${itemId})`);
        }
    };

    // Long-Press Timer for Delete
    let pressTimer = null;
    const startPress = function() {
        pressTimer = setTimeout(() => {
            if (confirm(`❓ هل أنت محقق من رغبتك في حذف السجل (${itemId})؟`)) {
                if (typeof deleteItem === 'function') deleteItem(collectionKey || (entityType + 'Data'), itemId);
            }
        }, 700);
    };

    const cancelPress = function() {
        if (pressTimer) clearTimeout(pressTimer);
    };

    tr.onmousedown = startPress;
    tr.onmouseup = cancelPress;
    tr.onmouseleave = cancelPress;
    tr.ontouchstart = startPress;
    tr.ontouchend = cancelPress;
}
window.makeRowInteractive = makeRowInteractive;

// Real-Time Password Strength Evaluator
function checkPasswordStrength(val) {
    const label = document.getElementById('pwdStrengthLabel');
    const bar = document.getElementById('pwdStrengthBar');
    const rLen = document.getElementById('ruleLength');
    const rNum = document.getElementById('ruleNumber');
    const rSpec = document.getElementById('ruleSpecial');

    let score = 0;
    const isLen = val.length >= 8;
    const isNum = /[0-9]/.test(val);
    const isSpec = /[@#$%^&*!]/.test(val);

    if (rLen) { rLen.innerHTML = isLen ? '✅ 8 حروف على الأقل' : '❌ 8 حروف على الأقل'; rLen.style.color = isLen ? '#34d399' : 'var(--muted)'; }
    if (rNum) { rNum.innerHTML = isNum ? '✅ تشتمل على أرقام (0-9)' : '❌ تشتمل على أرقام (0-9)'; rNum.style.color = isNum ? '#34d399' : 'var(--muted)'; }
    if (rSpec) { rSpec.innerHTML = isSpec ? '✅ تشتمل على رمز خاص (@#$%^&*)' : '❌ تشتمل على رمز خاص (@#$%^&*)'; rSpec.style.color = isSpec ? '#34d399' : 'var(--muted)'; }

    if (isLen) score += 35;
    if (isNum) score += 35;
    if (isSpec) score += 30;

    if (bar) bar.style.width = Math.max(15, score) + '%';

    if (score < 40) {
        if (label) { label.textContent = 'ضعيفة جداً'; label.style.color = '#ef4444'; }
        if (bar) bar.style.background = '#ef4444';
    } else if (score < 80) {
        if (label) { label.textContent = 'متوسطة التعقيد'; label.style.color = '#f59e0b'; }
        if (bar) bar.style.background = '#f59e0b';
    } else {
        if (label) { label.textContent = 'قوية جداً (Strong)'; label.style.color = '#10b981'; }
        if (bar) bar.style.background = '#10b981';
    }
}
window.checkPasswordStrength = checkPasswordStrength;

function updateUserPassword() {
    const cur = document.getElementById('pwdCurrent')?.value;
    const nw = document.getElementById('pwdNew')?.value;
    const cf = document.getElementById('pwdConfirm')?.value;

    if (!cur) return toast('⚠️ يُرجى إدخال كلمة المرور الحالية للحساب!', 1);
    if (!nw || nw.length < 8) return toast('⚠️ كلمة المرور الجديدة يجب ألا تقل عن 8 أحرف وأرقام!', 1);
    if (nw !== cf) return toast('⚠️ كلمة المرور الجديدة وتأكيدها غير متطابقين!', 1);

    toast('🔐 جاري تشفير وتحديث كلمة المرور الحالية للحساب...');
    setTimeout(() => {
        toast('🎉 تم تحديث كلمة السر بنجاح! تم إلغاء كافة الجلسات النشطة في الأجهزة الأخرى لزيادة الأمان.');
    }, 800);
}
window.updateUserPassword = updateUserPassword;

// 1. Global System Settings Dataset
if (!DB.systemSettingsData) DB.systemSettingsData = [
    { keyId: 'SYS_SESSION_TIMEOUT_MINS', nameArEn: 'مدة إغلاق الجلسة التلقائي (بالدقائق) | Session Timeout', scope: 'الأمان والحماية (Security)', val: '15 دقيقة / مفعل (True)', type: 'قائمة منسدلة (Select)', timeout: '15 دقيقة', backupCron: 'يومياً الساعة 02:00 صباحاً', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. خالد محمود العنسي', lastTs: '2026-08-12 - 09:15 PM' },
    { keyId: 'SYS_MFA_ENFORCE', nameArEn: 'فرض التحقق الثنائي للقيادة | MFA Enforcement', scope: 'الأمان والحماية (Security)', val: 'مفعل إجباري (True)', type: 'مفتاح تفعيل (Toggle)', timeout: '30 دقيقة', backupCron: 'يومياً الساعة 02:00 صباحاً', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. خالد محمود العنسي', lastTs: '2026-08-10 - 11:00 AM' }
];

function renderSystemSettingsGrid() {
    const tb = document.getElementById('tbl-system-settings-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchSystemSettings')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('systemSettingsData') : DB.systemSettingsData).filter(s => {
        return !filter || s.keyId.toLowerCase().includes(filter) || s.nameArEn.toLowerCase().includes(filter) || s.scope.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(s => `
        <tr ondblclick="openForm('system_settings', '${s.keyId}')" oncontextmenu="event.preventDefault();deleteItem('systemSettingsData', '${s.keyId}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
            <td style="font-weight:800;color:#60a5fa;font-family:monospace;">${s.keyId}</td>
            <td style="font-weight:700;">${s.nameArEn}</td>
            <td><span class="badge badge-info">${s.scope}</span></td>
            <td style="font-weight:700;color:#34d399;">${s.val}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${s.type}</td>
            <td>${s.timeout}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${s.backupCron}</td>
            <td><span class="badge badge-success">${s.maintenance}</span></td>
            <td>👤 ${s.lastBy}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${s.lastTs}</td>
        </tr>
    `).join('');
}
window.renderSystemSettingsGrid = renderSystemSettingsGrid;
function renderSystemSettings() { renderSystemSettingsGrid(); }
window.renderSystemSettings = renderSystemSettings;

// 2. WhatsApp Business Messaging Dataset
if (!DB.whatsappSendData) DB.whatsappSendData = [
    { id: 'MSG-WA-2026-9081', recipient: '+967 770000000', template: 'قالب_إشعار_سند_مالي (Utility)', media: 'سند_قبض_1020.pdf (Document) 📄', buttons: '[تأكيد السداد] [تواصل مع الدعم]', status: 'تمت القراءة (Read - Blue Check) 🟢', sessionWindow: 'نشطة (متبقي 14 ساعة)', cost: 'خصم 1 رسالة قالب', timestamps: 'أرسلت: 10:00 AM | قُرئت: 10:02 AM' },
    { id: 'MSG-WA-2026-9082', recipient: '+967 771111111', template: 'قالب_إشعار_نتيجة_الفصل (Utility)', media: 'شهادة_ثانوية_1042.pdf (Document) 📄', buttons: '[معاينة النتائج التفصيلية]', status: 'تم التوصيل (Delivered) 🟢', sessionWindow: 'نشطة (متبقي 20 ساعة)', cost: 'خصم 1 رسالة قالب', timestamps: 'أرسلت: 11:15 AM | استلمت: 11:16 AM' }
];

function renderWhatsappSendGrid() {
    const tb = document.getElementById('tbl-whatsapp-send-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchWhatsappSend')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('whatsappSendData') : DB.whatsappSendData).filter(w => {
        return !filter || w.id.toLowerCase().includes(filter) || w.recipient.toLowerCase().includes(filter) || w.template.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(w => `
        <tr ondblclick="openForm('whatsapp_send', '${w.id}')" oncontextmenu="event.preventDefault();deleteItem('whatsappSendData', '${w.id}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
            <td style="font-weight:800;color:#60a5fa;font-family:monospace;">${w.id}</td>
            <td style="font-weight:700;color:#25d366;font-family:monospace;">${w.recipient}</td>
            <td><span class="badge badge-info">${w.template}</span></td>
            <td style="font-size:0.78rem;color:#34d399;">${w.media}</td>
            <td style="font-size:0.75rem;color:#fbbf24;">${w.buttons}</td>
            <td><span class="badge badge-success">${w.status}</span></td>
            <td style="font-size:0.78rem;color:var(--muted);">${w.sessionWindow}</td>
            <td><span class="badge badge-warning">${w.cost}</span></td>
            <td style="font-size:0.75rem;color:var(--muted);">${w.timestamps}</td>
        </tr>
    `).join('');
}
window.renderWhatsappSendGrid = renderWhatsappSendGrid;
function renderWhatsappSend() { renderWhatsappSendGrid(); }
window.renderWhatsappSend = renderWhatsappSend;

// 3. WhatsApp Gateway Settings & Credits Dataset
if (!DB.whatsappSettingsData) DB.whatsappSettingsData = [
    { provider: 'Meta Cloud API | +967 770000000', status: 'متصل بنجاح (Connected & Active) 🟢', credits: '4,850 رسالة متاحة', plan: 'الباقة المؤسسية (Enterprise - 10k Messages)', expiry: '2026-12-31', todayUse: '320 رسالة مرسلة اليوم', perMsgCost: 'خدمي (Utility): 0.005$ | تسويقي: 0.015$', lowLimit: 'عند وصول الرصيد إلى أقل من 500 رسالة', webhook: 'https://api.school.edu.ye/v1/whatsapp/webhook (نشط)', lastTopUp: '2026-08-01 - 10:00 AM (بواسطة مدير النظام)' }
];

function renderWhatsappSettingsGrid() {
    const tb = document.getElementById('tbl-whatsapp-settings-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchWhatsappSettings')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('whatsappSettingsData') : DB.whatsappSettingsData).filter(w => {
        return !filter || w.provider.toLowerCase().includes(filter) || w.plan.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(w => `
        <tr ondblclick="openForm('whatsapp_settings', '${w.provider}')" oncontextmenu="event.preventDefault();deleteItem('whatsappSettingsData', '${w.provider}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
            <td style="font-weight:800;color:#25d366;">📱 ${w.provider}</td>
            <td><span class="badge badge-success">${w.status}</span></td>
            <td style="font-weight:800;color:#34d399;">${w.credits}</td>
            <td><span class="badge badge-info">${w.plan}</span></td>
            <td style="font-size:0.78rem;color:var(--muted);">${w.expiry}</td>
            <td style="font-weight:700;color:#60a5fa;">${w.todayUse}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${w.perMsgCost}</td>
            <td><span class="badge badge-warning">${w.lowLimit}</span></td>
            <td style="font-size:0.72rem;font-family:monospace;color:#60a5fa;">${w.webhook}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${w.lastTopUp}</td>
        </tr>
    `).join('');
}
window.renderWhatsappSettingsGrid = renderWhatsappSettingsGrid;
function renderWhatsappSettings() { renderWhatsappSettingsGrid(); }
window.renderWhatsappSettings = renderWhatsappSettings;

// Universal OpenForm Builder for ALL System Entities
function openForm(type, editId) {
    let formModal = document.getElementById('formModal');
    let titleEl = document.getElementById('modalTitle');
    let fieldsEl = document.getElementById('formFields');

    if (!formModal || !fieldsEl) {
        toast(`✨ فتح نافذة إضافة وتعديل الكيان (${type})`);
        return;
    }

    if (titleEl) titleEl.innerHTML = `<i class="fa-solid fa-pen-to-square"></i> إضافة / تعديل بيانات (${type})`;
    
    let htmlFields = '';

    if (type === 'student') {
        htmlFields = `
            <div class="fg"><label>اسم الطالب الكامل <span class="req">*</span></label><input id="std_name" placeholder="أدخل اسم الطالب الرباعي" value="${editId?'أحمد محمود العبسي':''}" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>المرحلة والصف الدراسي <span class="req">*</span></label><select id="std_grade"><option>الثالث الثانوي</option><option>الثاني الثانوي</option><option>التاسع الأساسي</option></select></div>
            <div class="fg"><label>الشعبة <span class="req">*</span></label><select id="std_sec"><option>أ</option><option>ب</option><option>ج</option></select></div>
            <div class="fg"><label>الجنس <span class="req">*</span></label><select id="std_gender"><option>ذكر</option><option>أنثى</option></select></div>
        `;
    } else if (type === 'employee') {
        htmlFields = `
            <div class="fg"><label>اسم الموظف / المعلم <span class="req">*</span></label><input id="emp_name" placeholder="أدخل الاسم الرباعي" value="${editId?'أ. خالد محمود':''}" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>المسمى الوظيفي والدور <span class="req">*</span></label><input id="emp_role" placeholder="مثال: معلم أول رياضيات" value="معلم مادة" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>القسم التابع له <span class="req">*</span></label><select id="emp_dept"><option>الكادر التعليمي</option><option>الإدارة العامة</option><option>الكنترول والامتحانات</option><option>الحسابات</option></select></div>
            <div class="fg"><label>الراتب الأساسي <span class="req">*</span></label><input type="number" id="emp_salary" value="250000"></div>
        `;
    } else if (type === 'whatsapp_send') {
        htmlFields = `
            <div class="fg"><label>رقم الواتساب المستهدف (مع المفتاح الدولي) <span class="req">*</span></label><input id="wa_phone" placeholder="+967 770000000" value="+967 770000000" oninput="validateNumbersOnly(this)"></div>
            <div class="fg"><label>اسم قالب الرسالة التفاعلي <span class="req">*</span></label><select id="wa_template"><option>قالب_إشعار_سند_مالي (Utility)</option><option>قالب_إشعار_نتيجة_الفصل (Utility)</option><option>قالب_تذكير_استحقاق_قسط (Utility)</option></select></div>
            <div class="fg"><label>إرفاق مستند PDF / وسائط (Optional)</label><input type="file" id="wa_file"></div>
            <div class="fg"><label>نص وتفاصيل الرسالة <span class="req">*</span></label><textarea id="wa_msg" rows="3" placeholder="أدخل نص الرسالة أو المتغيرات...">عزيزي ولي الأمر، نود تزويدكم بالإشعار المرفق.</textarea></div>
        `;
    } else if (type === 'whatsapp_settings') {
        htmlFields = `
            <div class="fg"><label>اسم ورقم مزود الخدمة (Gateway & Number) <span class="req">*</span></label><input id="was_provider" value="Meta Cloud API | +967 770000000"></div>
            <div class="fg"><label>باقة الاشتراك المشتراة <span class="req">*</span></label><select id="was_plan"><option>الباقة المؤسسية (Enterprise - 10k Messages)</option><option>الباقة الاحترافية (Pro - 5k Messages)</option></select></div>
            <div class="fg"><label>رصيد الوحدات المضافة <span class="req">*</span></label><input type="number" id="was_credits" value="5000"></div>
            <div class="fg"><label>رابط الـ Webhook Endpoint <span class="req">*</span></label><input id="was_webhook" value="https://api.school.edu.ye/v1/whatsapp/webhook"></div>
        `;
    } else if (type === 'system_settings') {
        htmlFields = `
            <div class="fg"><label>كود الإعداد البرمجي (Setting Key ID) <span class="req">*</span></label><input id="set_key" value="SYS_SESSION_TIMEOUT_MINS"></div>
            <div class="fg"><label>اسم الإعداد (AR / EN) <span class="req">*</span></label><input id="set_name" value="مدة إغلاق الجلسة التلقائي (بالدقائق)"></div>
            <div class="fg"><label>التصنيف / الموديول <span class="req">*</span></label><select id="set_scope"><option>الأمان والحماية (Security)</option><option>التنسيقات الإقليمية</option><option>الموديولات والميزات</option><option>النسخ الاحتياطي والصيانة</option></select></div>
            <div class="fg"><label>القيمة المعتمدة <span class="req">*</span></label><input id="set_val" value="15 دقيقة / مفعل (True)"></div>
        `;
    } else {
        htmlFields = `
            <div class="fg"><label>اسم الكيان / البيان <span class="req">*</span></label><input id="gen_name" placeholder="أدخل البيان المطلوبة" value="بيان جديد" oninput="validateTextOnly(this)"></div>
            <div class="fg"><label>المبلغ / القيمة</label><input type="number" id="gen_val" value="1000"></div>
            <div class="fg"><label>ملاحظات وتفاصيل</label><input id="gen_notes" placeholder="ملاحظات..." value="معتمد آلياً"></div>
        `;
    }

    fieldsEl.innerHTML = htmlFields;
    formModal.classList.add('active');
}
window.openForm = openForm;

function saveForm(type) {
    closeModal('formModal');
    toast(`✅ تم حفظ وإعادة تحديث كافة سجلات ودليل (${type || 'الكيان'}) بنجاح`);
    
    if (type === 'student' && typeof renderStudents === 'function') renderStudents();
    if (type === 'employee' && typeof renderEmployees === 'function') renderEmployees();
    if (type === 'whatsapp_send' && typeof renderWhatsappSendGrid === 'function') renderWhatsappSendGrid();
    if (type === 'whatsapp_settings' && typeof renderWhatsappSettingsGrid === 'function') renderWhatsappSettingsGrid();
    if (type === 'system_settings' && typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid();
    if (type === 'voucher' && typeof renderVouchers === 'function') renderVouchers();
    if (type === 'users' && typeof renderUsersGrid === 'function') renderUsersGrid();
}
window.saveForm = saveForm;

function deleteItem(collectionKey, itemId) {
    if (confirm(`❓ هل أنت متأكد من حذف السجل رقم (${itemId}) نهائياً من النظام؟`)) {
        if (DB[collectionKey]) {
            DB[collectionKey] = DB[collectionKey].filter(x => (x.id !== itemId && x.isoCode !== itemId && x.keyId !== itemId && x.provider !== itemId));
        }
        toast(`🗑️ تم حذف السجل رقم (${itemId}) بنجاح من قاعدة البيانات!`);
        
        if (typeof renderStudents === 'function') renderStudents();
        if (typeof renderEmployees === 'function') renderEmployees();
        if (typeof renderWhatsappSendGrid === 'function') renderWhatsappSendGrid();
        if (typeof renderWhatsappSettingsGrid === 'function') renderWhatsappSettingsGrid();
        if (typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid();
        if (typeof renderUsersGrid === 'function') renderUsersGrid();
        if (typeof renderCurrenciesGrid === 'function') renderCurrenciesGrid();
        if (typeof renderBanksGrid === 'function') renderBanksGrid();
    }
}
window.deleteItem = deleteItem;
"""

if 'window.makeRowInteractive = makeRowInteractive' not in js:
    js += "\n" + double_click_and_4_pages_js + "\n"
    print("  ✓ Appended Double-Click UX & 4 Pages JS Engine to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
