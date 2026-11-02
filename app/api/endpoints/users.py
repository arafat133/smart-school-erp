from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash
from app.api import deps

router = APIRouter()

allow_create_user = deps.RoleChecker(["super_admin", "school_admin"])

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    from app.services.honeytoken_service import honeytoken_service
    client_ip = request.client.host if request.client else "127.0.0.1"
    if honeytoken_service.is_canary_hit(user_id):
        honeytoken_service.trigger_canary_alert(
            identifier=user_id,
            client_ip=client_ip,
            endpoint=f"GET /api/users/{user_id}",
            user_agent=request.headers.get("user-agent", "Unknown")
        )
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")
        
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")
    return user

@router.post("/", response_model=UserResponse)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(allow_create_user)
):
    # Privilege Escalation Protection: Only super_admin can create super_admin accounts
    if getattr(user_in.role, 'value', str(user_in.role)) == "super_admin" and current_user.role != "super_admin":
        raise HTTPException(status_code=403, detail="فقط المشرف العام يمكنه إنشاء حسابات إدارة عليا")
    # Check if username exists
    result = await db.execute(select(User).where(User.username == user_in.username))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Username already registered")
        
    user_data = user_in.dict(exclude={"password"})
    hashed_password = get_password_hash(user_in.password)
    
    new_user = User(**user_data, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
