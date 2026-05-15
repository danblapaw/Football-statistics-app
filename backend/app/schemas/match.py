from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.match import MatchStatus


class MatchBase(BaseModel):
    league_id: str
    home_team_id: str
    away_team_id: str
    played_at: Optional[datetime] = None
    status: MatchStatus = MatchStatus.SCHEDULED
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    matchday: Optional[int] = None


class MatchCreate(MatchBase):
    pass


class MatchRead(MatchBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
