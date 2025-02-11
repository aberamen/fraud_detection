# src/explainability/shap_explain.py

import shap
import mlflow
import mlflow.sklearn
import pandas as pd
import os

def explain_with_shap(model_path, X):
    """Explain a model using SHAP."""
    # Load the model
    model = mlflow.sklearn.load_model(model_path)
    
    # Create a SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    # Summary plot
    shap.summary_plot(shap_values, X, plot_type="bar")
    
    # Force plot for the first prediction
    shap.initjs()
    shap.force_plot(explainer.expected_value[1], shap_values[1][0, :], X.iloc[0, :])
    
    # Dependence plot for the first feature
    shap.dependence_plot(0, shap_values[1], X, interaction_index=None)