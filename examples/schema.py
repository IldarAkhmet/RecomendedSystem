from pydantic import BaseModel
from datetime import datetime


### Создание классов для валидации типов( из бд в вид класса )

class UserGet(BaseModel):
    id: int
    age: int
    city: str
    country: str
    exp_group: int
    gender: int
    os: str
    source: str

    class Config:
        orm_mode = True


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    action: str
    post_id: int
    time: datetime
    user_id: int
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True