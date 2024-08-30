from fastapi import APIRouter
from services.game_service import simulate_game

router = APIRouter()

@router.get("/simulate")
async def simulate():
    result = simulate_game()
    return {"result": result}
