"""empty message

Revision ID: 1d31622bbed
Revises: 32f2dcfc96d
Create Date: 2015-09-21 14:29:04.876095

"""

# revision identifiers, used by Alembic.
revision = '1d31622bbed'
down_revision = '32f2dcfc96d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('contact_us', sa.Text(convert_unicode=True), nullable=True))
    op.add_column('departments', sa.Column('how_you_can_use_this_data', sa.Text(convert_unicode=True), nullable=True))
    op.add_column('departments', sa.Column('what_this_is', sa.Text(convert_unicode=True), nullable=True))
    op.add_column('departments', sa.Column('why_we_are_doing_this', sa.Text(convert_unicode=True), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('departments', 'why_we_are_doing_this')
    op.drop_column('departments', 'what_this_is')
    op.drop_column('departments', 'how_you_can_use_this_data')
    op.drop_column('departments', 'contact_us')
    ### end Alembic commands ###
