from fastapi import FastAPI
from routers import player, team, game
from db.session import engine
from db.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(player.router, prefix="/players", tags=["players"])
app.include_router(team.router, prefix="/teams", tags=["teams"])
app.include_router(game.router, prefix="/game", tags=["game"])
