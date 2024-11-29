from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load Hugging Face's emotion analysis pipeline
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

@app.route('/')
def home():
    return jsonify({"message": "Emotion Analysis API is live!"})

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    try:
        # Get text input from the request
        data = request.json
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided for analysis"}), 400

        # Analyze the emotions in the text
        results = emotion_analyzer(text)

        # Format the response for better readability
        formatted_results = [
            {"emotion": result["label"], "score": round(result["score"], 4)}
            for result in results[0]
        ]

        return jsonify({"text": text, "emotions": formatted_results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
