"""
Add form definitions for SMS & Reports openForm popups:
- sms-send
- sms-templates
- sms-settings
- custom-reports
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

sms_reports_forms_code = """
// ==================== SMS & REPORTS FORM MODALS ====================
const _origOpenFormSmsReportsModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'sms-send') {
        title.innerHTML = '<i class="fa-solid fa-paper-plane"></i> صياغة وإرسال دفعة رسائل نصية SMS';
        fields.innerHTML = `
            <div class="fg"><label>الشريحة والفئة المستهدفة</label><select><option>أولياء أمور طلاب الثالث الثانوي</option><option>الطلاب الغائبون اليوم آلياً</option><option>المشتركون في المواصلات</option><option>جميع المعلمين والكادر</option></select></div>
            <div class="fg"><label>نوع التنبيه</label><select><option>إشعار غياب يومي</option><option>نتائج الامتحانات</option><option>تذكير مالي بالأقساط</option><option>تعميم إداري عام</option></select></div>
            <div class="fg"><label>استدعاء قالب جاهز (اختياري)</label><select><option value="">-- اختر قالباً جاهزاً --</option><option>قالب غياب طالب (TMPL-ABS-01)</option><option>قالب تذكير بالأقساط المتبقية</option></select></div>
            <div class="fg"><label>نص الرسالة والرموز الديناميكية</label><textarea placeholder="ولي أمر الطالب {اسم_الطالب}، نود إحاطتكم بغياب ابنكم عن الحصة..."></textarea></div>
            <div class="fg"><label>حاسبة طول النص والتكلفة</label><input readonly value="135 حرفاً (يعادل 1 Segment - لغة عربية)"></div>
            <div class="fg"><label>موعد وتوقيت الإرسال</label><select><option>إرسال فوري الآن</option><option>جدولة في موعد محدد (تاريخ ووقت)</option></select></div>
            <button class="btn-save" onclick="toast('🚀 تم إرسال دفعة الرسائل النصية بنجاح عبر البوابة'); document.getElementById('formModal').classList.remove('active'); renderSmsSendGrid();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-paper-plane"></i> إطلاق دفعة الرسائل</button>
        `;
    } else if (type === 'sms-templates') {
        title.innerHTML = '<i class="fa-solid fa-file-code"></i> إضافة / صياغة قالب رسالة جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود القالب</label><input placeholder="TMPL-ABS-001" value="${d.code || ''}"></div>
            <div class="fg"><label>عنوان / اسم القالب</label><input placeholder="قالب إشعار غياب طالب عن الحصة" value="${d.name || ''}"></div>
            <div class="fg"><label>التصنيف والنظام التابع</label><select><option>الحضور والغياب</option><option>الكنترول والنتائج</option><option>الشؤون المالية</option><option>المواصلات والنقل</option></select></div>
            <div class="fg"><label>قناة الإرسال المخصصة</label><select><option>SMS / WhatsApp</option><option>البريد الإلكتروني</option><option>إشعار تطبيق الجوال (Push)</option></select></div>
            <div class="fg"><label>مُحدث الحدث التلقائي (System Trigger)</label><input placeholder="تسجيل غياب بدون عذر مقبول" value="${d.trigger || ''}"></div>
            <div class="fg"><label>نص القالب بالمتغيرات</label><textarea placeholder="ولي أمر الطالب {اسم_الطالب}، نحيطكم بغيابه اليوم الموافق {التاريخ} عن مادة {المادة}.">${d.body || ''}</textarea></div>
            <div class="fg"><label>المتغيرات المتاحة للاستدعاء</label><input readonly value="{اسم_الطالب}, {التاريخ}, {المادة}, {الصف}, {المبلغ_المستحق}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ القالب واعتماده في النظام'); document.getElementById('formModal').classList.remove('active'); renderSmsTemplatesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ قالب الرسالة</button>
        `;
    } else if (type === 'sms-settings') {
        title.innerHTML = '<i class="fa-solid fa-sliders"></i> إضافة / إعداد بوابة إرسال SMS جديدة';
        fields.innerHTML = `
            <div class="fg"><label>اسم مزود الخدمة</label><input placeholder="Yemen Mobile API / Twilio Gateway" value="${d.provider || ''}"></div>
            <div class="fg"><label>معرّف الراسل الرسمي (Sender ID)</label><input placeholder="AL-AMAL SCH" value="${d.senderId || ''}"></div>
            <div class="fg"><label>مفتاح الربط البرمجي (API Key / Token)</label><input placeholder="sk_live_992083810abf..." value="${d.apiKey || ''}"></div>
            <div class="fg"><label>حد التنبيه بانخفاض الرصيد (رسالة)</label><input type="number" placeholder="1000" value="${d.alertLimit || ''}"></div>
            <div class="fg"><label>فترة السماح بالإرسال اليومية</label><input placeholder="من 07:00 ص إلى 09:00 م" value="${d.window || ''}"></div>
            <div class="fg"><label>السقف اليومي الأقصى (رسالة)</label><input type="number" placeholder="2000" value="${d.dailyCap || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم ربط وحفظ إعدادات البوابة أونلاين'); document.getElementById('formModal').classList.remove('active'); renderSmsSettingsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ مفاتيح البوابة</button>
        `;
    } else if (type === 'custom-reports') {
        title.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> تصميم استعلام / تقرير مخصص جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود التقرير المخصص</label><input placeholder="RPT-CUST-2026-012" value="RPT-CUST-2026-${String(Date.now()).slice(-3)}"></div>
            <div class="fg"><label>عنوان التقرير المحدد</label><input placeholder="تقرير تحصيل رسوم المواصلات حسب الأحياء والصفوف"></div>
            <div class="fg"><label>مصدر البيانات الأساسي (Entities)</label><select><option>اشتراكات المواصلات + التحصيل المالي</option><option>الكنترول والنتائج + الحضور والغياب</option><option>المخازن والمشتريات + الموردين</option></select></div>
            <div class="fg"><label>الحقول والأعمدة المطلوب عرضها</label><input placeholder="اسم الطالب، الصف، الحي السكني، رقم الحافلة، المبلغ المدفوع"></div>
            <div class="fg"><label>الشروط والقيود المطبقة (Filters)</label><input placeholder="الحالة = نشط AND التاريخ >= 2026-01-01"></div>
            <div class="fg"><label>نمط العرض المرئي</label><select><option>جدول محوري (Pivot Table) + رسم بياني</option><option>جدول كشف تفصيلي</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم تصميم وحفظ التقرير المخصص بنجاح'); document.getElementById('formModal').classList.remove('active'); renderCustomReportsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-play"></i> حفظ وتشغيل التقرير</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormSmsReportsModals) {
        _origOpenFormSmsReportsModals(type, editData);
    }
};
"""

if 'SMS & REPORTS FORM MODALS' not in js:
    js += "\n" + sms_reports_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended SMS & Reports form modals in app.js successfully!")
