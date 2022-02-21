# pylint: skip-file
from logging.config import fileConfig
from os import environ

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from config.logger import logger
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
cmd_kwargs = context.get_x_argument(as_dictionary=True)

if "db" not in cmd_kwargs:
    raise Exception(
        "We couldn't find `db` in the CLI arguments. "
        "Please verify `alembic` was run with `-x db=<db_name>` "
        "(e.g. `alembic -x db=development upgrade head`)"
    )
db_name = cmd_kwargs["db"]

# ...
def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    # Overload db config on top of alembic config
    alembic_config = config.get_section(config.config_ini_section)
    db_config = config.get_section(db_name)
    for key in db_config:
        alembic_config[key] = db_config[key]
    engine = engine_from_config(
        alembic_config, prefix="sqlalchemy.", poolclass=pool.NullPool
    )
