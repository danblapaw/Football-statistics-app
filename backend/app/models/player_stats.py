from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.config import ACTIVE_SEASON

from .base import Base, TimestampMixin, new_uuid

if TYPE_CHECKING:
    from .match import Match
    from .player import Player


class PlayerStats(Base, TimestampMixin):
    __tablename__ = "player_stats"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    player_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("players.id", ondelete="CASCADE"), nullable=False
    )
    match_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("matches.id", ondelete="CASCADE"), nullable=False
    )
    season: Mapped[str] = mapped_column(
        String(20), nullable=False, default=ACTIVE_SEASON, server_default=ACTIVE_SEASON
    )

    # Participation
    minutes_played: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    started: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # Attacking
    goals: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    assists: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    shots: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    shots_on_target: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Passing
    passes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    passes_completed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    key_passes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Defending
    tackles: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    interceptions: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    clearances: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Discipline
    yellow_cards: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    red_cards: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # Advanced
    xg: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    xg_assist: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    player: Mapped["Player"] = relationship("Player", back_populates="stats")
    match: Mapped["Match"] = relationship("Match", back_populates="player_stats")

    def __repr__(self) -> str:
        return f"<PlayerStats player={self.player_id} match={self.match_id} [{self.season}]>"
