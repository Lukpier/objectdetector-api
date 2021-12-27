from app.detect_object import ObjectDetector
from app.version import VERSION, APP_NAME
from app.model import ResponseModel
import json
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
import sys
from PIL import Image
from io import BytesIO
import logging
import uvicorn

logger = logging.getLogger(__name__)

config_path = os.environ.get("CONFIG_PATH", "config/config.json")
try:
    with open(config_path, "rb") as f:
        config = json.load(f)
except Exception:
    sys.exit(1)


app = FastAPI()
object_detector = ObjectDetector(config)


@app.get("/", response_class=HTMLResponse)
def hello():
    return f"""
               <b>{APP_NAME}: {VERSION}</b>
            """


@app.post("/api/predict", response_model=ResponseModel)
async def predict(image: UploadFile = File(...)):
    image = read_image(await image.read())
    metadata = object_detector.detect(image)
    return metadata


def read_image(file: bytes) -> Image:
    return Image.open(BytesIO(file))

if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get('APP_PORT', "0.0.0.0"), port=int(os.environ.get('APP_PORT', 8000)))
