"""
Dashboard route
"""

from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.controllers.auth import JWTBearer, decode_jwt
from server.controllers.dashboard import (
    get_points,
    get_position,
    get_upcoming_events,
)
from server.models.dashboard import DashboardResponseModel
from server.models.errors import GenericError
from server.schemas.department import Department
from server.schemas.event import Event
from server.schemas.point import Point
from server.schemas.users import Users

router = APIRouter(
    prefix="/dashboard",
)


@router.get(
    "/",
    response_model=DashboardResponseModel,
    dependencies=[Depends(get_database)],
)
async def get_dashboard(
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> DashboardResponseModel:
    """
    GET route for Dashboard
    """
    try:
        user_email = decode_jwt(token)["user_email"]
        user = database.query(Users).filter_by(email=user_email).first()
        if not user:
            raise GenericError("User not found")

        department = (
            database.query(Department)
            .filter_by(id=user.department_id)
            .first()
        )
        if not department:
            raise GenericError("Department not found for the current user")

        points = (
            database.query(Point.department_id, func.sum(Point.point))
            .group_by(Point.department_id)
            .all()
        )
        print(points)
        events = tuple(database.query(Event).all())

        return DashboardResponseModel(
            department=department.name,
            point=get_points(points=points, department=department.id),
            upcoming_events=get_upcoming_events(events=events),
            position=get_position(points=points, department=department.id),
        )

    except GenericError as exception:
        logger.error(f"<Dashboard retrieval failed due to {exception}>")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while retrieving dashboard details ",
            headers={
                "X-Error": "An unexpected error occurred while retrieving dashboard"
            },
        ) from exception
