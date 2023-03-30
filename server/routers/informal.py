
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
 
from server.controllers.informal import (
    get_informals,
    update_informals,
)
from server.models.errors import GenericError
from server.models.informal import ClusterModel, InformalResponseModel, InformalRegisterRequestModel
from server.schemas.cluster import Cluster
from server.schemas.department import Department
from server.schemas.informal import Informal
from server.schemas.informals_registration import InformalsRegistration
from server.controllers.auth import JWTBearer, decode_jwt, test_admin
from server.schemas.users import Users

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

@router.post("/register", 
    dependencies=[Depends(get_database)],
)
async def register_informal(
    request: InformalRegisterRequestModel,
    session: Session = Depends(get_database),
    token: str = Depends(JWTBearer()),
) -> InformalResponseModel:
    """
	Register Informal
    """
    try:
        user_email = decode_jwt(token)["user_email"]
        user = session.query(Users).filter_by(email=user_email).first()
        if not user:
            raise GenericError("User not found")

        informal = session.query(Informal).filter_by(name=request.informal_name).first()
        if not informal:
            raise GenericError("Informals not found")

        if (
                session.query(InformalsRegistration).filter_by(
                    user_id=user.id, informal_id=informal.id
                ).count() > 0
        ):
            raise GenericError("Informal already registered")
        else:
            new_informal_registration = InformalsRegistration(
                user_id=user.id, informal_id=informal.id
            )
            session.add(new_informal_registration)
            session.commit()
            return InformalResponseModel(message="Informal Registered Succesfully")

    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while registering Informal:{Exception}",
        ) from Exception
