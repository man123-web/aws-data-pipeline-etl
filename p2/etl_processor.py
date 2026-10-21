import pandas as pd
from datetime import datetime

def extract_data(file_path):
    print(f"[EXTRACT] Reading from {file_path}")
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows")
    return df

def transform_data(df):
    print("[TRANSFORM] Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    df['processed_at'] = datetime.now()
    print(f"Transformed to {len(df)} rows")
    return df

def load_data(df, output_path):
    print(f"[LOAD] Saving to {output_path}")
    df.to_csv(output_path, index=False)
    print("Load completed!")
    return output_path

if __name__ == "__main__":
    input_file = "data/raw_sales_data.csv"
    output_file = "data/processed_sales_data.csv"
    df_raw = extract_data(input_file)
    df_clean = transform_data(df_raw)
    load_data(df_clean, output_file)