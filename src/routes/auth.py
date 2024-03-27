from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas.user import UserModel, UserResponse, TokenSchema

router = APIRouter(prefix='/auth', tags=["auth"])


@router.post("/signup")
async def signup(body: UserModel, db: Session = Depends(get_db)):
    pass
    return {}


@router.post("/login")
async def login(body: UserModel, db: Session = Depends(get_db)):
    pass
    return {}


@router.get("/refresh_token")
async def refresh_token(body: UserModel, db: Session = Depends(get_db)):
    pass
    return {}