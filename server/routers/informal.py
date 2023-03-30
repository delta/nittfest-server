
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
 
from server.controllers.informal import (
    get_informals,
    update_informals,
)
from server.models.errors import GenericError
from server.models.informal import ClusterModel, InformalResponseModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.informal import Informal
from server.controllers.auth import JWTBearer, test_admin

router = APIRouter(prefix="/informals")


@router.get(
    "/",
    dependencies=[Depends(get_database)],
    response_model=list[ClusterModel],
)
async def get_informal(
    database: Session = Depends(get_database),
) -> list[ClusterModel]:
    """
    GET route for events
    """
    try:
        informals = tuple(
            database.query(Informal).order_by(Informal.cluster_id).all()
        )
        cluster = tuple(
            database.query(Cluster).order_by(Cluster.id.asc()).all()
        )
        departments = tuple(database.query(Department).all())

        return get_informals(
            informals=informals,
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
async def update_informal(
    responses: ClusterModel,
    database: Session = Depends(get_database),
    # token: str = Depends(JWTBearer()),
) -> InformalResponseModel:
    """
    POST route for event updation
    """
    try:
        # test_admin(token=token)
        update_informals(informals=responses.informals[0], database=database)
        # update_points(events=responses.events[0], database=database)
        return InformalResponseModel(message="informals Updated Succesfully")
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while updating events:{Exception}",
        ) from Exception
# , Depends(JWTBearer())