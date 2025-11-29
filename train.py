# train.py
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# --------- Paths ---------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "healthcare.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

# --------- Load data ---------
df = pd.read_csv(DATA_PATH)

# Expecting columns: text, category
X = df["text"].astype(str)
y = df["category"].astype(str)

# --------- Split ---------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --------- Vectorizer ---------
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# --------- Model ---------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# --------- Evaluation ---------
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# --------- Save model & vectorizer ---------
joblib.dump(model, MODEL_DIR / "trained_model.pkl")
joblib.dump(vectorizer, MODEL_DIR / "vectorizer.pkl")

print("✅ Model and vectorizer saved in 'model/' folder.")
