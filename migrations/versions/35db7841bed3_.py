"""empty message

Revision ID: 35db7841bed3
Revises: 1f29c08de89f
Create Date: 2014-08-28 17:15:01.328782

"""

# revision identifiers, used by Alembic.
revision = '35db7841bed3'
down_revision = '1f29c08de89f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.TEXT(), nullable=False))
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('users', 'name')
    ### end Alembic commands ###