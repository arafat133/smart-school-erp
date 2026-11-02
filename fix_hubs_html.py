import re
import time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

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
            <h2><i class="fa-solid fa-comments"></i> مركز الرسائل والاتصالات الموحد</h2>
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

# Insert pages into school.html
if 'pg-exam-center' not in html:
    html = html.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + exam_center_page + '\n' + comm_center_page + '\n' + inventory_center_page)

# Add sidebar links
if 'pg-exam-center' not in html or 'مركز الامتحانات والكنترول' not in html:
    sidebar_links = """
            <a href="#" onclick="goTo('pg-exam-center')"><i class="fa-solid fa-graduation-cap"></i> <span>مركز الامتحانات والكنترول</span></a>
            <a href="#" onclick="goTo('pg-communication-center')"><i class="fa-solid fa-comments"></i> <span>مركز الرسائل والاتصالات</span></a>
            <a href="#" onclick="goTo('pg-inventory-center')"><i class="fa-solid fa-boxes-stacked"></i> <span>مركز المخازن والمشتريات</span></a>
"""
    html = html.replace('<a href="#" onclick="goTo(\'pg-students\')">', sidebar_links + '            <a href="#" onclick="goTo(\'pg-students\')">')

ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as fh:
    fh.write(html)
    
admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as fh:
    fh.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as fh:
    fh.write(parent_html)

print("Successfully injected all hub pages and sidebar links!")
