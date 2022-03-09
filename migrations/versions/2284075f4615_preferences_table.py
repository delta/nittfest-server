"""
preferences table
Revision ID: 2284075f4615
Revises: 9ef7b81f0d4e
Create Date: 2022-03-09 14:00:10.228249

"""
# pylint: skip-file

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2284075f4615"
down_revision = "9ef7b81f0d4e"
branch_labels = None
depends_on = None


def upgrade():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "preferences",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("preference_no", sa.Integer(), nullable=True),
        sa.Column("domain_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["domain_id"],
            ["domains.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("preferences")
    # ### end Alembic commands ###
