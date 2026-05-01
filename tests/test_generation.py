from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generation_endpoint():
    response = client.post(
        "/generation/",
        json={"prompt": "Build a CRM API"},
        headers={"Authorization": "Bearer test-token"}
    )

    assert response.status_code in [200, 401]