from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.config import ACTIVE_SEASON
from app.database.dependencies import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.player import PlayerRead
from app.services import player_service

router = APIRouter(prefix="/players", tags=["players"])

DbDep = Annotated[Session, Depends(get_db)]


@router.get("", response_model=PaginatedResponse[PlayerRead])
def list_players(
    db: DbDep,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=25, ge=1, le=100),
    team_id: Optional[str] = Query(default=None),
    season: Optional[str] = Query(default=ACTIVE_SEASON),
):
    players, total = player_service.get_players(
        db, skip=skip, limit=limit, team_id=team_id, season=season
    )
    return PaginatedResponse(data=players, total=total, skip=skip, limit=limit)


@router.get("/{player_id}", response_model=PlayerRead)
def get_player(player_id: str, db: DbDep):
    player = player_service.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
