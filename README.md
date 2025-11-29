# 🩺 Healthcare Text Classification – FastAPI NLP Project

This project is an end-to-end **NLP text classification system** for healthcare domain.  
It takes a **clinical / healthcare text input** (e.g., symptoms, notes, findings) and predicts the most relevant **medical specialty** (e.g., Cardiology, Neurology, Orthopedics, Gastroenterology, etc.).

Model is trained using **TF-IDF + Logistic Regression (Scikit-learn)** and exposed via a **FastAPI** backend with a simple HTML UI.

---

## 📂 Project Structure

```bash
Healthcare-Text-Classification
│
├── data/
│   └── healthcare_text_dataset.csv    # Labeled dataset (text, category)
│
├── models/
│   ├── model.pkl                      # Trained ML model (Logistic Regression)
│   └── vectorizer.pkl                 # Fitted TF-IDF vectorizer
│
├── app/
│   ├── main.py                        # FastAPI app + HTML UI + API endpoints
│   └── schema.py                      # Pydantic models for request/response
│
├── train.py                           # Script to load data, train model & save artefacts
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation

🧠 Problem Statement

Healthcare organisations receive unstructured text:

doctor notes,

call-center logs,

patient complaints,

medical reports, etc.

Manually reading and routing this text to the right medical department is slow and error-prone.
This project automatically classifies text into medical specialties to speed up triage and analysis.

🛠 Tech Stack

Language: Python 3.x

NLP & ML:

pandas, numpy

scikit-learn (TF-IDF, Logistic Regression)

API Framework:

FastAPI

uvicorn (ASGI server)

Validation:

pydantic

Frontend:

Simple HTML form (Jinja2 / plain templates)

📊 Dataset

The dataset is stored in:

data/healthcare.csv


Expected columns:

text      -> the input medical text (symptoms, notes, etc.)
category  -> the target label / medical specialty


Example rows:

text	category
Patient reports chest pain and shortness of breath.	Cardiology
MRI scan suggests possible brain tumor in frontal lobe.	Neurology
Blood sugar levels very high, recommend insulin adjustment.	Endocrinology
Severe knee pain after sports injury, swelling noticed.	Orthopedics

You can extend this CSV with more rows to improve performance.

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Healthcare-Text-Classification.git
cd Healthcare-Text-Classification

2️⃣ Create & activate virtual environment (optional but recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train the model

This will:

load data/healthcare_text_dataset.csv

preprocess text

train TF-IDF + Logistic Regression model

save trained_model.pkl and vectorizer.pkl into models/ folder

python train.py


After successful training you should see:

models/trained_model.pkl
models/vectorizer.pkl

5️⃣ Run the FastAPI server
uvicorn app.main:app --reload


Server will be available at:

Swagger docs: http://127.0.0.1:8000/docs

ReDoc docs: http://127.0.0.1:8000/redoc

HTML UI (if added): e.g. http://127.0.0.1:8000/
 or /form



🌐 API Endpoints
✅ Health Check

GET /health

Response:

{
  "status": "ok"
}

✅ Predict Category (API)

POST /predict

Request body:

{
  "text": "Patient reports chest pain and shortness of breath."
}


Response:

{
  "category": "Cardiology"
}

✅ HTML Form (optional UI)

If main.py includes a simple form route (for example /form):

Go to: http://127.0.0.1:8000/form

Type or paste medical text

Click Predict

The predicted medical category will be shown on the page.

🧪 Model Details

Vectorizer: TfidfVectorizer

max_features (e.g. 5000)

ngram_range=(1, 2) to capture unigrams & bigrams

Classifier: LogisticRegression

Works well with high-dimensional sparse text features (TF-IDF)

Good baseline for multi-class classification

Evaluation Metrics (from train.py):

accuracy_score

classification_report (precision, recall, F1-score)

🧾 Example train.py Flow (High-Level)

Load CSV from data/healthcare_text_dataset.csv

Clean text (lowercase, remove special chars, etc.)

Split into train/test sets

Fit TF-IDF on training text

Train Logistic Regression on transformed features

Evaluate on test set

Save model & vectorizer into models/ directory


