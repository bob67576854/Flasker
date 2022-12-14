"""Initial Migration

Revision ID: c0065949695d
Revises: 
Create Date: 2022-08-10 20:03:38.135178

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c0065949695d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dateOfBirth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dateOfBirth', mysql.VARCHAR(length=10), nullable=True))
    # ### end Alembic commands ###
