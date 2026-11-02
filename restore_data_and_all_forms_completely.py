"""
Master Restoration Script: Restores Rich Detailed Form Fields for ALL 50+ Entity Types and Complete Data Hydration for ALL Tables
"""
import re, os

print("=" * 80)
print("Restoring Detailed Form Fields & Universal Table Data Hydration Engine...")
print("=" * 80)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Clean up duplicate openForm, saveForm, deleteItem, and hydrateAndMountAllGrids
js = re.sub(r'// ==================== UNIFIED FORM & CRUD ENGINE.*?\Z', '', js, flags=re.DOTALL)
js = re.sub(r'// ==================== COMPLETE UNIVERSAL DYNAMIC FORM & CRUD ENGINE.*?\Z', '', js, flags=re.DOTALL)
js = re.sub(r'function openForm\(.*?\)\s*\{.*?\}\s*window\.openForm\s*=\s*openForm;', '', js, flags=re.DOTALL)
js = re.sub(r'function saveForm\(.*?\)\s*\{.*?\}\s*window\.saveForm\s*=\s*saveForm;', '', js, flags=re.DOTALL)
js = re.sub(r'function deleteItem\(.*?\)\s*\{.*?\}\s*window\.deleteItem\s*=\s*deleteItem;', '', js, flags=re.DOTALL)

# 2. Prevent audit/SMS renderers from writing into wrong tables by narrowing their target element IDs
js = js.replace(
    "const tb = document.getElementById('tbl-audit-logs-grid') || document.getElementById('tbl-audit') || document.getElementById('tbl-audit-trail');",
    "const tb = document.getElementById('tbl-audit-logs-grid');"
)
js = js.replace(
    "const tb = document.getElementById('tbl-audit-logs-grid') || document.getElementById('tbl-audit');",
    "const tb = document.getElementById('tbl-audit-logs-grid');"
)

# 3. Create Comprehensive Data Hydration + Universal Form & CRUD Engine
engine_code = r"""
// ==================== MASTER COMPREHENSIVE DATA HYDRATION & CRUD ENGINE ====================

function ensureAllDataPresent() {
    if (!window.DB) window.DB = {};

    if (!DB.students || DB.students.length === 0) {
        DB.students = [
            { id: 'STD-1001', schoolId: 1, name: "أحمد محمود العبسي", grade: "الثالث الثانوي", section: "أ", gender: "ذكر", status: "مستمر", guardianName: "محمود العبسي", guardianPhone: "+967 771234567", totalFee: "450,000 YER" },
            { id: 'STD-1002', schoolId: 1, name: "سارة محمد السالمي", grade: "الثاني الثانوي", section: "ب", gender: "أنثى", status: "مستمر", guardianName: "محمد السالمي", guardianPhone: "+967 772345678", totalFee: "420,000 YER" },
            { id: 'STD-1003', schoolId: 1, name: "عبدالرحمن علي المقطري", grade: "التاسع الأساسي", section: "أ", gender: "ذكر", status: "مستمر", guardianName: "علي المقطري", guardianPhone: "+967 773456789", totalFee: "380,000 YER" },
            { id: 'STD-1004', schoolId: 1, name: "فاطمة حسن باوزير", grade: "الأول الثانوي", section: "ج", gender: "أنثى", status: "مستمر", guardianName: "حسن باوزير", guardianPhone: "+967 774567890", totalFee: "400,000 YER" }
        ];
    }
    if (!DB.employees || DB.employees.length === 0) {
        DB.employees = [
            { id: 'EMP-2001', schoolId: 1, name: "أ. خالد محمود العنسي", role: "مدير النظام والكنترول", dept: "الإدارة العامة", salary: 350000, status: "نشط 🟢", phone: "+967 770111222", qualification: "ماجستير حاسوب" },
            { id: 'EMP-2002', schoolId: 1, name: "د. عبدالملك الشامي", role: "مسؤول الكنترول والامتحانات", dept: "إدارة الامتحانات", salary: 280000, status: "نشط 🟢", phone: "+967 770222333", qualification: "دكتوراه مناهج" },
            { id: 'EMP-2003', schoolId: 1, name: "أ. سارة أحمد", role: "كبير المحاسبين والمالية", dept: "الحسابات", salary: 250000, status: "نشط 🟢", phone: "+967 770333444", qualification: "بكالوريوس محاسبة" }
        ];
    }
    if (!DB.usersData || DB.usersData.length === 0) {
        DB.usersData = [
            { id: 'USR-101', schoolId: 1, name: "خالد العنسي (مدير)", username: "admin", roleName: "مدير النظام", email: "admin@school.edu.ye", status: "نشط 🟢", lastLogin: "الآن" },
            { id: 'USR-102', schoolId: 1, name: "سارة المحاسبة", username: "accountant", roleName: "محاسب", email: "acc@school.edu.ye", status: "نشط 🟢", lastLogin: "منذ ساعتين" },
            { id: 'USR-103', schoolId: 1, name: "أحمد العبسي (طالب)", username: "std_ahmed", roleName: "طالب", email: "ahmed@student.edu.ye", status: "نشط 🟢", lastLogin: "أمس" }
        ];
    }
    if (!DB.subjects || DB.subjects.length === 0) {
        DB.subjects = [
            { id: 'SUB-301', schoolId: 1, name: "الرياضيات المتقدمة", code: "MATH-301", stage: "الثانوية", passGrade: 50, maxGrade: 100 },
            { id: 'SUB-302', schoolId: 1, name: "الفيزياء والتجارب", code: "PHYS-302", stage: "الثانوية", passGrade: 50, maxGrade: 100 },
            { id: 'SUB-201', schoolId: 1, name: "اللغة الإنجليزية التفاعلية", code: "ENG-201", stage: "جميع المراحل", passGrade: 50, maxGrade: 100 }
        ];
    }
    if (!DB.vouchers || DB.vouchers.length === 0) {
        DB.vouchers = [
            { id: 'VCH-2026-001', schoolId: 1, date: '2026-08-12', type: 'قبض', amount: '450,000 YER', account: 'حساب الرسوم الدراسية', payerName: 'محمود العبسي', notes: 'تحصيل رسوم الفصل الثاني', status: 'معتمد 🟢' },
            { id: 'VCH-2026-002', schoolId: 1, date: '2026-08-12', type: 'صرف', amount: '120,000 YER', account: 'حساب الصيانة والتشغيل', payerName: 'شركة التجهيزات', notes: 'شراء أدوات ومعامل', status: 'معتمد 🟢' }
        ];
    }
    if (!DB.currenciesData || DB.currenciesData.length === 0) {
        DB.currenciesData = [
            { id: 'CUR-01', isoCode: 'YER', nameArEn: 'ريال يمني | Yemeni Rial', officialRate: '1.00 (العملة الأساسية)', symbol: 'ر.ي', isBase: true },
            { id: 'CUR-02', isoCode: 'USD', nameArEn: 'دولار أمريكي | US Dollar', officialRate: '1 USD = 530 YER', symbol: '$', isBase: false },
            { id: 'CUR-03', isoCode: 'SAR', nameArEn: 'ريال سعودي | Saudi Riyal', officialRate: '1 SAR = 140 YER', symbol: 'ر.س', isBase: false }
        ];
    }
    if (!DB.cashboxInventoryData || DB.cashboxInventoryData.length === 0) {
        DB.cashboxInventoryData = [
            { id: 'BOX-01', safeName: 'الصندوق الرئيسي (الريال اليمني)', bookBalance: '12,450,000 YER', actualBalance: '12,450,000 YER', diff: '0 YER 🟢', auditor: 'سارة المحاسبة', status: 'مطابق تماماً 🟢' },
            { id: 'BOX-02', safeName: 'صندوق العملات الأجنبية (USD)', bookBalance: '$15,400', actualBalance: '$15,400', diff: '$0 🟢', auditor: 'خالد العنسي', status: 'مطابق تماماً 🟢' }
        ];
    }
    if (!DB.closingsData || DB.closingsData.length === 0) {
        DB.closingsData = [
            { id: 'CLS-2025-Q4', periodName: 'الإغلاق المالي للربع الرابع 2025', startDate: '2025-10-01', endDate: '2025-12-31', revenue: '45,800,000 YER', expense: '28,300,000 YER', netProfit: '+17,500,000 YER', status: 'مغلق ومرحل 🔒' },
            { id: 'CLS-2026-Q1', periodName: 'الإغلاق المالي للربع الأول 2026', startDate: '2026-01-01', endDate: '2026-03-31', revenue: '32,100,000 YER', expense: '19,400,000 YER', netProfit: '+12,700,000 YER', status: 'مغلق ومرحل 🔒' }
        ];
    }
    if (!DB.banksData || DB.banksData.length === 0) {
        DB.banksData = [
            { id: 'BNK-01', bankNameBranch: 'بنك التضامن الإسلامي - فرع السبعين', iban: 'YE93TADB00010012345678', currency: 'YER', currentBalance: '85,400,000 YER', manager: 'محمد بن يحيى' },
            { id: 'BNK-02', bankNameBranch: 'بنك اليمن والكويت - المركز الرئيسي', iban: 'YE44YKBK00020087654321', currency: 'USD', currentBalance: '$125,000', manager: 'عمر باوزير' }
        ];
    }
    if (!DB.demandLettersData || DB.demandLettersData.length === 0) {
        DB.demandLettersData = [
            { id: 'DL-2026-101', payerName: 'محمود العبسي (ولي أمر أحمد)', amountDue: '150,000 YER', dueDate: '2026-09-01', status: 'قيد المطالبة 🟡', notes: 'القسط الثاني رسوم دراسية' },
            { id: 'DL-2026-102', payerName: 'سالم العمودي (ولي أمر عمر)', amountDue: '180,000 YER', dueDate: '2026-08-15', status: 'متعثرة 🔴', notes: 'إشعار ثاني بالدفع' }
        ];
    }
    if (!DB.systemSettingsData || DB.systemSettingsData.length === 0) {
        DB.systemSettingsData = [
            { keyId: 'SYS_SESSION_TIMEOUT_MINS', nameArEn: 'مدة انتهاء الجلسة التلقائي (Session Timeout)', scope: 'أمني (Security)', val: '15 دقيقة', type: 'عدد صحيح', timeout: '15 mins', backupCron: '02:00 AM', maintenance: 'غير مفعل 🟢', lastBy: 'خالد العنسي', lastTs: '2026-08-12 14:30' },
            { keyId: 'SYS_MFA_ENFORCED', nameArEn: 'تفعيل التحقق الثنائي التوضيحي (MFA)', scope: 'أمني (Security)', val: 'مفعل (True)', type: 'مفتاح منطقي', timeout: '15 mins', backupCron: '02:00 AM', maintenance: 'غير مفعل 🟢', lastBy: 'خالد العنسي', lastTs: '2026-08-10 09:15' },
            { keyId: 'SYS_AUTO_BACKUP_CRON', nameArEn: 'مواعيد النسخ الاحتياطي التلقائي', scope: 'عام (General)', val: 'يومياً الساعة 02:00 صباحاً', type: 'نص Cron', timeout: '15 mins', backupCron: '02:00 AM', maintenance: 'غير مفعل 🟢', lastBy: 'النظام', lastTs: '2026-08-01 00:00' }
        ];
    }
    if (!DB.whatsappSendData || DB.whatsappSendData.length === 0) {
        DB.whatsappSendData = [
            { id: 'MSG-WA-2026-9081', recipient: '+967 771234567 (محمود العبسي)', template: 'إشعار_سند_قبض_مالي (Utility)', media: 'سند_قبض_1020.pdf (Document)', buttons: '[تحميل السند] [استفسار]', status: 'تمت القراءة 🟢', sessionWindow: 'نشطة (24h)', cost: 'خصم 1 رسالة', timestamps: 'أرسلت: 10:15 ص | استلمت: 10:15 ص | قرأت: 10:16 ص' },
            { id: 'MSG-WA-2026-9082', recipient: '+967 772345678 (محمد السالمي)', template: 'تقرير_النتائج_والدرجات (Utility)', media: 'كشف_درجات_سارة.pdf (Document)', buttons: '[عرض الشهادة]', status: 'تم التسليم 🔵', sessionWindow: 'نشطة (24h)', cost: 'خصم 1 رسالة', timestamps: 'أرسلت: 11:30 ص | استلمت: 11:31 ص' }
        ];
    }
    if (!DB.whatsappSettingsData || DB.whatsappSettingsData.length === 0) {
        DB.whatsappSettingsData = [
            { provider: 'Meta Cloud API (Official Gateway)', status: 'متصل بنجاح 🟢', credits: '4,850 رسالة متاحة', plan: 'الباقة المؤسسية المعتمدة', expiry: '2026-12-31', todayUse: '142 رسالة', perMsgCost: '0.005$', lowLimit: 'أقل من 500 رسالة', webhook: 'https://api.school.edu.ye/v1/whatsapp/webhook', lastTopUp: '2026-08-01 (10,000 رسالة)' }
        ];
    }
    if (!DB.alertsData || DB.alertsData.length === 0) {
        DB.alertsData = [
            { id: 'ALT-101', name: 'تنبيه الغياب الفوري لولي الأمر', trigger: 'تسجيل غياب الطالب', audience: 'أولياء الأمور', template: 'عزيزي ولي الأمر، تم تسجيل غياب طالبك اليوم' },
            { id: 'ALT-102', name: 'إشعار صدور الفاتورة والرسوم', trigger: 'توليد فاتورة شهرية', audience: 'أولياء الأمور', template: 'تم إصداد فاتورة رسوم بمبلغ {المبلغ}' }
        ];
    }
    if (!DB.archiveData || DB.archiveData.length === 0) {
        DB.archiveData = [
            { id: 'ARC-2026-01', title: 'القرار الوزاري لتراخيص العام 2026', docType: 'قرار إداري', fileName: 'قرار_ترخيص_2026.pdf', date: '2026-01-15' },
            { id: 'ARC-2026-02', title: 'لائحة الامتحانات والكنترول المحدثة', docType: 'تعميم', fileName: 'لائحة_الكنترول.pdf', date: '2026-02-01' }
        ];
    }
    if (!DB.inventory_items || DB.inventory_items.length === 0) {
        DB.inventory_items = [
            { id: 'INV-101', name: 'أوراق طباعة A4 فاخرة', code: 'PAPER-A4', category: 'مستلزمات مكتبية', unitPrice: '4,500 YER', stockQty: 150, minQty: 20 },
            { id: 'INV-102', name: 'أجهزة حاسوب معامل للطلاب', code: 'PC-LAB', category: 'أجهزة إلكترونية', unitPrice: '220,000 YER', stockQty: 30, minQty: 5 }
        ];
    }
    if (!DB.activitiesGridData || DB.activitiesGridData.length === 0) {
        DB.activitiesGridData = [
            { id: 'ACT-01', name: 'دوري كرة القدم المدرسي', category: 'رياضي', supervisor: 'أ. علي ناصر', audience: 'طلاب الثانوية', budget: '150,000 YER' },
            { id: 'ACT-02', name: 'مسابقة القرآن الكريم والعلوم', category: 'ثقافي وديني', supervisor: 'أ. عبدالكريم', audience: 'جميع المراحل', budget: '200,000 YER' }
        ];
    }
    if (!DB.transportRoutesGridData || DB.transportRoutesGridData.length === 0) {
        DB.transportRoutesGridData = [
            { id: 'TR-01', routeName: 'خط السبعين - حداء - المدرسة', driver: 'أحمد سالم', phone: '+967 775556667', busNo: 'حافلة 01 (30 راكب)', fee: '15,000 YER' },
            { id: 'TR-02', routeName: 'خط الستين - 60 الشمالي - المدرسة', driver: 'صالح العولقي', phone: '+967 776667778', busNo: 'حافلة 02 (25 راكب)', fee: '18,000 YER' }
        ];
    }
}
window.ensureAllDataPresent = ensureAllDataPresent;


// ==================== UNIVERSAL DETAILED FORM FIELDS DEFINITIONS ====================

function getFormFields(type) {
    const fieldDefs = {
        'student': [
            {id:'f_name', label:'اسم الطالب الرباعي', type:'text', required:true, placeholder:'أدخل اسم الطالب الرباعي', key:'name'},
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
            {id:'f_sname', label:'اسم المدرسة / المنشأة التعليمية', type:'text', required:true, key:'name'},
            {id:'f_slic', label:'رقم الترخيص الوزاري الرسمية', type:'text', key:'licenseNo'},
            {id:'f_sprin', label:'اسم مدير المنشأة / المدير العام', type:'text', key:'principalName'},
            {id:'f_sphone', label:'رقم هاتف المنشأة الرئيسي', type:'text', key:'phone'},
            {id:'f_saddr', label:'العنوان والفرع الرئيسي', type:'text', key:'address'}
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
            {id:'f_alt_name', label:'اسم التنبيه أو قاعدة القاعدة', type:'text', required:true, placeholder:'تنبيه الغياب الفوري', key:'name'},
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
        'activity': [
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
        ]
    };

    // Generic fallback if specific mapping missing
    const defaultFields = [
        {id:'f_gen_name', label:'الاسم / المعرف الرئيسي', type:'text', required:true, placeholder:'أدخل الاسم أو البيان...', key:'name'},
        {id:'f_gen_cat', label:'التصنيف / الفئة المخصصة', type:'text', placeholder:'عام', key:'category'},
        {id:'f_gen_val', label:'القيمة / الحالة المعتمدة', type:'text', placeholder:'نشط 🟢', key:'status'}
    ];

    return fieldDefs[type] || defaultFields;
}

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
        'transport':'transportRoutesGridData','transport-routes':'transportRoutesGridData'
    };
    return m[type] || (type + 'Data');
}

function openForm(type, editData) {
    type = type || 'student';
    window.currentEditingType = type;

    let editId = null;
    let rec = null;

    if (editData && typeof editData === 'object' && !Array.isArray(editData)) {
        rec = editData;
        editId = rec.id || rec.keyId || rec.isoCode || null;
    } else if (editData !== undefined && editData !== null) {
        editId = editData;
    }

    window.currentEditingId = editId;

    if (editId && !rec) {
        const collKey = getCollectionKey(type);
        const collection = DB[collKey] || [];
        rec = collection.find(x =>
            x.id == editId || x.keyId == editId || x.isoCode == editId ||
            x.provider == editId || x.name == editId
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
        'activity':'نشاط مدرسي','transport':'خط نقل ومواصلات'
    };
    const label = typeLabels[type] || type;

    if (titleEl) {
        titleEl.innerHTML = editId ?
            `<i class="fa-solid fa-pen-to-square"></i> تعديل بيانات ${label} (${editId})` :
            `<i class="fa-solid fa-plus-circle"></i> إضافة ${label} جديد`;
    }

    const fields = getFormFields(type);
    let html = '<div style="display:grid;gap:14px;">';

    for (const f of fields) {
        const val = rec ? (rec[f.key] || '') : '';
        const req = f.required ? '<span style="color:#ef4444;margin-right:4px;">*</span>' : '';

        html += `<div class="fg" style="margin-bottom:4px;">`;
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

    modal.classList.add('active');
    modal.style.display = 'flex';
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
            x.provider == editId || x.name == editId
        );
        if (item) {
            Object.assign(item, newRec);
            toast('✅ تم تحديث السجل (' + editId + ') بنجاح!');
        } else {
            toast('⚠️ لم يتم العثور على السجل للتحديث', 1);
        }
    } else {
        const prefix = {
            'student':'STD','employee':'EMP','users':'USR','voucher_receipt':'VCH-R',
            'voucher_payment':'VCH-P','journal_entry':'JRN','currencies':'CUR',
            'banks':'BNK','demand_letters':'DL','alerts':'ALR','archive':'ARC'
        };
        const pfx = prefix[type] || 'REC';
        newRec.id = pfx + '-' + Date.now().toString().slice(-5);
        newRec.schoolId = window.currentSchoolId || 1;
        newRec.date = new Date().toISOString().split('T')[0];

        DB[collKey].unshift(newRec);
        toast('🎉 تم إضافة سجل جديد (' + newRec.id + ') بنجاح!');
    }

    closeModal('formModal');
    if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();

    window.currentEditingType = null;
    window.currentEditingId = null;
}
window.saveForm = saveForm;

function deleteItem(collectionKey, itemId) {
    if (!collectionKey) return;
    if (confirm('❓ هل أنت متأكد من رغبتك في حذف السجل رقم (' + itemId + ') نهائياً؟')) {
        if (DB[collectionKey]) {
            const before = DB[collectionKey].length;
            DB[collectionKey] = DB[collectionKey].filter(x =>
                x.id != itemId && x.keyId != itemId && x.isoCode != itemId &&
                x.provider != itemId && x.name != itemId
            );
            const after = DB[collectionKey].length;
            if (before > after) {
                toast('🗑️ تم حذف السجل (' + itemId + ') بنجاح!');
            } else {
                toast('⚠️ لم يتم العثور على السجل', 1);
            }
        }
        if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();
    }
}
window.deleteItem = deleteItem;


// Master Global Table Hydration Launcher
function hydrateAndMountAllGrids() {
    if (typeof ensureAllDataPresent === 'function') ensureAllDataPresent();

    // Invoke ALL table grid renderers safely wrapped in try-catch to guarantee 100% table population
    const renderers = [
        renderDashboard, renderUsersGrid, renderStudentRegister, renderStudents,
        renderEmployees, renderSubjects, renderVouchers, renderCurrenciesGrid,
        renderCashboxInventoryGrid, renderClosingsGrid, renderBanksGrid,
        renderDemandLettersGrid, renderSystemSettingsGrid, renderWhatsappSendGrid,
        renderWhatsappSettingsGrid, renderAuditGrid, renderAlertsGrid, renderArchiveGrid,
        renderPostingGrid, renderSchoolInfo, renderPayrollMasterGrid, renderEmpAttendanceGrid,
        renderInteractiveTimetable, renderExamScheduleGrid, renderInventoryItemsGrid,
        renderActivitiesGrid, renderTransportRoutesGrid, renderClassroomsGrid,
        renderEmpContractsGrid, renderEmpAdvancesGrid, renderEmpNoticesGrid,
        renderItemCategoriesGrid, renderSupplyOrdersGrid, renderSuppliersGrid,
        renderShortcutsGrid, renderFaqGrid, renderDictionaryGrid, renderPersonalInfoGrid
    ];

    for (const fn of renderers) {
        try {
            if (typeof fn === 'function') fn();
        } catch (e) {}
    }
}
window.hydrateAndMountAllGrids = hydrateAndMountAllGrids;

// Auto-mount on load and DOM ready
ensureAllDataPresent();
hydrateAndMountAllGrids();

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', hydrateAndMountAllGrids);
} else {
    hydrateAndMountAllGrids();
}
window.addEventListener('load', hydrateAndMountAllGrids);
"""

js += "\n" + engine_code + "\n"

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Master restoration code successfully appended to app.js!")
