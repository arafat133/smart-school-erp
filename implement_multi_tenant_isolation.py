"""
Implement Multi-Tenant Data Isolation for Schools in app.js and school.html
"""
import re, time

print("=" * 60)
print("Implementing Multi-Tenant School Data Isolation...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update DB initial data to include schoolId tags for all entities
multitenant_data_prep = """
// Global Current School Tenant Context
window.currentSchoolId = 1;

// Multi-Tenant School Filter Helper
function getSchoolData(key) {
    const list = DB[key] || [];
    // SaaS Admin sees all schools data
    if (window.me && (window.me.role === 'saas_admin' || window.me.roleName === 'مدير المنصة')) {
        return list;
    }
    const targetSchoolId = (window.me && window.me.schoolId) ? window.me.schoolId : (window.currentSchoolId || 1);
    return list.filter(item => !item.schoolId || item.schoolId == targetSchoolId);
}
window.getSchoolData = getSchoolData;

// Function to switch active school context dynamically
function switchActiveSchool(schoolId, schoolName) {
    window.currentSchoolId = parseInt(schoolId);
    if (window.me) window.me.schoolId = window.currentSchoolId;
    try { sessionStorage.setItem('currentSchoolId', window.currentSchoolId); } catch(e){}
    
    // Update Topbar badge
    const disp = document.getElementById('activeSchoolDisplay');
    if (disp) disp.textContent = schoolName || (window.currentSchoolId === 1 ? 'مدرسة المتفوقين الأهلية' : 'مدارس المستقبل الحديثة');
    
    toast(`🏫 تم التبديل إلى قاعدة بيانات (${schoolName || ('مدرسة ' + window.currentSchoolId)}) بنجاح`);
    
    // Re-render active page
    const activePage = document.querySelector('.page.active')?.id || 'pg-dashboard';
    if (typeof goTo === 'function') goTo(activePage);
}
window.switchActiveSchool = switchActiveSchool;
"""

if 'window.getSchoolData = getSchoolData' not in js:
    js = multitenant_data_prep + "\n" + js
    print("  ✓ Added Multi-Tenant School Context & Helper functions")

# 2. Tag existing demo datasets with schoolId: 1 or schoolId: 2
# Add schoolId to DB.students
js = js.replace("{id:1,name:\"أحمد محمود\",grade:\"الصف السابع\",section:\"أ\",gender:\"ذكر\",status:\"مستمر\"}",
                "{id:1,schoolId:1,name:\"أحمد محمود\",grade:\"الصف السابع\",section:\"أ\",gender:\"ذكر\",status:\"مستمر\"}")
js = js.replace("{id:2,name:\"سارة محمد\",grade:\"الصف الثامن\",section:\"ب\",gender:\"أنثى\",status:\"مستمر\"}",
                "{id:2,schoolId:1,name:\"سارة محمد\",grade:\"الصف الثامن\",section:\"ب\",gender:\"أنثى\",status:\"مستمر\"}")
js = js.replace("{id:3,name:\"علي حسين\",grade:\"الصف التاسع\",section:\"أ\",gender:\"ذكر\",status:\"مستمر\"}",
                "{id:3,schoolId:2,name:\"علي حسين (مدرسة المستقبل)\",grade:\"الصف التاسع\",section:\"أ\",gender:\"ذكر\",status:\"مستمر\"}")

# 3. Update handleLoginSubmit to capture selected schoolId and bind session to it
old_login_school_bind = """        // Authentication Success
        token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: userMatch.role,
            roleName: userMatch.roleName || userMatch.role,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };"""

new_login_school_bind = """        // Multi-Tenant School Binding
        const selectedSchoolId = parseInt(document.getElementById('schoolId')?.value || '1');
        const selectedSchoolName = document.getElementById('schoolId')?.options[document.getElementById('schoolId')?.selectedIndex]?.text || 'مدرسة المتفوقين الأهلية';
        window.currentSchoolId = selectedSchoolId;

        // Authentication Success
        token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: userMatch.role,
            roleName: userMatch.roleName || userMatch.role,
            schoolId: selectedSchoolId,
            schoolName: selectedSchoolName,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };

        // Update Topbar School Badge
        const disp = document.getElementById('activeSchoolDisplay');
        if (disp) disp.textContent = selectedSchoolName;"""

if old_login_school_bind in js:
    js = js.replace(old_login_school_bind, new_login_school_bind)
    print("  ✓ Updated handleLoginSubmit to bind session to selected schoolId!")

# 4. Replace raw DB queries in render functions to use getSchoolData(...)
js = js.replace("const list = DB.students || [];", "const list = getSchoolData('students');")
js = js.replace("const list = DB.exams || [];", "const list = getSchoolData('exams');")
js = js.replace("const list = DB.employees || [];", "const list = getSchoolData('employees');")
js = js.replace("const list = DB.vouchers || [];", "const list = getSchoolData('vouchers');")
js = js.replace("const list = DB.inventory_items || [];", "const list = getSchoolData('inventory_items');")
js = js.replace("const list = DB.receipts || [];", "const list = getSchoolData('receipts');")
js = js.replace("const list = DB.enrollment || [];", "const list = getSchoolData('enrollment');")

print("  ✓ Replaced raw collection queries with getSchoolData multi-tenant isolation!")

# 5. Automatically tag new entries with currentSchoolId in saveForm
old_save_tag = "const item = {"
new_save_tag = "const item = {\n                schoolId: window.currentSchoolId || 1,"
js = js.replace(old_save_tag, new_save_tag)

print("  ✓ Auto-tagging all new form entries with active schoolId")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with Multi-Tenant School Isolation Engine!")
