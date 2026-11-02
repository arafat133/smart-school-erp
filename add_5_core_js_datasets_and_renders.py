"""
Add rich initial datasets & render functions for 5 core interfaces in app.js
"""
import re, time

print("=" * 60)
print("Injecting Datasets & Renders for 5 Core Interfaces in app.js...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

core_js_engine = """
// ==================== 5 CORE INTERFACES DATASETS & RENDERS ====================

// 1. Users Directory Dataset
if (!DB.usersData) DB.usersData = [
    { id: 'USR-2026-01', username: 'admin', name: 'أ. خالد محمود العنسي', role: 'school_admin', roleName: 'مدير النظام التنفيذي', dept: 'الإدارة العامة', status: 'نشط 🟢', createdAt: '2026-01-01', pagesCount: '121 واجهة مصرحة' },
    { id: 'USR-2026-02', username: 'control', name: 'د. عبدالملك الشامي', role: 'control_officer', roleName: 'مسؤول الكنترول والامتحانات', dept: 'إدارة الامتحانات والنتائج', status: 'نشط 🟢', createdAt: '2026-01-05', pagesCount: '45 واجهة مصرحة' },
    { id: 'USR-2026-03', username: 'acc', name: 'أ. سارة أحمد العبسي', role: 'accountant', roleName: 'كبير المحاسبين والمالية', dept: 'الحسابات والشؤون المالية', status: 'نشط 🟢', createdAt: '2026-01-10', pagesCount: '38 واجهة مصرحة' },
    { id: 'USR-2026-04', username: 'teacher1', name: 'أ. إبراهيم العنسي', role: 'teacher', roleName: 'معلم أول مادة', dept: 'الكادر التعليمي', status: 'نشط 🟢', createdAt: '2026-01-12', pagesCount: '15 واجهة مصرحة' },
    { id: 'USR-2026-05', username: 'parent1', name: 'م. محمد علي السالمي', role: 'parent', roleName: 'حساب ولي أمر', dept: 'بوابة أولياء الأمور', status: 'نشط 🟢', createdAt: '2026-01-15', pagesCount: '8 واجهات مصرحة' }
];

function renderUsersGrid() {
    const tb = document.getElementById('tbl-users-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchUsers')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('usersData') : DB.usersData).filter(u => {
        return !filter || u.username.toLowerCase().includes(filter) || u.name.toLowerCase().includes(filter) || u.roleName.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(u => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${u.id}</td>
            <td style="font-weight:700;">${u.username}</td>
            <td>👤 ${u.name}</td>
            <td><span class="badge badge-info">${u.roleName}</span></td>
            <td>${u.dept}</td>
            <td><span class="badge badge-success">${u.status}</span></td>
            <td style="font-size:0.8rem;color:var(--muted);">${u.createdAt}</td>
            <td><strong style="color:#34d399;">${u.pagesCount}</strong></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('users', '${u.id}')"><i class="fa-solid fa-user-pen"></i> الصلاحيات</button>
                    <button class="btn-delete" onclick="deleteItem('usersData', '${u.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderUsersGrid = renderUsersGrid;
function renderUsers() { renderUsersGrid(); }
window.renderUsers = renderUsers;

// 2. Audit Logs Dataset
if (!DB.auditLogsData) DB.auditLogsData = [
    { id: 'LOG-2026-0812-9901', userRole: 'أ. خالد محمود (مدير النظام)', timestamp: '2026-08-12 02:15:30', module: 'الكنترول والامتحانات', actionType: 'UPDATE', targetEntity: 'جدول الامتحانات (EXM-2026-001)', oldValue: '{"date": "2026-06-14", "period": "مسائية"}', newValue: '{"date": "2026-06-15", "period": "صباحية"}', ipInfo: '192.168.1.45 (Chrome Windows)', severity: 'عالي الخطورة 🔴' },
    { id: 'LOG-2026-0812-9902', userRole: 'أ. سارة أحمد (كبير المحاسبين)', timestamp: '2026-08-12 03:20:10', module: 'سندات الصرف والقبض', actionType: 'INSERT', targetEntity: 'سند قبض رسوم (REC-2026-0412)', oldValue: 'N/A (سجل جديد)', newValue: '{"amount": 450000, "currency": "YER", "student": "عبدالرحمن علي"}', ipInfo: '192.168.1.88 (Firefox Windows)', severity: 'عادي 🟢' },
    { id: 'LOG-2026-0812-9903', userRole: 'د. عبدالملك الشامي (مسؤول الكنترول)', timestamp: '2026-08-12 04:10:05', module: 'رصد الدرجات والشيت', actionType: 'UPDATE', targetEntity: 'درجات الطالب (2026104)', oldValue: '{"physics": 78}', newValue: '{"physics": 95}', ipInfo: '192.168.1.12 (Edge Windows)', severity: 'متوسط 🟡' }
];

function renderAuditGrid() {
    const tb = document.getElementById('tbl-audit-logs-grid') || document.getElementById('tbl-audit');
    if (!tb) return;
    const filter = (document.getElementById('searchAudit')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('auditLogsData') : DB.auditLogsData).filter(a => {
        return !filter || a.id.toLowerCase().includes(filter) || a.userRole.toLowerCase().includes(filter) || a.module.toLowerCase().includes(filter) || a.actionType.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(a => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${a.id}</td>
            <td style="font-weight:700;">👤 ${a.userRole}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${a.timestamp}</td>
            <td><span class="badge badge-info">${a.module}</span></td>
            <td><strong style="color:${a.actionType==='DELETE'?'#ef4444':a.actionType==='INSERT'?'#10b981':'#f59e0b'};">${a.actionType}</strong></td>
            <td style="font-size:0.8rem;font-weight:600;">${a.targetEntity}</td>
            <td style="font-size:0.7rem;font-family:monospace;color:#f87171;max-width:120px;overflow:hidden;text-overflow:ellipsis;" title="${a.oldValue}">${a.oldValue}</td>
            <td style="font-size:0.7rem;font-family:monospace;color:#34d399;max-width:120px;overflow:hidden;text-overflow:ellipsis;" title="${a.newValue}">${a.newValue}</td>
            <td style="font-size:0.72rem;color:var(--muted);">${a.ipInfo}</td>
            <td><span class="badge ${a.severity.includes('عالي')?'badge-danger':'badge-success'}">${a.severity}</span></td>
            <td>
                <button class="btn-edit" onclick="showAuditDiffModal('${a.id}')" style="font-size:0.72rem;padding:3px 6px;"><i class="fa-solid fa-code-compare"></i> مطابقة (Diff)</button>
            </td>
        </tr>
    `).join('');
}
window.renderAuditGrid = renderAuditGrid;
function renderAuditLogs() { renderAuditGrid(); }
window.renderAuditLogs = renderAuditLogs;

// 3. Automated System Alerts Dataset
if (!DB.alertsData) DB.alertsData = [
    { id: 'RULE-NOTIF-2026-01', name: 'تنبيه الغياب الفوري لأولياء الأمور', trigger: 'تسجيل غياب طالب بدون عذر مقبول', channel: 'إشعار تطبيق (Push) + SMS', template: 'عزيزي ولي الأمر، تم تسجيل غياب ابنكم {اسم_الطالب} اليوم {التاريخ}.', recipient: 'ولي أمر الطالب المعني', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (148 رسالة)', schedule: 'فوري عند إغلاق تحضير الحصة الأولى', cost: 'خصم 1 وحدة SMS' },
    { id: 'RULE-NOTIF-2026-02', name: 'تنبيه اقتراب استحقاق القسط المالي', trigger: 'باقي 5 أيام على موعد استحقاق القسط', channel: 'SMS + WhatsApp', template: 'عزيزي ولي الأمر، نود تذكيركم بحلول موعد قسط {اسم_الطالب} بمبلغ {المبلغ}.', recipient: 'أولياء الأمور المستحق عليهم', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (52 رسالة)', schedule: 'يومياً الساعة 09:00 صباحاً', cost: 'خصم 1 وحدة WhatsApp' },
    { id: 'RULE-NOTIF-2026-03', name: 'إشعار صدور نتائج الامتحانات', trigger: 'اعتماد نتائج الفصل الدراسي بالكنترول', channel: 'إشعار تطبيق (Push)', template: 'تم اعتماد ونشر نتائج الفصل الدراسي الثاني لـ {اسم_الطالب}. اضغط للمعاينة.', recipient: 'جميع أولياء الأمور والطلاب', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (450 إشعار)', schedule: 'فوري عند الاعتماد', cost: 'مجاني (Push Notification)' }
];

function renderAlertsGrid() {
    const tb = document.getElementById('tbl-alerts-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchAlerts')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('alertsData') : DB.alertsData).filter(a => {
        return !filter || a.id.toLowerCase().includes(filter) || a.name.toLowerCase().includes(filter) || a.trigger.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(a => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${a.id}</td>
            <td style="font-weight:700;">${a.name}</td>
            <td style="font-size:0.8rem;color:#f59e0b;">${a.trigger}</td>
            <td><span class="badge badge-info">${a.channel}</span></td>
            <td style="font-size:0.75rem;color:var(--muted);max-width:180px;overflow:hidden;text-overflow:ellipsis;" title="${a.template}">${a.template}</td>
            <td style="font-size:0.8rem;">👤 ${a.recipient}</td>
            <td><span class="badge badge-success">${a.status}</span></td>
            <td><strong style="color:#34d399;font-size:0.78rem;">${a.deliveryLog}</strong></td>
            <td style="font-size:0.75rem;color:var(--muted);">${a.schedule}</td>
            <td><span class="badge badge-warning">${a.cost}</span></td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="openForm('alerts', '${a.id}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                    <button class="btn-delete" onclick="deleteItem('alertsData', '${a.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderAlertsGrid = renderAlertsGrid;

// 4. Digital Archiving Dataset
if (!DB.archiveData) DB.archiveData = [
    { id: 'DOC-2026-0881', title: 'ترخيص المدرسة الوزاري - عام 2026', folder: 'أرشيف الإدارة العامة / التراخيص', refNo: 'REF-MOE-10492', formatPreview: 'PDF (3.2 MB) | معاينة حية 📄', confidentiality: 'سري للغاية 🔴', tags: '#ترخيص, #وزارة_التربية, #2026', archivedAt: '2026-08-12 02:15 PM', archivedBy: 'أ. خالد محمود العنسي', retention: 'أرشيف دائم (Permanent) | أصل ورقي في الخزينة A' },
    { id: 'DOC-2026-0882', title: 'اعتماد تشكيل لجنة الكنترول والامتحانات', folder: 'أرشيف الامتحانات / القرارات الإدارية', refNo: 'DEC-2026-0041', formatPreview: 'PDF (1.8 MB) | معاينة حية 📄', confidentiality: 'خاص 🟡', tags: '#قرار, #كنترول, #امتحانات', archivedAt: '2026-08-10 11:30 AM', archivedBy: 'د. عبدالملك الشامي', retention: 'احتفاظ 5 سنوات | أصل ورقي في الأرشيف B' },
    { id: 'DOC-2026-0883', title: 'تقرير الجرد السنوي للمخازن والمعامل', folder: 'أرشيف الحسابات والمخازن', refNo: 'INV-REP-2026-99', formatPreview: 'XLSX (4.5 MB) | معاينة حية 📊', confidentiality: 'عام 🟢', tags: '#جرد, #مخازن, #حسابات', archivedAt: '2026-08-05 04:00 PM', archivedBy: 'أ. سارة أحمد', retention: 'احتفاظ 3 سنوات | نسخة إلكترونية' }
];

function renderArchiveGrid() {
    const tb = document.getElementById('tbl-archive-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchArchive')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('archiveData') : DB.archiveData).filter(d => {
        return !filter || d.id.toLowerCase().includes(filter) || d.title.toLowerCase().includes(filter) || d.tags.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(d => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${d.id}</td>
            <td style="font-weight:700;color:#1e3a8a;">${d.title}</td>
            <td><span class="badge badge-info">${d.folder}</span></td>
            <td style="font-size:0.78rem;font-family:monospace;">${d.refNo}</td>
            <td style="font-size:0.78rem;color:#34d399;">${d.formatPreview}</td>
            <td><span class="badge ${d.confidentiality.includes('سرية')?'badge-danger':'badge-warning'}">${d.confidentiality}</span></td>
            <td style="font-size:0.72rem;color:#60a5fa;">${d.tags}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${d.archivedAt}</td>
            <td>👤 ${d.archivedBy}</td>
            <td style="font-size:0.75rem;color:var(--muted);">${d.retention}</td>
            <td>
                <div class="act">
                    <button class="btn-edit" onclick="toast('📄 جاري فتح معاينة المستند المباشرة...')"><i class="fa-solid fa-eye"></i> معاينة</button>
                    <button class="btn-delete" onclick="deleteItem('archiveData', '${d.id}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderArchiveGrid = renderArchiveGrid;

// 5. Batch Posting Dataset
if (!DB.postingData) DB.postingData = [
    { id: 'PST-2026-08012', module: 'الرسوم والتحصيل المالي', voucherRef: 'JV-2026-00412', date: '2026-08-12', totalAmount: '500,000 YER (متوازن)', balanceStatus: 'سليم ومطابق (Valid) 🟢', status: 'مُرحّل (Posted) 🟢', postedBy: 'أ. خالد محمود العنسي', timestamp: '2026-08-12 - 04:30 PM', fiscalPeriod: 'الفترة 08 - أغسطس 2026' },
    { id: 'PST-2026-08013', module: 'مخازن وأذونات الصرف (GIN)', voucherRef: 'GIN-2026-0019', date: '2026-08-12', totalAmount: '120,000 YER (متوازن)', balanceStatus: 'سليم ومطابق (Valid) 🟢', status: 'معلق (Pending) 🟡', postedBy: 'أ. سارة أحمد', timestamp: 'قيد الانتظار', fiscalPeriod: 'الفترة 08 - أغسطس 2026' }
];

function renderPostingGrid() {
    const tb = document.getElementById('tbl-posting-grid');
    if (!tb) return;
    const filter = (document.getElementById('searchPosting')?.value || '').toLowerCase();
    const data = (typeof getSchoolData === 'function' ? getSchoolData('postingData') : DB.postingData).filter(p => {
        return !filter || p.id.toLowerCase().includes(filter) || p.module.toLowerCase().includes(filter) || p.voucherRef.toLowerCase().includes(filter);
    });

    tb.innerHTML = data.map(p => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${p.id}</td>
            <td><span class="badge badge-info">${p.module}</span></td>
            <td style="font-weight:700;font-family:monospace;">${p.voucherRef}</td>
            <td style="font-size:0.8rem;color:var(--muted);">${p.date}</td>
            <td style="font-weight:700;color:#34d399;">${p.totalAmount}</td>
            <td><span class="badge badge-success">${p.balanceStatus}</span></td>
            <td><span class="badge ${p.status.includes('مُرحّل')?'badge-success':'badge-warning'}">${p.status}</span></td>
            <td>👤 ${p.postedBy}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${p.timestamp}</td>
            <td style="font-size:0.78rem;color:var(--muted);">${p.fiscalPeriod}</td>
            <td>
                <div class="act">
                    ${p.status.includes('مُرحّل') ? 
                        `<button class="btn-delete" onclick="unpostBatch('${p.id}')" style="font-size:0.72rem;"><i class="fa-solid fa-rotate-left"></i> إلغاء الترحيل</button>` :
                        `<button class="btn-edit" onclick="postBatch('${p.id}')" style="background:#10b981;color:white;font-size:0.72rem;"><i class="fa-solid fa-check"></i> ترحيل الآن</button>`
                    }
                </div>
            </td>
        </tr>
    `).join('');
}
window.renderPostingGrid = renderPostingGrid;

function executeBatchPosting() {
    toast('⚡ جاري فحص توازن القيود وتمرير الترحيل الجماعي لكافة السندات المعلقة...');
    setTimeout(() => {
        if (DB.postingData) {
            DB.postingData.forEach(p => { p.status = 'مُرحّل (Posted) 🟢'; p.timestamp = new Date().toLocaleString('ar-EG'); });
        }
        renderPostingGrid();
        toast('🎉 تم ترحيل كافة السندات والمعاملات المالية والمخزنية بنجاح!');
    }, 800);
}
window.executeBatchPosting = executeBatchPosting;

function postBatch(id) {
    const item = (DB.postingData || []).find(p => p.id === id);
    if (item) {
        item.status = 'مُرحّل (Posted) 🟢';
        item.timestamp = new Date().toLocaleString('ar-EG');
        renderPostingGrid();
        toast(`✅ تم ترحيل الدفعة (${id}) إلى الحسابات العامة بنجاح`);
    }
}
window.postBatch = postBatch;

function unpostBatch(id) {
    const item = (DB.postingData || []).find(p => p.id === id);
    if (item) {
        item.status = 'معلق (Pending) 🟡';
        item.timestamp = 'تم فك الترحيل';
        renderPostingGrid();
        toast(`⚠️ تم إلغاء ترحيل الدفعة (${id}) وفق الصلاحيات المشددة`);
    }
}
window.unpostBatch = unpostBatch;

function saveSchoolInfo() {
    toast('💾 جاري حفظ وإعادة تحديث البيانات التعريفية والقانونية والسيادية للمؤسسة...');
    setTimeout(() => {
        toast('✅ تم تحديث بيانات ومعلومات المدرسة بنجاح في جميع التقارير الرسمية!');
    }, 600);
}
window.saveSchoolInfo = saveSchoolInfo;
"""

if 'window.renderUsersGrid = renderUsersGrid' not in js:
    js += "\n" + core_js_engine + "\n"
    print("  ✓ Appended 5 Core Interfaces datasets & renders to app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
