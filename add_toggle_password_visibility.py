"""
Add togglePasswordVisibility function to app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

toggle_fn = """
// ==================== TOGGLE PASSWORD VISIBILITY ====================
function togglePasswordVisibility(fieldId) {
    const input = document.getElementById(fieldId || 'password');
    const icon = document.getElementById('togglePassword') || (typeof event !== 'undefined' && event ? event.target : null);
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        if (icon) {
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
        }
    } else {
        input.type = 'password';
        if (icon) {
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
        }
    }
}
window.togglePasswordVisibility = togglePasswordVisibility;
"""

if 'window.togglePasswordVisibility = togglePasswordVisibility' not in js:
    js += "\n" + toggle_fn + "\n"
    print("  ✓ Appended togglePasswordVisibility function to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
