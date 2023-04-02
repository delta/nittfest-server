"""
Event controller
"""

from functools import lru_cache
from typing import List

from sqlalchemy.orm import Session
from server.models.errors import GenericError
from server.models.guestlectures import ClusterModel, GuestLectureModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.guestlectures import GuestLectures


@lru_cache()
def get_gls(
    gls: tuple[GuestLectures],
    clusters: tuple[Cluster],
    departments: tuple[Department],
) -> list[ClusterModel]:
    """
    Util function to make response
    """
    department_list = {}
    for department in departments:
        department_list.update({department.id: department.name})
    
    gl_list = {}
    for gl in gls:
        value = gl_list.get(gl.cluster_id, [])
        value.append(
            GuestLectureModel(
                name=gl.name,
                rules=gl.rules,
                description=gl.description,
                cluster_id=gl.cluster_id,
                form_link=gl.form_link,
                image_link=gl.image_link,
                start_time=gl.start_time,
                end_time=gl.end_time,
                venue=gl.venue,
                is_reg_completed=gl.is_reg_completed,
                is_gl_completed=gl.is_gl_completed,
                gl_link=gl.gl_link,
            )
        )
        gl_list.update({gl.cluster_id: value})
    response: List[ClusterModel] = []
    for cluster in clusters:
        response.append(
            ClusterModel(
                cluster=cluster.name, gls=gl_list.get(cluster.id, [])
            )
        )
    return response


def update_gls(gls: GuestLectureModel, database: Session):
    """
    Util function to update informals
    """
    gl_data = database.query(GuestLectures).filter_by(name=gls.name).first()
    if not gl_data:
        raise GenericError("Informal Does not exist")

    gl_data.description = gls.description
    gl_data.cluster_id = gls.cluster_id
    gl_data.rules = gls.rules
    gl_data.form_link = gls.form_link
    gl_data.gl_link = gls.gl_link
    gl_data.image_link = gls.image_link
    gl_data.start_time = gls.start_time
    gl_data.end_time = gls.end_time
    gl_data.venue = gls.venue
    gl_data.is_reg_completed = gls.is_reg_completed
    gl_data.is_gl_completed = gls.is_gl_completed
    database.commit()


# def update_points(informals: InformalModel, database: Session):
#     """
#     Util function to update points
#     """
#     gl_data = database.query(Informal).filter_by(name=informals.name).first()
#     point_list = (
#         database.query(Informal).filter_by(event_id=gl_data.id).all()
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
