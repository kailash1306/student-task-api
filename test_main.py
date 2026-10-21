
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Student Task Manager API is running!"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_add_task():
    response = client.post(
        "/tasks",
        json={"title": "Prepare lab record", "completed": False},
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Prepare lab record"


def test_missing_task():
    response = client.patch("/tasks/99999")
    assert response.status_code == 404
