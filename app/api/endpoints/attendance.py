from sqlalchemy.orm import selectinload
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

from app.core.database import get_db
from app.models.academic import AttendanceRecord
from app.models.student import Student
from app.models.user import User
from app.models.audit import SecurityAuditLog
from app.schemas.academic import AttendanceCreate, AttendanceResponse
from app.api import deps

router = APIRouter()

allow_attendance_write = deps.RoleChecker(["super_admin", "school_admin", "teacher", "attendance"])

@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
async def create_attendance(
    attendance_in: AttendanceCreate,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(allow_attendance_write)
):
    """
    تسجيل حضور وغياب مع التحقق من تبعية الطالب لمدرسة المستخدم ومنع حقن المستأجرين.
    """
    record_data = attendance_in.dict()

    # Verify student exists and belongs to the caller's school
    stu_res = await db.execute(select(Student).where(Student.id == attendance_in.student_id))
    student = stu_res.scalars().first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="لم يتم العثور على الطالب المحدد"
        )

    if current_user.role != "super_admin":
        if student.school_id != current_user.school_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="تحذير أمني: غير مصرح لك بتسجيل حضور لطالب في مدرسة أخرى"
            )
        record_data["school_id"] = current_user.school_id
    else:
        record_data["school_id"] = student.school_id

    new_record = AttendanceRecord(**record_data)
    db.add(new_record)
    await db.commit()
    await db.refresh(new_record)
    return new_record

@router.get("/student/{student_id}", response_model=List[AttendanceResponse])
async def get_student_attendance(
    student_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    استرجاع سجل حضور الطالب مع حماية IDOR لأولياء الأمور والطلاب.
    """
    # IDOR Check for parents
    if current_user.role == "parent":
        parent_students = await db.execute(select(Student).where(Student.parent_id == current_user.id))
        allowed_ids = [s.id for s in parent_students.scalars().all()]
        if student_id not in allowed_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="غير مصرح لك بالاطلاع على سجل حضور طالب آخر"
            )

    query = select(AttendanceRecord).where(AttendanceRecord.student_id == student_id)
    if current_user.role != "super_admin" and current_user.school_id:
        query = query.where(AttendanceRecord.school_id == current_user.school_id)
        
    result = await db.execute(query.order_by(AttendanceRecord.date.desc()))
    return result.scalars().all()
