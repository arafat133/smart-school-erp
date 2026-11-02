/**
 * ============================================================================
 * MODULE: SETTINGS-ALERTS.JS - System Settings, Alerts Engine & Digital Archive
 * ============================================================================
 */

// System Settings Grid Renderer
(function initSystemSettingsModule() {
    if (!window.DB) window.DB = {};
    if (!window.DB.systemSettingsData) {
        window.DB.systemSettingsData = [
            { keyId: 'SYS_UI_PRIMARY_COLOR', nameArEn: 'اللون الرئيسي للواجهة | Primary Theme Color', scope: 'المظهر والتصميم (UI & Branding)', val: '#1E40AF (أزرق ملكي سحابي)', type: 'منتقي ألوان (Color Picker)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. خالد العنسي (المدير العام)', lastTs: '2026-08-18 10:00 ص' },
            { keyId: 'SYS_SESSION_TIMEOUT_MINS', nameArEn: 'مهلة إغلاق الجلسة التلقائي | Session Inactivity Timeout', scope: 'الأمان والحماية (Security)', val: '15 دقيقة خمول (Auto Logout)', type: 'قائمة اختيار رقمية (Select Box)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. خالد العنسي (مدير النظام)', lastTs: '2026-08-18 09:30 ص' },
            { keyId: 'SYS_AUTO_BACKUP_CRON', nameArEn: 'جدول النسخ الاحتياطي التلقائي | Database Auto Backup Schedule', scope: 'قواعد البيانات والأرشفة (Database)', val: '0 2 * * * (يومياً الساعة 02:00 AM)', type: 'مجدول أوامر (Cron Picker)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'د. سالم باعباد (مدير التقنية)', lastTs: '2026-08-17 11:15 م' },
            { keyId: 'SYS_MAINTENANCE_MODE', nameArEn: 'وضع الصيانة والترقية العامة | Global Maintenance Mode', scope: 'حالة النظام والتشغيل (System Health)', val: 'غير مفعل (النظام يعمل حياً 🟢)', type: 'مفتاح تبديل سيادي (Toggle Switch)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. خالد العنسي (المدير العام)', lastTs: '2026-08-16 04:45 م' },
            { keyId: 'SYS_MFA_ENFORCED', nameArEn: 'فرض التوثيق الثنائي للقيادة | MFA 2-Factor Enforcement', scope: 'الأمان والحماية (Security)', val: 'مفعل إجباري للإدارة والمالية 🛡️', type: 'مفتاح تبديل أمني (Security Toggle)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. عبد الرحمن باعباد (المدير المالي)', lastTs: '2026-08-15 02:20 م' },
            { keyId: 'SYS_CURRENCY_PRIMARY', nameArEn: 'العملة الأساسية للمعاملات | Primary Base Currency', scope: 'الشؤون المالية (ERP Accounting)', val: 'YER (ريال يمني معتمد)', type: 'قائمة العملات المصرفية (Currency Select)', timeout: '15 دقيقة خمول', backupCron: 'يومياً الساعة 02:00 AM 🟢', maintenance: 'غير مفعل (System Live) 🟢', lastBy: 'أ. سارة المحاسبة', lastTs: '2026-08-14 01:10 م' }
        ];
    }

    window.renderSystemSettingsGrid = function() {
        const tb = document.getElementById('tbl-system-settings-grid');
        if (!tb) return;

        const searchInput = document.getElementById('searchSystemSettings') || document.getElementById('searchSettings');
        const q = searchInput ? searchInput.value.trim().toLowerCase() : '';

        const settingsList = window.DB.systemSettingsData || [];
        const filtered = settingsList.filter(s => {
            if (!q) return true;
            const k = (s.keyId || '').toLowerCase();
            const n = (s.nameArEn || s.settingName || '').toLowerCase();
            const c = (s.scope || s.category || '').toLowerCase();
            const v = (s.val || '').toLowerCase();
            return k.includes(q) || n.includes(q) || c.includes(q) || v.includes(q);
        });

        if (filtered.length === 0) {
            tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;">لا توجد إعدادات مطابقة للبحث</td></tr>';
            return;
        }

        tb.innerHTML = filtered.map(s => `
            <tr ondblclick="openForm('system_settings', '${s.keyId}')" oncontextmenu="event.preventDefault();deleteItem('systemSettingsData', '${s.keyId}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td style="font-weight:800;color:#60a5fa;font-family:monospace;font-size:0.85rem;"><i class="fa-solid fa-gear" style="margin-left:6px;color:#38bdf8;"></i>${s.keyId}</td>
                <td style="font-weight:700;color:#f8fafc;">${s.nameArEn}</td>
                <td><span class="badge badge-info" style="font-size:0.75rem;">${s.scope}</span></td>
                <td style="font-weight:700;color:#34d399;">${s.val}</td>
                <td style="font-size:0.78rem;color:var(--muted);">${s.type}</td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${s.timeout}</td>
                <td style="font-size:0.78rem;color:var(--muted);font-family:monospace;">${s.backupCron}</td>
                <td><span class="badge badge-success">${s.maintenance}</span></td>
                <td style="font-size:0.82rem;">👤 ${s.lastBy}</td>
                <td style="font-size:0.78rem;color:var(--muted);white-space:nowrap;">📅 ${s.lastTs}</td>
            </tr>
        `).join('');
    };

    window.renderSystemSettings = window.renderSystemSettingsGrid;
})();

// Alerts Engine Renderer
(function initAlertsModule() {
    if (!window.DB) window.DB = {};
    if (!window.DB.alertsData) {
        window.DB.alertsData = [
            { id: 'alt_1', title: 'تنبيه الغياب الصباحي التلقائي', trigger: 'تسجيل غياب طالب بدون عذر مقبول', channel: 'إشعار تطبيق (Push) + SMS', template: 'عزيزي ولي الأمر، تم تسجيل غياب ابنكم {اسم_الطالب} اليوم {التاريخ}.', targetAudience: 'أولياء الأمور', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (148 رسالة) 🟢', executionTime: '⏱️ يومياً 08:30 ص', gatewayCost: '0.02 YER' },
            { id: 'alt_2', title: 'تذكير استحقاق الأقساط والرسوم', trigger: 'باقي 5 أيام على موعد استحقاق القسط', channel: 'SMS + WhatsApp API 🟢', template: 'عزيزي ولي الأمر، نود تذكيركم بحلول موعد قسط {اسم_الطالب} بمبلغ {المبلغ}.', targetAudience: 'أولياء الأمور', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (52 رسالة) 🟢', executionTime: '⏱️ يومياً 09:00 ص', gatewayCost: '0.02 YER' },
            { id: 'alt_3', title: 'إشعار اعتماد ونشر النتائج النهائية', trigger: 'اعتماد نتائج الفصل الدراسي بالكنترول', channel: 'إشعار تطبيق (Push) + SMS', template: 'تم اعتماد ونشر نتائج الفصل الدراسي لـ {اسم_الطالب}. اضغط للمعاينة.', targetAudience: 'أولياء الأمور والطلاب', status: 'نشط ومفعل 🟢', deliveryLog: 'تم التوصيل بنجاح (450 إشعار) 🟢', executionTime: '⏱️ فوري عند الاعتماد', gatewayCost: '0.01 YER' }
        ];
    }

    window.renderAlertsGrid = function() {
        const el = document.getElementById('tbl-alerts-grid');
        if (!el) return;

        const q = (document.getElementById('searchAlerts')?.value || '').toLowerCase();
        const data = (window.DB.alertsData || []).filter(a =>
            !q || (a.title || '').toLowerCase().includes(q) || (a.trigger || '').toLowerCase().includes(q) || (a.channel || '').toLowerCase().includes(q)
        );

        if (data.length === 0) {
            el.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:30px;">لا توجد قواعد تنبيه مطابقة للبحث</td></tr>';
            return;
        }

        el.innerHTML = data.map((a, i) => `
            <tr ondblclick="openForm('alerts', '${a.id}')" oncontextmenu="event.preventDefault();deleteItem('alertsData', '${a.id}')" title="💡 انقر مرتين للتعديل، أو اضغط مطولاً للحذف">
                <td>${i + 1}</td>
                <td style="font-weight:700;color:#60a5fa;"><i class="fa-solid fa-bell" style="margin-left:6px;color:#38bdf8;"></i>${a.title}</td>
                <td><span class="badge badge-info">${a.trigger}</span></td>
                <td><span class="badge badge-success">${a.channel}</span></td>
                <td style="color:#cbd5e1;font-size:0.8rem;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="${a.template}">${a.template}</td>
                <td><span class="badge badge-primary">${a.targetAudience}</span></td>
                <td><span class="badge badge-success">${a.status}</span></td>
                <td><span class="badge badge-info">${a.deliveryLog}</span></td>
                <td style="font-size:0.8rem;color:#cbd5e1;">${a.executionTime}</td>
                <td><span class="badge badge-secondary">${a.gatewayCost}</span></td>
            </tr>
        `).join('');
    };

    window.renderAlerts = window.renderAlertsGrid;
})();
