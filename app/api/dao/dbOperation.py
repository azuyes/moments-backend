from app.core.db import engine
from sqlmodel import Session,select

from app.models.BaseModels.Bizexception import Bizexception
from app.models.table import Moment_User

from app.service.LogService import LogService

logger=LogService(name=__name__).getLogger()

'''
User相关
'''
def getUserFromDB(username:str):
    try:
        with Session(engine) as session:
            # Try to create session to check if DB is awake
            statement = select(Moment_User).where(Moment_User.username == username)
            result=session.exec(statement)
            user=result.one_or_none()
            logger.info("user查询成功："+str(user))
            return user
    except Exception as e:
        logger.error("user查询失败："+str(e))
        raise e

def addUser(id:str,username:str,phone_number:str,is_active:bool,is_superuser:bool,hashed_password:str):
    try:
        with Session(engine) as session:
            # Try to create session to check if DB is awake
            any_user=session.query(Moment_User).filter_by(username=username).first()
            if any_user:
                logger.info('username: '+username+' already exist')
                raise Bizexception(error_code=999,message='username: '+username+' already exist')
            user=Moment_User(id=id,username=username,phone_number=phone_number,is_active=is_active,is_superuser=is_superuser,hashed_password=hashed_password)
            session.add(user)
            session.commit()
            logger.info("user添加成功："+str(username))
            return True
    except Exception as e:
        logger.error("user添加失败："+str(e))
        raise e
