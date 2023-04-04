"""
Scores Router
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.controllers.scores import get_all_scores, get_leaderboard
from server.models.errors import GenericError
from server.models.scores import ScoreModel, PointsUpdateModel, ScoreLoginModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.leaderboard import Leaderboard
from server.schemas.event import Event
from server.schemas.point import Point
from config.settings import settings

router = APIRouter(prefix="/scores")


@router.get(
    "/",
    dependencies=[Depends(get_database)],
    response_model=list[ScoreModel],
)
async def get_scores(
    database: Session = Depends(get_database),
) -> list[ScoreModel]:
    """
    GET route for scores
    """
    try:
        # clusters = tuple(
        #     database.query(Cluster).order_by(Cluster.id.asc()).all()
        # )
        departments = tuple(database.query(Department).all())
        # points = tuple(
        #     database.query(Point, Event)
        #     .order_by(Point.event_id.asc())
        #     .join(Event, Event.id == Point.event_id)
        #     .all()
        # )
        leaderboard = tuple(database.query(Leaderboard).all())

        scores = get_leaderboard(
            departments=departments, leaderboard=leaderboard
        )
        scores.sort(key=lambda a: a.total_points, reverse=True)
        return scores
    except GenericError as exception:
        logger.error(f"Fetching Events failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching events:{exception}",
        ) from exception

@router.post(
    "/",
    dependencies=[Depends(get_database)],
)
async def post_scores(
    request: PointsUpdateModel,
    database: Session = Depends(get_database),
)-> str:
    """
    POST route for scores
    """
    try:
        if request.jwt == settings.admin_secret:
            dept_id = request.department_id
            point = request.points
            database.query(Leaderboard).filter_by(department_id=dept_id).update(
                dict(point=point)
		    )
            database.commit()
            return "Updated"
        else:
            return "Not logged in"
    except GenericError as exception:
        logger.error(f"Updating scores failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while updating scores:{exception}",
        ) from exception


@router.post(
    "/login",
    dependencies=[Depends(get_database)],
)
async def score_login(
    request: ScoreLoginModel,
    database: Session = Depends(get_database),
)-> str:
    """
    Login route
    """
    try:
        if request.username == settings.admin_username and request.password == settings.admin_password:
            return settings.admin_secret
        else:
            return "Invalid"
    except GenericError as exception:
        logger.error(f"Login failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while logging in:{exception}",
        ) from exception