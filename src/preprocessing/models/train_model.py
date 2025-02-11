# src/models/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import mlflow
import mlflow.sklearn
import os

def load_data(filename):
    """Load a processed dataset from the processed folder."""
    processed_data_path = os.path.join("data", "processed", filename)
    return pd.read_csv(processed_data_path)

def train_fraud_model():
    """Train a model for fraud detection using the fraud dataset."""
    # Load data
    df = load_data("fraud_data_with_features.csv")
    
    # Feature and target separation
    X = df.drop(columns=['class', 'user_id', 'signup_time', 'purchase_time', 'device_id', 'ip_address'])
    y = df['class']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest model
    with mlflow.start_run():
        model = RandomForestClassifier(random_state=42, class_weight='balanced')
        model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Log metrics
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"ROC-AUC Score: {roc_auc}")
        
        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.sklearn.log_model(model, "fraud_model")
        
        # Save the model
        model_path = os.path.join("models", "fraud_model.pkl")
        mlflow.sklearn.save_model(model, model_path)
        print(f"Model saved to {model_path}")

def train_creditcard_model():
    """Train a model for fraud detection using the credit card dataset."""
    # Load data
    df = load_data("creditcard_processed.csv")
    
    # Feature and target separation
    X = df.drop(columns=['Class', 'Time'])
    y = df['Class']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest model
    with mlflow.start_run():
        model = RandomForestClassifier(random_state=42, class_weight='balanced')
        model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Log metrics
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"ROC-AUC Score: {roc_auc}")
        
        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.sklearn.log_model(model, "creditcard_model")
        
        # Save the model
        model_path = os.path.join("models", "creditcard_model.pkl")
        mlflow.sklearn.save_model(model, model_path)
        print(f"Model saved to {model_path}")

if __name__ == "__main__":
    # Train models
    train_fraud_model()
    train_creditcard_model()