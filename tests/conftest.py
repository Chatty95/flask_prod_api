import pytest
from prod_ready_api import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client
