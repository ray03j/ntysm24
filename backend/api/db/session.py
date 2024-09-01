from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 環境変数からDATABASE_URLを取得。設定されていない場合はエラーを発生させる
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")

# SQLAlchemyエンジンの作成
engine = create_engine(DATABASE_URL)

# セッションの設定
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの宣言
Base = declarative_base()

# データベースセッションを取得するための依存関係
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
