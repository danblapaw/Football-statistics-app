from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.match import Match, MatchStatus


def get_matches(
    db: Session,
    skip: int = 0,
    limit: int = 25,
    league_id: str | None = None,
    status: MatchStatus | None = None,
) -> tuple[list[Match], int]:
    query = select(Match)
    count_query = select(func.count()).select_from(Match)
    if league_id:
        query = query.where(Match.league_id == league_id)
        count_query = count_query.where(Match.league_id == league_id)
    if status:
        query = query.where(Match.status == status)
        count_query = count_query.where(Match.status == status)
    total = db.execute(count_query).scalar_one()
    rows = db.execute(query.offset(skip).limit(limit)).scalars().all()
    return list(rows), total


def get_match(db: Session, match_id: str) -> Match | None:
    return db.get(Match, match_id)
