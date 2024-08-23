from pydantic import BaseModel
from sqlmodel import SQLModel


class PhoneNumberIn(SQLModel):
    phone_number: str

class getUserIn(BaseModel):
    username: str

class getLoginIn(BaseModel):
    username: str
    hashed_password:str
