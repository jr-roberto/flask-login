"""Mudanca na models.py

Revision ID: 6e03c675d963
Revises: e71c0cc3a092
Create Date: 2025-02-04 13:25:46.591735

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e03c675d963'
down_revision = 'e71c0cc3a092'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_column('idade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('idade', mysql.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
