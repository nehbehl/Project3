from fastapi.testclient import TestClient

from foo import app

client = TestClient(app)

def test_get_items():
    r=client.get("/items/1")
    assert r.status_code==200
    assert r.json() == {"fetch":"Fetched 1 of 1"}

def test_path_q():
    r=client.get("/items/2?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch":"Fetched 5 of 2"}
