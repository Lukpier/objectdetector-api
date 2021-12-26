from fastapi.testclient import TestClient
from app.main import app
from app.version import VERSION
from os import walk
import pprint
import time

client = TestClient(app)


def test_healtcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert VERSION in response.text
    
def test_predict():
    base_dir = './tests/input'
    images = next(walk(base_dir), (None, None, []))[2]  # [] if no file
    for image in images:
        print('ANALYZING IMAGE: ' + image)
        start = time.time()
        with open(f"{base_dir}/{image}", "rb") as f:
            response = client.post("/api/predict", files={"image": f})
        end = time.time()
        print(f'DONE IN {end - start} milliseconds - Entity:')
        pprint.pprint(response.json())