"""
Payments Route
"""

import stripe

from fastapi import APIRouter, Depends, HTTPException
from server.controllers.auth import JWTBearer, decode_jwt
from server.models.payments import (
    PaymentResponseModel,
    PaymentRequestModel,
)
from config.logger import logger
from config.settings import settings

stripe.api_key = settings.payment_secret

router = APIRouter(
    prefix="/payments",
)

YOUR_DOMAIN = "http://localhost:8000/payment"

price_chart = {"S": 69, "M": 420, "L": 694, "XL": 942}


@router.post(
    "/create_checkout_session",
    response_model=PaymentResponseModel,
    dependencies=[Depends(JWTBearer())],
)
async def create_checkout_session(
    size_requested: PaymentRequestModel,
    token: str = Depends(JWTBearer()),
) -> PaymentResponseModel:
    """
    Handles the payment checkout session
    """
    try:
        decode_jwt(token)
        size = size_requested.size
        if size not in ("XL", "L", "M", "S"):
            raise HTTPException(
                status_code=400,
                detail="Invalid Size",
            )
        price = price_chart[size]
        tshirt_product = stripe.Product.create(name=f"T-shirt {size}")
        tshirt_price = stripe.Price.create(
            product=tshirt_product.id,
            unit_amount=price,
            currency="inr",
        )
        checkout_session = await stripe.checkout.Session.create(
            line_items=[
                {
                    "price": tshirt_price.id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=YOUR_DOMAIN + "/shirt_payment_success",
            cancel_url=YOUR_DOMAIN + "/shirt_payment_fail",
        )
        logger.info(checkout_session.url)
        return PaymentRequestModel(url=checkout_session.url)

    except Exception as exception:
        logger.error(f"Payment failed due to {exception}")
        raise HTTPException(
            status_code=500,
            detail="Payment failed.",
            headers={"X-Error": str(exception)},
        ) from exception
