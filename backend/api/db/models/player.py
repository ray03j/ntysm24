from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from schemas.player import PlayerStatusEnum
import uuid

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    player_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    position_id = Column(UUID(as_uuid=True), ForeignKey('positions.position_id'))
    team_id = Column(UUID(as_uuid=True), ForeignKey('teams.team_id'))
    strength = Column(Integer, nullable=False)

    # プレイヤーの状態（ユーザーチームの場合は3つ、他のチームはスタメンのみ）
    status = Column(Enum(PlayerStatusEnum), nullable=False)

    position = relationship("Position")
    team = relationship("Team")


class Position(Base):
    __tablename__ = 'positions'

    position_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    position_name = Column(String(50), unique=True, nullable=False)