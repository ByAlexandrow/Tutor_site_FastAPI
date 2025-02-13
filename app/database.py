from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = 'sqlite+aiosqlite:///./tutor.db'

engine = create_async_engine(DATABASE_URL, echo=True)

Sessionlocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with Sessionlocal() as session:
        try:
            yield session
        finally:
            await session.close()
