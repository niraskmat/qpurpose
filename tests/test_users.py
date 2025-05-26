from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


def test_register_and_login():
    response = client.post("/register", json={"username": "testuser", "password": "secret"})
    assert response.status_code == 200

    response = client.post("/login", data={"username": "testuser", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()

if __name__ == "__main__":
    test_register_and_login()