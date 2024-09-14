from pydantic import BaseModel
from uuid import UUID
import enum

class TeamSchema(BaseModel):
    team_id: UUID
    name: str
    user_id: UUID | None  # 管理者がいない場合もあるのでNullable
    
    class Config:
        orm_mode = True

class PlayerStatusEnum(enum.Enum):
    STARTING_LINEUP = "starting_lineup"
    BENCH = "bench"
    OUT_OF_BENCH = "out_of_bench"
