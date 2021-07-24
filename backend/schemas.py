from typing import List, Optional
from pydantic import BaseModel


# class UserId(BaseModel):
#     id: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    id: int
    # email: str
    # blogs: List[Blog]

    class Config():
        orm_mode = True


class BlogBase(BaseModel):
    #id: int
    title: str
    body: str
    #user_id: int
    #creator: ShowUser


class Blog(BlogBase):
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
