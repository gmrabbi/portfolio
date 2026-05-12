"""Add years of experience to user

Revision ID: e7f3c9e2a1b4
Revises: d5c2adb258f4
Create Date: 2026-05-12 01:45:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e7f3c9e2a1b4'
down_revision = 'd5c2adb258f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('years_of_experience', sa.Integer(), nullable=True, server_default='0'))


def downgrade():
    op.drop_column('user', 'years_of_experience')
