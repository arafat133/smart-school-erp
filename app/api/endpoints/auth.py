import time
FAILED_LOGIN_ATTEMPTS = {}
LOCKED_USERS = {}
LOCKOUT_DURATION_SECS = 1800  # 30 minutes

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.core.security import verify_password, create_access_token
from app.core.config import settings
from app.models.user import User
from app.schemas.token import Token
from app.schemas.user import UserResponse
from app.api import deps

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_access_token(
    db: AsyncSession = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    now = time.time()
    uname = form_data.username.lower().strip()

    # Check 5 failed attempts lockout policy
    if uname in LOCKED_USERS:
        lock_time = LOCKED_USERS[uname]
        if now - lock_time < LOCKOUT_DURATION_SECS:
            rem_mins = int((LOCKOUT_DURATION_SECS - (now - lock_time)) // 60) + 1
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"🚫 تم حظر الحساب أمنياً لتجاوز أكثر من 5 محاولات دخول خاطئة. يرجى الانتظار {rem_mins} دقيقة أو التواصل مع مسؤول النظام."
            )
        else:
            del LOCKED_USERS[uname]
            FAILED_LOGIN_ATTEMPTS.pop(uname, None)

    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalars().first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        attempts = FAILED_LOGIN_ATTEMPTS.get(uname, 0) + 1
        FAILED_LOGIN_ATTEMPTS[uname] = attempts
        if attempts >= 5:
            LOCKED_USERS[uname] = now
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="🚫 تم حظر وقفل هذا الحساب أمنياً لتجاوز الحد الأقصى لمحاولات الدخول الخاطئة (5 محاولات)! يرجى التواصل مع مسؤول النظام."
            )
        rem = 5 - attempts
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"❌ اسم المستخدم أو كلمة المرور غير صحيحة. تبقّت لك ({rem}) محاولات قبل حظر وقفل الحساب."
        )
    
    # Success -> clear failed attempts
    FAILED_LOGIN_ATTEMPTS.pop(uname, None)
    LOCKED_USERS.pop(uname, None)

    if not user.is_active:
        raise HTTPException(status_code=400, detail="الحساب غير مفعل")
        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            subject=user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",  # nosec B105
    }

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: User = Depends(deps.get_current_active_user),
):
    return current_user
