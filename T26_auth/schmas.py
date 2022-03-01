from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


class UserPayload(User):
    exp: datetime
