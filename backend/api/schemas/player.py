from pydantic import BaseModel
import uuid

class PlayerSchema(BaseModel):
    player_id: uuid.UUID
    name: str
    position_id: uuid.UUID
    team_id: uuid.UUID
    attack: int
    defense: int

    class Config:
        orm_mode = True

