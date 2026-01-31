from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import text
from database import Base, unique_info
from enumsql import Gender, ProfessionEnum, StatusPost
class Posts(Base):
    __tablename__ = 'posts'

    title: Mapped[str]
    content: Mapped[str]
    status: Mapped[StatusPost] = mapped_column(
        default=StatusPost.DRAFT,
        server_default=text("'DRAFT'")
    )
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="posts",

    )