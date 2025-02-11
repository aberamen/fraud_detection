# src/models/evaluate_model.py

import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
import mlflow
import mlflow.sklearn
import os

def evaluate_model(model_path, X_test, y_test):
    """Evaluate a trained model."""
    # Load the model
    model = mlflow.sklearn.load_model(model_path)
    
    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    print(f"ROC-AUC Score: {roc_auc}")