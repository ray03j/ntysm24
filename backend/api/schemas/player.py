from pydantic import BaseModel
import uuid, enum

class PlayerSchema(BaseModel):
    player_id: uuid.UUID
    name: str
    position_id: uuid.UUID
    team_id: uuid.UUID
    strength: int

    class Config:
        orm_mode = True

class PlayerStatusEnum(enum.Enum):
    STARTING_LINEUP = "starting_lineup"
    BENCH = "bench"
    OUT_OF_BENCH = "out_of_bench"
