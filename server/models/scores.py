"""Score Models"""

from pydantic import BaseModel
from pydantic.fields import Field


class ClusterPointModel(BaseModel):
    """
    Model for cluster scores
    """

    cluster: str = Field(
        ...,
        title="Cluster",
        description="Cluster Name",
    )
    points: int = Field(
        ...,
        title="Points",
        description="Points for the cluster",
    )


class ScoreModel(BaseModel):
    """
    Model for all score details for a single department
    """

    department: str = Field(
        ...,
        title="Department",
        description="Department Name",
    )
    total_points: int = Field(
        ...,
        title="Total Points",
        description="Total points of the department",
    )
    cluster_points: list[ClusterPointModel] = Field(
        [],
        title="Cluster Points",
        description="Points for each cluster",
    )

class PointsUpdateModel(BaseModel):
    """
    Model for all
    """
    department_id: int = Field(
        ...,
        title="Department Id",
        description=""
	)
    points:int = Field(
        ...,
        title="Points",
        description=""
	)
    
    jwt:str = Field(
		...,
        title="JWT",
        description=""
	)
    
class ScoreLoginModel(BaseModel):
    """
    Model for all
    """
    username:str = Field(
        ...,
        title="username",
        description=""
	)
    password:str = Field(
        ...,
        title="password",
        description=""
	)