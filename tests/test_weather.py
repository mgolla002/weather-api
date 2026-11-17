from weather.main import app

def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200

def test_known_city():
    r = app.test_client().get("/weather/dallas")
    assert r.status_code == 200
    assert r.get_json()["condition"] == "Sunny"

def test_unknown_city():
    r = app.test_client().get("/weather/atlantis")
    assert r.status_code == 404