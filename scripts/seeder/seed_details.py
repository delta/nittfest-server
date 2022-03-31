"""
Seed Main data
"""

from requests.sessions import Session

from config.logger import logger
from scripts.main_constants import clusters, events, points, departments
from scripts.test_constants import test_departments, test_user
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point
from server.schemas.users import Users


async def seed_maindb(database: Session):
    """
    Seed the database with teams
    """
    try:
        logger.info("Seeding main database")
        if database.query(Department).count() == 0:
            logger.info("Seeding database with test departments")
            for department in departments:
                database.add(
                    Department(
                        key=department["id"],
                        name=department["name"],
                        description=department["description"],
                    )
                )
            database.commit()
        # if database.query(Users).count() == 0:
        #     database.add(
        #         Users(
        #             name=test_user["name"],
        #             email=test_user["email"],
        #             mobile_number=test_user["mobile_number"],
        #             gender=test_user["gender"],
        #             department_id=test_user["department_id"],
        #             fcm_token=None,
        #         )
        #     )
        #    database.commit()
        if database.query(Cluster).count() == 0:
            for cluster in clusters:
                database.add(
                    Cluster(
                        key=cluster["id"],
                        name=cluster["name"],
                        image_link=cluster["image_link"],
                    )
                )
            database.commit()
        if database.query(Event).count() == 0:
            for event in events:
                database.add(
                    Event(
                        key=event["id"],
                        name=event["name"],
                        description=event["description"],
                        rules=event["rules"],
                        cluster_id=event["cluster_id"],
                        image_link=event["image_link"],
                        form_link=event["form_link"],
                        event_link=event["event_link"],
                        start_time=event["start_time"],
                        end_time=event["end_time"],
                        is_reg_completed=event["is_reg_completed"],
                        is_event_completed=event["is_event_completed"],
                    )
                )
                database.commit()
        if database.query(Point).count() == 0:
            for point in points:
                database.add(
                    Point(
                        point=point["point"],
                        position=point["position"],
                        event_id=point["event_id"],
                        department_id=point["department_id"],
                    )
                )
            database.commit()
        logger.info("Successfully seeded database")
        database.commit()
        database.close()
    except Exception as exception:
        logger.error(f"failed to seed main data {exception}")
        database.rollback()
        database.close()
        raise exception
