"""
Models for general exception responses
"""


class GenericError(BaseException):
    """Model for generic error with detail"""

    detail: str
