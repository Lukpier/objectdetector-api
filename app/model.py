from dataclasses import dataclass
from typing import List


@dataclass
class Box:
    startX: float
    startY: float
    endX: float
    endY: float


@dataclass
class Detections:
    labels: List[str]
    scores: List[float]
    boxes: List[Box]


@dataclass
class ResponseModel:
    detections: Detections
