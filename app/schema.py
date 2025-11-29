# app/schema.py
from pydantic import BaseModel

class TextRequest(BaseModel):
    """
    Request body: input healthcare text to classify
    """
    text: str

class PredictionResponse(BaseModel):
    """
    Response body: predicted category
    """
    category: str
