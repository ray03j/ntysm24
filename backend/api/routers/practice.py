from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from db.session import get_db
from db.models import User, Player
from cruds import user as user_crud
from cruds import player as player_crud
from schemas.team import PlayerStatusEnum

router = APIRouter()

# プレイヤーの成長確率を定義
def grow_player(player: Player):
    # プレイヤーの攻撃・防御が成長する確率（例：20%）
    growth_chance = 0.2  # 20%の成長確率
    if random.random() < growth_chance:
        player.attack += random.randint(1, 5)
        player.defense += random.randint(1, 5)

@router.post("/{user_id}")
def practice(user_id: str, db: Session = Depends(get_db)):
    # ユーザーを取得
    user = user_crud.get_user_by_id(db, user_id)
    
    if not user:
        return {"error": "ユーザーが見つかりません"}
    
    # 試合日(0日)であれば練習はできない
    if user.days_until_next_match == 0:
        return {"message": "今日は試合日です。練習はできません。"}

    # プレイヤーの成長処理
    players = player_crud.get_players_by_status(db, user.team[0].team_id, PlayerStatusEnum.STARTING_LINEUP)
    if not players:
        raise HTTPException(status_code=404, detail="チームに該当するプレイヤーが見つかりません")

    for player in players:
        grow_player(player)
    
    # 次の試合までの日数を1日減らす
    user.days_until_next_match -= 1

    # データベースの変更を保存
    db.commit()
    
    return {"message": "プレイヤーが成長しました！", "days_until_next_match": user.days_until_next_match}
