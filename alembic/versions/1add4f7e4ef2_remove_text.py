"""remove_text

Revision ID: 1add4f7e4ef2
Revises: 4333a6f1259d
Create Date: 2016-08-26 15:25:14.824558

"""

# revision identifiers, used by Alembic.
revision = '1add4f7e4ef2'
down_revision = '4333a6f1259d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('radio_scheduledprogram', u'deleted')
    op.drop_column(u'telephony_message', u'text')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'telephony_message', sa.Column(u'text', sa.VARCHAR(length=160), nullable=True))
    op.add_column('radio_scheduledprogram', sa.Column(u'deleted', sa.BOOLEAN(), nullable=True))
    ### end Alembic commands ###
