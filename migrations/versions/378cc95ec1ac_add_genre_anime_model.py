"""Add genre_anime model

Revision ID: 378cc95ec1ac
Revises: 1a93f48ce585
Create Date: 2021-10-11 16:38:56.367602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '378cc95ec1ac'
down_revision = '1a93f48ce585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres_animes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('anime_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['anime_id'], ['animes.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genres_animes')
    # ### end Alembic commands ###
