# Pytorch Object Detector - FastAPI App

```{r, echo=FALSE}
# Define variable containing url
url <- "https://upwork-usw2-prod-file-storage-wp5.s3.us-west-2.amazonaws.com/workplace/attachment/8a316fcb2668bb405427e3eaff27aee3?response-content-disposition=inline%3B%20filename%3D%22Pasted%2520File%2520at%2520December%252027%252C%25202021%25202%253A39%2520PM.png%22%3B%20filename%2A%3Dutf-8%27%27Pasted%2520File%2520at%2520December%252027%252C%25202021%25202%253A39%2520PM.png&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBI4ZmlONKWs4KGkIj887mXk7CD0kM2LDq%2Bs2kf%2BgjdAiBcmMrknXorASjHt%2F%2Ft4vuXyZ8wvyrYrI%2Be4DlM2MwZgyrWBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczOTkzOTE3MzgxOSIMzf4iyXsBqAwjRCZgKqoELbq34OhIxtvtRV8iPv90J7qQcv82o1FRLLx2rpy14O10RXP9%2BlXK5lRtxxf1S1KPhO684Dfb%2Bfa1D3o5q1eTgivlO5SggQVHrZ%2Fsck%2FDGe7cbFyueAZJKO%2FNevsWIMg6P4dPCAYQu1ab1i2WqQGSYV%2BCYZYVuXaDhSCkx%2Bp%2FjDBqKzBswEzodrg0NA4nq3C1forKkEyTglhySIYZ1I6HPz532l6S7pj39nzvq0JtWmshA%2FKQFKq90bV5KctzRiO%2BqsFkOMVrKgOyxB%2FHo4cVWShZJGHvlxbvSDgRM2wNWfAMAG4DJtCFYoLig4%2F702HkssFRiQU%2FN43tS4JVHcZIRgezgITz7ypeAzHBjCBDjQLpDEa8o%2F83pldA93pqFqczVxi22KuwY6pn7oe%2BjyjLAc1Z95UzocOPr5Y6%2FFLqaacbRkYlJNjKkf9JCvlcdrb1PIQSwbgN86Uwi0UkaqkZsR4AVM0BJHlPtpTVt9KGc4OQow%2BP4nlI%2FK6N%2Bdmpfj9LJ7BOdyRawqYEYTtKFTh8F0sTaG4fFm2D2qqjKDMg5tEHEOE8YBcT0hYyRYbdLtatbjP4jPyH9WVGqnAowgRdXheaPBcYSe4FHzgTfXARmyqmv2us22YbtJkOffzjtGq3nPNyhhpLAVikyTkgv%2FYCA3D1a%2BWshJaxgbfqmBdvI9waoKpBt5aPy9KTVPFC%2FEwkMSefslaE%2BmF5POrtpAIYHclni0HjhwMb6FYw7JenjgY6qAExANJxFf21sl%2FKyHxk5tB6lUKKunaSu6gkRZw4BoDkMiOGCQ8SQgGxXVqhwuF9MVn0FYGkdf3oaLb1l93WQMDA0h58V%2FcyDV%2BjCNmOvOUWJ1qUzmtV%2BuYwNsXyc92BcLdLEef3qNiQyCyHJ3Twfdwk24pzztmvFJbIcPIYQgP0vhki6J8mi5EX9VSG2OJ25UqoTxVut4L1dj7piN1U5roNJ12Q9gY0C7k%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211227T162108Z&X-Amz-SignedHeaders=host&X-Amz-Expires=599&X-Amz-Credential=ASIA2YR6PYW52PC4TTNF%2F20211227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=dc8cab074e5ccb7f5fd3c5894cf0c062d3eb78870caccde51e5ae68629564e86"
```
## Some cat!
<center><img src="`r url`"></center>

## Alternatively...
![](`r url`)

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
