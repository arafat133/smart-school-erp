from sqlalchemy.orm import selectinload
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import uuid
from datetime import datetime

from app.core.database import get_db
from app.models.school import School
from app.models.user import User
from app.schemas.school import SchoolCreate, SchoolResponse
from app.api import deps

router = APIRouter()

# RBAC: Only Super Admin can manage school establishments
allow_super_admin = deps.RoleChecker(["super_admin"])

@router.post("/", response_model=SchoolResponse, status_code=status.HTTP_201_CREATED)
async def create_school(
    school_in: SchoolCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(allow_super_admin)
):
    """
    إنشاء مدرسة جديدة في المنظومة السحابية (حصرياً للمشرف العام Super Admin).
    تم إلغاء ابتلاع الأخطاء الصامت وإضافة التحقق الصارم من التكرار والصلاحيات.
    """
    # Check duplicate school name
    existing = await db.execute(select(School).where(School.name == school_in.name))
    if existing.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"المدرسة بالاسم '{school_in.name}' مسجلة مسبقاً في النظام."
        )

    try:
        new_school = School(**school_in.dict())
        db.add(new_school)
        await db.commit()
        await db.refresh(new_school)
        return new_school
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"فشل إنشاء المدرسة في قاعدة البيانات: {str(e)}"
        )

@router.get("/", response_model=List[SchoolResponse])
async def read_schools(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    """
    استرجاع قائمة المدارس المصرح للمستخدم بالاطلاع عليها.
    إذا كان المستخدم مديراً لمدرسة معينة يتم إرجاع مدرسته فقط (Tenant Isolation).
    """
    query = select(School)
    if current_user.role != "super_admin":
        if not current_user.school_id:
            return []
        query = query.where(School.id == current_user.school_id)
        
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
