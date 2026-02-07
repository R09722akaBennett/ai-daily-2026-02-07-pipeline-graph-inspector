from fastapi.testclient import TestClient

from app.main import app


def test_pipeline_ok() -> None:
    c = TestClient(app)
    r = c.post('/api/pipeline/inspect', json={'steps': [{'id': 'a', 'deps': []}, {'id': 'b', 'deps': ['a']}]})
    assert r.status_code == 200
    assert r.json()['ok'] is True
