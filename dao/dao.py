from models.users import Users
from models.posts import Posts
from models.profiles import Profiles
from .base import BaseDAO
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.exc import SQLAlchemyError


class UserDAO(BaseDAO):
    model = Users

    @classmethod
    async def create_user_with_profile(cls, session: AsyncSession, user_data: dict):
        new_user = cls.model(username = user_data['username'])
        session.add(new_user)
        await session.flush()

        new_profile = Profiles(
            user_id = new_user.id,
            email = user_data['email'],
            name = user_data['name'],
            age = user_data.get('age'),
            gender = user_data['gender'],
            proffession = user_data.get('proffession')
        )
        session.add(new_profile)
        try:
            await session.commit()
        except SQLAlchemyError as Er:
            await session.rollback()
            raise Er
        return new_user


class ProfileDAO(BaseDAO):
    model = Profiles


class PostDAO(BaseDAO):
    model = Posts

