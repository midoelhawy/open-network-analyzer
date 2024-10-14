from typing import Literal, overload, Union
from venv import logger

from lib.db import NFlowInstance
from lib.db.client.ClickHouseClient import ClickHouseClient
from lib.db.client.MySQLClient import MySQLClient
from lib.db.config.ConfigInterfaces import MySQLParams, ClickhouseParams


class DatabaseManager:

    @overload
    def __init__(self, db_type: Literal["mysql"], db_params: MySQLParams) -> None:
        ...

    @overload
    def __init__(self, db_type: Literal["clickhouse"], db_params: ClickhouseParams) -> None:
        ...

    def __init__(self, db_type: Literal["mysql", "clickhouse"],
                 db_params: Union[MySQLParams, ClickhouseParams]) -> None:

        if db_type == 'mysql':
            logger.warn(f"Using MySQL database; username:{db_params.user}; password:{db_params.password}; host:{db_params.host}; port:{db_params.port}" )
            self.client = MySQLClient(db_params)
        elif db_type == 'clickhouse':
            self.client = ClickHouseClient(db_params=db_params)
        else:
            raise ValueError("Unsupported database type")

    def add_flow(self, nflow_instance: 'NFlowInstance') -> None:
        self.client.add_flow(nflow_instance)