from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str = Field(max_length=10)
    birthday: datetime
    description: str

