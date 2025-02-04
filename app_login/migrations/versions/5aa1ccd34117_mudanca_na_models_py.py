"""Mudanca na models.py

Revision ID: 5aa1ccd34117
Revises: a8c3b39afd38
Create Date: 2025-02-04 10:59:48.311453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa1ccd34117'
down_revision = 'a8c3b39afd38'
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
