Esta é uma aplicação que utiliza d Flask para a partir de um texto retornar as emoções expressas no determinado texto.
- Pré-requisitos
Python 3.10 or higher
- Passo a Passo
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



