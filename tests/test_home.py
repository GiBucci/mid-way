from fastapi.testclient import TestClient

from mid_way.main import app


def test_home_renders_jinja_layout() -> None:
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "mid-way" in response.text
