"""
Python script to append Activities & Transport logic in frontend/app.js
"""
import re, time

print("=" * 60)
print("Updating app.js with Activities & Transport Logic...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

act_trans_db_additions = """
// Data collections for Activities & Transportation modules
if (!DB.activitiesGridData) DB.activitiesGridData = [
    { id: 'ACT-2026-015', name: 'نادي الروبوت والذكاء الاصطناعي', type: 'نشاط علمي / تكنولوجي', supervisor: 'م. حسام العنسي (قسم الحاسوب)', maxCap: '25 طالباً', target: 'الثاني والثالث الثانوي', dates: '2026-09-01 - 2026-11-15', venue: 'معمل الابتكار - المبنى الرئيسي', fee: 50, budget: 500, status: 'مفتوح للتسجيل' },
    { id: 'ACT-2026-018', name: 'بطولة كرة القدم السنوية', type: 'نشاط رياضي', supervisor: 'أ. ياسر سعيد (التربية الرياضية)', maxCap: '60 طالباً', target: 'جميع المراحل الثانوية', dates: '2026-10-01 - 2026-10-20', venue: 'الملعب الرياضي الرئيسي', fee: 0, budget: 300, status: 'جارٍ التنفيذ' }
];

if (!DB.transportRoutesGridData) DB.transportRoutesGridData = [
    { id: 'ROUTE-0103', name: 'خط حدة - الأصبحي - الحي السياسي', startEnd: 'الانطلاق: شارع حدة -> الوصول: المجمع', stops: 12, bus: 'حافلة رقم (08) - سعة 30', crew: 'السائق: علي العنسي', duration: '45 دقيقة', schedule: 'صباحاً: 06:30 ص / إياباً: 01:30 م', fee: 200, capacity: '24 / 30 مقعداً (متوفر 6)', status: 'نشط (Active)' }
];

if (!DB.busesGridData) DB.busesGridData = [
    { id: 'BUS-2026-008', plate: '12345-أ / نقل خاص', model: 'تويوتا كوستر (Toyota Coaster) - 2024', capacity: '30 مقعداً', fuel: 'ديزل (Diesel)', route: 'خط حدة - الأصبحي (ROUTE-0103)', crew: 'السائق: علي العنسي', odo: '45,200 كم', docStatus: 'التأمين: سارٍ حتى 2026-12-31', gpsStatus: 'متصل (Online - GP-883)', status: 'في الخدمة (Active)' }
];

if (!DB.transportEnrollmentGridData) DB.transportEnrollmentGridData = [
    { id: 'SUB-BUS-2026-042', student: 'عبدالرحمن محمد علي - الثاني الثانوي (2026104)', route: 'خط حدة - الأصبحي (ROUTE-0103)', stop: 'محطة (5) - المقطري بجوار جولة حدة', type: 'اتجاهين (ذهاب وإياب) - اشتراك سنوي', busCrew: 'حافلة رقم (08)', fee: 200, payStatus: 'مسدد بالكامل', status: 'نشط (Active)', qrCode: 'QR-PASS-042' }
];

if (!DB.transportManifestGridData) DB.transportManifestGridData = [
    { id: 'TRP-RPT-2026-88', routeBus: 'خط حدة (ROUTE-0103) - حافلة (08)', reportType: 'كشف ركاب يومي / تقرير الرسوم', student: 'عبدالرحمن محمد علي - الثاني الثانوي (2026104)', stop: 'محطة (5) - المقطري بجوار جولة حدة', fee: 200, paidBalance: 'المسدد: 150 $ | المتبقي: 50 $', payStatus: 'مسدد جزئياً', occupancy: '80% (24 مقعد مستغل من 30)', crewSign: 'السائق: علي العنسي' }
];
"""

act_trans_modules_js = """

// ==================== 1. ACTIVITIES MANAGEMENT ====================
function renderActivitiesGrid() {
    const tb = document.getElementById('tbl-activities-grid');
    if (!tb) return;

    const list = DB.activitiesGridData || [];
    tb.innerHTML = list.map(a => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${a.id}</td>
            <td style="font-weight:700;">${a.name}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${a.type}</span></td>
            <td>${a.supervisor}</td>
            <td style="font-weight:700;color:#34d399;">${a.maxCap}</td>
            <td>${a.target}</td>
            <td style="font-size:0.8rem;">${a.dates}</td>
            <td>${a.venue}</td>
            <td style="font-weight:700;color:#fbbf24;">${a.fee} $</td>
            <td style="font-weight:800;color:#34d399;">${a.budget} $</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${a.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('activities', ${JSON.stringify(a).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 2. TRANSPORT ROUTES ====================
function renderTransportRoutesGrid() {
    const tb = document.getElementById('tbl-transport-routes-grid');
    if (!tb) return;

    const list = DB.transportRoutesGridData || [];
    tb.innerHTML = list.map(r => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${r.id}</td>
            <td style="font-weight:700;">${r.name}</td>
            <td style="font-size:0.83rem;">${r.startEnd}</td>
            <td style="font-weight:700;color:#34d399;">${r.stops} محطات</td>
            <td>${r.bus}</td>
            <td>${r.crew}</td>
            <td>${r.duration}</td>
            <td style="font-size:0.8rem;">${r.schedule}</td>
            <td style="font-weight:800;color:#fbbf24;">${r.fee} $</td>
            <td style="font-size:0.83rem;font-weight:700;color:#60a5fa;">${r.capacity}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${r.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('transport-routes', ${JSON.stringify(r).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}

function openRouteMapModal() {
    const fields = document.getElementById('form-fields') || document.getElementById('dynamicForm');
    const title = document.getElementById('formTitle');
    if (!fields || !title) return;

    title.innerHTML = '<i class="fa-solid fa-map-location-dot"></i> الخريطة التفاعلية لمسارات ومحطات خط حدة - الأصبحي';
    fields.innerHTML = `
        <div style="background:rgba(15,23,42,0.9);border:1px solid rgba(59,130,246,0.3);padding:15px;border-radius:12px;color:#fff;margin-bottom:12px;">
            <div style="font-weight:700;color:#60a5fa;margin-bottom:8px;"><i class="fa-solid fa-route"></i> مسار خط حدة (12 محطة توقف):</div>
            <div style="display:flex;flex-direction:column;gap:6px;font-size:0.85rem;">
                <div>📍 محطة 1: شارع حدة - البداية (06:30 ص)</div>
                <div>📍 محطة 2: جولة الفروي (06:36 ص)</div>
                <div>📍 محطة 3: عمارة البريد (06:42 ص)</div>
                <div>📍 محطة 5: المقطري بجوار جولة حدة (06:50 ص)</div>
                <div>📍 محطة 12: الصرح التعليمي - النهاية (07:15 ص)</div>
            </div>
        </div>
        <button class="btn-cancel" onclick="document.getElementById('formModal').classList.remove('active');" style="width:100%;"><i class="fa-solid fa-xmark"></i> إغلاق الخريطة</button>
    `;
    document.getElementById('formModal').classList.add('active');
}


// ==================== 3. BUSES & FLEET MANAGEMENT ====================
function renderBusesGrid() {
    const tb = document.getElementById('tbl-buses-grid');
    if (!tb) return;

    const list = DB.busesGridData || [];
    tb.innerHTML = list.map(b => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${b.id}</td>
            <td style="font-weight:800;color:#fbbf24;">${b.plate}</td>
            <td>${b.model}</td>
            <td style="font-weight:700;color:#34d399;">${b.capacity}</td>
            <td>${b.fuel}</td>
            <td>${b.route}</td>
            <td>${b.crew}</td>
            <td>${b.odo}</td>
            <td style="font-size:0.8rem;">${b.docStatus}</td>
            <td style="color:#10b981;font-weight:700;"><i class="fa-solid fa-wifi"></i> ${b.gpsStatus}</td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${b.status}</span></td>
            <td><div class="act"><button class="btn-edit" onclick="openForm('buses', ${JSON.stringify(b).replace(/"/g, '&quot;')})"><i class="fa-solid fa-pen"></i></button></div></td>
        </tr>
    `).join('');
}


// ==================== 4. STUDENT TRANSPORT ENROLLMENT ====================
function renderTransportEnrollmentGrid() {
    const tb = document.getElementById('tbl-transport-enrollment-grid');
    if (!tb) return;

    const list = DB.transportEnrollmentGridData || [];
    tb.innerHTML = list.map(e => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${e.id}</td>
            <td style="font-weight:700;">${e.student}</td>
            <td>${e.route}</td>
            <td style="font-size:0.83rem;">${e.stop}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${e.type}</span></td>
            <td>${e.busCrew}</td>
            <td style="font-weight:800;color:#34d399;">${e.fee} $</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(16,185,129,0.15);color:#10b981;">${e.payStatus}</span></td>
            <td><span style="padding:3px 8px;border-radius:6px;font-size:0.75rem;font-weight:700;background:rgba(16,185,129,0.15);color:#10b981;">${e.status}</span></td>
            <td><a href="#" onclick="toast('معاينة بطاقة صعود الحافلة QR')" style="color:#38bdf8;font-size:0.8rem;"><i class="fa-solid fa-qrcode"></i> ${e.qrCode}</a></td>
            <td><button class="btn-edit" onclick="toast('طباعة Bus Pass فردي')"><i class="fa-solid fa-print"></i> كرت</button></td>
        </tr>
    `).join('');
}


// ==================== 5. TRANSPORT MANIFESTS & ANALYTICS ====================
function renderTransportManifestGrid() {
    const tb = document.getElementById('tbl-transport-manifest-grid');
    if (!tb) return;

    const list = DB.transportManifestGridData || [];
    tb.innerHTML = list.map(m => `
        <tr>
            <td style="font-weight:700;color:#60a5fa;">${m.id}</td>
            <td style="font-weight:700;">${m.routeBus}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(59,130,246,0.15);color:#93c5fd;">${m.reportType}</span></td>
            <td style="font-weight:700;">${m.student}</td>
            <td style="font-size:0.83rem;">${m.stop}</td>
            <td style="font-weight:700;color:#60a5fa;">${m.fee} $</td>
            <td style="font-size:0.8rem;font-weight:700;color:#fbbf24;">${m.paidBalance}</td>
            <td><span style="padding:2px 6px;border-radius:4px;font-size:0.75rem;background:rgba(245,158,11,0.15);color:#fbbf24;">${m.payStatus}</span></td>
            <td style="font-weight:800;color:#34d399;">${m.occupancy}</td>
            <td style="font-size:0.8rem;">${m.crewSign}</td>
            <td><button class="btn-edit" onclick="toast('معاينة كشف الركاب التفصيلي PDF')"><i class="fa-solid fa-file-pdf"></i> PDF</button></td>
        </tr>
    `).join('');
}
"""

if 'ACTIVITIES & TRANSPORTATION MODULES' not in js:
    js += act_trans_db_additions + "\n" + act_trans_modules_js

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Appended Activities & Transport logic in app.js successfully!")
