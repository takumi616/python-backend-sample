from app.core.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

async_engine = create_async_engine(settings.database_url, echo=False)

async_Session = sessionmaker(
    bind=async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_db():
    async with async_Session() as session:
        yield session        

