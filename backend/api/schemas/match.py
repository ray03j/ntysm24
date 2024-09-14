from pydantic import BaseModel
from typing import Optional
import uuid
from enum import Enum

class MatchSchema(BaseModel):
    match_id: uuid.UUID
    home_team_id: uuid.UUID
    away_team_id: uuid.UUID
    match_date: str
    result: Optional[str]

    class Config:
        orm_mode = True

class StrategyEnum(str, Enum):
    ATTACK = "attack"
    DEFENSE = "defense"
    BALANCED = "balanced"

class SimulateMatchRequest(BaseModel):
    my_team_id: uuid.UUID
    opponent_team_id: uuid.UUID
    strategy: str