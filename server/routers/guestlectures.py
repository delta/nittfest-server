from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger

from server.controllers.guestlectures import (
    get_gls,
    update_gls,
)
from server.models.errors import GenericError
from server.models.guestlectures import (
    ClusterModel,
    GuestLectureResponseModel,
)
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.guestlectures import GuestLectures
from server.controllers.auth import JWTBearer, test_admin

router = APIRouter(prefix="/gl")


@router.get(
    "/",
    dependencies=[Depends(get_database)],
    response_model=list[ClusterModel],
)
async def get_gl(
    database: Session = Depends(get_database),
) -> list[ClusterModel]:
    """
    GET route for guestlectures
    """
    try:
        gls = tuple(
            database.query(GuestLectures)
            .order_by(GuestLectures.cluster_id)
            .all()
        )
        cluster = tuple(
            database.query(Cluster).order_by(Cluster.id.asc()).all()
        )
        departments = tuple(database.query(Department).all())

        return get_gls(
            gls=gls,
            clusters=cluster,
            departments=departments,
        )

    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching events:{exception}",
        ) from exception


@router.post(
    "/update",
    dependencies=[Depends(get_database)],
)
async def update_gl(
    responses: ClusterModel,
    database: Session = Depends(get_database),
    # token: str = Depends(JWTBearer()),
) -> GuestLectureResponseModel:
    """
    POST route for event updation
    """
    try:
        # test_admin(token=token)
        update_gls(gls=responses.gls[0], database=database)
        # update_points(events=responses.events[0], database=database)
        return GuestLectureResponseModel(message="gls Updated Succesfully")
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while updating events:{Exception}",
        ) from Exception


# , Depends(JWTBearer())