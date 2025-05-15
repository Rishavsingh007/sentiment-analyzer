## Sentiment Analyzer Microservice

 ## A FastAPI-based microservice for sentiment analysis, demonstrating best practices for modern web development.

---

## What is This Project?
A RESTful API built using FastAPI to analyze the sentiment of input text (positive, neutral, or negative) using TextBlob and using Docker for deployment.

---

## Project Structure
sentiment-analyzer/
├── app/
│   ├── main.py           
│   └── analyzer.py       

├── tests/
│   └── test_sentiment.py 

├── .github/workflows/
│   └── ci.yml            

├── Dockerfile            

├── requirements.txt      

├── pytest.ini            

├── .pre-commit-config.yaml 

└── README.md             # Documentation

---

## Features & Best Practices
- **FastAPI** for fast web API development
- **Pydantic** for data validation
- **Docker** for containerization
- **GitHub Actions** for CI/CD
- **Pytest** for testing
- **Pre-commit hooks** for code quality
- **12-Factor App** principles for development

---

## Installation & Setup

1. Clone the repository:
   git clone https://github.com/Rishavsingh007/sentiment-analyzer.git

2. Set up a virtual environment:
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/macOS:
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app locally:
   uvicorn app.main:app --reload

Visit http://127.0.0.1:8000/docs to test the `/analyze` endpoint.

---

## Running Tests

Run tests with:
   pytest

---

## Running with Docker

1. Build the Docker image:
   docker build -t sentiment-api .

2. Run the container:
   docker run -p 8000:8000 sentiment-api

---

## Git Setup & CI/CD

1. Initialize git:
   git init
   git add .
   git commit -m "Initial commit"
   gh repo create sentiment-analyzer --public --source=. --remote=origin --push

2. GitHub Actions will handle CI/CD (tests, linting, Docker build).

---

## Pre-commit Hooks

Install pre-commit:
   pip install pre-commit
   pre-commit install

Run pre-commit on all files:
   pre-commit run --all-files

---

