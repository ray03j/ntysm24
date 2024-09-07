from fastapi import Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.models import Player
from schemas.player import PlayerStatusEnum
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

def update_player_status(db: Session, player: Player, new_status: PlayerStatusEnum):
    # プレイヤーの状態を更新
    player.status = new_status
    
    # コミット処理
    db.commit()
    db.refresh(player)  # 変更をリフレッシュして最新の情報を取得
    
    return player

def get_players_by_status(db: Session, status: PlayerStatusEnum):
    # 引数として受け取ったステータスに一致するプレイヤーを取得
    players = db.query(Player).filter(Player.status == status).all()
    return players