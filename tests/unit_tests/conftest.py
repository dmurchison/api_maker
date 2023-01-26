import pytest
from app.services.user import UserService



@pytest.fixture
def _profile_infos():
    val = {
        0: {
            "short_bio": "This is a short bio",
            "long_bio": "This is a long bio"
        }
    }

    return val


@pytest.fixture
def _users_content():
    val = {
        0: {
            "liked_posts": [1] * 9,
        }
    }

    return val


@pytest.fixture
def user_service(_profile_infos, _users_content):
    user_service = UserService(_profile_infos, _users_content)
    return user_service

