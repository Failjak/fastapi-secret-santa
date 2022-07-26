from fastapi import status

from services.v1.common.errors.exceptions import PredefinedError
from services.v1.common.errors.types import ErrorType


class SecretSantaError(PredefinedError):
    GENERIC_ERROR = \
        ("1001", ErrorType.TECHNICAL, status.HTTP_500_INTERNAL_SERVER_ERROR, "Unexpected error")


class PlayerError(PredefinedError):
    GENERIC_ERROR = \
        ("2001", ErrorType.TECHNICAL, status.HTTP_500_INTERNAL_SERVER_ERROR, "Unexpected error")

    INVALID_PLAYER_COUNT = \
        ("2002", ErrorType.BUSINESS, status.HTTP_400_BAD_REQUEST, "Count of users need be more than 2")
