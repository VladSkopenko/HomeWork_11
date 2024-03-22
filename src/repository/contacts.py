from typing import List, Type

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactResponse


async def get_contacts(skip: int, limit: int, db: Session) -> list[Type[Contact]]:
    return db.query(Contact).offset(skip).limit(limit).all()
