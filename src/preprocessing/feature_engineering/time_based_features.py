# src/feature_engineering/time_based_features.py

import pandas as pd
import os

def add_time_based_features(df):
    """Add time-based features to the dataset."""
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    return df

if __name__ == "__main__":
    # Load merged data
    merged_data_path = os.path.join("data", "processed", "fraud_data_merged.csv")
    df = pd.read_csv(merged_data_path)
    
    # Add time-based features
    df = add_time_based_features(df)
    
    # Save data with new features
    feature_data_path = os.path.join("data", "processed", "fraud_data_with_features.csv")
    df.to_csv(feature_data_path, index=False)
    print(f"Data with features saved to {feature_data_path}")