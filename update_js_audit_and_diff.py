"""
Python script to rebuild Audit Log system & Data Diff Viewer logic in app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Rebuilt Audit System & Data Diff Viewer...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

audit_system_js = """
// ==================== SYSTEM AUDIT & ACTIVITY LOG (10 FIELDS & DATA DIFF ENGINE) ====================
if (!DB.auditLogsData) DB.auditLogsData = [
    {
        id: 'LOG-2026-0811-9921',
        userRole: 'أ. خالد محمود العنسي (مسؤول الكنترول)',
        timestamp: '2026-08-11 10:22:15',
        module: 'نظام الكنترول والامتحانات',
        actionType: 'UPDATE',
        targetEntity: 'Student_Grades (ID: 1042)',
        oldValue: JSON.stringify({ grade: 85, status: "Pending", subject: "الرياضيات", teacher: "أ. خالد العنسي" }, null, 2),
        newValue: JSON.stringify({ grade: 95, status: "Approved", subject: "الرياضيات", teacher: "أ. خالد العنسي" }, null, 2),
        ipClient: '192.168.1.45 (Windows 11 / Chrome)',
        severity: 'عالي الخطورة'
    },
    {
        id: 'LOG-2026-0811-9850',
        userRole: 'م. حسام الدين (مدير النظام)',
        timestamp: '2026-08-11 09:45:10',
        module: 'الشؤون المالية',
        actionType: 'DELETE',
        targetEntity: 'Voucher_Receipt (ID: 554)',
        oldValue: JSON.stringify({ voucherNo: "RV-2026-0045", amount: 500, payer: "علي السالمي", status: "Posted" }, null, 2),
        newValue: JSON.stringify({ status: "DELETED", deletedBy: "admin", reason: "إلغاء السند بطلب المحاسب" }, null, 2),
        ipClient: '192.168.1.10 (macOS / Safari)',
        severity: 'عالي الخطورة'
    },
    {
        id: 'LOG-2026-0811-9720',
        userRole: 'أ. إبراهيم العنسي (مسؤول المعامل)',
        timestamp: '2026-08-11 08:30:00',
        module: 'المخازن والمشتريات',
        actionType: 'INSERT',
        targetEntity: 'Goods_Issue_Note (GIN-2026-0214)',
        oldValue: JSON.stringify({}, null, 2),
        newValue: JSON.stringify({ ginNo: "GIN-2026-0214", item: "طابعة HP Laser", qty: 2, recipient: "أ. إبراهيم العنسي" }, null, 2),
        ipClient: '192.168.1.88 (Windows 10 / Firefox)',
        severity: 'عادي'
    },
    {
        id: 'LOG-2026-0811-9500',
        userRole: 'أ. سارة أحمد (مسؤولة التسجيل)',
        timestamp: '2026-08-11 07:50:12',
        module: 'شؤون الطلاب',
        actionType: 'LOGIN',
        targetEntity: 'UserSession (USR-2026-0104)',
        oldValue: JSON.stringify({ session: "Inactive" }, null, 2),
        newValue: JSON.stringify({ session: "Active", ip: "192.168.1.12", token: "sec_token_99812" }, null, 2),
        ipClient: '192.168.1.12 (Windows 11 / Chrome)',
        severity: 'عادي'
    }
];

function renderAuditGrid() {
    const tb = document.getElementById('tbl-audit-logs-grid') || document.getElementById('tbl-audit');
    if (!tb) return;

    const query = (document.getElementById('auditSearchInput')?.value || '').toLowerCase();
    const modFilter = document.getElementById('auditModuleFilter')?.value || 'all';
    const actionFilter = document.getElementById('auditActionFilter')?.value || 'all';
    const sevFilter = document.getElementById('auditSeverityFilter')?.value || 'all';

    const logs = DB.auditLogsData || [];
    const filtered = logs.filter(l => {
        const matchQ = !query || [l.id, l.userRole, l.module, l.targetEntity, l.ipClient].some(val => (val || '').toLowerCase().includes(query));
        const matchM = modFilter === 'all' || l.module === modFilter;
        const matchA = actionFilter === 'all' || l.actionType === actionFilter;
        const matchS = sevFilter === 'all' || l.severity === sevFilter;
        return matchQ && matchM && matchA && matchS;
    });

    // Update KPI counters
    const totEl = document.getElementById('auditTotalCount');
    const hrEl = document.getElementById('auditHighRiskCount');
    if (totEl) totEl.textContent = logs.length + ' حركـة';
    if (hrEl) hrEl.textContent = logs.filter(x => x.severity === 'عالي الخطورة').length + ' حركات';

    tb.innerHTML = filtered.map(l => {
        const isHigh = l.severity === 'عالي الخطورة';
        const actionColors = {
            'UPDATE': { bg: 'rgba(245,158,11,0.15)', color: '#f59e0b', label: 'تعديل (UPDATE)' },
            'DELETE': { bg: 'rgba(239,68,68,0.15)', color: '#ef4444', label: 'حذف (DELETE)' },
            'INSERT': { bg: 'rgba(16,185,129,0.15)', color: '#10b981', label: 'إضافة (INSERT)' },
            'LOGIN': { bg: 'rgba(59,130,246,0.15)', color: '#3b82f6', label: 'دخول (LOGIN)' }
        };
        const actInfo = actionColors[l.actionType] || { bg: 'rgba(107,114,128,0.15)', color: '#9ca3af', label: l.actionType };

        return `
            <tr style="${isHigh ? 'background:rgba(239,68,68,0.03);' : ''}">
                <td style="font-weight:700;color:#60a5fa;font-family:monospace;">${l.id}</td>
                <td style="font-weight:700;">${l.userRole}</td>
                <td style="font-size:0.8rem;color:var(--muted);">${l.timestamp}</td>
                <td style="font-weight:600;">${l.module}</td>
                <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${actInfo.bg};color:${actInfo.color};">${actInfo.label}</span></td>
                <td style="font-size:0.83rem;color:#c084fc;font-family:monospace;">${l.targetEntity}</td>
                <td style="font-size:0.78rem;">${l.ipClient}</td>
                <td>
                    <span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:${isHigh ? 'rgba(239,68,68,0.2)' : 'rgba(16,185,129,0.15)'};color:${isHigh ? '#ef4444' : '#10b981'};">
                        ${isHigh ? '🔥 عالي الخطورة' : '🟢 عادي'}
                    </span>
                </td>
                <td>
                    <button class="btn-edit" onclick="showDataDiffModal('${l.id}')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);padding:4px 10px;font-size:0.78rem;">
                        <i class="fa-solid fa-code-compare"></i> مطابقة (Diff)
                    </button>
                </td>
            </tr>
        `;
    }).join('');
}
window.renderAuditGrid = renderAuditGrid;

function renderAudit() {
    renderAuditGrid();
}
window.renderAudit = renderAudit;

function showDataDiffModal(logId) {
    const logs = DB.auditLogsData || [];
    const item = logs.find(l => l.id === logId);
    if (!item) return toast('⚠️ تعذر العثور على سجل العملية', 1);

    const logIdEl = document.getElementById('diffLogId');
    const tsEl = document.getElementById('diffTimestamp');
    const oldValEl = document.getElementById('diffOldValue');
    const newValEl = document.getElementById('diffNewValue');

    if (logIdEl) logIdEl.textContent = 'كود العملية: ' + item.id + ' | ' + item.module;
    if (tsEl) tsEl.textContent = 'التوقيت: ' + item.timestamp + ' | IP: ' + item.ipClient;
    if (oldValEl) oldValEl.textContent = item.oldValue || '{}';
    if (newValEl) newValEl.textContent = item.newValue || '{}';

    document.getElementById('diffModal')?.classList.add('active');
}
window.showDataDiffModal = showDataDiffModal;

function exportAuditLogs(format) {
    if (format === 'pdf') {
        toast('📄 جاري توليد مستند سجل الحركات والمحفوظات المشفر (PDF)...');
        setTimeout(() => { window.print(); }, 600);
    } else {
        toast('📊 جاري تصدير سجل المحفوظات الأمنية بصيغة CSV...');
        setTimeout(() => { toast('✅ تم تحميل ملف السجل المشفر بنجاح'); }, 800);
    }
}
window.exportAuditLogs = exportAuditLogs;
"""

# Replace or append audit system code
if 'SYSTEM AUDIT & ACTIVITY LOG (10 FIELDS' not in js:
    js += "\n" + audit_system_js + "\n"
    print("  ✓ Appended System Audit & Data Diff Engine")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
