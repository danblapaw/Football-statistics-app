from typing import Optional

from pydantic import BaseModel, ConfigDict


class PlayerStatsBase(BaseModel):
    player_id: str
    match_id: str
    minutes_played: Optional[int] = None
    started: bool = False
    goals: int = 0
    assists: int = 0
    shots: int = 0
    shots_on_target: int = 0
    passes: int = 0
    passes_completed: int = 0
    key_passes: int = 0
    tackles: int = 0
    interceptions: int = 0
    clearances: int = 0
    yellow_cards: int = 0
    red_cards: int = 0
    xg: Optional[float] = None
    xg_assist: Optional[float] = None
    rating: Optional[float] = None


class PlayerStatsCreate(PlayerStatsBase):
    pass


class PlayerStatsRead(PlayerStatsBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
