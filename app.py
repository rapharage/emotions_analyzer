from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Initialize the Hugging Face sentiment analysis pipeline
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Define the route to analyze emotions
@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    data = request.get_json()  # Get JSON data from the request
    text = data.get('text', '')  # Get the 'text' field from the JSON

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Perform the emotion analysis using the Hugging Face model
    result = emotion_pipeline(text, top_k=None)

    # Create a dictionary of emotions and their scores
    emotions = [{'emotion': r['label'], 'score': r['score']} for r in result]

    # Return the analysis result
    return jsonify({'text': text, 'emotions': emotions})

# Run the app and bind it to the correct port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or fallback to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
