'''
/store/db/postgres.py
'''
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from store.core.config import settings

class PostgresClient:
    def __init__(self):
        self.engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)
        self.Base = declarative_base()

    def get_session(self) -> AsyncSession:
        return self.SessionLocal()

    def get_base(self):
        return self.Base

db_client = PostgresClient()
