"""
================================================================================
🔍 نظام المدارس الذكي - سكريبت التحقق الأمني من فراغ الحقول وعدم تسريب أي بيانات
================================================================================
يقوم هذا السكريبت بفحص جميع بوابات النظام (/school, /admin, /parent) والتأكد من:
1. حقول تسجيل الدخول (اسم المستخدم وكلمة السر) فارغة تماماً value="".
2. عدم وجود أي صناديق أو أزرار للحسابات التجريبية أو الملء التلقائي.
3. إخفاء حقل المدرسة نهائياً في بوابة مدير النظام /admin وبوابة ولي الأمر /parent.
4. مطابقة نوع الحسابات والصلاحيات لكل بوابة دون أي خلط.
================================================================================
"""

import urllib.request
import re
import sys

# ضبط ترميز المخرجات لدعم اللغة العربية
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PORTALS = [
    {
        "name": "بوابة المدارس (School Portal)",
        "url": "http://127.0.0.1:8000/school",
        "expect_school_field": True,
        "allowed_roles": ["school_admin", "teacher", "staff", "parent"],
        "forbidden_roles": ["saas_admin"]
    },
    {
        "name": "بوابة مدير عام النظام السحابي (SaaS Admin)",
        "url": "http://127.0.0.1:8000/admin",
        "expect_school_field": False,
        "allowed_roles": ["saas_admin", "db_admin", "security_officer"],
        "forbidden_roles": ["school_admin", "teacher", "staff"]
    },
    {
        "name": "بوابة أولياء الأمور والطلاب (Parent Portal)",
        "url": "http://127.0.0.1:8000/parent",
        "expect_school_field": False,
        "allowed_roles": ["parent"],
        "forbidden_roles": ["saas_admin", "school_admin", "teacher"]
    }
]

def audit_portal(portal):
    print(f"\n{'='*70}")
    print(f"📡 فحص: {portal['name']}")
    print(f"🔗 الرابط: {portal['url']}")
    print(f"{'='*70}")

    try:
        req = urllib.request.Request(portal["url"], headers={'User-Agent': 'SecurityAuditor/1.0'})
        html = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
    except Exception as e:
        print(f"❌ خطأ في الاتصال بالخادم: {e}")
        return False

    all_passed = True

    # 1. فحص حقل اسم المستخدم
    u_match = re.search(r'<input[^>]*id=["\']username["\'][^>]*>', html)
    if u_match:
        tag = u_match.group(0)
        val_match = re.search(r'value=["\']([^"\']*)["\']', tag)
        val = val_match.group(1) if val_match else ""
        if val == "":
            print("  ✅ [حقل اسم المستخدم]: فارغ تماماً ولا يحتوي على أي بيانات مسبقة (value=\"\").")
        else:
            print(f"  ❌ [حقل اسم المستخدم]: يحتوي على بيانات مسبقة! (القيمة: \"{val}\")")
            all_passed = False
    else:
        print("  ⚠️ لم يتم العثور على حقل username")
        all_passed = False

    # 2. فحص حقل كلمة المرور
    p_match = re.search(r'<input[^>]*id=["\']password["\'][^>]*>', html)
    if p_match:
        tag = p_match.group(0)
        val_match = re.search(r'value=["\']([^"\']*)["\']', tag)
        val = val_match.group(1) if val_match else ""
        if val == "":
            print("  ✅ [حقل كلمة المرور]: فارغ تماماً ومحمي ولا يحتوي على أي كلمة سر مسجلة (value=\"\").")
        else:
            print(f"  ❌ [حقل كلمة المرور]: يحتوي على كلمة سر مسجلة! (القيمة: \"{val}\")")
            all_passed = False
    else:
        print("  ⚠️ لم يتم العثور على حقل password")
        all_passed = False

    # 3. فحص صندوق الحسابات التجريبية أو شارات الدخول السريع
    has_demo = any(keyword in html for keyword in [
        "الحسابات التجريبية",
        "Quick Access Helper Badges",
        "👑 مدير مدرسة",
        "🛡️ مدير النظام (SaaS)"
    ])
    if not has_demo:
        print("  ✅ [صندوق الحسابات التجريبية]: غير موجود ومحذوف نهائياً من الواجهة.")
    else:
        print("  ❌ [صندوق الحسابات التجريبية]: ما زال يظهر في الصفحة!")
        all_passed = False

    # 4. فحص حالة حقل المدرسة (إخفاء / إظهار)
    sf_match = re.search(r'<div[^>]*id=["\']schoolField["\'][^>]*style=["\']([^"\']*)["\']', html)
    if sf_match:
        style = sf_match.group(1)
        is_hidden = "display: none" in style or "display:none" in style
        if portal["expect_school_field"]:
            if not is_hidden:
                print("  ✅ [حقل المنشأة / المدرسة]: ظاهر بنجاح لإتاحة اختيار المدرسة لبوابة المدرسة.")
            else:
                print("  ❌ [حقل المنشأة / المدرسة]: مخفي بالخطأ في بوابة المدرسة!")
                all_passed = False
        else:
            if is_hidden:
                print("  ✅ [حقل المنشأة / المدرسة]: محجوب ومخفي تماماً (display: none !important).")
            else:
                print("  ❌ [حقل المنشأة / المدرسة]: يظهر بالخطأ في بوابة الإدارة/أولياء الأمور!")
                all_passed = False

    # 5. فحص أنواع الحسابات لمنع التداخل
    ut_match = re.search(r'<select[^>]*id=["\']userType["\'][^>]*>(.*?)</select>', html, re.DOTALL)
    if ut_match:
        options = re.findall(r'<option[^>]*value=["\']([^"\']+)["\']', ut_match.group(1))
        forbidden_found = [r for r in portal["forbidden_roles"] if r in options]
        if not forbidden_found:
            print(f"  ✅ [قائمة الصلاحيات]: معزولة تماماً وتقتصر فقط على: {options}")
        else:
            print(f"  ❌ [قائمة الصلاحيات]: تحتوي على أدوار محظورة في هذه البوابة: {forbidden_found}")
            all_passed = False

    return all_passed

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║   🛡️  فاحص أمان الحقول والواجهات - Smart School ERP        ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    results = [audit_portal(p) for p in PORTALS]

    print(f"\n{'='*70}")
    if all(results):
        print("🎉 النتيجة النهائية: 100% نجاح تام — كافة الحقول فارغة ونظيفة ومحمية بالكامل!")
    else:
        print("⚠️ النتيجة النهائية: هناك ملاحظات تحتاج إلى مراجعة.")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
