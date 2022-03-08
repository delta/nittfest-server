"""
Department Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.models.department import (
    DepartmentModel,
    DepartmentResponseModel,
)
from server.models.errors import GenericError
from server.schemas.department import Department

router = APIRouter(prefix="/department")


@router.get(
    "/",
    response_model=DepartmentResponseModel,
    dependencies=[Depends(get_database)],
)
async def get_departments(
    database: Session = Depends(get_database),
):
    """
    GET route for departments
    """
    try:
        departments = database.query(Department).all()
        response: list[DepartmentModel] = []
        for department in departments:
            response.append(
                DepartmentModel(
                    name=department.name,
                    description=department.description,
                )
            )

        return DepartmentResponseModel(departments=response)
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching departments:{exception}",
        ) from exception
