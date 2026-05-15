from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.league import League
from app.models.player import Player
from app.models.team import Team


def get_players(
    db: Session,
    skip: int = 0,
    limit: int = 25,
    team_id: str | None = None,
    season: str | None = None,
) -> tuple[list[Player], int]:
    query = select(Player)
    count_query = select(func.count()).select_from(Player)
    if team_id:
        query = query.where(Player.team_id == team_id)
        count_query = count_query.where(Player.team_id == team_id)
    if season:
        query = query.join(Team).join(League).where(League.season == season)
        count_query = count_query.join(Team).join(League).where(League.season == season)
    total = db.execute(count_query).scalar_one()
    rows = db.execute(query.offset(skip).limit(limit)).scalars().all()
    return list(rows), total


def get_player(db: Session, player_id: str) -> Player | None:
    return db.get(Player, player_id)
