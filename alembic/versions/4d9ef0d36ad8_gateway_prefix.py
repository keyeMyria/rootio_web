"""gateway_prefix

Revision ID: 4d9ef0d36ad8
Revises: 23ff5dd92328
Create Date: 2014-04-29 20:40:59.740457

"""

# revision identifiers, used by Alembic.
revision = '4d9ef0d36ad8'
down_revision = '23ff5dd92328'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('telephony_gateway', sa.Column('gateway_prefix', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('telephony_gateway', 'gateway_prefix')
    ### end Alembic commands ###