import pytest
from app.schemas.user import FullUserProfile



@pytest.fixture(scope="session")
def valid_user_id() -> int:
    return 0


@pytest.fixture(scope="session")
def invalid_user_id() -> int:
    return 1


@pytest.fixture(scope="session")
def sample_full_user_profile() -> dict:
    return FullUserProfile(
                short_bio="This is a short bio",
                long_bio="This is a long bio",
                username="username",
                liked_posts=[1, 2, 3],
            )

