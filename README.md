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
1. activate venv via: `source .venv/bin/activate`
2. Run `python3 -m pytest` into project-root. 

This will trigger unit tests and a simple Demo that:
1. Uses test image data from tests/input folder
2. calls in memory endpoint for prediction making
3. print the desired metadata results.

## Start FastAPI app locally
`uvicorn app.main:app`

## Build Docker container
`docker build -t objectdetector`

## Start app via Docker container
docker run: `docker run -v /tmp/output:/tmp/output -p 5000:5000 -e APP_PORT=5000 -e APP_HOST=0.0.0.0 -e OUTPUT_DIR=/tmp/output -d`

OR

docker compose: `docker-compose up --build -d`

## Configuration

### Environment Variables

* <b>APP_PORT</b>: it enables custom port for deployment by overriding it. <i> Default 8000 </i>.
* <b>APP_HOST</b>: it enables custom host for deployment by overriding it. <i> Default 0.0.0.0 </i>.
* <b>OUTPUT_DIR</b>: it enables custom output dir by overriding it. <i> Default /tmp/output</i>.
  Note: it may be required to previously create folder on host filesystem, depending on your OS.

These variables are already configured both in above docker run command and [docker-compose](docker-compose.yml).

### Json Configuration

Default App configuration is located under config/config.json. It would be possibile to change configuration path by overriding env variable `CONFIG_PATH`.

In configuration, it is possibile to change parameter related to:
* confidence: decision threshold on prediction. Predictions which score is less than the threshold are filtered out.
* model: you can choice betweet 3 different models at the moment ("frcnn-resnet", "frcnn-mobilenet", "retinanet")

## Demo
The [demo](demo.sh) script works as the following:

1. Lookups for APP_HOST and APP_PORT variables. If not defined, they assume default values of (0.0.0.0, 5000).
2. start docker service at the specified address (logged in console).
3. Waits 20 seconds for service startup / model downloading (second time can be faster, SO PLEASE ADJUST SLEEP ACCORDINGLY).
4. performs a prediction request for every file comprised in ./tests/input folder.
5. Outputs filename, extracted metadata and time to perform the request.
6. Check $OUTPUT_DIR folder for annotated images.

## Bonus tip: Openapi
Extract OpenApi 3.0 json definition by calling http://$HOST:$PORT/openapi.json

## Bonus tip: Swagger
Access SwaggerUI by calling http://$HOST:$PORT/docs
