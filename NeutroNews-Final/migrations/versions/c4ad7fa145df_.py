"""empty message

Revision ID: c4ad7fa145df
Revises: 
Create Date: 2023-02-19 15:01:56.809147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4ad7fa145df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hot_news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('newsTitle', sa.String(length=200), nullable=False),
    sa.Column('newsUrl', sa.String(length=1000), nullable=False),
    sa.Column('newsImage', sa.String(length=1000), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('up_to_date_news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('newsTitle', sa.String(length=200), nullable=False),
    sa.Column('newsText', sa.String(length=200000), nullable=False),
    sa.Column('newsUrl', sa.String(length=1000), nullable=False),
    sa.Column('newsImage', sa.String(length=1000), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('sentiment', sa.String(length=25), nullable=True),
    sa.Column('category', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('up_to_date_news')
    op.drop_table('hot_news')
    # ### end Alembic commands ###
