from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas.user import UserModel, UserResponse, TokenSchema

router = APIRouter(prefix='/auth', tags=["auth"])


@router.post("/signup")
async def signup(body: UserModel, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.email == body.username).first()
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    new_user = User(email=body.username, password=hash_handler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"new_user": new_user.email}


@router.post("/login")
async def login(body: UserModel, db: Session = Depends(get_db)):
    pass
    return {}


@router.get("/refresh_token")
async def refresh_token(body: UserModel, db: Session = Depends(get_db)):
    pass
    return {}