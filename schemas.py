from pydantic import BaseModel, ConfigDict
from typing import List
from enumsql import Gender, ProfessionEnum, StatusPost


class ProfilesPydantic(BaseModel):
    name: str
    email: str
    age: int | None
    gender: Gender
    proffession: ProfessionEnum

    model_config = ConfigDict(from_attributes=True, use_attribute_docstrings=True)


class UsersPydantic(BaseModel):
    username: str
    # profile: ProfilesPydantic

    model_config = ConfigDict(from_attributes=True, use_attribute_docstrings=True)


class UserWithIdAndUsernamePydantic(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)