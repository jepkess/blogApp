"""add the column

Revision ID: 788dfd09d3ec
Revises: 8635242935a0
Create Date: 2021-11-11 23:03:16.549208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788dfd09d3ec'
down_revision = '8635242935a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
