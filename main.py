from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exceptions.exception_handler import add_exception_handlers



def create_app() -> FastAPI:
    user_router = create_user_router()
    
    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)

    return app


app = create_app()

