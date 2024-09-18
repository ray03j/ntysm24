from passlib.context import CryptContext
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session
from api.db.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.user_id == user_id).first()

def create_user(db: Session, name: str, email: str, hashed_password: str):
    db_user = User(name=name, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
