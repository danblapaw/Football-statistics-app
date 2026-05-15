from typing import Optional

from pydantic import BaseModel, ConfigDict


class TeamBase(BaseModel):
    name: str
    league_id: str
    short_name: Optional[str] = None
    founded: Optional[int] = None
    stadium: Optional[str] = None
    logo_url: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
