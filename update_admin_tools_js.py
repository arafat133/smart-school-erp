"""
Python script to append Administrative Tools logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Administrative Tools Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

admin_tools_db_additions = """
// Data collections for Administrative Tools modules
if (!DB.adminMessagesGridData) DB.adminMessagesGridData = [
    { id: 'ANN-2026-0045', title: 'تعميم إداري: تغيير مواعيد الدوام الشتوي الرسمي', category: 'قرار إداري', target: 'الكادر التعليمي (جميع المراحل)', body: 'استناداً إلى قرار وزارة التربية والتعليم تقرر بدء الدوام الشتوي من الساعة 07:30 صباحاً...', attachment: 'جدول_الدوام_الشتوي_2026.pdf', priority: 'عاجل وهام (Urgent)', dates: '2026-08-08 -> 2026-09-01', readStatus: 'المستهدف: 85 | تم الاطلاع: 80 (94%)', publisher: 'إدارة الموارد البشرية (أ. محمد الفاتح)' }
];

if (!DB.shortcutsGridData) DB.shortcutsGridData = [
    { id: 'SC-USER-2026-08', title: 'إرسال رسائل نصية (SMS)', module: 'نظام الرسائل والإشعارات', route: 'goTo("pg-sms-send")', iconColor: 'Icon: send-message | Color: #2563EB', hotkey: 'Ctrl + Shift + M', category: 'أدوات التواصل اليومية', order: 'المرتبة (1) في الأعلى', usage: '142 استخداماً هذا الشهر', status: 'مثبت (Pinned)' }
];

if (!DB.faqGridData) DB.faqGridData = [
    { id: 'FAQ-CTRL-05', category: 'نظام الكنترول والامتحانات', title: 'كيفية طباعة كشف التجميع النهائي (المشيت الرسمي)؟', solution: '1. انتقل لشاشة تقارير الكنترول 2. حدد الصف والمرحلة 3. انقر طباعة المشيت المعتمد', priority: 'عالية (High)', status: 'تم الحل (Resolved)', author: 'أ. خالد محمود العنسي (مسؤول الكنترول)', agent: 'م. أحمد الشامي (فريق الدعم الفني)', attachment: 'screenshot_guide.png', rating: '5 / 5 (ممتاز - 10 دقائق)' }
];

if (!DB.dictionaryGridData) DB.dictionaryGridData = [
    { key: 'TERM_ACAD_GPA', arTerm: 'المعدل التراكمي', enTerm: 'Cumulative Grade Point Average (CGPA)', domain: 'الشؤون الأكاديمية والكنترول', notes: 'يستخدم في كشوف الدرجات والشهادات الرسمية', output: 'الشهادات والتقارير (Certificates)', status: 'معتمد (Approved)', lastUpdate: '2026-08-08', reviewer: 'د. سامي القاضي (وحدة التعريب)', scope: 'القاموس الأكاديمي الموحد' }
];

if (!DB.personalInfoGridData) DB.personalInfoGridData = [
    { id: 'USR-2026-0104', name: 'أ. خالد محمود العنسي', role: 'مسؤول الكنترول والامتحانات (Control Officer)', dept: 'إدارة الشؤون الأكاديمية والكنترول', email: 'k.alansi@school.edu.ye', phone: '770000000', pref: 'اللغة العربية | المظهر الداكن (Dark Mode)', twoFactor: 'مفعل (SMS & Authenticator App)', sessions: 'Windows 11 - Chrome (متصل الآن)', status: 'نشط وموثق (Active & Verified)' }
];
"""

admin_tools_modules_js = """

// ==================== 1. ADMIN MESSAGES & ANNOUNCEMENTS ====================
function renderAdminMessagesGrid() {
    const tb = document.getElementById('tbl-admin-messages-grid');
    if (!tb) return;

    const list = DB.adminMessagesGridData || [];
    tb.innerHTML = list.map(a => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${a.id}</td>
            <td style="font-weight:700;">${a.title}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(239,68,68,0.15);color:#f87171;">${a.category}</span></td>
            <td>${a.target}</td>
            <td style="font-size:0.83rem;">${a.body}</td>
            <td style="font-size:0.8rem;color:#38bdf8;"><i class="fa-solid fa-paperclip"></i> ${a.attachment}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(239,68,68,0.2);color:#ef4444;">${a.priority}</span></td>
            <td style="font-size:0.8rem;">${a.dates}</td>
            <td style="font-size:0.83rem;font-weight:700;color:#34d399;">${a.readStatus}</td>
            <td style="font-size:0.8rem;">${a.publisher}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('admin-messages', ${JSON.stringify(a).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 2. FAVORITE SHORTCUTS ====================
function renderShortcutsGrid() {
    const tb = document.getElementById('tbl-shortcuts-grid');
    if (!tb) return;

    const list = DB.shortcutsGridData || [];
    tb.innerHTML = list.map(s => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${s.id}</td>
            <td style="font-weight:700;">${s.title}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${s.module}</span></td>
            <td style="font-size:0.8rem;color:#c084fc;">${s.route}</td>
            <td style="font-size:0.8rem;">${s.iconColor}</td>
            <td style="font-weight:700;color:#fbbf24;">${s.hotkey}</td>
            <td>${s.category}</td>
            <td>${s.order}</td>
            <td style="font-weight:700;color:#34d399;">${s.usage}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${s.status}</span></td>
            <td><button class="btn-add" onclick="${s.route}" style="padding:3px 8px;font-size:0.75rem;"><i class="fa-solid fa-play"></i> فتح</button></td>
        </tr>
    `).join('');
}


// ==================== 3. FAQ & SUPPORT HELPDESK ====================
function renderFaqGrid() {
    const tb = document.getElementById('tbl-faq-grid');
    if (!tb) return;

    const list = DB.faqGridData || [];
    tb.innerHTML = list.map(f => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${f.id}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${f.category}</span></td>
            <td style="font-weight:700;">${f.title}</td>
            <td style="font-size:0.83rem;">${f.solution}</td>
            <td style="color:#f59e0b;font-weight:700;">${f.priority}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${f.status}</span></td>
            <td style="font-size:0.8rem;">${f.author}</td>
            <td style="font-size:0.8rem;">${f.agent}</td>
            <td style="font-size:0.8rem;color:#38bdf8;"><i class="fa-solid fa-paperclip"></i> ${f.attachment}</td>
            <td style="font-weight:700;color:#fbbf24;">${f.rating}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('support-ticket', ${JSON.stringify(f).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 4. TRANSLATION & DICTIONARY ====================
function renderDictionaryGrid() {
    const tb = document.getElementById('tbl-dictionary-grid');
    if (!tb) return;

    const list = DB.dictionaryGridData || [];
    tb.innerHTML = list.map(d => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${d.key}</td>
            <td style="font-weight:700;">${d.arTerm}</td>
            <td style="font-weight:700;color:#38bdf8;">${d.enTerm}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(139,92,246,0.15);color:#c084fc;">${d.domain}</span></td>
            <td style="font-size:0.83rem;">${d.notes}</td>
            <td>${d.output}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${d.status}</span></td>
            <td style="font-size:0.8rem;">${d.lastUpdate}</td>
            <td style="font-size:0.8rem;">${d.reviewer}</td>
            <td>${d.scope}</td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('dictionary', ${JSON.stringify(d).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 5. PERSONAL PROFILE INFO ====================
function renderPersonalInfoGrid() {
    const tb = document.getElementById('tbl-personal-info-grid');
    if (!tb) return;

    const list = DB.personalInfoGridData || [];
    tb.innerHTML = list.map(p => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${p.id}</td>
            <td style="font-weight:700;">${p.name}</td>
            <td style="font-weight:700;color:#fbbf24;">${p.role}</td>
            <td>${p.dept}</td>
            <td style="font-size:0.83rem;">${p.email}</td>
            <td>${p.phone}</td>
            <td style="font-size:0.8rem;">${p.pref}</td>
            <td style="color:#10b981;font-weight:700;">${p.twoFactor}</td>
            <td style="font-size:0.8rem;">${p.sessions}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${p.status}</span></td>
            <td><button class="btn-edit" onclick="openForm('change-password')"><i class="fa-solid fa-key"></i> كلمة السر</button></td>
        </tr>
    `).join('');
}
"""

if 'ADMINISTRATIVE TOOLS MODULES' not in js:
    js += admin_tools_db_additions + "\n" + admin_tools_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Administrative Tools logic in app.js successfully!")
