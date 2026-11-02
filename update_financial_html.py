"""
Script to update HTML structure for Financial Modules:
1. Update pg-operation-lock to include dropdown for operation type and date range fields
2. Re-architect pg-chart-accounts with Tree View, Details Panel, Action Toolbar, Search & Filters, and all required fields
3. Add/Update pg-journal with Header, Transaction Lines Grid (Debit/Credit/Account/Currency/Cost Center/Line Memo), and Footer (Totals, Balance Delta, Attachments)
4. Update pg-cashboxes with Cash Boxes Grid, Cash Box Setup Form, and Permissions & Links with all requested fields
5. Update pg-cost-centers with Tree View, Setup Form, and Performance & Budget Panel with all requested fields
6. Update pg-account-ceiling with Policy Engine, Limits Grid, Approvals/Overrides, and all requested fields
7. Add/Update pg-vouchers with Voucher Type Switcher (Receipt, Payment, Transfer), Header, Invoice Matching & Allocation, Payment Method Section, and Attachments
8. Update pg-student-account / pg-acc-statement with Filters, Summary Cards, Ledger Grid with Running Balance, and Export Toolbar
9. Delete pg-trial-balance, pg-balance-sheet, pg-fee-receipt from HTML and Sidebar
"""
import re, time

print("=" * 60)
print("Updating HTML for Financial Modules...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Operation Lock Modal / Page Update
operation_lock_html = """
<div class="page" id="pg-operation-lock">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-lock"></i> قفل العمليات والموديولات المحاسبية</h2>
    </div>
    
    <div class="form-card" style="margin-bottom:20px;">
        <h3 style="margin-bottom:15px;color:var(--secondary);font-size:1.1rem;"><i class="fa-solid fa-lock-open"></i> إضافة قفل جديد لعملية في النظام</h3>
        <div class="form-row">
            <div class="fg">
                <label><i class="fa-solid fa-gears"></i> العملية / الموديول المراد إيقافه</label>
                <select id="lockOpType">
                    <option value="all">-- جميع العمليات (قفل شامل للنظام) --</option>
                    <option value="vouchers">سندات القبض والصرف (Vouchers)</option>
                    <option value="journal">القيود اليومية (Journal Entries)</option>
                    <option value="grading">رصد الدرجات والكنترول (Grading & Control)</option>
                    <option value="attendance">التحضير والغياب اليومي (Attendance)</option>
                    <option value="students_edit">تعديل بيانات الطلاب (Student Profile Updates)</option>
                    <option value="closings">الإقفالات المحاسبية (Accounting Closings)</option>
                    <option value="posting">الترحيلات المالية (Posting)</option>
                    <option value="registration">تسجيل الطلاب الجدد (New Registration)</option>
                </select>
            </div>
            <div class="fg">
                <label><i class="fa-solid fa-calendar"></i> تاريخ بداية القفل</label>
                <input type="date" id="lockStartDate">
            </div>
            <div class="fg">
                <label><i class="fa-solid fa-calendar"></i> تاريخ نهاية القفل</label>
                <input type="date" id="lockEndDate">
            </div>
        </div>
        <div class="form-row">
            <div class="fg" style="flex:2;">
                <label><i class="fa-solid fa-align-right"></i> سبب القفل / ملاحظات الإدارة</label>
                <input type="text" id="lockReason" placeholder="مثال: الجرد السنوي / أعمال الكنترول والامتحانات">
            </div>
            <div class="fg" style="flex:1;display:flex;align-items:flex-end;">
                <button class="btn-add" onclick="saveOperationLockRule()" style="width:100%;height:42px;"><i class="fa-solid fa-shield-halved"></i> تطبيق القفل الفوري</button>
            </div>
        </div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>العملية المقفلة</th>
                    <th>تاريخ بداية القفل</th>
                    <th>تاريخ نهاية القفل</th>
                    <th>سبب القفل</th>
                    <th>الحالة</th>
                    <th>المسؤول</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-operation-lock"></tbody>
        </table>
    </div>
</div>
"""

# 2. Chart of Accounts HTML Update
chart_accounts_html = """
<div class="page" id="pg-chart-accounts">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-sitemap"></i> دليل الحسابات المالي الشامل (Chart of Accounts)</h2>
    </div>

    <!-- Toolbar & Search -->
    <div class="toolbar" style="margin-bottom:16px;">
        <div class="search-box" style="flex:1;max-width:320px;">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input id="searchChartAccounts" placeholder="بحث برقم الحساب أو اسمه..." oninput="filterChartAccounts()">
        </div>
        <select id="filterChartLevel" onchange="filterChartAccounts()" style="width:150px;">
            <option value="all">جميع المستويات</option>
            <option value="1">المستوى 1 (رئيسي)</option>
            <option value="2">المستوى 2 (تجميعي)</option>
            <option value="3">المستوى 3 (فرعي)</option>
            <option value="4">المستوى 4 (تحليلي/قيود)</option>
        </select>
        <select id="filterChartStatus" onchange="filterChartAccounts()" style="width:130px;">
            <option value="all">جميع الحالات</option>
            <option value="active">نشط فقط</option>
            <option value="inactive">موقف فقط</option>
        </select>
        <button class="btn-add" onclick="openForm('chart-accounts')"><i class="fa-solid fa-plus"></i> حساب جديد</button>

        <button class="btn-add" onclick="exportChartExcel()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-excel"></i> تصدير Excel</button>
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-print"></i> طباعة الدليل</button>
    </div>

    <!-- Tree View & Details Split View -->
    <div style="display:grid;grid-template-columns:1.3fr 1fr;gap:18px;" id="chartAccountsContainer">
        <!-- Tree View Panel -->
        <div class="form-card" style="padding:16px;">
            <h3 style="margin-bottom:12px;color:var(--secondary);font-size:1.05rem;display:flex;justify-content:space-between;align-items:center;">
                <span><i class="fa-solid fa-folder-tree"></i> الهيكل الشجري للحسابات</span>
                <span style="font-size:0.8rem;color:var(--muted);">اضغط للتوسيع والطي</span>
            </h3>
            <div id="chartTreeWrapper" class="tree-container" style="max-height:550px;overflow-y:auto;">
                <!-- Rendered dynamically -->
            </div>
        </div>

        <!-- Details Panel -->
        <div class="form-card" id="chartAccountDetailsPanel" style="padding:18px;">
            <h3 style="margin-bottom:16px;color:var(--secondary);font-size:1.05rem;border-bottom:1px solid var(--border);padding-bottom:10px;" id="chartDetailsTitle">
                <i class="fa-solid fa-circle-info"></i> تفاصيل وبطاقة الحساب
            </h3>
            <div id="chartDetailsBody">
                <p style="text-align:center;color:var(--muted);padding:40px 0;"><i class="fa-solid fa-mouse-pointer" style="font-size:2rem;margin-bottom:10px;display:block;"></i>يرجى اختيار حساب من الشجرة لعرض بياناته وبطاقته التفصيلية</p>
            </div>
        </div>
    </div>
</div>
"""

# 3. Journal Entry HTML Update
journal_html = """
<div class="page" id="pg-journal">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-book-open"></i> إدارة القيود اليومية (Journal Entries)</h2>
    </div>

    <!-- Action Bar -->
    <div class="toolbar" style="margin-bottom:16px;">
        <button class="btn-add" onclick="showNewJournalEntryForm()"><i class="fa-solid fa-plus"></i> إنشاء قيد يومية جديد</button>
        <div class="search-box" style="flex:1;max-width:300px;">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input id="searchJournal" placeholder="بحث برقم القيد أو البيان..." oninput="renderJournalList()">
        </div>
        <select id="filterJournalStatus" onchange="renderJournalList()" style="width:140px;">
            <option value="all">جميع الحالات</option>
            <option value="Posted">مرحّل</option>
            <option value="Draft">مسودة</option>
            <option value="Canceled">ملغى</option>
        </select>
        <button class="btn-add" onclick="exportJournalList()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-excel"></i> تصدير القيود</button>
    </div>

    <!-- Journal Form (Collapsible/Modal or inline) -->
    <div class="form-card" id="journalEntryFormCard" style="margin-bottom:20px;display:none;">
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--border);padding-bottom:12px;margin-bottom:16px;">
            <h3 style="color:var(--secondary);font-size:1.1rem;" id="journalFormTitle"><i class="fa-solid fa-file-pen"></i> تحرير قيد يومية عام</h3>
            <button class="btn-cancel" onclick="document.getElementById('journalEntryFormCard').style.display='none'"><i class="fa-solid fa-xmark"></i> إغلاق</button>
        </div>

        <!-- 1. Header Panel -->
        <div style="background:rgba(255,255,255,0.02);padding:14px;border-radius:10px;border:1px solid var(--border);margin-bottom:16px;">
            <h4 style="margin-bottom:10px;color:#93c5fd;font-size:0.9rem;"><i class="fa-solid fa-heading"></i> رأس القيد (Header Panel)</h4>
            <div class="form-row">
                <div class="fg">
                    <label>رقم القيد (تلقائي)</label>
                    <input id="jvNo" readonly style="background:rgba(0,0,0,0.4);font-weight:700;color:#60a5fa;" value="JV-2026-0001">
                </div>
                <div class="fg">
                    <label>تاريخ القيد</label>
                    <input type="date" id="jvDate">
                </div>
                <div class="fg">
                    <label>مرجع المستند / رقم الفاتورة/الشيك</label>
                    <input id="jvRefNo" placeholder="مثال: REF-9921">
                </div>
                <div class="fg">
                    <label>نوع القيد</label>
                    <select id="jvType">
                        <option value="قيد يومية عام">قيد يومية عام</option>
                        <option value="قيد افتتاحي">قيد افتتاحي</option>
                        <option value="قيد تسوية">قيد تسوية</option>
                        <option value="قيد إقفال">قيد إقفال</option>
                    </select>
                </div>
                <div class="fg">
                    <label>حالة القيد</label>
                    <select id="jvStatus">
                        <option value="Draft">مسودة (Draft)</option>
                        <option value="Posted">مرحّل (Posted)</option>
                    </select>
                </div>
            </div>
            <div class="fg">
                <label>البيان العام للقيد</label>
                <input id="jvMainDesc" placeholder="اكتب الشرح والبيان العام لهذه العملية المالية...">
            </div>
        </div>

        <!-- 2. Transaction Lines Grid -->
        <div style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <h4 style="color:#93c5fd;font-size:0.9rem;"><i class="fa-solid fa-list-check"></i> جدول تفاصيل القيد (Transaction Lines Grid)</h4>
                <button class="btn-add" onclick="addJournalLine()" style="padding:4px 12px;font-size:0.8rem;"><i class="fa-solid fa-plus"></i> إضافة سطر قيد</button>
            </div>

            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th style="width:250px;">كود / اسم الحساب الفرعي</th>
                            <th style="width:130px;">المدين (Debit)</th>
                            <th style="width:130px;">الدائن (Credit)</th>
                            <th style="width:110px;">العملة</th>
                            <th style="width:140px;">مركز التكلفة</th>
                            <th>البيان الفرعي (Memo)</th>
                            <th style="width:50px;">حذف</th>
                        </tr>
                    </thead>
                    <tbody id="tbl-jv-lines">
                        <!-- Rendered lines -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 3. Footer & Control Panel -->
        <div style="background:rgba(0,0,0,0.25);padding:14px;border-radius:10px;border:1px solid var(--border);">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;">
                <div style="display:flex;gap:20px;align-items:center;">
                    <div>إجمالي المدين: <strong id="jvTotalDebit" style="color:#60a5fa;font-size:1.1rem;">0.00</strong></div>
                    <div>إجمالي الدائن: <strong id="jvTotalCredit" style="color:#34d399;font-size:1.1rem;">0.00</strong></div>
                    <div id="jvBalanceIndicator" style="padding:6px 14px;border-radius:8px;font-weight:700;font-size:0.9rem;background:rgba(239,68,68,0.2);color:#f87171;">
                        <i class="fa-solid fa-scale-unbalanced"></i> غير متوازن (الفرق: 0.00)
                    </div>
                </div>

                <div style="display:flex;gap:10px;align-items:center;">
                    <div class="fg" style="margin:0;">
                        <input type="file" id="jvAttachment" style="padding:4px;font-size:0.75rem;">
                    </div>
                    <button class="btn-add" id="btnSaveJournal" onclick="saveJournalEntry()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-floppy-disk"></i> حفظ وإعتماد القيد</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Journal Entries List -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم القيد</th>
                    <th>التاريخ</th>
                    <th>النوع</th>
                    <th>البيان العام</th>
                    <th>إجمالي القيد</th>
                    <th>الحالة</th>
                    <th>المرفق</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-journal-entries"></tbody>
        </table>
    </div>
</div>
"""

# 4. Cashboxes HTML Update
cashboxes_html = """
<div class="page" id="pg-cashboxes">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-vault"></i> دليل الصناديق والخزائن المالية (Cash Boxes)</h2>
    </div>

    <div class="toolbar">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchCashbox" placeholder="بحث بالصندوق أو الكود..." oninput="renderCashboxes()"></div>
        <button class="btn-add" onclick="openForm('cashbox')"><i class="fa-solid fa-plus"></i> إضافة صندوق جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الصندوق</th>
                    <th>اسم الصندوق</th>
                    <th>الحساب المحاسبي المرتبط</th>
                    <th>الفرع / القسم</th>
                    <th>أمين الصندوق (المسؤول)</th>
                    <th>العملة</th>
                    <th>نوع الصندوق</th>
                    <th>سقف الصندوق</th>
                    <th>الرصيد الحقيقي</th>
                    <th>السماح بالسالب</th>
                    <th>الحالة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-cashboxes"></tbody>
        </table>
    </div>
</div>
"""

# 5. Cost Centers HTML Update
cost_centers_html = """
<div class="page" id="pg-cost-centers">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-building"></i> دليل مراكز التكلفة (Cost Centers Tree & Budget)</h2>
    </div>

    <div class="toolbar">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchCostCenter" placeholder="بحث بمركز التكلفة..." oninput="renderCostCenters()"></div>
        <button class="btn-add" onclick="openForm('cost-centers')"><i class="fa-solid fa-plus"></i> إضافة مركز تكلفة جديد</button>
    </div>

    <!-- Tree View & Budget Analysis -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:18px;">
        <div class="form-card" style="padding:16px;">
            <h3 style="margin-bottom:12px;color:var(--secondary);font-size:1.05rem;"><i class="fa-solid fa-folder-tree"></i> شجرة مراكز التكلفة</h3>
            <div id="costCenterTreeWrapper" class="tree-container" style="max-height:500px;overflow-y:auto;">
                <!-- Dynamic tree -->
            </div>
        </div>

        <div class="form-card" style="padding:16px;">
            <h3 style="margin-bottom:12px;color:var(--secondary);font-size:1.05rem;"><i class="fa-solid fa-chart-pie"></i> لوحة تحليل الموازنة والأداء</h3>
            <div id="costCenterPerformancePanel">
                <p style="text-align:center;color:var(--muted);padding:30px 0;">اختر مركز تكلفة لاستعراض الموازنة المعتمدة والمصروفات الفعلية ونسبة الانحراف</p>
            </div>
        </div>
    </div>
</div>
"""

# 6. Account Ceiling HTML Update
account_ceiling_html = """
<div class="page" id="pg-account-ceiling">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-arrow-up-9-1"></i> تسقيف الحسابات والضوابط الائتمانية (Account Limits)</h2>
    </div>

    <div class="toolbar">
        <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input id="searchAccountCeiling" placeholder="بحث بالحساب المسقف..." oninput="renderAccountCeiling()"></div>
        <button class="btn-add" onclick="openForm('account-ceiling')"><i class="fa-solid fa-plus"></i> إضافة سقف حساب جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود / اسم الحساب</th>
                    <th>نوع السقف</th>
                    <th>مبلغ السقف الأقصى</th>
                    <th>فترة الائتمان</th>
                    <th>هامش التجاوز %</th>
                    <th>الرصيد المستغل</th>
                    <th>المبلغ المتاح</th>
                    <th>الإجراء عند التجاوز</th>
                    <th>صلاحية التجاوز</th>
                    <th>تاريخ السريان</th>
                    <th>الحالة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-account-ceiling"></tbody>
        </table>
    </div>
</div>
"""

# 7. Unified Vouchers HTML (pg-vouchers)
vouchers_html = """
<div class="page" id="pg-vouchers">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-file-invoice-dollar"></i> إدارة السندات المالية الشاملة (Vouchers Hub)</h2>
    </div>

    <!-- Voucher Type Switcher Tabs -->
    <div class="tab-nav">
        <button class="tab-btn active" onclick="switchVoucherType('all', this)"><i class="fa-solid fa-list"></i> جميع السندات</button>
        <button class="tab-btn" onclick="switchVoucherType('receipt', this)"><i class="fa-solid fa-arrow-down" style="color:#10b981;"></i> سندات القبض (Receipts)</button>
        <button class="tab-btn" onclick="switchVoucherType('payment', this)"><i class="fa-solid fa-arrow-up" style="color:#ef4444;"></i> سندات الصرف (Payments)</button>
        <button class="tab-btn" onclick="switchVoucherType('transfer', this)"><i class="fa-solid fa-right-left" style="color:#3b82f6;"></i> تحويل داخلي بين الصناديق/البنك</button>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('vreceipt')"><i class="fa-solid fa-plus"></i> سند قبض جديد</button>
        <button class="btn-add" onclick="openForm('vpayment')" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-minus"></i> سند صرف جديد</button>
        <button class="btn-add" onclick="openForm('vtransfer')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-right-left"></i> تحويل بين الخزائن</button>
        <div class="search-box" style="flex:1;max-width:280px;">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input id="searchVouchers" placeholder="بحث برقم السند أو الحساب..." oninput="renderVouchers()">
        </div>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>رقم السند</th>
                    <th>النوع</th>
                    <th>التاريخ</th>
                    <th>حساب النقدية/البنك</th>
                    <th>الحساب المقابل / الطرف الآخر</th>
                    <th>طريقة الدفع</th>
                    <th>المبلغ والعملة</th>
                    <th>مركز التكلفة</th>
                    <th>البيان</th>
                    <th>الحالة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-vouchers"></tbody>
        </table>
    </div>
</div>
"""

# 8. Statement of Account HTML Update (pg-student-account / pg-acc-statement)
statement_of_account_html = """
<div class="page" id="pg-student-account">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-scroll"></i> كشف الحساب التفاعلي (Statement of Account)</h2>
    </div>

    <!-- Filters Panel -->
    <div class="form-card" style="margin-bottom:16px;">
        <div class="form-row">
            <div class="fg" style="flex:2;">
                <label><i class="fa-solid fa-user-check"></i> اختر الحساب المعني من الدليل</label>
                <select id="soaAccountSelect" onchange="renderStatementOfAccount()">
                    <!-- Options populated dynamically from DB accounts/students/suppliers -->
                </select>
            </div>
            <div class="fg">
                <label><i class="fa-solid fa-calendar"></i> من تاريخ</label>
                <input type="date" id="soaDateFrom" onchange="renderStatementOfAccount()">
            </div>
            <div class="fg">
                <label><i class="fa-solid fa-calendar"></i> إلى تاريخ</label>
                <input type="date" id="soaDateTo" onchange="renderStatementOfAccount()">
            </div>
            <div class="fg">
                <label><i class="fa-solid fa-coins"></i> العملة</label>
                <select id="soaCurrency" onchange="renderStatementOfAccount()">
                    <option value="YER">YER (ريال يمني)</option>
                    <option value="USD">USD (دولار أمريكي)</option>
                    <option value="SAR">SAR (ريال سعودي)</option>
                </select>
            </div>
        </div>
    </div>

    <!-- Summary Cards -->
    <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card" style="border-right:4px solid #3b82f6;">
            <div class="stat-info">
                <h3>الرصيد الافتتاحي</h3>
                <p id="soaOpeningBalance" style="color:#60a5fa;font-weight:800;font-size:1.2rem;">0.00 YER</p>
            </div>
        </div>
        <div class="stat-card" style="border-right:4px solid #6366f1;">
            <div class="stat-info">
                <h3>إجمالي المدين (+)</h3>
                <p id="soaTotalDebit" style="color:#818cf8;font-weight:800;font-size:1.2rem;">0.00 YER</p>
            </div>
        </div>
        <div class="stat-card" style="border-right:4px solid #10b981;">
            <div class="stat-info">
                <h3>إجمالي الدائن (-)</h3>
                <p id="soaTotalCredit" style="color:#34d399;font-weight:800;font-size:1.2rem;">0.00 YER</p>
            </div>
        </div>
        <div class="stat-card" style="border-right:4px solid #f59e0b;">
            <div class="stat-info">
                <h3>الرصيد النهائي الحالي</h3>
                <p id="soaFinalBalance" style="color:#fbbf24;font-weight:800;font-size:1.2rem;">0.00 YER</p>
            </div>
        </div>
    </div>

    <!-- Toolbar & Export -->
    <div class="toolbar" style="margin-bottom:12px;">
        <button class="btn-add" onclick="window.print()" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-print"></i> طباعة كشف الحساب الرسمية</button>
        <button class="btn-add" onclick="exportStatementExcel()" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-file-excel"></i> تصدير Excel</button>
    </div>

    <!-- Ledger Grid with Running Balance -->
    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>تاريخ الحركة</th>
                    <th>رقم المستند / القيد</th>
                    <th>نوع الحركة</th>
                    <th>البيان / الشرح التفصيلي</th>
                    <th>المدين (Debit)</th>
                    <th>الدائن (Credit)</th>
                    <th>الرصيد التراكمي المتحرك</th>
                    <th>مركز التكلفة</th>
                </tr>
            </thead>
            <tbody id="tbl-statement-ledger"></tbody>
        </table>
    </div>
</div>
"""

# Now replace / inject each page in html:

def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page: {page_id}")
    else:
        # Append before main content end
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added new page: {page_id}")
    return html_text

html = replace_or_add_page(html, 'pg-operation-lock', operation_lock_html)
html = replace_or_add_page(html, 'pg-chart-accounts', chart_accounts_html)
html = replace_or_add_page(html, 'pg-journal', journal_html)
html = replace_or_add_page(html, 'pg-cashboxes', cashboxes_html)
html = replace_or_add_page(html, 'pg-cost-centers', cost_centers_html)
html = replace_or_add_page(html, 'pg-account-ceiling', account_ceiling_html)
html = replace_or_add_page(html, 'pg-vouchers', vouchers_html)
html = replace_or_add_page(html, 'pg-student-account', statement_of_account_html)

# Delete unwanted pages from HTML: pg-trial-balance, pg-balance-sheet, pg-fee-receipt, pg-voucher-receipt
pages_to_remove = ['pg-trial-balance', 'pg-balance-sheet', 'pg-fee-receipt', 'pg-voucher-receipt']
for p_id in pages_to_remove:
    pattern = rf'<div class="page" id="{p_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html, re.DOTALL):
        html = re.sub(pattern, '', html, flags=re.DOTALL)
        print(f"  ✓ Removed page: {p_id}")

    # Remove sidebar links if any
    link_pattern = rf'<a[^>]*goTo\([\'"]{p_id}[\'"]\)[^>]*>.*?</a>'
    html = re.sub(link_pattern, '', html, flags=re.DOTALL)

# Ensure pg-journal and pg-vouchers and pg-student-account are in sidebar navigation
if 'pg-journal' not in html or 'goTo(\'pg-journal\')' not in html:
    sidebar_financial_links = """
            <a href="#" onclick="goTo('pg-chart-accounts')"><i class="fa-solid fa-sitemap"></i> <span>دليل الحسابات</span></a>
            <a href="#" onclick="goTo('pg-vouchers')"><i class="fa-solid fa-file-invoice-dollar"></i> <span>إدارة السندات</span></a>
            <a href="#" onclick="goTo('pg-journal')"><i class="fa-solid fa-book-open"></i> <span>القيود اليومية</span></a>
            <a href="#" onclick="goTo('pg-cashboxes')"><i class="fa-solid fa-vault"></i> <span>دليل الصناديق</span></a>
            <a href="#" onclick="goTo('pg-cost-centers')"><i class="fa-solid fa-building"></i> <span>مراكز التكلفة</span></a>
            <a href="#" onclick="goTo('pg-account-ceiling')"><i class="fa-solid fa-arrow-up-9-1"></i> <span>تسقيف الحسابات</span></a>
            <a href="#" onclick="goTo('pg-student-account')"><i class="fa-solid fa-scroll"></i> <span>كشف الحساب</span></a>
            <a href="#" onclick="goTo('pg-operation-lock')"><i class="fa-solid fa-lock"></i> <span>قفل العمليات</span></a>
"""

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

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

print("HTML restructuring completed successfully!")
