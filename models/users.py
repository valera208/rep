from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, unique_info


class Users(Base):
    __tablename__ = 'users'

    name: Mapped[unique_info] = mapped_column(nullable=False)

    profile: Mapped["Profiles"] = relationship(
        "Profiles",
        back_populates="user",
        uselist=False,  # Ключевой параметр для связи один-к-одному
        lazy="joined"  # Автоматически подгружает profile при запросе user
    )

    posts: Mapped[list["Posts"]] = relationship(
        "Posts",
        back_populates="user",
        cascade="all, delete-orphan"
    )