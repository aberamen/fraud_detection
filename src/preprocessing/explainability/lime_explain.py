# src/explainability/lime_explain.py

import lime
import lime.lime_tabular
import mlflow
import mlflow.sklearn
import pandas as pd
import os

def explain_with_lime(model_path, X, feature_names):
    """Explain a model using LIME."""
    # Load the model
    model = mlflow.sklearn.load_model(model_path)
    
    # Create a LIME explainer
    explainer = lime.lime_tabular.LimeTabularExplainer(
        X.values,
        feature_names=feature_names,
        class_names=['Not Fraud', 'Fraud'],
        mode='classification'
    )
    
    # Explain the first prediction
    exp = explainer.explain_instance(X.iloc[0], model.predict_proba, num_features=5)
    exp.show_in_notebook()