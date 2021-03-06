from torchvision.models import detection
import numpy as np
import torch
import numpy
from PIL import Image
import cv2
import logging
from app.model import ResponseModel, Box, Detections
import time
import os

MODELS = {
    "frcnn-resnet": detection.fasterrcnn_resnet50_fpn,
    "frcnn-mobilenet": detection.fasterrcnn_mobilenet_v3_large_320_fpn,
    "retinanet": detection.retinanet_resnet50_fpn,
}
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/tmp/output")

class ObjectDetector:
    def __init__(self, config: dict):
        start = time.time()
        logger.info("Starting object detector using Config={}", config)
        self._classes = config["coco_classes"]
        self._model = MODELS[config["model"]](
            pretrained=True, progress=True, num_classes=91, pretrained_backbone=True
        ).to(DEVICE)
        self._colors = np.random.uniform(0, 255, size=(len(self._classes), 3))
        self._model.eval()

        self._confidence = config["confidence"]

        end = time.time()
        logger.info("Object detector started in {} ms", end - start)

    def detect(self, filename: str, image: Image, debug: bool) -> ResponseModel:
        image = ObjectDetector.to_opencv(image)
        orig = image.copy()
        image = ObjectDetector.preprocess(image)
        # send the input to the device and pass the it through the network to
        # get the detections and predictions
        image = image.to(DEVICE)
        detections = self._model(image)[0]

        return self.mk_output(filename, orig, detections, debug)

    def mk_output(self, filename: str, orig: np.ndarray, detections: dict, debug: bool) -> ResponseModel:
        labels = []
        scores = []
        boxes = []
        # loop over the detections
        for i in range(0, len(detections["boxes"])):
            # extract the confidence (i.e., probability) associated with the
            # prediction
            score = detections["scores"][i]
            # filter out weak detections by ensuring the confidence is
            # greater than the minimum confidence
            if score > self._confidence:
                # extract the index of the class label from the detections,
                # then compute the (x, y)-coordinates of the bounding box
                # for the object
                idx = int(detections["labels"][i])
                arr_box = detections["boxes"][i].detach().cpu().numpy()
                (startX, startY, endX, endY) = arr_box.astype("int")
                box = Box(startX=startX, startY=startY, endX=endX, endY=endY)
                label = self._classes[idx]
                
                if debug:
                    self.enrich_image_and_save(filename, orig, idx, label, score, startX, startY, endX, endY)
                
                score = float(score.detach().cpu().numpy().take(0))
                logger.info(
                    f"Detected entity: {self._classes[idx]}: {str(score * 100)}"
                )
                

                labels.append(label)
                boxes.append(box)
                scores.append(score)

        return ResponseModel(
            detections=Detections(labels=labels, scores=scores, boxes=boxes)
        )

    @staticmethod
    def preprocess(image: np.ndarray) -> torch.FloatTensor:
        # convert the image from BGR to RGB channel ordering and change the
        # image from channels last to channels first ordering
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = image.transpose((2, 0, 1))
        # add the batch dimension, scale the raw pixel intensities to the
        # range [0, 1], and convert the image to a floating point tensor
        image = np.expand_dims(image, axis=0)
        image = image / 255.0
        return torch.FloatTensor(image)

    @staticmethod
    def to_opencv(image: Image) -> np.ndarray:
        return cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    
    def enrich_image_and_save(self, 
                              filename: str, 
                              orig: np.ndarray, 
                              idx: int, 
                              label: str, 
                              score: torch.FloatTensor,
                              startX: int,
                              startY: int,
                              endX: int,
                              endY: int
                              ) -> None:
        
        logger.info("Saving annotated image {} to {}", filename, OUTPUT_DIR)
        
        if not os.path.isdir(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

         # save formatted image to output folder            
        label_formatted = "{}: {:.2f}%".format(label, score * 100)
        cv2.rectangle(orig, (startX, startY), (endX, endY),
            self._colors[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(orig, label_formatted, (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, self._colors[idx], 2)
        cv2.imwrite(f"{OUTPUT_DIR}/{filename}", orig)
