from fastapi.testclient import TestClient
from app.main import app
from app.version import VERSION

client = TestClient(app)


def test_healtcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert VERSION in response.text
    
def test_predict():
    with open('./tests/input/000000005802.jpg', "rb") as f:
        response = client.post("/predict", files={"image": f})
    assert response.status_code == 200
