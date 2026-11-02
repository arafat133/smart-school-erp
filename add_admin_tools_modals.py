"""
Add form definitions for Admin Tools openForm popups:
- admin-messages
- shortcuts
- support-ticket
- dictionary
- personal-info
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

admin_tools_forms_code = """
// ==================== ADMIN TOOLS FORM MODALS ====================
const _origOpenFormAdminToolsModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'admin-messages') {
        title.innerHTML = '<i class="fa-solid fa-bullhorn"></i> صياغة تعميم / إعلان إداري جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود الإعلان</label><input placeholder="ANN-2026-0045" value="ANN-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>عنوان القرار أو التعميم</label><input placeholder="تعميم إداري: تغيير مواعيد الدوام الشتوي" value="${d.title || ''}"></div>
            <div class="fg"><label>تصنيف الإعلان</label><select><option>قرار إداري</option><option>تهنئة ومناسبة</option><option>إشعار أكاديمي</option><option>تنبيه مالي</option></select></div>
            <div class="fg"><label>الجمهور المستهدف</label><select><option>الكادر التعليمي (جميع المراحل)</option><option>كافة الموظفين والإداريين</option><option>جميع الطلاب وأولياء الأمور</option></select></div>
            <div class="fg"><label>درجة الأهمية / الإلحاح</label><select><option>عاجل وهام (Urgent)</option><option>عادي (Normal)</option></select></div>
            <div class="fg"><label>نص وتفاصيل التعميم الكامل</label><textarea placeholder="استناداً إلى قرار وزارة التربية والتعليم تقرر...">${d.body || ''}</textarea></div>
            <div class="fg"><label>الملف المرفق (PDF / صورة)</label><input placeholder="جدول_الدوام_الشتوي_2026.pdf"></div>
            <button class="btn-save" onclick="toast('📢 تم نشر وتثبيت التعميم الإداري بنجاح'); document.getElementById('formModal').classList.remove('active'); renderAdminMessagesGrid();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-bullhorn"></i> نشر التعميم الرسمي</button>
        `;
    } else if (type === 'shortcuts') {
        title.innerHTML = '<i class="fa-solid fa-keyboard"></i> إضافة / تثبيت اختصار شاشة جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود الاختصار</label><input placeholder="SC-USER-2026-08" value="${d.id || ''}"></div>
            <div class="fg"><label>عنوان الاختصار والشاشة</label><input placeholder="إرسال رسائل نصية (SMS)" value="${d.title || ''}"></div>
            <div class="fg"><label>الموديول التابع</label><input placeholder="نظام الرسائل والإشعارات" value="${d.module || ''}"></div>
            <div class="fg"><label>دالة / مسار التوجيه المباشر</label><input placeholder="goTo('pg-sms-send')" value="${d.route || ''}"></div>
            <div class="fg"><label>مفتاح اختصار اللوحة (Hotkey)</label><input placeholder="Ctrl + Shift + M" value="${d.hotkey || ''}"></div>
            <div class="fg"><label>التصنيف الشخصي</label><input placeholder="أدوات التواصل اليومية" value="${d.category || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم تثبيت الاختصار في لوحة الوصول السريع'); document.getElementById('formModal').classList.remove('active'); renderShortcutsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-thumbtack"></i> تثبيت في اللوحة</button>
        `;
    } else if (type === 'support-ticket') {
        title.innerHTML = '<i class="fa-solid fa-headset"></i> رفع تذكرة دعم فني واستفسار';
        fields.innerHTML = `
            <div class="fg"><label>الموديول / القسم المعني</label><select><option>نظام الكنترول والامتحانات</option><option>الشؤون المالية والحسابات</option><option>نظام الرسائل</option><option>المخازن والمشتريات</option></select></div>
            <div class="fg"><label>عنوان المشكلة أو الاستفسار</label><input placeholder="كيفية طباعة كشف التجميع النهائي (المشيت الرسمي)؟" value="${d.title || ''}"></div>
            <div class="fg"><label>درجة الأهمية والتأثير</label><select><option>عالية (High)</option><option>حرجة (Critical)</option><option>عادية (Normal)</option></select></div>
            <div class="fg"><label>تفاصيل ووصف المشكلة</label><textarea placeholder="يرجى توضيح الخطوات أو رسالة الخطأ الظاهرة بالتفصيل..."></textarea></div>
            <div class="fg"><label>لقطة الشاشة المرفقة (Screenshot)</label><input placeholder="screenshot_error_500.png"></div>
            <button class="btn-save" onclick="toast('🎫 تم إرسال تذكرة الدعم الفني وتكليف مهندس المتابعة'); document.getElementById('formModal').classList.remove('active'); renderFaqGrid();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-paper-plane"></i> إرسال تذكرة الدعم</button>
        `;
    } else if (type === 'dictionary') {
        title.innerHTML = '<i class="fa-solid fa-language"></i> إضافة / تعديل مصطلح في قاموس النظام';
        fields.innerHTML = `
            <div class="fg"><label>كود المصطلح (Key)</label><input placeholder="TERM_ACAD_GPA" value="${d.key || ''}"></div>
            <div class="fg"><label>المصطلح باللغة العربية</label><input placeholder="المعدل التراكمي" value="${d.arTerm || ''}"></div>
            <div class="fg"><label>الترجمة المعتمدة بالإنجليزي</label><input placeholder="Cumulative Grade Point Average (CGPA)" value="${d.enTerm || ''}"></div>
            <div class="fg"><label>التصنيف والقسم</label><input placeholder="الشؤون الأكاديمية والكنترول" value="${d.domain || ''}"></div>
            <div class="fg"><label>السياق وملاحظات الاستخدام</label><input placeholder="يستخدم في شهادات التخرج وكشوف الدرجات" value="${d.notes || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ واعتماد المصطلح في القاموس'); document.getElementById('formModal').classList.remove('active'); renderDictionaryGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ المصطلح</button>
        `;
    } else if (type === 'personal-info') {
        title.innerHTML = '<i class="fa-solid fa-user-pen"></i> تحديث بيانات الملف الشخصي والاتصال';
        fields.innerHTML = `
            <div class="fg"><label>الاسم الكامل المعتمد</label><input placeholder="أ. خالد محمود العنسي" value="${d.name || 'أ. خالد محمود العنسي'}"></div>
            <div class="fg"><label>البريد الإلكتروني الرسمي</label><input placeholder="k.alansi@school.edu.ye" value="${d.email || 'k.alansi@school.edu.ye'}"></div>
            <div class="fg"><label>رقم الجوال المعتمد</label><input placeholder="770000000" value="${d.phone || '770000000'}"></div>
            <div class="fg"><label>تفضيلات المظهر واللغة</label><select><option>اللغة العربية | المظهر الداكن (Dark Mode)</option><option>اللغة الإنجليزية | Dark Mode</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم تحديث بيانات الملف الشخصي بنجاح'); document.getElementById('formModal').classList.remove('active'); renderPersonalInfoGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ التحديثات</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormAdminToolsModals) {
        _origOpenFormAdminToolsModals(type, editData);
    }
};
"""

if 'ADMIN TOOLS FORM MODALS' not in js:
    js += "\n" + admin_tools_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Admin Tools form modals in app.js successfully!")
