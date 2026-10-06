import fakeredis
import app as appmod


def client():
    appmod.r = fakeredis.FakeRedis(decode_responses=True)
    return appmod.app.test_client()


def test_health():
    assert client().get("/health").json["status"] == "ok"


def test_add_and_list():
    c = client()
    assert c.post("/api/items", json={"name": "a"}).status_code == 201
    assert c.get("/api/items").json == ["a"]


def test_validation():
    assert client().post("/api/items", json={}).status_code == 400