"""add season to matches and player_stats

Revision ID: 0002
Revises: 0001
Create Date: 2025-05-15 00:01:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0002"
down_revision: Union[str, None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

ACTIVE_SEASON = "2025-2026"


def upgrade() -> None:
    op.add_column(
        "matches",
        sa.Column(
            "season",
            sa.String(20),
            nullable=False,
            server_default=ACTIVE_SEASON,
        ),
    )
    op.add_column(
        "player_stats",
        sa.Column(
            "season",
            sa.String(20),
            nullable=False,
            server_default=ACTIVE_SEASON,
        ),
    )


def downgrade() -> None:
    op.drop_column("player_stats", "season")
    op.drop_column("matches", "season")
