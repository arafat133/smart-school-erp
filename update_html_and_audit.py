"""
Update school.html:
1. Clean up loginOverlay (remove extra chkShowPass checkbox, remove forgot password link, remove demo quick fill buttons)
2. Rebuild pg-audit HTML page container with all 10 requested fields & filters
3. Add diffModal overlay for Old vs New value comparison
4. Remove pg-permissions / pg-permission-matrix
"""
import re, time

print("=" * 60)
print("Updating school.html for Security, Login Cleanups & Rebuilt Audit...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean up loginOverlay:
# Remove chkShowPass container
chk_show_pass_regex = r'<div style="display:\s*flex;\s*justify-content:\s*flex-end;.*?<span>إظهار كلمة المرور</span>\s*</label>\s*</div>'
html = re.sub(chk_show_pass_regex, '', html, flags=re.DOTALL)

# Remove forgot password link
forgot_pass_regex = r'<a href="#" onclick="openForgotPasswordModal\(event\)"[^>]*>.*?نسيت كلمة المرور\؟\s*</a>'
html = re.sub(forgot_pass_regex, '', html, flags=re.DOTALL)

# Remove demo quick fill buttons container
demo_quick_fill_regex = r'<div style="margin-top:\s*20px;\s*padding-top:\s*15px;\s*border-top:\s*1px dashed #cbd5e1;.*?</div>\s*</form>'
html = re.sub(demo_quick_fill_regex, '</form>', html, flags=re.DOTALL)

print("  ✓ Cleaned up login form controls (removed extra show pass checkbox, forgot pass link, demo buttons)")

# 2. Rebuild pg-audit HTML container
audit_html = """
<div class="page" id="pg-audit">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-shield-cat"></i> سجل العمليات والمحفوظات الأمنية (System Audit & Activity Log)</h2>
    </div>

    <!-- Security KPI Header Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي الحركات المسجلة</h3><p style="color:#60a5fa;font-weight:800;font-size:1.3rem;" id="auditTotalCount">1,420 حركـة</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>حركات عالية الخطورة (Audit Alert)</h3><p style="color:#f87171;font-weight:800;font-size:1.3rem;" id="auditHighRiskCount">3 حركات</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>محاولات الدخول الفاشلة المحظورة</h3><p style="color:#fbbf24;font-weight:800;font-size:1.3rem;">0 محاولات</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>حالة جدار الحماية (Firewall)</h3><p style="color:#34d399;font-weight:800;font-size:1.3rem;">نشط ومحمّي 🛡️</p></div>
        </div>
    </div>

    <!-- Audit Filter & Search Bar -->
    <div class="form-card" style="padding:14px;margin-bottom:16px;background:rgba(15,23,42,0.85);border:1px solid rgba(59,130,246,0.3);">
        <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
            <div class="search-box" style="flex:2;min-width:200px;">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input id="auditSearchInput" placeholder="بحث بكود الحركة LOG- / اسم المستخدم / الكيان / الـ IP..." oninput="renderAuditGrid()">
            </div>
            <select id="auditModuleFilter" onchange="renderAuditGrid()" style="flex:1;min-width:140px;padding:8px;font-size:0.85rem;">
                <option value="all">جميع الأقسام والأنظمة</option>
                <option value="الكنترول والامتحانات">نظام الكنترول والامتحانات</option>
                <option value="شؤون الطلاب">شؤون الطلاب</option>
                <option value="الشؤون المالية">الشؤون المالية</option>
                <option value="شؤون الموظفين">شؤون الموظفين</option>
                <option value="المخازن والمشتريات">المخازن والمشتريات</option>
                <option value="إدارة النظام">إدارة النظام</option>
            </select>
            <select id="auditActionFilter" onchange="renderAuditGrid()" style="flex:1;min-width:140px;padding:8px;font-size:0.85rem;">
                <option value="all">جميع أنواع الإجراءات</option>
                <option value="UPDATE">تعديل سجل (UPDATE)</option>
                <option value="DELETE">حذف سجل (DELETE)</option>
                <option value="INSERT">إضافة سجل (INSERT)</option>
                <option value="LOGIN">تسجيل دخول (LOGIN)</option>
            </select>
            <select id="auditSeverityFilter" onchange="renderAuditGrid()" style="flex:1;min-width:140px;padding:8px;font-size:0.85rem;">
                <option value="all">جميع مستويات الخطورة</option>
                <option value="عالي الخطورة">عالي الخطورة (Security Audit)</option>
                <option value="عادي">عادي (Normal Audit)</option>
            </select>
            <button class="btn-add" onclick="exportAuditLogs('pdf')" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-file-pdf"></i> تصدير مشفر PDF</button>
            <button class="btn-add" onclick="exportAuditLogs('csv')" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-csv"></i> تصدير CSV</button>
        </div>
    </div>

    <!-- Main Audit Data Stream Table -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود العملية (Audit Log ID)</th>
                    <th>المستخدم ورتبته (User & Role)</th>
                    <th>التوقيت والختم الزمني</th>
                    <th>الموديول / القسم</th>
                    <th>نوع الإجراء (CRUD)</th>
                    <th>الكيان والصف المستهدف</th>
                    <th>عنوان الـ IP والجهاز</th>
                    <th>مستوى الخطورة</th>
                    <th>مستكشف التغييرات (Data Diff)</th>
                </tr>
            </thead>
            <tbody id="tbl-audit-logs-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or add pg-audit
pattern_audit = r'<div class="page" id="pg-audit">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
if re.search(pattern_audit, html, re.DOTALL):
    html = re.sub(pattern_audit, audit_html.strip() + '\n', html, flags=re.DOTALL)
    print("  ✓ Replaced pg-audit HTML container")
else:
    html = html.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + audit_html.strip())
    print("  ✓ Added pg-audit HTML container")

# 3. Add diffModal overlay before toastBox or at modals section
diff_modal_html = """
<div class="modal-overlay" id="diffModal">
    <div class="modal-content glass-panel" style="max-width:750px;">
        <div class="modal-header">
            <h3><i class="fa-solid fa-code-compare" style="color:#60a5fa;"></i> مستكشف ومطابقة التغييرات (Data Diff Viewer)</h3>
            <div class="window-controls"><button class="btn-close" onclick="closeModal('diffModal')"><i class="fa-solid fa-xmark"></i></button></div>
        </div>
        <div class="modal-body" style="padding:20px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:12px;font-size:0.85rem;color:var(--muted);">
                <span id="diffLogId"></span>
                <span id="diffTimestamp"></span>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
                <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.4);border-radius:10px;padding:14px;">
                    <h4 style="color:#f87171;margin-top:0;font-size:0.9rem;"><i class="fa-solid fa-rotate-left"></i> البيانات قبل التعديل (Old Value)</h4>
                    <pre id="diffOldValue" style="background:rgba(15,23,42,0.9);color:#fca5a5;padding:10px;border-radius:6px;font-size:0.8rem;white-space:pre-wrap;word-break:break-word;"></pre>
                </div>
                <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.4);border-radius:10px;padding:14px;">
                    <h4 style="color:#34d399;margin-top:0;font-size:0.9rem;"><i class="fa-solid fa-rotate-right"></i> البيانات بعد التعديل (New Value)</h4>
                    <pre id="diffNewValue" style="background:rgba(15,23,42,0.9);color:#6ee7b7;padding:10px;border-radius:6px;font-size:0.8rem;white-space:pre-wrap;word-break:break-word;"></pre>
                </div>
            </div>
        </div>
    </div>
</div>
"""

if 'id="diffModal"' not in html:
    html = html.replace('<div class="modal-overlay" id="formModal">', diff_modal_html.strip() + '\n<div class="modal-overlay" id="formModal">')
    print("  ✓ Added diffModal overlay")

# 4. Remove pg-permissions / pg-permission-matrix container & sidebar link
pattern_perm = r'<div class="page" id="pg-permissions">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
html = re.sub(pattern_perm, '', html, flags=re.DOTALL)

pattern_perm_matrix = r'<div class="page" id="pg-permission-matrix">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
html = re.sub(pattern_perm_matrix, '', html, flags=re.DOTALL)

# Remove sidebar link for permissions
pattern_nav_perm = r'<a[^>]*goTo\(\'pg-permissions\'\)[^>]*>.*?</a>\s*'
html = re.sub(pattern_nav_perm, '', html, flags=re.DOTALL)

pattern_nav_perm2 = r'<a[^>]*goTo\(\'pg-permission-matrix\'\)[^>]*>.*?</a>\s*'
html = re.sub(pattern_nav_perm2, '', html, flags=re.DOTALL)

print("  ✓ Removed pg-permissions and sidebar links")

# Update cache timestamps
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

print(f"Updated HTML files successfully with timestamp v={ts}!")
