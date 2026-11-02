from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List, Dict, Any, Optional
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel

from app.core.database import get_db
from app.models.academic import Grade, AcademicHistory, SubjectCatalog, AttendanceRecord
from app.models.student import Student
from app.models.finance import FinancialRecord, Account, JournalEntry, JournalEntryLine, JournalEntryStatus
from app.models.user import User
from app.models.audit import SecurityAuditLog
from app.api import deps
from app.services.blockchain import blockchain

router = APIRouter()

# Schema for Journal Entry Creation
class JournalLineIn(BaseModel):
    account_id: UUID
    debit: float = 0.0
    credit: float = 0.0
    memo: Optional[str] = None

class JournalEntryIn(BaseModel):
    entry_number: str
    description: str
    lines: List[JournalLineIn]

@router.get("/report/{academic_history_id}", response_model=Dict[str, Any])
async def get_masked_academic_report(
    academic_history_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    Granular Masking Policy:
    Check financial status before showing grades.
    """
    hist_result = await db.execute(select(AcademicHistory).where(AcademicHistory.id == academic_history_id))
    hist_record = hist_result.scalars().first()
    if not hist_record:
        raise HTTPException(status_code=404, detail="السجل الأكاديمي غير موجود")

    # IDOR Protection: Students/Parents can only query their own child's report
    privileged_roles = ["super_admin", "school_admin", "finance", "teacher"]
    if current_user.role not in privileged_roles:
        parent_students_res = await db.execute(select(Student).where(Student.parent_id == current_user.id))
        parent_student_ids = [s.id for s in parent_students_res.scalars().all()]
        if hist_record.student_id not in parent_student_ids and str(current_user.id) != str(hist_record.student_id):
            raise HTTPException(status_code=403, detail="تحذير أمني IDOR: غير مصرح لك بالاطلاع على التقرير المالي لطالب آخر")

    fin_query = select(FinancialRecord).where(FinancialRecord.academic_history_id == academic_history_id)
    if current_user.role != "super_admin" and current_user.school_id:
        fin_query = fin_query.where(FinancialRecord.school_id == current_user.school_id)
        
    fin_result = await db.execute(fin_query)
    fin_record = fin_result.scalars().first()

    if not fin_record:
        raise HTTPException(status_code=404, detail="لم يتم العثور على سجل مالي لهذا العام الدراسي")

    # Fetch Grades with subject names
    grades_query = (
        select(Grade)
        .options(selectinload(Grade.subject))
        .where(Grade.academic_history_id == academic_history_id)
    )
    if current_user.role != "super_admin" and current_user.school_id:
        grades_query = grades_query.where(Grade.school_id == current_user.school_id)
        
    grades_result = await db.execute(grades_query)
    grades = grades_result.scalars().all()

    report = {
        "status": "success",
        "financial_status": fin_record.payment_status,
        "total_required": float(fin_record.total_required),
        "amount_paid": float(fin_record.amount_paid),
        "message": "",
        "grades": []
    }

    if fin_record.payment_status.lower() != "paid":
        report["message"] = "تنبيه: الطالب متعثر مالياً. تم حجب الدرجات حتى يتم سداد القسط المتبقي."
        for g in grades:
            report["grades"].append({
                "subject_name": g.subject.name if g.subject else str(g.subject_id),
                "subject_id": str(g.subject_id),
                "score": "***"  # MASKED
            })
    else:
        report["message"] = "الرصيد مسدد بالكامل."
        for g in grades:
            report["grades"].append({
                "subject_name": g.subject.name if g.subject else str(g.subject_id),
                "subject_id": str(g.subject_id),
                "score": float(g.score),
                "blockchain_hash": g.blockchain_hash
            })

    return report


@router.get("/dashboard/students", response_model=List[Dict[str, Any]])
async def get_dashboard_students(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    لوحة التحكم المالية:
    تم حل معضلة N+1 Queries جذرياً عبر تفعيل Eager Loading (selectinload)
    للربط بين الطلاب وسجلاتهم الأكاديمية والمالية بدفعة استعلام واحدة بدلاً من 1,000+ استعلام.
    """
    query = (
        select(Student)
        .options(
            selectinload(Student.academic_history).selectinload(AcademicHistory.financial_record)
        )
    )
    if current_user.role != "super_admin" and current_user.school_id:
        query = query.where(Student.school_id == current_user.school_id)

    students_result = await db.execute(query)
    students = students_result.scalars().all()

    result = []
    for student in students:
        # Resolve latest academic history from in-memory preloaded relation (Zero Extra DB Queries)
        latest_acad = None
        if student.academic_history:
            latest_acad = sorted(
                student.academic_history,
                key=lambda h: str(h.academic_year or ""),
                reverse=True
            )[0]

        financial_status = "غير متوفر"
        academic_history_id = None
        if latest_acad:
            academic_history_id = str(latest_acad.id)
            fin = latest_acad.financial_record
            if fin:
                financial_status = "مسدد" if fin.payment_status.lower() == "paid" else "متعثر"

        result.append({
            "id": str(student.id),
            "full_name": student.full_name,
            "student_number": student.student_number,
            "grade_level": student.current_grade_level,
            "financial_status": financial_status,
            "academic_history_id": academic_history_id,
        })

    return result


@router.post("/journal-entries", status_code=status.HTTP_201_CREATED)
async def create_atomic_journal_entry(
    entry_in: JournalEntryIn,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.RoleChecker(["super_admin", "school_admin", "finance"]))
):
    """
    إنشاء قيد محاسبي مزدوج (Double-Entry Bookkeeping)
    التحقق الصارم من التوازن المحاسبي: مجموع المدين = مجموع الدائن بفارق صفري تماماً.
    """
    target_school_id = current_user.school_id
    if not target_school_id and current_user.role != "super_admin":
        raise HTTPException(status_code=400, detail="يجب تحديد مدرسة المستخدم")

    total_debit = Decimal("0.0000")
    total_credit = Decimal("0.0000")

    lines_models = []
    for line in entry_in.lines:
        d = Decimal(str(line.debit))
        c = Decimal(str(line.credit))
        total_debit += d
        total_credit += c
        lines_models.append(
            JournalEntryLine(
                school_id=target_school_id,
                account_id=line.account_id,
                debit=d,
                credit=c,
                memo=line.memo
            )
        )

    # Invariant: Total Debit == Total Credit
    delta = abs(total_debit - total_credit)
    if delta >= Decimal("0.0001") or total_debit <= Decimal("0.0000"):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"❌ رفض القيد المحاسبي: القيد غير متوازن! مجموع المدين ({total_debit}) لا يساوي مجموع الدائن ({total_credit}). الفارق: {delta}"
        )

    new_entry = JournalEntry(
        school_id=target_school_id,
        entry_number=entry_in.entry_number,
        description=entry_in.description,
        status=JournalEntryStatus.POSTED,
        total_debit=total_debit,
        total_credit=total_credit,
        posted_by_id=current_user.id,
        lines=lines_models
    )
    db.add(new_entry)

    # Audit Logging
    client_ip = request.client.host if request.client else "127.0.0.1"
    audit_entry = SecurityAuditLog(
        school_id=target_school_id,
        user_id=current_user.id,
        username=current_user.username,
        role=current_user.role,
        action="JOURNAL_ENTRY_POSTED",
        resource_type="JournalEntry",
        resource_id=entry_in.entry_number,
        ip_address=client_ip,
        user_agent=request.headers.get("user-agent", "Unknown"),
        status="SUCCESS",
        details=f"تم ترحيل قيد محاسبي متوازن: {entry_in.entry_number} بمبلغ إجمالي: {total_debit}"
    )
    db.add(audit_entry)

    await db.commit()
    await db.refresh(new_entry)
    return {
        "status": "success",
        "message": "تم ترحيل القيد المحاسبي بنجاح مع تطبيق شرط التوازن الذري",
        "entry_id": str(new_entry.id),
        "total_amount": float(total_debit)
    }
