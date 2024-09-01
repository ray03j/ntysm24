from pydantic import BaseModel
from typing import List, Optional
from schemas.player import Player

class TeamBase(BaseModel):
    name: str
    formation: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    players: List[Player] = []

    class Config:
        orm_mode = True
