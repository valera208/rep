from dao.dao import UserDAO
from database import connection, Base
from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import run
from schemas import UsersPydantic, UserWithIdAndUsernamePydantic



# @connection
# async def get_all(session):
#     users = await UserDAO.get_all_users(session)
#     return users
#
# all_users = run(get_all())
# for i in all_users:
#     user_pydantic = UsersPydantic.from_orm(i)
#     print(user_pydantic.dict())

@connection
async def get_users_with_id_and_username(session):
    users = await UserDAO.get_users_with_id_and_username(session)
    return users

all_users_2 = run(get_users_with_id_and_username())
for i in all_users_2:
    rez = UserWithIdAndUsernamePydantic.from_orm(i)
    print(rez.dict())