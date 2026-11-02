"""
Add form definitions for Warehouse openForm popups:
- item-categories
- inventory-items
- supply-orders
- suppliers
- stocktake
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

wh_forms_code = """
// ==================== WAREHOUSE & PURCHASING FORM MODALS ====================
const _origOpenFormWhModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'item-categories') {
        title.innerHTML = '<i class="fa-solid fa-boxes-stacked"></i> إضافة / تعديل فئة مخزونية';
        fields.innerHTML = `
            <div class="fg"><label>كود الفئة الشجري</label><input placeholder="CAT-IT-002" value="${d.code || ''}"></div>
            <div class="fg"><label>اسم الفئة المخزونية</label><input placeholder="أجهزة ومستلزمات المعامل الرقمية" value="${d.name || ''}"></div>
            <div class="fg"><label>الفئة الأب / الرئيسية</label><input placeholder="الأصول والتجهيزات التقنية" value="${d.parent || ''}"></div>
            <div class="fg"><label>وحدة القياس الافتراضية</label><input placeholder="قطعة / جهاز" value="${d.uom || ''}"></div>
            <div class="fg"><label>طريقة تقييم المخزون</label><select><option>الوارد أولاً يصرف أولاً (FIFO)</option><option>المتوسط الموزون</option></select></div>
            <div class="fg"><label>حد إعادة الطلب الافتراضي</label><input type="number" placeholder="10" value="${d.reorder || ''}"></div>
            <div class="fg"><label>طبيعة الأصناف</label><select><option>أصل ثابت (Asset)</option><option>صنف استهلاكي</option><option>خدمي</option></select></div>
            <div class="fg"><label>الحساب المحاسبي (GL)</label><input placeholder="مخزون الأجهزة الرقمية (120401)" value="${d.glAccount || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ بيانات الفئة المخزونية بنجاح'); document.getElementById('formModal').classList.remove('active'); renderItemCategoriesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ الفئة المخزونية</button>
        `;
    } else if (type === 'inventory-items') {
        title.innerHTML = '<i class="fa-solid fa-box"></i> إضافة / تعديل صنف ومنتج في المخزون';
        fields.innerHTML = `
            <div class="fg"><label>كود الصنف (SKU)</label><input placeholder="SKU-LAP-2026-001" value="${d.sku || ''}"></div>
            <div class="fg"><label>اسم الصنف والمنتج الدقيق</label><input placeholder="حاسوب محمول للمعامل الرقمية Dell XPS 15" value="${d.name || ''}"></div>
            <div class="fg"><label>الفئة الرئيسية والفرعية</label><input placeholder="الأجهزة الرقمية -> أجهزة محمول" value="${d.category || ''}"></div>
            <div class="fg"><label>الرمز الشريطي (Barcode)</label><input placeholder="6291100293812" value="${d.barcode || ''}"></div>
            <div class="fg"><label>حد إعادة الطلب (قطع)</label><input type="number" placeholder="5"></div>
            <div class="fg"><label>متوسط سعر التكلفة ($)</label><input type="number" placeholder="850" value="${d.avgCost || ''}"></div>
            <div class="fg"><label>سعر البيع / الصرف ($)</label><input type="number" placeholder="950" value="${d.sellRate || ''}"></div>
            <div class="fg"><label>موقع التخزين (المستودع والرف)</label><input placeholder="المخزن الرئيسي - الرف B-04" value="${d.location || ''}"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ الصنف وتوليد الباركود بنجاح'); document.getElementById('formModal').classList.remove('active'); renderInventoryItemsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ الصنف في المخزن</button>
        `;
    } else if (type === 'supply-orders') {
        title.innerHTML = '<i class="fa-solid fa-truck-ramp-box"></i> إنشاء إذن توريد واستلام بضائع (GRN)';
        fields.innerHTML = `
            <div class="fg"><label>رقم إذن التوريد (GRN)</label><input placeholder="GRN-2026-0415" value="GRN-2026-${String(Date.now()).slice(-4)}"></div>
            <div class="fg"><label>رقم أمر الشراء المرتبط (PO)</label><input placeholder="PO-2026-0089"></div>
            <div class="fg"><label>اسم المورد ورقم الفاتورة</label><input placeholder="شركة التقنية المتقدمة - فاتورة (8821)"></div>
            <div class="fg"><label>المستودع المستلم</label><select><option>المخزن الرئيسي - قسم الأجهزة الرقمية</option><option>المخزن الفرعي</option></select></div>
            <div class="fg"><label>حالة الفحص الفني والكميات</label><select><option>مقبول بالكامل</option><option>مقبول جزئياً</option><option>مرفوض</option></select></div>
            <div class="fg"><label>أمين المستودع المستلم</label><input placeholder="أ. إبراهيم العنسي"></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء وحفظ إذن التوريد GRN بنجاح'); document.getElementById('formModal').classList.remove('active'); renderSupplyOrdersGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> إرسال إذن التوريد للترحيل</button>
        `;
    } else if (type === 'suppliers') {
        title.innerHTML = '<i class="fa-solid fa-truck-field"></i> إضافة / توثيق مورد معتمد جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود المورد</label><input placeholder="SUP-2026-012" value="${d.code || ''}"></div>
            <div class="fg"><label>اسم الشركة / المورد الرسمية</label><input placeholder="شركة التقنية المتقدمة للمستلزمات" value="${d.name || ''}"></div>
            <div class="fg"><label>التصنيف والمجال</label><input placeholder="تجهيزات تقنية - أجهزة حاسوب والمعامل" value="${d.category || ''}"></div>
            <div class="fg"><label>السجل التجاري والضريبي</label><input placeholder="س.ت: 101088492 | ضريبي: 30048291" value="${d.taxCr || ''}"></div>
            <div class="fg"><label>مسؤول التواصل وهاتفه</label><input placeholder="م. أحمد السالمي (0501234567)" value="${d.contact || ''}"></div>
            <div class="fg"><label>شروط السداد وسقف الائتمان ($)</label><input placeholder="آجل - 30 يوماً / سقف: 50,000 $"></div>
            <button class="btn-save" onclick="toast('✅ تم توثيق واعتماد المورد بنجاح'); document.getElementById('formModal').classList.remove('active'); renderSuppliersGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ ملف المورد</button>
        `;
    } else if (type === 'stocktake') {
        title.innerHTML = '<div class="fa-solid fa-calculator"></div> إدخال محضر الجرد الفعلي للمخزون';
        fields.innerHTML = `
            <div class="fg"><label>رقم مأمورية الجرد</label><input placeholder="STK-2026-004"></div>
            <div class="fg"><label>المستودع المستهدف</label><select><option>المخزن الرئيسي - قاعة الأصول</option></select></div>
            <div class="fg"><label>الصنف والباركود</label><input placeholder="حاسوب محمول Dell (SKU-LAP-2026-001)"></div>
            <div class="fg"><label>الرصيد الفعلي المحصور</label><input type="number" placeholder="23"></div>
            <div class="fg"><label>أعضاء لجنة الجرد</label><input placeholder="أ. إبراهيم العنسي + م. خالد"></div>
            <button class="btn-save" onclick="toast('✅ تم تسجيل محضر الجرد وحساب التسويات آلياً'); document.getElementById('formModal').classList.remove('active'); renderInventoryReportsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-calculator"></i> إجراء تسوية الانحرافات</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormWhModals) {
        _origOpenFormWhModals(type, editData);
    }
};
"""

if 'WAREHOUSE & PURCHASING FORM MODALS' not in js:
    js += "\n" + wh_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Warehouse form modals in app.js successfully!")
