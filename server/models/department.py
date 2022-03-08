"""
Department Model
"""

from pydantic import BaseModel
from pydantic.fields import Field


class DepartmentModel(BaseModel):
    """
    model for department
    """

    name: str = Field(
        ..., title="name", description="name of the department"
    )

    description: str = Field(
        ...,
        title="description",
        description="description of the department",
    )


class DepartmentResponseModel(BaseModel):
    """
    Response model for department
    """

    departments: list[DepartmentModel] = Field(
        ..., title="departments", description="List of all departments"
    )
