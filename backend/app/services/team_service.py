from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.league import League
from app.models.team import Team


def get_teams(
    db: Session,
    skip: int = 0,
    limit: int = 25,
    league_id: str | None = None,
    season: str | None = None,
) -> tuple[list[Team], int]:
    query = select(Team)
    count_query = select(func.count()).select_from(Team)
    if league_id:
        query = query.where(Team.league_id == league_id)
        count_query = count_query.where(Team.league_id == league_id)
    if season:
        query = query.join(League).where(League.season == season)
        count_query = count_query.join(League).where(League.season == season)
    total = db.execute(count_query).scalar_one()
    rows = db.execute(query.offset(skip).limit(limit)).scalars().all()
    return list(rows), total


def get_team(db: Session, team_id: str) -> Team | None:
    return db.get(Team, team_id)
