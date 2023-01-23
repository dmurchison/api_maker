from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import Optional, Tuple

app = FastAPI()


class ProfileInfo(BaseModel):
    short_bio: str
    long_bio: str

class User(BaseModel):
    username: str
    profile_info: ProfileInfo
    liked_posts: Optional[list[int]] = None

@app.get('/', response_class=PlainTextResponse)
def home():
    return "Hello World, This is the home page"


def get_user_info() -> User:
    profile_info = {
        "short_bio": "This is a short bio",
        "long_bio": "This is a long bio"
    }
    profile_info = ProfileInfo(**profile_info)

    user_content = {
        "username": "testuser",
        "liked_posts": [8],
        "profile_info": profile_info
    }


    return User(**user_content)


@app.get('/user/me', response_model=User)
def test_endpoint():
    
    user = get_user_info()

    return user





