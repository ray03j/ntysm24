import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.session import Base

class Team(Base):
    __tablename__ = 'teams'

    team_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    # ユーザーがこのチームを管理している場合、user_idが設定される
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)

    user = relationship("User", back_populates="team")
    players = relationship("Player", back_populates="team")

