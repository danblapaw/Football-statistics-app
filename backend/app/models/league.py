from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, new_uuid

if TYPE_CHECKING:
    from .match import Match
    from .team import Team


class League(Base, TimestampMixin):
    __tablename__ = "leagues"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    season: Mapped[str] = mapped_column(String(20), nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    teams: Mapped[List["Team"]] = relationship("Team", back_populates="league")
    matches: Mapped[List["Match"]] = relationship("Match", back_populates="league")

    def __repr__(self) -> str:
        return f"<League {self.name} ({self.season})>"
