# app/predict.py
from pathlib import Path

import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "trained_model.pkl"
VECTORIZER_PATH = MODEL_DIR / "vectorizer.pkl"

# Load once at import time
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_category(text: str) -> str:
    """Takes raw text and returns predicted healthcare category."""
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return str(pred)
