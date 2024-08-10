from dataclasses import dataclass

from sqlalchemy import URL


@dataclass
class DatabaseConfig:
    login: str
    password: str
    host: str
    database: str
    port: int = 5432
    dialect: str = 'postgresql'
    driver: str = 'psycopg'

    def form_drivername(self) -> str:
        if all((self.driver, self.dialect)):
            drivername = f'{self.dialect}+{self.driver}'
        else:
            drivername = self.dialect
        return drivername

    def get_database_url(self) -> URL:
        url = URL.create(
            drivername=self.form_drivername(),
            username=self.host,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )
        return url


@dataclass
class RedisConfig:
    host: str
    port: int = 6379
    password = ''
    database: int = 1
