from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.user import User
from routers.auth import get_password_hash, verify_password, create_access_token
from cruds import user as user_crud
from schemas.user import SignupSchema, LoginSchema
router = APIRouter()

@router.post("/signup/")
def signup(data: SignupSchema, db: Session = Depends(get_db)):
    # すでにユーザーが存在するか確認
    existing_user = user_crud.get_user(db, data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # パスワードのハッシュ化
    hashed_password = get_password_hash(data.password)
    
    # 新規ユーザー作成
    new_user = user_crud.create_user(db, data.name, data.email, hashed_password)
    
    return {"message": "User created successfully", "user_id": new_user.user_id}

@router.post("/login/")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # トークン生成と保存
    access_token = create_access_token()
    user.access_token = access_token
    db.commit()
    
    return {"access_token": access_token, "token_type": "bearer"}
