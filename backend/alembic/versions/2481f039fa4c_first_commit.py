"""First commit

Revision ID: 2481f039fa4c
Revises: 
Create Date: 2022-06-22 13:18:17.611383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2481f039fa4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('secretsanta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id', 'code'),
    sa.UniqueConstraint('code')
    )
    op.create_index(op.f('ix_secretsanta_id'), 'secretsanta', ['id'], unique=True)
    op.create_table('player',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('social_url', sa.String(), nullable=False),
    sa.Column('santa_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['santa_id'], ['secretsanta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_player_id'), 'player', ['id'], unique=False)
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Enum('DESIRE', 'ANTI_DESIRE', name='cardtype'), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_id'), 'card', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_card_id'), table_name='card')
    op.drop_table('card')
    op.drop_index(op.f('ix_player_id'), table_name='player')
    op.drop_table('player')
    op.drop_index(op.f('ix_secretsanta_id'), table_name='secretsanta')
    op.drop_table('secretsanta')
    # ### end Alembic commands ###