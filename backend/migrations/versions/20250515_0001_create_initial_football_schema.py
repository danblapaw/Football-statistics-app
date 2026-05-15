"""create initial football schema

Revision ID: 0001
Revises:
Create Date: 2025-05-15 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- Enums ---
    position_enum = sa.Enum(
        "goalkeeper", "defender", "midfielder", "forward",
        name="position_enum",
    )
    match_status_enum = sa.Enum(
        "scheduled", "live", "finished", "postponed", "cancelled",
        name="match_status_enum",
    )
    position_enum.create(op.get_bind(), checkfirst=True)
    match_status_enum.create(op.get_bind(), checkfirst=True)

    # --- leagues ---
    op.create_table(
        "leagues",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("country", sa.String(100), nullable=False),
        sa.Column("season", sa.String(20), nullable=False),
        sa.Column("logo_url", sa.String(500), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # --- teams ---
    op.create_table(
        "teams",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("league_id", sa.String(36), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("short_name", sa.String(10), nullable=True),
        sa.Column("founded", sa.Integer(), nullable=True),
        sa.Column("stadium", sa.String(150), nullable=True),
        sa.Column("logo_url", sa.String(500), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["league_id"], ["leagues.id"], ondelete="RESTRICT"),
    )

    # --- players ---
    op.create_table(
        "players",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("team_id", sa.String(36), nullable=False),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("nationality", sa.String(100), nullable=True),
        sa.Column("position", position_enum, nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("jersey_number", sa.Integer(), nullable=True),
        sa.Column("photo_url", sa.String(500), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"], ondelete="RESTRICT"),
    )

    # --- matches ---
    op.create_table(
        "matches",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("league_id", sa.String(36), nullable=False),
        sa.Column("home_team_id", sa.String(36), nullable=False),
        sa.Column("away_team_id", sa.String(36), nullable=False),
        sa.Column("played_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "status",
            match_status_enum,
            nullable=False,
            server_default="scheduled",
        ),
        sa.Column("home_score", sa.Integer(), nullable=True),
        sa.Column("away_score", sa.Integer(), nullable=True),
        sa.Column("matchday", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["league_id"], ["leagues.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["home_team_id"], ["teams.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["away_team_id"], ["teams.id"], ondelete="RESTRICT"),
    )

    # --- player_stats ---
    op.create_table(
        "player_stats",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("player_id", sa.String(36), nullable=False),
        sa.Column("match_id", sa.String(36), nullable=False),
        sa.Column("minutes_played", sa.Integer(), nullable=True),
        sa.Column("started", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("goals", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("assists", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("shots", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("shots_on_target", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("passes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("passes_completed", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("key_passes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("tackles", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("interceptions", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("clearances", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("yellow_cards", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("red_cards", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("xg", sa.Float(), nullable=True),
        sa.Column("xg_assist", sa.Float(), nullable=True),
        sa.Column("rating", sa.Float(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["player_id"], ["players.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["match_id"], ["matches.id"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table("player_stats")
    op.drop_table("matches")
    op.drop_table("players")
    op.drop_table("teams")
    op.drop_table("leagues")

    sa.Enum(name="match_status_enum").drop(op.get_bind(), checkfirst=True)
    sa.Enum(name="position_enum").drop(op.get_bind(), checkfirst=True)
