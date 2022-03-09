"""
migrate schemas
Revision ID: 7e7da3fc5104
Revises: 
Create Date: 2022-03-09 13:29:05.670229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7e7da3fc5104"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "clusters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("image_link", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.String(length=3000), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "domains",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("domain", sa.String(length=20), nullable=True),
        sa.Column("description", sa.String(length=3000), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("description", sa.String(length=3000), nullable=True),
        sa.Column("cluster_id", sa.Integer(), nullable=False),
        sa.Column("rules", sa.String(length=3000), nullable=True),
        sa.Column("form_link", sa.String(length=255), nullable=True),
        sa.Column("event_link", sa.String(length=255), nullable=True),
        sa.Column("image_link", sa.String(length=255), nullable=True),
        sa.Column("start_time", sa.String(length=25), nullable=True),
        sa.Column("end_time", sa.String(length=25), nullable=True),
        sa.Column("date", sa.String(length=25), nullable=True),
        sa.Column("is_reg_completed", sa.Boolean(), nullable=True),
        sa.Column("is_event_completed", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["cluster_id"],
            ["clusters.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question", sa.String(length=2000), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("is_subjective", sa.Boolean(), nullable=True),
        sa.Column("options", sa.PickleType(), nullable=True),
        sa.Column("domain_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["domain_id"],
            ["domains.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("mobile_number", sa.String(length=255), nullable=True),
        sa.Column("gender", sa.String(length=255), nullable=True),
        sa.Column("department_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["department_id"],
            ["departments.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("answer", sa.String(length=2000), nullable=True),
        sa.Column("question_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "points",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("point", sa.Float(), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("department_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["department_id"],
            ["departments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
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
    op.drop_table("points")
    op.drop_table("answers")
    op.drop_table("users")
    op.drop_table("questions")
    op.drop_table("events")
    op.drop_table("domains")
    op.drop_table("departments")
    op.drop_table("clusters")
    # ### end Alembic commands ###
