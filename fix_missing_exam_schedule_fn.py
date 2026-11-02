"""
Fix missing renderExamScheduleGrid in app.js
"""
import re, time

print("=" * 60)
print("Fixing renderExamScheduleGrid ReferenceError in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add alias for renderExamScheduleGrid
alias_code = """
function renderExamScheduleGrid() {
    if (typeof renderExamSchedule === 'function') {
        renderExamSchedule();
    } else {
        const tb = document.getElementById('tbl-exam-schedule-grid') || document.getElementById('tbl-exam-schedule');
        if (!tb) return;
        const list = DB.exams || [];
        tb.innerHTML = list.map(e => `
            <tr>
                <td style="font-weight:700;color:#60a5fa;">EXM-SCH-2026-${e.id || '01'}</td>
                <td>العام الدراسي 2025/2026 - الفصل الثاني</td>
                <td>${e.grade || ''} ${e.section || ''}</td>
                <td style="font-weight:700;">${e.subject || ''}</td>
                <td>${e.date || ''}</td>
                <td>الفترة الأولى (صباحية)</td>
                <td>${e.time || '08:30 AM - 11:30 AM'}</td>
                <td>3 ساعات (180 دقيقة)</td>
                <td>${e.hall || 'القاعة الكبرى'}</td>
                <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">معتمد ورسمي</span></td>
                <td style="font-size:0.8rem;">يُسمح بالحاسبة العلمية فقط</td>
                <td>رئيس الكنترول</td>
                <td><div class="act"><button class="btn-edit" onclick="openForm('exam_schedule', ${JSON.stringify(e).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
            </tr>
        `).join('');
    }
}
window.renderExamScheduleGrid = renderExamScheduleGrid;
"""

if 'window.renderExamScheduleGrid' not in js:
    js += "\n" + alias_code.strip() + "\n"
    print("  ✓ Added renderExamScheduleGrid definition")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync timestamp in HTML
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

print(f"Fixed renderExamScheduleGrid successfully! Timestamp v={ts}")
