from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@patch("app.routes.scans.publish_message") 
def test_create_scan_session(mock_publish):
    payload = {
        "device_id": 1,
        "scanned_at": "2025-04-01T12:00:00Z"
    }
    response = client.post("/api/v1/scans", json=payload)
    assert response.status_code == 200
    data = response.json()
    mock_publish.assert_called_once()  
    mock_publish.assert_called_with("New ScanSession created with id=123")