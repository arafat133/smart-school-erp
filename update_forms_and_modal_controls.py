import re
import os

app_js_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\app.js"
style_css_path = r"c:\Users\LENOVO\Desktop\stu\secure_school_system\frontend\style.css"

with open(app_js_path, "r", encoding="utf-8") as f:
    js_code = f.read()

# 1. Update minModal, openModal, closeModal, and add enableModalDragging
modal_functions = '''
// ==================== UNIVERSAL MODAL CONTROLS & DRAGGING ====================

function openModal(id) {
    const m = document.getElementById(id);
    if (m) {
        m.classList.remove('minimized-overlay');
        m.classList.add('active');
        m.style.display = 'flex';
        const c = m.querySelector('.modal-content');
        if (c) {
            c.classList.remove('minimized');
            c.style.left = '';
            c.style.top = '';
            c.style.position = '';
            c.style.margin = '';
        }
        enableModalDragging();
    }
}
window.openModal = openModal;

function closeModal(id) {
    const m = document.getElementById(id);
    if (m) {
        m.classList.remove('active', 'minimized-overlay');
        m.style.display = 'none';
        const c = m.querySelector('.modal-content');
        if (c) {
            c.classList.remove('minimized');
            c.style.left = '';
            c.style.top = '';
            c.style.position = '';
            c.style.margin = '';
        }
    }
}
window.closeModal = closeModal;

function minModal(id) {
    const m = document.getElementById(id);
    if (!m) return;
    const content = m.querySelector('.modal-content');
    if (content) {
        const isMin = content.classList.toggle('minimized');
        if (isMin) {
            m.classList.add('minimized-overlay');
            toast('📉 تم تصغير النافذة إلى الشريط السفلي (انقر عليها لاستعادتها)');
        } else {
            m.classList.remove('minimized-overlay');
            toast('📈 تم استعادة النافذة بنجاح');
        }
    } else {
        closeModal(id);
    }
}
window.minModal = minModal;

function enableModalDragging() {
    document.querySelectorAll('.modal-header').forEach(header => {
        if (header.dataset.dragBound) return;
        header.dataset.dragBound = 'true';
        header.style.cursor = 'grab';
        header.title = 'انقر واسحب لتحريك النافذة';

        let isDragging = false;
        let startX, startY, initialLeft, initialTop;
        const modalContent = header.closest('.modal-content');
        if (!modalContent) return;

        header.addEventListener('click', (e) => {
            if (modalContent.classList.contains('minimized') && !e.target.closest('button')) {
                minModal(modalContent.closest('.modal-overlay')?.id || 'formModal');
            }
        });

        header.addEventListener('mousedown', (e) => {
            if (e.target.closest('button') || e.target.closest('a') || e.target.closest('input')) return;
            if (modalContent.classList.contains('minimized')) return;

            isDragging = true;
            header.style.cursor = 'grabbing';
            startX = e.clientX;
            startY = e.clientY;

            const rect = modalContent.getBoundingClientRect();
            initialLeft = rect.left;
            initialTop = rect.top;

            modalContent.style.position = 'fixed';
            modalContent.style.left = initialLeft + 'px';
            modalContent.style.top = initialTop + 'px';
            modalContent.style.margin = '0';

            const onMouseMove = (moveEvent) => {
                if (!isDragging) return;
                const dx = moveEvent.clientX - startX;
                const dy = moveEvent.clientY - startY;
                modalContent.style.left = (initialLeft + dx) + 'px';
                modalContent.style.top = (initialTop + dy) + 'px';
            };

            const onMouseUp = () => {
                isDragging = false;
                header.style.cursor = 'grab';
                document.removeEventListener('mousemove', onMouseMove);
                document.removeEventListener('mouseup', onMouseUp);
            };

            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        });
    });
}
window.enableModalDragging = enableModalDragging;
'''

# Substitute openModal & minModal if they exist, or append enableModalDragging
if 'function minModal' in js_code:
    js_code = re.sub(r'function minModal\(id\)\s*\{[^}]*\}', '', js_code)
if 'window.minModal = minModal;' in js_code:
    js_code = js_code.replace('window.minModal = minModal;', '')

# Insert modal_functions at top of JS file
js_code = modal_functions + '\n' + js_code

# Replace getFormFields, getCollectionKey, openForm, saveForm
full_form_engine = '''
// ==================== UNIVERSAL COMPLETE FORM FIELDS DEFINITIONS (77+ ENTITIES) ====================

function getFormFields(type) {
    const fieldDefs = {
        'student': [
            {id:'f_name', label:'اسم الطالب الرباعي الكامل', type:'text', required:true, placeholder:'أدخل اسم الطالب الرباعي', key:'name'},
            {id:'f_grade', label:'المرحلة والصف الدراسي', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي','التاسع الأساسي','الثامن الأساسي','السابع الأساسي'], key:'grade'},
            {id:'f_section', label:'الشعبة الدراسية', type:'select', options:['أ','ب','ج','د'], key:'section'},
            {id:'f_gender', label:'الجنس', type:'select', options:['ذكر','أنثى'], key:'gender'},
            {id:'f_gname', label:'اسم ولي الأمر المكفول', type:'text', placeholder:'اسم ولي الأمر الكامل', key:'guardianName'},
            {id:'f_gphone', label:'رقم هاتف ولي الأمر (واتساب)', type:'text', placeholder:'+967 770000000', key:'guardianPhone'},
            {id:'f_fee', label:'إجمالي الرسوم السنوية المقررة', type:'text', placeholder:'450,000 YER', key:'totalFee'},
            {id:'f_status', label:'حالة القيد الطلابي', type:'select', options:['مستمر','متوقف','خريج','منسحب'], key:'status'}
        ],
        'employee': [
            {id:'f_name', label:'اسم الموظف / المعلم الكامل', type:'text', required:true, placeholder:'أدخل الاسم الثلاثي/الرباعي', key:'name'},
            {id:'f_role', label:'المسمى الوظيفي والدور القيادي', type:'text', placeholder:'معلم مادة / مدير قسم / محاسب', key:'role'},
            {id:'f_dept', label:'القسم / الإدارة التابع لها', type:'select', options:['الإدارة العامة','الكادر التعليمي','الحسابات والمالية','إدارة الامتحانات','شؤون الطلاب'], key:'dept'},
            {id:'f_salary', label:'الراتب الأساسي الشهري (YER)', type:'number', placeholder:'250000', key:'salary'},
            {id:'f_phone', label:'رقم الهاتف الجوال', type:'text', placeholder:'+967 770000000', key:'phone'},
            {id:'f_qual', label:'المؤهل العلمي والتخصص', type:'text', placeholder:'بكالوريوس / ماجستير', key:'qualification'},
            {id:'f_status', label:'حالة العمل الوظيفي', type:'select', options:['نشط 🟢','موقوف 🔴','إجازة 🟡'], key:'status'}
        ],
        'users': [
            {id:'f_name', label:'اسم المستخدم الكامل', type:'text', required:true, placeholder:'أدخل اسم المستخدم الكامل', key:'name'},
            {id:'f_username', label:'اسم تسجيل الدخول (Username)', type:'text', required:true, placeholder:'admin_user', key:'username'},
            {id:'f_role', label:'الصلاحية والمستوى الاستئذاني', type:'select', options:['مدير النظام','مسؤول الكنترول','محاسب','معلم','ولي أمر','طالب'], key:'roleName'},
            {id:'f_email', label:'البريد الإلكتروني المعتمد', type:'email', placeholder:'user@school.edu.ye', key:'email'},
            {id:'f_status', label:'حالة الحساب الإلكتروني', type:'select', options:['نشط 🟢','معطل 🔴','مقفل 🟡'], key:'status'}
        ],
        'school': [
            {id:'f_sname', label:'اسم المدرسة / المنشأة التعليمية', type:'text', required:true, placeholder:'مدرسة المتفوقين الأهلية', key:'name'},
            {id:'f_slic', label:'رقم الترخيص الوزاري الرسمي', type:'text', placeholder:'LIC-2026-99', key:'licenseNo'},
            {id:'f_sprin', label:'اسم مدير المنشأة / المدير العام', type:'text', placeholder:'د. عبد الإله سالم', key:'principalName'},
            {id:'f_sphone', label:'رقم هاتف المنشأة الرئيسي', type:'text', placeholder:'+967 01 234567', key:'phone'},
            {id:'f_saddr', label:'العنوان والفرع الرئيسي', type:'text', placeholder:'صنعاء - شارع السبعين', key:'address'}
        ],
        'stage': [
            {id:'f_stg_grade', label:'اسم المرحلة أو الصف الدراسي', type:'text', required:true, placeholder:'الثالث الثانوي', key:'grade'},
            {id:'f_stg_code', label:'كود المرحلة الأكاديمي', type:'text', placeholder:'G12', key:'code'},
            {id:'f_stg_pass', label:'درجة النجاح الدنيا (المعيار)', type:'number', placeholder:'50', key:'passGrade'}
        ],
        'section': [
            {id:'f_sec_name', label:'اسم الشعبة الدراسية', type:'text', required:true, placeholder:'أ', key:'name'},
            {id:'f_sec_grade', label:'الصف التابعة له', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي','التاسع الأساسي'], key:'grade'},
            {id:'f_sec_cap', label:'الطاقة الاستيعابية للطلاب', type:'number', placeholder:'35', key:'capacity'}
        ],
        'subject': [
            {id:'f_sub_name', label:'اسم المادة الدراسية', type:'text', required:true, placeholder:'الرياضيات المتقدمة', key:'name'},
            {id:'f_sub_code', label:'كود المادة البرمجي', type:'text', placeholder:'MATH-301', key:'code'},
            {id:'f_sub_stage', label:'المرحلة المخصصة لها', type:'select', options:['الثانوية','الأساسية','جميع المراحل'], key:'stage'},
            {id:'f_sub_max', label:'الدرجة العظمى المعتمدة', type:'number', placeholder:'100', key:'maxGrade'},
            {id:'f_sub_pass', label:'درجة النجاح الدنيا', type:'number', placeholder:'50', key:'passGrade'}
        ],
        'voucher_receipt': [
            {id:'f_vr_payer', label:'اسم الدافع / ولي الأمر / الطالب', type:'text', required:true, placeholder:'أدخل اسم الدافع', key:'payerName'},
            {id:'f_vr_amt', label:'مبلغ السند المقبوض (YER)', type:'text', required:true, placeholder:'250,000 YER', key:'amount'},
            {id:'f_vr_acc', label:'الحساب المالي المستهدف (الدائن)', type:'select', options:['حساب الرسوم الدراسية','حساب الأنشطة والخدمات','حساب الباصات والنقل'], key:'account'},
            {id:'f_vr_method', label:'طريقة وسيلة الدفع', type:'select', options:['نقدي (Cash)','تحويل بنكي','شيك مصرفي','شبكة POS'], key:'method'},
            {id:'f_vr_notes', label:'البيان والشارح المالي للسند', type:'textarea', placeholder:'شارح تفصيلي لموجب القبض...', key:'notes'}
        ],
        'voucher_payment': [
            {id:'f_vp_payee', label:'اسم المدفوع له / المورد / الجهة', type:'text', required:true, placeholder:'أدخل اسم المستفيد', key:'payerName'},
            {id:'f_vp_amt', label:'المبلغ المصروف (YER)', type:'text', required:true, placeholder:'120,000 YER', key:'amount'},
            {id:'f_vp_acc', label:'حساب المصروفات المستهدف', type:'select', options:['حساب الصيانة والتشغيل','حساب شراء المستلزمات','حساب رواتب الموظفين'], key:'account'},
            {id:'f_vp_method', label:'وسيلة الصرف المالي', type:'select', options:['نقدي (Cash)','شيك بنكي','تحويل بنكي'], key:'method'},
            {id:'f_vp_notes', label:'سبب وسند الصرف التفصيلي', type:'textarea', placeholder:'تفاصيل مبررات الصرف...', key:'notes'}
        ],
        'journal_entry': [
            {id:'f_je_desc', label:'البيان الرئيسي للقيد المحاسبي', type:'text', required:true, placeholder:'قيد تسوية وإقفال شهري', key:'desc'},
            {id:'f_je_debit', label:'حساب الطرف المدين (Debit)', type:'text', placeholder:'حساب الصندوق / البنك', key:'debitAcc'},
            {id:'f_je_credit', label:'حساب الطرف الدائن (Credit)', type:'text', placeholder:'حساب الإيرادات', key:'creditAcc'},
            {id:'f_je_amt', label:'المبلغ المتوازن للقيد (YER)', type:'text', placeholder:'500,000 YER', key:'amount'}
        ],
        'currencies': [
            {id:'f_cur_code', label:'كود العملة الدولي (ISO Code)', type:'text', required:true, placeholder:'USD', key:'isoCode'},
            {id:'f_cur_name', label:'اسم العملة (عربي / إنجليزي)', type:'text', required:true, placeholder:'دولار أمريكي | US Dollar', key:'nameArEn'},
            {id:'f_cur_rate', label:'سعر الصرف الرسمي مقابل الأساسية', type:'text', required:true, placeholder:'1 USD = 530 YER', key:'officialRate'},
            {id:'f_cur_sym', label:'رمز الشعار العملي ($ / ر.ي)', type:'text', placeholder:'$', key:'symbol'}
        ],
        'cashbox_inventory': [
            {id:'f_cb_safe', label:'اسم الصندوق / الخزنة المستهدفة', type:'text', required:true, placeholder:'الصندوق الرئيسي', key:'safeName'},
            {id:'f_cb_book', label:'الرصيد الدفتري المسجل', type:'text', placeholder:'12,450,000 YER', key:'bookBalance'},
            {id:'f_cb_act', label:'الرصيد الفعلي بعد العد والعدالة', type:'text', placeholder:'12,450,000 YER', key:'actualBalance'},
            {id:'f_cb_aud', label:'اسم المحاسب أمين الصندوق / المراجع', type:'text', placeholder:'سارة المحاسبة', key:'auditor'}
        ],
        'closings': [
            {id:'f_cls_name', label:'اسم فترة الإغلاق المحاسبي', type:'text', required:true, placeholder:'الإغلاق المالي للربع الأول 2026', key:'periodName'},
            {id:'f_cls_start', label:'تاريخ بداية الفترة', type:'date', key:'startDate'},
            {id:'f_cls_end', label:'تاريخ نهاية الفترة وتصفية الحسابات', type:'date', key:'endDate'},
            {id:'f_cls_rev', label:'إجمالي الإيرادات المحققة', type:'text', placeholder:'32,100,000 YER', key:'revenue'},
            {id:'f_cls_exp', label:'إجمالي المصروفات والنفقات', type:'text', placeholder:'19,400,000 YER', key:'expense'}
        ],
        'banks': [
            {id:'f_bnk_name', label:'اسم البنك والفرع المعتمد', type:'text', required:true, placeholder:'بنك التضامن - فرع السبعين', key:'bankNameBranch'},
            {id:'f_bnk_iban', label:'رقم الحساب المصرفي (IBAN)', type:'text', placeholder:'YE93TADB00010012345678', key:'iban'},
            {id:'f_bnk_curr', label:'عملة الحساب البنكي', type:'select', options:['YER','USD','SAR','EUR'], key:'currency'},
            {id:'f_bnk_bal', label:'الرصيد الحسابي الحالي', type:'text', placeholder:'85,400,000 YER', key:'currentBalance'},
            {id:'f_bnk_mgr', label:'اسم مدير الفرع / مسؤول الحساب', type:'text', placeholder:'محمد بن يحيى', key:'manager'}
        ],
        'demand_letters': [
            {id:'f_dl_payer', label:'اسم المدين / ولي الأمر المستهدف', type:'text', required:true, placeholder:'محمود العبسي', key:'payerName'},
            {id:'f_dl_amt', label:'المبلغ المستحق المطالب به (YER)', type:'text', placeholder:'150,000 YER', key:'amountDue'},
            {id:'f_dl_date', label:'تاريخ الاستحقاق الأخير', type:'date', key:'dueDate'},
            {id:'f_dl_st', label:'حالة إشعار المطالبة المالية', type:'select', options:['قيد المطالبة 🟡','مسددة 🟢','متعثرة 🔴'], key:'status'}
        ],
        'system_settings': [
            {id:'f_set_key', label:'كود الإعداد البرمجي (Setting Key ID)', type:'text', required:true, placeholder:'SYS_SESSION_TIMEOUT_MINS', key:'keyId'},
            {id:'f_set_name', label:'اسم الإعداد باللغة العربية والإنجليزي', type:'text', required:true, placeholder:'مدة انتهاء الجلسة التلقائي', key:'nameArEn'},
            {id:'f_set_scope', label:'تصنيف ونطاق الإعداد', type:'select', options:['أمني (Security)','عام (General)','إقليمي (Regional)'], key:'scope'},
            {id:'f_set_val', label:'القيمة الحالية المعتمدة للنظام', type:'text', required:true, placeholder:'15 دقيقة', key:'val'}
        ],
        'whatsapp_send': [
            {id:'f_wa_phone', label:'رقم المستهدف (WhatsApp) الدولي', type:'text', required:true, placeholder:'+967 771234567', key:'recipient'},
            {id:'f_wa_tmpl', label:'اسم ونوع القالب المعتمد', type:'text', placeholder:'إشعار_سند_قبض_مالي (Utility)', key:'template'},
            {id:'f_wa_media', label:'اسم المستند المرفق (PDF Document)', type:'text', placeholder:'سند_قبض_1020.pdf', key:'media'}
        ],
        'whatsapp_settings': [
            {id:'f_was_prov', label:'اسم ورقم مزود بوابة WhatsApp', type:'text', required:true, placeholder:'Meta Cloud API', key:'provider'},
            {id:'f_was_cred', label:'رصيد الرسائل والوحدات المتاحة', type:'text', placeholder:'4,850 رسالة متاحة', key:'credits'},
            {id:'f_was_hook', label:'رابط Webhook Endpoint المباشر', type:'text', placeholder:'https://api.school.edu.ye/v1/whatsapp/webhook', key:'webhook'}
        ],
        'alerts': [
            {id:'f_alt_name', label:'اسم التنبيه أو قاعدة التفعيل', type:'text', required:true, placeholder:'تنبيه الغياب الفوري', key:'name'},
            {id:'f_alt_trig', label:'حدث التفعيل البرمجي', type:'text', placeholder:'تسجيل غياب طالب', key:'trigger'},
            {id:'f_alt_aud', label:'الجمهور والمستهدفون', type:'select', options:['أولياء الأمور','المعلمين','الطلاب','الإدارة'], key:'audience'},
            {id:'f_alt_tmpl', label:'قالب الرسالة الصادرة', type:'textarea', placeholder:'نص التنبيه التلقائي...', key:'template'}
        ],
        'archive': [
            {id:'f_arc_title', label:'عنوان الوثيقة الأرشيفية', type:'text', required:true, placeholder:'القرار الوزاري للترخيص', key:'title'},
            {id:'f_arc_type', label:'تصنيف نوع الوثيقة', type:'select', options:['قرار إداري','تعميم','محضر اجتماع','عقد','مستند مالي'], key:'docType'},
            {id:'f_arc_file', label:'اسم الملف المرفق الرقمي', type:'text', placeholder:'قرار_ترخيص_2026.pdf', key:'fileName'},
            {id:'f_arc_date', label:'تاريخ التوثيق والأرشفة', type:'date', key:'date'}
        ],
        'homework': [
            {id:'f_hw_title', label:'عنوان الواجب المنزلي', type:'text', required:true, placeholder:'حل تمارين الدرس الثالث', key:'title'},
            {id:'f_hw_sub', label:'المادة الدراسية', type:'select', options:['الرياضيات المتقدمة','الفيزياء والتجارب','اللغة الإنجليزية'], key:'subject'},
            {id:'f_hw_grd', label:'الصف المخصص له', type:'select', options:['الثالث الثانوي','الثاني الثانوي','التاسع الأساسي'], key:'grade'},
            {id:'f_hw_due', label:'آخر موعد للتسليم', type:'date', key:'dueDate'}
        ],
        'enrollment': [
            {id:'f_enr_std', label:'اسم الطالب المسجل', type:'text', required:true, placeholder:'أحمد محمود العبسي', key:'studentName'},
            {id:'f_enr_grd', label:'الصف الدراسي', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي'], key:'grade'},
            {id:'f_enr_yr', label:'العام الدراسي المسجل به', type:'text', placeholder:'2025-2026', key:'year'},
            {id:'f_enr_fee', label:'إجمالي مبلغ العقد السنوي', type:'text', placeholder:'450,000 YER', key:'totalFee'}
        ],
        'contract': [
            {id:'f_cnt_emp', label:'اسم الموظف / المعلم', type:'text', required:true, placeholder:'خالد العنسي', key:'name'},
            {id:'f_cnt_type', label:'نوع العقد الوظيفي', type:'select', options:['عقد سنوي كامل','عقد بالحصص','عقد مؤقت'], key:'contractType'},
            {id:'f_cnt_sal', label:'الراتب الإجمالي المتفق عليه', type:'number', placeholder:'350000', key:'salary'},
            {id:'f_cnt_start', label:'تاريخ بداية العقد', type:'date', key:'startDate'}
        ],
        'advance': [
            {id:'f_adv_emp', label:'اسم الموظف الطالب للسلفة', type:'text', required:true, placeholder:'سارة أحمد', key:'name'},
            {id:'f_adv_amt', label:'المبلغ المطلوب كقرض/سلفة', type:'number', placeholder:'50000', key:'amount'},
            {id:'f_adv_inst', label:'عدد الأقساط الشهرية للسداد', type:'number', placeholder:'5', key:'installments'}
        ],
        'inventory': [
            {id:'f_inv_name', label:'اسم الصنف الأصول/المستلزمات', type:'text', required:true, placeholder:'أوراق طباعة A4', key:'name'},
            {id:'f_inv_code', label:'كود الصنف / الباركود', type:'text', placeholder:'PAPER-A4', key:'code'},
            {id:'f_inv_cat', label:'فئة الصنف المخزني', type:'select', options:['مستلزمات مكتبية','أجهزة إلكترونية','أثاث مدرسي'], key:'category'},
            {id:'f_inv_qty', label:'الكمية المتوفرة في المخزن', type:'number', placeholder:'100', key:'stockQty'},
            {id:'f_inv_price', label:'سعر التكلفة للوحدة', type:'text', placeholder:'4,500 YER', key:'unitPrice'}
        ],
        'inventory-items': [
            {id:'f_inv_name', label:'اسم الصنف المخزني', type:'text', required:true, placeholder:'أوراق طباعة A4', key:'name'},
            {id:'f_inv_code', label:'كود الصنف / الباركود', type:'text', placeholder:'PAPER-A4', key:'code'},
            {id:'f_inv_cat', label:'فئة الصنف المخزني', type:'select', options:['مستلزمات مكتبية','أجهزة إلكترونية','أثاث مدرسي'], key:'category'},
            {id:'f_inv_qty', label:'الكمية المتوفرة في المخزن', type:'number', placeholder:'100', key:'stockQty'},
            {id:'f_inv_price', label:'سعر التكلفة للوحدة', type:'text', placeholder:'4,500 YER', key:'unitPrice'}
        ],
        'activity': [
            {id:'f_act_name', label:'اسم النشاط اللاصفائي', type:'text', required:true, placeholder:'دوري كرة القدم المدرسي', key:'name'},
            {id:'f_act_cat', label:'تصنيف النشاط', type:'select', options:['رياضي','ثقافي وديني','علمي وفني'], key:'category'},
            {id:'f_act_sup', label:'المعلم/المشرف المسؤول', type:'text', placeholder:'أ. علي ناصر', key:'supervisor'},
            {id:'f_act_bud', label:'الميزانية المخصصة للنشاط', type:'text', placeholder:'150,000 YER', key:'budget'}
        ],
        'activities': [
            {id:'f_act_name', label:'اسم النشاط اللاصفائي', type:'text', required:true, placeholder:'دوري كرة القدم المدرسي', key:'name'},
            {id:'f_act_cat', label:'تصنيف النشاط', type:'select', options:['رياضي','ثقافي وديني','علمي وفني'], key:'category'},
            {id:'f_act_sup', label:'المعلم/المشرف المسؤول', type:'text', placeholder:'أ. علي ناصر', key:'supervisor'},
            {id:'f_act_bud', label:'الميزانية المخصصة للنشاط', type:'text', placeholder:'150,000 YER', key:'budget'}
        ],
        'transport': [
            {id:'f_tr_name', label:'اسم خط النقل / المسار', type:'text', required:true, placeholder:'خط السبعين - حداء', key:'routeName'},
            {id:'f_tr_driver', label:'اسم السائق المسؤول', type:'text', placeholder:'أحمد سالم', key:'driver'},
            {id:'f_tr_phone', label:'هاتف السائق', type:'text', placeholder:'+967 775556667', key:'phone'},
            {id:'f_tr_bus', label:'رقم وتفاصيل الحافلة', type:'text', placeholder:'حافلة 01 (30 راكب)', key:'busNo'},
            {id:'f_tr_fee', label:'الاشتراك الشهري للطالب', type:'text', placeholder:'15,000 YER', key:'fee'}
        ],
        'transport-routes': [
            {id:'f_tr_name', label:'اسم خط النقل / المسار', type:'text', required:true, placeholder:'خط السبعين - حداء', key:'routeName'},
            {id:'f_tr_driver', label:'اسم السائق المسؤول', type:'text', placeholder:'أحمد سالم', key:'driver'},
            {id:'f_tr_phone', label:'هاتف السائق', type:'text', placeholder:'+967 775556667', key:'phone'},
            {id:'f_tr_bus', label:'رقم وتفاصيل الحافلة', type:'text', placeholder:'حافلة 01 (30 راكب)', key:'busNo'},
            {id:'f_tr_fee', label:'الاشتراك الشهري للطالب', type:'text', placeholder:'15,000 YER', key:'fee'}
        ],
        'academic-calendar': [
            {id:'f_cal_title', label:'عنوان الفعالية / الحدث الأكاديمي', type:'text', required:true, placeholder:'امتحانات نصف العام', key:'title'},
            {id:'f_cal_start', label:'تاريخ بداية الفعالية', type:'date', key:'startDate'},
            {id:'f_cal_end', label:'تاريخ نهاية الفعالية', type:'date', key:'endDate'},
            {id:'f_cal_target', label:'الجمهور المستهدف', type:'select', options:['الجميع','الطلاب','المعلمين','أولياء الأمور'], key:'target'}
        ],
        'academic-years': [
            {id:'f_ay_name', label:'السنة الدراسية (العام الأكاديمي)', type:'text', required:true, placeholder:'2025-2026', key:'yearName'},
            {id:'f_ay_start', label:'تاريخ بدء الدراسة', type:'date', key:'startDate'},
            {id:'f_ay_end', label:'تاريخ نهاية العام', type:'date', key:'endDate'},
            {id:'f_ay_status', label:'حالة السنة الدراسية', type:'select', options:['نشطة 🟢','مغلقة 🔴','قادمة 🟡'], key:'status'}
        ],
        'account-ceiling': [
            {id:'f_ac_name', label:'اسم الحساب المستهدف', type:'text', required:true, placeholder:'حساب رسوم الطلاب', key:'accountName'},
            {id:'f_ac_limit', label:'الحد الأعلى للسحب/الائتمان (YER)', type:'number', placeholder:'1000000', key:'creditLimit'},
            {id:'f_ac_type', label:'نوع السقف الائتماني', type:'select', options:['سقف مدين','سقف دائن','سقف سحب مكشوف'], key:'ceilingType'}
        ],
        'activity-enrollment': [
            {id:'f_ae_student', label:'اسم الطالب المشترك', type:'text', required:true, placeholder:'علي محمود العبسي', key:'studentName'},
            {id:'f_ae_activity', label:'النشاط المدرسي', type:'select', options:['دوري كرة القدم','جماعة الكشافة','نادي العلوم والتكنولوجيا'], key:'activityName'},
            {id:'f_ae_fee', label:'رسوم الاشتراك بالنشاط (YER)', type:'text', placeholder:'5,000 YER', key:'fee'}
        ],
        'activity-reports': [
            {id:'f_ar_title', label:'عنوان تقرير النشاط', type:'text', required:true, placeholder:'تقرير الدوري الرياضي للربع الأول', key:'title'},
            {id:'f_ar_act', label:'النشاط المرتبط', type:'text', placeholder:'دوري كرة القدم', key:'activity'},
            {id:'f_ar_summary', label:'ملخص الأنشطة والنتائج', type:'textarea', placeholder:'تفاصيل الإنجازات والطلاب المكرمين...', key:'summary'}
        ],
        'activity-supervisors': [
            {id:'f_as_name', label:'اسم مشرف النشاط', type:'text', required:true, placeholder:'أ. محمد عبد الله', key:'name'},
            {id:'f_as_act', label:'النشاط المسؤول عنه', type:'text', placeholder:'جماعة الكشافة', key:'activity'},
            {id:'f_as_phone', label:'رقم هاتف المشرف', type:'text', placeholder:'+967 771122334', key:'phone'}
        ],
        'activity-types': [
            {id:'f_at_name', label:'اسم نوع/تصنيف النشاط', type:'text', required:true, placeholder:'نشاط رياضي بدني', key:'name'},
            {id:'f_at_code', label:'رمز التصنيف البرمجي', type:'text', placeholder:'ACT-SPORTS', key:'code'},
            {id:'f_at_desc', label:'وصف ونطاق الأنشطة', type:'textarea', placeholder:'يشمل كرة القدم، السباحة، والجري...', key:'desc'}
        ],
        'admin-messages': [
            {id:'f_am_title', label:'عنوان الإعلان / الرسالة الإدارية', type:'text', required:true, placeholder:'تنبيه بشأن إجازة نهاية الفصل', key:'title'},
            {id:'f_am_aud', label:'الجمهور والموجه لهم', type:'select', options:['الجميع','كادر المعلمين','أولياء الأمور','الطلاب'], key:'audience'},
            {id:'f_am_msg', label:'نص الإعلان الإداري', type:'textarea', placeholder:'أدخل نص الإعلان الصادر من إدارة المدرسة...', key:'message'}
        ],
        'buses': [
            {id:'f_bus_no', label:'رقم الحافلة / المركبة', type:'text', required:true, placeholder:'حافلة 05 (تويوتا)', key:'busNo'},
            {id:'f_bus_cap', label:'سعة الركاب (مقعد)', type:'number', placeholder:'30', key:'capacity'},
            {id:'f_bus_driver', label:'اسم السائق المعتمد', type:'text', placeholder:'أحمد ناصر', key:'driver'},
            {id:'f_bus_phone', label:'رقم هاتف السائق', type:'text', placeholder:'+967 773344556', key:'phone'}
        ],
        'cashbox': [
            {id:'f_cb_name', label:'اسم الصندوق / الخزنة', type:'text', required:true, placeholder:'الصندوق الفرعي 01', key:'name'},
            {id:'f_cb_mgr', label:'اسم أمين الصندوق / المسؤول', type:'text', placeholder:'سارة المحاسبة', key:'manager'},
            {id:'f_cb_bal', label:'الرصيد الافتتاحي (YER)', type:'text', placeholder:'1,000,000 YER', key:'openingBalance'}
        ],
        'change-password': [
            {id:'f_cp_old', label:'كلمة المرور الحالية', type:'password', required:true, key:'oldPassword'},
            {id:'f_cp_new', label:'كلمة المرور الجديدة', type:'password', required:true, key:'newPassword'},
            {id:'f_cp_confirm', label:'تأكيد كلمة المرور الجديدة', type:'password', required:true, key:'confirmPassword'}
        ],
        'chart-accounts': [
            {id:'f_ca_code', label:'كود الحساب المحاسبي', type:'text', required:true, placeholder:'110101', key:'code'},
            {id:'f_ca_name', label:'اسم الحساب المالي', type:'text', required:true, placeholder:'حساب الصندوق الرئيسي', key:'name'},
            {id:'f_ca_type', label:'نوع الحساب الرئيسي', type:'select', options:['أصول','خصوم','إيرادات','مصروفات','حقوق ملكية'], key:'type'},
            {id:'f_ca_parent', label:'الحساب الأب / الرئيسي', type:'text', placeholder:'1101 - الأصول المتداولة', key:'parent'}
        ],
        'class-notes': [
            {id:'f_cn_student', label:'اسم الطالب المستهدف', type:'text', required:true, placeholder:'خالد محمود', key:'studentName'},
            {id:'f_cn_note', label:'ملاحظة وتوجيه رائد الفصل', type:'textarea', required:true, placeholder:'ملاحظة انضباطية وسلوكية...', key:'note'},
            {id:'f_cn_status', label:'طبيعة الملاحظة', type:'select', options:['توجيه سلوكي 🟡','إشادة وتكريم 🟢','تنبيه أكاديمي 🔴'], key:'type'}
        ],
        'classrooms': [
            {id:'f_cr_name', label:'اسم القاعة / المعمل الدراسي', type:'text', required:true, placeholder:'قاعة الحاسوب والذكاء الاصطناعي', key:'name'},
            {id:'f_cr_bld', label:'المبنى والطابق', type:'text', placeholder:'المبنى الرئيسي - الطابق الثاني', key:'location'},
            {id:'f_cr_cap', label:'سعة القاعة (مقعد)', type:'number', placeholder:'40', key:'capacity'}
        ],
        'class-times': [
            {id:'f_ct_period', label:'اسم/رقم الحصة الدراسية', type:'text', required:true, placeholder:'الحصة الأولى', key:'periodName'},
            {id:'f_ct_start', label:'وقت بداية الحصة', type:'text', placeholder:'07:45 ص', key:'startTime'},
            {id:'f_ct_end', label:'وقت نهاية الحصة', type:'text', placeholder:'08:30 ص', key:'endTime'}
        ],
        'cost-centers': [
            {id:'f_cc_code', label:'كود مركز التكلفة', type:'text', required:true, placeholder:'CC-101', key:'code'},
            {id:'f_cc_name', label:'اسم مركز التكلفة والموازنة', type:'text', required:true, placeholder:'قسم الأنشطة والرحلات', key:'name'},
            {id:'f_cc_budget', label:'الموازنة التقديرية المخصصة (YER)', type:'text', placeholder:'5,000,000 YER', key:'budget'}
        ],
        'custom-report': [
            {id:'f_crp_title', label:'اسم/عنوان التقرير المخصص', type:'text', required:true, placeholder:'تقرير التحصيل المالي السنوي', key:'title'},
            {id:'f_crp_type', label:'صيغة وتنسيق التقرير', type:'select', options:['PDF Document','Excel Sheet','جدول إحصائي interactive'], key:'format'},
            {id:'f_crp_scope', label:'نطاق ووحدة البيانات', type:'select', options:['الشؤون المالية','شؤون الطلاب','الكنترول','الموارد البشرية'], key:'scope'}
        ],
        'dictionary': [
            {id:'f_dic_ar', label:'المصطلح باللغة العربية', type:'text', required:true, placeholder:'لوحة التحكم الرئيسية', key:'termAr'},
            {id:'f_dic_en', label:'المقابل باللغة الإنجليزية', type:'text', required:true, placeholder:'Main Dashboard', key:'termEn'},
            {id:'f_dic_cat', label:'تصنيف المصطلح بالنظام', type:'select', options:['عام','محاسبة','كنترول','موارد بشرية'], key:'category'}
        ],
        'discontinued': [
            {id:'f_disc_student', label:'اسم الطالب غير المستمر', type:'text', required:true, placeholder:'يحيى صالح', key:'studentName'},
            {id:'f_disc_reason', label:'سبب عدم الاستمرار / الانقطاع', type:'select', options:['انتقال إلى مدرسة أخرى','ظروف عائلية','توقف دائم','استبعاد إداري'], key:'reason'},
            {id:'f_disc_notes', label:'تفاصيل وملاحظات الإدارة', type:'textarea', placeholder:'تفاصيل القرار الإداري...', key:'notes'}
        ],
        'discount-categories': [
            {id:'f_dc_name', label:'اسم فئة الخصم / المنحة', type:'text', required:true, placeholder:'خصم الأخوة 15%', key:'name'},
            {id:'f_dc_pct', label:'نسبة الخصم المئوية (%)', type:'number', placeholder:'15', key:'percentage'},
            {id:'f_dc_desc', label:'شروط وأحكام الاستحقاق', type:'textarea', placeholder:'ينطبق على الأخ الثاني فما فوق...', key:'description'}
        ],
        'emp-notices': [
            {id:'f_en_emp', label:'اسم الموظف المستهدف', type:'text', required:true, placeholder:'أ. محمد العنسي', key:'employeeName'},
            {id:'f_en_title', label:'عنوان الإشعار/التنبيه', type:'text', required:true, placeholder:'تنبيه تأخير صباحي', key:'title'},
            {id:'f_en_body', label:'نص الإشعار التوجيهي', type:'textarea', placeholder:'يرجى الالتزام بمواعيد البصمة الصباحية...', key:'message'}
        ],
        'exam_halls': [
            {id:'f_eh_name', label:'اسم قاعة/لجنة الامتحانات', type:'text', required:true, placeholder:'لجنة رقم 01 - القاعة الكبرى', key:'hallName'},
            {id:'f_eh_cap', label:'عدد المقاعد المتاحة', type:'number', placeholder:'50', key:'capacity'},
            {id:'f_eh_sup', label:'المراقب الرئيسي للجنة', type:'text', placeholder:'أ. عبد الرحمن سالم', key:'supervisor'}
        ],
        'faq-article': [
            {id:'f_faq_q', label:'السؤال المتكرر (Question)', type:'text', required:true, placeholder:'كيف يمكنني سداد الرسوم عبر البنك؟', key:'question'},
            {id:'f_faq_a', label:'الإجابة التفصيلية (Answer)', type:'textarea', required:true, placeholder:'يمكنك استخدام حساب البنك رقم...', key:'answer'},
            {id:'f_faq_cat', label:'تصنيف السؤال', type:'select', options:['المالية والرسوم','القبول والتسجيل','استخدام البوابة'], key:'category'}
        ],
        'fee-categories': [
            {id:'f_fc_name', label:'اسم فئة الرسوم الدراسية', type:'text', required:true, placeholder:'رسوم الكتب والمستلزمات', key:'name'},
            {id:'f_fc_amt', label:'المبلغ الافتراضي للفئة (YER)', type:'text', placeholder:'50,000 YER', key:'amount'},
            {id:'f_fc_opt', label:'الإلزامية', type:'select', options:['إجباري لجميع الطلاب','اختياري حسب الرغبة'], key:'mandatory'}
        ],
        'grade-fees': [
            {id:'f_gf_grade', label:'الصف الدراسي المستهدف', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي','التاسع الأساسي'], key:'grade'},
            {id:'f_gf_fee', label:'إجمالي رسوم الصف السنوية (YER)', type:'text', required:true, placeholder:'450,000 YER', key:'totalFee'},
            {id:'f_gf_inst', label:'عدد الأقساط المتاحة', type:'number', placeholder:'4', key:'installments'}
        ],
        'grade-progression': [
            {id:'f_gp_from', label:'الصف الحالي (المُرفّع منه)', type:'select', options:['الثاني الثانوي','الأول الثانوي','التاسع الأساسي','الثامن الأساسي'], key:'fromGrade'},
            {id:'f_gp_to', label:'الصف المستهدف (المُرفّع إليه)', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي','التاسع الأساسي'], key:'toGrade'},
            {id:'f_gp_min', label:'الحد الأدنى للمعدل الترفيعي (%)', type:'number', placeholder:'50', key:'minGPA'}
        ],
        'grade-ratings': [
            {id:'f_gr_symbol', label:'رمز/تقدير النتيجة', type:'text', required:true, placeholder:'ممتاز مرتفع (A+)', key:'rating'},
            {id:'f_gr_min', label:'الحد الأدنى للنسبة المئوية (%)', type:'number', placeholder:'95', key:'minScore'},
            {id:'f_gr_max', label:'الحد الأعلى للنسبة المئوية (%)', type:'number', placeholder:'100', key:'maxScore'}
        ],
        'grade-types': [
            {id:'f_gt_name', label:'اسم نوع التقييم / الاختبار', type:'text', required:true, placeholder:'اختبار منتصف الفصل الدراسي', key:'typeName'},
            {id:'f_gt_weight', label:'الوزن من النتيجة النهائية (%)', type:'number', placeholder:'20', key:'weight'},
            {id:'f_gt_max', label:'الدرجة العظمى المعتمدة', type:'number', placeholder:'20', key:'maxGrade'}
        ],
        'guarantors': [
            {id:'f_grt_name', label:'اسم الضامن / الكفيل الرباعي', type:'text', required:true, placeholder:'عبد الله سالم العبسي', key:'guarantorName'},
            {id:'f_grt_emp', label:'اسم الموظف المكفول', type:'text', required:true, placeholder:'أ. أحمد علي', key:'employeeName'},
            {id:'f_grt_phone', label:'رقم هاتف الكفيل (واتساب)', type:'text', placeholder:'+967 772233445', key:'phone'},
            {id:'f_grt_job', label:'جهة عمل ومسمى الكفيل', type:'text', placeholder:'مدير شركة تجارية', key:'jobTitle'}
        ],
        'hall-distribution': [
            {id:'f_hd_hall', label:'اسم لجنة/قاعة الامتحانات', type:'select', options:['لجنة رقم 01 - القاعة الكبرى','لجنة رقم 02 - القاعة 101'], key:'hallName'},
            {id:'f_hd_teacher', label:'المراقب المكلف باللجنة', type:'text', required:true, placeholder:'أ. محمد العنسي', key:'teacherName'},
            {id:'f_hd_shift', label:'الفترة الامتحانية', type:'select', options:['الفترة الأولى (8:00 - 10:00 ص)','الفترة الثانية (10:30 - 12:30 م)'], key:'shift'}
        ],
        'installment-plans': [
            {id:'f_ip_name', label:'اسم خطة الأقساط المعتمدة', type:'text', required:true, placeholder:'خطة الأقساط الأربعة الأرباع', key:'planName'},
            {id:'f_ip_count', label:'عدد الأقساط الدورية', type:'number', placeholder:'4', key:'installmentCount'},
            {id:'f_ip_pct', label:'الدفعة الأولى المقدمة (%)', type:'number', placeholder:'25', key:'downPaymentPct'}
        ],
        'issue-orders': [
            {id:'f_io_num', label:'رقم إذن الصرف المخزني', type:'text', required:true, placeholder:'ISS-2026-045', key:'orderNo'},
            {id:'f_io_target', label:'الجهة/القسم المستلم للمواد', type:'text', placeholder:'معامل الفيزياء والعلوم', key:'recipientDept'},
            {id:'f_io_items', label:'الأصناف والكميات المصروفة', type:'textarea', placeholder:'أوراق طباعة (10 رزم)، أقلام سبورة (5 كرائت)...', key:'itemsList'}
        ],
        'item-categories': [
            {id:'f_ic_name', label:'اسم فئة الأصناف المخزنية', type:'text', required:true, placeholder:'مستلزمات طباعة ومكتبة', key:'categoryName'},
            {id:'f_ic_code', label:'رمز الفئة البرمجي', type:'text', placeholder:'CAT-OFFICE', key:'code'},
            {id:'f_ic_desc', label:'وصف وتصنيف الأصناف', type:'textarea', placeholder:'تضم كافة الأدوات والأوراق والقرطاسية...', key:'description'}
        ],
        'leave-request': [
            {id:'f_lr_emp', label:'اسم الموظف طالب الإجازة', type:'text', required:true, placeholder:'أ. سارة أحمد', key:'employeeName'},
            {id:'f_lr_type', label:'نوع الإجازة المطلوبة', type:'select', options:['إجازة اعتيادية سنوية','إجازة مرضية','إجازة اضطرارية','مغادرة ساعتين'], key:'leaveType'},
            {id:'f_lr_start', label:'تاريخ بداية الإجازة', type:'date', key:'startDate'},
            {id:'f_lr_days', label:'عدد الأيام / الساعات', type:'number', placeholder:'3', key:'daysCount'}
        ],
        'parents': [
            {id:'f_prnt_name', label:'اسم ولي الأمر الكامل', type:'text', required:true, placeholder:'محمود عبد الله العبسي', key:'parentName'},
            {id:'f_prnt_id', label:'الرقم الوطني / الهوية الشخصية', type:'text', placeholder:'1019283746', key:'nationalId'},
            {id:'f_prnt_phone', label:'رقم الهاتف الجوال الرئيسي (واتساب)', type:'text', required:true, placeholder:'+967 770000000', key:'phone'},
            {id:'f_prnt_job', label:'المهنة وجهة العمل', type:'text', placeholder:'مهندس استشاري', key:'occupation'}
        ],
        'performance-eval': [
            {id:'f_pe_emp', label:'اسم الموظف التقييم', type:'text', required:true, placeholder:'أ. خالد العنسي', key:'employeeName'},
            {id:'f_pe_score', label:'النتيجة الكلية للتقييم (%)', type:'number', placeholder:'92', key:'totalScore'},
            {id:'f_pe_rating', label:'التقدير العام للأداء', type:'select', options:['ممتاز مرتفع 🟢','جيد جداً 🟡','مرضي 🟠','يحتاج تحسين 🔴'], key:'rating'},
            {id:'f_pe_notes', label:'ملاحظات وتوصيات الإدارة', type:'textarea', placeholder:'أداء متميز في التغطية الأكاديمية والالتزام...', key:'notes'}
        ],
        'personal-info': [
            {id:'f_pi_name', label:'الاسم الكامل للشخص', type:'text', required:true, key:'fullName'},
            {id:'f_pi_email', label:'البريد الإلكتروني المعتمد', type:'email', key:'email'},
            {id:'f_pi_phone', label:'رقم هاتف التواصل', type:'text', key:'phone'},
            {id:'f_pi_address', label:'العنوان ومحل الإقامة', type:'text', key:'address'}
        ],
        'required-docs': [
            {id:'f_rd_title', label:'اسم الوثيقة الرسمية المطلوبة', type:'text', required:true, placeholder:'شهادة الميلاد الأصلية معمدة', key:'docTitle'},
            {id:'f_rd_target', label:'الفئة الموجهة لها الوثيقة', type:'select', options:['الطلاب الجدد','الموظفين والتوظيف','الجميع'], key:'target'},
            {id:'f_rd_mandatory', label:'درجة الإلزامية', type:'select', options:['إجباري للتسجيل 🔴','اختياري تكملي 🟡'], key:'isMandatory'}
        ],
        'shortcuts': [
            {id:'f_sc_name', label:'اسم الاختصار السريع', type:'text', required:true, placeholder:'فتح نافذة تسجيل طالب جديد', key:'shortcutName'},
            {id:'f_sc_key', label:'زر اختصار الكيبورد', type:'text', placeholder:'Ctrl + Shift + S', key:'hotkey'},
            {id:'f_sc_action', label:'العملية المربوطة', type:'text', placeholder:'openForm("student")', key:'actionTarget'}
        ],
        'sms-settings': [
            {id:'f_smss_prov', label:'اسم بوابة إرسال SMS', type:'text', required:true, placeholder:'Yemen SMS Gateway', key:'provider'},
            {id:'f_smss_sender', label:'اسم المرسل المعالج (Sender ID)', type:'text', placeholder:'SMART-SCH', key:'senderId'},
            {id:'f_smss_bal', label:'رصيد الرسائل المتبقي', type:'number', placeholder:'10000', key:'balance'}
        ],
        'sms-templates': [
            {id:'f_smst_name', label:'اسم قالب الرسالة SMS', type:'text', required:true, placeholder:'قالب إشعار الغياب الفوري', key:'templateName'},
            {id:'f_smst_body', label:'نص الرسالة القصيرة', type:'textarea', required:true, placeholder:'عزيزي ولي الأمر، ننوه بغياب ابنكم {student_name} بتاريخ {date}...', key:'body'}
        ],
        'stocktake': [
            {id:'f_stk_title', label:'عنوان عملية الجرد المخزني', type:'text', required:true, placeholder:'الجرد السنوي الشامل لمخزن الأثاث 2026', key:'title'},
            {id:'f_stk_date', label:'تاريخ الجرد', type:'date', key:'date'},
            {id:'f_stk_auditor', label:'اسم رئيس لجنة الجرد', type:'text', placeholder:'أ. محمد المحاسب', key:'auditor'}
        ],
        'subject-distribution': [
            {id:'f_sdist_sub', label:'المادة الدراسية', type:'select', options:['الرياضيات المتقدمة','الفيزياء والتجارب','اللغة الإنجليزية'], key:'subjectName'},
            {id:'f_sdist_grade', label:'الصف الدراسي', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي'], key:'grade'},
            {id:'f_sdist_teacher', label:'المعلم المسند له التدريس', type:'text', placeholder:'أ. خالد العنسي', key:'teacherName'},
            {id:'f_sdist_periods', label:'عدد الحصص الأسبوعية', type:'number', placeholder:'5', key:'weeklyPeriods'}
        ],
        'substitute': [
            {id:'f_subst_absent', label:'المعلم الغائب الاصلي', type:'text', required:true, placeholder:'أ. علي سالم', key:'absentTeacher'},
            {id:'f_subst_sub', label:'المعلم البديل المكلف', type:'text', required:true, placeholder:'أ. محمد العنسي', key:'substituteTeacher'},
            {id:'f_subst_period', label:'الحصة والفصل المكلف به', type:'text', placeholder:'الحصة 3 (الثالث الثانوي أ)', key:'periodDetails'}
        ],
        'success-rate-section': [
            {id:'f_srs_sec', label:'اسم الشعبة الدراسية', type:'select', options:['الثالث الثانوي (أ)','الثاني الثانوي (ب)','التاسع (ج)'], key:'sectionName'},
            {id:'f_srs_target', label:'مستهدف نسبة النجاح المطلوب (%)', type:'number', placeholder:'95', key:'targetRate'},
            {id:'f_srs_current', label:'نسبة النجاح المحققة حالياً (%)', type:'number', placeholder:'91.5', key:'currentRate'}
        ],
        'suppliers': [
            {id:'f_supp_name', label:'اسم المورد / الشركة التوريدية', type:'text', required:true, placeholder:'شركة الأمل للمستلزمات المدرسية', key:'supplierName'},
            {id:'f_supp_phone', label:'رقم هاتف المورد', type:'text', placeholder:'+967 771112223', key:'phone'},
            {id:'f_supp_cat', label:'تخصص ونوع التوريدات', type:'text', placeholder:'أجهزة حاسوب ومستلزمات مكتبية', key:'category'}
        ],
        'supply-orders': [
            {id:'f_so_num', label:'رقم إذن/أمر التوريد', type:'text', required:true, placeholder:'SUP-2026-012', key:'orderNo'},
            {id:'f_so_supp', label:'المورد المعتمد', type:'text', placeholder:'شركة الأمل للمستلزمات', key:'supplier'},
            {id:'f_so_items', label:'تفاصيل الأصناف الموردة', type:'textarea', placeholder:'أجهزة حاسوب (50 جهاز)، طابعات (5 طابعات)...', key:'itemsList'}
        ],
        'support-ticket': [
            {id:'f_st_title', label:'موضوع التذكرة / المشكلة', type:'text', required:true, placeholder:'مشكلة في إصدار سند القبض', key:'title'},
            {id:'f_st_priority', label:'درجة الأهمية والاحتياج', type:'select', options:['عادية 🟢','متوسطة 🟡','عاجلة جداً 🔴'], key:'priority'},
            {id:'f_st_desc', label:'وصف التفاصيل الفنية للمشكلة', type:'textarea', placeholder:'يرجى توضيح الخطوات الظاهرة...', key:'description'}
        ],
        'teacher-subjects': [
            {id:'f_ts_teacher', label:'اسم المعلم', type:'text', required:true, placeholder:'أ. خالد العنسي', key:'teacherName'},
            {id:'f_ts_sub', label:'المادة المسندة', type:'text', placeholder:'الرياضيات المتقدمة', key:'subjectName'},
            {id:'f_ts_grade', label:'الصف الدراسي', type:'text', placeholder:'الثالث الثانوي', key:'grade'}
        ],
        'transport-enrollment': [
            {id:'f_te_std', label:'اسم الطالب المشترك بالمواصلات', type:'text', required:true, placeholder:'محمد أحمد العبسي', key:'studentName'},
            {id:'f_te_route', label:'خط السير المعتمد', type:'select', options:['خط السبعين - حداء','خط حدة - الستين','خط الدائري - أصحابه'], key:'routeName'},
            {id:'f_te_fee', label:'مبلغ الاشتراك الشهري (YER)', type:'text', placeholder:'15,000 YER', key:'fee'}
        ],
        'violations-catalog': [
            {id:'f_vc_title', label:'عنوان المخالفة السلوكية', type:'text', required:true, placeholder:'التأخر عن الحضور الصباحي بغير عذر', key:'title'},
            {id:'f_vc_degree', label:'درجة المخالفة السلوكية', type:'select', options:['درجة أولى (بسيطة) 🟡','درجة ثانية (متوسطة) 🟠','درجة ثالثة (جسيمة) 🔴'], key:'degree'},
            {id:'f_vc_penalty', label:'الإجراء/الجزاء المترتب المعتمد', type:'textarea', placeholder:'تنبيه أول، التزام خطي، إبلاغ ولي الأمر...', key:'penalty'}
        ]
    };

    const defaultFields = [
        {id:'f_gen_name', label:'الاسم / المعرف الرئيسي', type:'text', required:true, placeholder:'أدخل الاسم أو البيان...', key:'name'},
        {id:'f_gen_cat', label:'التصنيف / الفئة المخصصة', type:'text', placeholder:'عام', key:'category'},
        {id:'f_gen_val', label:'القيمة / الحالة المعتمدة', type:'text', placeholder:'نشط 🟢', key:'status'}
    ];

    return fieldDefs[type] || defaultFields;
}
window.getFormFields = getFormFields;

function getCollectionKey(type) {
    const m = {
        'student':'students','students':'students','stage':'stages','stages':'stages',
        'section':'sections','sections':'sections','subject':'subjects','subjects':'subjects',
        'employee':'employees','employees':'employees','contract':'empContractsData',
        'advance':'empAdvancesData','user':'usersData','users':'usersData',
        'voucher':'vouchers','voucher_receipt':'vouchers','voucher_payment':'vouchers',
        'journal':'vouchers','journal_entry':'vouchers',
        'enrollment':'vouchers','homework':'homework',
        'currencies':'currenciesData','cashbox_inventory':'cashboxInventoryData',
        'closings':'closingsData','banks':'banksData','demand_letters':'demandLettersData',
        'system_settings':'systemSettingsData',
        'whatsapp_send':'whatsappSendData','whatsapp_settings':'whatsappSettingsData',
        'alerts':'alertsData','archive':'archiveData','posting':'postingData',
        'inventory':'inventory_items','inventory-items':'inventory_items',
        'activity':'activitiesGridData','activities':'activitiesGridData',
        'transport':'transportRoutesGridData','transport-routes':'transportRoutesGridData',
        'academic-calendar':'academicCalendarData','academic-years':'academicYearsData',
        'account-ceiling':'accountCeilingData','activity-enrollment':'activityEnrollmentData',
        'activity-reports':'activityReportsData','activity-supervisors':'activitySupervisorsData',
        'activity-types':'activityTypesData','admin-messages':'adminMessagesData',
        'buses':'busesData','cashbox':'cashboxesData','chart-accounts':'chartAccountsData',
        'class-notes':'classNotesData','classrooms':'classroomsData','class-times':'classTimesData',
        'cost-centers':'costCentersData','custom-report':'customReportsData',
        'dictionary':'dictionaryData','discontinued':'discontinuedData',
        'discount-categories':'discountCategoriesData','emp-notices':'empNoticesData',
        'exam_halls':'examHallsData','faq-article':'faqData','fee-categories':'feeCategoriesData',
        'grade-fees':'gradeFeesData','grade-progression':'gradeProgressionData',
        'grade-ratings':'gradeRatingsData','grade-types':'gradeTypesData',
        'guarantors':'guarantorsData','hall-distribution':'hallDistributionData',
        'installment-plans':'installmentPlansData','issue-orders':'issueOrdersData',
        'item-categories':'itemCategoriesData','leave-request':'leaveRequestsData',
        'parents':'parentsData','performance-eval':'performanceEvalData',
        'personal-info':'personalInfoData','required-docs':'requiredDocsData',
        'shortcuts':'shortcutsData','sms-settings':'smsSettingsData','sms-templates':'smsTemplatesData',
        'stocktake':'stocktakeData','subject-distribution':'subjectDistributionData',
        'substitute':'substituteData','success-rate-section':'successRateSectionData',
        'suppliers':'suppliersData','supply-orders':'supplyOrdersData',
        'support-ticket':'supportTicketsData','teacher-subjects':'teacherSubjectsData',
        'transport-enrollment':'transportEnrollmentData','violations-catalog':'violationsCatalogData'
    };
    return m[type] || (type.replace(/-/g, '_') + 'Data');
}
window.getCollectionKey = getCollectionKey;

function openForm(type, editData) {
    type = type || 'student';
    window.currentEditingType = type;

    let editId = null;
    let rec = null;

    if (editData && typeof editData === 'object' && !Array.isArray(editData)) {
        rec = editData;
        editId = rec.id || rec.keyId || rec.isoCode || rec.code || null;
    } else if (editData !== undefined && editData !== null) {
        editId = editData;
    }

    window.currentEditingId = editId;

    if (editId && !rec) {
        const collKey = getCollectionKey(type);
        const collection = DB[collKey] || [];
        rec = collection.find(x =>
            x.id == editId || x.keyId == editId || x.isoCode == editId ||
            x.provider == editId || x.name == editId || x.code == editId
        );
    }

    const modal = document.getElementById('formModal');
    const titleEl = document.getElementById('formTitle');
    const formEl = document.getElementById('dynamicForm') || document.getElementById('form-fields');

    if (!modal) {
        console.error('formModal not found!');
        toast('خطأ: نموذج الإدخال غير موجود في الصفحة', 1);
        return;
    }

    const typeLabels = {
        'student':'طالب','employee':'موظف','users':'مستخدم','stage':'مرحلة دراسية',
        'section':'شعبة','subject':'مادة','voucher_receipt':'سند قبض','voucher_payment':'سند صرف',
        'journal_entry':'قيد يومية','currencies':'عملة','cashbox_inventory':'جرد خزنة',
        'banks':'حساب بنكي','demand_letters':'مطالبة مالية','system_settings':'إعداد نظام',
        'whatsapp_send':'رسالة واتساب','whatsapp_settings':'إعدادات واتساب',
        'alerts':'تنبيه','archive':'مستند أرشيف','homework':'واجب مدرسي',
        'enrollment':'تسجيل طالب','change-password':'تغيير كلمة المرور',
        'contract':'عقد موظف','advance':'سلفة / قرض','inventory':'صنف مخزني',
        'inventory-items':'صنف مخزني','activity':'نشاط مدرسي','activities':'نشاط مدرسي',
        'transport':'خط نقل ومواصلات','transport-routes':'خط نقل ومواصلات',
        'academic-calendar':'فعالية تقويم','academic-years':'سنة دراسية',
        'account-ceiling':'سقف ائتماني','activity-enrollment':'اشتراك نشاط',
        'activity-reports':'تقرير نشاط','activity-supervisors':'مشرف نشاط',
        'activity-types':'تصنيف نشاط','admin-messages':'إعلان إداري',
        'buses':'حافلة نقل','cashbox':'صندوق مالي','chart-accounts':'حساب محاسبي',
        'class-notes':'ملاحظة رائد الفصل','classrooms':'قاعة دراسية','class-times':'توقيت حصة',
        'cost-centers':'مركز تكلفة','custom-report':'تقرير مخصص','dictionary':'مصطلح قاموس',
        'discontinued':'طالب غير مستمر','discount-categories':'فئة خصم','emp-notices':'إشعار موظف',
        'exam_halls':'قاعة امتحانات','faq-article':'سؤال شائع','fee-categories':'فئة رسوم',
        'grade-fees':'رسوم صف','grade-progression':'تدرج صفوف','grade-ratings':'تقدير درجات',
        'grade-types':'نوع تقييم','guarantors':'كفيل موظف','hall-distribution':'توزيع مراقبين',
        'installment-plans':'خطة أقساط','issue-orders':'إذن صرف مخزني','item-categories':'فئة أصناف',
        'leave-request':'طلب إجازة','parents':'ولي أمر','performance-eval':'تقييم أداء',
        'personal-info':'ملف شخصي','required-docs':'وثيقة مطلوبة','shortcuts':'اختصار نظام',
        'sms-settings':'إعدادات SMS','sms-templates':'قالب SMS','stocktake':'جرد مخزون',
        'subject-distribution':'توزيع مواد','substitute':'معلم بديل','success-rate-section':'نسبة نجاح',
        'suppliers':'مورد معتمد','supply-orders':'إذن توريد','support-ticket':'تذكرة دعم',
        'teacher-subjects':'إسناد مادة','transport-enrollment':'اشتراك مواصلات','violations-catalog':'مخالفة سلوكية'
    };
    const label = typeLabels[type] || type;

    if (titleEl) {
        titleEl.innerHTML = editId ?
            `<i class="fa-solid fa-pen-to-square"></i> تعديل بيانات ${label} (${editId})` :
            `<i class="fa-solid fa-plus-circle"></i> إضافة ${label} جديد`;
    }

    const fields = getFormFields(type);
    let html = '<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:14px;">';

    for (const f of fields) {
        const val = rec ? (rec[f.key] !== undefined ? rec[f.key] : '') : '';
        const req = f.required ? '<span style="color:#ef4444;margin-right:4px;">*</span>' : '';
        const isFullWidth = f.type === 'textarea' || f.type === 'file';

        html += `<div class="fg" style="margin-bottom:4px; ${isFullWidth ? 'grid-column: 1 / -1;' : ''}">`;
        html += `<label style="display:block;margin-bottom:6px;font-size:0.85rem;color:#94a3b8;font-weight:600;">${f.label} ${req}</label>`;

        if (f.type === 'select' && f.options) {
            html += `<select id="${f.id}" data-key="${f.key}" style="width:100%;padding:10px 14px;border-radius:10px;background:rgba(15,23,42,0.9);border:1px solid #334155;color:#e2e8f0;font-size:0.9rem;">`;
            for (const opt of f.options) {
                const sel = (val == opt) ? 'selected' : '';
                html += `<option ${sel}>${opt}</option>`;
            }
            html += `</select>`;
        } else if (f.type === 'textarea') {
            html += `<textarea id="${f.id}" data-key="${f.key}" rows="3" style="width:100%;padding:10px 14px;border-radius:10px;background:rgba(15,23,42,0.9);border:1px solid #334155;color:#e2e8f0;font-size:0.9rem;resize:vertical;" placeholder="${f.placeholder||''}">${val}</textarea>`;
        } else {
            html += `<input type="${f.type||'text'}" id="${f.id}" data-key="${f.key}" style="width:100%;padding:10px 14px;border-radius:10px;background:rgba(15,23,42,0.9);border:1px solid #334155;color:#e2e8f0;font-size:0.9rem;" placeholder="${f.placeholder||''}" value="${val}">`;
        }

        html += `</div>`;
    }

    html += '</div>';

    if (formEl) formEl.innerHTML = html;

    openModal('formModal');
    toast('✨ نافذة ' + (editId ? 'التعديل' : 'الإضافة') + ' جاهزة (' + label + ')');
}
window.openForm = openForm;

function saveForm(type) {
    type = type || window.currentEditingType || 'student';
    const collKey = getCollectionKey(type);
    if (!DB[collKey]) DB[collKey] = [];

    const editId = window.currentEditingId;
    const fields = getFormFields(type);

    const newRec = {};
    for (const f of fields) {
        const el = document.getElementById(f.id);
        if (el) {
            newRec[f.key] = el.value;
        }
    }

    if (editId) {
        let item = DB[collKey].find(x =>
            x.id == editId || x.keyId == editId || x.isoCode == editId ||
            x.provider == editId || x.name == editId || x.code == editId
        );
        if (item) {
            Object.assign(item, newRec);
            toast('✅ تم تحديث بيانات السجل بنجاح!');
        } else {
            toast('⚠️ لم يتم العثور على السجل لتحديثه', 1);
        }
    } else {
        const prefix = {
            'student':'STD','employee':'EMP','users':'USR','voucher_receipt':'VCH-R',
            'voucher_payment':'VCH-P','journal_entry':'JRN','currencies':'CUR',
            'banks':'BNK','demand_letters':'DL','alerts':'ALR','archive':'ARC'
        };
        const pfx = prefix[type] || (type.toUpperCase().slice(0,3));
        newRec.id = pfx + '-' + Date.now().toString().slice(-5);
        newRec.schoolId = window.currentSchoolId || 1;
        newRec.date = new Date().toISOString().split('T')[0];

        DB[collKey].unshift(newRec);
        toast('🎉 تم حفظ وإضافة السجل الجديد بنجاح!');
    }

    closeModal('formModal');
    if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();

    window.currentEditingType = null;
    window.currentEditingId = null;
}
window.saveForm = saveForm;
'''

# Replace getFormFields, getCollectionKey, openForm, saveForm if exist
pattern = r'function getFormFields[\s\S]*?window\.saveForm = saveForm;'
if re.search(pattern, js_code):
    js_code = re.sub(pattern, full_form_engine, js_code)
else:
    js_code += '\n' + full_form_engine

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print("SUCCESS: Updated app.js successfully!")

# Now add css styles for draggable and minimized modals
css_minimized_rules = '''
/* ==================== UNIVERSAL DRAGGABLE & MINIMIZED MODAL STYLES ==================== */
.modal-overlay.minimized-overlay {
    background: transparent !important;
    pointer-events: none !important;
    backdrop-filter: none !important;
}

.modal-overlay.minimized-overlay .modal-content {
    pointer-events: auto !important;
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    left: auto !important;
    top: auto !important;
    margin: 0 !important;
    width: 320px !important;
    max-height: 55px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7) !important;
    border: 2px solid var(--secondary) !important;
    background: rgba(15, 23, 42, 0.95) !important;
    border-radius: 12px !important;
    cursor: pointer !important;
}

.modal-content.minimized .modal-body,
.modal-content.minimized .modal-actions {
    display: none !important;
}

.modal-header {
    user-select: none;
}
'''

with open(style_css_path, "r", encoding="utf-8") as f:
    css_code = f.read()

if 'UNIVERSAL DRAGGABLE & MINIMIZED MODAL STYLES' not in css_code:
    css_code += '\n' + css_minimized_rules

with open(style_css_path, "w", encoding="utf-8") as f:
    f.write(css_code)

print("SUCCESS: Updated style.css successfully!")

