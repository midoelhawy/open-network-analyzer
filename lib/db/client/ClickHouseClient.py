from lib.db.client.DatabaseClient import DatabaseClient
from lib.db.config.ConfigInterfaces import ClickhouseParams


class ClickHouseClient(DatabaseClient):
    def __init__(self, db_params: ClickhouseParams) -> None:
        db_url = f'clickhouse://{db_params.user}:{db_params.password}@{db_params.host}:{db_params.port}/{db_params.dbname}'
        super().__init__(db_url)

