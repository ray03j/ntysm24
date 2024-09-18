from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
# from sqlalchemy.dialects.postgresql import UUID
from schemas.team import TeamSchema
from schemas.player import PlayerSchema
from cruds import team as team_crud
from db.session import get_db
from typing import List
import uuid

router = APIRouter()

@router.get("/opponent/{team_id}", response_model=TeamSchema)
def get_opponent_team_route(team_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        opponent_team = team_crud.get_opponent_team(db, team_id)
        return opponent_team
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# チームの攻撃・守備力合計を計算
def calculate_team_stats(players: List[PlayerSchema]):
    total_attack = sum([player.attack for player in players])
    total_defense = sum([player.defense for player in players])
    return total_attack, total_defense