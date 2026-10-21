import json
import boto3
import pandas as pd
from datetime import datetime

s3 = boto3.client('s3')

def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    df['processed_at'] = datetime.now()
    return df

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"New file: {key} in {bucket}")
    
    download_path = f"/tmp/{key.split('/')[-1]}"
    s3.download_file(bucket, key, download_path)
    
    df = pd.read_csv(download_path)
    df_clean = transform_data(df)
    
    processed_bucket = "processed-data-bucket"
    processed_key = f"processed/{key}"
    df_clean.to_csv(download_path, index=False)
    s3.upload_file(download_path, processed_bucket, processed_key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('ETL Completed Successfully!')
    }