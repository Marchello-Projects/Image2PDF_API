import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

class DataBaseConfig:
    def __init__(self):
        self.__database_name = os.getenv("DATABASE_NAME")
        self.__db_user = os.getenv("DB_USER")
        self.__db_password = os.getenv("DB_PASSWORD")
        self.__db_host = os.getenv("DB_HOST")
        self.__db_port = os.getenv("DB_PORT")

    @property
    def database_name(self):
        return self.__database_name

    @property
    def db_user(self):
        return self.__db_user

    @property
    def db_password(self):
        return self.__db_password

    @property
    def db_host(self):
        return self.__db_host

    @property
    def db_port(self):
        return self.__db_port

    def uri_postgres(self):
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.database_name}"
        )

db_config = DataBaseConfig()

async_engine: AsyncEngine = create_async_engine(
    db_config.uri_postgres(),
    echo=True
)

async_session = async_sessionmaker(bind=async_engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session