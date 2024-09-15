from fastapi import FastAPI
from routers import player, team, match
from db.session import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(player.router, prefix="/players", tags=["players"])
app.include_router(team.router, prefix="/teams", tags=["teams"])
app.include_router(match.router, prefix="/match", tags=["match"])
