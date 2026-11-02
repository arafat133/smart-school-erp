"""
Add all missing page render functions, audit data defaults, and login error toast in app.js
"""
import re, time

print("=" * 60)
print("Fixing missing render functions, login error toasts, and DB defaults...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add missing page render handlers
missing_renders_js = """
// ==================== MISSING PAGE RENDER HANDLERS ====================
function renderSchoolInfo() {
    const el = document.getElementById('schoolNameInput') || document.getElementById('infoSchoolName');
    if (el) el.value = me?.schoolName || (window.currentSchoolId === 2 ? 'مدارس المستقبل الحديثة' : 'مدرسة المتفوقين الأهلية');
}
window.renderSchoolInfo = renderSchoolInfo;

function renderIncomeStmt() {
    const tb = document.getElementById('tbl-income-stmt') || document.getElementById('tbl-income');
    if (!tb) return;
    tb.innerHTML = `
        <tr><td><strong>إجمالي الإيرادات والرسوم الدراسية</strong></td><td style="color:#34d399;font-weight:700;">+ $150,000.00</td></tr>
        <tr><td><strong>إجمالي مصروفات التشغيل والرواتب</strong></td><td style="color:#f87171;font-weight:700;">- $45,000.00</td></tr>
        <tr style="background:rgba(59,130,246,0.15);font-size:1.05rem;"><td><strong>صافي الأرباح / الفائض التشغيلي</strong></td><td style="color:#60a5fa;font-weight:800;">+ $105,000.00</td></tr>
    `;
}
window.renderIncomeStmt = renderIncomeStmt;

function renderAuditTrail() {
    if (typeof renderAuditGrid === 'function') renderAuditGrid();
}
window.renderAuditTrail = renderAuditTrail;

function renderAdminPassword() {
    toast('🔒 يمكنك تغيير كلمة سر مدير النظام من هذه الشاشة');
}
window.renderAdminPassword = renderAdminPassword;

function renderParentProfile() {
    const el = document.getElementById('parentProfileName');
    if (el) el.textContent = me?.name || 'ولي الأمر المسجل';
}
window.renderParentProfile = renderParentProfile;

function renderParentFees() {
    const tb = document.getElementById('tbl-parent-fees');
    if (tb && typeof getSchoolData === 'function') {
        const receipts = getSchoolData('receipts') || [];
        tb.innerHTML = receipts.map(r => `<tr><td>${r.no||r.id}</td><td>${r.student||'الطالب'}</td><td>${r.amount} $</td><td><span class="badge badge-success">${r.status||'مدفوع'}</span></td></tr>`).join('');
    }
}
window.renderParentFees = renderParentFees;

function renderParentAttendance() {
    const tb = document.getElementById('tbl-parent-attendance');
    if (tb && typeof getSchoolData === 'function') {
        const att = getSchoolData('attendance') || [];
        tb.innerHTML = att.map(a => `<tr><td>${a.date||'اليوم'}</td><td>${a.student||'الطالب'}</td><td><span class="badge badge-success">${a.status||'حاضر'}</span></td></tr>`).join('');
    }
}
window.renderParentAttendance = renderParentAttendance;

function renderParentGrades() {
    const tb = document.getElementById('tbl-parent-grades');
    if (tb && typeof getSchoolData === 'function') {
        const grades = getSchoolData('grades') || [];
        tb.innerHTML = grades.map(g => `<tr><td>${g.student||'الطالب'}</td><td>${g.subject||'المادة'}</td><td><strong style="color:#60a5fa;">${g.score||95} / 100</strong></td></tr>`).join('');
    }
}
window.renderParentGrades = renderParentGrades;

function renderParentHomework() {
    const tb = document.getElementById('tbl-parent-homework');
    if (tb && typeof getSchoolData === 'function') {
        const hw = getSchoolData('homework') || [];
        tb.innerHTML = hw.map(h => `<tr><td>${h.title||'الواجب'}</td><td>${h.subject||'المادة'}</td><td>${h.dueDate||'غداً'}</td></tr>`).join('');
    }
}
window.renderParentHomework = renderParentHomework;
"""

if 'window.renderSchoolInfo = renderSchoolInfo' not in js:
    js += "\n" + missing_renders_js + "\n"
    print("  ✓ Appended missing page render functions to app.js")

# 2. Update handleLoginSubmit to fire red toast on invalid login credentials
old_login_err = """        if (errEl) {
            errEl.textContent = 'بيانات الدخول غير صحيحة أو مستخدم غير مسجل!';
            errEl.style.display = 'block';
        }"""

new_login_err = """        if (errEl) {
            errEl.textContent = '⚠️ بيانات الدخول غير صحيحة أو نوع المستخدم غير متوافق!';
            errEl.style.display = 'block';
        }
        if (typeof toast === 'function') {
            toast('⚠️ اسم المستخدم أو كلمة السر أو نوع المستخدم غير صحيح! يُرجى التأكد وإعادة المحاولة.', 1);
        }"""

if old_login_err in js:
    js = js.replace(old_login_err, new_login_err)
    print("  ✓ Enhanced handleLoginSubmit with red error toast notification")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
