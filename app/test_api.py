from fastapi import FastAPI
from starlette.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_user():
    payload = {'email': 'memo@memo.com', 'password': '123'}
    response = client.post('/user/', json=payload)
    assert response.status_code == 200