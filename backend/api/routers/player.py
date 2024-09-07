from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from cruds import player as player_crud
from db.session import get_db
from schemas.player import PlayerSchema, PlayerStatusEnum
import uuid 
from typing import List

router = APIRouter()

@router.get("/{player_id}", response_model=PlayerSchema)
def get_player(player_id: uuid.UUID, db: Session = Depends(get_db)):
    player = player_crud.get_players_by_id(db, player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/position/{position_id}", response_model=List[PlayerSchema])
def get_players_by_position(position_id: uuid.UUID, db: Session = Depends(get_db)):
    players = player_crud.get_position_of_player(db, position_id)
    return players

@router.patch("/{player_id}/status")
def update_player_status(player_id: uuid.UUID, new_status: PlayerStatusEnum, db: Session, user_id: uuid.UUID):
    player = player_crud.get_players_by_id(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # チームがこのユーザーのものであるかをチェック
    if player.team.user_id != user_id:
        # ユーザーチームでない場合はスタメン以外を設定できない
        if new_status != PlayerStatusEnum.STARTING_LINEUP:
            raise HTTPException(status_code=403, detail="Only user's team can have bench or out of bench players.")

    return player_crud.update_player_status(db, player, new_status)

@router.get("/players/status/{status}", response_model=List[PlayerSchema])
def get_players_by_status(status: PlayerStatusEnum, db: Session = Depends(get_db)):
    players = player_crud.get_players_by_status(db, status)
    return players