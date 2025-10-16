from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User Profile API and CatFActs"}

def test_get_user_profile():
    response = client.get("/me/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "user" in data
    assert "email" in data["user"]
    assert "name" in data["user"]
    assert "stack" in data["user"]
    assert "timestamp" in data
    assert "fact" in data

def test_get_user_profile_failure(monkeypatch):
    async def mock_get_profile_failure():
        raise Exception("Simulated failure")
    
    monkeypatch.setattr("services.user_profile.get_profile", mock_get_profile_failure)
    
    response = client.get("/me/")
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}