import boto3
import csv
import io

def hell(event, context):
    # Retrieve bucket and object key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read the CSV file from S3
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket, Key=key)
    csv_data = response['Body'].read().decode('utf-8')

    # Process CSV data
    csv_reader = csv.reader(io.StringIO(csv_data))
    for row in csv_reader:
        # Process each row
        print(row)
        print(hello)
