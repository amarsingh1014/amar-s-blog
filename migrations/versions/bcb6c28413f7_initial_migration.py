"""Initial migration

Revision ID: bcb6c28413f7
Revises: 
Create Date: 2024-10-03 22:51:16.671950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bcb6c28413f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('obsidian_note')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('obsidian_note',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('file_path', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='obsidian_note_pkey'),
    sa.UniqueConstraint('file_path', name='obsidian_note_file_path_key')
    )
    # ### end Alembic commands ###
