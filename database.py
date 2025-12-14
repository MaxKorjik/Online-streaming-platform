from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:97948679@localhost:5432/mydb"

engine = create_async_engine(
    DATABASE_URL
)

SessionLocal = async_sessionmaker(
    bind = engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        yield db
        
async def init_db():
    import models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)