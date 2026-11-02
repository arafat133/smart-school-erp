/**
 * ============================================================================
 * MODULE: OPERATION-LOCK.JS - Operational Period Locking & Validation Engine
 * ============================================================================
 */
(function initOperationLockModule() {
    if (!window.DB) window.DB = {};
    if (!window.DB.operationLocks) {
        window.DB.operationLocks = [
            { id: 'LCK-2026-001', opType: 'رصد واعتماد الدرجات (الكنترول)', startDate: '2026-08-01', endDate: '2026-08-15', reason: 'انتهاء فترة رصد درجات الفصل الأول', status: 'مقفل 🔒', lockedBy: 'د. سالم الحميري', createdAt: '2026-08-01' },
            { id: 'LCK-2026-002', opType: 'تعديل القيود والسندات المالية', startDate: '2026-08-10', endDate: '2026-08-20', reason: 'إتمام المراجعة والتدقيق المالي السنوي', status: 'مقفل 🔒', lockedBy: 'أ. عبد الرحمن باعباد', createdAt: '2026-08-10' }
        ];
    }

    window.renderOperationLockGrid = function() {
        const tb = document.getElementById('tbl-operation-lock');
        if (!tb) return;

        const data = window.DB.operationLocks || [];
        if (data.length === 0) {
            tb.innerHTML = '<tr><td colspan="8" style="text-align:center;color:var(--muted);padding:30px;">لا توجد قواعد قفل عمليات مسجلة حالياً</td></tr>';
            return;
        }

        tb.innerHTML = data.map((item, idx) => {
            const isLocked = item.status.includes('مقفل') || item.status.includes('🔒');
            const statusBadge = isLocked 
                ? '<span class="badge badge-danger">مقفل بالكامل 🔒</span>' 
                : '<span class="badge badge-success">مفتوح ونشط 🟢</span>';
            const toggleBtnText = isLocked ? 'إلغاء القفل 🔓' : 'إعادة القفل 🔒';
            const toggleBtnClass = isLocked ? 'background:#10b981;' : 'background:#ef4444;';

            return `
                <tr ondblclick="openForm('operation-lock', '${item.id}')" oncontextmenu="event.preventDefault();deleteOperationLock('${item.id}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                    <td>${idx + 1}</td>
                    <td><code style="color:#60a5fa;font-weight:700;">${item.id}</code></td>
                    <td style="font-weight:700;color:#f8fafc;">${item.opType}</td>
                    <td style="font-size:0.85rem;color:#cbd5e1;">📅 ${item.startDate} إلى ${item.endDate}</td>
                    <td style="color:#94a3b8;font-size:0.85rem;">${item.reason}</td>
                    <td>${statusBadge}</td>
                    <td style="font-size:0.85rem;">👤 ${item.lockedBy}</td>
                    <td>
                        <button class="btn-sm" style="${toggleBtnClass}color:#fff;border:none;padding:4px 8px;border-radius:6px;cursor:pointer;font-weight:700;font-size:0.75rem;" onclick="toggleOperationLock('${item.id}')">${toggleBtnText}</button>
                    </td>
                </tr>
            `;
        }).join('');
    };

    window.saveOperationLockRule = function() {
        const typeEl = document.getElementById('lockOpType');
        const startEl = document.getElementById('lockStartDate');
        const endEl = document.getElementById('lockEndDate');
        const reasonEl = document.getElementById('lockReason');

        const opType = (typeEl ? typeEl.value : '').trim();
        const startDate = (startEl ? startEl.value : '').trim();
        const endDate = (endEl ? endEl.value : '').trim();
        const reason = (reasonEl ? reasonEl.value : '').trim();

        if (!opType || opType === 'اختر العملية المراد إقفالها' || opType === '') {
            toast('⚠️ يرجى اختيار نوع العملية المراد قفلها!', 1);
            if (typeEl) typeEl.focus();
            return;
        }

        if (!startDate) {
            toast('⚠️ يرجى تحديد تاريخ بداية فترة القفل!', 1);
            if (startEl) startEl.focus();
            return;
        }

        if (!endDate) {
            toast('⚠️ يرجى تحديد تاريخ نهاية فترة القفل!', 1);
            if (endEl) endEl.focus();
            return;
        }

        if (new Date(endDate) < new Date(startDate)) {
            toast('⚠️ تاريخ نهاية القفل لا يمكن أن يكون قبل تاريخ البداية!', 1);
            if (endEl) endEl.focus();
            return;
        }

        if (!reason) {
            toast('⚠️ يرجى كتابة سبب أو مسوغ قفل هذه العملية!', 1);
            if (reasonEl) reasonEl.focus();
            return;
        }

        const newRule = {
            id: 'LCK-2026-' + String((window.DB.operationLocks || []).length + 1).padStart(3, '0'),
            opType: opType,
            startDate: startDate,
            endDate: endDate,
            reason: reason,
            status: 'مقفل 🔒',
            lockedBy: window.me ? (window.me.name || window.me.username) : 'أ. خالد العنسي (المدير العام)',
            createdAt: new Date().toISOString().slice(0, 10)
        };

        window.DB.operationLocks.unshift(newRule);
        if (typeof addAudit === 'function') addAudit('قفل عمليات', `تطبيق قفل جديد على: ${opType} حتى ${endDate}`, 'قفل العمليات', 'تحذير نظام (WARNING) 🟡');

        toast(`🔒 تم تفعيل وحفظ قفل (${opType}) بنجاح!`);
        if (reasonEl) reasonEl.value = '';
        window.renderOperationLockGrid();
    };

    window.toggleOperationLock = function(id) {
        const item = (window.DB.operationLocks || []).find(x => x.id === id);
        if (!item) return;
        if (item.status.includes('مقفل') || item.status.includes('🔒')) {
            item.status = 'مفتوح ونشط 🟢';
            toast(`🔓 تم إلغاء قفل العملية (${item.opType}) بنجاح!`);
        } else {
            item.status = 'مقفل 🔒';
            toast(`🔒 تمت إعادة قفل العملية (${item.opType}) بنجاح!`);
        }
        window.renderOperationLockGrid();
    };

    window.deleteOperationLock = function(id) {
        const idx = (window.DB.operationLocks || []).findIndex(x => x.id === id);
        if (idx !== -1) {
            if (confirm(`❓ هل أنت متأكد من حذف قاعدة القفل (${id}) نهائياً؟`)) {
                window.DB.operationLocks.splice(idx, 1);
                toast(`🗑️ تم حذف قاعدة القفل بنجاح!`);
                window.renderOperationLockGrid();
            }
        }
    };
})();
