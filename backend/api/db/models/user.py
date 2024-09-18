from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from api.db.session import Base
import uuid

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    # 次の試合までの日数を管理するカラム
    days_until_next_match = Column(Integer, default=14)

    # ユーザーが管理するチームとのリレーション
    team = relationship("Team", back_populates="user")




