from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.league import League


def get_leagues(
    db: Session,
    skip: int = 0,
    limit: int = 25,
    season: str | None = None,
) -> tuple[list[League], int]:
    query = select(League)
    count_query = select(func.count()).select_from(League)
    if season:
        query = query.where(League.season == season)
        count_query = count_query.where(League.season == season)
    total = db.execute(count_query).scalar_one()
    rows = db.execute(query.offset(skip).limit(limit)).scalars().all()
    return list(rows), total


def get_league(db: Session, league_id: str) -> League | None:
    return db.get(League, league_id)
