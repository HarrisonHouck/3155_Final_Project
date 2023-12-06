from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    response = client.post(
        "/orders/",
        json={
            "customer_name": "John Doe",
            "pizzas": [1, 2]
        }
    )
    assert response.status_code == 200
    assert response.json()["customer_name"] == "John Doe"
    assert response.json()["pizzas"][0]["id"] == 1
    assert response.json()["pizzas"][1]["id"] == 2
