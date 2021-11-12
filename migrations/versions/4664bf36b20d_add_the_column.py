"""add the column

Revision ID: 4664bf36b20d
Revises: 860dda7f79ff
Create Date: 2021-11-11 23:15:24.467604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4664bf36b20d'
down_revision = '860dda7f79ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(timezone=250), nullable=True),
    sa.Column('blogs_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogs_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
