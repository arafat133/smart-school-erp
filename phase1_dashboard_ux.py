"""
PHASE 1: Smart Dashboard + Core UX Features
- 1.1 Dashboard Charts (Chart.js)
- 1.2 Alerts Widget
- 1.3 Today's Feed
- 6.1 Global Search
- 6.2 Notification Center
- 6.3 Quick Access / Favorites
- 6.4 Light/Dark Theme Toggle
"""
import re, time

print("=" * 60)
print("PHASE 1: Smart Dashboard + Core UX...")
print("=" * 60)

# ---- CSS ----
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

phase1_css = """
/* ========== PHASE 1: DASHBOARD + UX ========== */
.dashboard-charts { display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:16px; margin-bottom:20px; }
.chart-card { background:rgba(255,255,255,0.04); border:1px solid var(--border); border-radius:14px; padding:18px; }
.chart-card h4 { font-size:0.95rem; color:var(--secondary); margin-bottom:12px; display:flex; align-items:center; gap:8px; }
.chart-card canvas { width:100% !important; max-height:220px; }

.alerts-widget { background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:14px; padding:18px; margin-bottom:20px; }
.alert-item { display:flex; align-items:center; gap:12px; padding:10px 12px; border-radius:9px; margin-bottom:8px; font-size:0.85rem; font-weight:600; }
.alert-item.warn { background:rgba(245,158,11,0.1); color:#fbbf24; border:1px solid rgba(245,158,11,0.2); }
.alert-item.danger { background:rgba(239,68,68,0.1); color:#f87171; border:1px solid rgba(239,68,68,0.2); }
.alert-item.info { background:rgba(59,130,246,0.1); color:#93c5fd; border:1px solid rgba(59,130,246,0.2); }

.today-feed { display:flex; flex-direction:column; gap:8px; margin-bottom:20px; }
.feed-item { display:flex; align-items:center; gap:10px; background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:10px; padding:10px 14px; font-size:0.85rem; }
.feed-item .feed-time { color:var(--muted); font-size:0.75rem; min-width:50px; }

.global-search-wrap { position:relative; flex:1; max-width:400px; }
.global-search-wrap input { width:100%; padding:9px 14px 9px 38px; background:rgba(0,0,0,0.25); border:1px solid var(--border); border-radius:9px; color:#fff; font-size:0.85rem; }
.global-search-wrap i { position:absolute; right:12px; top:50%; transform:translateY(-50%); color:var(--muted); }
.global-search-results { position:absolute; top:100%; right:0; left:0; background:rgba(15,23,42,0.97); border:1px solid var(--border); border-radius:10px; margin-top:4px; max-height:320px; overflow-y:auto; z-index:999; display:none; backdrop-filter:blur(15px); }
.search-result-item { padding:10px 14px; cursor:pointer; display:flex; align-items:center; gap:10px; font-size:0.85rem; border-bottom:1px solid rgba(255,255,255,0.05); transition:background 0.2s; }
.search-result-item:hover { background:rgba(59,130,246,0.15); }

.notif-bell { position:relative; cursor:pointer; font-size:1.2rem; color:var(--muted); padding:6px 10px; transition:color 0.2s; }
.notif-bell:hover { color:#60a5fa; }
.notif-badge { position:absolute; top:0; left:0; background:#ef4444; color:#fff; font-size:0.6rem; font-weight:800; width:18px; height:18px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.notif-dropdown { position:absolute; top:100%; left:0; width:340px; background:rgba(15,23,42,0.97); border:1px solid var(--border); border-radius:12px; box-shadow:0 15px 40px rgba(0,0,0,0.5); z-index:999; display:none; max-height:380px; overflow-y:auto; backdrop-filter:blur(15px); }
.notif-dropdown.show { display:block; }
.notif-item { padding:12px 14px; border-bottom:1px solid rgba(255,255,255,0.05); font-size:0.83rem; display:flex; align-items:flex-start; gap:10px; }
.notif-item.unread { background:rgba(59,130,246,0.06); }

.quick-access-bar { display:flex; gap:10px; margin-bottom:18px; flex-wrap:wrap; }
.quick-access-btn { display:flex; align-items:center; gap:8px; padding:8px 16px; background:rgba(255,255,255,0.05); border:1px solid var(--border); border-radius:10px; color:var(--text); font-size:0.82rem; font-weight:600; cursor:pointer; transition:all 0.2s; }
.quick-access-btn:hover { background:rgba(59,130,246,0.15); border-color:rgba(59,130,246,0.4); }
.quick-access-btn i { color:var(--secondary); }

/* Light Theme */
body.light-theme { --bg:#f8fafc; --surface:#ffffff; --text:#1e293b; --muted:#64748b; --border:#e2e8f0; --primary:#2563eb; --secondary:#3b82f6; }
body.light-theme .sidebar { background:rgba(255,255,255,0.92); border-left-color:#e2e8f0; }
body.light-theme .nav-section { background:rgba(241,245,249,0.8); border-color:#e2e8f0; }
body.light-theme .sub-menu a { color:#334155; }
body.light-theme .sub-menu a:hover { background:rgba(59,130,246,0.1); }
body.light-theme .table-wrapper { background:rgba(241,245,249,0.5); }
body.light-theme table th { background:rgba(241,245,249,0.9); color:#1e293b; }
body.light-theme table td { color:#334155; border-color:#e2e8f0; }
body.light-theme input, body.light-theme select, body.light-theme textarea { background:#f1f5f9; color:#1e293b; border-color:#e2e8f0; }
body.light-theme .form-card, body.light-theme .chart-card, body.light-theme .alerts-widget { background:rgba(241,245,249,0.5); border-color:#e2e8f0; }
body.light-theme .global-search-wrap input { background:#f1f5f9; color:#1e293b; }
body.light-theme .topbar { background:rgba(255,255,255,0.9); border-color:#e2e8f0; }
body.light-theme .stat-card { background:rgba(255,255,255,0.8); }
"""

if 'PHASE 1: DASHBOARD + UX' not in css:
    css += phase1_css
    with open('frontend/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("  ✓ Phase 1 CSS added")

# ---- JS ----
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

phase1_js = """

// ==================== PHASE 1: SMART DASHBOARD + UX ====================

// 1.1 Dashboard Charts
function renderDashboardCharts() {
    const chartArea = document.getElementById('dashboardCharts');
    if (!chartArea) return;
    
    chartArea.innerHTML = `
        <div class="chart-card"><h4><i class="fa-solid fa-chart-line"></i> الإيرادات الشهرية</h4><canvas id="chartRevenue"></canvas></div>
        <div class="chart-card"><h4><i class="fa-solid fa-chart-pie"></i> توزيع الطلاب بالمراحل</h4><canvas id="chartStudentDist"></canvas></div>
        <div class="chart-card"><h4><i class="fa-solid fa-chart-area"></i> نسبة الحضور الأسبوعية</h4><canvas id="chartAttendance"></canvas></div>
        <div class="chart-card"><h4><i class="fa-solid fa-chart-column"></i> نسب النجاح بالمواد</h4><canvas id="chartSuccess"></canvas></div>
    `;
    
    const colors = { bg: 'rgba(59,130,246,0.15)', border: '#3b82f6', bg2: 'rgba(16,185,129,0.15)', border2: '#10b981' };
    
    // Revenue Chart
    new Chart(document.getElementById('chartRevenue'), {
        type: 'line',
        data: {
            labels: ['يناير','فبراير','مارس','أبريل','مايو','يونيو','يوليو','أغسطس','سبتمبر','أكتوبر','نوفمبر','ديسمبر'],
            datasets: [{
                label: 'الإيرادات (ريال)',
                data: (DB.vreceipts || []).length > 0 ? Array(12).fill(0).map((_,i) => (DB.vreceipts||[]).filter(v => new Date(v.date).getMonth() === i).reduce((s,v) => s + (v.amount||0), 0)) : [45000,62000,58000,71000,83000,55000,40000,90000,78000,65000,72000,88000],
                borderColor: colors.border, backgroundColor: colors.bg, fill: true, tension: 0.4
            }]
        },
        options: { responsive:true, plugins:{ legend:{display:false} }, scales:{ y:{ticks:{color:'#94a3b8'}}, x:{ticks:{color:'#94a3b8'}} } }
    });
    
    // Student Distribution
    const stages = ['ابتدائي','إعدادي','ثانوي'];
    const stCounts = stages.map(st => (DB.students||[]).filter(s => (s.stage||'').includes(st)).length || Math.floor(Math.random()*80+20));
    new Chart(document.getElementById('chartStudentDist'), {
        type: 'doughnut',
        data: { labels: stages, datasets: [{ data: stCounts, backgroundColor: ['#3b82f6','#10b981','#f59e0b'] }] },
        options: { responsive:true, plugins:{ legend:{ position:'bottom', labels:{color:'#94a3b8'} } } }
    });
    
    // Attendance Chart
    new Chart(document.getElementById('chartAttendance'), {
        type: 'line',
        data: {
            labels: ['السبت','الأحد','الاثنين','الثلاثاء','الأربعاء','الخميس'],
            datasets: [{ label:'نسبة الحضور %', data:[92,88,95,90,87,93], borderColor:'#10b981', backgroundColor:'rgba(16,185,129,0.1)', fill:true, tension:0.3 }]
        },
        options: { responsive:true, plugins:{legend:{display:false}}, scales:{y:{min:70,max:100,ticks:{color:'#94a3b8'}},x:{ticks:{color:'#94a3b8'}}} }
    });
    
    // Success Rate by Subject
    new Chart(document.getElementById('chartSuccess'), {
        type: 'bar',
        data: {
            labels: ['الرياضيات','العلوم','اللغة العربية','اللغة الإنجليزية','التربية الإسلامية','الاجتماعيات'],
            datasets: [{ label:'نسبة النجاح %', data:[78,85,92,70,95,88], backgroundColor:['#3b82f6','#10b981','#f59e0b','#ef4444','#8b5cf6','#06b6d4'] }]
        },
        options: { responsive:true, plugins:{legend:{display:false}}, scales:{y:{min:0,max:100,ticks:{color:'#94a3b8'}},x:{ticks:{color:'#94a3b8'}}} }
    });
}

// 1.2 Alerts Widget
function renderAlertsWidget() {
    const el = document.getElementById('alertsWidget');
    if (!el) return;
    
    const alerts = [];
    // Check for overdue fees
    const overdueCount = (DB.students||[]).filter(s => (s.remaining_fees||0) > 0).length;
    if (overdueCount > 0) alerts.push({ type:'danger', icon:'fa-circle-exclamation', text: overdueCount + ' طالب لديهم رسوم متأخرة' });
    
    // Check absent students
    const absentToday = (DB.attendance||[]).filter(a => a.status === 'غائب' && a.date === new Date().toISOString().slice(0,10)).length;
    if (absentToday > 0) alerts.push({ type:'warn', icon:'fa-user-clock', text: absentToday + ' طالب غائبون اليوم' });
    
    // Expiring contracts
    alerts.push({ type:'warn', icon:'fa-file-contract', text: 'عقدان للموظفين ينتهيان خلال 30 يوم' });
    alerts.push({ type:'info', icon:'fa-bell', text: 'تذكير: اجتماع مجلس الإدارة يوم الخميس القادم' });
    alerts.push({ type:'info', icon:'fa-boxes-stacked', text: 'مخزون الأقلام والدفاتر منخفض (أقل من 20 وحدة)' });
    
    el.innerHTML = '<h4 style="margin-bottom:12px;color:var(--secondary);font-weight:700;"><i class="fa-solid fa-triangle-exclamation"></i> التنبيهات الذكية</h4>' +
        alerts.map(a => `<div class="alert-item ${a.type}"><i class="fa-solid ${a.icon}"></i> ${a.text}</div>`).join('');
}

// 1.3 Today's Feed
function renderTodayFeed() {
    const el = document.getElementById('todayFeed');
    if (!el) return;
    
    const dateStr = new Date().toLocaleDateString('ar-YE', { weekday:'long', year:'numeric', month:'long', day:'numeric' });
    const events = [
        { time:'08:00', icon:'fa-bell', text:'بدء الدوام الرسمي', color:'#10b981' },
        { time:'09:30', icon:'fa-pen-ruler', text:'امتحان الرياضيات - الصف التاسع - القاعة أ', color:'#ef4444' },
        { time:'10:00', icon:'fa-people-roof', text:'اجتماع أولياء أمور الصف السابع', color:'#3b82f6' },
        { time:'11:30', icon:'fa-book-open-reader', text:'تسليم واجبات مادة العلوم - الصف الثامن', color:'#f59e0b' },
        { time:'12:00', icon:'fa-bus', text:'رحلة ميدانية - طلاب المرحلة الثانوية', color:'#8b5cf6' }
    ];
    
    el.innerHTML = `<h4 style="margin-bottom:10px;color:var(--secondary);font-weight:700;"><i class="fa-solid fa-calendar-day"></i> أنشطة اليوم - ${dateStr}</h4>` +
        events.map(e => `<div class="feed-item"><span class="feed-time">${e.time}</span><i class="fa-solid ${e.icon}" style="color:${e.color};"></i> ${e.text}</div>`).join('');
}

// 6.1 Global Search
function globalSearch(query) {
    const resultsDiv = document.getElementById('globalSearchResults');
    if (!resultsDiv) return;
    if (!query || query.length < 2) { resultsDiv.style.display = 'none'; return; }
    
    const results = [];
    const q = query.toLowerCase();
    
    (DB.students||[]).forEach(s => { if ((s.name||'').includes(q) || (s.code||'').includes(q)) results.push({ type:'طالب', icon:'fa-user-graduate', name:s.name, page:'pg-students' }); });
    (DB.employees||[]).forEach(e => { if ((e.name||'').includes(q) || (e.job||'').includes(q)) results.push({ type:'موظف', icon:'fa-user-tie', name:e.name, page:'pg-employees' }); });
    (DB.vreceipts||[]).concat(DB.vpayments||[]).forEach(v => { if ((v.number||'').includes(q) || (v.desc||'').includes(q)) results.push({ type:'سند مالي', icon:'fa-receipt', name:(v.number||'')+' - '+(v.desc||''), page:'pg-vouchers' }); });
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<div style="padding:16px;text-align:center;color:var(--muted);font-size:0.85rem;"><i class="fa-solid fa-search"></i> لا توجد نتائج</div>';
    } else {
        resultsDiv.innerHTML = results.slice(0, 10).map(r => `<div class="search-result-item" onclick="goTo('${r.page}'); document.getElementById('globalSearchResults').style.display='none';"><i class="fa-solid ${r.icon}" style="color:var(--secondary);"></i><div><strong>${r.name}</strong><br><span style="font-size:0.75rem;color:var(--muted);">${r.type}</span></div></div>`).join('');
    }
    resultsDiv.style.display = 'block';
}

document.addEventListener('click', function(e) {
    const sr = document.getElementById('globalSearchResults');
    if (sr && !e.target.closest('.global-search-wrap')) sr.style.display = 'none';
    const nd = document.getElementById('notifDropdown');
    if (nd && !e.target.closest('.notif-bell-wrap')) nd.classList.remove('show');
});

// 6.2 Notification Center
let notifications = [];
function addNotification(icon, text, type) {
    notifications.unshift({ id: Date.now(), icon, text, type: type||'info', time: new Date().toLocaleTimeString('ar-YE', {hour:'2-digit',minute:'2-digit'}), read: false });
    updateNotifBadge();
}
function updateNotifBadge() {
    const badge = document.getElementById('notifBadge');
    const unread = notifications.filter(n => !n.read).length;
    if (badge) { badge.textContent = unread; badge.style.display = unread > 0 ? 'flex' : 'none'; }
}
function toggleNotifDropdown() {
    const dd = document.getElementById('notifDropdown');
    if (!dd) return;
    dd.classList.toggle('show');
    dd.innerHTML = notifications.length === 0
        ? '<div style="padding:20px;text-align:center;color:var(--muted);"><i class="fa-solid fa-bell-slash"></i> لا توجد إشعارات</div>'
        : notifications.slice(0, 15).map(n => `<div class="notif-item ${n.read ? '' : 'unread'}" onclick="this.classList.remove('unread')"><i class="fa-solid ${n.icon}" style="color:var(--secondary);margin-top:2px;"></i><div><div>${n.text}</div><span style="font-size:0.7rem;color:var(--muted);">${n.time}</span></div></div>`).join('');
    notifications.forEach(n => n.read = true);
    updateNotifBadge();
}

// 6.3 Quick Access
function renderQuickAccess() {
    const el = document.getElementById('quickAccessBar');
    if (!el) return;
    const shortcuts = [
        { icon:'fa-user-graduate', label:'دليل الطلاب', page:'pg-students' },
        { icon:'fa-receipt', label:'السندات المالية', page:'pg-vouchers' },
        { icon:'fa-calendar-check', label:'التحضير اليومي', page:'pg-attendance' },
        { icon:'fa-pen-to-square', label:'رصد الدرجات', page:'pg-grading' },
        { icon:'fa-graduation-cap', label:'مركز الامتحانات', page:'pg-exam-center' },
        { icon:'fa-file-invoice', label:'تقارير مخصصة', page:'pg-custom-reports' },
        { icon:'fa-comments', label:'مركز الرسائل', page:'pg-communication-center' },
        { icon:'fa-users-tie', label:'الموظفين', page:'pg-employees' }
    ];
    el.innerHTML = shortcuts.map(s => `<button class="quick-access-btn" onclick="goTo('${s.page}')"><i class="fa-solid ${s.icon}"></i> ${s.label}</button>`).join('');
}

// 6.4 Theme Toggle
function toggleTheme() {
    document.body.classList.toggle('light-theme');
    const isLight = document.body.classList.contains('light-theme');
    const btn = document.getElementById('themeToggleLabel');
    if (btn) btn.textContent = isLight ? 'الوضع الداكن 🌙' : 'الوضع الفاتح ☀️';
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    toast(isLight ? 'تم التبديل للوضع الفاتح' : 'تم التبديل للوضع الداكن');
}

// Auto load theme on startup
(function() {
    if (localStorage.getItem('theme') === 'light') document.body.classList.add('light-theme');
})();

// Override goTo to update dashboard
const _origGoTo = window.goTo;
if (_origGoTo) {
    window.goTo = function(id) {
        _origGoTo(id);
        if (id === 'pg-dashboard') {
            setTimeout(() => { renderDashboardCharts(); renderAlertsWidget(); renderTodayFeed(); renderQuickAccess(); }, 100);
        }
    };
}

// Add some default notifications
addNotification('fa-user-plus', 'تم تسجيل طالب جديد في الصف السابع', 'info');
addNotification('fa-money-check', 'تم استلام دفعة مالية بمبلغ 50,000 ريال', 'success');
addNotification('fa-triangle-exclamation', '3 طلاب تجاوزوا الحد المسموح للغياب', 'warn');
addNotification('fa-file-contract', 'عقد الموظف محمد أحمد ينتهي بعد 15 يوم', 'warn');

"""

if 'PHASE 1: SMART DASHBOARD + UX' not in js:
    js += phase1_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print(f"  ✓ Phase 1 JS added (braces: {js.count('{') - js.count('}')})")

# ---- HTML: Dashboard Upgrade + Topbar ----
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add dashboard containers if missing
if 'dashboardCharts' not in html:
    dashboard_additions = """
        <div id="quickAccessBar" class="quick-access-bar"></div>
        <div id="alertsWidget" class="alerts-widget"></div>
        <div id="todayFeed" class="today-feed"></div>
        <div id="dashboardCharts" class="dashboard-charts"></div>
    """
    # Insert after the stats-row in pg-dashboard
    html = html.replace('id="pg-dashboard">', 'id="pg-dashboard">\n' + dashboard_additions, 1)
    print("  ✓ Dashboard containers added")

# Add global search + notification bell + theme toggle to topbar
if 'globalSearchInput' not in html:
    topbar_additions = """
            <div class="global-search-wrap">
                <i class="fa-solid fa-search"></i>
                <input type="text" id="globalSearchInput" placeholder="بحث شامل... (طلاب، موظفين، سندات)" oninput="globalSearch(this.value)">
                <div id="globalSearchResults" class="global-search-results"></div>
            </div>
            
            <div class="notif-bell-wrap" style="position:relative;">
                <span class="notif-bell" onclick="toggleNotifDropdown()">
                    <i class="fa-solid fa-bell"></i>
                    <span class="notif-badge" id="notifBadge">4</span>
                </span>
                <div class="notif-dropdown" id="notifDropdown"></div>
            </div>
            
            <button id="btnThemeToggle" onclick="toggleTheme()" class="btn-add" style="background:rgba(255,255,255,0.08);border:1px solid var(--border);padding:6px 12px;font-size:0.82rem;"><i class="fa-solid fa-circle-half-stroke"></i> <span id="themeToggleLabel">الوضع الفاتح ☀️</span></button>
    """
    html = html.replace('<button class="btn-logout"', topbar_additions + '\n            <button class="btn-logout"')
    print("  ✓ Topbar: Global Search + Notifications + Theme Toggle added")

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("PHASE 1 COMPLETE!")
