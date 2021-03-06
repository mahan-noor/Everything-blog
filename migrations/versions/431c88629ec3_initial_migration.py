"""Initial Migration

Revision ID: 431c88629ec3
Revises: 438c9daa19c2
Create Date: 2021-05-02 15:57:02.928941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431c88629ec3'
down_revision = '438c9daa19c2'
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
