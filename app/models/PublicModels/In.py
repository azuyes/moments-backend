from pydantic import BaseModel
from sqlmodel import SQLModel


class PhoneNumberIn(SQLModel):
    phone_number: str

class getUserIn(BaseModel):
    username: str

class addUserIn(BaseModel):
    username: str
    hashed_password: str
    phone_number:str


class getLoginIn(BaseModel):
    username: str
    hashed_password:str
