from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.player import PlayerCreate, Player 
from cruds import player as player_crud
from db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Player])
def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = player_crud.get_players(db, skip=skip, limit=limit)
    return players

@router.post("/", response_model=Player)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = player_crud.create_player(db, player)
    return db_player
