"""Add education and publication image fields

Revision ID: d5c2adb258f4
Revises: 9f4fd081141e
Create Date: 2026-05-11 19:15:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd5c2adb258f4'
down_revision = '9f4fd081141e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('publication', sa.Column('image', sa.String(length=300), nullable=True))
    op.add_column('user', sa.Column('school', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('college', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('university', sa.String(length=200), nullable=True))


def downgrade():
    op.drop_column('user', 'university')
    op.drop_column('user', 'college')
    op.drop_column('user', 'school')
    op.drop_column('publication', 'image')
