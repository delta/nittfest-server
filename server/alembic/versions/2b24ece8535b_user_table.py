"""user table

Revision ID: 2b24ece8535b
Revises: f199bc92fca2
Create Date: 2022-01-16 09:00:24.412445

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "2b24ece8535b"
down_revision = "30591b09199e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("name", sa.String(length=255), nullable=True)
    )
    op.add_column(
        "users", sa.Column("email", sa.String(length=255), nullable=True)
    )
    op.add_column(
        "users",
        sa.Column("mobile_number", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "users", sa.Column("gender", sa.String(length=255), nullable=True)
    )
    op.drop_index("emailid", table_name="users")
    op.drop_column("users", "username")
    op.drop_column("users", "emailid")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("emailid", mysql.VARCHAR(length=50), nullable=True),
    )
    op.add_column(
        "users",
        sa.Column("username", mysql.VARCHAR(length=50), nullable=True),
    )
    op.create_index("emailid", "users", ["emailid"], unique=False)
    op.drop_column("users", "gender")
    op.drop_column("users", "mobile_number")
    op.drop_column("users", "email")
    op.drop_column("users", "name")
    # ### end Alembic commands ###
