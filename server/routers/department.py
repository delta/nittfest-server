"""
Department Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.logger import logger


from config.database import get_database
from server.models.errors import GenericError
from server.models.department import (
    DepartmentResponseModel,
    DepartmentModel,
)
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
        for i in departments:
            response.append(
                DepartmentModel(name=i.name, description=i.description)
            )

        return DepartmentResponseModel(departments=response)
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching departments:{exception}",
        ) from exception
