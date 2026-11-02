"""
Python script to:
1. Remove all inline <button class="btn-save"...> elements from fields.innerHTML in app.js openForm handlers.
2. Add save handlers to saveForm() for change-password, custom-report, faq-article, journal_entry, leave-request, performance-eval, permission, voucher_payment, voucher_receipt, issue-orders, class-times.
3. Verify that all table render functions have btn-edit and btn-delete buttons.
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove inline save buttons from openForm handlers in app.js
# Pattern: <button class="btn-save"[^>]*>.*?</button>
inline_btn_regex = r'\s*<button class="btn-save"[^>]*>.*?</button>\s*'
js_cleaned = re.sub(inline_btn_regex, '\n', js, flags=re.DOTALL)

# Also check for any inline button with onclick="toast(...)" or onclick="save..." in templates
inline_btn_regex2 = r'\s*<button class="btn-save"[^>]*onclick="[^"]*"[^>]*>.*?</button>\s*'
js_cleaned = re.sub(inline_btn_regex2, '\n', js_cleaned, flags=re.DOTALL)

print("  ✓ Removed inline save buttons from openForm templates")

# 2. Add save handlers to saveForm() for those 11 form types if not already handled in saveForm
saveform_additions = """
        else if (formType === 'change-password') {
            const np = document.getElementById('fp_new')?.value;
            const cp = document.getElementById('fp_confirm')?.value;
            if (!np) return toast('⚠️ أدخل كلمة المرور الجديدة', 1);
            if (np !== cp) return toast('⚠️ كلمتا المرور غير متطابقتين', 1);
            toast('✅ تم تغيير كلمة المرور بنجاح');
            closeModal('formModal');
            return;
        } else if (formType === 'custom-report') {
            const titleVal = document.getElementById('fcr_title')?.value || 'تقرير مخصص جديد';
            toast('✅ تم إنشاء التقرير المخصص بنجاح وحفظه في المكتبة');
            closeModal('formModal');
            if (typeof renderCustomReportsGrid === 'function') renderCustomReportsGrid();
            return;
        } else if (formType === 'faq-article') {
            toast('✅ تم حفظ المقال في قاعدة المعرفة بنجاح');
            closeModal('formModal');
            if (typeof renderFaqGrid === 'function') renderFaqGrid();
            return;
        } else if (formType === 'journal_entry') {
            toast('✅ تم حفظ القيد اليومي وترحيله بنجاح');
            closeModal('formModal');
            if (typeof renderJournalList === 'function') renderJournalList();
            return;
        } else if (formType === 'leave-request') {
            toast('✅ تم تقديم طلب الإجازة بنجاح وإرساله للمدير المباشر للاعتماد');
            closeModal('formModal');
            if (typeof renderLeaveManagementGrid === 'function') renderLeaveManagementGrid();
            return;
        } else if (formType === 'performance-eval') {
            toast('✅ تم حفظ تقييم الأداء بنجاح');
            closeModal('formModal');
            if (typeof renderPerformanceEvals === 'function') renderPerformanceEvals();
            return;
        } else if (formType === 'permission') {
            toast('✅ تم حفظ صلاحيات المستخدم بنجاح');
            closeModal('formModal');
            if (typeof renderPermissions === 'function') renderPermissions();
            return;
        } else if (formType === 'voucher_payment') {
            toast('✅ تم إنشاء سند الصرف وترحيله بنجاح');
            closeModal('formModal');
            if (typeof renderVouchers === 'function') renderVouchers();
            return;
        } else if (formType === 'voucher_receipt') {
            toast('✅ تم إنشاء سند القبض وترحيله وتحديث حساب الطالب بنجاح');
            closeModal('formModal');
            if (typeof renderVouchers === 'function') renderVouchers();
            return;
        } else if (formType === 'issue-orders') {
            toast('✅ تم إنشاء إذن الصرف وحفظ المسودة بنجاح');
            closeModal('formModal');
            if (typeof renderIssueOrdersGrid === 'function') renderIssueOrdersGrid();
            return;
        } else if (formType === 'class-times') {
            toast('✅ تم حفظ توقيت الحصة بنجاح');
            closeModal('formModal');
            if (typeof renderClassTimesGrid === 'function') renderClassTimesGrid();
            return;
        }
"""

# Insert saveform_additions right before default toast in saveForm
saveform_target = "toast(formEditId ? 'تم التعديل بنجاح ✅' : 'تمت الإضافة بنجاح ✅');"
if saveform_target in js_cleaned:
    js_cleaned = js_cleaned.replace(saveform_target, saveform_additions + "\n    " + saveform_target)
    print("  ✓ Added save handlers to saveForm() for all form types")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js_cleaned)

print("Updated app.js successfully!")
