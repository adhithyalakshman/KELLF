# dependecies
from pydantic import BaseModel, EmailStr


class Register(BaseModel):
    username: str
    email: EmailStr
    password: str

class login(BaseModel):
    email: EmailStr
    password: str





