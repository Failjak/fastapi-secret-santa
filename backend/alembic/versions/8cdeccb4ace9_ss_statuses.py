"""ss_statuses

Revision ID: 8cdeccb4ace9
Revises: b39cb0bbc0d1
Create Date: 2022-07-20 14:57:16.338986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects.postgresql import ENUM

revision = '8cdeccb4ace9'
down_revision = 'b39cb0bbc0d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    enum = ENUM('CREATED', 'READY', 'PLAYERS', 'SUBMITTED', 'FAILED', name='statustype', created_type=False)
    enum.create(op.get_bind(), checkfirst=False)
    op.add_column('secretsanta', sa.Column('status', enum, nullable=True))


def downgrade() -> None:
    op.drop_column('secretsanta', 'status')
    ENUM(name='statustype').drop(op.get_bind(), checkfirst=False)
