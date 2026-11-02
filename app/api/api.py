from fastapi import APIRouter
from app.api.endpoints import auth, students, attendance, grades, finance, schools, users, two_factor, encryption, blockchain, security_actions

api_router = APIRouter()
api_router.include_router(schools.router, prefix="/schools", tags=["Schools"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(students.router, prefix="/students", tags=["Students"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
api_router.include_router(grades.router, prefix="/grades", tags=["Grades & Blockchain"])
api_router.include_router(finance.router, prefix="/finance", tags=["Finance"])

api_router.include_router(two_factor.router, prefix="/auth/2fa", tags=["two-factor-auth"])
api_router.include_router(encryption.router, prefix="/security/encryption", tags=["data-encryption"])
api_router.include_router(blockchain.router, prefix="/blockchain", tags=["academic-blockchain"])
api_router.include_router(security_actions.router, prefix="/security/actions", tags=["security-actions"])
api_router.include_router(security_actions.router, prefix="/security", tags=["security-ai"])
