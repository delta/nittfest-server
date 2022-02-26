"""
setup MYSQL database
"""
import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """
    Settings
    """

    environment: str = os.getenv("ENVIRONMENT")
    mysql_user: str = os.getenv("MYSQL_USER")
    mysql_password: str = os.getenv("MYSQL_PASSWORD")
    mysql_host: str = os.getenv("MYSQL_HOST")
    mysql_db: str = os.getenv("MYSQL_DATABASE")
    client_id: str = os.getenv("CLIENT_ID")
    client_secret: str = os.getenv("CLIENT_SECRET")
    redirect_url: str = os.getenv("REDIRECT_URL")
    frontend_url: str = os.getenv("FRONTEND_URL")
    resource_endpoint: str = os.getenv("RESOURCE_ENDPOINT")
    token_endpoint: str = os.getenv("TOKEN_ENDPOINT")
    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algo: str = os.getenv("JWT_ALGORITHM")
    mailgun_key: str = os.getenv("MAILGUN_KEY")
    mailgun_domain: str = os.getenv("MAILGUN_DOMAIN")
    mailgun_email: str = os.getenv("MAILGUN_EMAIL")
    core_mail: str = os.getenv("CORE_EMAIL")
    admin: str = os.getenv("ADMIN")
    test_db: str = os.getenv("TEST_DATABASE")
    test_jwt: str = os.getenv("TEST_JWT")

    sqlalchemy_database_url: str = (
        f"mysql+pymysql://{mysql_user}:"
        f"{mysql_password}@{mysql_host}/{mysql_db}"
    )

    sqlalchemy_database_test_url: str = f"sqlite:///tests/{test_db}"

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


settings = Settings()
