"""
COMPREHENSIVE: Add icons to ALL tabs, h3/h4 headers, and buttons 
that are missing icons across school.html and app.js
"""
import re, time, sys

# Read files
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

changes_html = 0
changes_js = 0

# ======================================================
# 1. Add icons to ALL table header cells (th) - these are the "tabs" detected
# ======================================================
# Map common Arabic header texts to appropriate FA icons
th_icon_map = {
    'رقم المدرسة': 'fa-solid fa-hashtag',
    'اسم المدرسة': 'fa-solid fa-school',
    'الحالة': 'fa-solid fa-circle-info',
    'نهاية الاشتراك': 'fa-solid fa-calendar-xmark',
    'عدد المستخدمين': 'fa-solid fa-users',
    'إجراءات': 'fa-solid fa-ellipsis-vertical',
    'اسم المستخدم': 'fa-solid fa-user',
    'الدور': 'fa-solid fa-user-tag',
    'التاريخ': 'fa-solid fa-calendar',
    'المستخدم': 'fa-solid fa-user-circle',
    'العملية': 'fa-solid fa-cog',
    'التفاصيل': 'fa-solid fa-info-circle',
    'المرحلة': 'fa-solid fa-layer-group',
    'الصف': 'fa-solid fa-graduation-cap',
    'الترتيب': 'fa-solid fa-sort',
    'اسم الشعبة': 'fa-solid fa-object-group',
    'السعة': 'fa-solid fa-users-viewfinder',
    'الصورة': 'fa-solid fa-image',
    'الرقم': 'fa-solid fa-hashtag',
    'اسم الطالب': 'fa-solid fa-user-graduate',
    'الهاتف': 'fa-solid fa-phone',
    'الجنس': 'fa-solid fa-venus-mars',
    'تاريخ الميلاد': 'fa-solid fa-cake-candles',
    'الحالة المالية': 'fa-solid fa-coins',
    'الطالب': 'fa-solid fa-user-graduate',
    'السنة الدراسية': 'fa-solid fa-calendar-days',
    'الشعبة': 'fa-solid fa-object-group',
    'الرسوم': 'fa-solid fa-money-bill',
    'المسدد': 'fa-solid fa-check-circle',
    'حضور وغياب': 'fa-solid fa-calendar-check',
    'الكود': 'fa-solid fa-barcode',
    'اسم المادة': 'fa-solid fa-book',
    'الدرجة العظمى': 'fa-solid fa-arrow-up',
    'الدرجة الصغرى': 'fa-solid fa-arrow-down',
    'اسم الموظف': 'fa-solid fa-user-tie',
    'الوظيفة': 'fa-solid fa-briefcase',
    'محل الإقامة': 'fa-solid fa-location-dot',
    'الرقم الوطني': 'fa-solid fa-id-card',
    'التخصص': 'fa-solid fa-award',
    'رقم العقد': 'fa-solid fa-file-contract',
    'الراتب': 'fa-solid fa-money-bill-wave',
    'تاريخ البداية': 'fa-solid fa-calendar-plus',
    'حالة العقد': 'fa-solid fa-circle-check',
    'الموظف': 'fa-solid fa-user-tie',
    'الحضور': 'fa-solid fa-clock',
    'الانصراف': 'fa-solid fa-right-from-bracket',
    'المبلغ': 'fa-solid fa-money-bill',
    'ملاحظات': 'fa-solid fa-sticky-note',
    'الخصم': 'fa-solid fa-minus-circle',
    'المادة': 'fa-solid fa-book-open',
    'المعلم': 'fa-solid fa-chalkboard-user',
    'اليوم': 'fa-solid fa-calendar-day',
    'الحصة': 'fa-solid fa-clock',
    'الغائب': 'fa-solid fa-user-xmark',
    'البديل': 'fa-solid fa-user-pen',
    'النشاط': 'fa-solid fa-trophy',
    'النوع': 'fa-solid fa-tags',
    'المشرف': 'fa-solid fa-person-chalkboard',
    'المشاركون': 'fa-solid fa-people-group',
    'الخط': 'fa-solid fa-route',
    'السائق': 'fa-solid fa-id-badge',
    'الحافلة': 'fa-solid fa-bus',
    'الاشتراك': 'fa-solid fa-money-check',
    'الوصف': 'fa-solid fa-align-right',
    'المدين': 'fa-solid fa-arrow-trend-up',
    'الدائن': 'fa-solid fa-arrow-trend-down',
    'رقم السند': 'fa-solid fa-file-invoice',
    'من حساب': 'fa-solid fa-arrow-right-from-bracket',
    'إلى حساب': 'fa-solid fa-arrow-right-to-bracket',
    'طريقة الدفع': 'fa-solid fa-credit-card',
    'الترحيل': 'fa-solid fa-paper-plane',
    'الرصيد': 'fa-solid fa-wallet',
    'رقم الحساب': 'fa-solid fa-hashtag',
    'اسم الحساب': 'fa-solid fa-landmark',
    'الحساب الأب': 'fa-solid fa-folder-tree',
    'المستوى': 'fa-solid fa-signal',
    'الطبيعة': 'fa-solid fa-circle-half-stroke',
    'Column1': 'fa-solid fa-table-columns',
    'Calendar View': 'fa-solid fa-calendar-alt',
    'رقم القيد': 'fa-solid fa-hashtag',
    'حساب المدين': 'fa-solid fa-arrow-up',
    'حساب الدائن': 'fa-solid fa-arrow-down',
    'المعرف': 'fa-solid fa-fingerprint',
    'العنوان': 'fa-solid fa-heading',
    'المرجع': 'fa-solid fa-bookmark',
    'الفئة': 'fa-solid fa-folder',
    'العملية / النوع': 'fa-solid fa-cogs',
    'عملية الترحيل': 'fa-solid fa-paper-plane',
    'حالة الترحيل': 'fa-solid fa-circle-check',
    'التنبيه': 'fa-solid fa-bell',
    'الهدف': 'fa-solid fa-bullseye',
    'القاعة': 'fa-solid fa-location-dot',
    'نوع الامتحان': 'fa-solid fa-clipboard-list',
    'الوقت': 'fa-solid fa-clock',
    'رقم الجلوس': 'fa-solid fa-hashtag',
    'الرقم السري': 'fa-solid fa-lock',
    'القسم': 'fa-solid fa-building-user',
    'السنة': 'fa-solid fa-calendar',
    'تاريخ الالتحاق': 'fa-solid fa-calendar-plus',
    'العنوان / الهاتف': 'fa-solid fa-address-book',
    'نسبة النجاح': 'fa-solid fa-chart-line',
    'عدد الطلاب': 'fa-solid fa-users',
    'الناجحون': 'fa-solid fa-check-double',
    'الراسبون': 'fa-solid fa-xmark',
    'الدرجة': 'fa-solid fa-star',
    'التقدير': 'fa-solid fa-medal',
    'الواجب': 'fa-solid fa-book-open-reader',
    'تاريخ التسليم': 'fa-solid fa-calendar-check',
    'الشهادة': 'fa-solid fa-certificate',
    'رسائل المطالبة': 'fa-solid fa-envelope',
    'المبلغ المستحق': 'fa-solid fa-money-bill-wave',
    'المبلغ المسدد': 'fa-solid fa-check-circle',
    'المتبقي': 'fa-solid fa-hourglass-half',
    'الصنف': 'fa-solid fa-box',
    'الكمية': 'fa-solid fa-cubes',
    'السعر': 'fa-solid fa-tag',
    'المورد': 'fa-solid fa-truck-field',
    'المستلم': 'fa-solid fa-user-check',
    'رقم الأمر': 'fa-solid fa-file-alt',
    'حالة الأمر': 'fa-solid fa-circle-info',
    'الضامن': 'fa-solid fa-handshake',
    'رقم الهوية': 'fa-solid fa-id-card',
    'الجنسية': 'fa-solid fa-flag',
    'المخالفة': 'fa-solid fa-triangle-exclamation',
    'الإجراء': 'fa-solid fa-gavel',
    'الزائر': 'fa-solid fa-person-walking-arrow-right',
    'الغرض': 'fa-solid fa-bullseye',
    'البريد / التواصل': 'fa-solid fa-envelope',
    'العملة': 'fa-solid fa-money-bill-transfer',
    'السعر / سعر الصرف': 'fa-solid fa-exchange-alt',
    'رقم الشيك': 'fa-solid fa-money-check',
    'البنك': 'fa-solid fa-building-columns',
    'تاريخ الاستحقاق': 'fa-solid fa-calendar-xmark',
    'حالة الشيك': 'fa-solid fa-circle-info',
    'تاريخ الإقفال': 'fa-solid fa-lock',
    'نوع الإقفال': 'fa-solid fa-folder-closed',
    'القالب': 'fa-solid fa-file-code',
    'الرسالة': 'fa-solid fa-comment-sms',
    'المستلمون': 'fa-solid fa-users',
    'الباقة': 'fa-solid fa-credit-card',
    'الرصيد المتبقي': 'fa-solid fa-wallet',
    'تاريخ التجديد': 'fa-solid fa-calendar-plus',
}

# Function to add icon to <th> text
def add_th_icon(match):
    global changes_html
    content = match.group(1)
    if '<i ' in content or 'fa-' in content:
        return match.group(0)
    
    text = content.strip()
    icon_class = None
    
    # Try exact match first
    if text in th_icon_map:
        icon_class = th_icon_map[text]
    else:
        # Try partial match
        for key, val in th_icon_map.items():
            if key in text or text in key:
                icon_class = val
                break
    
    if not icon_class:
        # Default icon for unmatched
        icon_class = 'fa-solid fa-circle'
    
    changes_html += 1
    return f'<th><i class="{icon_class}"></i> {content}</th>'

html = re.sub(r'<th>((?:(?!</th>).)+?)</th>', add_th_icon, html)

# ======================================================
# 2. Add icons to h3 headers without icons in HTML
# ======================================================
h3_icon_map = {
    'مرحباً': 'fa-solid fa-hand-wave',
    'تحديث كلمة مرور': 'fa-solid fa-key',
    'الملخص المالي': 'fa-solid fa-chart-line',
    'أحدث الحركات': 'fa-solid fa-bolt',
    'Calendar View': 'fa-solid fa-calendar-alt',
}

def add_h3_icon(match):
    global changes_html
    tag = match.group(1)
    attrs = match.group(2)
    content = match.group(3)
    
    if '<i ' in content or 'fa-' in content:
        return match.group(0)
    
    text = re.sub(r'<[^>]+>', '', content).strip()
    icon_class = None
    
    for key, val in h3_icon_map.items():
        if key in text:
            icon_class = val
            break
    
    if icon_class:
        changes_html += 1
        return f'<{tag}{attrs}><i class="{icon_class}"></i> {content}</{tag}>'
    
    return match.group(0)

html = re.sub(r'<(h[34])([^>]*)>((?:(?!</h[34]>).)+?)</\1>', add_h3_icon, html, flags=re.DOTALL)

# ======================================================
# 3. Add icons to buttons "تحديد الكل" and "إلغاء الكل" in app.js
# ======================================================
js = js.replace(
    '>تحديد الكل</button>',
    '><i class="fa-solid fa-check-double"></i> تحديد الكل</button>'
)
js = js.replace(
    '>إلغاء الكل</button>',
    '><i class="fa-solid fa-xmark"></i> إلغاء الكل</button>'
)

# ======================================================
# 4. Add icons to h3 headings in app.js template literals
# ======================================================
# Pattern: <h3>Arabic text without icon</h3>
def add_js_h_icon(match):
    global changes_js
    tag = match.group(1)
    content = match.group(2)
    
    if '<i ' in content or 'fa-' in content:
        return match.group(0)
    
    text = re.sub(r'<[^>]+>', '', content).strip()
    
    icon_map = {
        'سند': 'fa-solid fa-file-invoice',
        'تفاصيل': 'fa-solid fa-circle-info',
        'ملخص': 'fa-solid fa-chart-pie',
        'إجمالي': 'fa-solid fa-calculator',
        'معلومات': 'fa-solid fa-info-circle',
        'بيانات': 'fa-solid fa-database',
        'تقرير': 'fa-solid fa-file-lines',
        'نتائج': 'fa-solid fa-ranking-star',
        'كشف': 'fa-solid fa-scroll',
    }
    
    icon_class = None
    for key, val in icon_map.items():
        if key in text:
            icon_class = val
            break
    
    if icon_class:
        changes_js += 1
        return f'<{tag}><i class="{icon_class}"></i> {content}</{tag}>'
    
    return match.group(0)

js = re.sub(r'<(h[23])>((?:(?!</h[23]>).)+?)</\1>', add_js_h_icon, js)

# ======================================================
# 5. Verify brace balance in JS
# ======================================================
opens = js.count('{')
closes = js.count('}')
print(f"app.js brace check: open={opens} close={closes} diff={opens-closes}")
if opens != closes:
    print("WARNING: Brace imbalance detected!")

# ======================================================
# 6. Save files
# ======================================================
ts = str(int(time.time()))

# Update cache busters
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync admin.html and parent.html
with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nHTML changes: {changes_html}")
print(f"JS changes: {changes_js}")
print(f"Cache buster: {ts}")
print("All files synced (school.html, admin.html, parent.html, app.js)")
print("DONE!")
