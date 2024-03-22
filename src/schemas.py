from datetime import datetime
from pydantic import BaseModel, Field, validator


class ContactModel(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str = Field(max_length=10)
    birthday: datetime
    description: str


class ContactResponse(ContactModel):
    id: int

    class Config:
        from_attributes = True
