"""Mudanca na models.py

Revision ID: 532e4f7e8ec7
Revises: db10e42450c5
Create Date: 2025-02-04 10:52:38.762972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532e4f7e8ec7'
down_revision = 'db10e42450c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_cadastro', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_column('data_cadastro')

    # ### end Alembic commands ###
