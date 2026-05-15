from __future__ import annotations

import enum
from datetime import date
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Date, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, new_uuid

if TYPE_CHECKING:
    from .player_stats import PlayerStats
    from .team import Team


class Position(str, enum.Enum):
    GOALKEEPER = "goalkeeper"
    DEFENDER = "defender"
    MIDFIELDER = "midfielder"
    FORWARD = "forward"


class Player(Base, TimestampMixin):
    __tablename__ = "players"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    team_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("teams.id", ondelete="RESTRICT"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    nationality: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    position: Mapped[Optional[Position]] = mapped_column(
        Enum(Position, name="position_enum"), nullable=True
    )
    birth_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    jersey_number: Mapped[Optional[int]] = mapped_column(nullable=True)
    photo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    team: Mapped["Team"] = relationship("Team", back_populates="players")
    stats: Mapped[List["PlayerStats"]] = relationship(
        "PlayerStats", back_populates="player"
    )

    def __repr__(self) -> str:
        return f"<Player {self.name} ({self.position})>"
