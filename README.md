
# Aplicação Flask para Análise de Emoções em Texto

Esta aplicação usa Flask para analisar as emoções expressas em um texto fornecido.

## Pré-requisitos
- Python 3.10 ou superior

## Passo a Passo

### Passo 1: Navegar até o Diretório do Projeto
Abra o terminal e navegue até o diretório onde seu projeto está localizado:
```bash
cd C:\Path
```

### Passo 2: Criar um Ambiente Virtual
Crie um ambiente virtual para gerenciar as dependências:
```bash
python -m venv venv
```

### Passo 3: Ativar o Ambiente Virtual
Ative o ambiente virtual:
- No Windows, use:
```bash
venv\Scripts\activate
```

### Passo 4: Instalar Dependências
Certifique-se de instalar o Flask e outras dependências necessárias:
```bash
pip install flask
```

### Passo 5: Rodar a Aplicação Flask
Inicie a aplicação Flask executando:
```bash
python app.py
```

### Passo 6: Testar a Aplicação com o Postman
- **Método**: POST
- **URL**: `http://127.0.0.1:5000/analyze`
- **Cabeçalhos**: 
    - `Content-Type: application/json`
- **Corpo (Raw JSON)**:
```json
{
  "text": "Estou me sentindo ótimo hoje!"
}
```

Após enviar a requisição, você receberá uma resposta com a análise emocional do texto fornecido.
