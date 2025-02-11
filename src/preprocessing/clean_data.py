# src/preprocessing/clean_data.py

import pandas as pd
import os

def clean_data(df):
    """Clean the dataset."""
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Correct data types
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    
    return df

if __name__ == "__main__":
    # Load processed data
    processed_data_path = os.path.join("data", "processed", "fraud_data_processed.csv")
    df = pd.read_csv(processed_data_path)
    
    # Clean data
    df_cleaned = clean_data(df)
    
    # Save cleaned data
    cleaned_data_path = os.path.join("data", "processed", "fraud_data_cleaned.csv")
    df_cleaned.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data saved to {cleaned_data_path}")