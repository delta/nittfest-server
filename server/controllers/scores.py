"""
Score Controller
"""
from server.models.scores import ClusterPointModel, ScoreModel
from server.schemas.point import Point


def get_all_scores(
    dept_list: dict,
    cluster_list: dict,
    points: list[Point],
) -> list[ScoreModel]:
    """
    Fucntion to get all scores of all departments
    """
    point_list: dict = {}
    total_list: dict = {}
    score_response: list[ScoreModel] = []

    for point in points:
        cluster_id: str = cluster_list.get(point[1].cluster_id)
        dept_id: str = dept_list.get(point[0].department_id)
        total: int = total_list.get(dept_id, 0)
        total += point[0].point
        total_list.update({dept_id: total})
        res = point_list.get(dept_id, {})
        cluster_points: ClusterPointModel = res.get(
            cluster_id, ClusterPointModel(cluster=cluster_id, points=0)
        )
        cluster_points.points += point[0].point
        res.update({cluster_id: cluster_points})
        point_list.update({dept_id: res})

    for dept, cluster_points in point_list.items():
        score_response.append(
            ScoreModel(
                department=dept,
                total_points=total_list.get(dept, 0),
                cluster_points=list(cluster_points.values()),
            )
        )

    return score_response
