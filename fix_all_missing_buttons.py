"""
Comprehensive fix script to add ALL missing openForm handlers, 
missing functions, and unused tbody render logic.
"""
import re, time

print("=" * 80)
print("COMPREHENSIVE FIX: All Missing Buttons, Forms & Functions")
print("=" * 80)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# ================================================================
# 1. Add missing standalone functions: minModal, publishExamSchedule
# ================================================================
missing_functions = """

// ==================== MISSING STANDALONE FUNCTIONS ====================

// minModal - minimize/close modal by ID
function minModal(id) {
    const m = document.getElementById(id);
    if (m) { m.style.display = 'none'; m.classList.remove('active'); }
}
window.minModal = minModal;

// publishExamSchedule - publish the exam schedule
function publishExamSchedule() {
    toast('📢 جاري نشر جدول الامتحانات وإرسال الإشعارات لجميع الطلاب والمعلمين...');
    setTimeout(() => {
        toast('✅ تم نشر جدول الامتحانات الرسمي بنجاح وتوزيعه على جميع المعنيين!');
    }, 800);
}
window.publishExamSchedule = publishExamSchedule;
"""

if 'function minModal' not in js:
    js += missing_functions
    print("  ✅ Added minModal() and publishExamSchedule()")

# ================================================================
# 2. Add ALL missing openForm handlers in a new wrapper
# ================================================================
missing_forms_wrapper = """

// ==================== MISSING OPENFORM HANDLERS ====================
const _origOpenFormMissingFix = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) { if (_origOpenFormMissingFix) _origOpenFormMissingFix(type, editData); return; }
    let handled = true;
    const d = editData || {};

    if (type === 'change-password') {
        title.innerHTML = '<i class="fa-solid fa-key"></i> تغيير كلمة المرور';
        fields.innerHTML = `
            <div class="fg"><label>كلمة المرور الحالية</label><input type="password" id="fp_current" placeholder="أدخل كلمة المرور الحالية"></div>
            <div class="fg"><label>كلمة المرور الجديدة</label><input type="password" id="fp_new" placeholder="أدخل كلمة المرور الجديدة"></div>
            <div class="fg"><label>تأكيد كلمة المرور الجديدة</label><input type="password" id="fp_confirm" placeholder="أعد إدخال كلمة المرور الجديدة"></div>
            <button class="btn-save" onclick="
                const np = document.getElementById('fp_new')?.value;
                const cp = document.getElementById('fp_confirm')?.value;
                if (!np) { toast('⚠️ أدخل كلمة المرور الجديدة', 1); return; }
                if (np !== cp) { toast('⚠️ كلمتا المرور غير متطابقتين', 1); return; }
                toast('✅ تم تغيير كلمة المرور بنجاح');
                document.getElementById('formModal')?.classList.remove('active');
            " style="width:100%;margin-top:12px;"><i class="fa-solid fa-check"></i> تغيير كلمة المرور</button>
        `;

    } else if (type === 'custom-report') {
        title.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> إنشاء تقرير مخصص جديد';
        fields.innerHTML = `
            <div class="fg"><label>عنوان التقرير</label><input id="fcr_title" placeholder="تقرير الأداء الشهري للأقسام" value="${d.title||''}"></div>
            <div class="fg"><label>مصادر البيانات</label><select id="fcr_source"><option>شؤون الطلاب</option><option>الشؤون المالية</option><option>المواصلات + المالية</option><option>شؤون الموظفين</option><option>المخازن والمشتريات</option><option>الكنترول والامتحانات</option></select></div>
            <div class="fg"><label>نوع العرض</label><select><option>جدول بيانات (Table)</option><option>جدول محوري (Pivot Table)</option><option>رسم بياني (Bar Chart)</option><option>رسم دائري (Pie Chart)</option></select></div>
            <div class="fg"><label>التجميع</label><select><option>حسب الصف</option><option>حسب القسم</option><option>حسب الشهر</option><option>حسب الفصل الدراسي</option></select></div>
            <div class="fg"><label>فلاتر التصفية</label><input placeholder="مثال: الفصل الأول 2025/2026"></div>
            <div class="fg"><label>جدولة التقرير</label><select><option>يدوي (عند الطلب)</option><option>يومي</option><option>أسبوعي</option><option>شهري</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء التقرير المخصص بنجاح وحفظه في المكتبة'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderCustomReportsGrid==='function') renderCustomReportsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ التقرير</button>
        `;

    } else if (type === 'faq-article') {
        title.innerHTML = '<i class="fa-solid fa-book-open"></i> إضافة مقال أو تذكرة دعم جديدة';
        fields.innerHTML = `
            <div class="fg"><label>عنوان المقال / المشكلة</label><input id="faq_title" placeholder="كيفية طباعة المشيت الرسمي؟" value="${d.title||''}"></div>
            <div class="fg"><label>القسم / التصنيف</label><select><option>الكنترول والامتحانات</option><option>شؤون الطلاب</option><option>الشؤون المالية</option><option>شؤون الموظفين</option><option>النظام والإعدادات</option><option>المخازن والمشتريات</option></select></div>
            <div class="fg"><label>خطوات الحل</label><textarea rows="4" placeholder="1. اذهب إلى الكنترول\\n2. اختر المشيت الرسمي\\n3. اضغط طباعة PDF">${d.solution||''}</textarea></div>
            <div class="fg"><label>مستوى الأهمية</label><select><option>عالي (High)</option><option>متوسط (Medium)</option><option>منخفض (Low)</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ المقال في قاعدة المعرفة بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderFaqGrid==='function') renderFaqGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ المقال</button>
        `;

    } else if (type === 'journal_entry') {
        title.innerHTML = '<i class="fa-solid fa-book"></i> إنشاء قيد يومي محاسبي جديد';
        fields.innerHTML = `
            <div class="fg"><label>رقم القيد</label><input id="fj_no" placeholder="JV-2026-0145" value="JV-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>التاريخ</label><input type="date" value="${new Date().toISOString().split('T')[0]}"></div>
            <div class="fg"><label>البيان / الوصف</label><input id="fj_desc" placeholder="قيد تسوية رسوم دراسية" value="${d.description||''}"></div>
            <div class="fg"><label>الحساب المدين</label><select><option>110101 - الصندوق الرئيسي</option><option>120401 - المخزون</option><option>130201 - ذمم مدينة</option></select></div>
            <div class="fg"><label>المبلغ المدين ($)</label><input type="number" id="fj_debit" placeholder="5000" value="${d.debit||''}"></div>
            <div class="fg"><label>الحساب الدائن</label><select><option>410101 - إيرادات الرسوم الدراسية</option><option>210301 - ذمم دائنة</option><option>110201 - البنك</option></select></div>
            <div class="fg"><label>المبلغ الدائن ($)</label><input type="number" id="fj_credit" placeholder="5000" value="${d.credit||''}"></div>
            <div class="fg"><label>مركز التكلفة</label><select><option>الإدارة العامة</option><option>الشؤون الأكاديمية</option><option>المعامل والمختبرات</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ القيد اليومي وترحيله بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderJournalList==='function') renderJournalList();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ وترحيل القيد</button>
        `;

    } else if (type === 'leave-request') {
        title.innerHTML = '<i class="fa-solid fa-plane-departure"></i> تقديم طلب إجازة جديد';
        fields.innerHTML = `
            <div class="fg"><label>اسم الموظف</label><input id="fl_name" placeholder="أ. خالد محمود العنسي" value="${d.employeeName||''}"></div>
            <div class="fg"><label>الرقم الوظيفي</label><input id="fl_empid" placeholder="EMP-2026-0104" value="${d.empId||''}"></div>
            <div class="fg"><label>نوع الإجازة</label><select id="fl_type"><option>إجازة سنوية (Annual)</option><option>إجازة مرضية (Sick)</option><option>إجازة طارئة (Emergency)</option><option>إجازة أمومة (Maternity)</option><option>إجازة بدون راتب (Unpaid)</option></select></div>
            <div class="fg"><label>تاريخ البداية</label><input type="date" id="fl_from"></div>
            <div class="fg"><label>تاريخ النهاية</label><input type="date" id="fl_to"></div>
            <div class="fg"><label>عدد الأيام</label><input type="number" id="fl_days" placeholder="5" value="${d.days||''}"></div>
            <div class="fg"><label>الرصيد المتبقي</label><input value="${d.balance||'25 يوماً'}" readonly style="background:rgba(16,185,129,0.1);color:#34d399;"></div>
            <div class="fg"><label>سبب الإجازة</label><textarea rows="2" placeholder="إجازة سنوية اعتيادية">${d.reason||''}</textarea></div>
            <button class="btn-save" onclick="toast('✅ تم تقديم طلب الإجازة بنجاح وإرساله للمدير المباشر للاعتماد'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderLeaveManagementGrid==='function') renderLeaveManagementGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> إرسال طلب الإجازة</button>
        `;

    } else if (type === 'performance-eval') {
        title.innerHTML = '<i class="fa-solid fa-star-half-stroke"></i> تقييم أداء وكفاءة موظف';
        fields.innerHTML = `
            <div class="fg"><label>اسم الموظف</label><input id="fpe_name" placeholder="أ. خالد محمود العنسي" value="${d.employeeName||''}"></div>
            <div class="fg"><label>الرقم الوظيفي</label><input id="fpe_empid" placeholder="EMP-2026-0104" value="${d.empId||''}"></div>
            <div class="fg"><label>فترة التقييم</label><select><option>الفصل الأول 2025/2026</option><option>الفصل الثاني 2025/2026</option><option>العام الدراسي كاملاً</option></select></div>
            <div class="fg"><label>الالتزام بالدوام (من 20)</label><input type="number" max="20" placeholder="18" value="${d.attendance||''}"></div>
            <div class="fg"><label>جودة العمل والإنجاز (من 25)</label><input type="number" max="25" placeholder="22" value="${d.quality||''}"></div>
            <div class="fg"><label>المبادرة والابتكار (من 15)</label><input type="number" max="15" placeholder="13" value="${d.initiative||''}"></div>
            <div class="fg"><label>العمل الجماعي والتعاون (من 20)</label><input type="number" max="20" placeholder="19" value="${d.teamwork||''}"></div>
            <div class="fg"><label>المظهر والانضباط (من 10)</label><input type="number" max="10" placeholder="9" value="${d.discipline||''}"></div>
            <div class="fg"><label>التطوير المهني (من 10)</label><input type="number" max="10" placeholder="8" value="${d.development||''}"></div>
            <div class="fg"><label>ملاحظات المقيّم</label><textarea rows="2" placeholder="موظف متميز ومنضبط">${d.notes||''}</textarea></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ تقييم الأداء بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderPerformanceEvals==='function') renderPerformanceEvals();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ التقييم</button>
        `;

    } else if (type === 'permission') {
        title.innerHTML = '<i class="fa-solid fa-shield-halved"></i> تعديل صلاحيات المستخدم';
        fields.innerHTML = `
            <div class="fg"><label>اسم المستخدم / الدور</label><input id="fperm_user" placeholder="مدير النظام" value="${d.roleName||''}"></div>
            <div class="fg"><label>مستوى الصلاحية</label><select><option>مدير عام (Full Admin)</option><option>مدير أكاديمي</option><option>محاسب مالي</option><option>معلم (Teacher)</option><option>ولي أمر (Parent - قراءة فقط)</option><option>موظف إداري</option></select></div>
            <h4 style="color:#60a5fa;margin:12px 0 8px;">الصلاحيات التفصيلية:</h4>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> شؤون الطلاب (عرض)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> شؤون الطلاب (تعديل)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> الشؤون المالية (عرض)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> الشؤون المالية (تعديل)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> شؤون الموظفين (عرض)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> شؤون الموظفين (تعديل)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> الكنترول (عرض)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> الكنترول (تعديل)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox" checked> المخازن (عرض)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> المخازن (تعديل)</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> إعدادات النظام</label>
                <label style="display:flex;align-items:center;gap:6px;cursor:pointer;"><input type="checkbox"> حذف البيانات</label>
            </div>
            <button class="btn-save" onclick="toast('✅ تم حفظ صلاحيات المستخدم بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderPermissions==='function') renderPermissions();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ الصلاحيات</button>
        `;

    } else if (type === 'voucher_payment') {
        title.innerHTML = '<i class="fa-solid fa-money-bill-transfer"></i> إنشاء سند صرف جديد';
        fields.innerHTML = `
            <div class="fg"><label>رقم السند</label><input placeholder="PV-2026-0088" value="PV-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>التاريخ</label><input type="date" value="${new Date().toISOString().split('T')[0]}"></div>
            <div class="fg"><label>المستفيد / المصروف له</label><input placeholder="شركة التوريدات المدرسية" value="${d.beneficiary||''}"></div>
            <div class="fg"><label>البيان / الوصف</label><input placeholder="دفعة مستحقات توريد أجهزة حاسوب" value="${d.description||''}"></div>
            <div class="fg"><label>المبلغ ($)</label><input type="number" id="fvp_amount" placeholder="5000" value="${d.amount||''}"></div>
            <div class="fg"><label>طريقة الدفع</label><select><option>نقداً (Cash)</option><option>تحويل بنكي</option><option>شيك</option></select></div>
            <div class="fg"><label>الصندوق / البنك المصدر</label><select><option>الصندوق الرئيسي</option><option>بنك اليمن الدولي</option></select></div>
            <div class="fg"><label>مركز التكلفة</label><select><option>الإدارة العامة</option><option>المعامل</option><option>الصيانة</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء سند الصرف وترحيله بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderVouchers==='function') renderVouchers();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-paper-plane"></i> إصدار سند الصرف</button>
        `;

    } else if (type === 'voucher_receipt') {
        title.innerHTML = '<i class="fa-solid fa-hand-holding-dollar"></i> إنشاء سند قبض جديد';
        fields.innerHTML = `
            <div class="fg"><label>رقم السند</label><input placeholder="RV-2026-0156" value="RV-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>التاريخ</label><input type="date" value="${new Date().toISOString().split('T')[0]}"></div>
            <div class="fg"><label>المستلم منه / الدافع</label><input placeholder="ولي أمر الطالب محمد أحمد" value="${d.payer||''}"></div>
            <div class="fg"><label>البيان / الوصف</label><input placeholder="تحصيل القسط الثاني من الرسوم الدراسية" value="${d.description||''}"></div>
            <div class="fg"><label>المبلغ ($)</label><input type="number" id="fvr_amount" placeholder="2500" value="${d.amount||''}"></div>
            <div class="fg"><label>طريقة الدفع</label><select><option>نقداً (Cash)</option><option>تحويل بنكي</option><option>شيك</option></select></div>
            <div class="fg"><label>الصندوق / البنك المستلم</label><select><option>الصندوق الرئيسي</option><option>بنك اليمن الدولي</option></select></div>
            <div class="fg"><label>الطالب المرتبط</label><input placeholder="20261042 - عبدالرحمن محمد" value="${d.studentRef||''}"></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء سند القبض وترحيله وتحديث حساب الطالب بنجاح'); document.getElementById('formModal')?.classList.remove('active'); if(typeof renderVouchers==='function') renderVouchers();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-paper-plane"></i> إصدار سند القبض</button>
        `;

    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormMissingFix) {
        _origOpenFormMissingFix(type, editData);
    }
};
"""

if '_origOpenFormMissingFix' not in js:
    js += missing_forms_wrapper
    print("  ✅ Added 9 missing openForm handlers")

# ================================================================
# 3. Add global delete/edit helper functions
# ================================================================
global_helpers = """

// ==================== GLOBAL EDIT/DELETE HELPERS ====================

// Universal delete confirmation with table refresh
function deleteRecord(tableName, recordId, recordLabel) {
    if (!confirm('هل أنت متأكد من حذف: ' + (recordLabel || recordId) + '؟')) return;
    
    // Remove from DB arrays
    const dbMap = {
        'activities': 'activitiesGridData',
        'buses': 'busesGridData', 
        'transport-routes': 'transportRoutesGridData',
        'transport-enrollment': 'transportEnrollmentGridData',
        'item-categories': 'itemCategoriesGridData',
        'inventory-items': 'inventoryItemsGridData',
        'supply-orders': 'supplyOrdersGridData',
        'suppliers': 'suppliersGridData',
        'inventory-reports': 'inventoryReportsGridData',
        'sms-send': 'smsSendGridData',
        'sms-templates': 'smsTemplatesGridData',
        'admin-messages': 'adminMessagesGridData',
        'shortcuts': 'shortcutsGridData',
        'faq': 'faqGridData',
        'dictionary': 'dictionaryGridData',
        'issue-orders': 'issueOrdersGridData',
        'leave-management': 'leaveManagementGridData',
        'performance-eval': 'performanceEvalsData',
    };
    
    const dbKey = dbMap[tableName];
    if (dbKey && DB[dbKey]) {
        DB[dbKey] = DB[dbKey].filter((item, idx) => idx !== recordId && item.id !== recordId);
    }
    
    // Re-render the table
    const renderMap = {
        'activities': renderActivitiesGrid,
        'buses': renderBusesGrid,
        'transport-routes': renderTransportRoutesGrid,
        'transport-enrollment': renderTransportEnrollmentGrid,
        'item-categories': renderItemCategoriesGrid,
        'inventory-items': renderInventoryItemsGrid,
        'supply-orders': renderSupplyOrdersGrid,
        'suppliers': renderSuppliersGrid,
        'inventory-reports': renderInventoryReportsGrid,
        'sms-send': renderSmsSendGrid,
        'sms-templates': renderSmsTemplatesGrid,
        'admin-messages': renderAdminMessagesGrid,
        'shortcuts': renderShortcutsGrid,
        'faq': renderFaqGrid,
        'dictionary': renderDictionaryGrid,
        'issue-orders': renderIssueOrdersGrid,
        'leave-management': renderLeaveManagementGrid,
        'performance-eval': renderPerformanceEvals,
    };
    
    if (renderMap[tableName]) {
        try { renderMap[tableName](); } catch(e) {}
    }
    
    toast('🗑️ تم حذف السجل بنجاح');
    addAudit('حذف', 'حذف سجل: ' + (recordLabel || recordId));
}
window.deleteRecord = deleteRecord;

// Universal search/filter function for any table
function filterTable(inputEl, tbodyId) {
    const query = (inputEl.value || '').toLowerCase();
    const tbody = document.getElementById(tbodyId);
    if (!tbody) return;
    const rows = tbody.querySelectorAll('tr');
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? '' : 'none';
    });
}
window.filterTable = filterTable;
"""

if 'function deleteRecord' not in js:
    js += global_helpers
    print("  ✅ Added global deleteRecord() and filterTable() helpers")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("\n  ✅ All missing functions and form handlers have been added to app.js!")

# ================================================================
# 4. Update HTML timestamp cache
# ================================================================
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')
with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print(f"  ✅ Updated HTML cache timestamps (v={ts})")
print("\n" + "=" * 80)
print("ALL FIXES APPLIED SUCCESSFULLY!")
print("=" * 80)
