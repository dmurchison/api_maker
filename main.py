from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field
from typing import Optional, Tuple, List, Dict, Any, Union

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
def home():
    return "Hello World, This is the home page"


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The Username",
        description="This is the username of the user",
        min_length=1,
        default=None
    )
    liked_posts: List[int] = Field(
        alias="liked_posts",
    )


class FullUserProfile(User):
    short_bio: str
    long_bio: str


class CreateUserResponse(BaseModel):
    user_id: int


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

def create_user(full_profile_info: FullUserProfile) -> CreateUserResponse:
    global profile_infos
    global users_content

    new_user_id = len(users_content)
    users_content[new_user_id] = full_profile_info.dict()
    profile_infos[new_user_id] = {
        "short_bio": full_profile_info.short_bio,
        "long_bio": full_profile_info.long_bio
    }
    return CreateUserResponse(user_id=new_user_id)

def get_user_info(user_id: int = 0) -> FullUserProfile:
    global profile_infos
    global users_content

    new_user_id = len(users_content)
    liked_posts = full_user_profile.liked_posts
    short_bio = full_profile.short_bio
    long_bio = profile_infos.long_bio


@app.get('/user/{user_id}', response_model=FullUserProfile)
def get_user_by_id(user_id: int):
    full_user_profile = get_user_info(user_id)
    return full_user_profile


@app.post('/users')
def add_user(full_profile_info: FullUserProfile):
    create_user(full_profile_info)





