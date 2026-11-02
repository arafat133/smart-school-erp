"""
Python script to update/re-architect Administrative Tools modules in school.html:
- pg-admin-messages (الرسائل الإدارية والإعلانات)
- pg-shortcuts (اختصارات النظام المفضلة)
- pg-faq (الأسئلة المتكررة والدعم الفني)
- pg-dictionary (قاموس الترجمة والمصطلحات)
- pg-personal-info (معلومات الملف الشخصي)
"""
import re, time

print("=" * 60)
print("Updating Administrative Tools Modules in school.html...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_or_add_page(html_text, page_id, new_content):
    pattern = rf'<div class="page" id="{page_id}">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
    if re.search(pattern, html_text, re.DOTALL):
        html_text = re.sub(pattern, new_content.strip() + '\n', html_text, flags=re.DOTALL)
        print(f"  ✓ Updated page content for: {page_id}")
    else:
        html_text = html_text.replace('<!-- ========== MAIN CONTENT ========== -->', '<!-- ========== MAIN CONTENT ========== -->\n' + new_content.strip())
        print(f"  ✓ Added page content for: {page_id}")
    return html_text

# 1. Administrative Messages & Announcements (pg-admin-messages)
admin_messages_html = """
<div class="page" id="pg-admin-messages">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-tower-broadcast"></i> الرسائل الإدارية والتعاميم والإعلانات الرسمية</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('admin-messages')" style="background:linear-gradient(135deg,#ef4444,#dc2626);"><i class="fa-solid fa-bullhorn"></i> صياغة تعميم / إعلان إداري جديد</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الإعلان</th>
                    <th>عنوان القرار والتعميم</th>
                    <th>تصنيف الإعلان</th>
                    <th>الجمهور المستهدف</th>
                    <th>محتوى وتفاصيل التعميم</th>
                    <th>الملفات المرفقة</th>
                    <th>مستوى الأهمية</th>
                    <th>فترة النشر والانتهاء</th>
                    <th>إحصائيات القراءة والتفاعل</th>
                    <th>مصدر الإعلان / الناشر</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-admin-messages-grid"></tbody>
        </table>
    </div>
</div>
"""

# 2. Favorite Shortcuts (pg-shortcuts)
shortcuts_html = """
<div class="page" id="pg-shortcuts">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-keyboard"></i> اختصارات النظام المفضلة والوصول السريع</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('shortcuts')"><i class="fa-solid fa-plus"></i> إضافة اختصار جديد للوحة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود الاختصار</th>
                    <th>عنوان الاختصار والشاشة</th>
                    <th>الموديول التابع</th>
                    <th>المسار / دالة التشغيل</th>
                    <th>رمز الأيقونة واللون</th>
                    <th>اختصار لوحة المفاتيح (Hotkey)</th>
                    <th>التصنيف الشخصي</th>
                    <th>ترتيب الظهور</th>
                    <th>معدل الاستخدام</th>
                    <th>حالة التثبيت</th>
                    <th>تشغيل سريع</th>
                </tr>
            </thead>
            <tbody id="tbl-shortcuts-grid"></tbody>
        </table>
    </div>
</div>
"""

# 3. FAQ & Support Helpdesk (pg-faq)
faq_html = """
<div class="page" id="pg-faq">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-circle-question"></i> الأسئلة المتكررة ومركز تذاكر الدعم الفني</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('support-ticket')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-headset"></i> رفع تذكرة دعم فني جديدة</button>
        <button class="btn-add" onclick="openForm('faq-article')" style="background:linear-gradient(135deg,#10b981,#059669);"><i class="fa-solid fa-plus"></i> إضافة سؤال ودليل معرفة</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود المقال / التذكرة</th>
                    <th>تصنيف القسم والموديول</th>
                    <th>عنوان السؤال / المشكلة</th>
                    <th>خطوات الحل / دليل الاستخدام</th>
                    <th>درجة الأهمية / الأولوية</th>
                    <th>حالة تذكرة الدعم</th>
                    <th>مُرسل التذكرة</th>
                    <th>الفني المسؤول</th>
                    <th>الملفات المرفقة</th>
                    <th>تقييم جودة الخدمة</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-faq-grid"></tbody>
        </table>
    </div>
</div>
"""

# 4. Translation & Terms Dictionary (pg-dictionary)
dictionary_html = """
<div class="page" id="pg-dictionary">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-language"></i> قاموس الترجمة والمصطلحات المعيارية للنظام</h2>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('dictionary')"><i class="fa-solid fa-plus"></i> إضافة مصطلح قاموس جديد</button>
        <button class="btn-add" onclick="toast('تم تصدير ملف الترجمة المجمّع i18n.json بنجاح')" style="background:linear-gradient(135deg,#3b82f6,#2563eb);"><i class="fa-solid fa-download"></i> تصدير القاموس (JSON/CSV)</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود المصطلح (Key)</th>
                    <th>المصطلح بالعربية (Primary)</th>
                    <th>الترجمة بالإنجليزي (English)</th>
                    <th>التصنيف والقسم</th>
                    <th>السياق وملاحظات الاستخدام</th>
                    <th>قناة الترجمة</th>
                    <th>حالة الاعتماد اللغوي</th>
                    <th>تاريخ آخر تحديث</th>
                    <th>المراجع اللغوي</th>
                    <th>القاموس المعتمد</th>
                    <th>إجراءات</th>
                </tr>
            </thead>
            <tbody id="tbl-dictionary-grid"></tbody>
        </table>
    </div>
</div>
"""

# 5. User Personal Profile Info (pg-personal-info)
personal_info_html = """
<div class="page" id="pg-personal-info">
    <div class="page-header">
        <button class="btn-back" onclick="goTo('pg-dashboard')"><i class="fa-solid fa-arrow-right"></i></button>
        <h2><i class="fa-solid fa-address-card"></i> معلومات الملف الشخصي وأمان الحساب</h2>
    </div>

    <!-- Personal Info Card & Security Panel -->
    <div style="background:rgba(15,23,42,0.85);border:1px solid rgba(59,130,246,0.3);padding:20px;border-radius:14px;margin-bottom:16px;">
        <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px;">
            <div style="width:70px;height:70px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#1d4ed8);display:flex;align-items:center;justify-content:center;font-size:2rem;color:#fff;font-weight:800;">خ</div>
            <div>
                <h3 style="margin:0;color:#fff;font-size:1.3rem;">أ. خالد محمود العنسي</h3>
                <p style="margin:4px 0 0 0;color:#60a5fa;font-weight:700;">مسؤول الكنترول والامتحانات - إدارة الشؤون الأكاديمية (USR-2026-0104)</p>
            </div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;font-size:0.9rem;color:#cbd5e1;">
            <div>📧 البريد: <strong>k.alansi@school.edu.ye</strong></div>
            <div>📱 الجوال: <strong>770000000</strong></div>
            <div>🌐 المظهر واللغة: <strong>اللغة العربية | المظهر الداكن</strong></div>
            <div>🔐 التوثيق الثنائي: <span style="color:#10b981;font-weight:700;">مفعل (2FA Active)</span></div>
        </div>
    </div>

    <div class="toolbar">
        <button class="btn-add" onclick="openForm('change-password')" style="background:linear-gradient(135deg,#f59e0b,#d97706);"><i class="fa-solid fa-key"></i> تغيير كلمة المرور</button>
        <button class="btn-add" onclick="openForm('personal-info')"><i class="fa-solid fa-user-pen"></i> تحديث بيانات الملف الشخصي</button>
    </div>

    <div class="table-wrapper">
        <table>
            <thead>
                <tr>
                    <th>كود / رقم المستخدم</th>
                    <th>الاسم الكامل</th>
                    <th>المسمى الوظيفي والدور</th>
                    <th>القسم / الإدارة</th>
                    <th>البريد الإلكتروني الرسمي</th>
                    <th>رقم الجوال المعتمد</th>
                    <th>لغة ومظهر النظام</th>
                    <th>حالة التوثيق الثنائي (2FA)</th>
                    <th>الجلسات النشطة والأجهزة</th>
                    <th>حالة الحساب</th>
                    <th>إجراءات الأمان</th>
                </tr>
            </thead>
            <tbody id="tbl-personal-info-grid"></tbody>
        </table>
    </div>
</div>
"""

# Replace or Add each page in school.html
html = replace_or_add_page(html, 'pg-admin-messages', admin_messages_html)
html = replace_or_add_page(html, 'pg-shortcuts', shortcuts_html)
html = replace_or_add_page(html, 'pg-faq', faq_html)
html = replace_or_add_page(html, 'pg-dictionary', dictionary_html)
html = replace_or_add_page(html, 'pg-personal-info', personal_info_html)

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

print("Administrative Tools HTML update completed successfully!")
