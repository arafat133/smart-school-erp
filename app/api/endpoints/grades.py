from sqlalchemy.orm import selectinload
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

from app.core.database import get_db
from app.models.academic import Grade, AcademicHistory, SubjectCatalog
from app.models.user import User
from app.models.audit import SecurityAuditLog
from app.schemas.academic import GradeCreate, GradeResponse
from app.api import deps
from app.services.blockchain import blockchain

router = APIRouter()

allow_grade_submission = deps.RoleChecker(["super_admin", "school_admin", "teacher"])

# Global Control Lock State (Can also be queried from a SystemSettings table)
CONTROL_PERIOD_LOCKED = False

@router.post("/", response_model=GradeResponse, status_code=status.HTTP_201_CREATED)
async def submit_grade(
    grade_in: GradeCreate,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(allow_grade_submission)
):
    """
    رصد الدرجات مع تفعيل حوكمة الكنترول الصارمة والتحقق من الأسقف وتسجيل البصمة في البلوكشين:
      1. فحص قفل الكنترول (Control Lock Enforcement).
      2. فحص سقف الدرجات (0 <= Score <= Max Score).
      3. منع تكرار رصد نفس المادة لنفس السجل الأكاديمي.
      4. توثيق العملية الحساسة في SecurityAuditLog.
    """
    # 1. Hard Business Constraint: Examination Control Governance & Lock
    if CONTROL_PERIOD_LOCKED and current_user.role != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="⚠️ لجنة الكنترول مغلقة رسمياً. لا يمكن إضافة أو تعديل درجات الطلاب بعد اعتماد النتائج."
        )

    # 2. Hard Business Constraint: Grade Ceilings (أسقف الدرجات)
    if grade_in.score < 0.0 or grade_in.score > 100.0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"الدرجة المدخلة ({grade_in.score}) غير صالحة. يجب أن تكون الدرجة بين 0 و 100."
        )

    # 3. Fetch academic history with tenant boundary verification
    hist_query = select(AcademicHistory).where(AcademicHistory.id == grade_in.academic_history_id)
    if current_user.role != "super_admin" and current_user.school_id:
        hist_query = hist_query.where(AcademicHistory.school_id == current_user.school_id)
        
    hist_result = await db.execute(hist_query)
    history = hist_result.scalars().first()
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="لم يتم العثور على سجل أكاديمي للطالب")

    # 4. Check for duplicate grade entry
    dup_check = await db.execute(
        select(Grade)
        .where(Grade.academic_history_id == grade_in.academic_history_id)
        .where(Grade.subject_id == grade_in.subject_id)
    )
    if dup_check.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="تم رصد درجة لهذه المادة مسبقاً. لتعديل الدرجة يرجى مراجعة إدارة الكنترول وتقديم طلب فتح تعديل رسمي."
        )

    # 5. Fetch previous grade to form the cryptographic blockchain chain
    prev_grade_result = await db.execute(
        select(Grade)
        .where(Grade.academic_history_id == grade_in.academic_history_id)
        .order_by(Grade.created_at.desc())
        .limit(1)
    )
    prev_grade = prev_grade_result.scalars().first()
    previous_hash = prev_grade.blockchain_hash if prev_grade else "0"

    # 6. Calculate immutable blockchain hash
    data_to_hash = {
        "student_id": str(history.student_id),
        "subject_id": str(grade_in.subject_id),
        "score": float(grade_in.score)
    }
    current_hash = blockchain.generate_hash(data_to_hash, previous_hash)

    target_school_id = current_user.school_id or history.school_id
    new_grade = Grade(
        **grade_in.dict(exclude={"school_id"}),
        school_id=target_school_id,
        blockchain_hash=current_hash
    )
    db.add(new_grade)

    # 7. Audit Log recording
    client_ip = request.client.host if request.client else "127.0.0.1"
    audit_entry = SecurityAuditLog(
        school_id=target_school_id,
        user_id=current_user.id,
        username=current_user.username,
        role=current_user.role,
        action="GRADE_COMMITTED",
        resource_type="Grade",
        resource_id=str(new_grade.id),
        ip_address=client_ip,
        user_agent=request.headers.get("user-agent", "Unknown"),
        status="SUCCESS",
        details=f"تم رصد درجة ({grade_in.score}) للمادة ({grade_in.subject_id}) برمز توثيق بلوكشين: {current_hash[:16]}..."
    )
    db.add(audit_entry)

    await db.commit()
    await db.refresh(new_grade)
    return new_grade

@router.get("/verify/{academic_history_id}", response_model=bool)
async def verify_grades_integrity(
    academic_history_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    التحقق من سلامة البلوكشين لكافة درجات الطالب والتأكد من عدم وجود أي تلاعب في قاعدة البيانات.
    تم حل خطأ MissingGreenlet بإضافة selectinload(Grade.academic_record).
    """
    query = (
        select(Grade)
        .options(selectinload(Grade.academic_record))
        .where(Grade.academic_history_id == academic_history_id)
    )
    if current_user.role != "super_admin" and current_user.school_id:
        query = query.where(Grade.school_id == current_user.school_id)
        
    result = await db.execute(query.order_by(Grade.created_at.asc()))
    grades = result.scalars().all()

    previous_hash = "0"
    for grade in grades:
        student_id_val = str(grade.academic_record.student_id) if grade.academic_record else ""
        data_to_hash = {
            "student_id": student_id_val,
            "subject_id": str(grade.subject_id),
            "score": float(grade.score)
        }
        if not blockchain.verify_integrity(data_to_hash, previous_hash, grade.blockchain_hash):
            return False  # Cryptographic tamper detected!
        previous_hash = grade.blockchain_hash

    return True
