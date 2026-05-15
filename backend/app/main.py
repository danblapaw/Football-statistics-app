from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import leagues, matches, players, teams

app = FastAPI(
    title="Football Statistics API",
    description="Professional football statistics and analytics platform",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api"
app.include_router(leagues.router, prefix=API_PREFIX)
app.include_router(teams.router, prefix=API_PREFIX)
app.include_router(players.router, prefix=API_PREFIX)
app.include_router(matches.router, prefix=API_PREFIX)


@app.get("/")
def root():
    return {"status": "ok", "message": "Football Statistics API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
