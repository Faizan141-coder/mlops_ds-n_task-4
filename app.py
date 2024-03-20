from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from request
    features = request.json['features']

    # Convert features to numpy array
    features = np.array(features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Return prediction as JSON
    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
