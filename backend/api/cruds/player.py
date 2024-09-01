from sqlalchemy.orm import Session
from db.models import Player
from schemas.player import PlayerCreate

def get_players(db:Session, skip:int=0, limit:int=10):
    return db.query(Player).offset(skip).limit(limit).all()

def create_player(db: Session, player: PlayerCreate):
    db_player = Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
