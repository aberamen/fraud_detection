# src/dashboard/app.py

from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load the processed fraud data
fraud_data_path = os.path.join("data", "processed", "fraud_data_with_features.csv")
fraud_df = pd.read_csv(fraud_data_path)

@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Serve summary statistics."""
    total_transactions = len(fraud_df)
    fraud_cases = fraud_df['class'].sum()
    fraud_percentage = (fraud_cases / total_transactions) * 100
    
    return jsonify({
        'total_transactions': total_transactions,
        'fraud_cases': fraud_cases,
        'fraud_percentage': fraud_percentage
    })

@app.route('/api/fraud_over_time', methods=['GET'])
def get_fraud_over_time():
    """Serve fraud cases over time."""
    fraud_over_time = fraud_df.groupby('purchase_time')['class'].sum().reset_index()
    return jsonify(fraud_over_time.to_dict(orient='records'))

@app.route('/api/fraud_by_country', methods=['GET'])
def get_fraud_by_country():
    """Serve fraud cases by country."""
    fraud_by_country = fraud_df.groupby('country')['class'].sum().reset_index()
    return jsonify(fraud_by_country.to_dict(orient='records'))

@app.route('/api/fraud_by_device', methods=['GET'])
def get_fraud_by_device():
    """Serve fraud cases by device."""
    fraud_by_device = fraud_df.groupby('device_id')['class'].sum().reset_index()
    return jsonify(fraud_by_device.to_dict(orient='records'))

@app.route('/api/fraud_by_browser', methods=['GET'])
def get_fraud_by_browser():
    """Serve fraud cases by browser."""
    fraud_by_browser = fraud_df.groupby('browser')['class'].sum().reset_index()
    return jsonify(fraud_by_browser.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)