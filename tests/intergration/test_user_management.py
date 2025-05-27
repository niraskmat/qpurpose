from app.database import clear_db



def test_register_and_login(client):
    clear_db()
    response = client.post("/register", json={"username": "testuser", "password": "secret"})
    assert response.status_code == 200

    response = client.post("/login", data={"username": "testuser", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()
