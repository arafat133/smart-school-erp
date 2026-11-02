import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class SecurityAuditLog(BaseModel):
    """
    سجل الرقابة والأمان للعمليات الحساسة في المنظومة (Enterprise Security Audit Log)
    يوثق كل حركة حساسة: هوية المستخدم، عنوان IP، نوع العملية، الحالة، والتفاصيل.
    """
    __tablename__ = "security_audit_logs"

    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id", ondelete="SET NULL"), nullable=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    username = Column(String, nullable=True, index=True)
    role = Column(String, nullable=True)
    
    action = Column(String, nullable=False, index=True) # e.g., LOGIN_SUCCESS, GRADE_MUTATED, TENANT_VIOLATION
    resource_type = Column(String, nullable=True, index=True) # e.g., Grade, User, FinancialRecord
    resource_id = Column(String, nullable=True)
    
    ip_address = Column(String, nullable=False, index=True)
    user_agent = Column(String, nullable=True)
    status = Column(String, nullable=False, default="SUCCESS") # SUCCESS, WARNING, BLOCKED, FAILED
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
