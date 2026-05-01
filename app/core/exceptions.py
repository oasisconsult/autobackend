from fastapi import Request
from fastapi.responses import JSONResponse
import logging

log = logging.getLogger("autobackend")


async def global_exception_handler(request: Request, exc: Exception):

    log.error(f"Unhandled exception: {exc}", exc_info=True)

    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "message": "Something went wrong. Please retry."
        }
    )
    


class BaseAppException(Exception):
    def __init__(self, message: str):
        self.message = message


class ValidationError(BaseAppException):
    pass


class AIExecutionError(BaseAppException):
    pass


class RuntimeFailure(BaseAppException):
    pass


async def app_exception_handler(request: Request, exc: BaseAppException):
    return JSONResponse(
        status_code=400,
        content={
            "error": exc.__class__.__name__,
            "message": exc.message
        }
    )
    
    