from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse
from src.repository import contacts as repository_notes

router = APIRouter(prefix='/notes', tags=["notes"])


@router.get("/", response_model=List[ContactResponse])
async def read_notes(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    contacts = await repository_notes.get_contacts(skip, limit, db)
    return contacts


@router.post("/", response_model=ContactResponse)
async def create_note(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_notes.create_contact(body, db)
