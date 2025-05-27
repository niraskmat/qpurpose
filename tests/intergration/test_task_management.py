import pytest


def test_task_actions(client, headers):

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

def test_create_task_bad_date_format(client, headers):
    response = client.post("/tasks", json={"title": "Bad Date", "start_date": "02.03.2025"}, headers=headers)
    assert response.status_code == 422
    error_detail = response.json()
    print(error_detail)
    assert any("start_date" in err["msg"] for err in error_detail["detail"])