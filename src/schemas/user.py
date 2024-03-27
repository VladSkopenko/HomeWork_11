from pydantic import BaseModel, Field


class UserModel(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=5, max_length=250)
    password: str = Field(min_length=2, max_length=10)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: str
    avatar: str

    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

