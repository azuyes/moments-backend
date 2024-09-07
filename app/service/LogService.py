import logging
from app.core.config import settings


class LogService:
    def __init__(self,name:str):
        logging.basicConfig(filename=settings.LOGGING_DIR+'/moment.log',level=logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s] : %(name)s : %(message)s')
        handler.setFormatter(formatter)
        logger=logging.getLogger(name)
        logger.addHandler(handler)
        self.logger =logger
    def getLogger(self) -> logging.Logger:
        return self.logger
