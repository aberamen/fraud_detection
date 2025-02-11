# src/preprocessing/handle_missing_values.py

import pandas as pd
import os

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    # Impute missing numerical values with the median
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Impute missing categorical values with the mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

if __name__ == "__main__":
    # Load raw data
    raw_data_path = os.path.join("data", "raw", "Fraud_Data.csv")
    df = pd.read_csv(raw_data_path)
    
    # Handle missing values
    df_cleaned = handle_missing_values(df)
    
    # Save processed data
    processed_data_path = os.path.join("data", "processed", "fraud_data_processed.csv")
    df_cleaned.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")