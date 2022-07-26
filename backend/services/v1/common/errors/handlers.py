import datetime
from uuid import uuid4

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status

from services.v1.common.errors.exceptions import PredefinedError
from services.v1.common.errors.models import ErrorMessage
from services.v1.common.errors.types import ErrorType


def get_error_message(error: Exception):
    error_message = error

    if isinstance(error, PredefinedError):
        error_message = ErrorMessage(
            uuid=uuid4(),
            error_datetime=datetime.datetime.now(),
            type=error.error_type,
            code=error.error_code,
            status=error.http_status_code,
            message=error.message,
            details=error.details,
            cause=error.cause,
        )
    elif isinstance(error, RequestValidationError):
        current_error = error.errors()[-1]
        error_message = ErrorMessage(
            uuid=uuid4(),
            error_datetime=datetime.datetime.now(),
            type=ErrorType.VALIDATION,
            code=status.HTTP_400_BAD_REQUEST,
            status=status.HTTP_400_BAD_REQUEST,
            message=current_error.get('msg'),
            details={
                'body': error.body,
            },
            cause=current_error.get('ctx'),
        )

    # TODO handling others errors

    return error_message


def handle_error_response(exception: Exception):
    exc_message = get_error_message(exception)
    return JSONResponse(exc_message.json(), status_code=exc_message.status)
