import multiprocessing
from sqlmodel import Session, create_engine, select
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.BaseModels.User import UserCreate
from app.models.table import User, Moment_User

# from app import crud
# from app.core.config import settings
# from app.models.User import UserCreate
# from app.models.table import User


cpu_count = multiprocessing.cpu_count() * 2
workers = cpu_count
max_db_conn = 500

pool_size = max_db_conn // (workers * 2)
max_overflow = pool_size

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_size=pool_size,
    max_overflow=max_overflow,
    pool_timeout=30,
    # 如果需要 SSL 连接，取消下面的注释并提供正确的参数
    # connect_args={
    #     "sslmode": "verify-full",
    #     "sslcert": "/path/to/client-cert.pem",
    #     "sslkey": "/path/to/client-key.pem",
    #     "sslrootcert": "/path/to/server-ca.pem",
    # }
)


# 标记
# 确保在初始化数据库之前导入了所有 SQLModel 模型 (app.models)
# 否则, SQLModel 可能无法正确初始化关系
# 更多详细信息: https://github.com/tiangolo/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    #
    print("✅初始化数据库，尝试检查或添加超级用户")
    # # 创建超级用户
    # # 查找第一个超级用户
    user = session.exec(
        select(Moment_User)
        .where(Moment_User.username == settings.FIRST_SUPERUSER)
    ).first()

    # 如果找不到超级用户, 则创建一个新的超级用户
    if not user:
        user = create_user(session=session)


def create_user(session: Session) -> Moment_User:
    """
    创建新用户并设置其邀请码。
    """
    # 验证数据并哈希密码
    # new_user = User.model_validate(
    #     user_create,
    #     update={"hashed_password": get_password_hash(user_create.password)}
    # )
    new_user=Moment_User(id='azu',username='azu',phone_number='13488856212',is_active=True,is_superuser=True,hashed_password='123456')

    # 将验证后的用户对象添加到数据库会话中
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
