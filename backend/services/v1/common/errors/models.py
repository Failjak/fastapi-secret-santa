from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel
from pydantic.types import UUID4

from services.v1.common.errors.types import ErrorType


class ErrorMessage(BaseModel):
    """ Error message """

    uuid: UUID4
    error_datetime: datetime
    type: ErrorType
    code: str
    status: int
    message: str
    details: dict
    cause: Optional[Any]
