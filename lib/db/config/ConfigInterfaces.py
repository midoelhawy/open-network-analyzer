from typing import Optional


class MySQLParams:
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        dbname: Optional[str] = "open-network-analyzer",
        port: Optional[int] = 3306,
        charset: str = 'utf8mb4'
    ) -> None:
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.dbname: str = dbname
        self.port: int = port
        self.charset: str = charset



class ClickhouseParams:
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        dbname: Optional[str] = "open-network-analyzer",
        port: Optional[int] = 8123
    ) -> None:
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.dbname: str = dbname
        self.port: int = port