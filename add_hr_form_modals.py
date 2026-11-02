"""
Add form definitions for HR & Staff openForm popups:
- guarantors
- teacher-subjects
- emp-notices
- contract
- advance
- leave_request
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

hr_forms_code = """
// ==================== HR & STAFF FORM MODALS ====================
const _origOpenFormHrModals = window.openForm;
window.openForm = function(type, editData) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;
    let handled = true;
    const d = editData || {};

    if (type === 'guarantors') {
        title.innerHTML = '<i class="fa-solid fa-handshake"></i> بطاقة تعريف كفيل / ضامن جديد';
        fields.innerHTML = `
            <div class="fg"><label>كود الكفيل / الضامن</label><input id="f_g_id" placeholder="SPN-2026-014" value="${d.id || ''}"></div>
            <div class="fg"><label>اسم الكفيل الكامل (رباعياً)</label><input id="f_g_name" placeholder="علي محمد أحمد المقطري" value="${d.name || ''}"></div>
            <div class="fg"><label>نوع الكفالة / الضمانة</label>
                <select id="f_g_type">
                    <option value="ضمانة تجارية" ${d.type==='ضمانة تجارية'?'selected':''}>ضمانة تجارية</option>
                    <option value="كفالة حضورية غرمية" ${d.type==='كفالة حضورية غرمية'?'selected':''}>كفالة حضورية غرمية</option>
                    <option value="سند لأمر" ${d.type==='سند لأمر'?'selected':''}>سند لأمر</option>
                    <option value="عقد رهن" ${d.type==='عقد رهن'?'selected':''}>عقد رهن</option>
                </select>
            </div>
            <div class="fg"><label>رقم الهوية / السجل التجاري</label><input id="f_g_crNo" placeholder="1019928374" value="${d.crNo || ''}"></div>
            <div class="fg"><label>جهة العمل / المنشأة التجاري</label><input id="f_g_employer" placeholder="محلات الأمل للمواد الغذائية (مالك)" value="${d.employer || ''}"></div>
            <div class="fg"><label>عنوان وبيانات التواصل</label><input id="f_g_contact" placeholder="صنعاء - شارع حدة / +967 771234567" value="${d.contact || ''}"></div>
            <div class="fg"><label>اسم المكفول (طالب / موظف)</label><input id="f_g_guaranteedPerson" placeholder="أحمد علي محمد" value="${d.guaranteedPerson || ''}"></div>
            <div class="fg"><label>السقف المالي للكفالة ($)</label><input type="number" id="f_g_limit" placeholder="5000" value="${d.limit || ''}"></div>
            <div class="fg"><label>صلاحية الكفالة (من - إلى)</label><input id="f_g_validDates" placeholder="2026-09-01 - 2027-08-31" value="${d.validDates || ''}"></div>
            <div class="fg"><label>مستوى التوثيق</label><input id="f_g_verification" placeholder="موثق من المحكمة الابتدائية" value="${d.verification || 'موثق رسمياً'}"></div>
            <div class="fg"><label>حالة الضمانة</label>
                <select id="f_g_status">
                    <option value="سارية وموثقة">سارية وموثقة</option>
                    <option value="تحت المراجعة">تحت المراجعة</option>
                    <option value="منتهية">منتهية</option>
                </select>
            </div>
            <div class="fg"><label>إرفاق المستندات (PDF / صورة)</label><input type="file"></div>
            <button class="btn-save" onclick="toast('✅ تم حفظ بيانات الكفيل/الضامن بنجاح'); document.getElementById('formModal').classList.remove('active'); renderGuarantorsList();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ بطاقة الكفيل</button>
        `;
    } else if (type === 'teacher-subjects') {
        title.innerHTML = '<i class="fa-solid fa-chalkboard-user"></i> إسناد مادة ومعلم';
        fields.innerHTML = `
            <div class="fg"><label>المعلم / المحاضر</label><select id="f_ts_teacher"><option>أ. إبراهيم علي (EMP-088)</option><option>د. حسام العنسي (EMP-204)</option></select></div>
            <div class="fg"><label>المادة الدراسية</label><select id="f_ts_subject"><option>الكيمياء العامة</option><option>الرياضيات</option></select></div>
            <div class="fg"><label>الصف والشعبة</label><select id="f_ts_grade"><option>الصف الثالث الثانوي - شعبة (أ)</option><option>الصف الثاني الثانوي - شعبة (ب)</option></select></div>
            <div class="fg"><label>نوع التكليف</label><select><option>مدرس رئيسي</option><option>مدرس مساعد</option><option>معيد معمل</option></select></div>
            <div class="fg"><label>عدد الحصص الأسبوعية</label><input type="number" value="4"></div>
            <button class="btn-save" onclick="toast('✅ تم إسناد المادة للمعلم بنجاح'); document.getElementById('formModal').classList.remove('active'); renderTeacherSubjectsMatrix();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ إسناد المادة</button>
        `;
    } else if (type === 'emp-notices') {
        title.innerHTML = '<i class="fa-solid fa-paper-plane"></i> صياغة وإرسال تعميم / تنبيه موجه';
        fields.innerHTML = `
            <div class="fg"><label>عنوان التنبيه / التعميم</label><input placeholder="تذكير: رفع درجات المنتصف"></div>
            <div class="fg"><label>نص الإشعار التفصيلي</label><textarea placeholder="يرجى إدخال البيانات قبل يوم الخميس..."></textarea></div>
            <div class="fg"><label>تصنيف الإشعار</label><select><option>أكاديمي</option><option>إداري</option><option>مالي</option><option>انضباط</option></select></div>
            <div class="fg"><label>مستوى الأولوية</label><select><option>عادية</option><option>مهمة</option><option>طارئة جداً (Pop-up Alert)</option></select></div>
            <div class="fg"><label>الشريحة المستهدفة</label><select><option>جميع معلمي المواد العلمية</option><option>قسم الحاسوب</option><option>جميع الموظفين</option></select></div>
            <div class="fg"><label>قناة التوصيل</label><select><option>تطبيق الجوال (Push)</option><option>SMS</option><option>E-mail</option></select></div>
            <button class="btn-save" onclick="toast('🚀 تم إرسال التعميم للمستهدفين بنجاح'); document.getElementById('formModal').classList.remove('active'); renderEmpNoticesGrid();" style="width:100%;margin-top:12px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-paper-plane"></i> إرسال التنبيه الفوري</button>
        `;
    } else if (type === 'contract') {
        title.innerHTML = '<i class="fa-solid fa-file-contract"></i> إنشاء عقد عمل موظف جديد';
        fields.innerHTML = `
            <div class="fg"><label>رقم العقد</label><input placeholder="CNT-2026-043" value="CNT-2026-${String(Date.now()).slice(-3)}"></div>
            <div class="fg"><label>اسم الموظف</label><input placeholder="د. عبدالله صالح علي (EMP-112)"></div>
            <div class="fg"><label>المسمى الوظيفي</label><input placeholder="أستاذ حاسوب مشارك"></div>
            <div class="fg"><label>القسم / الإدارة</label><input placeholder="قسم الأمن السيبراني"></div>
            <div class="fg"><label>نوع العقد</label><select><option>محدد المدة (سنوي)</option><option>غير محدد المدة</option><option>دوام جزئي</option></select></div>
            <div class="fg"><label>تاريخ البداية والنهاية</label><input placeholder="2026-09-01 - 2027-08-31"></div>
            <div class="fg"><label>الراتب الأساسي ($)</label><input type="number" placeholder="1200"></div>
            <div class="fg"><label>إجمالي البدلات ($)</label><input type="number" placeholder="250"></div>
            <button class="btn-save" onclick="toast('✅ تم إنشاء وحفظ عقد الموظف بنجاح'); document.getElementById('formModal').classList.remove('active'); renderEmpContractsGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-floppy-disk"></i> حفظ عقد العمل</button>
        `;
    } else if (type === 'advance') {
        title.innerHTML = '<i class="fa-solid fa-hand-holding-dollar"></i> تقديم طلب سلفة / قرض موظف';
        fields.innerHTML = `
            <div class="fg"><label>اسم الموظف المتقدم</label><input placeholder="م. أحمد حسن العنسي (EMP-204)"></div>
            <div class="fg"><label>نوع السلفة</label><select><option>سلفة طارئة على الراتب</option><option>قرض شخصي طويل الأجل</option></select></div>
            <div class="fg"><label>المبلغ المطلوب ($)</label><input type="number" placeholder="1000"></div>
            <div class="fg"><label>عدد الأقساط الشهرية</label><input type="number" placeholder="10"></div>
            <div class="fg"><label>اسم الموظف الضامن / الكفيل</label><input placeholder="د. خالد عبدالله (EMP-108)"></div>
            <div class="fg"><label>سبب السلفة</label><textarea placeholder="شرح مختصر لسبب الطلب..."></textarea></div>
            <button class="btn-save" onclick="toast('✅ تم إرسال طلب السلفة للاعتماد'); document.getElementById('formModal').classList.remove('active'); renderEmpAdvancesGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> تقديم طلب السلفة</button>
        `;
    } else if (type === 'leave_request') {
        title.innerHTML = '<i class="fa-solid fa-calendar-xmark"></i> نموذج تقديم طلب إجازة';
        fields.innerHTML = `
            <div class="fg"><label>نوع الإجازة</label><select><option>إجازة سنوية</option><option>إجازة مرضية</option><option>إجازة اضطرارية</option></select></div>
            <div class="fg"><label>تاريخ البداية والنهاية</label><input placeholder="2026-08-10 إلى 2026-08-17"></div>
            <div class="fg"><label>الموظف البديل</label><input placeholder="م. حسام العنسي (EMP-204)"></div>
            <div class="fg"><label>المرفقات / التقرير الطبي</label><input type="file"></div>
            <div class="fg"><label>مبررات وسبب الإجازة</label><textarea placeholder="سبب تقديم الطلب..."></textarea></div>
            <button class="btn-save" onclick="toast('✅ تم تقديم طلب الإجازة للاعتماد'); document.getElementById('formModal').classList.remove('active'); renderLeaveManagementGrid();" style="width:100%;margin-top:12px;"><i class="fa-solid fa-paper-plane"></i> تقديم طلب الإجازة</button>
        `;
    } else {
        handled = false;
    }

    if (handled) {
        document.getElementById('formModal')?.classList.add('active');
    } else if (_origOpenFormHrModals) {
        _origOpenFormHrModals(type, editData);
    }
};
"""

if 'HR & STAFF FORM MODALS' not in js:
    js += "\n" + hr_forms_code

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended HR form modal popups in app.js successfully!")
