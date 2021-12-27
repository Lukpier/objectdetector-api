FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV APP_PORT=5000
ENV CONFIG_PATH=config/config.json
ENV UVICORN_PORT=$APP_PORT

WORKDIR /opt

RUN apt clean && apt update && apt install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

COPY ./app app
COPY ./config config
EXPOSE ${APP_PORT}

RUN mkdir -p .cache/torch/hub/checkpoints
RUN wget https://download.pytorch.org/models/retinanet_resnet50_fpn_coco-eeacb38b.pth -O .cache/torch/hub/checkpoints/retinanet_resnet50_fpn_coco-eeacb38b.pth
RUN wget https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth  -O .cache/torch/hub/checkpoints/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth
RUN wget https://download.pytorch.org/models/fasterrcnn_mobilenet_v3_large_320_fpn-907ea3f9.pth  -O .cache/torch/hub/checkpoints/fasterrcnn_mobilenet_v3_large_320_fpn-907ea3f9.pth

ENV TORCH_HOME=/opt/.cache/torch

CMD ["python3", "-m", "app"]