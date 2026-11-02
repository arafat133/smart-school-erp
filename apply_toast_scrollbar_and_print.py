"""
1. Inject global toast function at top of frontend/app.js
2. Append global Glassmorphism scrollbar & full column print CSS rules to frontend/style.css
3. Update HTML timestamps and sync admin.html & parent.html
"""
import re, time

print("=" * 60)
print("Injecting Global Toast, Scrollbar CSS, and Print Engine...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Global Toast Function
toast_js_code = """// ==================== GLOBAL TOAST NOTIFICATION SYSTEM ====================
function toast(msg, type = 0) {
    let box = document.getElementById('toastBox');
    if (!box) {
        box = document.createElement('div');
        box.id = 'toastBox';
        box.style.cssText = 'position:fixed;bottom:24px;left:24px;z-index:99999;display:flex;flex-direction:column;gap:8px;pointer-events:none;';
        document.body.appendChild(box);
    }
    const t = document.createElement('div');
    const isErr = type === 1 || type === 'error';
    const bg = isErr ? 'linear-gradient(135deg, #ef4444, #dc2626)' : 'linear-gradient(135deg, #1e293b, #0f172a)';
    const border = isErr ? '1px solid #f87171' : '1px solid #3b82f6';
    const shadow = isErr ? '0 10px 25px rgba(239, 68, 68, 0.4)' : '0 10px 25px rgba(59, 130, 246, 0.3)';
    
    t.style.cssText = `background:${bg};border:${border};box-shadow:${shadow};color:#fff;padding:12px 20px;border-radius:10px;font-size:0.9rem;font-weight:700;display:flex;align-items:center;gap:10px;min-width:260px;max-width:420px;opacity:0;transform:translateY(20px);transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1);pointer-events:auto;direction:rtl;`;
    t.innerHTML = `<i class="${isErr ? 'fa-solid fa-circle-exclamation' : 'fa-solid fa-circle-check'}" style="color:${isErr ? '#fca5a5' : '#60a5fa'};font-size:1.1rem;"></i> <span>${msg}</span>`;
    
    box.appendChild(t);
    requestAnimationFrame(() => {
        t.style.opacity = '1';
        t.style.transform = 'translateY(0)';
    });
    
    setTimeout(() => {
        t.style.opacity = '0';
        t.style.transform = 'translateY(20px)';
        setTimeout(() => { t.remove(); }, 300);
    }, 3200);
}
window.toast = toast;

"""

if 'window.toast = toast' not in js:
    js = toast_js_code + js
    print("  ✓ Injected Global Toast Notification function at line 1 of app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Global Scrollbar & Full Column Print CSS in style.css
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

scrollbar_print_css = """

/* ==================== GLOBAL GLASSMORPHISM SCROLLBAR FOR ALL INTERFACES ==================== */
* {
    scrollbar-width: thin;
    scrollbar-color: rgba(59, 130, 246, 0.6) rgba(15, 23, 42, 0.4);
}
*::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
*::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.5);
    border-radius: 4px;
}
*::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, rgba(59, 130, 246, 0.7), rgba(37, 99, 235, 0.9));
    border-radius: 4px;
    min-height: 30px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
*::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, rgba(59, 130, 246, 1), rgba(29, 78, 216, 1));
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.8);
}
*::-webkit-scrollbar-corner {
    background: transparent;
}

.page {
    overflow-y: auto !important;
    max-height: calc(100vh - 65px);
    padding-bottom: 35px;
}
.table-wrapper {
    overflow-x: auto !important;
    overflow-y: auto !important;
    max-height: 72vh;
}
.modal-body {
    overflow-y: auto !important;
    max-height: 70vh;
}
textarea, div, section {
    scrollbar-width: thin;
}

/* ==================== PRINT ENGINE - SHOW ALL COLUMNS WITHOUT TRUNCATION ==================== */
@media print {
    @page {
        size: landscape;
        margin: 6mm;
    }
    body, html {
        background: #fff !important;
        color: #000 !important;
        font-family: 'Cairo', 'Segoe UI', sans-serif !important;
        width: 100% !important;
        height: auto !important;
        overflow: visible !important;
    }
    .sidebar, .topbar, .toolbar, .btn-back, .btn-add, .btn-edit, .btn-delete, .btn-cancel, .btn-save, .act, .page-header button, #toastBox, .modal-overlay, .tab-nav, .search-box, .stats-row, #schoolTenantBadge, .window-controls {
        display: none !important;
    }
    .page-container {
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        box-shadow: none !important;
    }
    .page {
        display: block !important;
        overflow: visible !important;
        max-height: none !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }
    .page.active {
        display: block !important;
    }
    .page:not(.active) {
        display: none !important;
    }
    .page-header {
        background: none !important;
        border: none !important;
        padding: 4px 0 !important;
        margin-bottom: 8px !important;
        text-align: center !important;
    }
    .page-header h2 {
        color: #000 !important;
        font-size: 16pt !important;
        text-align: center !important;
        font-weight: 800 !important;
    }
    .page-header h2 i {
        display: none !important;
    }
    .table-wrapper {
        overflow: visible !important;
        max-height: none !important;
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    table {
        width: 100% !important;
        table-layout: auto !important;
        border-collapse: collapse !important;
        font-size: 8pt !important;
        page-break-inside: auto !important;
    }
    table th, table td {
        border: 1px solid #222 !important;
        padding: 4px 5px !important;
        color: #000 !important;
        background: #fff !important;
        text-align: center !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        word-break: break-word !important;
    }
    table th {
        background: #e2e8f0 !important;
        font-weight: 800 !important;
    }
    table thead {
        display: table-header-group !important;
    }
    table tr {
        page-break-inside: avoid !important;
    }
    .form-card, .stat-card {
        background: #fff !important;
        border: 1px solid #999 !important;
        color: #000 !important;
        box-shadow: none !important;
    }
}
"""

if 'GLOBAL GLASSMORPHISM SCROLLBAR FOR ALL INTERFACES' not in css:
    css += "\n" + scrollbar_print_css + "\n"
    print("  ✓ Appended Global Scrollbar & Full Column Print CSS to style.css")

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML cache timestamps
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

print(f"Updated HTML cache timestamps to v={ts}!")
