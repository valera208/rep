from config import settings
from sqlalchemy import Integer, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Annotated
DB_URL = settings.get_db_by_url()

async_engine = create_async_engine(url=DB_URL)

async_session_maker = async_sessionmaker(bind=async_engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.nowy())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now())

unique_info = Annotated[str, mapped_column(unique=True)]

def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                return await method(*args, **kwargs, session = session)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()
    return wrapper