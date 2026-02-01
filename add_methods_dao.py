from dao.dao import UserDAO
from database import connection
from asyncio import run
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, List, Any

@connection
async def create_user_1(user_data: dict, session: AsyncSession):
    new_user = await UserDAO.add_one(**user_data, session=session)
    print(f"Пользователь с {new_user.id} id добавлен")
    return new_user

one_user = {"username": "oliver_jackson"}
run(create_user_1(one_user))

@connection
async def create_users_2(session: AsyncSession, users_data: List[dict]):
    new_users = await UserDAO.add_many(instances=users_data, session=session)
    return new_users

# @connection
# async def create_user_with_profile(session: AsyncSession, )