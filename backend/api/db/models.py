import uuid
from sqlalchemy import Column, Integer, String , ForeignKey, Date
from sqlalchemy.orm import relationship
from .session import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, default=lambda:str(uuid.uuid4()))
    name = Column(String, nullable=False)
    formation = Column(String, nullable=True)

    # リレーションシップを定義
    players = relationship("Player", back_populates="team")
    home_matches = relationship("Match", foreign_keys="[Match.home_team_id]", back_populates="home_team")
    away_matches = relationship("Match", foreign_keys="[Match.away_team_id]", back_populates="away_team")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, default=lambda:str(uuid.uuid4()))
    team_id = Column(Integer, ForeignKey("teams.id"))

    name = Column(String, nullable=False)
    position = Column(String, nullable=False)

    overall = Column(Integer)
    speed = Column(Integer)
    strength = Column(Integer)
    technique = Column(Integer)
    stamina = Column(Integer)

    # リレーションシップを定義
    team = relationship("Team", back_populates="players")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    date = Column(Date, nullable=False)
    home_score = Column(Integer)
    away_score = Column(Integer)

#     # リレーションシップを定義
    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
