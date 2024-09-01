from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.team import TeamCreate, Team
from cruds import team as team_crud
from db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[Team])
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teams = team_crud.get_teams(db, skip=skip, limit=limit)
    return teams

@router.post("/", response_model=Team)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    db_team = team_crud.create_team(db, team)
    return db_team
