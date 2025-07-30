from pydantic import BaseModel, EmailStr, Field

class NotificationRequest(BaseModel):
    email: EmailStr = Field(...)
    message: str = Field(...)
