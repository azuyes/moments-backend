#


from sqlmodel import Session
from app.core.db import engine, init_db
from app.service.LogService import LogService

logger=LogService(name=__name__).getLogger()


def init() -> None:
    with Session(engine) as session:
        init_db(session)


def main() -> None:
    logger.info("🚀——————开始初始化数据库")
    init()
    logger.info("✅——————数据库初始化完成")


if __name__ == "__main__":
    main()
