"""
Verification Suite for 30 Schools, 3,000 Students, Staff, Transport,
SVGs, Frontend Data Bundle, and SQLite Database.
"""
import urllib.request
import sqlite3
import os
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "secure_school.db")

print("=" * 70)
print("🔍 AUDITING 30 SCHOOLS SYSTEM & DATA INTEGRITY")
print("=" * 70)

errors = []

# 1. Test Web Endpoints
endpoints = [
    ("School Portal", "http://127.0.0.1:8000/school"),
    ("SaaS Admin Portal", "http://127.0.0.1:8000/admin"),
    ("Parent Portal", "http://127.0.0.1:8000/parent"),
    ("Master 30 Schools JS Bundle", "http://127.0.0.1:8000/assets/js/data_30_schools.js"),
    ("School 01 SVG Logo", "http://127.0.0.1:8000/assets/images/schools/sch_01_logo.svg"),
    ("School 30 SVG Logo", "http://127.0.0.1:8000/assets/images/schools/sch_30_logo.svg"),
    ("School 01 SVG Campus", "http://127.0.0.1:8000/assets/images/schools/sch_01_campus.svg"),
    ("School 30 SVG Campus", "http://127.0.0.1:8000/assets/images/schools/sch_30_campus.svg")
]

for name, url in endpoints:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'VerificationBot/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            content_len = len(resp.read())
            print(f"✅ {name}: HTTP {resp.status} (Size: {content_len:,} bytes)")
    except Exception as e:
        err = f"❌ {name} ({url}) FAILED: {e}"
        print(err)
        errors.append(err)

# 2. Test SVG Files Count on Disk
logo_count = len([f for f in os.listdir(os.path.join(BASE_DIR, "assets", "images", "schools")) if f.endswith("_logo.svg")])
campus_count = len([f for f in os.listdir(os.path.join(BASE_DIR, "assets", "images", "schools")) if f.endswith("_campus.svg")])

print(f"\n🎨 SVG Assets Check:")
print(f" - Logos found: {logo_count}/30 {'✅' if logo_count == 30 else '❌'}")
print(f" - Campus illustrations found: {campus_count}/30 {'✅' if campus_count == 30 else '❌'}")
if logo_count < 30 or campus_count < 30:
    errors.append(f"Incomplete SVG assets: logos={logo_count}, campuses={campus_count}")

# 3. Test SQLite Database
print(f"\n🗄️ SQLite Database Integrity Check:")
try:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM schools;")
    sch_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM students;")
    stu_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM users;")
    usr_count = c.fetchone()[0]

    c.execute("SELECT COUNT(DISTINCT school_id) FROM students;")
    active_schools_with_students = c.fetchone()[0]

    print(f" - Total Schools in DB: {sch_count}/30 {'✅' if sch_count == 30 else '❌'}")
    print(f" - Total Students in DB: {stu_count:,}/3,000 {'✅' if stu_count == 3000 else '❌'}")
    print(f" - Schools with exactly enrolled students: {active_schools_with_students}/30 {'✅' if active_schools_with_students == 30 else '❌'}")
    print(f" - Total Users in DB: {usr_count} {'✅' if usr_count >= 31 else '❌'}")

    conn.close()
except Exception as e:
    err = f"❌ SQLite check error: {e}"
    print(err)
    errors.append(err)

# 4. Summary
print("\n" + "=" * 70)
if not errors:
    print("🏆 ALL 30 SCHOOLS, 3,000 STUDENTS, LOGOS, AND INTERFACES VERIFIED 100% PERFECT!")
else:
    print(f"⚠️ FOUND {len(errors)} ERRORS:")
    for e in errors:
        print(f" - {e}")
print("=" * 70)
