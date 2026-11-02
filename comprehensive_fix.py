"""
Comprehensive Fix Script - Addresses ALL root causes:
1. Remove conflicting openForm definitions (keep only the comprehensive one at end)
2. Fix hydrateAndMountAllGrids to ONLY render the ACTIVE page's table
3. Remove duplicate goTo render calls
4. Fix openForm to use the existing HTML formModal (with dynamicForm + formTitle)
5. Remove stray pg-timetable-builder outside pageContainer from school.html
6. Ensure all btn-add onclick calls work with the unified openForm
"""
import re, os, time

print("=" * 70)
print("COMPREHENSIVE FIX - Addressing ALL Root Causes")
print("=" * 70)

# ========================================================================
# STEP 1: Fix app.js
# ========================================================================
print("\n[1/6] Reading app.js...")
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

original_len = len(js)
print(f"  Original size: {original_len} bytes, {js.count(chr(10))} lines")

# ========================================================================
# STEP 2: Remove the DUPLICATE openForm wrappers at lines ~1553-1710 and ~4377-4415
# Keep ONLY the comprehensive CRUD engine openForm at end of file
# ========================================================================
print("\n[2/6] Removing conflicting openForm wrapper definitions...")

# Remove first wrapper: "// ==================== MISSING OPENFORM HANDLERS =="
# This wraps window.openForm with a chain that checks for form-fields/dynamicForm
pattern1 = r'// ==================== MISSING OPENFORM HANDLERS ====================\n.*?(?=\n// (?:=====|Master Central)|\nfunction (?:render|delete)Record)'
match1 = re.search(pattern1, js, re.DOTALL)
if match1:
    print(f"  Found first openForm wrapper block at offset {match1.start()}, length {len(match1.group())}")
    js = js[:match1.start()] + '\n' + js[match1.end():]
    print("  Removed first conflicting openForm wrapper block")
else:
    print("  First openForm wrapper block not found, trying alternate pattern...")
    # Try to find by the const _origOpenFormMissingFix pattern
    alt_pattern = r'const _origOpenFormMissingFix = window\.openForm;.*?(?=\nfunction deleteRecord|\n// ====)'
    alt_match = re.search(alt_pattern, js, re.DOTALL)
    if alt_match:
        js = js[:alt_match.start()] + '\n' + js[alt_match.end():]
        print("  Removed first conflicting block via alternate pattern")

# Remove second wrapper: at ~line 4377
pattern2 = r'const _origOpenFormIssueOrdersModals = window\.openForm;.*?window\.openForm = function\(type, editData\)\s*\{.*?\n\};'
match2 = re.search(pattern2, js, re.DOTALL)
if match2:
    print(f"  Found second openForm wrapper at offset {match2.start()}, length {len(match2.group())}")
    js = js[:match2.start()] + '\n' + js[match2.end():]
    print("  Removed second conflicting openForm wrapper block")
else:
    print("  Second openForm wrapper not found")

# ========================================================================
# STEP 3: Remove duplicate goTo render calls
# The goTo function has two identical blocks of if-statements for the same pages
# ========================================================================
print("\n[3/6] Cleaning up duplicate goTo render calls...")

# Find the goTo function
goto_match = re.search(r'function goTo\(id\)\s*\{', js)
if goto_match:
    # Find the closing brace of goTo
    start = goto_match.start()
    brace_count = 0
    i = goto_match.end() - 1  # position of the opening brace
    end = i
    for end in range(i, len(js)):
        if js[end] == '{':
            brace_count += 1
        elif js[end] == '}':
            brace_count -= 1
            if brace_count == 0:
                break
    
    goto_body = js[start:end+1]
    
    # Remove the FIRST block of Financial/System render*Grid calls (lines 912-924)
    # These are duplicates of the later renderXXX calls (lines 1003-1015)
    # The Grid variants don't exist for most, they'll cause errors
    goto_body = re.sub(
        r'\n\s*// 4 Requested Pages Dispatcher Routing\n'
        r'\s*if \(id === \'pg-system-settings\'\) renderSystemSettingsGrid\(\);\n'
        r'\s*if \(id === \'pg-change-password\'\) renderChangePassword\(\);\n'
        r'\s*if \(id === \'pg-sms-send\'\) renderWhatsappSendGrid\(\);\n'
        r'\s*if \(id === \'pg-sms-settings\'\) renderWhatsappSettingsGrid\(\);\n',
        '\n', goto_body
    )
    goto_body = re.sub(
        r'\n\s*// Financial Pages Dispatcher Routing\n'
        r'\s*if \(id === \'pg-currencies\'\) renderCurrenciesGrid\(\);\n'
        r'\s*if \(id === \'pg-cashbox-inventory\'\) renderCashboxInventoryGrid\(\);\n'
        r'\s*if \(id === \'pg-closings\'\) renderClosingsGrid\(\);\n'
        r'\s*if \(id === \'pg-banks\'\) renderBanksGrid\(\);\n'
        r'\s*if \(id === \'pg-demand-letters\'\) renderDemandLettersGrid\(\);\n',
        '\n', goto_body
    )
    
    # Remove the FIRST duplicate block of generic renders (lines ~984-994)
    # Keep only the second identical block (lines ~1003+)
    # Detect the exact duplicate: pg-vouchers appears twice, pg-custom-reports twice, etc.
    # Remove the first occurrence of each pair
    first_dup = (
        "    if (id === 'pg-vouchers') renderVouchers();\r\n"
        "    if (id === 'pg-custom-reports') updateReportColumns();\r\n"
        "    if (id === 'pg-exam-center') renderExamSchedule();\r\n"
        "    if (id === 'pg-communication-center') renderSmsLogs();\r\n"
        "    if (id === 'pg-inventory-center') renderInventoryItems();\r\n"
    )
    # Count occurrences of this block
    count = goto_body.count(first_dup)
    if count >= 2:
        # Remove the first occurrence only
        idx = goto_body.index(first_dup)
        goto_body = goto_body[:idx] + goto_body[idx + len(first_dup):]
        print(f"  Removed first duplicate render block (was duplicated {count} times)")
    
    # Also handle \n line endings
    first_dup_unix = first_dup.replace('\r\n', '\n')
    count2 = goto_body.count(first_dup_unix)
    if count2 >= 2:
        idx = goto_body.index(first_dup_unix)
        goto_body = goto_body[:idx] + goto_body[idx + len(first_dup_unix):]
        print(f"  Removed first duplicate render block (unix endings, was duplicated {count2} times)")
    
    # Remove the Specific Page Handlers that appear before the page switch
    # These run BEFORE the page is even shown, which is wrong
    goto_body = re.sub(
        r'\n\s*// Specific Page Handlers Routing\n'
        r'\s*if \(id === \'pg-school-info\'\) renderSchoolInfo\(\);\n'
        r'\s*if \(id === \'pg-income-stmt\'\) renderIncomeStmt\(\);\n'
        r'\s*if \(id === \'pg-audit-trail\' \|\| id === \'pg-audit\'\) renderAuditGrid\(\);\n'
        r'\s*if \(id === \'pg-admin-password\'\) renderAdminPassword\(\);\n'
        r'\s*if \(id === \'pg-parent-profile\'\) renderParentProfile\(\);\n'
        r'\s*if \(id === \'pg-parent-fees\'\) renderParentFees\(\);\n'
        r'\s*if \(id === \'pg-parent-attendance\'\) renderParentAttendance\(\);\n'
        r'\s*if \(id === \'pg-parent-grades\'\) renderParentGrades\(\);\n'
        r'\s*if \(id === \'pg-parent-homework\'\) renderParentHomework\(\);\n',
        '\n', goto_body
    )
    
    js = js[:start] + goto_body + js[end+1:]
    print("  Cleaned up goTo function")

# ========================================================================
# STEP 4: Fix hydrateAndMountAllGrids - ONLY render the active page
# ========================================================================
print("\n[4/6] Fixing hydrateAndMountAllGrids to only render active page...")

old_hydrate = re.search(
    r'function hydrateAndMountAllGrids\(\)\s*\{.*?\}\s*\nwindow\.hydrateAndMountAllGrids\s*=\s*hydrateAndMountAllGrids;',
    js, re.DOTALL
)
if old_hydrate:
    new_hydrate = """function hydrateAndMountAllGrids() {
    if (typeof ensureAllDataPresent === 'function') ensureAllDataPresent();
    
    // ONLY render the currently active page's grid - NOT all grids
    const activePage = document.querySelector('.page.active');
    if (!activePage) return;
    const activeId = activePage.id;
    
    // Route to the correct render function for the active page only
    try {
        if (activeId === 'pg-dashboard' && typeof renderDashboard === 'function') renderDashboard();
        if (activeId === 'pg-users' && typeof renderUsersGrid === 'function') renderUsersGrid();
        if ((activeId === 'pg-audit-trail' || activeId === 'pg-audit') && typeof renderAuditGrid === 'function') renderAuditGrid();
        if (activeId === 'pg-alerts' && typeof renderAlerts === 'function') renderAlerts();
        if (activeId === 'pg-archive' && typeof renderArchive === 'function') renderArchive();
        if (activeId === 'pg-posting' && typeof renderPosting === 'function') renderPosting();
        if (activeId === 'pg-currencies' && typeof renderCurrencies === 'function') renderCurrencies();
        if (activeId === 'pg-cashbox-inventory' && typeof renderCashboxInventory === 'function') renderCashboxInventory();
        if (activeId === 'pg-closings' && typeof renderClosings === 'function') renderClosings();
        if (activeId === 'pg-banks' && typeof renderBanks === 'function') renderBanks();
        if (activeId === 'pg-demand-letters' && typeof renderDemandLetters === 'function') renderDemandLetters();
        if (activeId === 'pg-system-settings' && typeof renderSystemSettings === 'function') renderSystemSettings();
        if (activeId === 'pg-sms-send' && typeof renderSmsSend === 'function') renderSmsSend();
        if (activeId === 'pg-sms-settings' && typeof renderSmsSettings === 'function') renderSmsSettings();
        if (activeId === 'pg-vouchers' && typeof renderVouchers === 'function') renderVouchers();
        if (activeId === 'pg-students' && typeof renderStudentRegister === 'function') renderStudentRegister();
        if (activeId === 'pg-student-register' && typeof renderStudentRegister === 'function') renderStudentRegister();
        if (activeId === 'pg-employees' && typeof renderEmployees === 'function') renderEmployees();
        if (activeId === 'pg-school-info' && typeof renderSchoolInfo === 'function') renderSchoolInfo();
    } catch(e) { console.warn('hydrateAndMountAllGrids error:', e); }
}
window.hydrateAndMountAllGrids = hydrateAndMountAllGrids;"""
    
    js = js[:old_hydrate.start()] + new_hydrate + js[old_hydrate.end():]
    print("  Replaced hydrateAndMountAllGrids with active-page-only renderer")
else:
    print("  WARNING: hydrateAndMountAllGrids not found!")

# ========================================================================
# STEP 5: Fix the CRUD engine's openForm to use the EXISTING HTML formModal
# The HTML already has: #formModal with #formTitle and #dynamicForm
# So openForm should populate #dynamicForm (not create a new modal)
# ========================================================================
print("\n[5/6] Rewriting openForm to use existing HTML formModal...")

# Remove the entire CRUD engine block and replace with a proper one
old_crud = re.search(
    r'// ==================== COMPLETE UNIVERSAL DYNAMIC FORM & CRUD ENGINE ====================.*$',
    js, re.DOTALL
)
if old_crud:
    js = js[:old_crud.start()]
    print("  Removed old CRUD engine block")

# Build proper CRUD engine that uses the existing HTML modal
new_crud_engine = r"""
// ==================== UNIFIED FORM & CRUD ENGINE (Uses existing #formModal) ====================

window.currentEditingType = null;
window.currentEditingId = null;

function getCollectionKey(type) {
    const m = {
        'student':'students','students':'students','stage':'stages','stages':'stages',
        'section':'sections','sections':'sections','subject':'subjects','subjects':'subjects',
        'employee':'employees','employees':'employees','contract':'empContractsData',
        'advance':'empAdvancesData','user':'usersData','users':'usersData',
        'voucher':'vouchers','voucher_receipt':'vouchers','voucher_payment':'vouchers',
        'journal':'journal','journal_entry':'journal',
        'enrollment':'enrollment','homework':'homework',
        'currencies':'currenciesData','cashbox_inventory':'cashboxInventoryData',
        'closings':'closingsData','banks':'banksData','demand_letters':'demandLettersData',
        'system_settings':'systemSettingsData',
        'whatsapp_send':'whatsappSendData','whatsapp_settings':'whatsappSettingsData',
        'alerts':'alertsData','archive':'archiveData','posting':'postingData',
        'inventory':'inventory_items','inventory-items':'inventory_items',
        'item-categories':'itemCategoriesGridData',
        'activity':'activities','activities':'activitiesGridData',
        'activity-types':'activity_types','activity-supervisors':'activity_supervisors',
        'activity-enrollment':'activity_enrollment','activity-reports':'activity_reports',
        'transport':'transport','transport-routes':'transportRoutesGridData',
        'buses':'busesGridData','transport-enrollment':'transportEnrollmentGridData',
        'supply-orders':'supplyOrdersGridData','issue-orders':'issueOrdersGridData',
        'suppliers':'suppliersGridData','stocktake':'inventoryReportsGridData',
        'sms-templates':'smsTemplatesGridData',
        'academic-years':'stages','academic-calendar':'academic_calendar',
        'required-docs':'required_docs','violations-catalog':'violations_catalog',
        'classrooms':'classroomsData','grade-progression':'grade_progression',
        'subject-distribution':'subject_distribution','grade-types':'grade_types',
        'grade-ratings':'grade_ratings','fee-categories':'fee_categories',
        'discount-categories':'discount_categories','installment-plans':'installment_plans',
        'grade-fees':'grade_fees','parents':'students',
        'discontinued':'discontinuedStudents','class-notes':'classNotesData',
        'guarantors':'guarantorsData','teacher-subjects':'teacherSubjectsData',
        'emp-notices':'empNoticesData','exam_halls':'examHallsData',
        'hall-distribution':'hallDistributionData','substitute':'substituteData',
        'cashbox':'cashboxes','chart-accounts':'chart_accounts',
        'cost-centers':'costCenters','account-ceiling':'accountLimits',
        'class-times':'classTimesGridData',
        'leave-request':'leaveRequestsData','performance-eval':'employees',
        'custom-report':'customReportsGridData',
        'admin-messages':'adminMessagesGridData','shortcuts':'shortcutsGridData',
        'faq-article':'faqGridData','support-ticket':'faqGridData',
        'dictionary':'dictionaryGridData','personal-info':'personalInfoGridData',
        'change-password':'usersData',
        'school':'schools','school_info':'schools',
        'success-rate-section':'successRateSubjectGridData'
    };
    return m[type] || (type + 'Data');
}

// Form field definitions for each entity type
function getFormFields(type) {
    const fieldDefs = {
        'student': [
            {id:'f_name', label:'اسم الطالب الرباعي', type:'text', required:true, placeholder:'أدخل اسم الطالب الرباعي', key:'name'},
            {id:'f_grade', label:'المرحلة والصف الدراسي', type:'select', options:['الثالث الثانوي','الثاني الثانوي','الأول الثانوي','التاسع الأساسي','الثامن الأساسي','السابع الأساسي'], key:'grade'},
            {id:'f_section', label:'الشعبة', type:'select', options:['أ','ب','ج','د'], key:'section'},
            {id:'f_gender', label:'الجنس', type:'select', options:['ذكر','أنثى'], key:'gender'},
            {id:'f_status', label:'الحالة', type:'select', options:['مستمر','متوقف','خريج','منسحب'], key:'status'}
        ],
        'employee': [
            {id:'f_name', label:'اسم الموظف / المعلم', type:'text', required:true, placeholder:'أدخل الاسم الكامل', key:'name'},
            {id:'f_role', label:'المسمى الوظيفي', type:'text', placeholder:'معلم / إداري / محاسب', key:'role'},
            {id:'f_dept', label:'القسم / الإدارة', type:'text', placeholder:'الكادر التعليمي', key:'dept'},
            {id:'f_salary', label:'الراتب الأساسي', type:'number', placeholder:'250000', key:'salary'},
            {id:'f_status', label:'الحالة', type:'select', options:['نشط 🟢','موقوف 🔴','إجازة 🟡'], key:'status'}
        ],
        'users': [
            {id:'f_name', label:'اسم المستخدم الكامل', type:'text', required:true, key:'name'},
            {id:'f_username', label:'اسم الدخول (Username)', type:'text', key:'username'},
            {id:'f_role', label:'الدور والصلاحية', type:'select', options:['مدير النظام','محاسب','معلم','ولي أمر','طالب'], key:'roleName'},
            {id:'f_email', label:'البريد الإلكتروني', type:'email', key:'email'},
            {id:'f_status', label:'الحالة', type:'select', options:['نشط 🟢','معطل 🔴','مقفل 🟡'], key:'status'}
        ],
        'stage': [
            {id:'f_grade', label:'اسم المرحلة / الصف', type:'text', required:true, placeholder:'مثال: الثالث الثانوي', key:'grade'},
            {id:'f_code', label:'كود المرحلة', type:'text', placeholder:'G12', key:'code'}
        ],
        'section': [
            {id:'f_name', label:'اسم الشعبة', type:'text', required:true, placeholder:'مثال: أ', key:'name'},
            {id:'f_grade', label:'الصف', type:'text', placeholder:'الثالث الثانوي', key:'grade'}
        ],
        'subject': [
            {id:'f_name', label:'اسم المادة', type:'text', required:true, placeholder:'رياضيات / فيزياء', key:'name'},
            {id:'f_code', label:'كود المادة', type:'text', placeholder:'MATH-101', key:'code'},
            {id:'f_max', label:'الدرجة العظمى', type:'number', placeholder:'100', key:'maxGrade'}
        ],
        'voucher_receipt': [
            {id:'f_payerName', label:'اسم الدافع / المستلم منه', type:'text', required:true, key:'payerName'},
            {id:'f_amount', label:'المبلغ', type:'number', required:true, key:'amount'},
            {id:'f_desc', label:'البيان / الوصف', type:'text', key:'desc'},
            {id:'f_method', label:'طريقة الدفع', type:'select', options:['نقدي','تحويل بنكي','شيك','POS'], key:'method'}
        ],
        'voucher_payment': [
            {id:'f_payeeName', label:'اسم المستفيد / المدفوع له', type:'text', required:true, key:'payerName'},
            {id:'f_amount', label:'المبلغ', type:'number', required:true, key:'amount'},
            {id:'f_desc', label:'البيان / الوصف', type:'text', key:'desc'},
            {id:'f_method', label:'طريقة الدفع', type:'select', options:['نقدي','تحويل بنكي','شيك'], key:'method'}
        ],
        'journal_entry': [
            {id:'f_desc', label:'البيان / القيد', type:'text', required:true, placeholder:'قيد يومية', key:'desc'},
            {id:'f_debit', label:'حساب المدين', type:'text', key:'debitAcc'},
            {id:'f_credit', label:'حساب الدائن', type:'text', key:'creditAcc'},
            {id:'f_amount', label:'المبلغ', type:'number', key:'amount'}
        ],
        'currencies': [
            {id:'f_code', label:'كود العملة (ISO)', type:'text', required:true, placeholder:'USD', key:'isoCode'},
            {id:'f_name', label:'اسم العملة (AR/EN)', type:'text', placeholder:'دولار أمريكي | US Dollar', key:'nameArEn'},
            {id:'f_rate', label:'سعر الصرف الرسمي', type:'text', placeholder:'1 USD = 530 YER', key:'officialRate'},
            {id:'f_symbol', label:'رمز العملة', type:'text', placeholder:'$', key:'symbol'}
        ],
        'cashbox_inventory': [
            {id:'f_safe', label:'اسم الخزنة / الصندوق', type:'text', required:true, key:'safeName'},
            {id:'f_book', label:'الرصيد الدفتري', type:'text', key:'bookBalance'},
            {id:'f_actual', label:'الرصيد الفعلي', type:'text', key:'actualBalance'},
            {id:'f_diff', label:'الفرق', type:'text', key:'diff'}
        ],
        'banks': [
            {id:'f_bank', label:'اسم البنك والفرع', type:'text', required:true, key:'bankNameBranch'},
            {id:'f_acc', label:'رقم الحساب (IBAN)', type:'text', key:'iban'},
            {id:'f_balance', label:'الرصيد الحالي', type:'text', key:'currentBalance'},
            {id:'f_currency', label:'عملة الحساب', type:'select', options:['YER','USD','SAR','EUR'], key:'currency'}
        ],
        'demand_letters': [
            {id:'f_payer', label:'اسم المدين / ولي الأمر', type:'text', required:true, key:'payerName'},
            {id:'f_amount', label:'المبلغ المستحق', type:'text', key:'amountDue'},
            {id:'f_due', label:'تاريخ الاستحقاق', type:'date', key:'dueDate'},
            {id:'f_status', label:'الحالة', type:'select', options:['قيد المطالبة 🟡','مسددة 🟢','متعثرة 🔴'], key:'status'}
        ],
        'system_settings': [
            {id:'f_key', label:'كود الإعداد (Setting Key)', type:'text', required:true, key:'keyId'},
            {id:'f_name', label:'اسم الإعداد (AR/EN)', type:'text', key:'nameArEn'},
            {id:'f_val', label:'القيمة الحالية', type:'text', key:'val'},
            {id:'f_scope', label:'النطاق', type:'select', options:['عام (General)','أمني (Security)','إقليمي (Regional)'], key:'scope'}
        ],
        'whatsapp_send': [
            {id:'f_phone', label:'رقم WhatsApp المستهدف', type:'text', required:true, placeholder:'+967 770000000', key:'recipient'},
            {id:'f_template', label:'القالب المعتمد', type:'text', placeholder:'قالب_إشعار_سند_مالي (Utility)', key:'template'},
            {id:'f_media', label:'المرفقات (Document)', type:'text', placeholder:'سند_قبض.pdf', key:'media'}
        ],
        'whatsapp_settings': [
            {id:'f_provider', label:'مزود الخدمة', type:'text', required:true, placeholder:'Meta Cloud API', key:'provider'},
            {id:'f_credits', label:'رصيد الرسائل', type:'text', key:'credits'},
            {id:'f_webhook', label:'Webhook Endpoint', type:'text', key:'webhook'}
        ],
        'alerts': [
            {id:'f_name', label:'اسم التنبيه / القاعدة', type:'text', required:true, key:'name'},
            {id:'f_trigger', label:'حدث التفعيل', type:'text', key:'trigger'},
            {id:'f_audience', label:'الجمهور المستهدف', type:'text', key:'audience'},
            {id:'f_template', label:'قالب الرسالة', type:'text', key:'template'}
        ],
        'archive': [
            {id:'f_title', label:'عنوان الوثيقة', type:'text', required:true, key:'title'},
            {id:'f_type', label:'نوع الوثيقة', type:'select', options:['قرار إداري','تعميم','محضر اجتماع','عقد','مستند مالي'], key:'docType'},
            {id:'f_file', label:'اسم الملف', type:'text', key:'fileName'}
        ],
        'homework': [
            {id:'f_title', label:'عنوان الواجب', type:'text', required:true, key:'title'},
            {id:'f_subject', label:'المادة', type:'text', key:'subject'},
            {id:'f_grade', label:'الصف', type:'text', key:'grade'},
            {id:'f_due', label:'تاريخ التسليم', type:'date', key:'dueDate'}
        ],
        'enrollment': [
            {id:'f_student', label:'اسم الطالب', type:'text', required:true, key:'studentName'},
            {id:'f_grade', label:'الصف', type:'text', key:'grade'},
            {id:'f_year', label:'العام الدراسي', type:'text', placeholder:'2025-2026', key:'year'},
            {id:'f_fee', label:'الرسوم المقررة', type:'number', key:'totalFee'}
        ]
    };
    
    // Default generic fields for any unrecognized type
    const defaultFields = [
        {id:'f_name', label:'الاسم / المعرف', type:'text', required:true, placeholder:'أدخل البيان...', key:'name'},
        {id:'f_cat', label:'التصنيف / النوع', type:'text', placeholder:'عام', key:'category'},
        {id:'f_val', label:'القيمة / الحالة', type:'text', placeholder:'نشط', key:'status'}
    ];
    
    return fieldDefs[type] || defaultFields;
}

function openForm(type, editData) {
    type = type || 'student';
    window.currentEditingType = type;
    
    // Handle editData - could be an ID (number/string) or an object
    let editId = null;
    let rec = null;
    
    if (editData && typeof editData === 'object' && !Array.isArray(editData)) {
        rec = editData;
        editId = rec.id || rec.keyId || rec.isoCode || null;
    } else if (editData !== undefined && editData !== null) {
        editId = editData;
    }
    
    window.currentEditingId = editId;
    
    // Find existing record if editing by ID
    if (editId && !rec) {
        const collKey = getCollectionKey(type);
        const collection = DB[collKey] || [];
        rec = collection.find(x => 
            x.id == editId || x.keyId == editId || x.isoCode == editId || 
            x.provider == editId || x.name == editId
        );
    }
    
    // Get the existing formModal from the HTML
    const modal = document.getElementById('formModal');
    const titleEl = document.getElementById('formTitle');
    const formEl = document.getElementById('dynamicForm') || document.getElementById('form-fields');
    
    if (!modal) {
        console.error('formModal not found in HTML!');
        toast('خطأ: نموذج الإدخال غير موجود في الصفحة', 1);
        return;
    }
    
    // Set title
    const typeLabels = {
        'student':'طالب','employee':'موظف','users':'مستخدم','stage':'مرحلة دراسية',
        'section':'شعبة','subject':'مادة','voucher_receipt':'سند قبض','voucher_payment':'سند صرف',
        'journal_entry':'قيد يومية','currencies':'عملة','cashbox_inventory':'جرد خزنة',
        'banks':'حساب بنكي','demand_letters':'مطالبة مالية','system_settings':'إعداد نظام',
        'whatsapp_send':'رسالة واتساب','whatsapp_settings':'إعدادات واتساب',
        'alerts':'تنبيه','archive':'مستند أرشيف','homework':'واجب مدرسي',
        'enrollment':'تسجيل طالب','change-password':'تغيير كلمة المرور',
        'custom-report':'تقرير مخصص','classrooms':'فصل دراسي','exam_halls':'قاعة امتحان',
        'contract':'عقد موظف','advance':'سلفة / قرض','cashbox':'صندوق نقدي',
        'chart-accounts':'حساب محاسبي','cost-centers':'مركز تكلفة',
        'account-ceiling':'سقف حساب','activity-types':'نوع نشاط',
        'transport-routes':'خط نقل','buses':'حافلة','suppliers':'مورد',
        'parents':'ولي أمر','guarantors':'كفيل / ضامن',
        'academic-years':'عام دراسي','academic-calendar':'حدث تقويمي',
        'violations-catalog':'مخالفة سلوكية','class-times':'حصة زمنية'
    };
    const label = typeLabels[type] || type;
    
    if (titleEl) {
        titleEl.innerHTML = editId ? 
            `<i class="fa-solid fa-pen"></i> تعديل بيانات ${label} (${editId})` : 
            `<i class="fa-solid fa-plus-circle"></i> إضافة ${label} جديد`;
    }
    
    // Build form fields HTML
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
    
    // Show the modal
    modal.classList.add('active');
    
    toast('✨ نافذة ' + (editId ? 'التعديل' : 'الإضافة') + ' جاهزة (' + label + ')');
}
window.openForm = openForm;


function saveForm(type) {
    type = type || window.currentEditingType || 'student';
    const collKey = getCollectionKey(type);
    if (!DB[collKey]) DB[collKey] = [];
    
    const editId = window.currentEditingId;
    const fields = getFormFields(type);
    
    // Collect values from form inputs
    const newRec = {};
    for (const f of fields) {
        const el = document.getElementById(f.id);
        if (el) {
            newRec[f.key] = el.value;
        }
    }
    
    if (editId) {
        // Update existing record
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
        // Create new record with auto ID
        const prefix = {
            'student':'STD','employee':'EMP','users':'USR','voucher_receipt':'VCH-R',
            'voucher_payment':'VCH-P','journal_entry':'JRN','currencies':'CUR',
            'banks':'BNK','demand_letters':'DL','alerts':'ALR','archive':'ARC',
            'homework':'HW','enrollment':'ENR'
        };
        const pfx = prefix[type] || 'REC';
        newRec.id = pfx + '-' + Date.now().toString().slice(-6);
        newRec.schoolId = window.currentSchoolId || 1;
        newRec.date = new Date().toISOString().split('T')[0];
        
        DB[collKey].unshift(newRec);
        toast('🎉 تم إضافة سجل جديد (' + newRec.id + ') بنجاح!');
    }
    
    // Close modal
    closeModal('formModal');
    
    // Re-render active page
    if (typeof hydrateAndMountAllGrids === 'function') hydrateAndMountAllGrids();
    
    // Also try calling the active page's specific render
    const activePage = document.querySelector('.page.active');
    if (activePage) {
        const activeId = activePage.id;
        if (typeof goTo === 'function') {
            // Re-trigger goTo to re-render the current page
            const pg = document.getElementById(activeId);
            if (pg) pg.classList.add('active');
        }
    }
    
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
"""

js += '\n' + new_crud_engine + '\n'
print("  Injected new unified CRUD engine")

# ========================================================================
# STEP 6: Write the fixed app.js
# ========================================================================
print(f"\n[6/6] Writing fixed app.js ({len(js)} bytes)...")
with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"  Written! Size change: {original_len} -> {len(js)} bytes")

# ========================================================================
# STEP 7: Fix school.html - remove stray pg-timetable-builder outside pageContainer
# ========================================================================
print("\n[BONUS] Fixing school.html - removing stray content outside pageContainer...")
for html_file in ['frontend/school.html', 'frontend/admin.html', 'frontend/parent.html']:
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Remove stray pg-timetable-builder div outside pageContainer
        stray = re.search(
            r'<div id="pg-timetable-builder" class="page-content".*?</div>\s*</div>\s*</div>',
            html, re.DOTALL
        )
        if stray:
            html = html[:stray.start()] + html[stray.end():]
            print(f"  Removed stray pg-timetable-builder from {html_file}")
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)

# ========================================================================
# Verify brace balance
# ========================================================================
print("\n[VERIFY] Checking brace balance...")
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

opens = content.count('{')
closes = content.count('}')
print(f"  Open braces: {opens}")
print(f"  Close braces: {closes}")
print(f"  Difference: {opens - closes}")

if opens != closes:
    print("  ⚠️ BRACE IMBALANCE DETECTED! Will need further fix.")
else:
    print("  ✅ Braces balanced perfectly!")

print("\n" + "=" * 70)
print("COMPREHENSIVE FIX COMPLETE!")
print("=" * 70)
