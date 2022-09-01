from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "id" and "dice" and "value" and "links" in response.json()

def test_default_dice():
    response = client.get("/dice/")
    assert response.status_code == 200
    assert "id" and "dice" and "value" and "links" in response.json()

def test_valid_dice():
    response = client.get("/dice/d4,d6,d8,d12,d20")
    assert response.status_code == 200

def test_invalid_dice():
    response = client.get("/dice/d4,d5,d8,d12,d20")
    assert response.status_code == 422

def test_invalid_input():
    response = client.get("/dice/d4,d6,d8-d12,d20")
    assert response.status_code == 422
    response = client.get("/dice/d4,d6,")
    assert response.status_code == 422
    response = client.get("/dice/d4d6d8")
    assert response.status_code == 422 
