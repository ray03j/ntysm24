from fastapi import Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.models import Player
from schemas.team import PlayerStatusEnum

import uuid 

def get_player_by_id(player_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        player = db.query(Player).filter(Player.player_id == player_id).first()
        return player
    except Exception as e:
        raise e

def get_position_of_player(position_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        position = db.query(Player).filter(Player.position_id == position_id).all()
        return position
    except Exception as e:
        raise e

def get_players_by_status(db: Session, user_team_id: uuid.UUID, status: PlayerStatusEnum):
    # チームIDとステータスが一致するプレイヤーを取得
    players = db.query(Player).filter(Player.team_id == user_team_id, Player.status == status).all()
    return players