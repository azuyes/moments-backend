from sqlalchemy import MetaData
from sqlmodel import Field
from app.models.BaseModels.SMSCodeRecordBase import SMSCodeRecordBase
from app.models.BaseModels.User import UserBase
from sqlmodel import SQLModel


# 用户表
class Moment_User(UserBase, table=True):
    __tablename__ = "MOMENT_USER"
    metadata = MetaData(schema="public")
    id: str = Field(primary_key=True)

class User(UserBase, table=True):
    id: int = Field(primary_key=True)


# 短信发送记录
class SMSCodeRecord(SMSCodeRecordBase, table=True):
    id: int = Field(primary_key=True)
