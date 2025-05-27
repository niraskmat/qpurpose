import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def headers(client):
    token = get_auth_token(client)
    return {"Authorization": f"Bearer {token}"}

def get_auth_token(client):
    client.post("/register", json={"username": "taskuser", "password": "secret"})
    response = client.post("/login", data={"username": "taskuser", "password": "secret"})
    return response.json()["access_token"]