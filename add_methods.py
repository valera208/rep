from models.users import Users
from models.profiles import Profiles
from database import connection
from sqlalchemy.ext.asyncio import AsyncSession
from asyncio import run
from enumsql import Gender, ProfessionEnum, StatusPost
from dao.dao import UserDAO

# @connection
# async def create_user_example_1(username: str,session: AsyncSession) -> int:
#     """
#     Создает нового пользователя с использованием ORM SQLAlchemy.
#
#     Аргументы:
#     - username: str - имя пользователя
#     - email: str - адрес электронной почты
#     - password: str - пароль пользователя
#     - session: AsyncSession - асинхронная сессия базы данных
#
#     Возвращает:
#     - int - идентификатор созданного пользователя
#     """
#
#     user = Users(username=username)
#     session.add(user)
#     await session.commit()
#     return user.id
#
# new_user_id = run(create_user_example_1(username="shoto"))
#
# print(f"Новый пользователь с идентификатором {new_user_id} создан")


@connection
async def create_user_example_2(username: str,
                                name: str,
                                email: str,
                                age: int,
                                gender: Gender,
                                proffession: ProfessionEnum,
                                session: AsyncSession
                                ) -> dict[str: int]:
   try:
       user = Users(username=username)
       session.add(user)
       await session.flush()

       profile = Profiles(
           user_id=user.id,
           name=name,
           email=email,
           age=age,
           gender=gender,
           proffession=proffession
       )
       session.add(profile)
       await session.commit()

       print(f"Пользователь с {user.id} ID создан с профилем {profile.id} ID")
       return {"user id": user.id, "profile id": profile.id}

   except Exception as e:
       await session.rollback()
       raise e

# user_profile = run(create_user_example_2(
#     username="john_doe",
#     email="john.doe@example.com",
#     name="John",
#     age=28,
#     gender=Gender.MALE,
#     proffession=ProfessionEnum.ENGINEER,
# ))

# @connection
# async def create_user_example_3(users_data: list[dict] ,session: AsyncSession)  -> list[int]:
#     users_list = [Users(username = user_data['username']) for user_data in users_data]
#     session.add_all(users_list)
#     await session.commit()
#     return [user.id for user in users_list]
#
# users = [
#     {"username": "michael_brown"},
#     {"username": "sarah_wilson"},
#     {"username": "david_clark"},
#     {"username": "emma_walker"},
#     {"username": "james_martin"}
# ]
#
# run(create_user_example_3(users))


@connection
async def add_full_user(user_data: dict, session: AsyncSession):
    new_user = await UserDAO.create_user_with_profile(session=session, user_data=user_data)
    print(f"Добавлен новый пользователь с ID: {new_user.id}")
    return new_user.id

user_data_bob = {
    "username": "bob_smith",
    "email": "bob.smith@example.com",
    "name": "Bob",
    "age": 25,
    "gender": Gender.MALE,
    "profession": ProfessionEnum.DESIGNER,
}

run(add_full_user(user_data_bob))











