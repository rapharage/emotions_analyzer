import gradio as gr
from transformers import pipeline

# Inicializar o modelo de análise emocional da Hugging Face
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Função para analisar emoções
def analyze_emotion(text):
    if not text:
        return "Erro: Nenhum texto fornecido."

    # Realizar a análise emocional
    result = emotion_pipeline(text, top_k=None)

    # Criar uma lista formatada com emoções e suas pontuações
    emotions = {r['label']: round(r['score'], 4) for r in result}

    return emotions

# Configuração da interface do Gradio
interface = gr.Interface(
    fn=analyze_emotion,  # Função de análise
    inputs=gr.Textbox(lines=3, placeholder="Digite seu texto aqui..."),  # Entrada: caixa de texto
    outputs=gr.JSON(label="Resultado das Emoções"),  # Saída: formato JSON
    title="Analisador de Emoções",
    description="Digite um texto para analisar as emoções predominantes usando um modelo pré-treinado da Hugging Face."
)

# Lançar a interface com o link compartilhável
if __name__ == "__main__":
    interface.launch(share=True)
