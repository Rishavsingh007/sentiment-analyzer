from fastapi import FastAPI
from app.models import InputText
from app.analyzer import analyze_sentiment

app = FastAPI()

@app.post("/analyze")
def analyze(input: InputText):
    sentiment = analyze_sentiment(input.text)
    return {"sentiment": sentiment}
