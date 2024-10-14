from venv import logger

from lib.db.client.DatabaseClient import DatabaseClient
from lib.db.config.ConfigInterfaces import MySQLParams


class MySQLClient(DatabaseClient):
    def __init__(self, db_params:MySQLParams) -> None:
        db_url = f'mysql+pymysql://{db_params.user}:{db_params.password}@{db_params.host}/{db_params.dbname}'
        logger.warn(db_url)
        super().__init__(db_url)