def test_secret_no_token(client):
    response = client.get("/api/v1/secret")
    assert response.status_code == 401

def test_secret_valid_token(client):
    login_resp = client.post("/api/v1/auth/login", json={"username": "test", "password": "123"})
    token = login_resp.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/api/v1/secret", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["msg"].startswith("Hello")