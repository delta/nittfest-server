"""
Models for the payments.
"""

from pydantic import BaseModel
from pydantic.fields import Field


class PaymentRequestModel(BaseModel):
    """
    Request model for payment
    """

    size: str = Field(
        ...,
        title="Size",
        description="Size of the T-Shirt",
    )


class PaymentResponseModel(BaseModel):
    """
    Response model for payment
    """

    url: str = Field(
        ...,
        title="Checkout Session URL",
        description="URL for the payment checkout session",
    )
