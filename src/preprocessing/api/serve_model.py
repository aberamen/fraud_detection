# src/api/serve_model.py

from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='../logs/api.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

# Load the fraud detection model
fraud_model_path = "../models/fraud_model.pkl"
fraud_model = mlflow.sklearn.load_model(fraud_model_path)

# Load the credit card fraud detection model
creditcard_model_path = "../models/creditcard_model.pkl"
creditcard_model = mlflow.sklearn.load_model(creditcard_model_path)

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    """Predict fraud for e-commerce transactions."""
    try:
        # Get input data
        data = request.get_json()
        input_data = pd.DataFrame(data)
        
        # Make prediction
        prediction = fraud_model.predict(input_data)
        prediction_proba = fraud_model.predict_proba(input_data)[:, 1]
        
        # Log the request and prediction
        logging.info(f"Input Data: {input_data.to_dict()}")
        logging.info(f"Prediction: {prediction.tolist()}")
        
        # Return the result
        return jsonify({
            'prediction': prediction.tolist(),
            'prediction_proba': prediction_proba.tolist()
        })
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict_creditcard_fraud', methods=['POST'])
def predict_creditcard_fraud():
    """Predict fraud for credit card transactions."""
    try:
        # Get input data
        data = request.get_json()
        input_data = pd.DataFrame(data)
        
        # Make prediction
        prediction = creditcard_model.predict(input_data)
        prediction_proba = creditcard_model.predict_proba(input_data)[:, 1]
        
        # Log the request and prediction
        logging.info(f"Input Data: {input_data.to_dict()}")
        logging.info(f"Prediction: {prediction.tolist()}")
        
        # Return the result
        return jsonify({
            'prediction': prediction.tolist(),
            'prediction_proba': prediction_proba.tolist()
        })
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)