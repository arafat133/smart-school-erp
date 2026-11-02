"""
Add form definitions for Activities & Transport openForm popups:
- activities
- transport-routes
- buses
- transport-enrollment
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

act_trans_forms_code = """
// ==================== ACTIVITIES & TRANSPORT FORM MODALS ====================
const _origOpenFormActTransModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'activities') {
        title.innerHTML = '<i class="fa-solid fa-medal"></i> إضافة / إعداد نشاط لاصفي جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود النشاط</label><input placeholder="ACT-2026-015" value="${d.id || ''}"></div>
            <div class="fg"><label>اسم النشاط المعلن</label><input placeholder="نادي الروبوت والذكاء الاصطناعي" value="${d.name || ''}"></div>
            <div class="fg"><label>تصنيف النشاط</label><select><option>نشاط علمي / تكنولوجي</option><option>نشاط رياضي</option><option>رحلة ميدانية</option><option>أندية ثقافة وفنون</option></select></div>
            <div class="fg"><label>المشرف المسؤول</label><input placeholder="م. حسام العنسي (قسم الحاسوب)" value="${d.supervisor || ''}"></div>
            <div class="fg"><label>السعة الاستيعابية (طالب)</label><input type="number" placeholder="25" value="${d.maxCap || ''}"></div>
            <div class="fg"><label>الفئة المستهدفة</label><input placeholder="الثاني والثالث الثانوي" value="${d.target || ''}"></div>
            <div class="fg"><label>النطاق الزمني (من - إلى)</label><input placeholder="2026-09-01 - 2026-11-15" value="${d.dates || ''}"></div>
            <div class="fg"><label>مكان التنفيذ</label><input placeholder="معمل الابتكار - المبنى الرئيسي" value="${d.venue || ''}"></div>
            <div class="fg"><label>رسوم الاشتراك ($)</label><input type="number" placeholder="50" value="${d.fee || ''}"></div>
            <div class="fg"><label>الميزانية المعتمدة ($)</label><input type="number" placeholder="500" value="${d.budget || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم إضافة وتخطيط النشاط بنجاح'); document.getElementById('formModal').classList.remove('active'); renderActivitiesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ بيانات النشاط</button>
        `;
    } else if (type === 'transport-routes') {
        title.innerHTML = '<i class="fa-solid fa-route"></i> إضافة / تعديل خط سير مواصلات';
        fields.innerHTML = `
            <div class="fg"><label>كود الخط</label><input placeholder="ROUTE-0103" value="${d.id || ''}"></div>
            <div class="fg"><label>اسم الخط والحي الرئيسي</label><input placeholder="خط حدة - الأصبحي - الحي السياسي" value="${d.name || ''}"></div>
            <div class="fg"><label>نقطة البداية والنهاية</label><input placeholder="انطلاق: شارع حدة -> وصول: المجمع" value="${d.startEnd || ''}"></div>
            <div class="fg"><label>عدد محطات التوقف</label><input type="number" placeholder="12" value="${d.stops || ''}"></div>
            <div class="fg"><label>الحافلة المخصصة</label><input placeholder="حافلة رقم (08) - سعة 30" value="${d.bus || ''}"></div>
            <div class="fg"><label>طاقم الحافلة (سائق/مشرفة)</label><input placeholder="السائق: علي العنسي" value="${d.crew || ''}"></div>
            <div class="fg"><label>رسوم الاشتراك السنوي ($)</label><input type="number" placeholder="200" value="${d.fee || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ خط السير بنجاح'); document.getElementById('formModal').classList.remove('active'); renderTransportRoutesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ خط السير</button>
        `;
    } else if (type === 'buses') {
        title.innerHTML = '<i class="fa-solid fa-bus-simple"></i> إضافة / تحديث حافلة مركبة';
        fields.innerHTML = `
            <div class="fg"><label>كود الحافلة</label><input placeholder="BUS-2026-008" value="${d.id || ''}"></div>
            <div class="fg"><label>رقم اللوحة المعدنية</label><input placeholder="12345-أ / نقل خاص" value="${d.plate || ''}"></div>
            <div class="fg"><label>الماركة والموديل</label><input placeholder="تويوتا كوستر - 2024" value="${d.model || ''}"></div>
            <div class="fg"><label>السعة الاستيعابية (مقعد)</label><input type="number" placeholder="30" value="${d.capacity || ''}"></div>
            <div class="fg"><label>خط السير المسند</label><input placeholder="خط حدة - الأصبحي (ROUTE-0103)" value="${d.route || ''}"></div>
            <div class="fg"><label>طاقم الحافلة المكلف</label><input placeholder="السائق: علي العنسي" value="${d.crew || ''}"></div>
            <div class="fg"><label>جهاز التتبع الـ GPS</label><input placeholder="Online - GP-883" value="${d.gpsStatus || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ بيانات الحافلة بنجاح'); document.getElementById('formModal').classList.remove('active'); renderBusesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ بيانات المركبة</button>
        `;
    } else if (type === 'transport-enrollment') {
        title.innerHTML = '<i class="fa-solid fa-user-check"></i> تسجيل اشتراك طالب في المواصلات';
        fields.innerHTML = `
            <div class="fg"><label>بيانات الطالب الكاملة</label><input placeholder="عبدالرحمن محمد علي - الثاني الثانوي (2026104)"></div>
            <div class="fg"><label>خط السير المحدد</label><select><option>خط حدة - الأصبحي (ROUTE-0103)</option></select></div>
            <div class="fg"><label>محطة التوقف والركوب الأقرب</label><input placeholder="محطة (5) - المقطري بجوار جولة حدة"></div>
            <div class="fg"><label>نوع الاشتراك</label><select><option>اتجاهين (ذهاب وإياب) - اشتراك سنوي</option><option>اتجاه واحد فقط (ذهاب)</option></select></div>
            <div class="fg"><label>رسوم الخدمة ($)</label><input type="number" placeholder="200"></div>
            <button class="btn-save" onclick="toast('✅ تم تسجيل اشتراك الطالب وتوليد الـ QR بنجاح'); document.getElementById('formModal').classList.remove('active'); renderTransportEnrollmentGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> إصدار الاشتراك وكرت الحافلة</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormActTransModals) {
        _origOpenFormActTransModals(type, editData);
    }
};
"""

if 'ACTIVITIES & TRANSPORT FORM MODALS' not in js:
    js += "\n" + act_trans_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Activities & Transport form modals in app.js successfully!")
