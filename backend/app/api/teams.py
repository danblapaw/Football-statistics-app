from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.config import ACTIVE_SEASON
from app.database.dependencies import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.team import TeamRead
from app.services import team_service

router = APIRouter(prefix="/teams", tags=["teams"])

DbDep = Annotated[Session, Depends(get_db)]


@router.get("", response_model=PaginatedResponse[TeamRead])
def list_teams(
    db: DbDep,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=25, ge=1, le=100),
    league_id: Optional[str] = Query(default=None),
    season: Optional[str] = Query(default=ACTIVE_SEASON),
):
    teams, total = team_service.get_teams(
        db, skip=skip, limit=limit, league_id=league_id, season=season
    )
    return PaginatedResponse(data=teams, total=total, skip=skip, limit=limit)


@router.get("/{team_id}", response_model=TeamRead)
def get_team(team_id: str, db: DbDep):
    team = team_service.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
