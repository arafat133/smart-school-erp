import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Update templates/partials/_login.html
login_html_path = os.path.join(BASE_DIR, "templates", "partials", "_login.html")
with open(login_html_path, "r", encoding="utf-8") as f:
    login_html = f.read()

# Make onchange intelligent and portal-aware
old_onchange = """                        onchange="
                        const isParent = this.value === 'parent';
                        
                        const sf = document.getElementById('schoolField');
                        if (sf) sf.style.display = isParent ? 'none' : 'flex';
                        const uLbl = document.getElementById('usernameLbl');
                        if (uLbl) uLbl.textContent = isParent ? 'الرقم الوطني / هاتف ولي الأمر' : 'اسم المستخدم / رقم الحساب';
                        const pLbl = document.getElementById('passwordLbl');
                        if (pLbl) pLbl.textContent = isParent ? 'رقم قيد الطالب / كلمة السر' : 'كلمة المرور السرية';
                    ">"""

new_onchange = """                        onchange="
                        const pth = window.location.pathname.toLowerCase();
                        const isAdm = pth.includes('/admin') || pth.includes('/saas');
                        const isPar = pth.includes('/parent') || this.value === 'parent';
                        const sf = document.getElementById('schoolField');
                        if (sf) sf.style.display = (isAdm || isPar) ? 'none' : 'flex';
                        const uLbl = document.getElementById('usernameLbl');
                        if (uLbl) uLbl.textContent = isPar ? 'الرقم الوطني / هاتف ولي الأمر' : (isAdm ? 'اسم حساب مدير النظام العام' : 'اسم المستخدم / رقم الحساب');
                        const pLbl = document.getElementById('passwordLbl');
                        if (pLbl) pLbl.textContent = isPar ? 'رقم قيد الطالب / كلمة السر' : 'كلمة المرور السرية';
                    ">"""

if old_onchange in login_html:
    login_html = login_html.replace(old_onchange, new_onchange, 1)
    print("Updated onchange in _login.html successfully!")
else:
    print("Warning: old_onchange not matched exactly, replacing select userType tag")
    login_html = login_html.replace('onchange="\n                        const isParent = this.value === \'parent\';', 'onchange="\n                        const pth = window.location.pathname.toLowerCase();\n                        const isAdm = pth.includes(\'/admin\') || pth.includes(\'/saas\');\n                        const isPar = pth.includes(\'/parent\') || this.value === \'parent\';')
    login_html = login_html.replace("if (sf) sf.style.display = isParent ? 'none' : 'flex';", "if (sf) sf.style.display = (isAdm || isPar) ? 'none' : 'flex';")

with open(login_html_path, "w", encoding="utf-8") as f:
    f.write(login_html)

print("Saved updated _login.html!")
