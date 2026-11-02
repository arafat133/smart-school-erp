"""
سكربت إعادة حقن البيانات الأولية
يحذف البيانات القديمة ثم يعيد إدخالها بالكامل
"""
import asyncio
import uuid
from datetime import date
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import text

from app.core.config import settings
from app.core.security import get_password_hash
from app.services.blockchain import blockchain

from app.models.school import School
from app.models.user import User
from app.models.student import Student
from app.models.academic import AcademicHistory, SubjectCatalog, Grade, AttendanceRecord
from app.models.finance import FinancialRecord

engine = create_async_engine(settings.DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def seed():
    async with AsyncSessionLocal() as db:
        # Clean all tables
        for tbl in ['grades', 'financial_records', 'attendance_records', 'academic_history',
                     'daily_assignments', 'subjects_catalog', 'students', 'users', 'schools']:
            await db.execute(text(f'DELETE FROM {tbl}'))
        await db.commit()
        print("Cleaned all tables.")

        # 1. School
        school_id = uuid.uuid4()
        school = School(
            id=school_id, name="mdrsa almtwfqyn alahlya",
            governorate_district="amant al3asma", center_type="bnyn",
            directorate_location="mdyryt m3yn", school_location="shr3 t3z - sn3a2",
            manager_name="a. mhmd ahmd al3lwy", manager_phone="777123456",
            it_manager="m. khald s3yd", is_active=True,
        )
        db.add(school)
        await db.commit()
        print("School created.")

        # 2. Admin
        admin_id = uuid.uuid4()
        db.add(User(id=admin_id, school_id=school_id, username="admin",
                     hashed_password=get_password_hash("password123"),
                     role="super_admin", phone="777000000", is_active=True))
        print("Admin created: admin / password123")

        # 3. Teacher
        teacher_id = uuid.uuid4()
        db.add(User(id=teacher_id, school_id=school_id, username="teacher1",
                     hashed_password=get_password_hash("teacher123"),
                     role="teacher", phone="777111111", is_active=True))
        print("Teacher created: teacher1 / teacher123")

        # 4. Parent
        parent_id = uuid.uuid4()
        db.add(User(id=parent_id, school_id=school_id, username="parent1",
                     hashed_password=get_password_hash("parent123"),
                     role="parent", phone="777222222", is_active=True))
        print("Parent created: parent1 / parent123")
        await db.commit()

        # 5. Subjects
        subjects_data = [
            ("alryadyat", "alsf altas3"),
            ("alfyzya2", "alsf altas3"),
            ("allgha al3rbya", "alsf altas3"),
            ("allgha alenjlyzyya", "alsf altas3"),
            ("al3lwm", "alsf altas3"),
        ]
        subjects = []
        for name, level in subjects_data:
            s = SubjectCatalog(id=uuid.uuid4(), school_id=school_id, name=name, grade_level=level)
            db.add(s)
            subjects.append(s)
        print("5 subjects created.")

        # 6. Students
        student1_id = uuid.uuid4()
        db.add(Student(id=student1_id, school_id=school_id, full_name="ahmed ali mohammed",
                        student_number="STU-001", parent_id=parent_id,
                        date_of_birth=date(2010, 3, 15), place_of_birth="sanaa",
                        residence="sanaa", current_grade_level="alsf altas3",
                        father_national_id="01234567890", gender="male", nationality="yemeni"))

        student2_id = uuid.uuid4()
        db.add(Student(id=student2_id, school_id=school_id, full_name="sara khaled alomari",
                        student_number="STU-002",
                        date_of_birth=date(2010, 7, 22), place_of_birth="aden",
                        residence="sanaa", current_grade_level="alsf altas3",
                        father_national_id="09876543210", gender="female", nationality="yemeni"))

        student3_id = uuid.uuid4()
        db.add(Student(id=student3_id, school_id=school_id, full_name="yousef abdullah naser",
                        student_number="STU-003",
                        date_of_birth=date(2011, 1, 10), place_of_birth="taiz",
                        residence="sanaa", current_grade_level="alsf altas3",
                        father_national_id="05678901234", gender="male", nationality="yemeni"))
        print("3 students created.")
        await db.commit()

        # 7. Academic History
        acad1_id = uuid.uuid4()
        db.add(AcademicHistory(id=acad1_id, school_id=school_id, student_id=student1_id,
                                grade_level="alsf altas3", academic_year="2025-2026", status="pass"))
        acad2_id = uuid.uuid4()
        db.add(AcademicHistory(id=acad2_id, school_id=school_id, student_id=student2_id,
                                grade_level="alsf altas3", academic_year="2025-2026", status="pass"))
        acad3_id = uuid.uuid4()
        db.add(AcademicHistory(id=acad3_id, school_id=school_id, student_id=student3_id,
                                grade_level="alsf altas3", academic_year="2025-2026", status="pass"))
        print("Academic history created.")
        await db.commit()

        # 8. Grades with blockchain
        scores_student1 = [92, 88, 95, 78, 85]
        scores_student2 = [75, 82, 90, 70, 88]
        scores_student3 = [60, 55, 72, 65, 68]

        for student_scores, acad_id in [
            (scores_student1, acad1_id),
            (scores_student2, acad2_id),
            (scores_student3, acad3_id),
        ]:
            previous_hash = "0"
            for i, score in enumerate(student_scores):
                data_to_hash = {"student_id": str(acad_id), "subject_id": str(subjects[i].id), "score": score}
                current_hash = blockchain.generate_hash(data_to_hash, previous_hash)
                db.add(Grade(id=uuid.uuid4(), school_id=school_id, academic_history_id=acad_id,
                             subject_id=subjects[i].id, score=score, blockchain_hash=current_hash))
                previous_hash = current_hash
        print("15 grades with blockchain hashes created.")

        # 9. Financial Records
        db.add(FinancialRecord(id=uuid.uuid4(), school_id=school_id, academic_history_id=acad1_id,
                                grade_level="alsf altas3", academic_year="2025-2026",
                                total_required=500000, amount_paid=500000, payment_status="paid"))
        db.add(FinancialRecord(id=uuid.uuid4(), school_id=school_id, academic_history_id=acad2_id,
                                grade_level="alsf altas3", academic_year="2025-2026",
                                total_required=500000, amount_paid=150000, payment_status="unpaid"))
        db.add(FinancialRecord(id=uuid.uuid4(), school_id=school_id, academic_history_id=acad3_id,
                                grade_level="alsf altas3", academic_year="2025-2026",
                                total_required=500000, amount_paid=500000, payment_status="paid"))
        print("Financial records created (1 unpaid, 2 paid).")

        # 10. Attendance
        attendance_data = [
            (student1_id, date(2026, 7, 6), "present"), (student1_id, date(2026, 7, 7), "present"),
            (student1_id, date(2026, 7, 8), "absent"), (student1_id, date(2026, 7, 9), "present"),
            (student2_id, date(2026, 7, 6), "present"), (student2_id, date(2026, 7, 7), "late"),
            (student2_id, date(2026, 7, 8), "present"), (student2_id, date(2026, 7, 9), "present"),
            (student3_id, date(2026, 7, 6), "absent"), (student3_id, date(2026, 7, 7), "present"),
            (student3_id, date(2026, 7, 8), "present"), (student3_id, date(2026, 7, 9), "excused"),
        ]
        for sid, d, s in attendance_data:
            db.add(AttendanceRecord(id=uuid.uuid4(), school_id=school_id, student_id=sid,
                                     grade_level="alsf altas3", academic_year="2025-2026", date=d, status=s))
        print("12 attendance records created.")

        await db.commit()
        print("\nDONE! All data seeded successfully.")
        print("Login: admin / password123")
        print("Login: teacher1 / teacher123")
        print("Login: parent1 / parent123")


if __name__ == "__main__":
    asyncio.run(seed())
