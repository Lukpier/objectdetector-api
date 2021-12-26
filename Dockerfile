FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV API_PORT=5000
ENV CONFIG_PATH=config/config.json

WORKDIR /opt

RUN apt clean && apt update && apt install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

COPY ./app app
COPY ./config config