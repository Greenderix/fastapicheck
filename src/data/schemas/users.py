from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    is_superuser: bool
    level: int
    level_progress: int

    class Config:
        orm_mode = True
