from src.database.db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.models import User
from sqlalchemy import select


async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    query = select(User).filter_by(email=email)
    user = db.execute(query)
    user = user.scalar_one_or_none()
    return user
