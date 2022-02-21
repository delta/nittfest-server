"""
Script to send mail using mailGun
"""

from datetime import date
import requests

from config.settings import settings
from server.models.errors import GenericError

file_path: str = "scripts/parser/"


def send_mail():
    """
    sends mail the response csv to fest-core via mail-gun api
    """
    try:
        with open(f"{file_path}/preferences-{date.today()}.csv",
        encoding="UTF-8",
        ) as file:
            res = requests.post(
                f"https://api.mailgun.net/v3/{settings.mailgun_domain}/messages",
                auth=("api", settings.mailgun_key),
                files=[
                    (
                        "attachment",
                        file
                    )
                ],
                data={
                    "from": f"NITTFEST-WebOps <mailgun@{settings.mailgun_domain}>",
                    "to": [settings.core_mail],
                    "subject": "Inductions Response",
                    "text": "Attachment of today's response can be found in this mail",
                },
            )
            if res.status_code == 200:
                print("Successfully sent")
            else:
                raise GenericError(
                    f"failed to send because {res.content.message}"
                )
    except GenericError as exception:
        print(f"Error: unable to send email due to : {exception}")
