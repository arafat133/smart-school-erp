"""
Rebuild HTML containers for currencies, cashbox-inventory, closings, banks, demand-letters in school.html
"""
import re, time

print("=" * 60)
print("Rebuilding HTML containers for 5 Financial Interfaces...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Rebuild pg-currencies
currencies_html = """
<div class="page" id="pg-currencies">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-money-bill-transfer"></i> واجهة دليل العملات وأسعار الصرف (Currencies & Exchange Rates)</h2>
    </div>

    <!-- Live Rates Dashboard KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>العملة الأساسية للنظام</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">ريال يمني (YER)</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>سعر الصرف الرسمي (USD)</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">1 USD = 530 YER 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info"><h3>سعر صرف الريال السعودي (SAR)</h3><p style="color:#fbbf24;font-weight:800;font-size:1.2rem;">1 SAR = 140 YER 🟢</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchCurrencies" placeholder="ابحث بكود العملة، الاسم، أو الرمز..." oninput="renderCurrenciesGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('currencies')"><i class="fa-solid fa-plus"></i> إضافة عملة جديدة وسعر صرف</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة دليل العملات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود العملة الدولي (ISO)</th>
                    <th>اسم العملة (AR / EN)</th>
                    <th>رمز العملة والطباعة</th>
                    <th>هل العملة أساسية؟</th>
                    <th>سعر الصرف الرسمي</th>
                    <th>سعر الشراء والبيع التفصيلي</th>
                    <th>تاريخ وساعة التحديث</th>
                    <th>عدد الخانات العشرية</th>
                    <th>حساب فروق الصرف (Gain/Loss)</th>
                    <th>حالة التفعيل</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-currencies-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Rebuild pg-cashbox-inventory
cashbox_inv_html = """
<div class="page" id="pg-cashbox-inventory">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><div style="display:inline;"><i class="fa-solid fa-cash-register"></i> واجهة جرد الصناديق النقدية والخزائن (Cash Drawer Audit)</div></h2>
    </div>

    <!-- Audit KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي الجرد النقدي هذا الشهر</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">3,745,000 YER</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>نسبة المطابقة الدفترية</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">99.6% (مطابق) 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>إجمالي فروقات العجز الموجهة</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">5,000 YER 🔴</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchCashboxInventory" placeholder="ابحث بكود محضر الجرد، الصندوق، أو أمين الخزينة..." oninput="renderCashboxInventoryGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('cashbox_inventory')"><i class="fa-solid fa-calculator"></i> إجراء محضر جرد نقدي جديد</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف محاضر الجرد</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود عملية الجرد</th>
                    <th>الصندوق / الخزينة الخاضعة للجرد</th>
                    <th>تاريخ ووقت الجرد الفعلي</th>
                    <th>الرصيد الدفتري المسجل</th>
                    <th>الجرد الفعلي التفصيلي</th>
                    <th>قيمة ونوع الفرق (الفارق)</th>
                    <th>أمين الصندوق المسؤول</th>
                    <th>رئيس لجنة الجرد والمراجع</th>
                    <th>توجيه فرق الجرد (حساب التسوية)</th>
                    <th>حالة المحضر والاعتماد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-cashbox-inventory-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. Rebuild pg-closings
closings_html = """
<div class="page" id="pg-closings">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-folder-closed"></i> واجهة الإقفالات المحاسبية وإغلاق الفترات (Period-End Closures)</h2>
    </div>

    <!-- Closures KPI Status Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>حالة الفترات المالية</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">الفترة 08 مغلقة ومقفلة 🔒</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>نتيجة فحص ما قبل الإقفال</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">سليم وجاهز (0 معلقات) 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>صافي الفائض التشغيلي المرحّل</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">+ 12,450,000 YER</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchClosings" placeholder="ابحث بكود الإقفال، اسم الفترة، أو نوع الإغلاق..." oninput="renderClosingsGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="executePeriodClosing()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-lock"></i> تنفيذ قيد الإقفال الشهري/السنوي الآلي</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف الإقفالات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود عملية الإقفال</th>
                    <th>اسم ونطاق الفترة المحاسبية</th>
                    <th>نوع الإقفال (شهري / ختامي)</th>
                    <th>نتيجة فحص ما قبل الإقفال</th>
                    <th>رقم قيد الإقفال الآلي</th>
                    <th>صافي نتيجة النشاط (ربح/خسارة)</th>
                    <th>حالة قفل الفترة</th>
                    <th>المحاسب المنفذ</th>
                    <th>تاريخ وختم الإقفال بالدفاتر</th>
                    <th>السنة المالية الجديدة المستهدفة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-closings-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Rebuild pg-banks
banks_html = """
<div class="page" id="pg-banks">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-building-columns"></i> واجهة دليل البنوك والحسابات المصرفية (Bank Accounts Directory)</h2>
    </div>

    <!-- Bank Overview KPI Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي الرصيد الدفتري بالبنوك</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">45,200,000 YER</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>عدد الحسابات المصرفية النشطة</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">3 حسابات معتمدة 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #8b5cf6;">
            <div class="stat-info"><h3>دفتر الشيكات النشط</h3><p style="color:#c084fc;font-weight:800;font-size:1.2rem;">5001 إلى 5100</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchBanks" placeholder="ابحث بكود الحساب، البنك، رقم الحساب، أو IBAN..." oninput="renderBanksGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('banks')"><i class="fa-solid fa-plus"></i> إضافة حساب بنكي جديد وربط شجرة الحسابات</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة دليل البنوك</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الحساب البنكي بالنظام</th>
                    <th>اسم البنك والفرع</th>
                    <th>رقم الحساب المصرفي</th>
                    <th>رقم الآيبان (IBAN) والرمز السويفت</th>
                    <th>الحساب المحاسبي المرتبط بالشجرة</th>
                    <th>عملة الحساب</th>
                    <th>الرصيد الدفتري الحالي</th>
                    <th>نوع الحساب البنكي</th>
                    <th>تسلسل دفتر الشيكات النشط</th>
                    <th>حالة الحساب البنكي</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-banks-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. Rebuild pg-demand-letters
demand_letters_html = """
<div class="page" id="pg-demand-letters">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-envelope-open-text"></i> واجهة رسائل المطالبة المالية وإشعارات المتأخرات (Dunning Letters)</h2>
    </div>

    <!-- Dunning KPI Status Cards -->
    <div class="stats-row" style="margin-bottom:14px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info"><h3>إجمالي المتأخرات المطالب بها</h3><p style="color:#60a5fa;font-weight:800;font-size:1.2rem;">450,000 YER</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info"><h3>معدل استجابة أولياء الأمور</h3><p style="color:#34d399;font-weight:800;font-size:1.2rem;">84.2% تم السداد 🟢</p></div>
        </div>
        <div class="stat-card" style="border-right:4px solid #ef4444;">
            <div class="stat-info"><h3>مطالبات تصعيدية (إنذار نهائي)</h3><p style="color:#f87171;font-weight:800;font-size:1.2rem;">2 إشعار تصعيدي 🔴</p></div>
        </div>
    </div>

    <div class="toolbar" style="justify-content:space-between;display:flex;flex-wrap:wrap;gap:10px;">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchDemandLetters" placeholder="ابحث بكود المطالبة، ولي الأمر، الطالب، أو المستوى..." oninput="renderDemandLettersGrid()"></div>
        <div style="display:flex;gap:8px;">
            <button class="btn-add" onclick="openForm('demand_letters')"><i class="fa-solid fa-paper-plane"></i> إصدار إشعار مطالبة مالية جديد</button>
            <button class="btn-add" onclick="triggerOfficialPrint()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة كشف المطالبات</button>
        </div>
    </div>
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود إشعار المطالبة</th>
                    <th>اسم ولي الأمر / الملتزم سداداً</th>
                    <th>اسم الطالب والمرحلة الدراسية</th>
                    <th>مستوى المطالبة والتصعيد</th>
                    <th>إجمالي المبلغ المتأخر</th>
                    <th>عدد أيام التأخير</th>
                    <th>قناة التوصيل</th>
                    <th>رابط الدفع السريع (Direct Pay)</th>
                    <th>حالة الرسالة والتفاعل</th>
                    <th>تاريخ الإرسال والموعد النهائي</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-demand-letters-grid"></tbody>
        </table>
    </div>
</div>
"""

pages_replacements = [
    ('pg-currencies', currencies_html),
    ('pg-cashbox-inventory', cashbox_inv_html),
    ('pg-closings', closings_html),
    ('pg-banks', banks_html),
    ('pg-demand-letters', demand_letters_html)
]

for pid, new_h in pages_replacements:
    pattern = rf'<div class="page" id="{pid}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    html = re.sub(pattern, new_h.strip() + '\n', html, flags=re.DOTALL)
    print(f"  ✓ Updated {pid} in school.html")

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

print(f"Updated HTML files with timestamp v={ts}!")
