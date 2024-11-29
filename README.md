Emotion Analyzer App

This is a Flask-based application that analyzes emotions in text using a Hugging Face model.

## Prerequisites

- Python 3.10 or higher
Primeiro Passo: cd C:\Path
Segundo Passo: python -m venv venv
Terceiro Passo: venv\Scripts\activate
Quarto Passo: python app.py

Quinto Passo: No Postman faça;
New 
HTTP
Set the method to POST.
Set the URL to http://127.0.0.1:5000/analyze.
Add headers:
Content-Type: application/json.
In the body (raw JSON), send the text you want to analyze:
json
{
    "text": "I am feeling great today!"
}



