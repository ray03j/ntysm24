import random
from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from routers.player import get_players_by_status
from schemas.team import PlayerStatusEnum
from services.game_service import simulate_game
from schemas.match import StrategyEnum, SimulateMatchRequest
from schemas.player import PlayerSchema
import uuid
from db.session import get_db

router = APIRouter()

@router.get("/simulate")
async def simulate():
    result = simulate_game()
    return {"result": result}


# 得点確率を計算する関数
def calculate_score_probability(player: PlayerSchema, opponent_defense: int, strategy: StrategyEnum):
    base_attack = player.attack

    # 戦略に応じて攻撃力に補正をかける
    if strategy == StrategyEnum.ATTACK:
        attack_multiplier = 1.2  # 攻撃重視では攻撃力を20%増加
    elif strategy == StrategyEnum.DEFENSE:
        attack_multiplier = 0.8  # 守備重視では攻撃力を20%減少
    else:  # BALANCED 戦略
        attack_multiplier = 1.0

    # 攻撃力に補正を適用
    modified_attack = base_attack * attack_multiplier

    # 得点確率の算出: 攻撃力に対して相手チームの守備力で割る
    score_probability = modified_attack / (modified_attack + opponent_defense)

    return score_probability


# チームの攻撃力と守備力を計算する関数
def calculate_total_power(players: List[PlayerSchema]) -> Dict[str, int]:
    total_attack = sum(player.attack for player in players)
    total_defense = sum(player.defense for player in players)
    return {"attack": total_attack, "defense": total_defense}



# 試合をシミュレートするエンドポイント
@router.post("/simulate_match/")
def simulate_match(request: SimulateMatchRequest, db: Session = Depends(get_db)):
    # 自分のチームと相手チームのスタメンを取得
    my_team_players = get_players_by_status(request.my_team_id, PlayerStatusEnum.STARTING_LINEUP, db)
    opponent_team_players = get_players_by_status(request.opponent_team_id, PlayerStatusEnum.STARTING_LINEUP, db)

    if not my_team_players or not opponent_team_players:
        raise HTTPException(status_code=404, detail="One of the teams has no starting lineup players.")

    # 自分チームと相手チームの攻撃・防御力を計算
    my_team_power = calculate_total_power(my_team_players)
    opponent_team_power = calculate_total_power(opponent_team_players)

    my_total_score = 0
    opponent_total_score = 0

    # 自分チームの得点判定
    for player in my_team_players:
        score_probability = calculate_score_probability(player, opponent_team_power["defense"], request.strategy)
        if random.random() < score_probability:
            my_total_score += 1

    # 相手チームの得点判定
    for opponent in opponent_team_players:
        score_probability = calculate_score_probability(opponent, my_team_power["defense"], StrategyEnum.BALANCED)
        if random.random() < score_probability:
            opponent_total_score += 1

    return {
        "my_team_score": my_total_score,
        "opponent_team_score": opponent_total_score
    }