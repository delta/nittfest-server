"""
Event controller
"""

from functools import lru_cache
from typing import List

from sqlalchemy.orm import Session
from server.models.errors import GenericError
from server.models.informal import ClusterModel, InformalModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.informal import Informal


@lru_cache()
def get_informals(
    informals: tuple[Informal],
    clusters: tuple[Cluster],
    departments: tuple[Department],
) -> list[ClusterModel]:
    """
    Util function to make response
    """
    department_list = {}
    for department in departments:
        department_list.update({department.id: department.name})
    
    informal_list = {}
    for informal in informals:
        value = informal_list.get(informal.cluster_id, [])
        value.append(
            InformalModel(
                name=informal.name,
                rules=informal.rules,
                description=informal.description,
                cluster_id=informal.cluster_id,
                form_link=informal.form_link,
                image_link=informal.image_link,
                start_time=informal.start_time,
                end_time=informal.end_time,
                venue=informal.venue,
                is_reg_completed=informal.is_reg_completed,
                is_informal_completed=informal.is_informal_completed,
                informal_link=informal.informal_link,
            )
        )
        informal_list.update({informal.cluster_id: value})
    response: List[ClusterModel] = []
    for cluster in clusters:
        response.append(
            ClusterModel(
                cluster=cluster.name, informals=informal_list.get(cluster.id, [])
            )
        )
    return response


def update_informals(informals: InformalModel, database: Session):
    """
    Util function to update informals
    """
    informal_data = database.query(Informal).filter_by(name=informals.name).first()
    if not informal_data:
        raise GenericError("Informal Does not exist")

    informal_data.description = informals.description
    informal_data.cluster_id = informals.cluster_id
    informal_data.rules = informals.rules
    informal_data.form_link = informals.form_link
    informal_data.informal_link = informals.informal_link
    informal_data.image_link = informals.image_link
    informal_data.start_time = informals.start_time
    informal_data.end_time = informals.end_time
    informal_data.venue = informals.venue
    informal_data.is_reg_completed = informals.is_reg_completed
    informal_data.is_informal_completed = informals.is_informal_completed
    database.commit()


# def update_points(informals: InformalModel, database: Session):
#     """
#     Util function to update points
#     """
#     informal_data = database.query(Informal).filter_by(name=informals.name).first()
#     point_list = (
#         database.query(Informal).filter_by(event_id=informal_data.id).all()
#     )

#     # if len(informals.points) != len(point_list):
#         # raise GenericError("Number of points does not match")

#     for index, item in enumerate(point_list):
#         # item.point = informals.points[index].point
#         # item.position = informals.points[index].position
#         department_id = (
#             database.query(Department)
#             .filter_by(name=informals.points[index].department)
#             .first()
#             .id
#         )
#         if department_id is None:
#             raise GenericError("Invalid Department")
#         item.department_id = department_id
#     database.commit()
