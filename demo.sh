#!/bin/bash

APP_HOST=${APP_HOST:-0.0.0.0}
APP_PORT=${APP_PORT:-5000}
OUTPUT_DIR=${OUTPUT_DIR:-/tmp/output}

echo "Starting ObjectDetector on http://$APP_HOST:$APP_PORT"
docker container rm objectdetector
docker build -t objectdetector .
docker run -v $OUTPUT_DIR:$OUTPUT_DIR -p$APP_PORT:$APP_PORT -e APP_PORT=$APP_PORT -e APP_HOST=$APP_HOST -e OUTPUT_DIR=$OUTPUT_DIR-d --name objectdetector objectdetector

echo "Waiting for service to be up and running...."
sleep 20
for filename in ./tests/input/*.jpg; do
    echo "Extracting metadata from $filename"
    curl -X POST "http://$APP_HOST:$APP_PORT/api/predict?debug=true" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@$filename;type=image/jpg" -w "\nTime to Connect: %{time_connect}; Time to Transfer: %{time_starttransfer}; Time Total: %{time_total}\n"
done

echo "Shutting down ObjectDetector"
docker stop objectdetector
