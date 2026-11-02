"""
Multi-School Master Data Generator & Seeder
Populates 30 complete schools, 3,000 students (100 per school), staff, buses, routes,
all 76 UI interface data stores, generates 30 SVG logos & 30 SVG campus illustrations,
and seeds the SQLite secure_school.db database.
"""
import os
import sys
import json
import uuid
import random
import sqlite3
import hashlib
from datetime import datetime, date

# Set UTF-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMG_SCHOOLS_DIR = os.path.join(ASSETS_DIR, "images", "schools")
FE_IMG_SCHOOLS_DIR = os.path.join(BASE_DIR, "frontend", "images", "schools")
JS_DIR = os.path.join(ASSETS_DIR, "js")
DB_PATH = os.path.join(BASE_DIR, "secure_school.db")

os.makedirs(IMG_SCHOOLS_DIR, exist_ok=True)
os.makedirs(FE_IMG_SCHOOLS_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. THE 30 SCHOOLS SPECIFICATION (Across 8 Yemeni Governorates)
# -----------------------------------------------------------------------------
SCHOOLS_SPEC = [
    # صنعاء (6 مدارس)
    {
        "id": "SCH-01", "code": "SCH-SAN-01",
        "name": "مدرسة المتفوقين الأهلية النموذجية", "nameEn": "Al-Motafawiqeen Modern Model School",
        "governorate": "صنعاء", "district": "مديرية السبعين", "city": "صنعاء — حدة",
        "address": "صنعاء - مديرية السبعين - شارع حدة - جوار المركز التجاري",
        "license": "LIC-2026-9941", "principal": "د. عبد الرحمن الصبري",
        "phone": "770112233 | 01411222", "email": "info@motafawiqeen.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "1998", "motto": "صرح التفوق والريادة العلمية",
        "theme": {"p": "#1e3a8a", "s": "#3b82f6", "g": "#f59e0b", "style": "shield"}
    },
    {
        "id": "SCH-02", "code": "SCH-SAN-02",
        "name": "مدارس رواد اليمن الحديثة الأهلية", "nameEn": "Rowad Al-Yemen Modern Schools",
        "governorate": "صنعاء", "district": "مديرية السبعين", "city": "صنعاء — الأصبحي",
        "address": "صنعاء - مديرية السبعين - الأصبحي - شارع المقالح",
        "license": "LIC-2026-9942", "principal": "أ. محمد عبد الله الحيمي",
        "phone": "771223344 | 01522333", "email": "info@rowad-yemen.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2002", "motto": "نبني قادة الغد وصناع المجد",
        "theme": {"p": "#065f46", "s": "#10b981", "g": "#d97706", "style": "crest"}
    },
    {
        "id": "SCH-03", "code": "SCH-SAN-03",
        "name": "مدارس النهضة الدولية للغات", "nameEn": "Al-Nahda International Language Schools",
        "governorate": "صنعاء", "district": "مديرية الوحدة", "city": "صنعاء — شارع بغداد",
        "address": "صنعاء - مديرية الوحدة - شارع بغداد - تقاطع شارع 14 أكتوبر",
        "license": "LIC-2026-9943", "principal": "د. فؤاد إسماعيل الكبسي",
        "phone": "772334455 | 01233444", "email": "info@alnahda-languages.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2005", "motto": "نافذتك العالمية نحو التميز اللغوي",
        "theme": {"p": "#7c2d12", "s": "#ea580c", "g": "#fbbf24", "style": "hexagon"}
    },
    {
        "id": "SCH-04", "code": "SCH-SAN-04",
        "name": "مدارس الرشيد الأهلية النموذجية", "nameEn": "Al-Rasheed Modern Model Schools",
        "governorate": "صنعاء", "district": "مديرية الوحدة", "city": "صنعاء — الحي الدبلوماسي",
        "address": "صنعاء - مديرية الوحدة - الحي الدبلوماسي - شارع مجاهد",
        "license": "LIC-2026-9944", "principal": "أ. أروى ناصر المقالح",
        "phone": "773445566 | 01445566", "email": "info@alrasheed-school.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "1995", "motto": "أصالة التعليم وحداثة المعرفة",
        "theme": {"p": "#4c1d95", "s": "#8b5cf6", "g": "#f59e0b", "style": "octagon"}
    },
    {
        "id": "SCH-05", "code": "SCH-SAN-05",
        "name": "مدارس الأوائل الأهلية الحديثة", "nameEn": "Al-Awael Modern Private Schools",
        "governorate": "صنعاء", "district": "مديرية معين", "city": "صنعاء — شارع الستين الغربي",
        "address": "صنعاء - مديرية معين - الستين الغربي - بجانب جامعة الإيمان",
        "license": "LIC-2026-9945", "principal": "د. أحمد قاسم الصعفاني",
        "phone": "774556677 | 01345678", "email": "info@alawael-school.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2008", "motto": "المعرفة قوة والابتكار غايتنا",
        "theme": {"p": "#0f172a", "s": "#0284c7", "g": "#38bdf8", "style": "arch"}
    },
    {
        "id": "SCH-06", "code": "SCH-SAN-06",
        "name": "مدارس دار العلوم الأهلية النموذجية", "nameEn": "Dar Al-Uloom Modern Model Schools",
        "governorate": "صنعاء", "district": "مديرية الثورة", "city": "صنعاء — الحصبة",
        "address": "صنعاء - مديرية الثورة - الحصبة - شارع مازدا",
        "license": "LIC-2026-9946", "principal": "أ. حميد طه المؤيد",
        "phone": "775667788 | 01246810", "email": "info@dar-aluloom.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2000", "motto": "منهل العلم وبوابة المستقبل",
        "theme": {"p": "#14532d", "s": "#22c55e", "g": "#eab308", "style": "shield"}
    },

    # تعز (5 مدارس)
    {
        "id": "SCH-07", "code": "SCH-TAI-07",
        "name": "مدارس الرواد الدولية للغات", "nameEn": "Al-Rowad International Languages School",
        "governorate": "تعز", "district": "مديرية القاهرة", "city": "تعز — المسبح",
        "address": "تعز - مديرية القاهرة - شارع جمال - المسبح الأسفل",
        "license": "LIC-2026-8812", "principal": "د. سالم الحميري",
        "phone": "771234567 | 04200000", "email": "info@alrowad-school.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2001", "motto": "رواد الفكر وقادة النهضة",
        "theme": {"p": "#1e3a8a", "s": "#2563eb", "g": "#f59e0b", "style": "crest"}
    },
    {
        "id": "SCH-08", "code": "SCH-TAI-08",
        "name": "مدارس المعالي الأهلية الحديثة", "nameEn": "Al-Maali Modern Private Schools",
        "governorate": "تعز", "district": "مديرية القاهرة", "city": "تعز — شارع جمال",
        "address": "تعز - مديرية القاهرة - شارع جمال عبد الناصر - جوار المجمع الحكومي",
        "license": "LIC-2026-8813", "principal": "أ. عبد القادر الشميري",
        "phone": "772112244 | 04221144", "email": "info@almaali-taiz.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2006", "motto": "سمو في الأخلاق وإتقان في التعلم",
        "theme": {"p": "#831843", "s": "#db2777", "g": "#fde047", "style": "hexagon"}
    },
    {
        "id": "SCH-09", "code": "SCH-TAI-09",
        "name": "مدرسة النوابغ النموذجية للبنين والبنات", "nameEn": "Al-Nawabigh Model School",
        "governorate": "تعز", "district": "مديرية المظفر", "city": "تعز — النسيم",
        "address": "تعز - مديرية المظفر - حي النسيم - شارع الثلاثين",
        "license": "LIC-2026-8814", "principal": "أ. بشرى عبد الله العريقي",
        "phone": "773223355 | 04233221", "email": "info@nawabigh-taiz.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2010", "motto": "نكتشف العبقرية ونرعى الموهبة",
        "theme": {"p": "#115e59", "s": "#0d9488", "g": "#fbbf24", "style": "octagon"}
    },
    {
        "id": "SCH-10", "code": "SCH-TAI-10",
        "name": "مدارس الصرح التعليمي الأهلية", "nameEn": "Al-Sarh Educational Schools",
        "governorate": "تعز", "district": "مديرية المظفر", "city": "تعز — الدحي",
        "address": "تعز - مديرية المظفر - الدحي - جوار حبيل سلمان",
        "license": "LIC-2026-8815", "principal": "د. منير عبده فارع",
        "phone": "774334466 | 04255443", "email": "info@alsarh-edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2012", "motto": "صرح راسخ لجيل واعد",
        "theme": {"p": "#1e1b4b", "s": "#4f46e5", "g": "#38bdf8", "style": "arch"}
    },
    {
        "id": "SCH-11", "code": "SCH-TAI-11",
        "name": "مدرسة الإشراق الأهلية الحديثة", "nameEn": "Al-Ishraq Modern Model School",
        "governorate": "تعز", "district": "مديرية صالة", "city": "تعز — الجحملية",
        "address": "تعز - مديرية صالة - الجحملية العليا - جوار مدرسة الثورة",
        "license": "LIC-2026-8816", "principal": "أ. مروان قائد الصلوي",
        "phone": "775445577 | 04266554", "email": "info@ishraq-school.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2014", "motto": "إشراقة أمل ونور معرفة",
        "theme": {"p": "#701a75", "s": "#c026d3", "g": "#fde047", "style": "shield"}
    },

    # عدن (5 مدارس)
    {
        "id": "SCH-12", "code": "SCH-ADN-12",
        "name": "مدارس المستقبل الحديثة الأهلية", "nameEn": "Future Modern Private School",
        "governorate": "عدن", "district": "مديرية خور مكسر", "city": "عدن — ساحل أبين",
        "address": "عدن - مديرية خور مكسر - الحي الدبلوماسي - كورنيش ساحل أبين",
        "license": "LIC-2026-7734", "principal": "أ. فاطمة باحيدرة",
        "phone": "772345678 | 02200000", "email": "info@future-aden.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2003", "motto": "نصنع المستقبل بإرادة الحاضر",
        "theme": {"p": "#0369a1", "s": "#0284c7", "g": "#f59e0b", "style": "crest"}
    },
    {
        "id": "SCH-13", "code": "SCH-ADN-13",
        "name": "مدارس النخبة الدولية للغات", "nameEn": "Elite International Language School",
        "governorate": "عدن", "district": "مديرية خور مكسر", "city": "عدن — الشابات",
        "address": "عدن - مديرية خور مكسر - حي الشابات - بالقرب من كلية الطب",
        "license": "LIC-2026-7735", "principal": "د. وضاح أنيس الجاوي",
        "phone": "773112233 | 02233445", "email": "info@elite-aden.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2007", "motto": "تعليم النخبة لمعايير المستقبل",
        "theme": {"p": "#0f766e", "s": "#14b8a6", "g": "#fbbf24", "style": "hexagon"}
    },
    {
        "id": "SCH-14", "code": "SCH-ADN-14",
        "name": "ثانوية عدن النموذجية للبنين والبنات", "nameEn": "Aden Model Secondary School",
        "governorate": "عدن", "district": "مديرية صيرة (كريتر)", "city": "عدن — كريتر",
        "address": "عدن - مديرية صيرة - كريتر - شارع أروى - العقبة",
        "license": "LIC-2026-7736", "principal": "أ. سميرة حسن العبدلي",
        "phone": "774223344 | 02255667", "email": "info@aden-model.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "1994", "motto": "تاريخ عريق ومستقبل مشرق",
        "theme": {"p": "#881337", "s": "#e11d48", "g": "#fde047", "style": "octagon"}
    },
    {
        "id": "SCH-15", "code": "SCH-ADN-15",
        "name": "مدارس الأمل الأهلية الدولية", "nameEn": "Al-Amal International Schools",
        "governorate": "عدن", "district": "مديرية المعلا", "city": "عدن — الشارع الرئيسي",
        "address": "عدن - مديرية المعلا - الشارع الرئيسي - جوار الميناء",
        "license": "LIC-2026-7737", "principal": "أ. جلال صالح الردفاني",
        "phone": "775334455 | 02244556", "email": "info@alamal-aden.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2009", "motto": "أمل يتجدد وعطاء لا ينضب",
        "theme": {"p": "#312e81", "s": "#6366f1", "g": "#38bdf8", "style": "arch"}
    },
    {
        "id": "SCH-16", "code": "SCH-ADN-16",
        "name": "مدرسة شمسان الحديثة الأهلية", "nameEn": "Shamshan Modern School",
        "governorate": "عدن", "district": "مديرية المنصورة", "city": "عدن — ريمي",
        "address": "عدن - مديرية المنصورة - حي ريمي - شارع الكثيري",
        "license": "LIC-2026-7738", "principal": "د. إيناس عادل اليافعي",
        "phone": "776445566 | 02345678", "email": "info@shamshan-school.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2011", "motto": "شموخ كشمسان وتفوق بلا حدود",
        "theme": {"p": "#14532d", "s": "#16a34a", "g": "#eab308", "style": "shield"}
    },

    # حضرموت (4 مدارس)
    {
        "id": "SCH-17", "code": "SCH-HAD-17",
        "name": "مدارس حضرموت العالمية الأهلية", "nameEn": "Hadramout Global International Schools",
        "governorate": "حضرموت", "district": "مديرية المكلا", "city": "المكلا — فوه",
        "address": "حضرموت - المكلا - منطقة فوه - حي المساكن - بجانب سيتي مول",
        "license": "LIC-2026-6621", "principal": "د. عمر صالح باوزير",
        "phone": "770889900 | 05300112", "email": "info@hadramout-global.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2004", "motto": "أصالة حضرمية بمعايير عالمية",
        "theme": {"p": "#1e3a8a", "s": "#3b82f6", "g": "#f59e0b", "style": "crest"}
    },
    {
        "id": "SCH-18", "code": "SCH-HAD-18",
        "name": "مدرسة ابن خلدون النموذجية", "nameEn": "Ibn Khaldun Model Private School",
        "governorate": "حضرموت", "district": "مديرية المكلا", "city": "المكلا — الديس",
        "address": "حضرموت - المكلا - الديس - الغليلة - بجانب ثانوية المكلا",
        "license": "LIC-2026-6622", "principal": "أ. فرج مبارك باعباد",
        "phone": "771990011 | 05322110", "email": "info@ibn-khaldun.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "1999", "motto": "علم وعمران وتربية وإتقان",
        "theme": {"p": "#7c2d12", "s": "#ea580c", "g": "#fbbf24", "style": "hexagon"}
    },
    {
        "id": "SCH-19", "code": "SCH-HAD-19",
        "name": "مدارس وادي حضرموت الدولية", "nameEn": "Wadi Hadramout International School",
        "governorate": "حضرموت", "district": "مديرية سيئون", "city": "سيئون — حي القرن",
        "address": "حضرموت - سيئون - حي القرن - شارع المطار - جوار قصر الكثيري",
        "license": "LIC-2026-6623", "principal": "أ. هاشم علوي الحبشي",
        "phone": "772001122 | 05401122", "email": "info@wadi-hadramout.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2008", "motto": "نقاء الوادي وإشراق المعرفة",
        "theme": {"p": "#065f46", "s": "#10b981", "g": "#d97706", "style": "octagon"}
    },
    {
        "id": "SCH-20", "code": "SCH-HAD-20",
        "name": "مدرسة المكارم الأهلية الحديثة", "nameEn": "Al-Makarim Modern School",
        "governorate": "حضرموت", "district": "مديرية الشحر", "city": "الشحر — المنصورة",
        "address": "حضرموت - الشحر - حي المنصورة - بجانب ميناء الشحر التاريخي",
        "license": "LIC-2026-6624", "principal": "أ. سعيد أحمد باجبير",
        "phone": "773112244 | 05341122", "email": "info@almakarim-school.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2013", "motto": "مكارم الأخلاق ورقي العلم",
        "theme": {"p": "#4c1d95", "s": "#8b5cf6", "g": "#fde047", "style": "arch"}
    },

    # إب (4 مدارس)
    {
        "id": "SCH-21", "code": "SCH-IBB-21",
        "name": "مدارس اللواء الأخضر الأهلية النموذجية", "nameEn": "Green Brigade Modern Model School",
        "governorate": "إب", "district": "مديرية الظهار", "city": "إب — شارع العدين",
        "address": "إب - مديرية الظهار - شارع العدين - تقاطع مفرق جبلة",
        "license": "LIC-2026-5511", "principal": "د. فيصل عبد الله الغيثي",
        "phone": "774223355 | 04401122", "email": "info@green-brigade.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2001", "motto": "واحة المعرفة في ربا اللواء الأخضر",
        "theme": {"p": "#14532d", "s": "#22c55e", "g": "#eab308", "style": "shield"}
    },
    {
        "id": "SCH-22", "code": "SCH-IBB-22",
        "name": "مدارس أجيال الغد الحديثة", "nameEn": "Ajyal Al-Ghad Modern Schools",
        "governorate": "إب", "district": "مديرية الظهار", "city": "إب — المشنة الغربية",
        "address": "إب - مديرية الظهار - خط الدائري الغربي - جوار جامعة إب",
        "license": "LIC-2026-5512", "principal": "أ. نجلاء قاسم السقاف",
        "phone": "775334466 | 04422233", "email": "info@ajyal-alghad.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2007", "motto": "أجيال تصنع المجد وتنافس العالم",
        "theme": {"p": "#1e3a8a", "s": "#2563eb", "g": "#f59e0b", "style": "crest"}
    },
    {
        "id": "SCH-23", "code": "SCH-IBB-23",
        "name": "مدرسة السلام الأهلية للبنين والبنات", "nameEn": "Al-Salam Modern Private School",
        "governorate": "إب", "district": "مديرية المشنة", "city": "إب — المركز الثقافي",
        "address": "إب - مديرية المشنة - شارع تعز - خلف المركز الثقافي",
        "license": "LIC-2026-5513", "principal": "أ. رشيد منصور الحداد",
        "phone": "776445577 | 04411199", "email": "info@alsalam-ibb.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2010", "motto": "سلام وتعليم يرتقي بالإنسان",
        "theme": {"p": "#0f766e", "s": "#14b8a6", "g": "#fbbf24", "style": "hexagon"}
    },
    {
        "id": "SCH-24", "code": "SCH-IBB-24",
        "name": "مدرسة سيدة سبأ التاريخية النموذجية", "nameEn": "Sayyidat Saba Historic Model School",
        "governorate": "إب", "district": "مديرية جبلة", "city": "جبلة — حي الروضة",
        "address": "إب - مديرية جبلة - حي الروضة - جوار دار العز التاريخي",
        "license": "LIC-2026-5514", "principal": "أ. جميلة علي المتوكل",
        "phone": "777556688 | 04433311", "email": "info@sayyidat-saba.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2015", "motto": "عبق التاريخ ومجد العلم والمعرفة",
        "theme": {"p": "#831843", "s": "#ec4899", "g": "#fde047", "style": "octagon"}
    },

    # الحديدة (2 مدرستان)
    {
        "id": "SCH-25", "code": "SCH-HOD-25",
        "name": "مدرسة عروس البحر الأحمر الأهلية", "nameEn": "Bride of Red Sea Modern School",
        "governorate": "الحديدة", "district": "مديرية الحوك", "city": "الحديدة — شارع صنعاء",
        "address": "الحديدة - مديرية الحوك - شارع صنعاء - جوار جولة الساعة",
        "license": "LIC-2026-4401", "principal": "د. عبد السلام الأهدل",
        "phone": "778667799 | 03211222", "email": "info@redsea-school.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2003", "motto": "منارة تهامة وموئل العلم",
        "theme": {"p": "#0284c7", "s": "#38bdf8", "g": "#fbbf24", "style": "arch"}
    },
    {
        "id": "SCH-26", "code": "SCH-HOD-26",
        "name": "مدرسة الفجر الساحلية الحديثة", "nameEn": "Al-Fajr Modern Coastal School",
        "governorate": "الحديدة", "district": "مديرية الميناء", "city": "الحديدة — الكورنيش",
        "address": "الحديدة - مديرية الميناء - طريق الكورنيش الشمالي - جوار الميناء",
        "license": "LIC-2026-4402", "principal": "أ. إبراهيم يحيى شوعي",
        "phone": "779778800 | 03244555", "email": "info@alfajr-school.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2012", "motto": "فجر جديد لكل جيل صاعد",
        "theme": {"p": "#115e59", "s": "#0d9488", "g": "#f59e0b", "style": "shield"}
    },

    # ذمار (2 مدرستان)
    {
        "id": "SCH-27", "code": "SCH-DHA-27",
        "name": "مدرسة سبأ الأهلية النموذجية", "nameEn": "Saba Modern Model School",
        "governorate": "ذمار", "district": "مديرية ذمار", "city": "ذمار — حي الجامعة",
        "address": "ذمار - مديرية ذمار - حي الجامعة - شارع رداع",
        "license": "LIC-2026-3391", "principal": "أ. عادل حمود العنسي",
        "phone": "770119922 | 06500112", "email": "info@saba-dhamar.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2005", "motto": "حضارة سبأ وفخر الأجيال",
        "theme": {"p": "#9a3412", "s": "#f97316", "g": "#fde047", "style": "crest"}
    },
    {
        "id": "SCH-28", "code": "SCH-DHA-28",
        "name": "مدارس النهضة التعليمية بمعبر", "nameEn": "Al-Nahda Modern Schools Ma'bar",
        "governorate": "ذمار", "district": "مديرية معبر / جهران", "city": "معبر — الشارع العام",
        "address": "ذمار - مديرية جهران / معبر - الشارع العام - بجانب مبنى البريد",
        "license": "LIC-2026-3392", "principal": "أ. طه يحيى الديلمي",
        "phone": "771228833 | 06522334", "email": "info@nahda-mabar.edu.ye",
        "plan": "الخطة الأساسية (Standard)", "est": "2014", "motto": "نهضة تربوية شاملة ومستدامة",
        "theme": {"p": "#1e1b4b", "s": "#4338ca", "g": "#38bdf8", "style": "hexagon"}
    },

    # مأرب (2 مدرستان)
    {
        "id": "SCH-29", "code": "SCH-MAR-29",
        "name": "مدارس بلقيس الدولية النموذجية", "nameEn": "Bilqees International Model School",
        "governorate": "مأرب", "district": "مديرية مدينة مأرب", "city": "مأرب — الروضة",
        "address": "مأرب - مدينة مأرب - حي الروضة - شارع الأربعين - جوار المجمع الحكومي",
        "license": "LIC-2026-2281", "principal": "د. سلطان ناصر المرادي",
        "phone": "772337744 | 06301122", "email": "info@bilqees-marib.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2016", "motto": "تاج المعرفة وعرش التفوق",
        "theme": {"p": "#854d0e", "s": "#ca8a04", "g": "#fde047", "style": "octagon"}
    },
    {
        "id": "SCH-30", "code": "SCH-MAR-30",
        "name": "مدارس أرض الجنتين الأهلية الحديثة", "nameEn": "Two Gardens Land Modern Schools",
        "governorate": "مأرب", "district": "مديرية الوادي", "city": "مأرب — وادي عبيدة",
        "address": "مأرب - مديرية الوادي - وادي عبيدة - خط صافر الدولي",
        "license": "LIC-2026-2282", "principal": "أ. سيف مبارك العرادة",
        "phone": "773446655 | 06322334", "email": "info@jannatain-marib.edu.ye",
        "plan": "الخطة الاحترافية (Enterprise)", "est": "2018", "motto": "ثمار العلم وطريق الريادة",
        "theme": {"p": "#14532d", "s": "#15803d", "g": "#fbbf24", "style": "arch"}
    }
]

print(f"Loaded {len(SCHOOLS_SPEC)} school definitions successfully.")

# -----------------------------------------------------------------------------
# 2. VECTOR SVG GENERATORS (Logos & Campus Illustrations)
# -----------------------------------------------------------------------------
def generate_school_logo_svg(sch):
    theme = sch["theme"]
    p = theme["p"]
    s = theme["s"]
    g = theme["g"]
    style = theme["style"]
    name_ar = sch["name"]
    short_name = name_ar.replace("مدارس ", "").replace("مدرسة ", "").replace(" الأهلية", "").replace(" النموذجية", "").replace(" الحديثة", "").replace(" الدولية", "").strip()
    est = sch["est"]

    # Template styles
    if style == "shield":
        body_path = '<path d="M 100,15 L 175,40 C 175,120 100,185 100,185 C 100,185 25,120 25,40 Z" fill="url(#bgGrad)" stroke="url(#goldGrad)" stroke-width="5" />'
        inner_path = '<path d="M 100,26 L 163,47 C 163,113 100,170 100,170 C 100,170 37,113 37,47 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="4,3" />'
    elif style == "crest":
        body_path = '<circle cx="100" cy="100" r="88" fill="url(#bgGrad)" stroke="url(#goldGrad)" stroke-width="6" />'
        inner_path = '<circle cx="100" cy="100" r="76" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="5,3" /><circle cx="100" cy="100" r="72" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1" />'
    elif style == "hexagon":
        body_path = '<polygon points="100,12 178,55 178,145 100,188 22,145 22,55" fill="url(#bgGrad)" stroke="url(#goldGrad)" stroke-width="5" />'
        inner_path = '<polygon points="100,22 166,60 166,140 100,178 34,140 34,60" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="4,3" />'
    elif style == "octagon":
        body_path = '<polygon points="65,15 135,15 185,65 185,135 135,185 65,185 15,135 15,65" fill="url(#bgGrad)" stroke="url(#goldGrad)" stroke-width="5" />'
        inner_path = '<polygon points="68,23 132,23 177,68 177,132 132,177 68,177 23,132 23,68" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="4,3" />'
    else: # arch
        body_path = '<path d="M 30,185 L 30,80 Q 100,10 170,80 L 170,185 Z" fill="url(#bgGrad)" stroke="url(#goldGrad)" stroke-width="5" />'
        inner_path = '<path d="M 40,178 L 40,84 Q 100,22 160,84 L 160,178 Z" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="4,3" />'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{p}" />
      <stop offset="100%" stop-color="{s}" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{g}" />
      <stop offset="50%" stop-color="#fffbeb" />
      <stop offset="100%" stop-color="{g}" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.45" />
    </filter>
  </defs>
  <g filter="url(#glow)">
    {body_path}
    {inner_path}
  </g>
  <!-- Decorative Laurels / Stars -->
  <g fill="{g}">
    <polygon points="100,32 103,40 111,40 105,45 107,53 100,48 93,53 95,45 89,40 97,40" />
    <polygon points="80,38 82,44 88,44 83,48 85,54 80,50 75,54 77,48 72,44 78,44" transform="scale(0.85) translate(15, 5)" />
    <polygon points="120,38 122,44 128,44 123,48 125,54 120,50 115,54 117,48 112,44 118,44" transform="scale(0.85) translate(25, 5)" />
  </g>
  <!-- Central Emblem: Academic Book & Torch -->
  <g transform="translate(100, 95) scale(0.85)">
    <!-- Open Book -->
    <path d="M 0,0 C -15,-10 -35,-8 -50,-2 L -50,28 C -35,22 -15,20 0,30 C 15,20 35,22 50,28 L 50,-2 C 35,-8 15,-10 0,0 Z" fill="#ffffff" stroke="{g}" stroke-width="2" />
    <line x1="0" y1="0" x2="0" y2="30" stroke="{g}" stroke-width="2" />
    <!-- Book pages lines -->
    <line x1="-42" y1="8" x2="-8" y2="3" stroke="#cbd5e1" stroke-width="1.5" />
    <line x1="-42" y1="16" x2="-8" y2="11" stroke="#cbd5e1" stroke-width="1.5" />
    <line x1="8" y1="3" x2="42" y2="8" stroke="#cbd5e1" stroke-width="1.5" />
    <line x1="8" y1="11" x2="42" y2="16" stroke="#cbd5e1" stroke-width="1.5" />
    <!-- Torch Flame -->
    <path d="M 0,-5 C -8,-15 -2,-30 0,-38 C 2,-30 8,-15 0,-5 Z" fill="{g}" />
    <path d="M 0,-8 C -4,-15 0,-24 0,-28 C 0,-24 4,-15 0,-8 Z" fill="#ffffff" />
  </g>
  <!-- Ribbon Banner -->
  <path d="M 35,142 L 165,142 L 155,164 L 45,164 Z" fill="#0f172a" stroke="{g}" stroke-width="1.5" />
  <text x="100" y="157" font-family="'Cairo', 'Segoe UI', Tahoma, sans-serif" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">{short_name}</text>
  <text x="100" y="176" font-family="'Cairo', 'Segoe UI', Tahoma, sans-serif" font-size="8.5" font-weight="700" fill="{g}" text-anchor="middle">تأسست {est} م</text>
</svg>'''
    return svg

def generate_school_campus_svg(sch):
    theme = sch["theme"]
    p = theme["p"]
    s = theme["s"]
    name_ar = sch["name"]
    code = sch["code"]
    city = sch["city"]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 400" width="700" height="400">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="60%" stop-color="#bae6fd" />
      <stop offset="100%" stop-color="#f0f9ff" />
    </linearGradient>
    <linearGradient id="wallGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#e2e8f0" />
    </linearGradient>
    <linearGradient id="brickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{p}" />
      <stop offset="100%" stop-color="{s}" />
    </linearGradient>
    <linearGradient id="glassGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
  </defs>

  <!-- Sky -->
  <rect x="0" y="0" width="700" height="270" fill="url(#skyGrad)" />
  <!-- Mountains in background -->
  <polygon points="0,270 90,180 220,270" fill="#94a3b8" opacity="0.35" />
  <polygon points="180,270 310,160 450,270" fill="#94a3b8" opacity="0.25" />
  <polygon points="400,270 540,175 700,270" fill="#94a3b8" opacity="0.3" />

  <!-- Ground / Courtyard -->
  <rect x="0" y="270" width="700" height="130" fill="#334155" />
  <polygon points="0,300 700,300 700,400 0,400" fill="#1e293b" />
  <line x1="0" y1="350" x2="700" y2="350" stroke="#f8fafc" stroke-width="2" stroke-dasharray="25,20" />

  <!-- Lawns & Landscaping -->
  <rect x="15" y="260" width="120" height="35" rx="6" fill="#15803d" />
  <rect x="565" y="260" width="120" height="35" rx="6" fill="#15803d" />
  <!-- Decorative Palm Trees -->
  <path d="M 60,260 Q 62,210 65,170" stroke="#78350f" stroke-width="7" fill="none" />
  <circle cx="65" cy="165" r="22" fill="#16a34a" />
  <circle cx="50" cy="160" r="18" fill="#15803d" />
  <circle cx="80" cy="160" r="18" fill="#15803d" />
  
  <path d="M 630,260 Q 628,210 625,170" stroke="#78350f" stroke-width="7" fill="none" />
  <circle cx="625" cy="165" r="22" fill="#16a34a" />
  <circle cx="610" cy="160" r="18" fill="#15803d" />
  <circle cx="640" cy="160" r="18" fill="#15803d" />

  <!-- Main Academic Building Structure -->
  <!-- Left Wing -->
  <rect x="90" y="110" width="170" height="160" fill="url(#wallGrad)" stroke="#94a3b8" stroke-width="2" />
  <!-- Right Wing -->
  <rect x="440" y="110" width="170" height="160" fill="url(#wallGrad)" stroke="#94a3b8" stroke-width="2" />
  <!-- Center Main Block -->
  <rect x="230" y="80" width="240" height="190" fill="url(#wallGrad)" stroke="#94a3b8" stroke-width="2" />
  <!-- Roof cornice -->
  <rect x="80" y="100" width="540" height="12" fill="url(#brickGrad)" />
  <rect x="220" y="70" width="260" height="14" fill="url(#brickGrad)" />

  <!-- Pediment / Header -->
  <polygon points="350,25 210,70 490,70" fill="url(#brickGrad)" stroke="#cbd5e1" stroke-width="1.5" />
  <!-- School Name Sign on Pediment -->
  <rect x="240" y="45" width="220" height="22" rx="4" fill="#0f172a" />
  <text x="350" y="60" font-family="'Cairo', sans-serif" font-size="10.5" font-weight="bold" fill="#f8fafc" text-anchor="middle">{name_ar}</text>

  <!-- Clock Tower on Center -->
  <circle cx="350" cy="115" r="18" fill="#ffffff" stroke="{p}" stroke-width="3" />
  <line x1="350" y1="115" x2="350" y2="104" stroke="#0f172a" stroke-width="2" />
  <line x1="350" y1="115" x2="358" y2="115" stroke="#0f172a" stroke-width="2" />

  <!-- Yemeni Flags on Wings -->
  <!-- Flag 1 (Left) -->
  <line x1="120" y1="100" x2="120" y2="45" stroke="#94a3b8" stroke-width="3" />
  <rect x="120" y="45" width="26" height="6" fill="#ce1126" />
  <rect x="120" y="51" width="26" height="6" fill="#ffffff" />
  <rect x="120" y="57" width="26" height="6" fill="#000000" />
  <!-- Flag 2 (Right) -->
  <line x1="580" y1="100" x2="580" y2="45" stroke="#94a3b8" stroke-width="3" />
  <rect x="580" y="45" width="26" height="6" fill="#ce1126" />
  <rect x="580" y="51" width="26" height="6" fill="#ffffff" />
  <rect x="580" y="57" width="26" height="6" fill="#000000" />

  <!-- Windows Grid -->
  <!-- Left Wing Windows -->
  <g fill="url(#glassGrad)" stroke="#64748b" stroke-width="1.5">
    <rect x="110" y="130" width="30" height="40" rx="3" />
    <rect x="160" y="130" width="30" height="40" rx="3" />
    <rect x="210" y="130" width="30" height="40" rx="3" />
    <rect x="110" y="195" width="30" height="40" rx="3" />
    <rect x="160" y="195" width="30" height="40" rx="3" />
    <rect x="210" y="195" width="30" height="40" rx="3" />
  </g>
  <!-- Right Wing Windows -->
  <g fill="url(#glassGrad)" stroke="#64748b" stroke-width="1.5">
    <rect x="460" y="130" width="30" height="40" rx="3" />
    <rect x="510" y="130" width="30" height="40" rx="3" />
    <rect x="560" y="130" width="30" height="40" rx="3" />
    <rect x="460" y="195" width="30" height="40" rx="3" />
    <rect x="510" y="195" width="30" height="40" rx="3" />
    <rect x="560" y="195" width="30" height="40" rx="3" />
  </g>
  <!-- Center Windows & Main Entrance Portico -->
  <g fill="url(#glassGrad)" stroke="#64748b" stroke-width="1.5">
    <rect x="280" y="145" width="40" height="45" rx="3" />
    <rect x="380" y="145" width="40" height="45" rx="3" />
  </g>

  <!-- Grand Entrance Columns & Portal -->
  <rect x="285" y="200" width="130" height="70" fill="#0f172a" />
  <path d="M 285,200 Q 350,170 415,200 Z" fill="#0f172a" />
  <!-- Glass Doors -->
  <rect x="325" y="215" width="50" height="55" fill="url(#glassGrad)" stroke="#f8fafc" stroke-width="1.5" />
  <line x1="350" y1="215" x2="350" y2="270" stroke="#ffffff" stroke-width="2" />
  <!-- Columns -->
  <rect x="275" y="190" width="12" height="80" fill="#f8fafc" stroke="#94a3b8" />
  <rect x="413" y="190" width="12" height="80" fill="#f8fafc" stroke="#94a3b8" />

  <!-- School Bus Parked at Right Courtyard -->
  <g transform="translate(480, 290)">
    <!-- Bus Body -->
    <rect x="0" y="0" width="140" height="50" rx="8" fill="#eab308" stroke="#ca8a04" stroke-width="2" />
    <!-- Black stripe -->
    <rect x="0" y="25" width="140" height="8" fill="#0f172a" />
    <text x="70" y="32" font-family="'Cairo', sans-serif" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">حافلة مدرسية • SCHOOL BUS</text>
    <!-- Windows -->
    <rect x="10" y="6" width="22" height="15" rx="2" fill="#0284c7" />
    <rect x="38" y="6" width="22" height="15" rx="2" fill="#0284c7" />
    <rect x="66" y="6" width="22" height="15" rx="2" fill="#0284c7" />
    <rect x="94" y="6" width="22" height="15" rx="2" fill="#0284c7" />
    <!-- Wheels -->
    <circle cx="30" cy="50" r="12" fill="#0f172a" stroke="#64748b" stroke-width="2" />
    <circle cx="30" cy="50" r="5" fill="#e2e8f0" />
    <circle cx="110" cy="50" r="12" fill="#0f172a" stroke="#64748b" stroke-width="2" />
    <circle cx="110" cy="50" r="5" fill="#e2e8f0" />
    <!-- Headlight -->
    <polygon points="140,25 145,28 140,32" fill="#fbbf24" />
  </g>

  <!-- Modern Campus Badge Badge at Bottom-Left -->
  <rect x="25" y="320" width="210" height="60" rx="8" fill="rgba(15,23,42,0.92)" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" />
  <text x="38" y="342" font-family="'Cairo', sans-serif" font-size="12" font-weight="900" fill="#38bdf8">📍 الحرم المدرسي الرئيسي</text>
  <text x="38" y="360" font-family="'Cairo', sans-serif" font-size="10" font-weight="700" fill="#f8fafc">{city}</text>
  <text x="38" y="374" font-family="monospace" font-size="9" fill="#fbbf24">كود المنشأة: {code}</text>
</svg>'''
    return svg

# Generate all 30 logos and campus SVGs
for idx, sch in enumerate(SCHOOLS_SPEC, start=1):
    logo_svg = generate_school_logo_svg(sch)
    campus_svg = generate_school_campus_svg(sch)
    
    logo_filename = f"sch_{idx:02d}_logo.svg"
    campus_filename = f"sch_{idx:02d}_campus.svg"

    # Save to assets/images/schools/
    with open(os.path.join(IMG_SCHOOLS_DIR, logo_filename), "w", encoding="utf-8") as f:
        f.write(logo_svg)
    with open(os.path.join(IMG_SCHOOLS_DIR, campus_filename), "w", encoding="utf-8") as f:
        f.write(campus_svg)

    # Save mirror to frontend/images/schools/
    with open(os.path.join(FE_IMG_SCHOOLS_DIR, logo_filename), "w", encoding="utf-8") as f:
        f.write(logo_svg)
    with open(os.path.join(FE_IMG_SCHOOLS_DIR, campus_filename), "w", encoding="utf-8") as f:
        f.write(campus_svg)

    # Attach paths to school record
    sch["logo"] = f"/assets/images/schools/{logo_filename}"
    sch["campusPhoto"] = f"/assets/images/schools/{campus_filename}"
    sch["studentsCount"] = 100
    sch["teachersCount"] = 11
    sch["busesCount"] = 3
    sch["routesCount"] = 3
    sch["status"] = "ساري ومفعل 🟢"
    sch["stages"] = "الأساسية (1-9) + الثانوية (علمي/أدبي)"
    sch["currency"] = "ريال يمني (YER)"
    sch["fiscalYear"] = "من 01 سبتمبر إلى 30 يونيو"

print(f"Generated 30 SVG logos and 30 SVG campus illustrations in assets and frontend.")

# -----------------------------------------------------------------------------
# 3. YEMENI NAMES POOL & ATTRIBUTES
# -----------------------------------------------------------------------------
FIRST_NAMES_MALE = [
    "محمد", "أحمد", "عبد الله", "علي", "عمر", "خالد", "حسام", "إبراهيم", "طارق", "فؤاد",
    "سالم", "ماجد", "ياسر", "أنس", "حمزة", "معاذ", "بلال", "عثمان", "أيمن", "عمار",
    "عبد الرحمن", "عبد العزيز", "هشام", "مروان", "قاسم", "زياد", "نبيل", "وسيم", "رائد", "منير",
    "جمال", "صلاح", "صخر", "غسان", "أصيل", "ماهر", "براء", "لؤي", "يحيى", "وليد"
]
FIRST_NAMES_FEMALE = [
    "فاطمة", "سارة", "أروى", "مريم", "زينب", "نور", "هدى", "سمية", "بشرى", "بلقيس",
    "ريماس", "ملاك", "آية", "منى", "رغد", "إيمان", "ياسمين", "خلود", "شهد", "رزان",
    "وفاء", "صفاء", "سندس", "رنا", "دينا", "سلمى", "حنان", "نجلاء", "جميلة", "دعاء"
]
MIDDLE_NAMES = [
    "عبد الله", "محمد", "أحمد", "علي", "صالح", "حسن", "حسين", "ناصر", "سعيد", "قاسم",
    "عبد الرحمن", "سالم", "يحيى", "إسماعيل", "منصور", "عبده", "محمود", "عمر", "خالد", "طه"
]
FAMILY_NAMES = [
    "الصبري", "الحميري", "باعباد", "باوزير", "العنسي", "الشامي", "الكبسي", "المقالح", "الصعفاني", "المؤيد",
    "الشميري", "العريقي", "الصلوي", "باحيدرة", "الجاوي", "العبدلي", "الردفاني", "اليافعي", "الحبشي", "باجبير",
    "الغيثي", "السقاف", "الحداد", "المتوكل", "الأهدل", "شوعي", "الديلمي", "المرادي", "العرادة", "القاضي",
    "الحيمي", "الريمي", "الدبعي", "الحكيمي", "الزبيري", "السري", "الوزير", "الخولاني", "الهمداني", "الأكوع",
    "الجرافي", "الماوري", "بازرعة", "باديب", "بامطرف", "العطاس", "الكاف", "الجفري", "المحضار", "بارجاء",
    "بن شملان", "بن محفوظ", "بقشان", "السعدي", "الفضلي", "العولقي", "الصبيحي", "المشجري", "باحميد", "النعمان"
]

GRADES_CONFIG = [
    {"stage": "المرحلة الأساسية 📚", "grade": "الأول الابتدائي", "sec": "شعبة (أ)", "age": 7},
    {"stage": "المرحلة الأساسية 📚", "grade": "الأول الابتدائي", "sec": "شعبة (ب)", "age": 7},
    {"stage": "المرحلة الأساسية 📚", "grade": "الثاني الابتدائي", "sec": "شعبة (أ)", "age": 8},
    {"stage": "المرحلة الأساسية 📚", "grade": "الثاني الابتدائي", "sec": "شعبة (ب)", "age": 8},
    {"stage": "المرحلة الأساسية 📚", "grade": "الثالث الابتدائي", "sec": "شعبة (أ)", "age": 9},
    {"stage": "المرحلة الأساسية 📚", "grade": "الرابع الابتدائي", "sec": "شعبة (أ)", "age": 10},
    {"stage": "المرحلة الأساسية 📚", "grade": "الخامس الابتدائي", "sec": "شعبة (أ)", "age": 11},
    {"stage": "المرحلة الأساسية 📚", "grade": "السادس الابتدائي", "sec": "شعبة (أ)", "age": 12},
    {"stage": "المرحلة الأساسية 📚", "grade": "السابع أساسي", "sec": "شعبة (أ)", "age": 13},
    {"stage": "المرحلة الأساسية 📚", "grade": "الثامن أساسي", "sec": "شعبة (أ)", "age": 14},
    {"stage": "المرحلة الأساسية 📚", "grade": "التاسع أساسي", "sec": "شعبة (أ) - بنين", "age": 15},
    {"stage": "المرحلة الأساسية 📚", "grade": "التاسع أساسي", "sec": "شعبة (ب) - بنات", "age": 15},
    {"stage": "المرحلة الثانوية 🏫", "grade": "الأول الثانوي", "sec": "شعبة (أ) عام", "age": 16},
    {"stage": "المرحلة الثانوية 🏫", "grade": "الثاني الثانوي", "sec": "علمي (1)", "age": 17},
    {"stage": "المرحلة الثانوية 🏫", "grade": "الثاني الثانوي", "sec": "أدبي (1)", "age": 17},
    {"stage": "المرحلة الثانوية 🏫", "grade": "الثالث الثانوي", "sec": "علمي (1)", "age": 18},
    {"stage": "المرحلة الثانوية 🏫", "grade": "الثالث الثانوي", "sec": "أدبي (1)", "age": 18}
]

# -----------------------------------------------------------------------------
# 4. GENERATING 100 STUDENTS PER SCHOOL (3,000 Total)
# -----------------------------------------------------------------------------
ALL_STUDENTS = []
ALL_PARENTS = []
STUDENT_GLOBAL_IDX = 1

random.seed(2026)

for sch_idx, sch in enumerate(SCHOOLS_SPEC, start=1):
    sch_id = sch["id"]
    sch_code = sch["code"]
    gov = sch["governorate"]
    city = sch["city"]

    for st_num in range(1, 101):
        is_male = random.random() < 0.52
        first = random.choice(FIRST_NAMES_MALE) if is_male else random.choice(FIRST_NAMES_FEMALE)
        father = random.choice(MIDDLE_NAMES)
        gfather = random.choice(MIDDLE_NAMES)
        fam = random.choice(FAMILY_NAMES)
        full_name = f"{first} {father} {gfather} {fam}"

        std_code = f"STD-{sch_idx:02d}-{st_num:03d}"
        nat_id = f"1089{sch_idx:02d}{st_num:05d}"

        cfg = GRADES_CONFIG[st_num % len(GRADES_CONFIG)]
        birth_year = 2026 - cfg["age"]
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        dob = f"{birth_year}-{birth_month:02d}-{birth_day:02d}"

        parent_title = "الشيخ" if random.random() < 0.25 else ("م." if random.random() < 0.45 else "أ.")
        parent_name = f"{parent_title} {father} {gfather} {fam}"
        parent_phone = f"77{random.randint(1000000, 9999999)}"

        # Tuition & Status
        r = random.random()
        if r < 0.76:
            status = "مسدد بالكامل 🟢"
            fin_status = "مسدد بالكامل 🟢"
            balance = 0
        elif r < 0.88:
            status = "أقساط مجدولة 🟡"
            fin_status = "متبقي قسط أخير 🟡"
            balance = random.choice([50000, 80000, 120000])
        elif r < 0.97:
            status = "منحة تفوق 🔵"
            fin_status = "معفى بمنحة دراسية 🔵"
            balance = 0
        else:
            status = "منسحب 🔴"
            fin_status = "ملف مؤرشف 🔴"
            balance = 0

        gpa = round(random.uniform(84.0, 99.8), 1)

        std_obj = {
            "id": std_code,
            "student_number": std_code,
            "academicNo": std_code,
            "name": full_name,
            "full_name": full_name,
            "nationalId": nat_id,
            "father_national_id": nat_id[:8] + "001",
            "schoolId": sch_id,
            "schoolCode": sch_code,
            "schoolName": sch["name"],
            "gender": "ذكر" if is_male else "أنثى",
            "parentName": parent_name,
            "parentPhone": parent_phone,
            "phone": parent_phone,
            "dateOfBirth": dob,
            "dob": dob,
            "place_of_birth": gov,
            "residence": f"{gov} - {city}",
            "address": f"{gov} - {city} - شارع النصر",
            "nationality": "يمني 🇾🇪",
            "stage": cfg["stage"],
            "grade": cfg["grade"],
            "section": cfg["sec"],
            "grade_level": f"{cfg['grade']} - {cfg['sec']}",
            "current_grade_level": cfg["grade"],
            "enrollmentDate": "2026-08-15",
            "date": "2026-08-15",
            "status": status,
            "financial_status": fin_status,
            "balance": balance,
            "gpa": gpa,
            "bloodType": random.choice(["O+", "A+", "B+", "AB+", "O-"]),
            "busSubscribed": random.choice(["نعم (مشترك بالنقل 🚌)", "لا (خاص 🚗)"])
        }
        ALL_STUDENTS.append(std_obj)

        # Parent directory record (deduplicated by phone/name)
        if st_num % 3 == 0:
            ALL_PARENTS.append({
                "id": f"PAR-{sch_idx:02d}-{st_num:03d}",
                "name": parent_name,
                "phone": parent_phone,
                "nationalId": nat_id[:8] + "001",
                "relation": "ولي أمر (أب)",
                "studentName": full_name,
                "studentCode": std_code,
                "schoolCode": sch_code,
                "schoolName": sch["name"],
                "address": f"{gov} - {city}",
                "job": random.choice(["مهندس مدني", "طبيب استشاري", "تاجر ورجل أعمال", "أستاذ جامعي", "محامٍ ومستشار", "مسؤول حكومي"])
            })

        STUDENT_GLOBAL_IDX += 1

print(f"Generated {len(ALL_STUDENTS)} students across all 30 schools (100 per school).")
print(f"Generated {len(ALL_PARENTS)} parent directory profiles.")

# -----------------------------------------------------------------------------
# 5. GENERATING EMPLOYEES & TEACHERS (~330 Total)
# -----------------------------------------------------------------------------
ALL_EMPLOYEES = []
STAFF_ROLES = [
    {"role": "مدير المدرسة والمدير العام", "dept": "الإدارة المدرسية", "salary": 650000, "spec": "إدارة تربوية ونظم تعليمية"},
    {"role": "وكيل شؤون الطلاب والامتحانات", "dept": "شؤون الطلاب", "salary": 450000, "spec": "إرشاد تربوي وقياس وتقويم"},
    {"role": "محاسب مالي رئيسي", "dept": "الشؤون المالية", "salary": 400000, "spec": "محاسبة مالية وتدقيق"},
    {"role": "أخصائي اجتماعي ونفسي", "dept": "الإرشاد والتوجيه", "salary": 340000, "spec": "علم نفس وإرشاد مدرسي"},
    {"role": "معلم أول قرآن كريم وإسلامية", "dept": "الكادر التعليمي", "salary": 380000, "spec": "دراسات إسلامية وقراءات"},
    {"role": "معلم أول لغة عربية وأدب", "dept": "الكادر التعليمي", "salary": 390000, "spec": "لغة عربية وبلاغة"},
    {"role": "معلم أول لغة إنجليزية", "dept": "الكادر التعليمي", "salary": 420000, "spec": "لغويات وترجمة إنجليزية"},
    {"role": "معلم أول رياضيات متقدمة", "dept": "الكادر التعليمي", "salary": 430000, "spec": "رياضيات تطبيقية وإحصاء"},
    {"role": "معلم أول فيزياء وعلوم", "dept": "الكادر التعليمي", "salary": 410000, "spec": "فيزياء ذرية وعلوم عامة"},
    {"role": "معلم أول كيمياء وأحياء", "dept": "الكادر التعليمي", "salary": 410000, "spec": "كيمياء حيوية وبيولوجيا"},
    {"role": "معلم حاسوب وذكاء اصطناعي", "dept": "الكادر التعليمي", "salary": 440000, "spec": "علوم حاسوب وروبوتات"},
    {"role": "مشرف النقل والمواصلات والصحة", "dept": "الخدمات المساندة", "salary": 320000, "spec": "إدارة أساطيل وإسعافات"}
]

for sch_idx, sch in enumerate(SCHOOLS_SPEC, start=1):
    sch_id = sch["id"]
    sch_code = sch["code"]
    for emp_idx, role_cfg in enumerate(STAFF_ROLES, start=1):
        if emp_idx == 1:
            emp_name = sch["principal"]
        else:
            first = random.choice(FIRST_NAMES_MALE) if emp_idx % 4 != 0 else random.choice(FIRST_NAMES_FEMALE)
            emp_name = f"أ. {first} {random.choice(MIDDLE_NAMES)} {random.choice(FAMILY_NAMES)}"

        emp_code = f"EMP-{sch_idx:02d}-{emp_idx:02d}"
        ALL_EMPLOYEES.append({
            "id": emp_code,
            "code": emp_code,
            "name": emp_name,
            "role": role_cfg["role"],
            "job": role_cfg["role"],
            "dept": role_cfg["dept"],
            "specialization": role_cfg["spec"],
            "schoolId": sch_id,
            "schoolCode": sch_code,
            "schoolName": sch["name"],
            "nationalId": f"1000{sch_idx:02d}{emp_idx:04d}",
            "phone": f"77{random.randint(1100000, 9900000)}",
            "email": f"staff.{sch_idx}_{emp_idx}@edu.ye",
            "salary": f"{role_cfg['salary']:,} ر.ي",
            "salaryNum": role_cfg["salary"],
            "contract": "عقد دائم سنوي معتمد",
            "hireDate": f"202{random.randint(0,4)}-08-15",
            "status": "على رأس العمل 🟢"
        })

print(f"Generated {len(ALL_EMPLOYEES)} employees and teachers for all 30 schools.")

# -----------------------------------------------------------------------------
# 6. GENERATING TRANSPORTATION (Buses & Routes) (~100 Buses & ~100 Routes)
# -----------------------------------------------------------------------------
ALL_BUSES = []
ALL_ROUTES = []

BUS_MODELS = [
    {"model": "تويوتا كوستر 2024", "cap": 32},
    {"model": "مرسيدس بنز سبرينتر 2023", "cap": 48},
    {"model": "هيونداي كاونتي سوبر 2024", "cap": 30},
    {"model": "ميتسوبيشي روزا ديلوكس 2023", "cap": 35}
]

DRIVER_NAMES = [
    "عماد عبد الله القاضي", "صالح محمد الحيمي", "فارس قاسم الريمي", "عادل منصور الحكيمي",
    "جمال يحيى العريقي", "مروان سعيد باعباد", "وضاح ناصر الصلوي", "طارق أحمد الشميري",
    "فؤاد حسن باوزير", "سلطان علي المرادي", "رشيد قائد السقاف", "عصام عبد السلام الأهدل"
]
MATRON_NAMES = [
    "أ. مريم صالح", "أ. هدى ناصر", "أ. سميرة علي", "أ. بلقيس عبده", "أ. أروى عبد الله", "أ. وفاء قاسم"
]

for sch_idx, sch in enumerate(SCHOOLS_SPEC, start=1):
    sch_id = sch["id"]
    sch_code = sch["code"]
    gov = sch["governorate"]
    city = sch["city"]

    for b_idx in range(1, 4): # 3 buses per school
        bus_id = f"BUS-{sch_idx:02d}-{b_idx:02d}"
        model_info = BUS_MODELS[(sch_idx + b_idx) % len(BUS_MODELS)]
        plate_no = f"{random.randint(1000, 9999)}-{gov[0]} (حافلة {b_idx})"
        driver = DRIVER_NAMES[(sch_idx * 3 + b_idx) % len(DRIVER_NAMES)]
        matron = MATRON_NAMES[(sch_idx + b_idx) % len(MATRON_NAMES)]
        driver_phone = f"77{random.randint(1000000, 8999999)}"

        ALL_BUSES.append({
            "id": bus_id,
            "plate": plate_no,
            "model": model_info["model"],
            "capacity": model_info["cap"],
            "driver": driver,
            "phone": driver_phone,
            "matron": matron,
            "schoolId": sch_id,
            "schoolCode": sch_code,
            "schoolName": sch["name"],
            "checkDate": "2027-01-15",
            "status": "جاهزة بالخدمة 🟢" if b_idx < 3 else "صيانة دورية 🟡"
        })

        rot_id = f"ROT-{sch_idx:02d}-{b_idx:02d}"
        rot_name = f"خط {city} - مسار {b_idx} (الحي السكني)"
        ALL_ROUTES.append({
            "id": rot_id,
            "code": f"LINE-{sch_idx:02d}-{b_idx:02d}",
            "name": rot_name,
            "zone": f"قطاع {gov} {b_idx}",
            "stops": random.randint(5, 9),
            "bus": f"حافلة #{b_idx} ({plate_no})",
            "time": f"06:{30 + b_idx * 10:02d} ص",
            "driver": driver,
            "schoolId": sch_id,
            "schoolCode": sch_code,
            "status": "منتظم ونشط 🟢"
        })

print(f"Generated {len(ALL_BUSES)} buses and {len(ALL_ROUTES)} routes.")

# -----------------------------------------------------------------------------
# 7. GENERATING COMPLETE DATA FOR ALL 76 MODULES (window.DB)
# -----------------------------------------------------------------------------
CORE_DATA = {
    # 1. المدارس والمنشآت
    "schoolsList": SCHOOLS_SPEC,

    # 2. الطلاب والقبول
    "students": ALL_STUDENTS,
    "studentsData": ALL_STUDENTS,
    "parents": ALL_PARENTS,

    # 3. الموظفون والكادر
    "employees": ALL_EMPLOYEES,
    "employeesData": ALL_EMPLOYEES,

    # 4. النقل والمواصلات
    "buses": ALL_BUSES,
    "transportRoutes": ALL_ROUTES,

    # 5. الحسابات والمستخدمين
    "users": [
        # SaaS Super Admins
        {
            "id": "USR-SYS-01", "username": "saas_admin", "password": "123",
            "name": "م. عبد الله الشامي", "role": "saas_admin", "roleName": "مدير عام النظام السحابي (Super Admin)",
            "portal": "saas", "dept": "إدارة الأنظمة السحابية والسيادية", "phone": "777112233",
            "nationalId": "10001000101", "email": "superadmin@saas-cloud.edu.ye", "status": "نشط 🟢"
        },
        {
            "id": "USR-SYS-02", "username": "db_admin", "password": "123",
            "name": "م. طارق المعمري", "role": "db_admin", "roleName": "مهندس البنية وقواعد البيانات (DBA)",
            "portal": "saas", "dept": "قسم البنية السحابية والنسخ الاحتياطي", "phone": "777889900",
            "nationalId": "10001000102", "email": "dba@saas-cloud.edu.ye", "status": "نشط 🟢"
        },
        {
            "id": "USR-SYS-03", "username": "soc_guardian", "password": "123",
            "name": "الرائد صقر الحميري (Cyber Guardian AI)", "role": "security_officer", "roleName": "ضابط أمن المعلومات والسيبرانية",
            "portal": "saas", "dept": "مركز العمليات السيبرانية والدفاع الرقمي", "phone": "777009988",
            "nationalId": "10001000103", "email": "soc@saas-cloud.edu.ye", "status": "نشط 🟢"
        }
    ],

    # 6. الهيكل الأكاديمي والفصول
    "stages": [
        {"id": "STG-01", "code": "STG-KG", "name": "مرحلة رياض الأطفال (KG)", "grades": "روضة 1، روضة 2، تمهيدي", "sectionsCount": 6, "studentsCount": 180, "head": "أ. صفاء المقالح", "status": "نشط 🟢"},
        {"id": "STG-02", "code": "STG-PRI", "name": "المرحلة الأساسية (صفوف 1-6)", "grades": "الصف الأول حتى السادس الأساسي", "sectionsCount": 18, "studentsCount": 1200, "head": "أ. منير الشميري", "status": "نشط 🟢"},
        {"id": "STG-03", "code": "STG-MID", "name": "المرحلة الإعدادية (صفوف 7-9)", "grades": "الصف السابع، الثامن، التاسع أساسي", "sectionsCount": 12, "studentsCount": 900, "head": "د. عادل العنسي", "status": "نشط 🟢"},
        {"id": "STG-04", "code": "STG-SEC", "name": "المرحلة الثانوية (صفوف 10-12)", "grades": "الأول الثانوي، الثاني والثالث (علمي/أدبي)", "sectionsCount": 10, "studentsCount": 720, "head": "أ. عبد القادر الحيمي", "status": "نشط 🟢"}
    ],
    "classrooms": [
        {"id": "CLS-101", "code": "ROOM-A1", "name": "قاعة الخوارزمي الذكية", "building": "مبنى (أ) الأكاديمي", "floor": "الدور الأول", "capacity": 35, "smartBoard": "نعم (شاشة تفاعلية 4K)", "status": "متاح ونشط 🟢"},
        {"id": "CLS-102", "code": "ROOM-A2", "name": "قاعة ابن الهيثم للعلوم", "building": "مبنى (أ) الأكاديمي", "floor": "الدور الأول", "capacity": 35, "smartBoard": "نعم (شاشة تفاعلية 4K)", "status": "متاح ونشط 🟢"},
        {"id": "CLS-103", "code": "ROOM-B1", "name": "مختبر الحاسوب والذكاء الاصطناعي", "building": "مبنى (ب) التقني", "floor": "الدور الثاني", "capacity": 40, "smartBoard": "معمل روبوتات متكامل", "status": "متاح ونشط 🟢"},
        {"id": "CLS-104", "code": "ROOM-B2", "name": "قاعة المتنبي للغات والآداب", "building": "مبنى (ب) الأكاديمي", "floor": "الدور الثاني", "capacity": 30, "smartBoard": "نعم", "status": "متاح ونشط 🟢"},
        {"id": "CLS-105", "code": "ROOM-C1", "name": "مدرج الأقصى الكبرى للاجتماعات", "building": "المبنى الرئيسي", "floor": "الدور الأرضي", "capacity": 250, "smartBoard": "نظام سينمائي ومسرحي", "status": "متاح ونشط 🟢"}
    ],
    "sections": [
        {"id": "SEC-01", "code": "SEC-1A", "name": "أول ابتدائي (أ) - بنين", "stage": "المرحلة الأساسية 📚", "grade": "الأول الابتدائي", "capacity": 30, "enrolled": 28, "advisor": "أ. فاطمة باحيدرة", "status": "مكتمل 🟢"},
        {"id": "SEC-02", "code": "SEC-1B", "name": "أول ابتدائي (ب) - بنات", "stage": "المرحلة الأساسية 📚", "grade": "الأول الابتدائي", "capacity": 30, "enrolled": 27, "advisor": "أ. أروى المقالح", "status": "مكتمل 🟢"},
        {"id": "SEC-03", "code": "SEC-9A", "name": "تاسع أساسي (أ) - وزاري", "stage": "المرحلة الإعدادية 📚", "grade": "التاسع أساسي", "capacity": 35, "enrolled": 34, "advisor": "د. سالم الحميري", "status": "مكتمل 🟢"},
        {"id": "SEC-04", "code": "SEC-12S", "name": "ثالث ثانوي (علمي 1) - نخبة", "stage": "المرحلة الثانوية 🏫", "grade": "الثالث الثانوي", "capacity": 32, "enrolled": 31, "advisor": "أ. عبد الرحمن الصبري", "status": "مكتمل 🟢"}
    ],
    "subjects": [
        {"id": "SUB-01", "code": "QUR-01", "name": "القرآن الكريم والتجويد", "stage": "كافة المراحل", "classesPerWeek": 4, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-02", "code": "ARB-01", "name": "اللغة العربية وقواعد النحو", "stage": "كافة المراحل", "classesPerWeek": 6, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-03", "code": "ENG-01", "name": "اللغة الإنجليزية (Oxford)", "stage": "كافة المراحل", "classesPerWeek": 5, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-04", "code": "MTH-01", "name": "الرياضيات المتقدمة والهندسة", "stage": "كافة المراحل", "classesPerWeek": 6, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-05", "code": "SCI-01", "name": "العلوم العامة والتجريبية", "stage": "المرحلة الأساسية", "classesPerWeek": 4, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-06", "code": "PHY-01", "name": "الفيزياء النظرية والعملية", "stage": "المرحلة الثانوية", "classesPerWeek": 4, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-07", "code": "CHM-01", "name": "الكيمياء العضوية والمخبرية", "stage": "المرحلة الثانوية", "classesPerWeek": 4, "maxScore": 100, "passScore": 50, "status": "معتمد وزارياً 🟢"},
        {"id": "SUB-08", "code": "CMP-01", "name": "الحاسوب والذكاء الاصطناعي", "stage": "كافة المراحل", "classesPerWeek": 3, "maxScore": 100, "passScore": 50, "status": "معتمد إثرائياً 🟢"}
    ],

    # 7. الرسوم والأقساط
    "feeCategories": [
        {"id": "FEE-01", "code": "FEE-TUIT", "name": "الرسوم الدراسية السنوية (Tuition)", "amount": 450000, "currency": "YER", "period": "سنوي (4 أقساط)", "mandatory": "إلزامي 🟢"},
        {"id": "FEE-02", "code": "FEE-REG", "name": "رسوم القيد والتسجيل الوزاري", "amount": 35000, "currency": "YER", "period": "تدفع مرة واحدة", "mandatory": "إلزامي 🟢"},
        {"id": "FEE-03", "code": "FEE-TRAN", "name": "اشتراك النقل والمواصلات المدرسي", "amount": 120000, "currency": "YER", "period": "فصلي", "mandatory": "اختياري 🔵"},
        {"id": "FEE-04", "code": "FEE-BOOK", "name": "الحقيبة المدرسية والكتب المطورة", "amount": 40000, "currency": "YER", "period": "سنوي", "mandatory": "إلزامي 🟢"},
        {"id": "FEE-05", "code": "FEE-ACT", "name": "الأنشطة الطلابية والمختبرات الذكية", "amount": 25000, "currency": "YER", "period": "سنوي", "mandatory": "إلزامي 🟢"}
    ],
    "installmentPlans": [
        {"id": "INS-01", "name": "القسط الأول (عند بدء التسجيل)", "pct": "30%", "dueDate": "2026-08-20", "notes": "رسوم التسجيل والقسط الأول"},
        {"id": "INS-02", "name": "القسط الثاني (منتصف الفصل الأول)", "pct": "25%", "dueDate": "2026-11-10", "notes": "قبل اختبارات نهاية الفصل الأول"},
        {"id": "INS-03", "name": "القسط الثالث (بداية الفصل الثاني)", "pct": "25%", "dueDate": "2027-02-05", "notes": "عند انطلاق الفصل الدراسي الثاني"},
        {"id": "INS-04", "name": "القسط الرابع (النهائي والتصفية)", "pct": "20%", "dueDate": "2027-04-20", "notes": "قبل إصدار شهادات نهاية العام"}
    ],

    # 8. الكنترول وقاعات الامتحانات
    "examHalls": [
        {"id": "HAL-01", "code": "HAL-QUD", "name": "قاعة القدس الكبرى للامتحانات", "capacity": 80, "building": "المبنى الأكاديمي الرئيسي", "chief": "د. سالم الحميري", "invigilators": 4, "status": "جاهزة ومجهزة 🟢"},
        {"id": "HAL-02", "code": "HAL-YEM", "name": "قاعة اليمن السعيد للاختبارات", "capacity": 60, "building": "مبنى المرحلة الثانوية", "chief": "أ. عبد الرحمن الصبري", "invigilators": 3, "status": "جاهزة ومجهزة 🟢"},
        {"id": "HAL-03", "code": "HAL-AML", "name": "قاعة الأمل النموذجية", "capacity": 50, "building": "مبنى المرحلة الأساسية", "chief": "أ. فاطمة باحيدرة", "invigilators": 3, "status": "جاهزة ومجهزة 🟢"}
    ],

    # 9. المخازن والعهد المدرسية
    "inventoryItems": [
        {"id": "INV-01", "code": "BK-MTH-09", "name": "كتاب الرياضيات المطورة (الصف التاسع)", "category": "الكتب المدرسية", "stock": 450, "unit": "نسخة", "minAlert": 50, "status": "متوفر بمستودع أ 🟢"},
        {"id": "INV-02", "code": "BK-ENG-03", "name": "سلسلة أوكسفورد لتعليم الإنجليزية (KG)", "category": "الكتب المدرسية", "stock": 380, "unit": "حقيبة", "minAlert": 40, "status": "متوفر بمستودع أ 🟢"},
        {"id": "INV-03", "code": "IT-TAB-10", "name": "أجهزة لوحية ذكية لمعمل الحاسوب (10 بوصة)", "category": "الأجهزة التقنية", "stock": 85, "unit": "جهاز", "minAlert": 10, "status": "متوفر بمستودع ب 🟢"},
        {"id": "INV-04", "code": "LAB-MIC-01", "name": "مجهر ضوئي إلكتروني رقمي للمختبرات", "category": "أدوات المختبرات", "stock": 25, "unit": "مجهر", "minAlert": 5, "status": "متوفر بمستودع ج 🟢"},
        {"id": "INV-05", "code": "UNF-PRI-01", "name": "الزي المدرسي الموحد (المرحلة الأساسية)", "category": "الزي المدرسي", "stock": 620, "unit": "بدلة", "minAlert": 100, "status": "متوفر بمستودع د 🟢"}
    ],

    # 10. العملات والبنوك والخزن
    "currencies": [
        {"code": "YER", "name": "ريال يمني (عملة الأساس)", "rate": 1.0, "symbol": "ر.ي", "isBase": True, "status": "نشط 🟢"},
        {"code": "USD", "name": "دولار أمريكي", "rate": 530.0, "symbol": "$", "isBase": False, "status": "نشط 🟢"},
        {"code": "SAR", "name": "ريال سعودي", "rate": 140.0, "symbol": "ر.س", "isBase": False, "status": "نشط 🟢"}
    ],
    "banks": [
        {"id": "BNK-01", "code": "CAC", "name": "بنك التسليف التعاوني والزراعي (CAC Bank)", "accountNo": "1001-2026-9901", "currency": "YER", "balance": 48500000, "status": "نشط ومعتمد 🟢"},
        {"id": "BNK-02", "code": "KRM", "name": "بنك الكريمي للتمويل الأصغر الإسلامي", "accountNo": "7701-3321-4455", "currency": "YER", "balance": 35200000, "status": "نشط ومعتمد 🟢"},
        {"id": "BNK-03", "code": "TDH", "name": "بنك التضامن الإسلامي الدولي", "accountNo": "5002-8812-7711", "currency": "YER", "balance": 24800000, "status": "نشط ومعتمد 🟢"},
        {"id": "BNK-04", "code": "YKB", "name": "بنك اليمن والكويت", "accountNo": "3004-9912-3322", "currency": "USD", "balance": 45000, "status": "نشط ومعتمد 🟢"}
    ],
    "cashboxes": [
        {"id": "CSH-01", "name": "الخزينة الرئيسية للمركز المالي", "custodian": "أ. سارة المحاسبة", "currency": "YER", "balance": 6450000, "ceiling": 15000000, "status": "مفتوحة ونشطة 🟢"},
        {"id": "CSH-02", "name": "صندوق استقبال المقبوضات اليومية", "custodian": "أ. رائد العريقي", "currency": "YER", "balance": 1820000, "ceiling": 5000000, "status": "مفتوحة ونشطة 🟢"},
        {"id": "CSH-03", "name": "عهدة النثريات والمشتريات العاجلة", "custodian": "أ. محمود الدبعي", "currency": "YER", "balance": 450000, "ceiling": 1000000, "status": "مفتوحة ونشطة 🟢"}
    ],

    # 11. الأنشطة والمسابقات المدرسية
    "activities": [
        {"id": "ACT-01", "code": "ACT-QURAN", "name": "المسابقة السنوية الكبرى لحفظ وتلاوة القرآن الكريم", "date": "2026-10-15", "supervisor": "أ. رضوان المحيا", "location": "مدرج الأقصى الكبرى", "participants": 120, "status": "قيد التنفيذ 🟢"},
        {"id": "ACT-02", "code": "ACT-ROBOT", "name": "الأولمبياد المدرسي للروبوت والذكاء الاصطناعي", "date": "2026-11-25", "supervisor": "م. طارق المعمري", "location": "معمل الابتكار والتقنية", "participants": 45, "status": "معتمد ومجدول 🔵"},
        {"id": "ACT-03", "code": "ACT-SOCCER", "name": "دوري أبطال المدارس الرياضي لكرة القدم", "date": "2026-12-05", "supervisor": "أ. محمود الدبعي", "location": "الملعب العشبي الرئيسي", "participants": 180, "status": "معتمد ومجدول 🔵"},
        {"id": "ACT-04", "code": "ACT-SCI", "name": "معرض الاختراعات والتجارب العلمية الحديثة", "date": "2027-01-20", "supervisor": "أ. سمير الأهدل", "location": "قاعة المعارض المركزية", "participants": 80, "status": "معتمد ومجدول 🔵"}
    ],

    # 12. سندات الصرف والقبض
    "vouchers": [
        {"id": "VOU-2026-001", "type": "سند قبض رسوم 📥", "date": "2026-08-20", "beneficiary": "أحمد علي باعباد (STD-01-001)", "amount": 150000, "currency": "YER", "desc": "سداد القسط الأول للعام 2026/2027", "cashbox": "الخزينة الرئيسية", "status": "معتمد ومرحل 🟢"},
        {"id": "VOU-2026-002", "type": "سند صرف مشتريات 📤", "date": "2026-08-22", "beneficiary": "مكتبة ومطابع دار الكتب", "amount": 420000, "currency": "YER", "desc": "شراء الكتب المدرسية والمستلزمات الورقية", "cashbox": "الخزينة الرئيسية", "status": "معتمد ومرحل 🟢"},
        {"id": "VOU-2026-003", "type": "سند صرف صيانة 📤", "date": "2026-08-25", "beneficiary": "مركز الفجر لصيانة الحافلات", "amount": 95000, "currency": "YER", "desc": "صيانة وتجهيز حافلات النقل المدرسي", "cashbox": "عهدة النثريات", "status": "معتمد ومرحل 🟢"}
    ],
    "vouchersData": [],

    # 13. سجلات الرقابة الأمنية وسجل العمليات
    "auditLogs": [
        {"id": "AUD-01", "timestamp": "2026-10-28 08:00:15", "user": "saas_admin", "action": "تسجيل دخول مشرف النظام السحابي", "ip": "127.0.0.1", "device": "Windows Workstation (Chrome 122)", "status": "نجاح 🟢"},
        {"id": "AUD-02", "timestamp": "2026-10-28 08:15:30", "user": "admin_motafawiqeen", "action": "تحديث بيانات منشأة مدرسة المتفوقين", "ip": "127.0.0.1", "device": "Windows Workstation", "status": "نجاح 🟢"},
        {"id": "AUD-03", "timestamp": "2026-10-28 09:30:10", "user": "Cyber Guardian AI", "action": "فحص وتحصين البنية وتشفير الحقول الحساسة", "ip": "127.0.0.1", "device": "SOC Autonomous Engine", "status": "سليم 100% 🛡️"}
    ],

    # 14. إعدادات النظام والسنة الأكاديمية
    "systemSettingsData": {
        "systemName": "نظام الإدارة المدرسية السحابي الذكي (School Smart ERP Multi-Tenant)",
        "currentAcademicYear": "2026/2027",
        "currentSemester": "الفصل الدراسي الأول",
        "activeSchoolsCount": 30,
        "totalStudentsEnrolled": 3000,
        "backupSchedule": "يومي تلقائي عند الساعة 02:00 صباحاً",
        "encryptionStandard": "AES-256-GCM Military Grade",
        "socGuardianStatus": "مفعل 24/7 (Cyber Guardian AI v2.5)"
    }
}

# Attach Principal Accounts for each of the 30 schools to users
for sch in SCHOOLS_SPEC:
    CORE_DATA["users"].append({
        "id": f"USR-PRIN-{sch['id']}",
        "username": f"admin_{sch['id'].lower().replace('-', '_')}",
        "password": "123",
        "name": sch["principal"],
        "role": "school_admin",
        "roleName": "مدير المنشأة والفرع",
        "portal": "school",
        "isPrincipal": True,
        "schoolId": sch["id"],
        "schoolCode": sch["code"],
        "schoolName": sch["name"],
        "branch": sch["city"],
        "dept": "الإدارة المدرسية",
        "phone": sch["phone"].split("|")[0].strip(),
        "nationalId": f"1000{sch['id'][-2:]}001",
        "email": sch["email"],
        "status": "نشط 🟢"
    })

CORE_DATA["vouchersData"] = CORE_DATA["vouchers"]
CORE_DATA["usersData"] = CORE_DATA["users"]

print("Assembled all 76 UI modules and database keys successfully.")

# -----------------------------------------------------------------------------
# 8. WRITE JAVASCRIPT MASTER DATA BUNDLE
# -----------------------------------------------------------------------------
js_content = f"""/**
 * SCHOOL SMART ERP - MASTER 30 SCHOOLS HIGH-VOLUME DATASET
 * Contains 30 Complete Schools, 3,000 Registered Students (100 per school),
 * Staff, Buses, Routes, and All 76 UI Modules.
 * Generated: {datetime.now().isoformat()}
 */

(function() {{
    if (!window.DB) window.DB = {{}};

    const MASTER_DATA = {json.dumps(CORE_DATA, ensure_ascii=False, indent=2)};

    // Hydrate window.DB safely
    for (const key of Object.keys(MASTER_DATA)) {{
        window.DB[key] = MASTER_DATA[key];
    }}

    // Export Master Injector Function
    window.ensureMaster30SchoolsData = function() {{
        for (const key of Object.keys(MASTER_DATA)) {{
            if (!window.DB[key] || window.DB[key].length === 0) {{
                window.DB[key] = MASTER_DATA[key];
            }}
        }}
    }};

    // Ensure DOMContentLoaded synchronization
    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', window.ensureMaster30SchoolsData);
    }} else {{
        window.ensureMaster30SchoolsData();
    }}

    console.log("🏫 [School Smart ERP] Successfully loaded 30 Schools, 3,000 Students, Staff, Transport, and 76 System Modules!");
}})();
"""

js_path = os.path.join(JS_DIR, "data_30_schools.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Wrote master JavaScript data bundle to {js_path} ({len(js_content):,} bytes).")

# -----------------------------------------------------------------------------
# 9. SEED SQLITE DATABASE (secure_school.db)
# -----------------------------------------------------------------------------
print(f"Connecting to SQLite database at {DB_PATH}...")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 9.1 Seed Schools
cursor.execute("DELETE FROM schools;")
for sch in SCHOOLS_SPEC:
    sch_uid = str(uuid.uuid4()).replace("-", "")
    cursor.execute("""
        INSERT INTO schools (id, name, governorate_district, center_type, directorate_location, school_location, manager_name, manager_phone, it_manager, is_active, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sch_uid,
        sch["name"],
        f"{sch['governorate']} - {sch['district']}",
        "مختلط (بنين وبنات)",
        sch["district"],
        sch["address"],
        sch["principal"],
        sch["phone"].split("|")[0].strip(),
        "مهندس البنية والأنظمة",
        1,
        datetime.now().isoformat(),
        datetime.now().isoformat()
    ))
    sch["sqlite_id"] = sch_uid

# 9.2 Seed Users (Principals + Admins)
cursor.execute("DELETE FROM users;")
cursor.execute("""
    INSERT INTO users (id, username, hashed_password, role, phone, is_active, school_id, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    str(uuid.uuid4()).replace("-", ""),
    "saas_admin",
    "$2b$12$e6mZc0vV6H4lqg37EeVb1u5yD7/m4l2vV7hO8a.k9q3.b1u5yD7/m", # mock or argon2 hash
    "super_admin",
    "777112233",
    1,
    SCHOOLS_SPEC[0]["sqlite_id"],
    datetime.now().isoformat(),
    datetime.now().isoformat()
))

for sch in SCHOOLS_SPEC:
    cursor.execute("""
        INSERT INTO users (id, username, hashed_password, role, phone, is_active, school_id, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        str(uuid.uuid4()).replace("-", ""),
        f"admin_{sch['id'].lower().replace('-', '_')}",
        "$2b$12$e6mZc0vV6H4lqg37EeVb1u5yD7/m4l2vV7hO8a.k9q3.b1u5yD7/m",
        "school_admin",
        sch["phone"].split("|")[0].strip(),
        1,
        sch["sqlite_id"],
        datetime.now().isoformat(),
        datetime.now().isoformat()
    ))

# 9.3 Seed Subjects Catalog
cursor.execute("DELETE FROM subjects_catalog;")
sub_ids = []
for sub in CORE_DATA["subjects"]:
    s_uid = str(uuid.uuid4()).replace("-", "")
    cursor.execute("""
        INSERT INTO subjects_catalog (id, name, grade_level, school_id, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        s_uid,
        sub["name"],
        sub["stage"],
        SCHOOLS_SPEC[0]["sqlite_id"],
        datetime.now().isoformat(),
        datetime.now().isoformat()
    ))
    sub_ids.append(s_uid)

# 9.4 Seed 3,000 Students into SQLite
cursor.execute("DELETE FROM students;")
cursor.execute("DELETE FROM attendance_records;")
cursor.execute("DELETE FROM grades;")
cursor.execute("DELETE FROM financial_records;")

sch_map = {s["id"]: s["sqlite_id"] for s in SCHOOLS_SPEC}

student_rows = []
for st in ALL_STUDENTS:
    st_uid = str(uuid.uuid4()).replace("-", "")
    target_sch_sqlite = sch_map.get(st["schoolId"], SCHOOLS_SPEC[0]["sqlite_id"])
    student_rows.append((
        st_uid,
        st["full_name"],
        st["student_number"],
        None,
        st["parentPhone"],
        st["dob"],
        st["place_of_birth"],
        st["residence"],
        st["current_grade_level"],
        st["father_national_id"],
        st["gender"],
        st["nationality"],
        target_sch_sqlite,
        datetime.now().isoformat(),
        datetime.now().isoformat()
    ))

cursor.executemany("""
    INSERT INTO students (id, full_name, student_number, parent_id, parent2_phone, date_of_birth, place_of_birth, residence, current_grade_level, father_national_id, gender, nationality, school_id, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", student_rows)

conn.commit()
print(f"Committed {len(student_rows)} students into SQLite 'students' table.")

# 9.5 Verify counts in SQLite
cursor.execute("SELECT COUNT(*) FROM schools;")
count_schools = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM users;")
count_users = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM students;")
count_students = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM subjects_catalog;")
count_subjects = cursor.fetchone()[0]

conn.close()

print("\n" + "="*60)
print("🎯 MASTER DATA SEEDING SUMMARY:")
print(f" - Schools in SQLite: {count_schools} (SCH-01 to SCH-30)")
print(f" - Users in SQLite: {count_users}")
print(f" - Students in SQLite: {count_students} (Exactly 100 students per school)")
print(f" - Subjects in Catalog: {count_subjects}")
print(f" - SVG Logos Created: 30 vector logos in assets/images/schools/")
print(f" - SVG Campus Created: 30 vector illustrations in assets/images/schools/")
print(f" - Master JS Data Bundle: {js_path}")
print("="*60 + "\n")
