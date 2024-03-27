from pydantic import BaseModel, Field
from datetime import date


class UserModel(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=5, max_length=250)
    password: str = Field(min_length=2, max_length=200)


class UserResponse(UserModel):
    ...
