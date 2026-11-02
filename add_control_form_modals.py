"""
Add form definitions for Control & Exam openForm popups:
- exam_halls
- hall-distribution
- substitute
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

control_forms_code = """
// ==================== CONTROL & EXAM FORM MODALS ====================
const _origOpenFormCtrlModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'exam_halls') {
        title.innerHTML = '<i class="fa-solid fa-location-dot"></i> إضافة / تهيئة لجنة امتحانية وقاعة';
        fields.innerHTML = `
            <div class="fg"><label>رقم / اسم اللجنة</label><input placeholder="لجنة رقم (12) - القاعة الكبرى" value="${d.no || ''}"></div>
            <div class="fg"><label>المبنى والدور والقاعة</label><input placeholder="المبنى (أ) - الدور الثاني - قاعة A-201" value="${d.location || ''}"></div>
            <div class="fg"><label>السعة الاستيعابية (عدد المقاعد)</label><input type="number" placeholder="40" value="${d.capacity || ''}"></div>
            <div class="fg"><label>الصفوف والشعب المستهدفة</label><input placeholder="الثالث الثانوي (أ) + الثاني الثانوي (ب)" value="${d.target || ''}"></div>
            <div class="fg"><label>رئيس اللجنة (المشرف)</label><input placeholder="د. أحمد علي العنسي" value="${d.supervisor || ''}"></div>
            <div class="fg"><label>نمط التوزيع</label><select><option>تبادلي (خلط مستويين دراسيين)</option><option>تسلسلي أبجدي</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ القاعة واللجنة بنجاح'); document.getElementById('formModal').classList.remove('active'); renderExamHallsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ القاعة الامتحانية</button>
        `;
    } else if (type === 'hall-distribution') {
        title.innerHTML = '<i class="fa-solid fa-users-rectangle"></i> تكليف معلم / مراقب في لجنة امتحانية';
        fields.innerHTML = `
            <div class="fg"><label>اسم المراقب / الملاحظ</label><select><option>أ. خالد محمود العنسي (EMP-088)</option><option>أ. ياسر سعيد (EMP-102)</option></select></div>
            <div class="fg"><label>الدور الإشرافي</label><select><option>رئيس لجنة</option><option>ملاحظ رئيسي</option><option>ملاحظ مساعد</option></select></div>
            <div class="fg"><label>اسم / رقم اللجنة</label><select><option>لجنة رقم (08) - القاعة الكبرى</option><option>لجنة رقم (12) - قاعة A-201</option></select></div>
            <div class="fg"><label>المادة وتاريخ الامتحان</label><input placeholder="الكيمياء - السبت 2026-08-15"></div>
            <div class="fg"><label>الفترة / الوردية</label><select><option>الفترة الأولى (08:00 AM - 10:30 AM)</option><option>الفترة الثانية</option></select></div>
            <button class="btn-save" onclick="toast('✅ تم إسناد تكليف المراقبة'); document.getElementById('formModal').classList.remove('active'); renderHallDistributionGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> إرسال التكليف</button>
        `;
    } else if (type === 'substitute') {
        title.innerHTML = '<i class="fa-solid fa-user-pen"></i> تكليف معلم بديل (حصة احتياط)';
        fields.innerHTML = `
            <div class="fg"><label>المعلم الأصلي (الغائب)</label><input placeholder="أ. محمد عبدالله"></div>
            <div class="fg"><label>الصف والحصة والقاعة</label><input placeholder="الصف 10/أ - الحصة الثالثة (09:45 ص)"></div>
            <div class="fg"><label>المادة والدرس المقرر</label><input placeholder="رياضيات - حل تمارين المعاملات"></div>
            <div class="fg"><label>المعلم البديل المقترح</label><select><option>أ. سليم أحمد (مدرس رياضيات / متفرغ)</option><option>أ. حسام العنسي</option></select></div>
            <div class="fg"><label>ملاحظات وتغذية الحصة</label><textarea placeholder="تعليمات التغطية..."></textarea></div>
            <button class="btn-save" onclick="toast('✅ تم تكليف وإشعار المعلم البديل'); document.getElementById('formModal').classList.remove('active'); renderSubstituteGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> تأكيد التكليف البديل</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormCtrlModals) {
        _origOpenFormCtrlModals(type, editData);
    }
};
"""

if 'CONTROL & EXAM FORM MODALS' not in js:
    js += "\n" + control_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Control & Exam form modals in app.js successfully!")
