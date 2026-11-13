from pydantic import BaseModel, ConfigDict
from typing import Optional

class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"

class ApplicationUpdate(BaseModel):
    company: str
    role: str
    status: str

class ApplicationPatch(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None

class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    app_id: int
    company: str
    role: str
    status: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
