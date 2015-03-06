"""added table CounterStat

Revision ID: 450fe5f7942d
Revises: bd0dab2e478
Create Date: 2015-02-19 23:40:08.934834

"""

# revision identifiers, used by Alembic.
revision = '450fe5f7942d'
down_revision = 'bd0dab2e478'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('counter_stat',
    sa.Column('name', sa.String(length=127), nullable=False),
    sa.Column('counter_type', sa.String(length=30), nullable=True),
    sa.Column('counter', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('counter_stat')
    ### end Alembic commands ###
