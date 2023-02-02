from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette_context.middleware import RawContextMiddleware
from itertools import chain
from app.routers import health
from app.routers import parse
from more_itertools import only
from fastapi import HTTPException
from starlette.responses import JSONResponse
from starlette import status


def create_app():
    """Create and return a FastApi app instance."""

    middleware = [
        Middleware(
            RawContextMiddleware,
        )
    ]
    tags_metadata = chain(
        [
            {
                "name": "Parse",
                "description": "Parses a full name into parts of first name and last name.",
            },
        ],
    )
    app = FastAPI(
        middleware=middleware,
        openapi_tags=list(tags_metadata),
    )

    app.add_middleware(
        CORSMiddleware,
        # Allow any website to contact the API.
        allow_origins=["*"],
        # HTTP method allowed by the REST.
        allow_methods=["GET"],
        # Don't allow the browser to send cookies with the request.
        allow_credentials=False,
    )

    app.include_router(
        health.router,
        prefix="/health",
        tags=["Health"],
    )

    app.include_router(
        parse.router,
        prefix="/api/v1",
        tags=["Parse"],
    )

    app.add_exception_handler(Exception, fallback_handler)
    app.add_exception_handler(HTTPException, fallback_handler)

    return app


async def fallback_handler(*args, **kwargs):
    """Sending a JSON formatted error whenever an HTTP exception is raised."""
    exc = only(  # Checks if the exception is an instance of Exception in a chained instance
        # of args and kwargs. Runs a filter on the chained arguments.
        filter(lambda arg: isinstance(arg, Exception), chain(args, kwargs.values()))
    )
    if exc and isinstance(exc, HTTPException):
        return http_exception_to_json_response(exc=exc)  # Returns the exception as JSON.
    if exc:
        err = HTTPException(detail=str(exc), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return http_exception_to_json_response(exc=err)
    err = HTTPException(detail=f"Error details:\nargs: {args}\nkwargs: {kwargs}",
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return http_exception_to_json_response(exc=err)


def http_exception_to_json_response(exc: HTTPException) -> JSONResponse:
    """Handling body of the HTTP exception to be returned as JSON."""
    body = {
        "error": True,
        "description": exc.detail,
        "status": exc.status_code,
    }

    return JSONResponse(status_code=exc.status_code, content=body)
