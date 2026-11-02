/**
 * ============================================================================
 * 02-AUTH-RBAC.JS - Authentication Engine, RBAC & Session Management
 * ============================================================================
 */
function handleLoginSubmit(e) {
    if (e) e.preventDefault();
    const btn = document.getElementById('loginBtn');
    let err = document.getElementById('loginError');
    const uTypeEl = document.getElementById('userType');
    const selectedRole = uTypeEl ? uTypeEl.value : 'school_admin';
    const loginBox = document.querySelector('.login-box');
    
    if (!err) {
        err = document.createElement('div');
        err.id = 'loginError';
        err.style.cssText = 'display:none;background:rgba(239,68,68,0.12);color:#ef4444;border:1px solid #f87171;padding:12px 16px;border-radius:8px;font-size:0.9rem;font-weight:700;text-align:center;line-height:1.5;margin-top:10px;';
        const form = document.getElementById('loginForm');
        if (form) form.insertBefore(err, form.lastElementChild);
    }

    if (btn) { 
        btn.disabled = true; 
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> جاري التدقيق والتحقق...'; 
    }
    if (err) {
        err.style.display = 'none';
        err.innerHTML = '';
    }

    try {
        const uInput = document.getElementById('username');
        const pInput = document.getElementById('password');
        let uName = (uInput ? uInput.value : '').trim();
        let pWord = (pInput ? pInput.value : '').trim();

        if (!uName) {
            if (uInput) uInput.focus();
            throw new Error('⚠️ يرجى إدخال اسم المستخدم أو رقم الحساب!');
        }

        if (!pWord) {
            if (pInput) pInput.focus();
            throw new Error('⚠️ يرجى إدخال كلمة السر المعتمدة!');
        }

        const allUsers = (window.DB && window.DB.users) ? window.DB.users : [
            { id: 'usr_1', username: 'admin', password: '123', name: 'أ. خالد العنسي (المدير العام)', role: 'school_admin', roleName: 'مدير المدرسة', status: 'نشط' },
            { id: 'usr_2', username: 'teacher', password: '123', name: 'أ. عبد الرحمن باعباد', role: 'teacher', roleName: 'معلم', status: 'نشط' },
            { id: 'usr_3', username: 'staff', password: '123', name: 'أ. سارة المحاسبة', role: 'staff', roleName: 'محاسب وموظف', status: 'نشط' },
            { id: 'usr_4', username: 'parent', password: '123', name: 'الشيخ باعباد (ولي أمر)', role: 'parent', roleName: 'ولي أمر', status: 'نشط' }
        ];

        const userMatch = allUsers.find(u => 
            (u.username === uName || String(u.username).toLowerCase() === uName.toLowerCase() || String(u.id) === uName || String(u.nationalId) === uName)
        );

        if (!userMatch) {
            if (uInput) uInput.focus();
            throw new Error(`❌ خطأ: اسم المستخدم أو الرقم (${uName}) غير مسجل في النظام! تحقق من صحة المدخلات.`);
        }

        if (userMatch.password !== pWord) {
            if (pInput) pInput.focus();
            if (typeof addAudit === 'function') addAudit('محاولة فاشلة', `محاولة دخول بكلمة سر خاطئة للمستخدم: ${uName}`);
            throw new Error('❌ خطأ: كلمة السر المدخلة غير صحيحة! يرجى إعادة التأكد من كلمة المرور.');
        }

        if (userMatch.status && userMatch.status !== 'نشط' && !userMatch.status.includes('🟢') && !userMatch.status.includes('نشط')) {
            throw new Error('⛔ تنبيه: هذا الحساب موقوف أو معطل حالياً من قِبل إدارة النظام!');
        }

        const roleMap = {
            'school_admin': ['school_admin', 'admin', 'مدير المدرسة', 'مدير النظام', 'Super Admin'],
            'saas_admin': ['saas_admin', 'admin', 'مدير النظام', 'Super Admin'],
            'teacher': ['teacher', 'معلم', 'مدرس'],
            'staff': ['staff', 'محاسب', 'موظف', 'مشرف الطابق', 'كادر'],
            'parent': ['parent', 'ولي أمر', 'طالب', 'student']
        };

        const allowedRoles = roleMap[selectedRole] || [selectedRole];
        const isRoleValid = allowedRoles.includes(userMatch.role) || allowedRoles.includes(userMatch.roleName);

        if (!isRoleValid) {
            const roleLabels = {
                'school_admin': 'مدير المدرسة',
                'teacher': 'معلم',
                'staff': 'موظف / مشرف / محاسب',
                'parent': 'ولي أمر / طالب'
            };
            const selectedLabel = roleLabels[selectedRole] || selectedRole;
            const actualLabel = userMatch.roleName || userMatch.role;
            throw new Error(`⚠️ خطأ في نوع المستخدم: الحساب (${uName}) مسجل كـ [${actualLabel}]، بينما تم اختيار نوع [${selectedLabel}]!`);
        }

        const selectedSchoolId = parseInt(document.getElementById('schoolId')?.value || '1');
        const selectedSchoolName = document.getElementById('schoolId')?.options[document.getElementById('schoolId')?.selectedIndex]?.text || 'مدرسة المتفوقين الأهلية';
        window.currentSchoolId = selectedSchoolId;

        const token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        const me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: userMatch.role,
            roleName: userMatch.roleName || userMatch.role,
            schoolId: selectedSchoolId,
            schoolName: selectedSchoolName,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };
        window.me = me;

        const disp = document.getElementById('activeSchoolDisplay');
        if (disp) disp.textContent = selectedSchoolName;

        try { 
            sessionStorage.setItem('sec_session_token', token); 
            sessionStorage.setItem('sec_user', JSON.stringify(me)); 
            localStorage.setItem('sec_user_session', JSON.stringify(me));
        } catch(e){}

        const lw = document.getElementById('loginWrapper');
        const al = document.getElementById('appLayout');
        if (lw) lw.style.display = 'none';
        if (al) al.style.display = 'flex';

        const uNameDisp = document.getElementById('userNameDisplay');
        if (uNameDisp) uNameDisp.textContent = me.name || me.username;

        if (typeof addAudit === 'function') addAudit('تسجيل دخول ناجح', `تم تسجيل الدخول بنجاح للمستخدم: ${me.name} (${me.roleName})`);
        if (typeof toast === 'function') toast(`👋 مرحباً بك ${me.name}! تم توثيق الدخول بنجاح`);

        if (typeof applyRBACPermissions === 'function') applyRBACPermissions(me);

        requestAnimationFrame(() => {
            setTimeout(() => {
                if (me.role === 'parent') {
                    if (typeof goTo === 'function') goTo('pg-parent-dashboard');
                } else if (me.role === 'saas_admin') {
                    if (typeof goTo === 'function') goTo('pg-saas-admin');
                } else {
                    if (typeof goTo === 'function') goTo('pg-dashboard');
                }
            }, 30);
        });

    } catch (errEx) {
        const errorMsg = errEx.message || 'خطأ أثناء التدقيق في بيانات تسجيل الدخول';
        
        if (err) { 
            err.innerHTML = `<i class="fa-solid fa-triangle-exclamation" style="margin-left:6px;"></i> ${errorMsg}`; 
            err.style.display = 'block'; 
        }

        if (typeof toast === 'function') {
            toast(errorMsg, 1);
        }

        if (loginBox) {
            loginBox.style.transition = 'transform 0.1s ease';
            loginBox.style.transform = 'translateX(-10px)';
            setTimeout(() => { loginBox.style.transform = 'translateX(10px)'; }, 100);
            setTimeout(() => { loginBox.style.transform = 'translateX(-6px)'; }, 200);
            setTimeout(() => { loginBox.style.transform = 'translateX(6px)'; }, 300);
            setTimeout(() => { loginBox.style.transform = 'translateX(0)'; }, 400);
        }

    } finally {
        if (btn) { 
            btn.disabled = false; 
            btn.innerHTML = '<i class="fa-solid fa-right-to-bracket"></i> تسجيل الدخول'; 
        }
    }
}
window.handleLoginSubmit = handleLoginSubmit;

function quickFillLogin(user, pass, role) {
    const uInput = document.getElementById('username');
    const pInput = document.getElementById('password');
    const rSelect = document.getElementById('userType');
    if (uInput) uInput.value = user;
    if (pInput) pInput.value = pass;
    if (rSelect) rSelect.value = role;
    toast(`🔑 تم تعبئة البيانات التلقائية للحساب (${user})`);
}
window.quickFillLogin = quickFillLogin;

function applyRBACPermissions(user) {
    if (!user) return;
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;

    if (user.role === 'parent') {
        const links = sidebar.querySelectorAll('.nav-links > li');
        links.forEach(li => {
            const hasParent = li.querySelector('a[onclick*="pg-parent"]') || li.querySelector('a[onclick*="pg-student-"]');
            if (!hasParent) li.style.display = 'none';
        });
    }
}
window.applyRBACPermissions = applyRBACPermissions;

function togglePasswordVisibility() {
    const passInput = document.getElementById('password');
    const icon = document.getElementById('togglePassword');
    if (!passInput || !icon) return;
    if (passInput.type === 'password') {
        passInput.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        passInput.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}
window.togglePasswordVisibility = togglePasswordVisibility;

function logout() {
    try {
        sessionStorage.clear();
        localStorage.removeItem('sec_user_session');
    } catch(e){}
    const lw = document.getElementById('loginWrapper');
    const al = document.getElementById('appLayout');
    if (lw) lw.style.display = 'flex';
    if (al) al.style.display = 'none';
    toast('👋 تم تسجيل الخروج بأمان');
}
window.logout = logout;
