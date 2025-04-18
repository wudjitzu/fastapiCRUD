from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime, timezone

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOUT(PostBase):
    post: Post  
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]
