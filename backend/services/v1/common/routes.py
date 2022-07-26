from typing import Callable

from fastapi import Request, Response

from fastapi.routing import APIRoute
from services.v1.common.errors.handlers import handle_error_response


class ValidationErrorLoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except Exception as exc:
                return handle_error_response(exc)

        return custom_route_handler
