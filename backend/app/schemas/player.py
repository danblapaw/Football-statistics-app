from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.player import Position


class PlayerBase(BaseModel):
    name: str
    team_id: str
    nationality: Optional[str] = None
    position: Optional[Position] = None
    birth_date: Optional[date] = None
    jersey_number: Optional[int] = None
    photo_url: Optional[str] = None


class PlayerCreate(PlayerBase):
    pass


class PlayerRead(PlayerBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
