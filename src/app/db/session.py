# src/app/db/session.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config

# URL do banco (pode ser SQLite local em dev, PostgreSQL em prod)
DATABASE_URL = config(
    "DATABASE_URL", default="sqlite+aiosqlite:///./dev.db"
)

# engine assíncrono
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

# sessão para dependências
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# base declarativa para modelos
Base = declarative_base()

# dependência para injection no FastAPI
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session