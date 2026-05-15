from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.config import ACTIVE_SEASON
from app.database.dependencies import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.league import LeagueRead
from app.services import league_service

router = APIRouter(prefix="/leagues", tags=["leagues"])

DbDep = Annotated[Session, Depends(get_db)]


@router.get("", response_model=PaginatedResponse[LeagueRead])
def list_leagues(
    db: DbDep,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=25, ge=1, le=100),
    season: Optional[str] = Query(default=ACTIVE_SEASON),
):
    leagues, total = league_service.get_leagues(db, skip=skip, limit=limit, season=season)
    return PaginatedResponse(data=leagues, total=total, skip=skip, limit=limit)


@router.get("/{league_id}", response_model=LeagueRead)
def get_league(league_id: str, db: DbDep):
    league = league_service.get_league(db, league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league
