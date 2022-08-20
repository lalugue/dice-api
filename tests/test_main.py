from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "id" and "dice" and "value" and "links" in response.json()

def test_valid_dice():
    response = client.get("/dice/d2,d4,d6,d8,d12,d20")
    assert response.status_code == 200
