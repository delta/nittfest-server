"""
setup MYSQL database
"""
import os
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """
    Settings
    """

    environment: str = os.getenv("ENVIRONMENT").upper()
    mysql_user: str = os.getenv("MYSQL_USER")
    mysql_password: str = os.getenv("MYSQL_PASSWORD")
    mysql_host: str = os.getenv("MYSQL_HOST")
    mysql_db: str = os.getenv("MYSQL_DATABASE")
    client_id: str = os.getenv("CLIENT_ID")
    client_secret: str = os.getenv("CLIENT_SECRET")
    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algo: str = os.getenv("JWT_ALGORITHM")
    sqlalchemy_database_url: str = (
        f"mysql+pymysql://{mysql_user}:"
        f"{mysql_password}@{mysql_host}/{mysql_db}"
    )

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


settings = Settings()
