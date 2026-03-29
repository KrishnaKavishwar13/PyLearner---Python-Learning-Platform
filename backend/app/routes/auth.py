from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)

    db_user = User(name=user.name, email=user.email, password=hashed_pw)
    db.add(db_user)
    db.commit()

    return {"message": "User registered"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        return {"error": "Invalid credentials"}

    token = create_token({"sub": db_user.email})
    return {"access_token": token}