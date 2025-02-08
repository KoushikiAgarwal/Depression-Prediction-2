from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import gensim
import os

# Initialize Flask App
app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)  # Enables frontend-backend communication

# Load trained model
model = tf.keras.models.load_model("model/depression_prediction_model.h5")

# Load Word2Vec model (if used)
w2v_model = gensim.models.Word2Vec.load("model/word2vec_model.bin")

# Function to process user input text
def preprocess_text(text):
    tokens = text.lower().split()  # Tokenization
    vector = np.mean([w2v_model.wv[word] for word in tokens if word in w2v_model.wv] or [np.zeros(100)], axis=0)  # Convert to vector
    return vector.reshape(1, -1)  # Reshape for prediction

@app.route("/")
def home():
    return send_from_directory('frontend', 'index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    vector = preprocess_text(text)
    prediction = model.predict(vector)[0][0]
    result = "Depressed" if prediction > 0.5 else "Not Depressed"

    return jsonify({"text": text, "prediction": result, "confidence": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
