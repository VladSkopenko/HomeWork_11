from typing import List, Type

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactResponse


async def get_contacts(skip: int, limit: int, db: Session) -> list[Type[Contact]]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(name=body.name,
                      last_name=body.last_name,
                      email=body.email,
                      phone=body.phone,
                      birthday=body.birthday,
                      description=body.description)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact
