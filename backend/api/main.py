from fastapi import FastAPI
from routers import player, team, match, user, practice
from db.session import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(player.router, prefix="/players", tags=["players"])
app.include_router(team.router, prefix="/teams", tags=["teams"])
app.include_router(practice.router, prefix="/practice", tags=["practice"])
app.include_router(match.router, prefix="/match", tags=["match"])
