from typing import Optional

from pydantic import BaseModel, ConfigDict


class LeagueBase(BaseModel):
    name: str
    country: str
    season: str
    logo_url: Optional[str] = None


class LeagueCreate(LeagueBase):
    pass


class LeagueRead(LeagueBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
