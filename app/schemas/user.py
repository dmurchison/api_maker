from typing import List
from pydantic import BaseModel, Field



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


class MultipleUsersResponse(BaseModel):
    users: List[User]
    total: int


class CreateUserResponse(BaseModel):
    users: List[FullUserProfile]
    total: int

