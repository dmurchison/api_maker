import pytest
from app.main import create_app
from fastapi.testclient import TestClient



@pytest.fixture(scope="session")
def testing_app():
    app = create_app()
    testing_app = TestClient(app)
    return testing_app






