import gradio as gr
from transformers import pipeline

# Inicializar os dois modelos de análise emocional
emotion_pipeline_roberta = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
emotion_pipeline_xlm_roberta = pipeline("text-classification", model="xlm-roberta-base")

# Mapeamento das labels genéricas para algo mais compreensível
xlm_roberta_label_map = {
    "LABEL_0": "Negativo",
    "LABEL_1": "Positivo"
}

# Função para analisar emoções, dependendo do modelo escolhido
def analyze_emotion(text, use_roberta=False, use_xlm_roberta=False):
    if not text:
        return "Erro: Nenhum texto fornecido."

    if use_roberta and use_xlm_roberta:
        return "Erro: Escolha apenas um modelo."

    # Selecionar o pipeline correto
    if use_xlm_roberta:
        result = emotion_pipeline_xlm_roberta(text, top_k=None)
        # Traduzir as labels usando o mapeamento
        emotions = {xlm_roberta_label_map.get(r['label'], r['label']): round(r['score'], 4) for r in result}
    elif use_roberta:
        result = emotion_pipeline_roberta(text, top_k=None)
        emotions = {r['label']: round(r['score'], 4) for r in result}
    else:
        return "Erro: Nenhum modelo selecionado."

    return emotions

# Configuração da interface do Gradio
interface = gr.Interface(
    fn=analyze_emotion,  # Função de análise
    inputs=[
        gr.Textbox(lines=3, placeholder="Digite seu texto aqui..."),  # Entrada: caixa de texto
        gr.Checkbox(label="Usar DistilRoBERTa", value=False),  # Checkbox para DistilRoBERTa
        gr.Checkbox(label="Usar XLM-RoBERTa", value=False),  # Checkbox para XLM-RoBERTa
    ],
    outputs=gr.JSON(label="Resultado das Emoções"),  # Saída: formato JSON
    title="Analisador de Emoções",
    description="Digite um texto e escolha o modelo para analisar as emoções predominantes. Você pode escolher entre DistilRoBERTa ou XLM-RoBERTa."
)

# Lançar a interface com o link compartilhável
if __name__ == "__main__":
    interface.launch(share=True)
