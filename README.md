# Pytorch Object Detector - Flask App

Takes an image as input and returns metadata (JSON), extracted from the image

## Development

1. `conda create --name objectdetector --file requirements-dev.txt`
2. activate venv via: `conda activate objectdetector`
3. enjoy!

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
`docker run -e API_PORT=5000 objectdetector`

## Bonus tip: Openapi
Extract OpenApi 3.0 json definition by calling ....

## Notes

- [ ] Startup might be slow for the first time locally and every time for Dockerized version: app code must download the desired model before prediction making.