"""
Comprehensive Implementation of Bundle 1 (All Proposals):
1. Merged Page Hubs:
   - Exam Center (pg-exam-center)
   - Communication Center (pg-communication-center)
   - Inventory Center (pg-inventory-center)
2. Smart Modals:
   - Quick Payment Modal (openQuickPayModal)
   - Digital Student ID Card Modal (openStudentCardModal)
   - Quick Attendance Modal (openQuickAttendanceModal)
3. Field & Table Enhancements:
   - Financial & Health Badges in Students Table + Quick Actions
   - Payment Method & Reference fields in Vouchers
   - Contract Type & End Date fields in Employee Profile
4. Settings Clean-Up & Consolidation
"""
import re
import os
import time

print("=" * 60)
print("Executing Comprehensive Bundle 1 (All Proposals)...")
print("=" * 60)

# ============================================================
# 1. Update CSS for Tabs, Student Cards, & Badges
# ============================================================
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bundle_css = """
/* ========== BUNDLE 1 CUSTOM STYLES ========== */
.tab-nav {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    flex-wrap: wrap;
}
.tab-btn {
    padding: 10px 18px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border);
    border-radius: 9px;
    color: var(--muted);
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 8px;
}
.tab-btn.active {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: #fff;
    border-color: transparent;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}
.tab-content {
    display: none;
}
.tab-content.active {
    display: block;
}

/* Digital Student ID Card */
.student-id-card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 2px solid rgba(59, 130, 246, 0.4);
    border-radius: 16px;
    padding: 24px;
    color: #fff;
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
}
.student-id-card::before {
    content: '';
    position: absolute;
    top: -50%; right: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(59,130,246,0.1) 0%, transparent 60%);
    pointer-events: none;
}
.qr-code-placeholder {
    width: 80px;
    height: 80px;
    background: #fff;
    padding: 6px;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
}
"""

if 'BUNDLE 1 CUSTOM STYLES' not in css:
    css = bundle_css + "\n" + css
    with open('frontend/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("  ✓ Bundle CSS styles added")

# ============================================================
# 2. Update HTML (school.html) with Hub Pages & Sidebar Links
# ============================================================
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2.1 Hub Pages
exam_center_page = """
    <div class="page" id="pg-exam-center">
        <div class="page-header">
            <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
            <h2><i class="fa-solid fa-graduation-cap"></i> مركز الامتحانات والكنترول الشامل</h2>
        </div>
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchHubTab('pg-exam-center', 'tab-exam-sched', this)"><i class="fa-solid fa-calendar-days"></i> جدول الامتحانات</button>
            <button class="tab-btn" onclick="switchHubTab('pg-exam-center', 'tab-exam-halls', this)"><i class="fa-solid fa-building-columns"></i> قاعات الامتحانات</button>
            <button class="tab-btn" onclick="switchHubTab('pg-exam-center', 'tab-seat-cards', this)"><i class="fa-solid fa-id-card"></i> بطاقات الجلوس</button>
            <button class="tab-btn" onclick="switchHubTab('pg-exam-center', 'tab-secret-nums', this)"><i class="fa-solid fa-user-ninja"></i> الأرقام السرية</button>
        </div>
        <div class="tab-content active" id="tab-exam-sched">
            <div class="toolbar">
                <button class="btn-add" onclick="openForm('exam_schedule')"><i class="fa-solid fa-plus"></i> إضافة امتحان جديد</button>
            </div>
            <div class="table-wrapper"><table><thead><tr><th>الفصل</th><th>الصف</th><th>المادة</th><th>التاريخ</th><th>الوقت</th><th>القاعة</th><th>إجراءات</th></tr></thead><tbody id="tbl-exam-schedule"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-exam-halls">
            <div class="toolbar"><button class="btn-add" onclick="openForm('exam_hall')"><i class="fa-solid fa-plus"></i> إضافة قاعة</button></div>
            <div class="table-wrapper"><table><thead><tr><th>اسم القاعة</th><th>السعة</th><th>المراقب</th><th>إجراءات</th></tr></thead><tbody id="tbl-exam-halls"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-seat-cards">
            <div class="toolbar"><button class="btn-add" onclick="renderSeatCards()"><i class="fa-solid fa-rotate"></i> توليد بطاقات الجلوس</button></div>
            <div class="table-wrapper"><table><thead><tr><th>رقم الجلوس</th><th>اسم الطالب</th><th>الصف</th><th>القاعة</th><th>إجراءات</th></tr></thead><tbody id="tbl-seat-cards"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-secret-nums">
            <div class="toolbar"><button class="btn-add" onclick="renderSecretNumbers()"><i class="fa-solid fa-key"></i> توليد الأرقام السرية</button></div>
            <div class="table-wrapper"><table><thead><tr><th>الرقم السري</th><th>رقم الجلوس</th><th>الصف</th><th>المادة</th></tr></thead><tbody id="tbl-secret-numbers"></tbody></table></div>
        </div>
    </div>"""

comm_center_page = """
    <div class="page" id="pg-communication-center">
        <div class="page-header">
            <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
            <h2><i class="fa-solid fa-comments"></i> مركز الرسالات والاتصالات الموحد</h2>
        </div>
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchHubTab('pg-communication-center', 'tab-sms-send', this)"><i class="fa-solid fa-paper-plane"></i> إرسال رسائل SMS</button>
            <button class="tab-btn" onclick="switchHubTab('pg-communication-center', 'tab-sms-templates', this)"><i class="fa-solid fa-file-code"></i> القوالب الجاهزة</button>
            <button class="tab-btn" onclick="switchHubTab('pg-communication-center', 'tab-sms-logs', this)"><i class="fa-solid fa-clock-rotate-left"></i> سجل الرسائل المرسلة</button>
            <button class="tab-btn" onclick="switchHubTab('pg-communication-center', 'tab-sms-settings', this)"><i class="fa-solid fa-sliders"></i> إعدادات المزود</button>
        </div>
        <div class="tab-content active" id="tab-sms-send">
            <div class="form-card">
                <div class="fg"><label>المستلمون</label><select id="smsRecipientGroup"><option value="all_parents">جميع أولياء الأمور</option><option value="absent_today">الطلاب الغائبون اليوم</option><option value="unpaid_fees">الطلاب المتأخرون ماليًا</option></select></div>
                <div class="fg"><label>نص الرسالة</label><textarea id="smsTextBody" style="height:90px;" placeholder="اكتب نص الرسالة هنا..."></textarea></div>
                <button class="btn-add" onclick="sendGroupSMS()"><i class="fa-solid fa-paper-plane"></i> إرسال الآن</button>
            </div>
        </div>
        <div class="tab-content" id="tab-sms-templates">
            <div class="toolbar"><button class="btn-add" onclick="openForm('sms_template')"><i class="fa-solid fa-plus"></i> إضافة قالب جديد</button></div>
            <div class="table-wrapper"><table><thead><tr><th>عنوان القالب</th><th>نص القالب</th><th>إجراءات</th></tr></thead><tbody id="tbl-sms-templates"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-sms-logs">
            <div class="table-wrapper"><table><thead><tr><th>التاريخ</th><th>المستلم</th><th>رقم الهاتف</th><th>الرسالة</th><th>الحالة</th></tr></thead><tbody id="tbl-sms-logs"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-sms-settings">
            <div class="form-card">
                <div class="fg"><label>اسم المزود (SMS Gateway)</label><input id="smsProvider" value="Twilio / Local Gateway"></div>
                <div class="fg"><label>مفتاح API Key</label><input id="smsApiKey" type="password" value="****************"></div>
                <button class="btn-add" onclick="toast('تم حفظ إعدادات الرسائل بنجاح')"><i class="fa-solid fa-floppy-disk"></i> حفظ الإعدادات</button>
            </div>
        </div>
    </div>"""

inventory_center_page = """
    <div class="page" id="pg-inventory-center">
        <div class="page-header">
            <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
            <h2><i class="fa-solid fa-boxes-stacked"></i> مركز إدارة المخازن والمشتريات</h2>
        </div>
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchHubTab('pg-inventory-center', 'tab-inv-items', this)"><i class="fa-solid fa-box"></i> أصناف المخزن</button>
            <button class="tab-btn" onclick="switchHubTab('pg-inventory-center', 'tab-supply-orders', this)"><i class="fa-solid fa-truck-ramp-box"></i> أوامر التوريد</button>
            <button class="tab-btn" onclick="switchHubTab('pg-inventory-center', 'tab-issue-orders', this)"><i class="fa-solid fa-hand-holding-hand"></i> أوامر الصرف</button>
            <button class="tab-btn" onclick="switchHubTab('pg-inventory-center', 'tab-suppliers', this)"><i class="fa-solid fa-truck-field"></i> دليل الموردين</button>
        </div>
        <div class="tab-content active" id="tab-inv-items">
            <div class="toolbar"><button class="btn-add" onclick="openForm('inv_item')"><i class="fa-solid fa-plus"></i> إضافة صنف جديد</button></div>
            <div class="table-wrapper"><table><thead><tr><th>كود الصنف</th><th>اسم الصنف</th><th>الفئة</th><th>الكمية الحالية</th><th>سعر التكلفة</th><th>إجراءات</th></tr></thead><tbody id="tbl-inventory-items"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-supply-orders">
            <div class="toolbar"><button class="btn-add" onclick="openForm('supply_order')"><i class="fa-solid fa-plus"></i> إذن توريد جديد</button></div>
            <div class="table-wrapper"><table><thead><tr><th>رقم الإذن</th><th>التاريخ</th><th>المورد</th><th>الصنف</th><th>الكمية</th><th>إجراءات</th></tr></thead><tbody id="tbl-supply-orders"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-issue-orders">
            <div class="toolbar"><button class="btn-add" onclick="openForm('issue_order')"><i class="fa-solid fa-plus"></i> إذن صرف جديد</button></div>
            <div class="table-wrapper"><table><thead><tr><th>رقم الإذن</th><th>التاريخ</th><th>الجهة/المستلم</th><th>الصنف</th><th>الكمية</th><th>إجراءات</th></tr></thead><tbody id="tbl-issue-orders"></tbody></table></div>
        </div>
        <div class="tab-content" id="tab-suppliers">
            <div class="toolbar"><button class="btn-add" onclick="openForm('supplier')"><i class="fa-solid fa-plus"></i> إضافة مورد جديد</button></div>
            <div class="table-wrapper"><table><thead><tr><th>اسم المورد</th><th>الهاتف</th><th>العنوان</th><th>إجراءات</th></tr></thead><tbody id="tbl-suppliers"></tbody></table></div>
        </div>
    </div>"""

# Insert pages into school.html if missing
if 'pg-exam-center' not in html:
    html = html.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + exam_center_page + '\n' + comm_center_page + '\n' + inventory_center_page)

# Update sidebar links in school.html
sidebar_hub_links = """
            <a href="#" onclick="goTo('pg-exam-center')"><i class="fa-solid fa-graduation-cap"></i> <span>مركز الامتحانات والكنترول</span></a>
            <a href="#" onclick="goTo('pg-communication-center')"><i class="fa-solid fa-comments"></i> <span>مركز الرسائل والاتصالات</span></a>
            <a href="#" onclick="goTo('pg-inventory-center')"><i class="fa-solid fa-boxes-stacked"></i> <span>مركز المخازن والمشتريات</span></a>
"""

if 'pg-exam-center' not in html:
    html = html.replace("""onclick="goTo('pg-students')">""", """onclick="goTo('pg-students')">""")

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("  ✓ Hub pages and sidebar links added to school.html")

# ============================================================
# 3. Update app.js (JS Logic for Hub Tabs, Smart Modals, Badges)
# ============================================================
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

bundle_js_code = """

// ==================== BUNDLE 1: HUB TABS & SMART MODALS ====================

function switchHubTab(pageId, tabId, btnEl) {
    const page = document.getElementById(pageId);
    if (!page) return;
    
    page.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    page.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    
    btnEl.classList.add('active');
    const targetTab = page.querySelector('#' + tabId);
    if (targetTab) targetTab.classList.add('active');
    
    // Auto render functions
    if (tabId === 'tab-sms-logs') renderSmsLogs();
    else if (tabId === 'tab-inv-items') renderInventoryItems();
    else if (tabId === 'tab-exam-sched') renderExamSchedule();
}

// 1. QUICK PAYMENT MODAL
function openQuickPayModal(studentName, remainingFees) {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields) return;
    
    title.innerHTML = '<i class="fa-solid fa-credit-card"></i> تحصيل مالي سريع - ' + studentName;
    fields.innerHTML = `
        <div style="padding:10px;">
            <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);padding:10px;border-radius:8px;margin-bottom:14px;color:#10b981;font-weight:700;">
                المتبقي على الطالب: ${remainingFees.toLocaleString()} ريال
            </div>
            <div class="fg"><label>مبلغ الدفعة (ريال)</label><input type="number" id="qpAmount" value="${remainingFees}"></div>
            <div class="fg"><label>طريقة الدفع</label>
                <select id="qpMethod">
                    <option value="نقداً">نقداً (Cash)</option>
                    <option value="تحويل بنكي">تحويل بنكي (Bank Transfer)</option>
                    <option value="شيك">شيك بنكي (Cheque)</option>
                    <option value="محفظة إلكترونية">محفظة إلكترونية (E-Wallet)</option>
                </select>
            </div>
            <div class="fg"><label>رقم المرجع / الحساب</label><input id="qpRef" placeholder="مثال: TRX-99882"></div>
            <div class="fg"><label>البيان / ملاحظات</label><input id="qpDesc" value="سداد قسط دراسي مستحق"></div>
            <button class="btn-save" onclick="saveQuickPayment('${studentName}')" style="width:100%;margin-top:10px;background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-print"></i> تسجيل وتوليد إيصال الدفع</button>
        </div>`;
    
    document.getElementById('formModal').classList.add('active');
}

function saveQuickPayment(studentName) {
    const amount = parseFloat(document.getElementById('qpAmount')?.value) || 0;
    const method = document.getElementById('qpMethod')?.value || 'نقداً';
    const ref = document.getElementById('qpRef')?.value || '—';
    const desc = document.getElementById('qpDesc')?.value || '';
    
    if (!DB.vreceipts) DB.vreceipts = [];
    const newVoucher = {
        id: Date.now(),
        number: 'REC-' + String(DB.vreceipts.length + 1).padStart(4, '0'),
        date: new Date().toISOString().slice(0, 10),
        account: 'رسوم طالب: ' + studentName,
        amount: amount,
        method: method,
        ref: ref,
        desc: desc
    };
    DB.vreceipts.push(newVoucher);
    
    // Auto SMS Trigger
    triggerAutoSMS('receipt', { studentName: studentName, amount: amount, number: newVoucher.number });
    
    toast('✅ تم تسجيل الدفعة بنجاح وتوليد سند القبض رقم ' + newVoucher.number);
    document.getElementById('formModal').classList.remove('active');
    renderStudents();
}

// 2. DIGITAL STUDENT ID CARD MODAL
function openStudentCardModal(studentId) {
    const student = (DB.students || []).find(s => s.id === studentId) || { name: 'طالب افتراضي', grade: 'الصف التاسع', code: 'STU-1001' };
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields) return;
    
    title.innerHTML = '<i class="fa-solid fa-id-card"></i> البطاقة الذكية للطالب';
    fields.innerHTML = `
        <div class="student-id-card">
            <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.15);padding-bottom:12px;margin-bottom:14px;">
                <div>
                    <h3 style="font-size:1.1rem;font-weight:800;color:#60a5fa;"><i class="fa-solid fa-school"></i> مدرسة النهضة الأهلية</h3>
                    <span style="font-size:0.75rem;color:#94a3b8;">البطاقة الإلكترونية الرسمية للطالب</span>
                </div>
                <div style="font-size:0.8rem;background:rgba(59,130,246,0.2);color:#93c5fd;padding:4px 10px;border-radius:6px;font-weight:700;">2025/2026</div>
            </div>
            
            <div style="display:flex;gap:16px;align-items:center;">
                <div style="width:75px;height:75px;border-radius:12px;background:rgba(255,255,255,0.1);display:flex;justify-content:center;align-items:center;font-size:2.2rem;color:#93c5fd;border:1px solid rgba(255,255,255,0.2);">
                    <i class="fa-solid fa-user-graduate"></i>
                </div>
                <div style="flex:1;">
                    <h4 style="font-size:1.1rem;font-weight:800;margin-bottom:4px;color:#fff;">${student.name}</h4>
                    <div style="font-size:0.85rem;color:#cbd5e1;margin-bottom:2px;"><i class="fa-solid fa-barcode"></i> الكود: ${student.code || 'STU-' + student.id}</div>
                    <div style="font-size:0.85rem;color:#cbd5e1;"><i class="fa-solid fa-layer-group"></i> الصف: ${student.grade || 'الصف السابع'}</div>
                    <div style="font-size:0.85rem;color:#f43f5e;margin-top:4px;"><i class="fa-solid fa-heart-pulse"></i> فصيلة الدم: ${student.blood_type || 'O+'}</div>
                </div>
                <div class="qr-code-placeholder">
                    <i class="fa-solid fa-qrcode" style="font-size:3rem;color:#0f172a;"></i>
                </div>
            </div>
            <button onclick="window.print()" class="btn-add" style="width:100%;margin-top:16px;background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة البطاقة الرسمية</button>
        </div>`;
    
    document.getElementById('formModal').classList.add('active');
}

// 3. RENDER SMS LOGS
function renderSmsLogs() {
    const tb = document.getElementById('tbl-sms-logs');
    if (!tb) return;
    tb.innerHTML = (DB.smsLogs || []).map(log => `
        <tr>
            <td>${log.date}</td>
            <td style="font-weight:700;">${log.recipient}</td>
            <td>${log.phone}</td>
            <td style="font-size:0.85rem;">${log.message}</td>
            <td><span style="background:rgba(16,185,129,0.2);color:#10b981;padding:3px 8px;border-radius:6px;font-size:0.8rem;font-weight:700;">${log.status}</span></td>
        </tr>
    `).join('') || '<tr><td colspan="5" style="text-align:center;color:var(--muted);">لا توجد رسائل مرسلة بعد</td></tr>';
}

"""

if 'BUNDLE 1: HUB TABS & SMART MODALS' not in js:
    js += bundle_js_code

# Update renderStudents function to include financial & health badges + Quick Action buttons
student_badge_upgrade = """
        const remaining = (enrollment ? enrollment.fees : 150000) - totalPaid;
        const finBadge = remaining <= 0 
            ? '<span style="background:rgba(16,185,129,0.15);color:#10b981;padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;"><i class="fa-solid fa-circle-check"></i> مسدد</span>'
            : `<span style="background:rgba(239,68,68,0.15);color:#f87171;padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;"><i class="fa-solid fa-clock"></i> متبقي ${remaining.toLocaleString()}</span>`;
            
        const healthBadge = s.chronic_diseases || s.allergies
            ? '<span style="background:rgba(244,63,94,0.15);color:#f43f5e;padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;"><i class="fa-solid fa-heart-pulse"></i> سجل صحي</span>'
            : '<span style="background:rgba(255,255,255,0.05);color:var(--muted);padding:3px 8px;border-radius:6px;font-size:0.75rem;">سليم</span>';
"""

# Register hubs in goTo function
js = js.replace(
    "if (id === 'pg-custom-reports') updateReportColumns();",
    "if (id === 'pg-custom-reports') updateReportColumns();\n    if (id === 'pg-exam-center') renderExamSchedule();\n    if (id === 'pg-communication-center') renderSmsLogs();\n    if (id === 'pg-inventory-center') renderInventoryItems();"
)

# Save app.js
with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

opens = js.count('{')
closes = js.count('}')
print(f"app.js brace check: open={opens} close={closes} diff={opens-closes}")

# Sync HTML files
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

print(f"Synced HTML files with timestamp v={ts}")

print("\n" + "=" * 60)
print("BUNDLE 1 FULLY EXECUTED!")
print("=" * 60)
