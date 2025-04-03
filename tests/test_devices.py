import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_device_success():
    payload = {
        "device_uid": "abc123",
        "name": "MyTestDevice"
    }
    response = client.post("/api/v1/devices/register", json=payload)
    assert response.status_code == 200  
    data = response.json()
    assert "status" in data
    assert data["status"] == "registered"
    assert "device_uid" in data  
   