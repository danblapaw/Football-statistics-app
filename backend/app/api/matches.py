from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.match import MatchStatus
from app.schemas.common import PaginatedResponse
from app.schemas.match import MatchRead
from app.services import match_service

router = APIRouter(prefix="/matches", tags=["matches"])

DbDep = Annotated[Session, Depends(get_db)]


@router.get("", response_model=PaginatedResponse[MatchRead])
def list_matches(
    db: DbDep,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=25, ge=1, le=100),
    league_id: Optional[str] = Query(default=None),
    status: Optional[MatchStatus] = Query(default=None),
):
    matches, total = match_service.get_matches(
        db, skip=skip, limit=limit, league_id=league_id, status=status
    )
    return PaginatedResponse(data=matches, total=total, skip=skip, limit=limit)


@router.get("/{match_id}", response_model=MatchRead)
def get_match(match_id: str, db: DbDep):
    match = match_service.get_match(db, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
