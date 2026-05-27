import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket_name = 'my-demo-bucket-12345'

response = s3.create_bucket(
    Bucket=bucket_name
)

print(f"Bucket created: {bucket_name}")
