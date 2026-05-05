from pydantic import BaseModel
from typing import Optional, List

# 用户注册登录
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

# 文章
class ArticleCreate(BaseModel):
    title: str
    content: str

class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    class Config:
        orm_mode = True