"""
Fix handleLoginSubmit definition hoisting issue in app.js
"""
import re, time

print("=" * 60)
print("Fixing handleLoginSubmit hoisting in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Define function handleLoginSubmit as standard hoisted function AT THE TOP or before event listeners
hoisted_login_function = """
// Standard hoisted login handler
function handleLoginSubmit(e) {
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

        // Instant login session setup
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

        // Defer heavy dashboard rendering asynchronously
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
}
window.handleLoginSubmit = handleLoginSubmit;
"""

# Remove any existing const handleLoginSubmit or window.handleLoginSubmit
js = re.sub(r'const\s+handleLoginSubmit\s*=\s*async\s+function\(e\)\s*\{.*?\n\s*\};', '', js, flags=re.DOTALL)
js = re.sub(r'const\s+handleLoginSubmit\s*=\s*function\(e\)\s*\{.*?\n\s*\};', '', js, flags=re.DOTALL)
js = re.sub(r'function\s+handleLoginSubmit\(e\)\s*\{.*?\n\s*\}', '', js, flags=re.DOTALL)

# Insert hoisted_login_function near top before event listeners
event_listener_idx = js.find('addEventListener(\'submit\', handleLoginSubmit)')
if event_listener_idx == -1:
    event_listener_idx = js.find('addEventListener("submit", handleLoginSubmit)')
if event_listener_idx == -1:
    event_listener_idx = js.find('loginForm')

if event_listener_idx >= 0:
    # Insert before
    line_start = js.rfind('\n', 0, event_listener_idx)
    if line_start == -1: line_start = 0
    js = js[:line_start] + "\n" + hoisted_login_function.strip() + "\n\n" + js[line_start:]
    print("  ✓ Inserted hoisted handleLoginSubmit before event listeners")
else:
    js = hoisted_login_function.strip() + "\n" + js
    print("  ✓ Prepended hoisted handleLoginSubmit to top of app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync HTML files with new timestamp
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

print(f"Fixed handleLoginSubmit hoisting and synced HTML files (v={ts})!")
