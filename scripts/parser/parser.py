"""
Db data to csv parser script
"""
import csv
from datetime import date
from typing import Tuple

import pymysql

from scripts.constants import prefs_title
from config.settings import settings

NO_OF_PREFS = 3

cnx = pymysql.connect(
    host=settings.mysql_host,
    user=settings.mysql_user,
    password=settings.mysql_password,
    database=settings.mysql_db,
)


def get_query_year(year: int) -> str:
    """
    function to get query year using provided year
    """
    switcher = {1: "1", 2: "0", 3: "9", 4: "8"}
    return switcher.get(year)

def get_answers(question_list:list,user:Tuple)->list:
    """
    function to get response answer of a user
    """
    row = [user[1], user[2]]
    for question in question_list:
        answers = cnx.cursor()
        answers.execute(
            f"SELECT * FROM answers WHERE user_id={user[0]} and question_id={question}"
        )
        for answer in answers:
            row.append(answer[1])
            answers.close()
    return row

async def generate_preferences():
    """
    parses db data and writes to csv file
    using pymysql
    """
    data = []
    data.append(prefs_title)
    domains = cnx.cursor()
    domains.execute("SELECT * FROM domains")
    domain_list = {}
    for domain in domains:
        domain_list.update({domain[0]: domain[1]})
    domains.close()
    users = cnx.cursor()
    users.execute("SELECT * from users")
    for user in users:
        row = [user[1], user[2], user[3], user[4]]
        preferences = cnx.cursor()
        preferences.execute(
            f"SELECT * FROM preferences WHERE user_id={user[0]} ORDER BY preference_no"
        )
        i = 0
        for preference in preferences:
            row.append(domain_list.get(preference[3]))
            i += 1

        while i < NO_OF_PREFS:
            row.append("NONE")

        data.append(row)
        preferences.close()
    users.close()
    cnx.close()
    filename = f"scripts/parser/preferences-{date.today()}.csv"
    with open(filename, "w+", encoding="UTF-8") as my_csv:
        csv_writer = csv.writer(my_csv, delimiter=",")
        csv_writer.writerows(data)
    return filename


async def generate_forms_responses(domain: str, year: int) -> str:
    """
    parses db data and writes to csv file
    using pymysql
    """
    data = []
    question_list = []
    domains = cnx.cursor()
    domains.execute("SELECT * FROM domains")
    domain_list = {}
    for dom in domains:
        domain_list.update({dom[1]: dom[0]})
    domains.close()
    questions = cnx.cursor()
    title = ["Name", "Roll-Number"]
    questions.execute(
        f"SELECT * FROM questions WHERE domain_id={domain_list.get(domain)} ORDER BY id"
    )
    for question in questions:
        question_list.append(question[0])
        title.append(question[1])
    questions.close()
    data.append(title)
    users = cnx.cursor()
    users.execute(
        f"SELECT * from users where POSITION({get_query_year(year)} IN email) = 6"
    )
    for user in users:
        data.append(get_answers(question_list,user))
    filepath = f"scripts/parser/{domain}-{year}-{date.today()}.csv"
    with open(
        filepath,
        "w+",
        encoding="UTF-8",
    ) as my_csv:
        csv_writer = csv.writer(my_csv, delimiter=",")
        csv_writer.writerows(data)
    users.close()
    cnx.close()
    return filepath
