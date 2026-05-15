from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, new_uuid

if TYPE_CHECKING:
    from .league import League
    from .match import Match
    from .player import Player


class Team(Base, TimestampMixin):
    __tablename__ = "teams"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    league_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("leagues.id", ondelete="RESTRICT"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    short_name: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    founded: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    stadium: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    league: Mapped["League"] = relationship("League", back_populates="teams")
    players: Mapped[List["Player"]] = relationship("Player", back_populates="team")
    home_matches: Mapped[List["Match"]] = relationship(
        "Match", foreign_keys="Match.home_team_id", back_populates="home_team"
    )
    away_matches: Mapped[List["Match"]] = relationship(
        "Match", foreign_keys="Match.away_team_id", back_populates="away_team"
    )

    def __repr__(self) -> str:
        return f"<Team {self.name}>"
