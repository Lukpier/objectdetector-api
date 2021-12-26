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

## Start Flask app locally

## Build Docker container

## Start app via Docker container

## Bonus tip: Openapi
Extract OpenApi 3.0 json definition by calling ....