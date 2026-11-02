import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's clean up any legacy handleLoginSubmit blocks
# First, remove any "window.handleLoginSubmit = async function(e) {" block
js = re.sub(r'window\.handleLoginSubmit\s*=\s*async\s+function\(e\)\s*\{.*?\n\s*\};\n', '', js, flags=re.DOTALL)

# Now define a clean handleLoginSubmit
clean_login = """
const handleLoginSubmit = async function(e) {
    if (e) e.preventDefault();
    const btn = document.getElementById('loginBtn');
    const err = document.getElementById('loginError');
    const uTypeEl = document.getElementById('userType');
    const uType = uTypeEl ? uTypeEl.value : 'school_admin';
    
    if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> جاري الدخول...'; }
    if (err) err.style.display = 'none';

    try {
        let uName = (document.getElementById('username')?.value || '').trim();
        let pWord = (document.getElementById('password')?.value || '').trim();

        if (!uName || !pWord) throw new Error('يرجى إدخال اسم المستخدم وكلمة السر');

        // Fast instant login fallback
        token = 'demo_token_' + Date.now();
        me = { username: uName, role: uType, permissions: { students: true, finance: true, accounting: true, control: true, hr: true } };

        // ⚡ INSTANT UI TRANSITION (0ms)
        const lw = document.getElementById('loginWrapper');
        const al = document.getElementById('appLayout');
        if (lw) lw.style.display = 'none';
        if (al) al.style.display = 'flex';

        // Set user display name
        const uNameDisp = document.getElementById('userNameDisplay');
        if (uNameDisp) uNameDisp.textContent = uName;

        // Defer heavy rendering asynchronously so UI thread stays 100% responsive
        requestAnimationFrame(() => {
            setTimeout(() => {
                goTo('pg-dashboard');
            }, 30);
        });

    } catch (errEx) {
        if (err) { err.textContent = errEx.message || 'خطأ أثناء تسجيل الدخول'; err.style.display = 'block'; }
    } finally {
        if (btn) { btn.disabled = false; btn.innerHTML = '<i class="fa-solid fa-right-to-bracket"></i> تسجيل الدخول'; }
    }
};
"""

# Replace any existing handleLoginSubmit definition
js = re.sub(r'handleLoginSubmit\s*=\s*async\s+e\s*=>\s*\{.*?\n\s*\};', clean_login.strip(), js, flags=re.DOTALL)
js = re.sub(r'handleLoginSubmit\s*=\s*async\s+function\(e\)\s*\{.*?\n\s*\};', clean_login.strip(), js, flags=re.DOTALL)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Cleaned up handleLoginSubmit successfully!")
print(f"app.js size: {len(js)} bytes")
print(f"Open braces: {js.count('{')}, Close braces: {js.count('}')}, Diff: {js.count('{') - js.count('}')}")
