from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.league import League


def get_leagues(db: Session, skip: int = 0, limit: int = 25) -> tuple[list[League], int]:
    total = db.execute(select(func.count()).select_from(League)).scalar_one()
    rows = db.execute(select(League).offset(skip).limit(limit)).scalars().all()
    return list(rows), total


def get_league(db: Session, league_id: str) -> League | None:
    return db.get(League, league_id)
