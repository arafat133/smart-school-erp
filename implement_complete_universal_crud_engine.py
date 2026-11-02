"""
Implement Complete Universal Dynamic Form & CRUD Engine in app.js
"""
import re, time

print("=" * 60)
print("Injecting Complete Universal Dynamic Form & CRUD Engine in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove duplicate openForm / saveForm / deleteItem declarations to ensure SINGLE unified engine
js = re.sub(r'// ==================== ROBUST MODAL & FORM BUILDER ENGINE ====================.*?(?=function hydrateAndMountAllGrids|\Z)', '', js, flags=re.DOTALL)
js = re.sub(r'function openForm\(.*?\)\s*\{.*?\}\s*window\.openForm\s*=\s*openForm;', '', js, flags=re.DOTALL)
js = re.sub(r'function saveForm\(.*?\)\s*\{.*?\}\s*window\.saveForm\s*=\s*saveForm;', '', js, flags=re.DOTALL)
js = re.sub(r'function deleteItem\(.*?\)\s*\{.*?\}\s*window\.deleteItem\s*=\s*deleteItem;', '', js, flags=re.DOTALL)

crud_engine_js = """
// ==================== COMPLETE UNIVERSAL DYNAMIC FORM & CRUD ENGINE ====================

window.currentEditingType = null;
window.currentEditingId = null;

function closeModal(id) {
    const m = document.getElementById(id || 'formModal');
    if (m) {
        m.classList.remove('active');
        m.style.display = 'none';
    }
}
window.closeModal = closeModal;

function getCollectionKey(type) {
    const mapping = {
        'student': 'students',
        'employee': 'employees',
        'user': 'usersData',
        'users': 'usersData',
        'voucher': 'vouchers',
        'journal': 'vouchers',
        'subject': 'subjects',
        'currencies': 'currenciesData',
        'cashbox_inventory': 'cashboxInventoryData',
        'closings': 'closingsData',
        'banks': 'banksData',
        'demand_letters': 'demandLettersData',
        'system_settings': 'systemSettingsData',
        'whatsapp_send': 'whatsappSendData',
        'whatsapp_settings': 'whatsappSettingsData',
        'alerts': 'alertsData',
        'archive': 'archiveData',
        'posting': 'postingData',
        'inventory': 'inventory_items',
        'activity': 'activities',
        'transport': 'transport'
    };
    return mapping[type] || (type + 'Data');
}

function openForm(type, editId) {
    type = type || 'student';
    window.currentEditingType = type;
    window.currentEditingId = editId || null;

    let formModal = document.getElementById('formModal');
    if (!formModal) {
        formModal = document.createElement('div');
        formModal.className = 'modal';
        formModal.id = 'formModal';
        formModal.innerHTML = `
            <div class="modal-content">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:12px;">
                    <h3 id="modalTitle" style="margin:0;color:#60a5fa;font-size:1.1rem;"><i class="fa-solid fa-pen-to-square"></i> إضافة / تعديل بيانات</h3>
                    <button onclick="closeModal('formModal')" style="background:none;border:none;color:#ef4444;font-size:1.4rem;cursor:pointer;">&times;</button>
                </div>
                <div id="formFields"></div>
                <div style="display:flex;gap:10px;justify-content:flex-end;margin-top:20px;">
                    <button class="btn-cancel" onclick="closeModal('formModal')" style="padding:8px 16px;border-radius:8px;background:#374151;color:#fff;border:none;cursor:pointer;">إلغاء</button>
                    <button class="btn-save" onclick="saveForm(window.currentEditingType)" style="padding:8px 20px;border-radius:8px;background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;border:none;cursor:pointer;font-weight:700;">حفظ البيانات</button>
                </div>
            </div>
        `;
        document.body.appendChild(formModal);
    }

    let titleEl = document.getElementById('modalTitle');
    let fieldsEl = document.getElementById('formFields');

    // Fetch existing record if editing
    const collectionKey = getCollectionKey(type);
    const collection = DB[collectionKey] || [];
    let rec = editId ? collection.find(x => (x.id == editId || x.keyId == editId || x.isoCode == editId || x.provider == editId)) : null;

    if (titleEl) {
        titleEl.innerHTML = editId ? 
            `<i class="fa-solid fa-pen"></i> تعديل بيانات (${type} - ${editId})` : 
            `<i class="fa-solid fa-plus"></i> إضافة بيانات جديدة (${type})`;
    }

    let htmlFields = '';

    if (type === 'student') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم الطالب الرباعي <span style="color:#ef4444;">*</span></label><input id="f_std_name" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" placeholder="أدخل اسم الطالب الرباعي" value="${rec ? rec.name : ''}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">المرحلة والصف الدراسي</label><select id="f_std_grade" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;"><option ${rec&&rec.grade==='الثالث الثانوي'?'selected':''}>الثالث الثانوي</option><option ${rec&&rec.grade==='الثاني الثانوي'?'selected':''}>الثاني الثانوي</option><option ${rec&&rec.grade==='التاسع الأساسي'?'selected':''}>التاسع الأساسي</option></select></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">الشعبة</label><select id="f_std_sec" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;"><option ${rec&&rec.section==='أ'?'selected':''}>أ</option><option ${rec&&rec.section==='ب'?'selected':''}>ب</option><option ${rec&&rec.section==='ج'?'selected':''}>ج</option></select></div>
        `;
    } else if (type === 'employee') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم الموظف / المعلم <span style="color:#ef4444;">*</span></label><input id="f_emp_name" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" placeholder="أدخل اسم الموظف الكامل" value="${rec ? rec.name : ''}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">المسمى الوظيفي والدور</label><input id="f_emp_role" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.role : 'معلم مادة'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">الراتب الأساسي</label><input type="number" id="f_emp_salary" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.salary : '250000'}"></div>
        `;
    } else if (type === 'whatsapp_send') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">الرقم المستهدف (WhatsApp) <span style="color:#ef4444;">*</span></label><input id="f_wa_phone" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" placeholder="+967 770000000" value="${rec ? rec.recipient : '+967 770000000'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم ونوع القالب المعتمد</label><input id="f_wa_template" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.template : 'قالب_إشعار_سند_مالي (Utility)'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">المرفقات والوسائط (Document PDF)</label><input id="f_wa_media" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.media : 'سند_قبض_1020.pdf (Document)'}"></div>
        `;
    } else if (type === 'whatsapp_settings') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم ورقم مزود الخدمة <span style="color:#ef4444;">*</span></label><input id="f_was_provider" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.provider : 'Meta Cloud API | +967 770000000'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">رصيد الوحدات المتاحة</label><input id="f_was_credits" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.credits : '5,000 رسالة متاحة'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">رابط Webhook Endpoint</label><input id="f_was_webhook" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.webhook : 'https://api.school.edu.ye/v1/whatsapp/webhook'}"></div>
        `;
    } else if (type === 'system_settings') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">كود الإعداد البرمجي (Setting Key ID) <span style="color:#ef4444;">*</span></label><input id="f_set_key" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.keyId : 'SYS_SESSION_TIMEOUT_MINS'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم الإعداد (AR / EN)</label><input id="f_set_name" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.nameArEn : 'مدة إغلاق الجلسة التلقائي (بالدقائق)'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">القيمة الحالية المعتمدة</label><input id="f_set_val" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.val : '15 دقيقة / مفعل (True)'}"></div>
        `;
    } else if (type === 'currencies') {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">كود العملة الدولي (ISO Code) <span style="color:#ef4444;">*</span></label><input id="f_cur_code" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.isoCode : 'USD'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">اسم العملة (AR / EN)</label><input id="f_cur_name" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.nameArEn : 'دولار أمريكي | US Dollar'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">سعر الصرف الرسمي مقابل الأساسية</label><input id="f_cur_rate" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? rec.officialRate : '1 USD = 530 YER'}"></div>
        `;
    } else {
        htmlFields = `
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">الاسم / المعرف الرئيسي <span style="color:#ef4444;">*</span></label><input id="f_gen_name" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" placeholder="أدخل البيان المطلوبة..." value="${rec ? (rec.name || rec.id || rec.safeName || rec.bankNameBranch || rec.payerName) : ''}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">التصنيف / الحالة</label><input id="f_gen_cat" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? (rec.status || rec.accType || 'نشط 🟢') : 'نشط 🟢'}"></div>
            <div class="fg" style="margin-bottom:12px;"><label style="display:block;margin-bottom:4px;font-size:0.85rem;color:#94a3b8;">المبلغ / الرصيد المسجل</label><input id="f_gen_val" style="width:100%;padding:8px 12px;border-radius:8px;background:rgba(15,23,42,0.8);border:1px solid #334155;color:#fff;" value="${rec ? (rec.amount || rec.bookBalance || rec.salary || '100,000 YER') : '100,000 YER'}"></div>
        `;
    }

    if (fieldsEl) fieldsEl.innerHTML = htmlFields;

    formModal.style.display = 'flex';
    formModal.classList.add('active');
    toast(`✨ تم فتح نافذة ${editId?'تعديل':'إضافة'} بيانات (${type})`);
}
window.openForm = openForm;

function saveForm(type) {
    type = type || window.currentEditingType || 'student';
    const collectionKey = getCollectionKey(type);
    if (!DB[collectionKey]) DB[collectionKey] = [];

    const editId = window.currentEditingId;

    if (type === 'student') {
        const name = document.getElementById('f_std_name')?.value || 'طالب جديد';
        const grade = document.getElementById('f_std_grade')?.value || 'الثالث الثانوي';
        const section = document.getElementById('f_std_sec')?.value || 'أ';
        if (editId) {
            let item = DB[collectionKey].find(x => x.id == editId);
            if (item) { item.name = name; item.grade = grade; item.section = section; }
        } else {
            DB[collectionKey].unshift({ id: Date.now(), schoolId: 1, name: name, grade: grade, section: section, gender: 'ذكر', status: 'مستمر' });
        }
    } else if (type === 'employee') {
        const name = document.getElementById('f_emp_name')?.value || 'موظف جديد';
        const role = document.getElementById('f_emp_role')?.value || 'معلم';
        const salary = document.getElementById('f_emp_salary')?.value || 250000;
        if (editId) {
            let item = DB[collectionKey].find(x => x.id == editId);
            if (item) { item.name = name; item.role = role; item.salary = salary; }
        } else {
            DB[collectionKey].unshift({ id: Date.now(), schoolId: 1, name: name, role: role, dept: 'الكادر التعليمي', salary: salary, status: 'نشط 🟢' });
        }
    } else if (type === 'whatsapp_send') {
        const recipient = document.getElementById('f_wa_phone')?.value || '+967 770000000';
        const template = document.getElementById('f_wa_template')?.value || 'قالب_خدمي';
        const media = document.getElementById('f_wa_media')?.value || 'مستند.pdf';
        if (editId) {
            let item = DB[collectionKey].find(x => x.id == editId);
            if (item) { item.recipient = recipient; item.template = template; item.media = media; }
        } else {
            DB[collectionKey].unshift({ id: 'MSG-WA-' + Date.now().toString().slice(-4), recipient: recipient, template: template, media: media, buttons: '[تأكيد]', status: 'تمت القراءة 🟢', sessionWindow: 'نشطة', cost: 'خصم 1 رسالة', timestamps: 'أرسلت: الآن' });
        }
    } else if (type === 'whatsapp_settings') {
        const provider = document.getElementById('f_was_provider')?.value || 'Meta Cloud API';
        const credits = document.getElementById('f_was_credits')?.value || '5,000 رسالة';
        const webhook = document.getElementById('f_was_webhook')?.value || 'https://api.school.edu.ye/v1/whatsapp/webhook';
        if (editId) {
            let item = DB[collectionKey].find(x => x.provider == editId);
            if (item) { item.provider = provider; item.credits = credits; item.webhook = webhook; }
        } else {
            DB[collectionKey].unshift({ provider: provider, status: 'متصل بنجاح 🟢', credits: credits, plan: 'الباقة المؤسسية', expiry: '2026-12-31', todayUse: '10 رسائل', perMsgCost: '0.005$', lowLimit: 'أقل من 500', webhook: webhook, lastTopUp: 'الآن' });
        }
    } else if (type === 'system_settings') {
        const keyId = document.getElementById('f_set_key')?.value || 'SYS_CUSTOM_KEY';
        const nameArEn = document.getElementById('f_set_name')?.value || 'إعداد جديد';
        const val = document.getElementById('f_set_val')?.value || 'مفعل';
        if (editId) {
            let item = DB[collectionKey].find(x => x.keyId == editId);
            if (item) { item.nameArEn = nameArEn; item.val = val; }
        } else {
            DB[collectionKey].unshift({ keyId: keyId, nameArEn: nameArEn, scope: 'عام (General)', val: val, type: 'مفتاح تفعيل', timeout: '15 دقيقة', backupCron: 'يومياً', maintenance: 'غير مفعل 🟢', lastBy: 'مدير النظام', lastTs: 'الآن' });
        }
    } else {
        const gName = document.getElementById('f_gen_name')?.value || 'سجل جديد';
        const gCat = document.getElementById('f_gen_cat')?.value || 'نشط 🟢';
        const gVal = document.getElementById('f_gen_val')?.value || '100,000 YER';
        if (editId) {
            let item = DB[collectionKey].find(x => x.id == editId);
            if (item) { if (item.name) item.name = gName; item.status = gCat; }
        } else {
            DB[collectionKey].unshift({ id: 'REC-' + Date.now().toString().slice(-4), name: gName, status: gCat, amount: gVal, date: '2026-08-12' });
        }
    }

    closeModal('formModal');
    if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();
    toast(`🎉 تم حفظ وإعادة رسم كشف بيانات (${type}) بنجاح!`);
}
window.saveForm = saveForm;

function deleteItem(collectionKey, itemId) {
    if (!collectionKey) return;
    if (confirm(`❓ هل أنت متأكد من رغبتك في حذف السجل رقم (${itemId}) نهائياً؟`)) {
        if (DB[collectionKey]) {
            DB[collectionKey] = DB[collectionKey].filter(x => (x.id != itemId && x.isoCode != itemId && x.keyId != itemId && x.provider != itemId));
        }
        if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();
        toast(`🗑️ تم حذف السجل رقم (${itemId}) بنجاح من قاعدة البيانات!`);
    }
}
window.deleteItem = deleteItem;
"""

js += "\n" + crud_engine_js + "\n"

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with Complete Universal Form Builder & CRUD Engine!")
