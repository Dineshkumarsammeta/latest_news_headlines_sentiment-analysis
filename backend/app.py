from flask import Flask, request, jsonify
from datetime import datetime
import traceback
import random

# (Optional) import your existing sentiment logic
# from src.analyze import analyze_sentiment

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Flask API is running for News Sentiment Analysis."
    }), 200


# Predict endpoint — mock or integrate real model
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "Text input is required"}), 400

        # For demo, we randomly simulate sentiment
        # Replace this with your actual sentiment function:
        # result = analyze_sentiment(text)
        sentiment = random.choice(["positive", "negative", "neutral"])

        response = {
            "input_text": text,
            "predicted_sentiment": sentiment,
            "confidence_score": round(random.uniform(0.6, 0.99), 2),
            "timestamp": datetime.utcnow().isoformat()
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
