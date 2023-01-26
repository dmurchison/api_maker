from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exceptions.exception_handler import add_exception_handlers



def create_app() -> FastAPI:
    profile_infos, users_content = create_profile_infos_and_create_users_content()
    user_router = create_user_router(profile_infos, users_content)
    
    app = FastAPI()
    app.include_router(user_router)

    add_exception_handlers(app)

    return app


def create_profile_infos_and_create_users_content():
    profile_infos = {
        0: {
            "short_bio": "This is a short bio",
            "long_bio": "This is a long bio"
        }
    }

    users_content = {
        0: {
            "liked_posts": [1] * 9,
        }
    }

    return profile_infos, users_content


app = create_app()

