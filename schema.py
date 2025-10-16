from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    name: str
    email: EmailStr
    stack: str

class UserProfileResponse(BaseModel):
    status: str
    user: UserInfo
    timestamp: str
    fact: str