"""create_new_names_table

Revision ID: 88a60c6f480a
Revises:
Create Date: 2023-12-17 18:02:47.738828

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "88a60c6f480a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "names",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("name", sa.String),
    )


def downgrade():
    op.drop_table("names")
