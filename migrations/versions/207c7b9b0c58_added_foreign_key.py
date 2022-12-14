"""added Foreign Key

Revision ID: 207c7b9b0c58
Revises: 540dbb1067d3
Create Date: 2022-08-13 14:05:57.698283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207c7b9b0c58'
down_revision = '540dbb1067d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('poster_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['poster_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'poster_id')
    # ### end Alembic commands ###
