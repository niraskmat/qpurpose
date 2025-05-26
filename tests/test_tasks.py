from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


def get_auth_token():
    client.post("/register", json={"username": "taskuser", "password": "secret"})
    response = client.post("/login", data={"username": "taskuser", "password": "secret"})
    return response.json()["access_token"]

def test_task_actions():

    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Create
    response = client.post("/tasks", json={"title": "Test Task"}, headers=headers)
    assert response.status_code == 200
    task_id = response.json()["id"]

    # Read
    response = client.get("/tasks", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1

    # Update - overwrite
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

    # Update - edit
    response = client.patch(f"/tasks/{task_id}", json={"description": "This is the new description"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["description"] == "This is the new description"

    # Delete
    response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 200


if __name__ == "__main__":
    test_task_actions()
