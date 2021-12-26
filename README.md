# Pytorch Object Detector - FastAPI App

Takes an image as input and returns metadata (JSON), extracted from the image

## Changelog
- <b>1.0.0</b> First release.

## Development

1. `python3 -m venv .venv`
2. activate venv via: `source .venv/bin/activate`
3. `pip install -r requirements-dev.txt`
4. enjoy!

## Tests
Run `python3 -m pytest` into project-root. This will trigger unit tests and a simple Demo that:
1. Uses test image data from tests/input folder
2. calls in memory endpoint for prediction making
3. print the desired metadata results.

## Start FastAPI app locally
`uvicorn app.main:app`

## Build Docker container
`docker build -t objectdetector`

## Start app via Docker container
docker run: `docker run -e APP_PORT=5000 objectdetector`

OR

docker compose: `docker-compose up --build -d`

## Configuration
Default App configuration is located under config/config.json. It would be possibile to change configuration path by overriding env variable `CONFIG_PATH`.

In configuration, it is possibile to change parameter related to:
* confidence: decision threshold on prediction. Predictions which score is less than the threshold are filtered out.
* model: you can choice betweet 3 different models at the moment ("frcnn-resnet", "frcnn-mobilenet", "retinanet")

## Bonus tip: Openapi
Extract OpenApi 3.0 json definition by calling http://localhost:$PORT/openapi.json

## Bonus tip: Swagger
Access SwaggerUI by calling http://localhost:$PORT/docs

## Notes

- [ ] Startup might be slow for the first time locally and every time for Dockerized version: app code must download the desired model before prediction making.
