# app/main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.schema import TextRequest, PredictionResponse
from app.predict import predict_category

app = FastAPI(
    title="Healthcare Text Classification API",
    description="Classifies healthcare text into medical categories.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: TextRequest):
    """Takes input text and returns predicted healthcare category."""
    category = predict_category(request.text)
    return {"category": category}


# Simple HTML UI for users
@app.get("/", response_class=HTMLResponse)
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Healthcare Text Classification</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background:#f7f7f7; }
            .container { max-width: 700px; margin: auto; background: white; padding: 24px;
                         border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            textarea { width: 100%; height: 140px; padding: 10px; font-size: 14px; }
            button { margin-top: 12px; padding: 10px 18px; font-size: 14px;
                     border: none; border-radius: 6px; background: #2563eb; color: white;
                     cursor: pointer; }
            button:hover { background: #1d4ed8; }
            .result { margin-top: 18px; font-weight: bold; font-size: 16px; }
            .label { font-weight: bold; margin-bottom: 6px; display:block; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Healthcare Text Classification</h2>
            <p>Enter a clinical note / complaint and get the predicted medical category.</p>
            <label class="label" for="text">Input Text</label>
            <textarea id="text" placeholder="e.g. Patient reports chest pain and shortness of breath."></textarea>
            <br/>
            <button onclick="sendRequest()">Predict Category</button>
            <div id="result" class="result"></div>
        </div>

        <script>
            async function sendRequest() {
                const text = document.getElementById('text').value;
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = "Predicting...";
                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({ text: text })
                    });
                    const data = await response.json();
                    if (data.category) {
                        resultDiv.innerHTML = "Predicted Category: " + data.category;
                    } else {
                        resultDiv.innerHTML = "Error: " + JSON.stringify(data);
                    }
                } catch (err) {
                    resultDiv.innerHTML = "Request failed: " + err;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
