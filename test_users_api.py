import requests

BASE_URL = "http://localhost:5000"  # your backend server

def test_get_users():
    response = requests.get(f"{BASE_URL}/api/users")
    assert response.status_code == 200
    assert "users" in response.json()
