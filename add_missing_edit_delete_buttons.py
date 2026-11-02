"""
Python script to ensure Edit and Delete buttons are present in all active table render functions in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update renderExamScheduleGrid to include Edit & Delete buttons
old_exam = """<td><div class="act"><button class="btn-edit" onclick="openForm('exam_schedule', ${JSON.stringify(e).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button><button class="btn-delete" onclick="toast('تم حذف السجل 🗑️')"><i class="fa-solid fa-trash"></i></button></div></td>"""
new_exam = """<td><div class="act"><button class="btn-edit" onclick="openForm('exam_schedule', ${JSON.stringify(e).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('exam_schedule', '${e.id}', '${e.subject}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""

if old_exam in js:
    js = js.replace(old_exam, new_exam)
    print("  ✓ Updated renderExamScheduleGrid Edit & Delete buttons")

# 2. Update renderCustomReportsGrid
old_custom = """<td><span class="badge badge-success">جاهز للمعاينة</span></td>"""
new_custom = """<td><span class="badge badge-success">جاهز للمعاينة</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('custom-report', ${JSON.stringify(r).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('custom-reports', '${r.id}', '${r.title}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""
if old_custom in js and 'btn-delete' not in js[js.find('renderCustomReportsGrid'):js.find('renderCustomReportsGrid')+1000]:
    js = js.replace(old_custom, new_custom, 1)
    print("  ✓ Updated renderCustomReportsGrid Edit & Delete buttons")

# 3. Update renderShortcutsGrid
old_shortcut = """<td style="font-weight:800;color:#34d399;">${s.usage}</td>"""
new_shortcut = """<td style="font-weight:800;color:#34d399;">${s.usage}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('shortcuts', ${JSON.stringify(s).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('shortcuts', '${s.id}', '${s.title}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""
if old_shortcut in js and 'btn-delete' not in js[js.find('renderShortcutsGrid'):js.find('renderShortcutsGrid')+1000]:
    js = js.replace(old_shortcut, new_shortcut, 1)
    print("  ✓ Updated renderShortcutsGrid Edit & Delete buttons")

# 4. Update renderDiscontinuedList
old_discont = """<td style="font-size:0.8rem;">${d.reason}</td>"""
new_discont = """<td style="font-size:0.8rem;">${d.reason}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('discontinued', ${JSON.stringify(d).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('discontinued', '${d.id}', '${d.name}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""
if old_discont in js and 'btn-delete' not in js[js.find('renderDiscontinuedList'):js.find('renderDiscontinuedList')+1000]:
    js = js.replace(old_discont, new_discont, 1)
    print("  ✓ Updated renderDiscontinuedList Edit & Delete buttons")

# 5. Update renderEnrollmentList
old_enroll = """<td style="font-weight:700;color:#34d399;">${e.paid}</td>"""
new_enroll = """<td style="font-weight:700;color:#34d399;">${e.paid}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('enrollment', ${JSON.stringify(e).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('enrollment', '${e.id}', '${e.name}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""
if old_enroll in js and 'btn-delete' not in js[js.find('renderEnrollmentList'):js.find('renderEnrollmentList')+1000]:
    js = js.replace(old_enroll, new_enroll, 1)
    print("  ✓ Updated renderEnrollmentList Edit & Delete buttons")

# 6. Update renderHomeworkList
old_hw = """<td style="font-size:0.8rem;">${h.dueDate}</td>"""
new_hw = """<td style="font-size:0.8rem;">${h.dueDate}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('homework', ${JSON.stringify(h).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i> تعديل</button><button class="btn-delete" onclick="deleteRecord('homework', '${h.id}', '${h.subject}')"><i class="fa-solid fa-trash"></i> حذف</button></div></td>"""
if old_hw in js and 'btn-delete' not in js[js.find('renderHomeworkList'):js.find('renderHomeworkList')+1000]:
    js = js.replace(old_hw, new_hw, 1)
    print("  ✓ Updated renderHomeworkList Edit & Delete buttons")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Finished updating edit and delete buttons!")
