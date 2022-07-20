"""ondelete_CASCADE

Revision ID: b39cb0bbc0d1
Revises: 2898e4b3b0f7
Create Date: 2022-07-20 14:40:55.516481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b39cb0bbc0d1'
down_revision = '2898e4b3b0f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('player_gives_to_id_fkey', 'player', type_='foreignkey')
    op.create_foreign_key(None, 'player', 'player', ['gives_to_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'player', type_='foreignkey')
    op.create_foreign_key('player_gives_to_id_fkey', 'player', 'player', ['gives_to_id'], ['id'])
    # ### end Alembic commands ###