from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from cruds import player as player_crud
from db.session import get_db
from schemas.team import PlayerStatusEnum
from schemas.player import PlayerSchema
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
def update_player_status(player_id: uuid.UUID, new_status: PlayerStatusEnum, user_id: uuid.UUID, db: Session = Depends(get_db)):
    player = player_crud.get_players_by_id(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # チームがこのユーザーのものであるかをチェック
    if player.team.user_id != user_id:
        # ユーザーチームでない場合はスタメン以外を設定できない
        if new_status != PlayerStatusEnum.STARTING_LINEUP:
            raise HTTPException(status_code=403, detail="Only user's team can have bench or out of bench players.")

    return player_crud.update_player_status(db, player, new_status)

@router.get("/{team_id}/{status}", response_model=List[PlayerSchema])
def get_players_by_status(team_id: uuid.UUID, status: PlayerStatusEnum, db: Session = Depends(get_db)):
    try:
        # プレイヤーを取得
        players = player_crud.get_players_by_status(db, team_id, status)

        # プレイヤーが見つからない場合、404エラーを返す
        if not players:
            raise HTTPException(status_code=404, detail=f"No players found for team {team_id} with status {status}.")

        return players

    except SQLAlchemyError as e:
        # データベース関連のエラーを処理
        raise HTTPException(status_code=500, detail="Database error occurred while fetching players.")
    
    except Exception as e:
        # 予期しないエラーを処理
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")