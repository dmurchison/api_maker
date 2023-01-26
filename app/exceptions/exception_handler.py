import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.exceptions import UserNotFound



logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFound)
    async def handle_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f'User with id {exc.user_id} not found')
        return JSONResponse(
            status_code=404,
            content={'message': f"User ain't real"}
        )

    return None


