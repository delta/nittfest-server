"""
Score Controller
"""
from functools import lru_cache

from server.models.scores import ClusterPointModel, ScoreModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department


@lru_cache()
def get_all_scores(
    clusters: tuple[Cluster], departments: tuple[Department], points: tuple
) -> list[ScoreModel]:
    """
    Function to get all scores of all departments
    """
    dept_list: dict = {}
    cluster_point_list: dict = {}

    for dept in departments:
        cluster_point_list1: dict = {}
        for cluster in clusters:
            cluster_point_list1.update(
                {
                    cluster.id: ClusterPointModel(
                        cluster=cluster.name, points=0
                    )
                }
            )
        dept_list.update({dept.id: cluster_point_list1})

    total_list: dict = {}
    score_response: list[ScoreModel] = []

    for point in points:
        cluster_id: int = point[1].cluster_id
        total: int = total_list.get(point[0].department_id, 0)
        total += point[0].point
        total_list.update({point[0].department_id: total})
        cluster_points = dept_list.get(point[0].department_id)

        if cluster_points is not None:
            points_of_cluster: ClusterPointModel = cluster_points.get(
                cluster_id
            )
            points_of_cluster.points += point[0].point
            cluster_points.update({cluster_id: points_of_cluster})
            dept_list.update({point[0].department_id: cluster_points})

    for dept in departments:
        score_response.append(
            ScoreModel(
                department=dept.name,
                total_points=total_list.get(dept.id, 0),
                cluster_points=list(
                    dept_list.get(dept.id, cluster_point_list).values()
                ),
            )
        )

    return score_response
