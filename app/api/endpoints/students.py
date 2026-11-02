from sqlalchemy.orm import selectinload
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID

from app.core.database import get_db
from app.models.student import Student
from app.models.user import User
from app.models.audit import SecurityAuditLog
from app.schemas.student import StudentCreate, StudentResponse
from app.api import deps

router = APIRouter()

allow_create = deps.RoleChecker(["super_admin", "school_admin"])

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(
    student_in: StudentCreate,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(allow_create)
):
    """
    تسجيل طالب جديد مع فرض العزل التام للمستأجر (Tenant Boundary Enforcement).
    يمنع منعاً باتاً لمدير المدرسة حقن بيانات تخص مدارس أخرى.
    """
    student_data = student_in.dict()
    
    # Hard Isolation: School admins can ONLY create students inside their own school
    if current_user.role != "super_admin":
        if not current_user.school_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="الحساب غير مرتبط بمدرسة محددة"
            )
        student_data["school_id"] = current_user.school_id
    elif "school_id" not in student_data or not student_data["school_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="يجب تحديد معرف المدرسة (school_id) للطالب"
        )

    # Check student_number collision within the school
    existing = await db.execute(
        select(Student)
        .where(Student.student_number == student_data["student_number"])
        .where(Student.school_id == student_data["school_id"])
    )
    if existing.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"رقم القيد '{student_data['student_number']}' مستخدم بالفعل في هذه المدرسة."
        )

    new_student = Student(**student_data)
    db.add(new_student)

    # Security Audit Logging
    client_ip = request.client.host if request.client else "127.0.0.1"
    audit_entry = SecurityAuditLog(
        school_id=new_student.school_id,
        user_id=current_user.id,
        username=current_user.username,
        role=current_user.role,
        action="STUDENT_ENROLLED",
        resource_type="Student",
        resource_id=str(new_student.id),
        ip_address=client_ip,
        user_agent=request.headers.get("user-agent", "Unknown"),
        status="SUCCESS",
        details=f"تم تسجيل الطالب: {new_student.full_name} برقم قيد: {new_student.student_number}"
    )
    db.add(audit_entry)

    await db.commit()
    await db.refresh(new_student)
    return new_student

@router.get("/", response_model=List[StudentResponse])
async def read_students(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    استرجاع قائمة الطلاب مع تطبيق سياسة حظر التسلل الأفقي بين المدارس (Row-Level Security).
    """
    query = select(Student)
    if current_user.role != "super_admin":
        if not current_user.school_id:
            return []
        query = query.where(Student.school_id == current_user.school_id)
        
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
