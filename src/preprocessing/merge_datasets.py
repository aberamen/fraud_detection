# src/preprocessing/merge_datasets.py

import pandas as pd
import os

def ip_to_int(ip):
    return int(''.join(f'{int(octet):08b}' for octet in ip.split('.')), 2)

def merge_datasets():
    # Load Fraud_Data.csv
    fraud_data_path = os.path.join("data", "processed", "fraud_data_cleaned.csv")
    fraud_df = pd.read_csv(fraud_data_path)
    
    # Convert IP addresses to integers
    fraud_df['ip_address_int'] = fraud_df['ip_address'].apply(ip_to_int)
    
    # Load IpAddress_to_Country.csv
    ip_country_path = os.path.join("data", "raw", "IpAddress_to_Country.csv")
    ip_country_df = pd.read_csv(ip_country_path)
    
    # Merge datasets
    merged_df = pd.merge(fraud_df, ip_country_df, 
                         left_on='ip_address_int', 
                         right_on='lower_bound_ip_address', 
                         how='left')
    
    # Save merged data
    merged_data_path = os.path.join("data", "processed", "fraud_data_merged.csv")
    merged_df.to_csv(merged_data_path, index=False)
    print(f"Merged data saved to {merged_data_path}")

if __name__ == "__main__":
    merge_datasets()