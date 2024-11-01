"""create tables

Revision ID: bfd640f2cf8b
Revises: 
Create Date: 2024-10-26 22:40:36.550301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'bfd640f2cf8b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rubaiyat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_with_parentheses', sa.Boolean(), nullable=False),
    sa.Column('section', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('poem_body', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('poem_body_with_ruby', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('is_boozeism', sa.Boolean(), nullable=False),
    sa.Column('footnote', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('yourtag',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('rubaiyat_id', sa.Integer(), nullable=False),
    sa.Column('tag', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.ForeignKeyConstraint(['rubaiyat_id'], ['rubaiyat.id'], ),
    sa.PrimaryKeyConstraint('tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('yourtag')
    op.drop_table('rubaiyat')
    # ### end Alembic commands ###
