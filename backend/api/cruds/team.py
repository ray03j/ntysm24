from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from api.db.models import Player, Team
from api.schemas.team import TeamSchema, PlayerStatusEnum
import random

def get_team_by_name(db: Session, name: str):
    return db.query(Team).filter(Team.name == name).first()

def get_player_by_team(db: Session, team_id: UUID):
    return db.query(Player).filter(Player.team_id == team_id).all()

def create_team(db: Session, team: TeamSchema):
    db_team = Team(name=team.name, coach_name=team.coach_name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_opponent_team(db: Session, user_team_id: UUID):
    # ユーザーのチーム以外のすべてのチームを取得
    teams = db.query(Team).filter(Team.team_id != user_team_id).all()
    
    if not teams:
        raise Exception("No opponent teams available")
    
    # ランダムに1つのチームを選ぶ
    opponent_team = random.choice(teams)
    return opponent_team


def update_player_status(db: Session, player: Player, new_status: PlayerStatusEnum):
    # プレイヤーの状態を更新
    player.status = new_status
    
    # コミット処理
    db.commit()
    db.refresh(player)  # 変更をリフレッシュして最新の情報を取得
    
    return player

def get_players_by_status(db: Session, user_team_id: UUID, status: PlayerStatusEnum):
    # チームIDとステータスが一致するプレイヤーを取得
    players = db.query(Player).filter(Player.team_id == user_team_id, Player.status == status).all()
    return players