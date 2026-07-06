from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source-code')))
from main import app

client = TestClient(app)

def test_get_tasks_healthy():
    response = client.get("/tasks")
    assert response.status_code == 500
    assert response.json()["status"] == "healthy"
