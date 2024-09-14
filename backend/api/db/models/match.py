import uuid
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.session import Base


class Match(Base):
    __tablename__ = 'matches'

    match_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    home_team_id = Column(UUID(as_uuid=True), ForeignKey('teams.team_id'))
    away_team_id = Column(UUID(as_uuid=True), ForeignKey('teams.team_id'))
    match_date = Column(DateTime, nullable=False)
    result = Column(String(50))  # "win", "loss", "draw"

    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
