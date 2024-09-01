from sqlalchemy.orm import Session
from db.models import Team
from schemas.team import TeamCreate

def get_team_by_name(db: Session, name: str):
    return db.query(Team).filter(Team.name == name).first()

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: TeamCreate):
    db_team = Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
