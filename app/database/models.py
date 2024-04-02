from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from config import SQL_ALCHEMY_DATABASE_URI

# Creating tables needed for registration in the bot

# Create an asynchronous engine using the specified database URI(config.py)
engine = create_async_engine(SQL_ALCHEMY_DATABASE_URI, echo=True)

# Create an asynchronous session factory
async_session = async_sessionmaker(engine)


# Base class for declarative models with asynchronous support
class Base(AsyncAttrs, DeclarativeBase):
    pass


# Model for Registered Users
class RegisteredUsers(Base):
    __tablename__ = "Registered users"
    id: Mapped[int] = mapped_column(primary_key=True)
    language: Mapped[str] = mapped_column(String(20))
    time_zone: Mapped[str] = mapped_column(String(2))

    def __repr__(self):
        return str(self)

async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)