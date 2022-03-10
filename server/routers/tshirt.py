"""
T-shirt Registration Route
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_database
from config.logger import logger
from server.models.tshirt import TshirtRequestModel
from server.models.errors import GenericError
from server.schemas.tshirt import Tshirt
from server.schemas.users import Users
from server.controllers.auth import JWTBearer, decode_jwt

valid_sizes = ["S", "M", "L", "XL", "XXL"]

router = APIRouter(
    prefix="/register_tshirt",
)


@router.post(
    "/",
    dependencies=[Depends(get_database), Depends(JWTBearer())],
)
async def register_tshirt(
    size_requested: TshirtRequestModel,
    token: str = Depends(JWTBearer()),
    database: Session = Depends(get_database),
) -> None:
    """
    POST route for Tshirt Registration
    """
    try:
        email = decode_jwt(token)["email"]
        user_id = database.query(Users.id).filter_by(email=email).first()
        user_id = 1
        if size_requested.size not in valid_sizes:
            raise GenericError(
                f"Invalid size requested: Size can only be {' '.join(valid_sizes)}"
            )
        # if not user_id:
        #     raise GenericError("User not found")
        tshirt = Tshirt(
            size=size_requested.size,
            user_id=user_id,
        )
        database.add(tshirt)
        database.commit()
        database.close()
        return {"message": "Tshirt registered successfully"}
    except GenericError as exception:
        logger.error("Tshirt registration failed due to {exception}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while registering tshirt",
            headers={"X-Error": str(exception)},
        ) from exception
