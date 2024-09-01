from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    position: str
    overall: int
    speed: int
    strength: int
    technique: int
    stamina: int

class PlayerCreate(PlayerBase):
    team_id: int

class Player(PlayerBase):
    id: int
    team_id: int

    class Config:
        orm_mode = True
