import os
from app.database.models import RegisteredUsers, engine, async_session
from sqlalchemy import insert, select, delete, update


# functions for working with database

async def insert_user(id: str, language: str, time_zone: str) -> None:
    statement = insert(RegisteredUsers).values(id=id, language=language, time_zone=time_zone)
    async with engine.connect() as connection:
        await connection.execute(statement)
        await connection.commit()


async def check_registered_user(user_id: str) -> bool:  # registred -> true
    statement = select(RegisteredUsers).where(RegisteredUsers.id == user_id)
    async with engine.connect() as connection:
        result = await connection.execute(statement)
        for line in result.all():
            if line[0] == user_id:
                return True
        return False


async def get_user_language(user_id: str) -> str:
    statement = select(RegisteredUsers).where(RegisteredUsers.id == user_id)
    async with engine.connect() as connection:
        result = await connection.execute(statement)
        for line in result.all():
            if line[0] == user_id:
                return line[1]
        return ""


async def get_user_time_zone(user_id: str) -> str:
    statement = select(RegisteredUsers).where(RegisteredUsers.id == user_id)
    async with engine.connect() as connection:
        result = await connection.execute(statement)
        for line in result.all():
            if line[0] == user_id:
                return line[2]
        return ""
