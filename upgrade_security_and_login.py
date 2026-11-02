"""
Upgrade login authentication and system security in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Define comprehensive default DB.users array if not present or expand it
updated_db_users = """users: [
        { id: 1, username: "admin", password: "admin123", name: "مدير النظام", role: "school_admin", roleName: "مدير النظام", status: "نشط", permissions: { students: true, finance: true, accounting: true, control: true, hr: true, settings: true, add: true, edit: true, del: true } },
        { id: 2, username: "saas", password: "saas123", name: "مدير منصة SaaS", role: "saas_admin", roleName: "مدير المنصة", status: "نشط", permissions: { saas: true, schools: true, db: true, settings: true } },
        { id: 3, username: "teacher1", password: "teacher123", name: "أ. خالد محمود العنسي", role: "teacher", roleName: "معلم", status: "نشط", permissions: { students: true, attendance: true, student_tree: true, grading: true, results: true, homework: true, schedule: true, exam_schedule: true, add: true, edit: true, del: false } },
        { id: 4, username: "parent1", password: "parent123", name: "محمد علي السالمي", role: "parent", roleName: "ولي أمر", status: "نشط", studentId: 1, permissions: { parent_grades: true, parent_fees: true, parent_attendance: true } },
        { id: 5, username: "1234567890", password: "101", name: "محمد علي السالمي", role: "parent", roleName: "ولي أمر", status: "نشط", studentId: 1, permissions: { parent_grades: true, parent_fees: true, parent_attendance: true } },
        { id: 6, username: "accountant1", password: "acc123", name: "أ. إبراهيم العنسي", role: "accountant", roleName: "محاسب مالي", status: "نشط", permissions: { finance: true, accounting: true, vouchers: true, journal: true, add: true, edit: true, del: false } }
    ],"""

# Replace users definition in DB
js = re.sub(r'users:\s*\[.*?\]\s*,', updated_db_users, js, flags=re.DOTALL)

# Rebuild handleLoginSubmit and quickFillLogin with STRICT SECURITY
strict_login_js = """
// ==================== SECURE AUTHENTICATION ENGINE ====================
function handleLoginSubmit(e) {
    if (e) e.preventDefault();
    const btn = document.getElementById('loginBtn');
    const err = document.getElementById('loginError');
    const uTypeEl = document.getElementById('userType');
    const selectedRole = uTypeEl ? uTypeEl.value : 'school_admin';
    
    if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> جاري التدقيق والتحقق...'; }
    if (err) err.style.display = 'none';

    try {
        let uName = (document.getElementById('username')?.value || '').trim();
        let pWord = (document.getElementById('password')?.value || '').trim();

        if (!uName || !pWord) {
            throw new Error('⚠️ يرجى إدخال اسم المستخدم وكلمة السر المعتمدة');
        }

        // Search user in DB.users
        const allUsers = DB.users || [];
        const userMatch = allUsers.find(u => 
            (u.username === uName || String(u.username) === uName)
        );

        if (!userMatch) {
            throw new Error('⚠️ اسم المستخدم غير مقتيد بالنظام! تحقق من اسم المستخدم');
        }

        // Verify password
        if (userMatch.password !== pWord) {
            addAudit('محاولة فاشلة', `محاولة دخول فاشلة للمستخدم: ${uName}`);
            throw new Error('⚠️ كلمة السر غير صحيحة! يرجى إعادة المحاولة');
        }

        // Verify active status
        if (userMatch.status && userMatch.status !== 'نشط') {
            throw new Error('⚠️ هذا الحساب معطل أو موقوف حالياً من قبل إدارة النظام');
        }

        // Verify Role match
        const roleMap = {
            'school_admin': ['school_admin', 'admin', 'مدير النظام'],
            'saas_admin': ['saas_admin', 'admin', 'مدير النظام'],
            'teacher': ['teacher', 'معلم'],
            'parent': ['parent', 'ولي أمر']
        };

        const allowedRoles = roleMap[selectedRole] || [selectedRole];
        const isRoleValid = allowedRoles.includes(userMatch.role) || allowedRoles.includes(userMatch.roleName);

        if (!isRoleValid) {
            throw new Error(`⚠️ نوع المستخدم المحدد (${selectedRole}) لا يتوافق مع صلاحيات هذا الحساب (${userMatch.roleName || userMatch.role})`);
        }

        // Authentication Success
        token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: userMatch.role,
            roleName: userMatch.roleName || userMatch.role,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };

        // Store session in sessionStorage securely
        try { sessionStorage.setItem('sec_session_token', token); sessionStorage.setItem('sec_user', JSON.stringify(me)); } catch(e){}

        // UI Transition
        const lw = document.getElementById('loginWrapper');
        const al = document.getElementById('appLayout');
        if (lw) lw.style.display = 'none';
        if (al) al.style.display = 'flex';

        const uNameDisp = document.getElementById('userNameDisplay');
        if (uNameDisp) uNameDisp.textContent = me.name || me.username;

        addAudit('تسجيل دخول ناجح', `تم تسجيل الدخول بنجاح للمستخدم: ${me.name} (${me.roleName})`);
        toast(`👋 مرحباً بك ${me.name}! تم توثيق الدخول بنجاح`);

        // Apply RBAC permissions to navigation sidebar
        applyRBACPermissions(me);

        // Transition to default role dashboard
        requestAnimationFrame(() => {
            setTimeout(() => {
                if (me.role === 'parent') {
                    goTo('pg-parent-dashboard');
                } else if (me.role === 'saas_admin') {
                    goTo('pg-saas-admin');
                } else {
                    goTo('pg-dashboard');
                }
            }, 30);
        });

    } catch (errEx) {
        if (err) { 
            err.textContent = errEx.message || 'خطأ أثناء التدقيق في بيانات تسجيل الدخول'; 
            err.style.display = 'block'; 
        }
    } finally {
        if (btn) { btn.disabled = false; btn.innerHTML = '<i class="fa-solid fa-right-to-bracket"></i> تسجيل الدخول'; }
    }
}
window.handleLoginSubmit = handleLoginSubmit;

// Quick fill credentials for demo testing
function quickFillLogin(user, pass, role) {
    const uInput = document.getElementById('username');
    const pInput = document.getElementById('password');
    const rSelect = document.getElementById('userType');
    if (uInput) uInput.value = user;
    if (pInput) pInput.value = pass;
    if (rSelect) rSelect.value = role;
    toast(`🔑 تم تعبئة البيانات التلقائية للم الحساب (${user})`);
}
window.quickFillLogin = quickFillLogin;

// Apply Role-Based Access Control (RBAC) to system sidebar
function applyRBACPermissions(user) {
    const sidebar = document.getElementById('sidebarNav');
    if (!sidebar) return;
    
    // Show all for full admin
    if (user.role === 'school_admin' || user.role === 'admin' || user.roleName === 'مدير النظام') {
        sidebar.querySelectorAll('.nav-section, .nav-item').forEach(el => el.style.display = '');
        return;
    }

    // Role-based visibility rules
    if (user.role === 'teacher') {
        sidebar.querySelectorAll('.nav-section').forEach((sec, idx) => {
            // Keep academic, students, control, activities sections visible
            if ([2, 3, 5, 6].includes(idx)) sec.style.display = '';
            else sec.style.display = 'none';
        });
    } else if (user.role === 'parent') {
        if (document.getElementById('sidebarNav')) document.getElementById('sidebarNav').style.display = 'none';
        if (document.getElementById('parentNav')) document.getElementById('parentNav').style.display = 'block';
    }
}
window.applyRBACPermissions = applyRBACPermissions;
"""

# Find handleLoginSubmit pattern in app.js and replace it with strict_login_js
pattern_login = r'function handleLoginSubmit\s*\(e\)\s*\{.*?\}\s*window\.handleLoginSubmit\s*=\s*handleLoginSubmit;'
if re.search(pattern_login, js, re.DOTALL):
    js = re.sub(pattern_login, strict_login_js, js, flags=re.DOTALL)
    print("  ✓ Replaced handleLoginSubmit with strict authentication engine!")
else:
    print("  ⚠️ Using regex fallback for handleLoginSubmit replacement...")
    js += "\n" + strict_login_js + "\n"

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with strict security & authentication!")
