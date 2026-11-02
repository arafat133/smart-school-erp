"""
Script to fix syntax error around line 2725 in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the corrupted block around academic-calendar in saveForm
corrupted_block = """        } else if (type === 'academic-calendar') {
        const d = editId ? (DB.academic_calendar||[]).find(x=>x.id==editId)||{} : {};
        title.innerHTML = `<i class="fa-solid fa-pen-to-square"></i> ${editId?'تعديل':'إضافة'} حدث تقويم`;
        h = `<div class="fg"><label>العنوان / الحدث</label><input id="f_cal_title" value="${d.f_cal_title||''}" oninput="validateTextOnly(this)"></div>
        <div class="fg"><label>من تاريخ</label><input type="date" id="f_cal_start" value="${d.f_cal_start||new Date().toLocaleDateString('en-CA')}"></div>
        <div class="fg"><label>إلى تاريخ</label><input type="date" id="f_cal_end" value="${d.f_cal_end||new Date().toLocaleDateString('en-CA')}"></div>
        <div class="fg"><label>اللون</label><input type="color" id="f_cal_color" value="${d.color||'#3b82f6'}" style="width:100%; height:40px; background:var(--surface); border:1px solid var(--border); padding:2px; border-radius:4px; cursor:pointer;"></div>
        <div class="fg"><label>الجمهور المستهدف</label><select id="f_cal_target"><option ${d.f_cal_target==='الكل'?'selected':''}>الكل</option><option ${d.f_cal_target==='الطلاب'?'selected':''}>الطلاب</option><option ${d.f_cal_target==='المعلمون'?'selected':''}>المعلمون</option><option ${d.f_cal_target==='أولياء الأمور'?'selected':''}>أولياء الأمور</option></select></div>`;
    }
    if (!val0) return toast('⚠️ يرجى إدخال البيانات المطلوبة', 1);
            const item = {
                id: formEditId || Date.now(),
                name: val0,
                f_cal_title: document.getElementById('f_cal_title')?.value||'',
                f_cal_start: document.getElementById('f_cal_start')?.value||'',
                f_cal_end: document.getElementById('f_cal_end')?.value||'',
                f_cal_target: document.getElementById('f_cal_target')?.value||''
            };
            if (!DB.academic_calendar) DB.academic_calendar = [];
            if (formEditId) {
                const idx = DB.academic_calendar.findIndex(x => x.id == formEditId);
                if (idx >= 0) DB.academic_calendar[idx] = item;
            } else {
                DB.academic_calendar.push(item);
            }
            closeModal('formModal');
            if (typeof renderAcademiccalendar === 'function') renderAcademiccalendar();
            toast('تم حفظ البيانات بنجاح ✅');
            return;"""

correct_block = """        } else if (type === 'academic-calendar') {
            const val0 = document.getElementById('f_cal_title')?.value;
            if (!val0) return toast('⚠️ يرجى إدخال عنوان الحدث', 1);
            const item = {
                id: (typeof formEditId !== 'undefined' && formEditId) ? formEditId : Date.now(),
                title: val0,
                f_cal_title: val0,
                f_cal_start: document.getElementById('f_cal_start')?.value || '',
                f_cal_end: document.getElementById('f_cal_end')?.value || '',
                color: document.getElementById('f_cal_color')?.value || '#3b82f6',
                f_cal_target: document.getElementById('f_cal_target')?.value || 'الكل',
                category: 'حدث تقويم',
                startDate: document.getElementById('f_cal_start')?.value || '',
                endDate: document.getElementById('f_cal_end')?.value || '',
                audience: document.getElementById('f_cal_target')?.value || 'الكل',
                location: 'المدرسة',
                publishStatus: 'مفعل'
            };
            if (!DB.academic_calendar) DB.academic_calendar = [];
            if (!DB.calendarEvents) DB.calendarEvents = [];
            if (typeof formEditId !== 'undefined' && formEditId) {
                const idx = DB.academic_calendar.findIndex(x => x.id == formEditId);
                if (idx >= 0) DB.academic_calendar[idx] = item;
                const idx2 = DB.calendarEvents.findIndex(x => x.id == formEditId);
                if (idx2 >= 0) DB.calendarEvents[idx2] = item;
            } else {
                DB.academic_calendar.push(item);
                DB.calendarEvents.push(item);
            }
            closeModal('formModal');
            if (typeof renderAcademicCalendar === 'function') renderAcademicCalendar();
            toast('تم حفظ البيانات بنجاح ✅');
            return;"""

if corrupted_block in js:
    js = js.replace(corrupted_block, correct_block)
    print("  ✓ Successfully replaced corrupted block!")
else:
    print("  ❌ Corrupted block not found exact match. Using regex replacement...")
    # Regex fallback replacement
    pattern = r"\}\s*else\s*if\s*\(\s*type\s*===\s*'academic-calendar'\s*\)\s*\{.*?return;\s*\}"
    js = re.sub(pattern, correct_block, js, flags=re.DOTALL)
    print("  ✓ Replaced via regex!")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js!")
