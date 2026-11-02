import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
core_js_path = os.path.join(BASE_DIR, "assets", "js", "core.js")

with open(core_js_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update checkAuthAndInitPortal in core.js
old_portal_logic = """            if (isParentPortal) {
                if (heading) heading.textContent = 'بوابة أولياء الأمور والطلاب | Parent Portal';
                if (subTitle) subTitle.textContent = 'متابعة المستوى الدراسي، الحضور، النتائج، والرسوم المدرسية';
                if (portalIcon) portalIcon.className = 'fa-solid fa-house-user';
                if (boxTitle) boxTitle.textContent = 'دخول ولي الأمر / الطالب';
                if (boxDesc) boxDesc.textContent = 'أدخل رقم الهاتف أو الهوية وكلمة السر المسجلة';
                if (boxIcon) boxIcon.className = 'fa-solid fa-users';
                if (uTypeSelect) uTypeSelect.value = 'parent';
                if (schoolField) schoolField.style.display = 'none';
                if (uNameLbl) uNameLbl.textContent = 'رقم هاتف ولي الأمر / الرقم الوطني';
                if (pWordLbl) pWordLbl.textContent = 'رقم قيد الطالب / كلمة المرور';
                if (uNameInput) { uNameInput.placeholder = 'أدخل هاتف ولي الأمر أو الرقم الوطني'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور'; pWordInput.value = ''; }
            } else if (isAdminPortal) {
                if (heading) heading.textContent = 'المركز السحابي الموحد | SaaS Command Center';
                if (subTitle) subTitle.textContent = 'بوابة مدير عام النظام لإدارة الخوادم، المدارس، والاشتراكات';
                if (portalIcon) portalIcon.className = 'fa-solid fa-server';
                if (boxTitle) boxTitle.textContent = 'دخول مدير النظام العام';
                if (boxDesc) boxDesc.textContent = 'صلاحية عليا للتحكم بالبنية التحتية والتراخيص';
                if (boxIcon) boxIcon.className = 'fa-solid fa-shield-halved';
                if (uTypeSelect) uTypeSelect.value = 'saas_admin';
                if (schoolField) schoolField.style.display = 'none';
                if (uNameLbl) uNameLbl.textContent = 'اسم حساب مدير النظام العام';
                if (uNameInput) { uNameInput.placeholder = 'أدخل اسم حساب مدير النظام'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور'; pWordInput.value = ''; }
            } else {
                if (heading) heading.textContent = 'نظام إدارة المدارس الشامل | ERP';
                if (subTitle) subTitle.textContent = 'المنظومة السحابية الموحدة لإدارة المدارس والطلاب والشؤون المالية';
                if (portalIcon) portalIcon.className = 'fa-solid fa-graduation-cap';
                if (boxTitle) boxTitle.textContent = 'تسجيل الدخول لبوابة المدرسة';
                if (boxDesc) boxDesc.textContent = 'لإدارة المدرسة، المعلمين، والمحاسبين';
                if (boxIcon) boxIcon.className = 'fa-solid fa-school';
                
                // Strictly remove SaaS Admin from School Portal userType dropdown
                if (uTypeSelect) {
                    const saasOpt = uTypeSelect.querySelector('option[value="saas_admin"]');
                    if (saasOpt) saasOpt.remove();
                    uTypeSelect.value = 'school_admin';
                }
                
                if (schoolField) schoolField.style.display = 'flex';
                
                // Dynamically populate all 30 schools into the school dropdown
                const schSelect = document.getElementById('schoolId');
                if (schSelect && window.DB && window.DB.schoolsList && window.DB.schoolsList.length > 0) {
                    const cur = schSelect.value;
                    schSelect.innerHTML = window.DB.schoolsList.map((s, idx) => {
                        const val = s.id || `SCH-${String(idx + 1).padStart(2, '0')}`;
                        return `<option value="${val}">🏫 ${s.name} (${s.city || (s.governorate + ' — ' + s.district)})</option>`;
                    }).join('');
                    if (cur) schSelect.value = cur;
                }
                
                if (uNameLbl) uNameLbl.textContent = 'اسم المستخدم / رقم الحساب';
                if (uNameInput) { uNameInput.placeholder = 'أدخل اسم المستخدم المعتمد'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور السرية'; pWordInput.value = ''; }
            }"""

new_portal_logic = """            if (isParentPortal) {
                if (heading) heading.textContent = 'بوابة أولياء الأمور والطلاب | Parent Portal';
                if (subTitle) subTitle.textContent = 'متابعة المستوى الدراسي، الحضور، النتائج، والرسوم المدرسية';
                if (portalIcon) portalIcon.className = 'fa-solid fa-house-user';
                if (boxTitle) boxTitle.textContent = 'دخول ولي الأمر / الطالب';
                if (boxDesc) boxDesc.textContent = 'أدخل رقم الهاتف أو الهوية وكلمة السر المسجلة';
                if (boxIcon) boxIcon.className = 'fa-solid fa-users';
                if (schoolField) schoolField.style.display = 'none';
                if (uTypeSelect) {
                    uTypeSelect.innerHTML = '<option value="parent">ولي أمر / طالب</option>';
                    uTypeSelect.value = 'parent';
                }
                if (uNameLbl) uNameLbl.textContent = 'رقم هاتف ولي الأمر / الرقم الوطني';
                if (pWordLbl) pWordLbl.textContent = 'رقم قيد الطالب / كلمة المرور';
                if (uNameInput) { uNameInput.placeholder = 'أدخل هاتف ولي الأمر أو الرقم الوطني'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور'; pWordInput.value = ''; }
            } else if (isAdminPortal) {
                if (heading) heading.textContent = 'المركز السحابي الموحد | SaaS Command Center';
                if (subTitle) subTitle.textContent = 'بوابة مدير عام النظام لإدارة الخوادم، المدارس، والاشتراكات';
                if (portalIcon) portalIcon.className = 'fa-solid fa-server';
                if (boxTitle) boxTitle.textContent = 'دخول مدير النظام العام';
                if (boxDesc) boxDesc.textContent = 'صلاحية عليا للتحكم بالبنية التحتية والتراخيص السحابية';
                if (boxIcon) boxIcon.className = 'fa-solid fa-shield-halved';
                
                // Hide school field completely on SaaS Admin Portal!
                if (schoolField) schoolField.style.display = 'none';
                
                // Provide dedicated SaaS admin roles only!
                if (uTypeSelect) {
                    uTypeSelect.innerHTML = `
                        <option value="saas_admin">مدير عام النظام السحابي (Super Admin / SaaS)</option>
                        <option value="db_admin">مهندس قواعد البيانات السحابية (DBA)</option>
                        <option value="security_officer">ضابط الأمن السيبراني (Cyber SOC)</option>
                    `;
                    uTypeSelect.value = 'saas_admin';
                }
                
                if (uNameLbl) uNameLbl.textContent = 'اسم حساب مدير النظام العام';
                if (pWordLbl) pWordLbl.textContent = 'كلمة المرور السرية';
                if (uNameInput) { uNameInput.placeholder = 'أدخل اسم الحساب (saas_admin أو root)'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور السرية'; pWordInput.value = ''; }
            } else {
                if (heading) heading.textContent = 'نظام إدارة المدارس الشامل | ERP';
                if (subTitle) subTitle.textContent = 'المنظومة السحابية الموحدة لإدارة المدارس والطلاب والشؤون المالية';
                if (portalIcon) portalIcon.className = 'fa-solid fa-graduation-cap';
                if (boxTitle) boxTitle.textContent = 'تسجيل الدخول لبوابة المدرسة';
                if (boxDesc) boxDesc.textContent = 'لإدارة المدرسة، المعلمين، والمحاسبين';
                if (boxIcon) boxIcon.className = 'fa-solid fa-school';
                
                // Show schoolField on School Portal!
                if (schoolField) schoolField.style.display = 'flex';
                
                // Provide School roles only!
                if (uTypeSelect) {
                    uTypeSelect.innerHTML = `
                        <option value="school_admin">مدير المدرسة (School Admin)</option>
                        <option value="teacher">معلم / عضو هيئة تدريس</option>
                        <option value="staff">محاسب / شؤون مالية وإدارية</option>
                        <option value="parent">ولي أمر / طالب</option>
                    `;
                    uTypeSelect.value = 'school_admin';
                }
                
                // Dynamically populate all 30 schools into the school dropdown
                const schSelect = document.getElementById('schoolId');
                if (schSelect && window.DB && window.DB.schoolsList && window.DB.schoolsList.length > 0) {
                    const cur = schSelect.value;
                    schSelect.innerHTML = window.DB.schoolsList.map((s, idx) => {
                        const val = s.id || `SCH-${String(idx + 1).padStart(2, '0')}`;
                        return `<option value="${val}">🏫 ${s.name} (${s.city || (s.governorate + ' — ' + s.district)})</option>`;
                    }).join('');
                    if (cur) schSelect.value = cur;
                }
                
                if (uNameLbl) uNameLbl.textContent = 'اسم المستخدم / رقم الحساب';
                if (pWordLbl) pWordLbl.textContent = 'كلمة المرور السرية';
                if (uNameInput) { uNameInput.placeholder = 'أدخل اسم المستخدم المعتمد'; uNameInput.value = ''; }
                if (pWordInput) { pWordInput.placeholder = 'أدخل كلمة المرور السرية'; pWordInput.value = ''; }
            }"""

if old_portal_logic in text:
    text = text.replace(old_portal_logic, new_portal_logic, 1)
    print("Updated checkAuthAndInitPortal logic in core.js successfully!")
else:
    print("Warning: old_portal_logic not matched directly!")

# 2. Fix handleLoginSubmit: selectedSchoolId ReferenceError and support all admin/school logins
old_login_block = """        // Determine appropriate role & display name
        const rawSchoolVal = document.getElementById('schoolId')?.value || 'SCH-01';
        const rawSchoolNum = parseInt(String(rawSchoolVal).replace(/\\D/g, '')) || 1;
        const selectedSchoolName = document.getElementById('schoolId')?.options[document.getElementById('schoolId')?.selectedIndex]?.text || 'مدرسة المتفوقين الأهلية';
        window.currentSchoolId = rawSchoolNum;
        window.currentSchoolCode = String(rawSchoolVal).startsWith('SCH-') ? rawSchoolVal : `SCH-${String(rawSchoolNum).padStart(2, '0')}`;

        const token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        const me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: userMatch.role || selectedRole,
            roleName: userMatch.roleName || userMatch.role || selectedRole,
            schoolId: selectedSchoolId,
            schoolName: selectedSchoolName,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };"""

new_login_block = """        // Determine appropriate role & display name based on active portal
        const path = window.location.pathname.toLowerCase();
        const isAdminPortal = path.includes('/admin') || path.includes('/saas');
        const isParentPortal = path.includes('/parent');

        const rawSchoolVal = document.getElementById('schoolId')?.value || 'SCH-01';
        const rawSchoolNum = parseInt(String(rawSchoolVal).replace(/\\D/g, '')) || 1;
        const selectedSchoolId = rawSchoolNum; // Ensure selectedSchoolId is defined!
        const selectedSchoolCode = String(rawSchoolVal).startsWith('SCH-') ? rawSchoolVal : `SCH-${String(rawSchoolNum).padStart(2, '0')}`;
        const selectedSchoolName = isAdminPortal ? 'المركز السحابي الموحد (كافة المدارس الـ 30)' : (document.getElementById('schoolId')?.options[document.getElementById('schoolId')?.selectedIndex]?.text || 'مدرسة المتفوقين الأهلية');

        window.currentSchoolId = selectedSchoolId;
        window.currentSchoolCode = selectedSchoolCode;

        // If on SaaS Admin portal, guarantee saas_admin role
        let finalRole = userMatch.role || selectedRole;
        if (isAdminPortal) {
            finalRole = (userMatch.role === 'db_admin' || userMatch.role === 'security_officer') ? userMatch.role : 'saas_admin';
        }

        const token = 'sec_token_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
        const me = {
            id: userMatch.id,
            username: userMatch.username,
            name: userMatch.name || userMatch.username,
            role: finalRole,
            roleName: userMatch.roleName || (finalRole === 'saas_admin' ? 'مدير عام النظام (Super Admin)' : finalRole),
            schoolId: isAdminPortal ? 'ALL' : selectedSchoolId,
            schoolCode: isAdminPortal ? 'ALL' : selectedSchoolCode,
            schoolName: selectedSchoolName,
            permissions: userMatch.permissions || { students: true, finance: true, accounting: true, control: true }
        };"""

if old_login_block in text:
    text = text.replace(old_login_block, new_login_block, 1)
    print("Fixed selectedSchoolId and admin login block in core.js successfully!")
else:
    print("Warning: old_login_block not matched directly!")

# Also ensure default accounts list includes saas_admin, root, admin, and all school principals
old_def_acc = """        // Standard system accounts
        const defaultAccounts = [
            { id: 'usr_1', username: 'admin', password: '123', name: 'أ. خالد العنسي (المدير العام)', role: 'school_admin', roleName: 'مدير المدرسة', status: 'نشط' },
            { id: 'usr_root', username: 'root', password: '123', name: 'م. حسام الدين (مدير النظام)', role: 'saas_admin', roleName: 'مدير عام النظام (Super Admin)', status: 'نشط' },
            { id: 'usr_2', username: 'teacher', password: '123', name: 'أ. عبد الرحمن باعباد', role: 'teacher', roleName: 'معلم', status: 'نشط' },
            { id: 'usr_3', username: 'staff', password: '123', name: 'أ. سارة المحاسبة', role: 'staff', roleName: 'محاسب وموظف', status: 'نشط' },
            { id: 'usr_4', username: 'parent', password: '123', name: 'عبد الله أحمد الأهدل (ولي أمر)', role: 'parent', roleName: 'ولي أمر', status: 'نشط' }
        ];"""

new_def_acc = """        // Standard system accounts
        const defaultAccounts = [
            { id: 'usr_1', username: 'admin', password: '123', name: 'أ. خالد العنسي (المدير العام)', role: 'school_admin', roleName: 'مدير المدرسة', status: 'نشط' },
            { id: 'usr_saas', username: 'saas_admin', password: '123', name: 'م. عبد الله الشامي (مدير النظام العام)', role: 'saas_admin', roleName: 'مدير عام النظام (Super Admin)', status: 'نشط' },
            { id: 'usr_root', username: 'root', password: '123', name: 'م. حسام الدين (مدير النظام)', role: 'saas_admin', roleName: 'مدير عام النظام (Super Admin)', status: 'نشط' },
            { id: 'usr_dba', username: 'db_admin', password: '123', name: 'م. طارق المعمري (مهندس قواعد البيانات)', role: 'db_admin', roleName: 'مهندس البنية وقواعد البيانات', status: 'نشط' },
            { id: 'usr_soc', username: 'soc_guardian', password: '123', name: 'الرائد صقر الحميري (Cyber Guardian AI)', role: 'security_officer', roleName: 'ضابط الأمن السيبراني', status: 'نشط' },
            { id: 'usr_2', username: 'teacher', password: '123', name: 'أ. عبد الرحمن باعباد', role: 'teacher', roleName: 'معلم', status: 'نشط' },
            { id: 'usr_3', username: 'staff', password: '123', name: 'أ. سارة المحاسبة', role: 'staff', roleName: 'محاسب وموظف', status: 'نشط' },
            { id: 'usr_4', username: 'parent', password: '123', name: 'عبد الله أحمد الأهدل (ولي أمر)', role: 'parent', roleName: 'ولي أمر', status: 'نشط' }
        ];"""

if old_def_acc in text:
    text = text.replace(old_def_acc, new_def_acc, 1)
    print("Enhanced default accounts in core.js!")

with open(core_js_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated core.js!")
