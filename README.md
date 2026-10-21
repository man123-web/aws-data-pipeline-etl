# aws-data-pipeline-etl
Built an automated ETL data pipeline using AWS S3, Lambda and Python. It ingests raw data from S3, cleans and transforms using Pandas, and loads processed data into S3 for analytics. Includes error handling and logging.
# AWS Data Pipeline - ETL Project
Automated ETL pipeline using AWS S3, Lambda, Python for Data Engineering.

## Architecture
Local CSV -> S3 Bucket (Raw) -> Lambda Trigger -> Python ETL (Clean + Transform) -> S3 Bucket (Processed) -> Visualization

## Tech Stack
AWS S3, AWS Lambda, Python, Pandas, ETL, Data Engineering

## How to Run
1. python etl_processor.py
2. Upload raw file to S3
3. Check processed bucket

## Features
- Automated data ingestion from S3
- Data cleaning and transformation
- Error handling and logging
- Processed data ready for analytics
