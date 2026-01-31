from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import text
from database import Base, unique_info
from enumsql import Gender, ProfessionEnum, StatusPost


class Profiles(Base):
    __tablename__ = 'profiles'
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
    name: Mapped[unique_info] = mapped_column(nullable=False)
    email: Mapped[unique_info] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[Gender]
    proffession: Mapped[ProfessionEnum] = mapped_column(default=ProfessionEnum.UNEMPLOYED)

    user: Mapped["Users"] = relationship(
        "Users",
        uselist=False,
        back_populates="profile"
    )
