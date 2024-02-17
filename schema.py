from typing import List
from pydantic import BaseModel


class DataTrain(BaseModel):
    category: str
    price: float
    promotion: int
    discount_perc: int
    channel: str
    purchased: int


class TrainRequestBody(BaseModel):
    save_path: str
    data: List[DataTrain]


class TrainResponse(BaseModel):
    accuracy: float
    status: str


class PredictRequestBody(BaseModel):
    category: str
    price: float
    promotion: int
    discount_perc: int
    channel: str


class PredictResponse(BaseModel):
    result: str
    status: str
